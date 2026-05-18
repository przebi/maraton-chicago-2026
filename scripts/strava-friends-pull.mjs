// Pulls Tomasz's full friends list (122 athletes) via paginated /follows page
// Saves to /tmp/strava_friends.json
import CDP from '/tmp/node_modules/chrome-remote-interface/index.js';

const MY_ATHLETE_ID = 24659157;
const tabs = await CDP.List({ port: 9223 });
const tab = tabs.find(t => t.type === 'page' && t.url.includes('strava'));
if (!tab) { console.log('No strava tab — open Chrome on :9223 first'); process.exit(1); }
const client = await CDP({ target: tab.webSocketDebuggerUrl });
const { Runtime, Page } = client;
await Runtime.enable(); await Page.enable();
const evalJS = async (e) => (await Runtime.evaluate({ expression: e, returnByValue: true, awaitPromise: true })).result.value;

const all = new Map();
for (let page = 1; page <= 20; page++) {
  await Page.navigate({ url: `https://www.strava.com/athletes/${MY_ATHLETE_ID}/follows?page=${page}` });
  await new Promise(r => setTimeout(r, 2000));
  const list = await evalJS(`
    Array.from(document.querySelectorAll('a[href^="/athletes/"]'))
      .map(a => { const m = a.getAttribute('href').match(/^\\/athletes\\/(\\d+)$/); if (!m) return null; const id = m[1]; if (id === '${MY_ATHLETE_ID}') return null; return [id, a.textContent?.trim().replace(/\\s+/g,' ').substr(0,60)]; })
      .filter(Boolean)
  `);
  if (!list?.length) break;
  let newCount = 0;
  for (const [id, name] of list) if (!all.has(id)) { all.set(id, name); newCount++; }
  console.log(`Page ${page}: ${list.length} cards (${newCount} new, total ${all.size})`);
  if (!newCount && page > 1) break;
  await new Promise(r => setTimeout(r, 500));
}

import fs from 'fs';
fs.writeFileSync('/tmp/strava_friends.json', JSON.stringify([...all.entries()], null, 2));
console.log(`\nSaved ${all.size} friends to /tmp/strava_friends.json`);
await client.close();
