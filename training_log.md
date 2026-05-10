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

## T1 — RECOVERY (50 km, 11–17.05.2026)

<!-- 5 sesji easy, zero akcentów. HR cel: Z1–Z2 (max 127). -->

---

## T2 — RECOVERY+ (60 km, 18–24.05.2026)

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
