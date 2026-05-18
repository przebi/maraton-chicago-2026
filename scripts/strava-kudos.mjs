import CDP from '/tmp/node_modules/chrome-remote-interface/index.js';
import fs from 'fs';

const friends = JSON.parse(fs.readFileSync('/tmp/strava_friends.json', 'utf8'));
const START_IDX = 17; // continue from Pepe Nicola

const tabs = await CDP.List({ port: 9223 });
const tab = tabs.find(t => t.type === 'page' && t.url.includes('strava'));
const client = await CDP({ target: tab.webSocketDebuggerUrl });
const { Runtime, Page, Input, Network } = client;
await Runtime.enable(); await Page.enable(); await Network.enable();
await Page.addScriptToEvaluateOnNewDocument({ source: `Object.defineProperty(navigator,'webdriver',{get:()=>undefined});` });

const PENDING = ['Give kudos', 'Przyznaj kudos'];
const WEEKS = ['202618', '202619', '202620', '202621'];
const PAUSE_MS = 3 * 60_000; // 3 min
const CLICK_THROTTLE_MS = 2000; // 2s between clicks (slower than v7b's 1s)

const recentResults = [];
let totalOk = 0, totalBlock = 0;
const kudoIds = new Set();
Network.on('responseReceived', e => {
  if (e.response.url.includes('/feed/activity/') && e.response.url.endsWith('/kudo')) {
    const id = e.response.url.match(/\/activity\/(\d+)\/kudo/)?.[1];
    if (e.response.status === 200) { totalOk++; recentResults.push('ok'); if (id) kudoIds.add(id); }
    else if (e.response.status === 403 || e.response.status === 429) { totalBlock++; recentResults.push('block'); }
    else { recentResults.push('other'); }
    if (recentResults.length > 10) recentResults.shift();
  }
});

const evalJS = async (e) => (await Runtime.evaluate({ expression: e, returnByValue: true, awaitPromise: true })).result.value;

console.log(`v7d: 3 min pre-pause to let Strava cool down...`);
await new Promise(r => setTimeout(r, PAUSE_MS));

console.log(`Starting from athlete index ${START_IDX} (${friends[START_IDX]?.[1]})`);

const startTime = Date.now();
let pauseCount = 0;

for (let i = START_IDX; i < friends.length; i++) {
  const [aid, name] = friends[i];
  
  // Smart pause: trigger if last 10 POSTs have > 30% blocks (tighter than v7c's 50%)
  if (recentResults.length >= 5) {
    const blockRate = recentResults.filter(r => r === 'block').length / recentResults.length;
    if (blockRate > 0.3) {
      pauseCount++;
      console.log(`⚠️  Block rate ${(blockRate*100).toFixed(0)}% in last ${recentResults.length} — pause #${pauseCount} 3min`);
      if (pauseCount >= 3) {
        console.log('STOPPING — 3 pauses, blocked again. Wait for user.');
        break;
      }
      await new Promise(r => setTimeout(r, PAUSE_MS));
      recentResults.length = 0;
    }
  }
  
  try {
    await Page.navigate({ url: `https://www.strava.com/athletes/${aid}` });
    await new Promise(r => setTimeout(r, 2500));
    
    const h1 = await evalJS(`document.querySelector('h1')?.textContent?.substr(0,80) || ''`);
    if (h1.includes('czerwone') || h1.includes('red light')) {
      pauseCount++;
      console.log(`⚠️  "czerwone światło" at ${i+1} — pause #${pauseCount} 3min`);
      if (pauseCount >= 3) { console.log('STOPPING — 3 pauses'); break; }
      await new Promise(r => setTimeout(r, PAUSE_MS));
      i--; continue;
    }
    
    let athClicks = 0;
    for (const week of WEEKS) {
      await evalJS(`location.hash = '#interval?interval=${week}&interval_type=week&chart_type=miles&year_offset=0'`);
      await new Promise(r => setTimeout(r, 1500));
      await evalJS(`(() => { const el = document.querySelector('#interval'); if (el) el.scrollIntoView({block:'start',behavior:'instant'}); else window.scrollTo(0, document.body.scrollHeight * 0.6); })()`);
      await new Promise(r => setTimeout(r, 800));
      
      let safety = 30;
      while (safety-- > 0) {
        const next = await evalJS(`
          (() => {
            const PENDING = ${JSON.stringify(PENDING)};
            const btns = Array.from(document.querySelectorAll('button[data-testid="kudos_button"]')).filter(b => PENDING.includes(b.title));
            if (!btns.length) return null;
            const b = btns[0];
            b.scrollIntoView({block:'center', behavior:'instant'});
            const r = b.getBoundingClientRect();
            return { x: Math.round(r.left + r.width/2), y: Math.round(r.top + r.height/2) };
          })()
        `);
        if (!next) break;
        await new Promise(r => setTimeout(r, 300));
        await Input.dispatchMouseEvent({ type: 'mouseMoved', x: next.x, y: next.y });
        await new Promise(r => setTimeout(r, 50));
        await Input.dispatchMouseEvent({ type: 'mousePressed', x: next.x, y: next.y, button: 'left', clickCount: 1 });
        await new Promise(r => setTimeout(r, 80));
        await Input.dispatchMouseEvent({ type: 'mouseReleased', x: next.x, y: next.y, button: 'left', clickCount: 1 });
        athClicks++;
        await new Promise(r => setTimeout(r, CLICK_THROTTLE_MS));
      }
    }
    
    const elapsed = ((Date.now()-startTime)/1000).toFixed(0);
    console.log(`[${elapsed}s] ${i+1}/${friends.length} ${name.substr(0,28).padEnd(28)} → clicks ${athClicks} | ok=${totalOk} block=${totalBlock} | unique ${kudoIds.size}`);
    
    await new Promise(r => setTimeout(r, 1500));
  } catch (e) {
    console.log(`  ERR ${name}: ${e.message?.substr(0,80)}`);
  }
}

console.log('\n=== DONE v7d ===');
console.log(`Time: ${((Date.now()-startTime)/1000/60).toFixed(1)} min`);
console.log(`Total: ${totalOk} OK / ${totalBlock} blocked | unique ${kudoIds.size}`);
console.log(`Pauses triggered: ${pauseCount}`);
fs.writeFileSync('/tmp/strava_v7d_log.json', JSON.stringify({ ok: totalOk, block: totalBlock, kudoIds: [...kudoIds] }, null, 2));
await client.close();
