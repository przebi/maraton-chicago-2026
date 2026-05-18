---
name: strava-analyze
description: Pogłębiona analiza biegu/biegów ze Stravy — profil wysokości, tempo vs grade, HR drift, vertical work per km, detekcja spike'ów strapa. Używać gdy Tomasz pyta o "deep dive" pojedynczego biegu lub kilku ostatnich. Aktualizuje runs.html i deployuje.
---

# /strava-analyze — pogłębiona analiza biegów

## Cel

Surowy `get-recent-activities` daje tylko sumaryczne metryki (dystans, czas, HR avg, splits per km). To za mało żeby zrozumieć:
- **Gdzie HR rośnie i dlaczego** (cumulative drift vs reakcja na podbieg)
- **Jak pace zmienia się z gradem** (terenowa odporność)
- **Czy są spike'y strapa** (HR > realny przy zimnym strap'ie)
- **Vertical work per km** (suma gain+loss — pokazuje rampki tam gdzie net elev ~0)

Ten skill robi to pobierając **streams** (point-by-point ~1s) i generując interaktywne wykresy.

## Use cases

- Tomasz pyta: *"czy to drift czy coś innego?"*, *"przeanalizuj głębiej ten bieg"*, *"profil trasy + HR vs czas?"*
- Po długim biegu / quality session — zrozumieć co się działo
- Walidacja rough impresji (np. "bieg czuł się trudny" → faktyczne dane potwierdzają?)
- Detekcja artifactów (strap glitch, GPS jitter na zbiegach)

## Workflow

### Krok 1: Identyfikacja aktywności

Tomasz może podać:
- Konkretne ID Stravy (`activity_id`)
- Datę (np. "13.05") → poszukaj w training_log lub `mcp__strava__get-recent-activities`
- "Ostatnie N biegów" → `mcp__strava__get-recent-activities` z limit=N
- "Sesja signature z T8" → szukaj w `training_log.md`

### Krok 2: Fetch streams

Endpoint:
```
GET https://www.strava.com/api/v3/activities/{id}/streams
  ?keys=time,distance,altitude,heartrate,velocity_smooth,grade_smooth
  &key_by_type=true
Authorization: Bearer <STRAVA_ACCESS_TOKEN ze strava-mcp/.env>
```

Returns: `{ time: {data:[]}, distance: {data:[]}, altitude:..., heartrate:..., velocity_smooth:..., grade_smooth:... }` — wszystkie tablice tej samej długości, ~1 sample/sekundę.

**Token odświeżenie:**
- Strava access token żyje **6 godzin**. Jeśli 401:
```bash
curl -s -X POST https://www.strava.com/oauth/token \
  -d client_id=$STRAVA_CLIENT_ID \
  -d client_secret=$STRAVA_CLIENT_SECRET \
  -d refresh_token=$STRAVA_REFRESH_TOKEN \
  -d grant_type=refresh_token
```
- Update `strava-mcp/.env` z nowymi `access_token` i `refresh_token`.

### Krok 3: Analiza — co liczyć

#### A) Per-km splits z **gain/loss/vertical work**

Dla każdego km:
- avg pace (z velocity_smooth)
- avg HR (filter HR 50-200, ignoruj outliers)
- **gain** = suma dodatnich różnic altitude
- **loss** = suma ujemnych różnic altitude (jako wartość bezwzględna)
- **vertical work** = gain + loss (**kluczowy wskaźnik pofałdowania**)
- net elev = alt_end - alt_start

⚠️ **PUŁAPKA:** `avg grade_smooth per km` jest zwodniczy w pofałdowanym terenie — rampki ±9% co 100m dają net grade ~0%. **Patrz na vertical work, nie na grade avg**. Lekcja z 13.05.2026: skok HR na km 11-12 wyglądał jak drift, w rzeczywistości to były rampki ±8-9% (vert work 75 m/km vs ~20 m/km na płaskich km).

#### B) Quartile HR drift

Podziel stream na 4 równe okna czasowe (Q1, Q2, Q3, Q4). Dla każdego:
- avg HR
- avg pace

**Drift Q4 - Q1**:
- ≤ +3 bpm = elite (easy run zdrowy)
- +4 do +7 bpm = OK
- > +8 bpm = drift, sprawdź co go powoduje (cumulative fatigue / topografia / temperatura)

⚠️ **Drift przy stałym pace** = aerobic decoupling (zmęczenie).
**Drift przy rosnącej topografii** = topografia, nie zmęczenie. Krzyżuj z vert work per km.

#### C) HR vs grade bucket

Podziel point-by-point na 4 buckety:
- zbieg (-3% do -10%)
- płasko (-1% do +1%)
- łagodny pod (+1% do +3%)
- hill (+3% do +10%)

Dla każdego bucketu: avg HR + avg pace + n=sekund.

**Czego szuka:** czy biegacz utrzymuje stałe HR (przez zwalnianie pace na podbiegach — mądry pattern) czy HR mocno rośnie na hilli (forsowanie).

#### D) Spike detection

Strap pulsometru daje fałszywe spike'y (HR > 180) gdy elektrody są suche/zimne — typowo **pierwsze 5-10 minut** biegu.

Algorytm:
- Znajdź wszystkie punkty z HR ≥ 170 (lub ≥ 90% HRmax)
- Grupuj w "ranges" (gap między punktami > 10s = nowy range)
- Dla każdego: km start-end, t start-end, HR max
- Flag jako "strap glitch" jeśli:
  - W pierwszych 10 minutach
  - HR > 180 przy pace easy (>5:30/km)
  - HR pre-spike < 130 (zimny start)
- Inaczej: real cardio response (np. interwał, sprint końcowy)

#### E) Total elevation

Sumuj absolute gain i loss z raw altitude. Porównaj z Stravy raw `total_elevation_gain` — Strava często smoothuje i daje niższą liczbę.

### Krok 4: Output

Dwa tryby:

**A) Tylko tekstowy raport** (gdy Tomasz pyta pojedynczy bieg w trakcie rozmowy):

```markdown
## {data} — {label}

**Meta:** {dystans} km · {czas} · {avg pace} · HR {avg}/{max} · elev gain {gain}m

### Splity per km
| km | pace | HR | +gain | -loss | vert work |
|----|------|----|----|----|----------|
| 1 | 6:10 | 122 | +23m | -13m | 36m |
...

### Quartile drift
HR: Q1 / Q2 / Q3 / Q4 = X / Y / Z / W
Drift Q4-Q1: +N bpm → {ocena}

### HR vs grade
zbieg: HR {N}, pace {P}
płasko: HR {N}, pace {P}
hill: HR {N}, pace {P}

### Interpretacja
- 1-3 najistotniejsze obserwacje
```

**B) Update runs.html + deploy** (gdy Tomasz prosi viewera albo "zrób wykresy"):

1. Build `/tmp/runs_data.json` z 3 najnowszymi biegami (downsample do ~400 pkt każdy)
2. Zaktualizuj `runs.html` (podmień `const DATA = {...}` — używaj python z re.sub bo strings są długie)
3. Update "Wnioski z tygodnia" insight card
4. Deploy: `bash scripts/deploy-viewer.sh`

Format viewera: 4 wykresy per bieg (elevation, pace, HR, vertical work bar) + tabela splitów + summary.

### Krok 5: Sanity checks przed wnioskami

Zawsze sprawdź:
1. **Pierwsze 5 min HR** — jeśli > 170 przy pace > 5:30/km, to strap glitch, NIE używaj do liczenia Q1 drift
2. **Pace z velocity_smooth** może mieć dziury (null lub > 10 min/km na zatrzymaniach) — filtruj v > 1 m/s
3. **Altitude noise** — barometer ma ±2m noise. Jeśli liczsz mikro-rampy < 5m, to artifact
4. **GPS jitter na zbiegach** — bardzo szybki pace (3:30/km) na -10% grade często prawdziwy, ale > 3:00 to GPS jump

## Schemat danych JSON dla runs.html

```js
{
  "<activity_id>": {
    meta: {
      date, label, shoes, summary,
      distKm, durStr, avgHr, maxHr, avgPace, gain, loss
    },
    series: {
      dist: [],  // km, downsampled to ~400 pts
      alt: [],   // m npm
      hr: [],    // bpm
      pace: [],  // min/km decimal (np. 5.5 = 5:30)
    },
    splits: [
      { km, pace, hr, net, gain, loss, vertWork }
    ]
  }
}
```

## Pułapki które już złapaliśmy

- **`grade_smooth` avg per km = zwodniczy** w pofałdowanym terenie → zawsze raportuj **vertical work** (gain+loss).
- **Strap spike pierwsze 5-10 min** → flaguj, nie używaj do Q1 drift.
- **"Drift" może być topografia** → krzyżuj drift z vert work per km. Jeśli vert work skacze, to nie drift.
- **Pace cap dla wykresów** — niektóre punkty pace > 15 min/km (zatrzymania), klipuj do 95th percentile żeby wykres był czytelny.
- **GPS distance vs ID** — czasem dystans podany w get-activity ≠ ostatni element distance stream. Dla per-km splits używaj `distance.data`.

## Co Tomasz wie i ceni

- Krótkie, liczbowe insighty bez owijania w bawełnę
- Tabele > paragrafy
- Pokazanie błędu/słabości diagnozy = ważne (lekcja 13.05 — Tomasz zauważył że to topografia, ja pomyliłem się ze "słońce/dehydracja")
- Lekkie samokrytycyzm jest OK — przyznać że dane można było inaczej interpretować
- Avg grade per km NIE pokazuj jako kluczowy metric — zmieniaj na vertical work

## Reference

- `viewer.html` / `runs.html` — kolory, styl, layout
- `scripts/deploy-viewer.sh` — sync + netlify deploy
- `strava-mcp/.env` — STRAVA_ACCESS_TOKEN (rotuje co 6h, refresh przez OAuth)
- Memory: `signature_workout.md`, `baseline_speed_ceiling_*.md`
