// TRYB A: Dashboard kudos quick run
// Scroll dashboard, click pending kudo buttons via real CDP mouse events.
// ~5 min, daje ~30-150 kudosów z aktualnego feedu (last ~7 dni).
import CDP from '/tmp/node_modules/chrome-remote-interface/index.js';

const PORT = 9223;
const MAX_DURATION_MS = 360_000; // 6 min cap
const CLICK_THROTTLE_MS = 250;
const PENDING = ['Give kudos', 'Przyznaj kudos'];

const tabs = await CDP.List({ port: PORT });
const tab = tabs.find(t => t.type === 'page' && t.url.includes('strava'));
if (!tab) { console.log('No strava tab — open Chrome on :9223 first'); process.exit(1); }
const client = await CDP({ target: tab.webSocketDebuggerUrl });
const { Runtime, Page, Input, Network } = client;
await Runtime.enable(); await Page.enable(); await Network.enable();

await Page.addScriptToEvaluateOnNewDocument({ source: `Object.defineProperty(navigator,'webdriver',{get:()=>undefined});` });
await Runtime.evaluate({ expression: `Object.defineProperty(navigator,'webdriver',{get:()=>undefined});` });

let posts = 0, ok = 0, err = 0;
const kudoIds = new Set();
Network.on('requestWillBeSent', e => {
  if (e.request.url.includes('/feed/activity/') && e.request.url.endsWith('/kudo') && e.request.method === 'POST') posts++;
});
Network.on('responseReceived', e => {
  if (e.response.url.includes('/feed/activity/') && e.response.url.endsWith('/kudo')) {
    const id = e.response.url.match(/\/activity\/(\d+)\/kudo/)?.[1];
    if (e.response.status >= 200 && e.response.status < 300) { ok++; if (id) kudoIds.add(id); }
    else err++;
  }
});

const evalJS = async (e) => (await Runtime.evaluate({ expression: e, returnByValue: true, awaitPromise: true })).result.value;

await Page.navigate({ url: 'https://www.strava.com/dashboard?num_entries=200' });
await Page.loadEventFired();
await new Promise(r => setTimeout(r, 3000));

const start = Date.now();
let totalClicks = 0;
let stuckCount = 0;

while (Date.now() - start < MAX_DURATION_MS && stuckCount < 5) {
  // JS click (faster + works after Strava layout change 02.06.2026)
  const clickedRound = await evalJS(`
    (() => {
      const PENDING = ${JSON.stringify(PENDING)};
      const all = Array.from(document.querySelectorAll('button[data-testid="kudos_button"]'))
        .filter(b => PENDING.includes(b.title))
        .filter(b => { const r = b.getBoundingClientRect(); return r.top > 30 && r.top < window.innerHeight - 30; });
      let count = 0;
      for (const b of all) { b.scrollIntoView({block:'center', behavior:'instant'}); b.click(); count++; }
      return count;
    })()
  `);
  totalClicks += clickedRound;
  // throttle after the batch
  if (clickedRound > 0) await new Promise(r => setTimeout(r, CLICK_THROTTLE_MS * clickedRound));

  const beforeY = await evalJS(`window.scrollY`);
  const beforeH = await evalJS(`document.documentElement.scrollHeight`);
  await evalJS(`window.scrollBy(0, window.innerHeight * 0.7)`);
  await new Promise(r => setTimeout(r, 1500));
  const afterY = await evalJS(`window.scrollY`);
  const afterH = await evalJS(`document.documentElement.scrollHeight`);

  const elapsed = ((Date.now()-start)/1000).toFixed(0);
  const domBtns = await evalJS(`document.querySelectorAll('button[data-testid="kudos_button"]').length`);
  console.log(`[${elapsed}s] +${clickedRound} (cum ${totalClicks}) | scroll ${afterY}/${afterH} | DOM total btns ${domBtns} | POSTs ${posts} ok=${ok} err=${err} | unique IDs ${kudoIds.size}`);

  if (afterY === beforeY && afterH === beforeH && clickedRound === 0) {
    await evalJS(`window.scrollTo(0, document.documentElement.scrollHeight)`);
    await new Promise(r => setTimeout(r, 2500));
    const newH = await evalJS(`document.documentElement.scrollHeight`);
    if (newH <= afterH + 50) {
      stuckCount++;
      console.log(`  bottom reached, stuck count ${stuckCount}`);
    } else stuckCount = 0;
  } else stuckCount = 0;
}

console.log('\n=== FINAL v4 ===');
console.log(`Time: ${((Date.now()-start)/1000).toFixed(0)} s`);
console.log(`DOM clicks: ${totalClicks}`);
console.log(`POSTs sent to /kudo: ${posts} | 2xx: ${ok} | errors: ${err}`);
console.log(`Unique activity IDs kudosed: ${kudoIds.size}`);

const final = await evalJS(`
  (() => {
    const all = Array.from(document.querySelectorAll('button[data-testid="kudos_button"]'));
    return { total: all.length, pending: all.filter(b => ${JSON.stringify(PENDING)}.includes(b.title)).length };
  })()
`);
console.log('DOM final:', final);
await client.close();
