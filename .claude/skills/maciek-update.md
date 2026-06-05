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
2. **CDP client**: `[ -d /tmp/node_modules/chrome-remote-interface ] || (cd /tmp && npm install --no-save chrome-remote-interface)`
3. **Maciek profile follow** w sesji Tomasza (już jest)

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

- Memory: [[maciek_profile]] — pełny profil
- Plan CSV (Tomasz dostarczył): plan 8 tyg HM block bazowy z notatkami
- Cele: sub-1:40 wrz / sub-1:38 paź
- Sesja danych: `/tmp/maciek_2026.json` (W1-W23), `/tmp/maciek_quality.json` (quality sessions)
