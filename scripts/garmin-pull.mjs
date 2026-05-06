#!/usr/bin/env node
// Garmin Connect data scraper via CDP (Chrome remote debugging)
//
// USAGE:
//   node scripts/garmin-pull.mjs                    # pull missing days up to today
//   node scripts/garmin-pull.mjs --from 2026-04-01  # pull from specific date
//   node scripts/garmin-pull.mjs --from 2026-04-01 --to 2026-04-30
//   node scripts/garmin-pull.mjs --force            # re-pull existing days
//   node scripts/garmin-pull.mjs --week             # last 7 days only
//
// PREREQUISITE:
//   Chrome started with --remote-debugging-port=9222 + zalogowany do Garmin Connect.
//   Aliasing helper:
//     alias chrome-debug='killall "Google Chrome" 2>/dev/null; sleep 2; open -na "Google Chrome" --args --remote-debugging-port=9222'
//
// OUTPUT:
//   data/garmin_year/{YYYY-MM-DD}.json  — full daily wellness payload

import { chromium } from 'playwright';
import fs from 'fs/promises';
import path from 'path';
import { existsSync } from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PROJECT_ROOT = path.resolve(__dirname, '..');
const OUT_DIR = path.join(PROJECT_ROOT, 'data', 'garmin_year');
const USER = 'przebi';
const CDP_URL = 'http://localhost:9222';

// ---------- CLI args ----------
const args = process.argv.slice(2);
const getArg = (name, def) => {
  const i = args.indexOf(`--${name}`);
  if (i >= 0 && args[i + 1] && !args[i + 1].startsWith('--')) return args[i + 1];
  if (i >= 0) return true;
  return def;
};

const force = !!getArg('force');
const weekMode = !!getArg('week');
const today = new Date().toISOString().slice(0, 10);
let fromDate = getArg('from', null);
let toDate = getArg('to', today);

await fs.mkdir(OUT_DIR, { recursive: true });

if (weekMode) {
  const d = new Date(today);
  d.setDate(d.getDate() - 7);
  fromDate = d.toISOString().slice(0, 10);
}

if (!fromDate) {
  // Default: find last fetched day, start day after
  const files = (await fs.readdir(OUT_DIR)).filter(f => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).sort();
  if (files.length > 0) {
    const last = files[files.length - 1].replace('.json', '');
    const d = new Date(last);
    d.setDate(d.getDate() + 1);
    fromDate = d.toISOString().slice(0, 10);
  } else {
    // No history — default to last 30 days
    const d = new Date(today);
    d.setDate(d.getDate() - 30);
    fromDate = d.toISOString().slice(0, 10);
  }
}

if (fromDate > toDate) {
  console.log(`✓ Up to date (last: ${fromDate}, today: ${toDate})`);
  process.exit(0);
}

// Generate date range
const dates = [];
for (let d = new Date(fromDate); d <= new Date(toDate); d.setDate(d.getDate() + 1)) {
  dates.push(d.toISOString().slice(0, 10));
}

console.log(`[i] Pulling ${dates.length} days: ${fromDate} → ${toDate}${force ? ' (force re-pull)' : ''}`);

// ---------- Connect via CDP ----------
let browser;
try {
  browser = await chromium.connectOverCDP(CDP_URL);
} catch (e) {
  console.error(`✗ Cannot connect to Chrome at ${CDP_URL}`);
  console.error('  Start Chrome with: open -na "Google Chrome" --args --remote-debugging-port=9222');
  console.error('  Then login to connect.garmin.com');
  process.exit(1);
}

const ctx = browser.contexts()[0];
let page = ctx.pages().find(p => p.url().includes('connect.garmin.com'));
if (!page) {
  console.log('[i] No Garmin tab open, navigating...');
  page = await ctx.newPage();
  await page.goto('https://connect.garmin.com/modern/dashboard', { waitUntil: 'domcontentloaded', timeout: 20000 });
  await page.waitForTimeout(5000);
}

// ---------- Get CSRF token ----------
console.log('[i] Capturing CSRF token...');
let csrfToken = null;
const handler = (req) => {
  if (req.url().includes('/gc-api/') && req.headers()['connect-csrf-token']) {
    csrfToken = req.headers()['connect-csrf-token'];
  }
};
page.on('request', handler);
// Trigger some API calls if not on /modern
if (!page.url().includes('/modern/')) {
  await page.goto('https://connect.garmin.com/modern/dashboard', { waitUntil: 'domcontentloaded', timeout: 15000 });
}
await page.waitForTimeout(5000);
page.off('request', handler);

if (!csrfToken) {
  // Force trigger by reloading
  console.log('[i] CSRF not found, reloading...');
  page.on('request', handler);
  await page.reload({ waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(8000);
  page.off('request', handler);
}

if (!csrfToken) {
  console.error('✗ Could not capture CSRF token. Are you logged in to Garmin Connect?');
  await browser.close();
  process.exit(1);
}
console.log(`[i] CSRF: ${csrfToken.slice(0, 8)}...`);

// ---------- Endpoints ----------
const endpoints = {
  sleep: (d) => `/gc-api/sleep-service/sleep/dailySleepData?date=${d}&nonSleepBufferMinutes=60`,
  sleep_stats: (d) => {
    const past = new Date(d); past.setDate(past.getDate() - 6);
    return `/gc-api/sleep-service/stats/sleep/daily/${past.toISOString().slice(0,10)}/${d}`;
  },
  heart_rate: (d) => `/gc-api/wellness-service/wellness/dailyHeartRate?date=${d}`,
  stress: (d) => `/gc-api/wellness-service/wellness/dailyStress/${d}`,
  body_battery_events: (d) => `/gc-api/wellness-service/wellness/bodyBattery/events/${d}`,
  daily_summary: (d) => `/gc-api/usersummary-service/usersummary/daily/${USER}?calendarDate=${d}`,
  daily_events: (d) => `/gc-api/wellness-service/wellness/dailyEvents/${USER}?calendarDate=${d}`,
  hrv: (d) => `/gc-api/hrv-service/hrv/${d}`,
  training_readiness: (d) => `/gc-api/metrics-service/metrics/trainingreadiness/${d}`,
  vo2max: (d) => `/gc-api/metrics-service/metrics/maxmet/latest/${d}`,
  spo2: (d) => `/gc-api/wellness-service/wellness/dailySpo2/${d}`,
};

const fetchOne = async (url) => {
  return await page.evaluate(async ({url, csrf}) => {
    try {
      const r = await fetch(url, {
        method: 'GET',
        credentials: 'include',
        headers: {
          'Accept': 'application/json',
          'connect-csrf-token': csrf,
          'NK': 'NT',
          'X-app-ver': '5.24.1.3a',
          'X-lang': 'pl-PL',
        },
      });
      const txt = await r.text();
      let json = null;
      try { json = JSON.parse(txt); } catch {}
      return { status: r.status, body: json !== null ? json : (txt.length < 100 ? txt : null) };
    } catch (e) {
      return { error: e.message };
    }
  }, {url, csrf: csrfToken});
};

// ---------- Pull ----------
let success = 0, skipped = 0, errors = 0;
for (const date of dates) {
  const outFile = path.join(OUT_DIR, `${date}.json`);
  if (!force && existsSync(outFile)) { skipped++; continue; }

  const data = { date };
  let dayErrors = 0;
  for (const [name, fn] of Object.entries(endpoints)) {
    const r = await fetchOne(fn(date));
    if (r.status === 200) {
      data[name] = r.body;
    } else {
      data[name] = null;
      dayErrors++;
    }
    await new Promise(r => setTimeout(r, 80));
  }

  await fs.writeFile(outFile, JSON.stringify(data, null, 2));
  success++;
  if (dayErrors >= Object.keys(endpoints).length) errors++;

  if (success % 10 === 0 || success === dates.length - skipped) {
    console.log(`  [${success}/${dates.length - skipped}] ${date}${dayErrors ? ` (${dayErrors} endpoints failed)` : ''}`);
  }
}

console.log(`\n✓ Done. Saved: ${success}, skipped: ${skipped}, full-error days: ${errors}`);
console.log(`  Output: ${OUT_DIR}/`);

await browser.close();
