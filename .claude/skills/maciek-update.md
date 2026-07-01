---
name: maciek-update
description: Pobiera treningi Maćka (syn Tomasza, Strava ID 138427035) ze Stravy przez Chrome CDP. Strava API blokuje cudze activity details, więc scrape przez Chrome zalogowany na konto Tomasza (Tomasz follow Maciek). Tygodniowa analiza + porównanie z planem CSV.
---

# /maciek-update — pull + analiza treningu Maćka

## Cel

Tomasz coachuje syna (Maciek). Cel: HM sub-1:40 wrz/paź 2026.
Strava API odmawia cudzych activity details (403 Forbidden), więc używamy **Chrome CDP scrape przez sesję Tomasza** (Tomasz follow Maciek, więc widzi jego activities).

## Pre-requisites

1. **Chrome 9223 zalogowany** na konto Tomasza ([[strava_kudos_setup]])
2. **CDP client**: `[ -d /tmp/node_modules/chrome-remote-interface ] || (cd /tmp && npm install chrome-remote-interface)`
3. **Maciek profile follow** w sesji Tomasza (już jest)
4. ⚠️ **/tmp jest EFEMERYCZNE** — po czyszczeniu (reboot / zmiana dnia) znika `/tmp/node_modules` (reinstall jw.) **ORAZ profil Chrome `/tmp/chrome-strava` = sesja Stravy/Garmina pada**. Symptom: scrape zwraca teaser „Zarejestruj się za darmo" / `hasPrzebieracz:false` / `activityLinks:0`. **Fix:** poproś Tomasza o ponowne zalogowanie w oknie Chrome (Strava i/lub Garmin), potem ponów scrape.

## Workflow

### Krok 1: Pull weekly summary (wszystkie tygodnie)

Iteruje przez tygodnie ISO 2026 URL pattern:
```
https://www.strava.com/athletes/138427035#interval?interval=2026WW&interval_type=week&chart_type=miles&year_offset=0
```
gdzie `WW` = numer tygodnia ISO 8601 (2-cyfrowy padding).

Per week scrape:
- Activity IDs (filter only Maciek's via `Maciej Przebieracz` w textContent)
- Data, dystans, tempo, nazwa activity

**WAŻNE**: linki `/activities/{ID}` na profilu Maćka czasem prowadzą do **MOICH** activities (Strava "Twoje ostatnie aktywności" sekcja "Widok porównawczy" — Strava porównuje z moimi PB). Filtruj **TYLKO te z `Maciej Przebieracz` w karcie**.

Reference: `/tmp/maciek_pull.mjs`, `/tmp/maciek_months.mjs`, `/tmp/maciek_last4.mjs`

### Krok 2: Pull activity details (per quality session)

Per activity:
```
https://www.strava.com/activities/{ID}
```

Z DOM page extract:
- `Dystans`, `Czas ruchu`, `Tempo` (avg pace)
- `Wysokość`, `Kilokalorie`
- **HR avg** — szukaj `(\d+)\s*bpm` w body text (jest tam "5:49 /km 156 bpm 171 spm 26 ℃" format)
- **Kadencja**: `(\d+)\s*spm`
- **Temperatura**: `(\d+)\s*℃`
- **Splity per km**: szukaj sekcji `Międzyczasy` → regex `(\d+)\s*([\d:]+) \/km`

**HR max NIE widoczne** dla cudzych — Strava ukrywa max/strefy. Mamy tylko **avg HR**.

**Toggle "Tętno"** w UI Stravy nie działa automation (label DIV, nie button — click nic nie robi via CDP). Akceptujemy że mamy avg.

Reference: `/tmp/maciek_details.mjs`, `/tmp/maciek_quality.mjs`, `/tmp/maciek_hr_deep.mjs`

### Krok 3: Identifikacja quality sessions

Pace per km > tempo threshold (~4:30/km lub szybciej):

```js
// W splits: find segments where pace < 5:00/km AND duration > 60s
const fastSplits = splits.filter(s => {
  const [m, sec] = s.pace.split(':').map(Number);
  return (m + sec/60) < 5.0;
});
```

Typowe wzorce Maćka:
- **TEMPO 4-5×1km**: km 4-5 fast, km 6 recovery, km 7-8 fast, etc. Pace ~4:25-4:50/km
- **LONG z progresją**: km 1-17 easy 5:55-6:10, km 18+ FAST 4:43-4:56
- **FARTLEK + PB**: km 1-3 warmup slow, km 4 fast, km 7 fast, km 11 PB (np. Agrykola 4:01)

### Krok 4: VDOT + HM prediction

Aktualne benchmarki:
- 1000m PB → VDOT (Daniels tables) → HM prediction
- Tempo 4-5×1km avg → VDOT (5K equivalent) → HM
- Long z finish → race-day equivalent

**Daniels VDOT 49 → HM ~1:34**, VDOT 47 → HM ~1:39.
Maciek aktualny VDOT 47-49 = HM 1:34-1:39.

### Krok 5: Wykonanie vs plan (CSV)

Tomasz dostarczył CSV z planem 8 tyg z notatkami. Porównanie:
- Plan km vs wykonane km (Maciek konsekwentnie +5-15% over)
- Plan tempo vs wykonane tempo (Maciek konsekwentnie szybciej niż target)
- Subjective feedback z notatek ("lekkie zmęczenie nogi" itp)

## ŹRÓDŁA DANYCH (ustalone 14.06.2026)

- **Strava = TYLKO kudosy** (skill strava-kudos).
- **Tomasz (własne dane) = Garmin MCP** (`mcp__garmin__*`) — czyste, strukturalne + **HRV / training-readiness / sen / body-battery / stress** = fatigue markers (priorytet #1).
- **Maciek = Garmin SCRAPE** (sesja Tomasza + Connections). MCP NIE widzi connection-shared activities Maćka.

Garmin > Strava dla danych: Strava ukrywa cudze **max HR / strefy**; Garmin (przez Connections „Moje połączenia") daje **splity + HR avg/max + kadencję + międzyczasy**.

### Setup Garmin MCP BEZ drugiego logowania / 2FA (kluczowy trik — DZIAŁA)

MCP potrzebuje `~/.garmin-connect-mcp/session.json`. Zamiast osobnego loginu Playwright (2FA!), **reużyj zalogowanego Chrome 9223** (Tomasz loguje Garmina RAZ w oknie Chrome) i wyciągnij sesję przez CDP — skrypt `/tmp/garmin_session.mjs`:
- nawiguj tab na `https://connect.garmin.com/app/activities`, `sleep(9000)`
- CSRF: `Runtime.evaluate` → `document.querySelector('meta[name="csrf-token"]').content`
- cookies: `Network.enable()` → `Network.getAllCookies()` → filtr `domain.includes('garmin')` → `[{name,value,domain}]` (29 cookies: SESSION, GARMIN-SSO, JWT_WEB, CASTGC...)
- **zapis pliku z Node** (`fs.writeFileSync`), NIE z `browser_run_code_unsafe` (sandbox blokuje require/import → `ERR_VM_DYNAMIC_IMPORT_CALLBACK_MISSING`)
- format: `{ "csrf_token": "...", "cookies": [...] }` → `~/.garmin-connect-mcp/session.json`
- `mcp__garmin__check-session` → `status: ok` + profil (id 2405885, VO2 56, LTHR 169, waga 61)
- ⚠️ cookies wygasają po kilku h → Tomasz re-login w Chrome → re-run `/tmp/garmin_session.mjs`

Po setupie (Tomasz): `list-activities`, `get-activity {id}`, `get-activity-splits`, `get-activity-hr-zones`, `get-hrv`, `get-training-readiness`, `get-sleep`, `get-body-battery`, `get-daily-stress`.

### Maciek przez Garmin scrape (Connections) — DZIAŁA

- **Maciek Garmin profile GUID: `d3c4637c-c93b-4944-aac6-f0ff090fbf2e`** (Tomasz = profil `przebi`).
- **Lista recent:** scrape `https://connect.garmin.com/modern/profile/{GUID}` → linki `a[href*="/activity/"]` + tekst karty (Maciej Przebiercz / Dziś-Wczoraj-dzień / dystans / czas / tempo). Skrypt `/tmp/garmin_maciek_list.mjs`. Zwraca `order` (od najnowszej) + `map{ID:tekst}`.
- **Detale:** scrape `https://connect.garmin.com/modern/activity/{ID}` → `body.innerText` (dystans/czas/tempo/kalorie; HR `(\d+) bpm`; okrążenia/splity niżej — scroll + grab full text). Skrypt `/tmp/garmin_activity.mjs {ID}` / `/tmp/garmin_detail.mjs {ID}`.
- SPA → po `Page.navigate` daj `sleep(9000)` + scroll. **Feed `/app/home` NIE renderuje aktywności (0 linków) — idź przez PROFIL Maćka, nie feed.**
- ⚠️ Garmin pokazuje dzień-nazwę (Dziś/Wczoraj/Poniedziałek) dla bieżącego tyg, datę dla starszych — **relatywne do realnej daty Garmina** (może ≠ data systemowa sesji).

**Precedens:** 5K test (sob, act `23230291426`) — 5000 m, 21:14, 4:15/km, Tarnowskie Góry track; avg HR 181, max HR 190 (94% HRmax 201) — wyciągnięte z Garmina (Strava by max HR nie dała).

Skrypty referencyjne: `/tmp/garmin_session.mjs`, `/tmp/garmin_maciek_list.mjs`, `/tmp/garmin_activity.mjs`, `/tmp/open_garmin.mjs`

## Pułapki

| Bug | Symptom | Fix |
|---|---|---|
| **Strava overlay "Widok porównawczy"** | Linki `/activities/N` z profilu Maćka prowadzą do MOICH activities | Filter karty po tekście `Maciej Przebieracz` w textContent |
| **Best efforts to też MOJE** | Sekcja PB na profilu Maćka pokazuje MOJE PB jako overlay porównawczy | NIE używać sekcji "Najlepsze próby" — używać 1000m PB z Strava activity page |
| **HR Forerunner 165** | HR widoczny tylko ~3 tyg historii (Maciek dopiero dostał zegarek) | Activities sprzed ~14.05.2026 nie mają HR data |
| **Strava best efforts widoczne ale max HR ukryty** | Mamy avg HR, ale max + strefy private | Akceptujemy. Estymata HRmax z avg + VDOT confidence |
| **Toggle "Tętno" w UI** | Nie reaguje na automation click | Mamy avg HR z text body, max HR niedostępne via Chrome scrape |
| **Activity name w włoskim** | "Corsa serale", "Corsa mattutina", "Corsa dell'ora di pranzo" | Strava auto-detects (Maciek phone Italian locale?) — to JEST Maciek mimo języka |
| **Multiple runs per day** | Maciek robi 1-3 biegi dziennie | Sumuj dystans per day, identifikuj quality vs easy |

## Quick run

```bash
# 1. Sprawdź Chrome (zalogowany Tomasz?)
curl -s http://localhost:9223/json | python3 -c "import json,sys; print([t.get('url','')[:80] for t in json.load(sys.stdin) if t.get('type')=='page'])"

# 2. Pull last 4 weeks summary (lub całość)
# Edit week range w skrypcie, run:
node /tmp/maciek_months.mjs   # iterates W1-W23 (lub modify range)

# 3. Pull details quality sessions
node /tmp/maciek_quality.mjs  # bierze ostatnie 6 quality

# 4. Analiza VDOT + HM prediction
node -e "..." # custom analiza per session
```

## Cele 2026

- **Wrzesień 2026**: HM #1 sub-1:40 (test race)
- **Październik 2026**: HM #2 sub-1:38 (PB)
- **Wakacje lip+sie**: high volume base + race-specific

## Output format

Po każdym pull dla Tomasza:

```markdown
## Maciek — Update tygodnia W{NN}

### Objętość
- {N} aktywności, {KM} km total
- {N} quality sessions: {LIST}

### Quality sessions detail
- {DATA} {LABEL}: {DYST} @ avg {PACE} HR {AVG_HR} ({Z%}HRmax = Z{N}-Z{N+1})
- Splity: {LIST km pace}
- Komentarz: {analysis}

### VDOT + HM prediction
- Current VDOT: {N} (z {benchmark})
- HM equivalent: {1:XX-1:YY}

### Wykonanie vs plan
- Plan W{NN}: {N} km, {quality}
- Wykonanie: {N} km, {actual quality}
- Δ: {+%/-%}

### Rekomendacje
- {1-3 specific things to adjust next week}
```

## Reference

- **LOG: `data/maciek_log.md`** — po KAŻDYM pullu dopisz nową sesję na górę tabeli + rozbicie interwałów dla sesji jakościowych. To kanoniczny zapis progresu Maćka.
- Cele aktualne: **sub-1:35 (Praski 5.09) / sub-1:33 (Cracovia 11.10)** — plan `data/maciek_plan_full.xlsx` (W9-25).
- Memory: [[maciek_profile]] — pełny profil
- Plan CSV (Tomasz dostarczył): plan 8 tyg HM block bazowy z notatkami
- Cele: sub-1:40 wrz / sub-1:38 paź
- Sesja danych: `/tmp/maciek_2026.json` (W1-W23), `/tmp/maciek_quality.json` (quality sessions)
