# Training Log

Aktualizowany przez `/coach-update` (Claude pobiera ze Stravy i analizuje).

## Format wpisu

```
### YYYY-MM-DD — typ
- Dystans: X km
- Czas: HH:MM:SS (avg pace M:SS/km)
- HR avg / max: X / Y
- Strefy (% czasu): Z1: %, Z2: %, Z3: %, Z4: %, Z5: %
- Plan: <co miało być> / Wykonanie: <co wyszło>
- Komentarz: <subiektywny / od Claude>
- URL: <link Strava>
```

---

## Baseline: ostatnie 5 tygodni (01.04–06.05.2026)

Pobrane bezpośrednio ze Strava API (36 aktywności, w tym 22 biegi).

### Wolumen biegowy per tydzień

| Tydzień | Daty | Km biegowe | Sesji bieg. | Walk km | Komentarz |
|---|---|---:|---:|---:|---|
| W14 (część) | 01.04–05.04 | 44.1 | 2 | 13.5 | 2× długi przed taperem |
| **W15** | 06.04–12.04 | **91.4** | 5 | 4.3 | Peak. Akcent 8 dni przed Wiedniem (3×5K) |
| **W16** | 13.04–19.04 | 66.5 | 3 | 5.3 | **Maraton Wiedeń 19.04 — 3:11** |
| W17 | 20.04–26.04 | 63.3 | 4 | 8.9 | Wariant C — recovery niedopełniony |
| W18 | 27.04–03.05 | 78.7 | 5 | 7.1 | 2 hard days (29.04, 03.05) — 14 dni po marathonie |
| W19 (do śr) | 04.05–06.05 | 26.7 | 2 | 4.7 | Quality session 06.05 |

### Kluczowe sesje

#### 2026-04-11 — 3×5 km progresywne (8 dni przed Wiedniem)
- Dystans: 21.39 km, czas 1:39:46 moving (4:40/km avg)
- HR avg/max: 143 / **174** (stream **czysty**, 0 spike'ów)
- Struktura (z auto-lapów Garmina):
  - Rozgrzewka 3.12 km @ 5:17, HR 113
  - REP 1 (5.00 km @ 4:04, HR avg ~150, max 167)
  - Trucht 1.10 km @ 6:48
  - REP 2 (5.01 km @ 3:59, HR avg ~164, max 170)
  - Trucht 0.96 km @ 7:30
  - REP 3 (5.02 km @ 3:53, HR avg ~169, max 174)
  - Cooldown 1.18 km @ 7:18
- Komentarz: trening ciężki, tempo lekko szybsze niż plan (4:05/4:00/3:55). Suffer 201. Lekcja: za mocno + za blisko (8 dni). Następnym razem 14 dni przed.

#### 2026-04-19 — Maraton Wiedeń
- Czas: **3:11** (3:10:35 ruchowy)
- Pace avg: 4:30/km (positive split)
- Dystans: 42.37 km
- HR avg/max: 155 / 188 (max do weryfikacji vs spike)
- Suffer: 559
- Komentarz: odpuszczony bieg od 15 km, ciepło 20+°C. Forma realna na 3:00–3:05.

#### 2026-04-29 — Quality 15 km (10 dni po marathonie)
- 15.25 km @ 5:07 avg, HR avg 148 (Z3+ / Z4 dolny), suffer 171
- Komentarz: za dużo, za blisko po marathonie. Wariant C w działaniu.

#### 2026-05-03 — Quality 20 km @ 4:50 (14 dni po marathonie)
- 20.0 km @ 4:50 avg, HR avg 147, suffer 212
- + Hike 16.76 km / 4h16 tego samego dnia
- Komentarz: heavy day. Threshold cardiac drift, podwójna sesja.

#### 2026-05-06 — Sesja kluczowa (dziś, pre-T1)
- Plan: 6×1600 m progresywnie 4:05/4:00/3:55/3:50/3:45/3:40
- Wykonanie: 4 reps zgodnie z planem + 5. przerwany na 0.61 km (sufit 3:46), 6. nie próbowany
- Dystans: 12.78 km, HR avg/max: 149 / **176** (stream czysty)
- Lapy:
  - WU 3.01 km @ 5:32 (HR 138/153)
  - REP 1: 1.59 km @ 4:04 (HR 164/170)
  - REP 2: 1.60 km @ 3:59 (HR 168/173)
  - REP 3: 1.60 km @ 3:54 (HR 168/175)
  - REP 4: 1.60 km @ 3:49 (HR 170/176)
  - REP 5 (przerwany): 0.61 km @ 3:46 (HR 160/170)
- Komentarz: silnik OK (4 reps zgodnie z planem), bateria na granicy (5. nie utrzymane). Sufit prędkościowy dziś = 3:46/km. **Decyzja: Ryga skreślona, T1 startuje 11.05 zgodnie z planem.**

### Diagnoza HR / czujnika

W okresie 01.04–06.05 znalezione spike'i HR (electrode disconnect chest strap'a) na biegach:
- 04-08 (max 203), 04-12 (206), 04-16 (213), 04-29 (200) — fake high readings (typowo 5–10% biegu w >190)
- Pattern: pierwszy fake spike 1–10 min po starcie biegu, po nawiązaniu paska
- **Czyste streamy:** 04-11, 04-22, 05-06 (dziś)
- **Implikacja:** średnie HR z biegów ze spike'ami są zawyżone. „Grey zone running" diagnoza była częściowo artefaktem czujnika, mniej dramatyczna niż początkowy obraz.
- **Praktyka:** zwilż elektrody przed biegiem (ślina/żel), sprawdź styk. Rozważyć ramienny czujnik (Polar OH1, Garmin HRM-Pro) na przyszłość.

### HRmax — werdykt

W sesjach z czystym streamem najwyższe odczyty:
- 04-11 hard (3×5K): max **174** (ostatni rep @ 3:49)
- 05-06 hard (5×1600): max **176** (4. rep @ 3:49)
- Oba „ciężko ale nie all-out"

**HRmax 182 zostaje** w CLAUDE.md. Realny zapas widać przy 5K test (T8) i pierwszych VO₂max (T4–T5).

### Strefy w 5-tyg oknie (% czasu w biegu, na bazie czystych biegów)

| Strefa | % czasu (cele) | % czasu (wyk.) | Komentarz |
|---|---:|---:|---|
| Z1–Z2 (≤127) | 70–80% | ~40% | Za mało easy |
| Z3 (127–146) | 10–20% | ~45% | Grey zone — za dużo |
| Z4 (146–164) | 5–10% | ~10% | OK na akcenty |
| Z5 (>164) | <5% | ~5% | OK na reps |

**Wniosek:** baseline aerobic za płytka, wynik wariantu C i medium-paced runs. Plan T1–T2 (HR cap 127) bezpośrednio adresuje to.

---

## Tydzień 0 — pre-T1 (07–10.05.2026)

Cel: post-quality recovery 4 dni. ~25–30 km. Bez akcentów.

### 2026-05-07 (czw) — REST + cross-training (rower)
- Morning Ride: 28.78 km @ ~17.5 km/h, HR avg 104/129 — easy spinning
- Afternoon Ride: 27.94 km @ ~16.6 km/h, HR avg 108/152 — drugi ride
- **Total: 56.7 km roweru w jeden dzień, HR Z1-Z2** = active recovery, idealne post-quality
- Zero biegu zgodnie z planem ✓

### 2026-05-08 (pt) — REST
- Morning Walk: 4.46 km
- Afternoon Walk: 4.76 km
- Zero biegu (plan) ✓
- Pegasus 42 + Plus dostawa po południu

### 2026-05-10 (nd) — Debiut **Pegasus 42** ⭐
- **Achillesy rano:** lekko czuł (insertional, lewa). Po 15.35 km w nowych butach = OK, nie acute. Eccentric calves zaczął ostro = aktywne treatment Alfredson MODIFIED.
- **Status:** subclinical stable, kontynuujemy plan T1 z monitorowaniem
- Morning Run: **15.35 km @ 5:53/km** (plan był 8 km — pojechał 2×)
- HR avg/max raw: 139.5 / 178 — **ALE pasek HR FAILED km 1-11** (electrode disconnect, spike'y)
- Real HR (km 12-16, gdy strap zaczął działać): **119-125 bpm**
- Drift na km 12-16: **0 bpm** (idealne aerobic state)
- Suffer 153 (zawyżony przez fake HR spike'y)
- Buty: **Pegasus 42** (g30955501) — debiut. Plus 1.5 dnia po debiucie Pegasus Plus (09.05 12.7 km).
- **Real interpretation:** Real avg HR pewnie ~125 bpm (z drugiej połowy stable). Pace 5:53 + HR 125 = idealny easy w Z2 (66% HRmax 183).
- **Komentarz:** ciało wciąż w base state, drift = 0 bpm w 5 km stable danych = aerobic engine genialny. ALE 15.35 km zamiast 8 km plan = **przekroczenie** (dzień przed T1 start). Pegasus 42 OK, achillesy do potwierdzenia.
- HR pasek issue: zwilż elektrody przed startem, sprawdzić jakość paska (czasem wymiana po 1-2 latach)
- URL: https://www.strava.com/activities/18447023903

### 2026-05-09 (sb) — Debiut **Pegasus PLUS** ⭐
- Morning Run: **12.67 km @ 5:31/km**
- HR avg/max: **129.9 / 163**, suffer 73
- **HR drift po ćwiartkach: Q1=130, Q2=131, Q3=130, Q4=126** (NEGATYWNY -4 bpm)
- Buty: **Pegasus Plus** (gear_id g30955507) — debiut. Pegasus 42 (g30955501) wciąż 0 km, czeka.
- Plan: easy 10-12 km @ >5:45, HR<135 — wykonanie pace 5:31 lekko szybciej, ale HR średnia 130 = blisko Z2 cap (127), Q4 schodzi do 126 = OK
- **Komentarz:** negative HR drift na 12+ km easy = świetny aerobic state. Ciało zregenerowane po Wiedniu + 06.05 quality. Pegasus Plus z ZoomX dał pop = nogi same chcą lekko szybciej. Max 163 = pewnie krótki odcinek szybszy w środku.
- **Ciekawa decyzja:** Tomasz wybrał Plus (long-run shoe) na pierwszy bieg, nie 42 (daily). To może być dobry sygnał — ZoomX feel pewnie super.
- URL: https://www.strava.com/activities/18433994386

---

## T1 — RECOVERY (~44 km, 11–17.05.2026)

### 2026-05-11 (pn) — REST (DOMS uda+glutes po 10.05)
- Spacer + foam roll + sauna
- DOMS recovery active

### 2026-05-12 (wt) — T1 sesja 1, easy run
- Morning Run: **10.22 km @ 5:53/km**, HR 128/158, suffer 57
- Buty: Pegasus 42 ✓
- HR avg 1 bpm nad cap, OK
- Plan 8 km, +25%
- Kreatyna 1100 start (5 caps/dzień)

### 2026-05-13 (śr) — T1 sesja 2, easy run
- Morning Run: **13.09 km @ 5:59/km**, HR 130/195 (strap spike), suffer 78
- Buty: **PrimeX 2 Strung** ⚠️ (race shoe na easy — marnotrawstwo pianki)
- Plan 10 km, +31%

### 2026-05-14 (cz) — T1 sesja 3, easy run (zamiast REST!)
- Morning Run: **10.00 km @ 6:04/km**, HR avg **125** (Z2 idealnie), max 140
- **HR drift Q1→Q4: 122→127→125→123 = 0 bpm drift = idealne aerobic state**
- Suffer 38 (low)
- Buty: **Pegasus 42** (Tomasz poprawił tagging w Stravie — pierwotnie Strava tagowała PrimeX 2 jako default)
- Plan: REST (Tomasz zamiast tego pojechał 10K + siłownia)
- **Komentarz:** ciało reaguje świetnie (HR <127, drift 0, mięśnie OK po DOMS). ALE: 33 km w 3 dni vs plan 18 km = **+83%**. Pattern wariant C — Tomasz robi więcej niż plan zakłada gdy się czuje dobrze. Krytyczne dla long-term recovery & Achilles protection.
- URL: https://www.strava.com/activities/18499513489

### 2026-05-15 (pt) — REST (active walk)
- Morning Walk: **4.73 km**, HR 82, 52 min
- Spacer regeneracyjny

### 2026-05-16 (sb) — T1 sesja 4 — **PIERWSZY LONG T1 (21.10 km HM dystans!)** ⭐
- Morning Run: **21.10 km @ 5:43/km**, HR **128**/178, suffer 111, czas 2:00:51
- Buty: Pegasus Plus (g30955507) ✓
- Elev gain **271m** (najwięcej z T1, falisty teren)
- **Quartile HR drift: Q1=129 / Q2=128 / Q3=127 / Q4=130 → +1 bpm po 21 km = elite tier**
- HR vs grade: zbiegi 129 @ 5:13, płasko 127 @ 5:48, hill ≥3% 128 @ 6:19 (stałe HR, pace adaptive — mądry "by feel" pattern)
- Spike HR 170-176 w pierwszych 90 sec (strap glitch, NIE real)
- Km 20 pace 5:02 @ HR 138 (finisz zbiegowy), km 21 cooldown 6:16
- **Komentarz:** baseline po Wiedniu zakończony — drift +1 bpm na HM dystansie = aerobic engine sub-3 forma. Tygodniowo: 44 km T1 plan vs ~54 km wykonane + walk 4.7 = **+25%** ale Achilles tolerował 271m gain. T2 startujemy z mocnej bazy.
- URL: https://www.strava.com/activities/18524428624

### 2026-05-17 (nd) — siła w ogródku **1h mocno**
- **Siłownia 1h** (potwierdzone przez Tomasza 18.05): hantle 7.5/5 kg + bodyweight
- Następnego dnia: DOMS w nogach
- T1 zakończony — łączny km tygodnia: **~54 km run + ~5 km walk = 59 km** (plan 50 km, **+18%**)

---

## T2 — RECOVERY+ (60 km, 18–24.05.2026)

## T3 — REENTRY (75 km, 25–31.05.2026)

### 2026-05-31 (nd) — T3.nd **LONG 24.80 km** ⭐ (drugi BEST sezonu!)
- Morning Run: **24.80 km @ 5:37/km**, HR **128**/147, suffer **138**
- Elev gain **307m** (rolling terrain)
- **Quartile HR: 125/128/127/131 → drift +6 bpm**
- **0 strap spikes** (HR>=170: zero) = perfect clean data
- HR max 147 = NIGDY nie wszedł w Z4 (cap 146). Pełna Z2/Z3 control.
- Pace dist: 11% <5:00, 27% 5:00-5:30, 35% 5:30-6:00, 26% 6:00-7:00 = progresywny
- Plan T3.nd = 22km HR<130 drift<5. Wykonano: 24.80km HR 128 drift +6 (delicate over).
- **Komentarz:** ⭐ drugi najlepszy long w sezonie (po 27km nd 24.05 z drift -10). Forma sub-3 utrwalona po 6 tyg od Wiednia. Drift +6 bpm na 24.80km z 307m elev = elite aerobic + thermal control. T3 zamknięty mocno.
- URL: https://www.strava.com/activities/18723731808

### 2026-05-30 (sb) — T3.sb: 10.87 km + krótkie sprinty
- Morning Run: **10.87 km @ 5:54/km**, HR **133**/198 (strap spike Q1), suffer 73
- Elev gain 84m
- **2 fast accelerations**: 7s/35m @ 3:01/km + 5s/23m @ 3:18/km (HR 144)
- Real Quartile HR (po wykluczeniu Q1 spike): 129/131/125 = drift ~−4 bpm
- Plan T3.sb = 8km + 6×6s hill sprints. Wykonano 10.87km + ~2 krótkie sprinty (lub plan 6 ale ledwo wykryte).
- **Komentarz:** ✅ akceptowalna shake-out. HR avg 133 = lekko wyższe niż T2 baseline (125-128) — po cumulative T3 (4 siły + VO2max + 21km + rower 56km). Sprinty TODO sprawdzić w urządzeniu (Garmin laps). Achilles bez bólu = OK.
- URL: https://www.strava.com/activities/18710099543

### 2026-05-29 (pt) — T3.pt: siła w ogródku 1:20 💪 + rower commute x2 🚴
- **Siła w ogródku 1:20** (rozszerzona vs 22.05/25.05 — więcej serii)
  - Bazowy układ: przysiady 1-nóż + bułgarskie + przysiady dwunóż + lunge walk + jaskółki
  - **+ DODATKOWO ŁYDKI 3×20/nogę na schodku z oparciem** — eccentric heel raises = **klasyczny modified Alfredson dla Achillesa**
  - Klasyczny core (3×1:30 plank front+P+L) + rozciąganie
- **Morning Ride: 27.88 km / 78 min / HR 124 avg (max 169) / Z2** + **Afternoon Ride: 28.48 km / 120 min / HR 91 (Z1) / suffer 19** = total 56.4km rower
- Plan T3.pt po korekcie = REST. Wykonano: siła + rower x2 commute.
- **Komentarz:** 🎯 dodatek łydek (3×20/nogę eccentric) to **defensywne ćwiczenie dla Achillesa insertional** — dokładnie modified Alfredson (do neutralnej, NIE pod krawędź). Po 240m elev hill reps + 27km long + 21km easy + VO2max = tendon load wysoki, calf eccentrics dziś = inteligentna prewencja. ⚠️ ALE: to **4-ta siła w 13 dni** (17.05, 22.05, 25.05, 29.05) — intensywność z gym też trzeba sprawdzać. Sobota plan = sprints + easy. Niedziela long 22 km. Achilles monitoring obligatory.

### 2026-05-28 (cz) — CROSS-TRAINING: rower commute x2 🚴 ✅
- **Morning Ride: 27.31 km / 72 min / HR 118 (Z1-Z2!) / +199m**, avg 22.8 km/h
- **Afternoon Ride: 28.94 km / 105 min / HR 108 (Z1!) / max 147**, powrót z pracy
- Total: **56.25 km na rowerze**, HR avg ~113 = pure recovery zone
- Plan T3.cz po korekcie = REST/easy max 8km. Wykonano: rower x2.
- **Komentarz:** ✅ idealne T3.cz po 3 dniach intensywnych. HR 108-118 = czysty Z1-Z2, Achilles bezpieczny, aerobic base mileage bez impactu. Pattern recovery via rower utrzymany.

### 2026-05-27 (śr) — T3.śr **21.09 km LONG-EASY** ⭐ (zamiast hill repeats)
- Morning Run: **21.09 km @ 5:46/km**, HR **129**/167, suffer **125**
- Buty: g30955520
- Elev gain **300m**
- **Quartile HR: 129/128/129/130 → drift Q4-Q1 +1 bpm = ELITE** 🔥
- Pace distribution: 30% w 5:30-6:00, 35% w 6:00-7:00 = healthy easy
- 0 strap spikes — perfect data
- **Komentarz:** Plan T3.śr = HILL REPEATS 6×140m. Tomasz: 21km easy zamiast. Hill workout faktycznie zaliczony już 21.05 (20× hill reps). Drift +1 bpm na 21km z 300m elev **dzień po 12×150 VO2max + 2 dni po sile** = absolutnie elite recovery + aerobic engine. Forma sub-3 trzyma się od 24.05 (27km drift -10).
- URL: https://www.strava.com/activities/18670491286

### 2026-05-26 (wt) — T3.wt **12×150 @ 3:01-3:17/km** ⚡ (VO2max session)
- Morning Run: **13.67 km @ 6:18/km avg**, HR **139**/194 (strap spike), suffer **147**
- Buty: Pegasus Plus (g30955507)
- Elev gain ~140m
- **12 × 150m intervals:**
  - **Avg dist: 123m (range 117-127m), avg dur: 24-25s**
  - Pace progression: rep 1 @ 3:17 → rep 11 @ 3:04 (escalating)
  - **Najszybszy chwilowy: 2:46/km** (rep #8!)
  - **HR ramping: 134 → 162 (rep 1 → 11), max 171 (94% HRmax = Z5)**
  - **Drift Q4-Q1: +2 bpm** (vs +10 z 18.05 = BETTER kontrola)
- **Komentarz:** Plan T3.wt = easy 10 + 4×100m strides @ ~3:30. Wykonano: **12×150 @ avg ~3:08/km z escalating HR**. To NIE strides — to **klasyczny VO2max session**. Plan T4 zakładał pierwsze VO2max — wykonano 2 tygodnie za wcześnie. Pozytyw: kontrola lepsza niż 18.05 (drift +2 vs +10), pace escalating (smart pacing), HR adekwatny. Po sile pn + VO2 wt → środa miała być hill, ale Tomasz dał long easy 21km = recovery active.
- URL: https://www.strava.com/activities/18656364502

### 2026-05-24 (nd) afternoon — Walk 9 km
- Afternoon Walk: 8.99 km / 122 min / HR 83 (chodzenie)
- Po długim 27km long w rano. Active recovery z kimś (lub solo).

### 2026-05-25 (pn) — siła w ogródku 1h+ 💪 (NIE rest!)
- **Siła w ogródku 1h+**: ten sam układ jak 22.05 (single-leg focus, hantle 5kg)
  - Przysiady jednonóż na schodku 4×10/nogę
  - Bułgarskie 3×10/nogę
  - Przysiady dwunóż 3×20
  - Lunge walk 4×30 kroków
  - Jaskółki 4×10/nogę
  - Deska front/P/L 3×1:30
  - Stretching
- Plan T3.pn = REST (po 27km long). Wykonano: siła zamiast.
- **Komentarz:** trzecia siła w cyklu (17.05 → 22.05 → 25.05) = **2×/tydzień teraz**. Pattern wariant C trwa, ale konsekwentny i strukturalny (single-leg focus). Po 27km long z drift −10 bpm + 6h sen post-long = body ready. ⚠️ Sprawdzić Achillesy palcem rano — po 240m elev na hill reps + 335m na long + teraz siła ekscentryczna = obciążenie tendonów. Jutro wt easy 10km z 4×100m strides plan.

### 2026-05-24 (nd) — T2 LONG ⭐ **27.38 km** — outstanding!
- Morning Run: **27.38 km @ 5:38/km**, HR **131**/199 (spike), suffer **163**
- Buty: g30955581
- Elev gain **335m** (rekord T2)
- **Quartile HR: 139 / 127 / 128 / 129 → drift NEGATYWNY −10 bpm** 🔥
- Pace distribution: 66% czasu w Z2 (5:00-6:00/km), 24% w Z2 (5:00-5:30), 32% (5:30-6:00)
- Spike HR 359 punktów ≥180 w pierwszych 8 min = **strap glitch warm-up**, real max pewnie ~165-170
- **Komentarz:** **najlepszy long sezonu**. Plan zakładał 18-22 km, wykonano 27.38 (+24%). Negatywny drift −10 bpm na 27km = sub-3 forma faktycznie wróciła. Q1 HR 139 = strap glitch artifact; od Q2 zaczął się real running HR 127-129 = elite Z2. 335m elev na 27km = pofałdowany teren. Pattern wariant C dalej (przekroczenie planu), ale **rezultat doskonały** — ciało reaguje świetnie. Jutro pn pewnie REST (lub łatwy spacer max).
- URL: https://www.strava.com/activities/18629806885

### 2026-05-23 (sb) — Morning HIKE 🥾 (zamiast REST!)
- Morning Hike: **15.7 km @ 17:33/km** (4h 35min moving, 8h elapsed)
- HR avg **77** / max 113 = chodzenie/lekki hike
- Elev gain **+401m** (góry!)
- 2 osoby (athlete_count=2) — z kimś szedł
- Plan T2.sb = REST (i ja pisałem "OBOWIĄZKOWE REST"). Wykonano: 4h 35min hike w górach.
- **Komentarz:** ⚠️ to NIE jest REST. 15.7 km / 4h+ time-on-feet / +401m elev = dodatkowa praca, mimo niskiego HR. Bezpieczne dla Achillesa (chodzenie, nie bieg), ale przed niedzielnym long (27 km!) to akumulacja. Mimo to: drift −10 bpm na long pokazuje że ciało dało radę. Pattern: Tomasz NIE wykonuje "true REST" — zawsze coś robi. Z perspektywy planu: warto przestać planować REST i zamiast tego planować **cross-training (hike/rower)** explicit — wtedy mniej zaskoczenia.
- URL: https://www.strava.com/activities/18623416159

### 2026-05-22 (pt) — siła w ogródku 1h 💪 (single-leg + glute + core)
- **Siła w ogródku 1h** (hantle 5 kg każda + bodyweight + schodek + huśtawka):
  1. **Przysiady jednonóż na schodku z hantlami**: 4×10/nogę = **80 reps single-leg**
  2. **Bułgarskie split squats na huśtawce z hantlami**: 3×10/nogę = **60 reps single-leg**
  3. **Przysiady z hantlami (dwunóż)**: 3×20 = **60 reps**
  4. **Lunge walk z hantlami w wykroku** (kolana prawie do ziemi = pełny ROM): 4×30 kroków = **120 kroków**
  5. **Jaskółki z hantlami** (single-leg deadlift): 4×10/nogę = **80 reps single-leg**
  6. **Plank frontal**: 1:30
  7. **Plank boczny prawo**: 1:30
  8. **Plank boczny lewo**: 1:30
  9. Rozciąganie
- **Total**: 220 reps single-leg + 60 dwunożnych + 120 kroków lunge + 4:30 plank
- **Komentarz:** ✅ **idealne workout dla biegacza 51L post-Achilles**: glute medius/maximus dominance + single-leg stability (korekcja asymetrii post-9 tyg przerwy) + posterior chain + core anti-rotation. To NIE jest "lekka siła" — 220 reps unilateralnych z hantlami = poważny stimulus. Wszystko ekscentryczne dominant = Achilles-friendly. Druga siła w T2 (po 17.05 też 1h). Sobota REST obowiązkowe.

### 2026-05-21 (cz) — T2 sesja 4, **HILL REPS** 🏔️ (T3 wykonany 4 dni za wcześnie!)
- Morning Run: **13.70 km @ 6:14/km**, HR **140**/174, suffer **156** (najwyższy w T2)
- Buty: g30955581 (nowe? sprawdzić)
- Elev gain **240m** (po Wiedniu rekord T2)
- **~20 hill repeats w sekcji km 7-12 (forest hills, continuous loop):**
  - Średnia długość: **110m** (range 95-137m)
  - Średni czas: **32s** (range 28-39s)
  - Najszybszy pace (chwilowy): **3:44/km**
  - Najszybszy avg w rep: 4:08/km
  - Najwolniejszy avg w rep: 5:09/km
  - **Średnie nachylenie: 7.5%** (max chwilowo 15.2%)
  - HR avg/rep: **152** (Z4 threshold), HR max: 171 (94% HRmax = Z5)
  - Total elev w samych reps: 193m
- **Komentarz:** T3 plan zakładał **6×140m hill repeats** w środę 27.05. Tomasz zrobił **3.3× więcej (20 reps)** już dziś — ale każda krótsza (32s vs ~50s planowanych). HR 152 = Z4 próg = stymulus wytrzymałości progowej + power. ⚠️ **Achilles risk**: 20 podbiegów + 193m elev w reps = duża objętość ekscentryczna jeśli zbieg biegiem. Sprawdzić palcem rano w insertion! T3 hill workout zalicza, ale T3 środa wymaga korekty (nie powtarzać hill repeats za 6 dni — Achilles potrzebuje regeneracji).
- URL: https://www.strava.com/activities/18591006066

### 2026-05-20 (śr) — CROSS-TRAINING: rower x2 🚴 ✅
- **Morning Ride**: 27.29 km / 82:32, HR avg 104, elev +195m, suffer 20
- **Afternoon Ride**: 29.35 km / 116:00, HR avg 94, elev +257m, suffer 20
- Total: **56.64 km na rowerze**, ~720 kJ
- Tomasz: "relaksik"
- **Komentarz:** ✅ idealny T2.3 po wczorajszym easy clean. Cross-training aerobic bez impact, HR avg 99 (Z1 recovery) = pure aerobic base. Plan zakładał REST/walk — rower lepszy (większy stimulus przy zero leg impact).

### 2026-05-19 (wt) — T2 sesja 2, easy clean ✅
- Morning Run: **10.76 km @ 5:50/km avg**, HR **125**/152, suffer 54
- Buty: Pegasus Plus
- Elev gain 118m
- **Quartile HR: 116 / 130 / 129 / 126** — slow start, settled, cool down (NIE drift cumulative)
- **Zero fast spikes** (0% pace <4:00/km) = czysty easy
- **Komentarz:** ✅ korekta T2 wykonana. HR avg 125 (vs wczoraj 138 = −13 bpm), suffer 54 (vs 126 = −57%), żadnych intervalów. Plan: cd. tygodnia jak w viewerze (śr REST/walk, cz easy 10, pt 8 recovery, sb REST, nd long 18-22).
- URL: https://www.strava.com/activities/18563580777

### 2026-05-18 (pn) — T2 sesja 1, **"easy + 10×150m"** ⚠️
- Morning Run: **11.78 km @ 6:06/km avg**, HR **138**/174 (Z3/Z5 spikes), suffer **126**
- Buty: Pegasus Plus (g30955507)
- Elev gain 144m
- **10 × 150m repeats** (pace 3:02-3:20/km, średnio 3:13/km):
  - Rep 1-3: HR 147→154, pace 3:13-3:20 (rozgrzewka)
  - Rep 4-7: HR 145-158, pace 3:08-3:15 (stabilnie)
  - Rep 8-9: HR 160-162, pace 3:02-3:15 (peak speed, 93% HRmax!)
  - Rep 10: cool down
- **Quartile HR**: 133/133/144/144 → drift **+10 bpm** (vs +1 z 21km T1)
- Tomasz: "czuję nogi po wczoraj" (DOMS po siłowni 1h)
- **Komentarz:** plan T2 = easy + strides max. To NIE strides, to **VO2max session** (HR max 174 = 95% HRmax = Z5). Pattern wariant C powtarza się — siłownia 1h → DOMS → "rozruszanie" zamieniło się w hard speed work. HR easy 138 vs T1 baseline 125 = +13 bpm = znak fatigue. Cumulative load (Wiedeń 19.04 → T1 +25% volume → siła 1h → speed work) zaczyna kosztować.
- **Wniosek dla T2:** twardszy reset. Reszta tygodnia = TYLKO easy ≤6:00/km, HR ≤130. Bez strides do końca tygodnia.
- URL: https://www.strava.com/activities/18551034592

<!-- 5 sesji easy + strides + drills. -->

---

## Markery do śledzenia

- **Easy pace przy HR 120–125:** powinien spadać z czasem (np. 6:00 → 5:50 → 5:40 przy tym samym HR = poprawa ekonomii)
- **HR drift na long (>15 km):** różnica HR pierwsza vs ostatnia ćwiartka — < 5 bpm = OK, >10 bpm = fatigue / undertraining
- **HR po hill sprintach / VO₂max szczyt:** powinno być w Z5 (164–182), spadać szybko między reps
- **Resting HR rano:** jeśli notujesz, dorzucaj — wzrost o 5+ bpm vs baseline = zmęczenie / choroba zbliżająca

---

## Statystyki tygodniowe

| Tydzień | Plan km | Wykonanie km | Sesji plan | Sesji wyk. | Avg HR easy | Notatki |
|---|---|---|---|---|---|---|
| W14 cz. | – | 44.1 | – | 2 | – | baseline |
| W15 | – | 91.4 | – | 5 | – | peak taperowy + 3×5K hard |
| W16 | – | 66.5 | – | 3 | – | maraton Wiedeń 3:11 |
| W17 | – | 63.3 | – | 4 | – | wariant C, post-race |
| W18 | – | 78.7 | – | 5 | – | 2 hard sessions, fatigue |
| W19 (do śr) | – | 26.7 | – | 2 | – | quality 06.05 → Ryga skreślona |
| Pre-T1 | ~30 | – | 4 | – | – | – |
| T1 | 50 | – | 5 | – | – | – |
| T2 | 60 | – | 5 | – | – | – |
