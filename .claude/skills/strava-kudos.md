---
name: strava-kudos
description: Daje kudosy znajomym Tomasza na Stravie. Dwa tryby — szybki (feed dashboard) i pełny (per friend × per tydzień). Wymaga Chrome zalogowanego z portem CDP 9223. Klika realne mouse events przez CDP (Strava blokuje JS .click()). Dzienny limit ~300 kudosów; po przekroczeniu Strava blokuje 24h.
---

# /strava-kudos — automatyczne dawanie kudosów

## Cel

Tomasz okresowo prosi "daj kudosy znajomym ile zdołasz". Skill steruje Chrome'em Tomasza przez CDP, omija anti-bot, wykonuje POSTy `/feed/activity/{id}/kudo`. Powtarzamy mniej więcej raz dziennie.

**Strava API NIE obsługuje kudosów dla cudzych aktywności** (friend feed endpoint zdeprecjonowany 2018, scope `activity:write` ich nie obejmuje). Jedyna droga = przeglądarka.

## TRYBY

| Tryb | Zasięg | Kudosy/run | Czas | Plik |
|---|---|---|---|---|
| **A: Quick dashboard** | Aktualny feed (~7 dni) | 50-150 | 5-8 min | scripts/strava-kudos.mjs (v4) |
| **B: Per-friend per-week** | Ostatnie 4 tyg każdego z 122 friends | 100-200 | 30-50 min | v7d (referencyjny, w skill body) |

Tomasz zwykle prosi tryb B jeśli pyta "daj kudosy wszystkim" lub "za ostatnie X tygodni". Tryb A jest szybką wersją z feedu domowego.

## Wymagania pre-runu (oba tryby)

### 1. Chrome z portem CDP 9223

```bash
mkdir -p /tmp/chrome-strava
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9223 \
  --user-data-dir=/tmp/chrome-strava \
  --no-first-run --no-default-browser-check \
  https://www.strava.com/dashboard > /tmp/chrome-strava.log 2>&1 &
```

**Ważne:** osobny `--user-data-dir`, NIE główny profil Tomasza (macOS singleton lock pozbywa się portu). Jednorazowe logowanie na Stravę w tym profilu przeżyje w `/tmp/chrome-strava` do następnego runu (chyba że Chrome padnie).

### 2. Sprawdź czy port live + zalogowany

```bash
curl -s --max-time 2 http://localhost:9223/json/version  # powinno zwrócić Browser
curl -s http://localhost:9223/json | python3 -c "import json,sys; print([(t['title'],t['url']) for t in json.load(sys.stdin) if t['type']=='page'])"
```

Jeśli URL = `/login` → poproś Tomasza zalogował się raz.

### 3. CDP client

```bash
cd /tmp && [ -d node_modules/chrome-remote-interface ] || (npm init -y > /dev/null && npm install --no-save chrome-remote-interface)
```

### 4. Lista friends (cache w /tmp/strava_friends.json)

Pobiera się raz, paginacja po 25 osób per stronę:

```js
for (let page = 1; page <= 20; page++) {
  await Page.navigate({ url: `https://www.strava.com/athletes/${MY_ATHLETE_ID}/follows?page=${page}` });
  // parse a[href=/athletes/N] (exclude self), stop on empty page
}
```

Tomasz athlete ID = **24659157**.

## TRYB A: Quick dashboard

Szybki, gdy Tomasz chce po prostu nadrobić ostatnie aktywności znajomych z feedu home.

```bash
node /Users/tomaszprzebieracz/projects/maraton-chicago-2026/scripts/strava-kudos.mjs
```

Logika:
1. Otwiera `/dashboard?num_entries=200` (Strava cap zwykle ~100-200 entries)
2. Scrolluje w dół, klika każdy pending `button[data-testid="kudos_button"]` z title "Przyznaj kudos" / "Give kudos"
3. Real mouse via `Input.dispatchMouseEvent` (NIE `.click()`, Strava ignoruje JS-trigger)
4. Throttle 250-350ms między klikami

Output: ~70-150 kudosów / 5-8 min jeśli feed pełen pending.

## TRYB B: Per-friend per-week (preferowany dla "wszystkich znajomych")

Najpełniejszy zasięg. Każdy z 122 friends × 4 ostatnie tygodnie ISO.

### Mechanika

```js
const WEEKS = ['2026XX', '2026XX', '2026XX', '2026XX']; // last 4 ISO weeks
const FRIENDS = [[athleteId, name], ...]; // 122 osoby z /tmp/strava_friends.json

for (const [aid, name] of FRIENDS) {
  await Page.navigate({ url: `https://www.strava.com/athletes/${aid}` });
  
  for (const week of WEEKS) {
    // Zmiana hash bez full reload — Strava sama ładuje aktywności tygodnia
    await evalJS(`location.hash = '#interval?interval=${week}&interval_type=week&chart_type=miles&year_offset=0'`);
    await sleep(1500);
    await evalJS(`document.querySelector('#interval')?.scrollIntoView({block:'start'})`);
    
    // Klikaj pending dopóki są
    while (true) {
      const coords = await evalJS(`(() => {
        const PENDING = ['Give kudos', 'Przyznaj kudos'];
        const btns = Array.from(document.querySelectorAll('button[data-testid="kudos_button"]')).filter(b => PENDING.includes(b.title));
        if (!btns.length) return null;
        btns[0].scrollIntoView({block:'center'});
        const r = btns[0].getBoundingClientRect();
        return { x: r.left + r.width/2, y: r.top + r.height/2 };
      })()`);
      if (!coords) break;
      // Real mouse click via CDP
      await Input.dispatchMouseEvent({type:'mouseMoved', x:coords.x, y:coords.y});
      await Input.dispatchMouseEvent({type:'mousePressed', x:coords.x, y:coords.y, button:'left', clickCount:1});
      await Input.dispatchMouseEvent({type:'mouseReleased', x:coords.x, y:coords.y, button:'left', clickCount:1});
      await sleep(2000); // 2s throttle — testowane, mniej = rate limit szybciej
    }
  }
}
```

### Numer tygodnia ISO

Strava używa `YYYYWW` (4 cyfry rok + 2 cyfry tydzień ISO 8601). Bieżący tydzień:

```js
const now = new Date();
const isoWeek = (d => {
  const t = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
  const day = t.getUTCDay() || 7;
  t.setUTCDate(t.getUTCDate() + 4 - day);
  const yearStart = new Date(Date.UTC(t.getUTCFullYear(),0,1));
  return [t.getUTCFullYear(), Math.ceil((((t - yearStart) / 86400000) + 1)/7)];
})(now);
// last 4 weeks
const WEEKS = [];
for (let i = 0; i < 4; i++) {
  const [y, w] = [isoWeek[0], isoWeek[1] - i];
  WEEKS.unshift(`${y}${String(w).padStart(2,'0')}`);
}
```

### Rate limit playbook

**Daily cap obserwowany: ~300 kudosów / 24h**. Po przekroczeniu Strava zwraca 403 na każdy POST. Plan:

1. **Rolling window** ostatnich 10 POSTów — jeśli >30% błąd 403/429 → pauza
2. **Pierwsza pauza: 3 min** (1 min nie wystarcza — Strava utrzymuje block dłużej)
3. **Druga pauza: 3 min** — jeśli znów blocked
4. **Po 3 pauzach: STOP, wait user** (zapisz `processed_idx` do JSON)
5. **Continue next day**: resume od ostatniego `processed_idx`

```js
const recentResults = []; // 'ok' | 'block' | 'other'
Network.on('responseReceived', e => {
  if (e.response.url.match(/\/feed\/activity\/\d+\/kudo$/)) {
    const status = e.response.status;
    if (status === 200) recentResults.push('ok');
    else if (status === 403 || status === 429) recentResults.push('block');
    else recentResults.push('other');
    if (recentResults.length > 10) recentResults.shift();
  }
});

// Before each athlete
if (recentResults.length >= 5) {
  const blockRate = recentResults.filter(r => r === 'block').length / recentResults.length;
  if (blockRate > 0.3) {
    pauseCount++;
    if (pauseCount >= 3) { /* STOP, save state */ break; }
    await sleep(3 * 60_000);
    recentResults.length = 0;
  }
}
```

### Continue-from-index

State plik: `/tmp/strava_kudos_state.json` z `last_processed_idx`. Per athleta po sukcesie, zapisz. Jutro restart od `last_processed_idx + 1`.

## PUŁAPKI (wszystkie dziś złapane — 18.05.2026)

| Bug | Symptom | Fix |
|---|---|---|
| **i18n title** | "Give kudos" filter pomija polskie aktywności | `PENDING = ['Give kudos', 'Przyznaj kudos']` |
| **Endpoint** `/kudo` vs `/kudos` | Network monitor 0 POSTów do `/kudos` | Filter `url.endsWith('/kudo')` (singular!) |
| **`.click()` ignorowany przez Stravę** | DOM zmienia title ale POST nie idzie | `Input.dispatchMouseEvent` (CDP — generuje `isTrusted=true`) |
| **`navigator.webdriver=true`** | Strava blokuje POST | `Page.addScriptToEvaluateOnNewDocument({source: "Object.defineProperty(navigator,'webdriver',{get:()=>undefined})"})` |
| **Scroll loop** | Skrypt klika te same buttony cyklicznie | NIGDY scroll wstecz, monotonic w dół ALBO hash-change |
| **CSRF nie pasuje** | POST z fetch + CSRF z innej strony = 401/403 | Real click via CDP omija CSRF (browser sam wstawia) |
| **`window` w Node template literal** | `ERR: window is not defined` | Wszystkie kalkulacje koordynat w **browser-side IIFE**, nie w Node string interpolation |
| **Training log nie ma kudo buttons** | Activity IDs ale brak buttonów | Użyj `/athletes/{id}#interval?interval=YYYYWW` na profile, NIE `/training/log` |
| **Profile bez `#interval` pokazuje tylko 4 tyg kalendarz dni** | Brak "tygodniowych słupków" | Wymaga hash `#interval?interval_type=week` |
| **Dni kalendarza (a.bar `text="27 0h 23min"`) ≠ słupki tygodni** | Sam selektor `.bar` myli | Filter `href.includes('interval=') && href.includes('week')` |
| **Strava blokuje 403 silent** | 30 clicks, ok=0, blocked=8, 22 brak response | Rolling window 30% block rate threshold + 3min pauza |
| **WebSocket CDP padnie po ~30 min** | `Error: WebSocket connection closed` | Re-connect lub krótsze sesje. Save state co athleta. |
| **Cookies tracone przy Chrome crash** | Profile padł → wraca /login | Brak fixu, trzeba ponownie zalogować |

## Quick run dla Tomasza

```bash
# 1. Chrome up?
curl -s --max-time 2 http://localhost:9223/json/version > /dev/null && echo OK || echo DEAD

# 2. Lista friends (cache)
[ -f /tmp/strava_friends.json ] || node scripts/strava-friends-pull.mjs

# 3. Tryb B (preferowany)
node scripts/strava-kudos.mjs --mode=friends-weeks --weeks=4

# 4. Tomasz sprawdza wynik w jego Chrome → Cmd+Shift+R
```

## Co Tomasz wie i ceni

- **Liczbowe statusy** per athleta (clicks, ok, block, unique cum)
- **Honest** raportowanie kiedy Strava blokuje (NIE udawać że klikamy)
- **Auto-pause + auto-resume** — nie pytać o każdą pauzę
- **Stop po 3 pauzach** żeby nie bombardować serwera dalej
- **State save** dla continue jutro

## Reference

- Working script: [scripts/strava-kudos.mjs](../../scripts/strava-kudos.mjs) — najnowsza wersja v7d
- Friends cache: `/tmp/strava_friends.json` (122 IDs + names)
- State file: `/tmp/strava_kudos_state.json` (last_processed_idx, total_ok_today)
- Tomasz athlete ID: 24659157
- Today's bug session: dashboard limits ~100 entries → friends/weeks tryb obowiązkowy dla pełnego pokrycia

## Empirical limits (18.05.2026 session)

W jednym dniu (~3.5h sesji):
- **253 confirmed kudos** w 3 fazach (dashboard 70 + profile interval 100 + 83 = 253)
- **236 blocked** (status **429** silent)
- 58/122 athletes processed do auto-stop

**Strava limit empirycznie ~250-300 kudosów / 24h** dla cudzych aktywności przez ten endpoint.

### Rate limit response anatomy

```
HTTP/1.1 429 Too Many Requests
content-type: application/json; charset=utf-8
server: istio-envoy
status: 429 Too Many Requests
{"success":"false"}
```

**Kluczowe:**
- Status: **429** (Too Many Requests, NIE 403 Forbidden — wcześniej mi się myliło)
- Body: zawsze `{"success":"false"}`
- **BRAK `Retry-After` header** — Strava nie ujawnia kiedy odblokuje (anti-bot)
- Server: `istio-envoy` — rate limit jest na Envoy proxy layer, NIE w aplikacji Stravy
- 3 min pauza nie wystarcza — limit trzyma się ≥24h od ostatniego successu

**Conclusion**: pełna runda 122 friends × 4 tygodnie wymaga **3 dni** żeby zrobić bez 429. Plan:
- Dzień 1: athletes #1-58 (~250 kudosów)
- Dzień 2: athletes #59-100
- Dzień 3: athletes #101-122

Po 3 pauzach z rzędu (każda 3 min, każda kończąca się 429 streak) — stop, jutro resume z `START_IDX=<last_done>`.

### Future improvement: exponential backoff zamiast fixed 3 min

Zamiast 3-3-3 min, można spróbować: 1min → 5min → 15min → stop. Jeśli po 15 min nadal 429, to faktycznie limit dzienny. Test jutro empirycznie ile musi czekać po pierwszym 429 żeby się odblokować.
