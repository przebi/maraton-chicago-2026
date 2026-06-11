// Guarded dashboard kudos sweep (Tryb A) — sesja 2026-06-10.
// FIX vs ślepe klikanie: elementFromPoint guard PRZED dispatchMouseEvent
// (klik tylko gdy ikona kudos jest pod kursorem i w widoku) + Escape na popup
// + skip-marker (data-kudos-skip) zapobiega pętli + MAX_CLICKS cap + live-log.
// Wymaga: Chrome --remote-debugging-port=9223 (profil /tmp/chrome-strava, zalogowany)
//         + chrome-remote-interface w /tmp/node_modules.
import CDP from '/tmp/node_modules/chrome-remote-interface/index.js';
import fs from 'fs';
const LOG = '/tmp/kudos2_progress.log';
fs.writeFileSync(LOG, '');
const log = m => { const l = `[${new Date().toISOString().substr(11,8)}] ${m}`; console.log(l); try { fs.appendFileSync(LOG, l + '\n'); } catch {} };
const PENDING = ['Give kudos', 'Przyznaj kudos'];
const P = JSON.stringify(PENDING);
const MAX_CLICKS = 220;

const tabs = await CDP.List({ port: 9223 });
const tab = tabs.find(t => t.type === 'page' && t.url.includes('strava'));
if (!tab) { log('NO STRAVA TAB'); process.exit(1); }
const client = await CDP({ target: tab.webSocketDebuggerUrl });
const { Runtime, Page, Input, Network } = client;
await Runtime.enable(); await Page.enable(); await Network.enable();
await Page.addScriptToEvaluateOnNewDocument({ source: `Object.defineProperty(navigator,'webdriver',{get:()=>undefined});` });
let ok = 0, block = 0, skipped = 0; const ids = new Set(); const recent = [];
Network.on('responseReceived', e => {
  const u = e.response.url;
  if (u.includes('/feed/activity/') && u.endsWith('/kudo')) {
    const id = u.match(/\/activity\/(\d+)\/kudo/)?.[1]; const s = e.response.status;
    if (s === 200) { ok++; recent.push('ok'); if (id) ids.add(id); }
    else if (s === 403 || s === 429) { block++; recent.push('block'); }
    else recent.push('other');
    if (recent.length > 12) recent.shift();
  }
});
const evalJS = async e => (await Runtime.evaluate({ expression: e, returnByValue: true, awaitPromise: true })).result.value;
const sleep = ms => new Promise(r => setTimeout(r, ms));
const esc = async () => {
  await Input.dispatchKeyEvent({ type: 'rawKeyDown', windowsVirtualKeyCode: 27, key: 'Escape' });
  await Input.dispatchKeyEvent({ type: 'keyUp', windowsVirtualKeyCode: 27, key: 'Escape' });
};

await Page.navigate({ url: 'https://www.strava.com/dashboard?num_entries=200' });
await sleep(3500);
await esc(); await sleep(300);
log('start guarded sweep');
const start = Date.now();
let clicks = 0, dry = 0, stop = false;

while (!stop && clicks < MAX_CLICKS) {
  const picked = await evalJS(`(() => {
    document.querySelectorAll('[data-kudos-target]').forEach(e=>e.removeAttribute('data-kudos-target'));
    const b = Array.from(document.querySelectorAll('button[data-testid="kudos_button"]:not([data-kudos-skip])')).filter(x=>${P}.includes(x.title))[0];
    if(!b) return false;
    b.setAttribute('data-kudos-target','1');
    b.scrollIntoView({block:'center',behavior:'instant'});
    return true;
  })()`);
  if (!picked) {
    await evalJS(`window.scrollTo(0, document.body.scrollHeight)`);
    await sleep(1300);
    const more = await evalJS(`!!Array.from(document.querySelectorAll('button[data-testid="kudos_button"]:not([data-kudos-skip])')).filter(x=>${P}.includes(x.title))[0]`);
    if (!more) { if (++dry >= 3) { log('feed wyczyszczony (3 dry rundy)'); break; } continue; }
    dry = 0; continue;
  }
  dry = 0;
  await sleep(450);
  const hit = await evalJS(`(() => {
    const b = document.querySelector('[data-kudos-target]');
    if(!b) return {gone:true};
    if(!${P}.includes(b.title)) return {done:true};
    const r = b.getBoundingClientRect();
    const cx = Math.round(r.left+r.width/2), cy = Math.round(r.top+r.height/2);
    const el = document.elementFromPoint(cx,cy);
    const underBtn = !!(el && (el===b || b.contains(el) || (el.closest && el.closest('button[data-testid="kudos_button"]')===b)));
    return {x:cx, y:cy, underBtn, inView: cy>60 && cy<(innerHeight-20)};
  })()`);
  if (hit.gone) continue;
  if (hit.done) { await evalJS(`document.querySelector('[data-kudos-target]')?.removeAttribute('data-kudos-target')`); continue; }
  if (!hit.underBtn || !hit.inView) {
    await esc(); await sleep(250);
    await evalJS(`{const b=document.querySelector('[data-kudos-target]'); if(b){b.setAttribute('data-kudos-skip','1'); b.removeAttribute('data-kudos-target');}}`);
    skipped++; log(`SKIP mis-target (underBtn=${hit.underBtn} inView=${hit.inView}) | ok=${ok} skip=${skipped}`);
    continue;
  }
  await Input.dispatchMouseEvent({ type: 'mouseMoved', x: hit.x, y: hit.y });
  await sleep(40);
  await Input.dispatchMouseEvent({ type: 'mousePressed', x: hit.x, y: hit.y, button: 'left', clickCount: 1 });
  await sleep(70);
  await Input.dispatchMouseEvent({ type: 'mouseReleased', x: hit.x, y: hit.y, button: 'left', clickCount: 1 });
  clicks++;
  await sleep(500);
  const after = await evalJS(`(() => { const b=document.querySelector('[data-kudos-target]'); if(!b) return {gone:true}; const pend=${P}.includes(b.title); if(pend) b.setAttribute('data-kudos-skip','1'); b.removeAttribute('data-kudos-target'); return {stillPending:pend}; })()`);
  if (after.stillPending) { await esc(); await sleep(200); skipped++; log(`click nie zaliczyl — skip | ok=${ok} skip=${skipped}`); }
  else { log(`KUDOS | ok=${ok} block=${block} unique=${ids.size}`); }
  if (recent.length >= 6) {
    const br = recent.filter(x => x === 'block').length / recent.length;
    if (br > 0.3) { log(`block rate ${(br * 100) | 0}% — STOP (rate limit)`); stop = true; }
  }
  await sleep(300);
}
log(`=== DONE === ${((Date.now() - start) / 1000).toFixed(0)}s | clicks ${clicks} | ok=${ok} block=${block} skip=${skipped} | unique ${ids.size}`);
await client.close();
process.exit(0);
