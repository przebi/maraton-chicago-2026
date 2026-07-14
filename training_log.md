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

## T10 — PEAK SPECIFICITY (95 km, 13–19.07.2026)

**Kontekst wejścia:** T9 zamknięte DWOMA jakościami (07.07 próg 2×3 km + 12.07 signature 2×5 km, oba w carbonie, negative split). Plan T10 = signature peak **4×4 km progres** + VO2 alt + LR 32 km z 10 km MP.

**⚠️⚠️ MARKERY 13-14.07 (Garmin, pobrane 14.07) — CZERWONE:**
- **HRV noc 12→13.07 = 38** (!) = poziom crashu z 28.06. weeklyAvg 48, status UNBALANCED (balancedLow 49, lowUpper 45 → 38 głęboko w „low").
- **Readiness 13.07 = 3/100 POOR** „TIME_TO_SLOW_DOWN / POOR_HRV_UNBALANCED", recovery debt 2260 min (37 h), sleepScore 57 POOR.
- **Readiness 14.07 = 12/100 POOR** „TIME_TO_SLOW_DOWN", recovery debt 2448 min (**40 h**), sleepHistory POOR 39%, acuteLoad 1319 (wysoki).
- HRV noc 13→14.07 = 48, **14.07 = 49** (wróciło do balancedLow w ~1 dobę). Sen tydzień 6:30-7 h **+ drzemka min 30 min = 7-7,5 h/dzień** (POWYŻEJ baseline 6,2). weekly 48.
- **Diagnoza Tomasza (14.07, przyjęta):** „problem to nie HRV tylko waga + brak treningu na tempie". Zgoda — regeneracja adekwatna, HRV nie limituje. Realne dźwignie: (1) **waga 64→61-62**, (2) **deficyt TEMPA ciągłego** (robi progresje/interwały VO2, prawie zero sustained threshold 4:05-4:10). Kierunek planu: mniej progresji-do-3:35 (spiky, drogie), więcej ciągłego tempa MP/próg.
- **Wniosek (skorygowany — NIE crash):** 38 to był **ostry dip PO akcencie 12.07** (signature TRIMP 201), odbił do 49 w dobę = **zdrowa rezyliencja autonomiczna**, nie zapaść. To ≠ 28.06 (tam HRV 38 ZOSTAŁO nisko, 7-dn 43, RHR ↑, sen 5,7). Tomasz słusznie: „HRV spada po akcencie" — prawda, liczy się szybkość odbicia (tu OK). **Realny (łagodny) problem:** dług regeneracyjny z **3 twardych/8 dni** (readiness lag: POOR 12/100 na 14.07 mimo HRV 49) → dlatego 7×1 km „bolało jak śmierć" choć nie ma crashu. **Ścieżka:** śr/czw naprawdę easy → sobota 12k@4:10 warunkowo (HRV utrzyma ≥49). Bez alarmu, ale bez 4. twardej przed sobotą.
- Waga: **64 kg (14.07, podane przez Tomasza)** = BMI 21,4, **+3 kg vs waga startowa 61 kg** (Hannover 2:59, wiosna 2025). Cel −2/−3 kg do 61-62 jest ZASADNY (powrót do race weight, ~2-3 s/km/kg ekonomii). ALE **nie teraz** — deficyt przy HRV 38/readiness POOR dobija regenerację. Metoda: powolne cięcie (≤0,4 kg/tydz) w blokach easy, białko-forward, PEŁNE dojadanie wokół jakości. Nie na crashu.

### 2026-07-13 (pon) — T10.pn recovery easy 11.45 km @ 5:55 ✅
- 11.45 km @ 5:55/km, HR avg **128 (Z2)** / max 159, elev 96 m, **Pegasus 42** (trainer), effort 63, kadencja 96.
- Struktura (lapy): km 1-8 czysty easy HR 116→130 (settled ~127), km 9-10 HR 133→138 (max 159 = kilka lekkich przyspieszeń/strides na końcu), km 11 cool.
- Komentarz: wzorowy recovery po sobotnio-niedzielnym double quality. HR 128 = dyscyplina easy trzymana, buty trainer. Mądry dzień przed jakością. ✅
- URL: https://www.strava.com/activities/19289949012

### 2026-07-14 (wt) — T10.wt **PROGRESJA 7×1 km @ 4:02 → 3:35** ⭐⭐⭐ (14.91 km) — speed-endurance
- 14.91 km total @ 5:30 avg, HR avg 146 / **max 179 (98% HRmax)**, elev 4 m (płasko), **Adios Pro 4** (race), effort 178, kadencja 96.
- Struktura (lapy): WU 3.08 km @ ~5:52 (HR 139) → **7×1 km progresywne z krótkim floatem (0,4-0,6 km):**
  | Rep | Pace | HR avg | Power |
  |---|---|---|---|
  | 1 | 4:02 | 161 | 325 W |
  | 2 | 3:59 | 164 | 333 W |
  | 3 | 3:53 | 166 | 346 W |
  | 4 | 3:49 | 168 | 355 W |
  | 5 | 3:44 | 169 | 361 W |
  | 6 | 3:41 | 170 | 365 W |
  | 7 | 3:35 | 169 (max 178) | 368 W |
  - CD 1.84 km @ ~7:24 (HR 127).
- **Komentarz:** ⭐⭐⭐ czysta **wytrzymałość prędkościowa** — dokładnie zidentyfikowana słabość. Idealna progresja: każdy rep ~4-5 s/km szybszy, zero fade, ostatni **3:35/km** = mocno pod sufitem prędkościowym (~3:46 baseline 06.05), power ciągle rośnie 325→368 W. HR 161→170 (LTHR 169), max 179 = próg/VO2 dolny — kontrolowane, nie all-out. **Świetny wskaźnik formy.**
  ⚠️ **ALE (pattern):** to **TRZECIA jakość w 8 dni** (07.07 próg + 12.07 signature + 14.07 progresja). Plan T10.wt to była raczej signature 4×4K LUB VO2 — a signature Tomasz zrobił już 12.07. To 1 km reps = VO2/speed, więc nie duplikat, ale **gęstość intensywności wysoka** po dopiero co zamkniętym bloku regeneracyjnym T8 (HRV crash 28.06). Korekta z 09.07 (1 twarda/tydz do odbicia HRV) systematycznie przekraczana — „nogi proszą".
  **Wniosek:** forma rośnie realnie (3:35 to najlepszy sygnał od Wiednia). Ale **fatigue-monitoring priorytet #1**: sprawdzić HRV/RHR/readiness (Garmin) gdy wróci sesja. Jeśli HRV trzyma ≥49 → jedziemy, ale kolejne 2-3 dni MUSZĄ być easy + LR (bez trzeciej intensywności). Jeśli <47 → wymuszony reset, bo 3 twarde/8 dni po crashu to za dużo.
- URL: https://www.strava.com/activities/19303780649

## T9 — SPECIFICITY BUILD (6–12.07.2026)

**Kontekst (fatigue, Garmin 09.07):** HRV wraca po dnie 28.06 (noc 38) — trend noc: 30.06 **51** / 01.07 51 / 02.07 48 / 03.07 42 / 05.07 45 / 07.07 48 / 08.07 47 / **09.07 53**; 7-dn stabilne **47** (balanced low ~49, status UNBALANCED, ale trend ↑). Readiness 09.07 = **63 MODERATE** ("LISTEN_TO_YOUR_BODY"): recovery 99% / ACWR 97% (acuteLoad 783) / stress 92% — wszystko GOOD; hamują tylko HRV 58% (MOD) + sleep-history 51% (MOD, dług skumulowany). Sen 08→09.07 = 6,6 h / score 80 GOOD, body battery +60 rano. **Zero czerwonych flag → żaden auto-reset.** Powrót jakości od 02.07 (jeszcze w T8) udźwignięty — HRV nie zapadło.

### 2026-07-07 (wt) — T9.wt **PRÓG 2×3 km @ 4:03 / 3:56** ⭐ (10.01 km)
- 10.01 km total @ 4:52 avg, HR avg 150 / max 178, elev 7 m, **Prime X**, effort 123.
- Struktura (lapy): WU 2.95 km @ ~5:44 (HR 134) → **3.02 km @ 4:03** (HR 170) → rec 0.94 km (HR 129) → **3.01 km @ 3:56** (HR 167) → 0.09 km stop.
- Komentarz: solidny próg cruise. Pace 3:56–4:03 = okolice progu (LTHR 169; HR 167–170 = lekko nad). Płasko (7 m). ⭐
- URL: https://www.strava.com/activities/19209922117

### 2026-07-08 (śr) — T9.śr recovery 8.60 km @ 6:32 ✅
- 8.60 km @ 6:32/km, HR avg **123 (Z2 dolny)** / max 139, elev 65 m, **Pegasus 42**, effort 34.
- Komentarz: wzorowy recovery po progu z wt. HR 123 = czysty easy, buty trainer. ✅
- URL: https://www.strava.com/activities/19223942879

### 2026-07-09 (czw) — T9.czw SIŁA + spacer 6.19 km 💪🚶
- Bez biegu. Afternoon Walk **6.19 km**. Plan = SIŁA ogród 1,5 h przy HRV UNBALANCED (umiarkowanie, nie ciężki leg-day). **Do potwierdzenia: czy siła wykonana i jak ciężka** (30.06 heavy leg-day przygasił odbicie HRV).

### 2026-07-10 (pt) — T9.pt LONG easy 21.41 km @ 5:49 ✅ (long przeniesiony z nd)
- 21.41 km @ 5:49/km, HR avg **129 (Z2)** / max 164, elev 196 m, **Pegasus Plus**, effort 131, kadencja 95.
- Plan: easy 10-12 km + strides. Wykonanie: **long 21,4 km** (≈2× planu). HR 129 dyscyplina easy OK (cel <127, +2 kosmetyka). Buty trainer. De facto przełożył niedzielny long na piątek → uwolnił niedzielę.
- URL: https://www.strava.com/activities/19251466877

### 2026-07-11 (sob) — T9.sob easy 9.35 km @ 5:59 ✅
- 9.35 km @ 5:59/km, HR avg **135 (Z2)** / max 176 (kilka strides/spike), elev 68 m, **Pegasus 42**, effort 80.
- Plan: easy 12-14 km + strides. Wykonanie: 9,35 (krócej). Czysty easy dzień przed jakością. ✅
- URL: https://www.strava.com/activities/19263712894

### 2026-07-12 (nd) — T9.nd **SIGNATURE 2×5 km progresywne @ 4:04 / 3:58** ⭐⭐⭐ (15.20 km) — DRUGA jakość T9
- 15.20 km total @ 4:50 avg, HR avg 153 / max 178, elev 3 m (płasko), **Prime X2 Strung** (carbon race), effort **201**, kadencja 97.
- Struktura (lapy):
  - WU 3.04 km @ 5:31 (HR 138)
  - **REP 1 = 5 km progres: 2 km @ 4:08 (164) + 2 km @ 4:05 (171) + 1 km @ 4:01 (173)** → avg ~4:05, HR 164→173
  - float 0.97 km @ 7:13 (131)
  - **REP 2 = 5 km progres: 2 km @ 3:58 (169) + 2 km @ 4:00 (169) + 1 km @ 3:56 (174)** → avg ~3:58, HR 169→174, **max 178**
  - CD 1.15 km @ 7:35 (123)
- **Komentarz:** ⭐⭐⭐ **to jest signature workout** (3-4×4-5K progresywne z floating recovery — wzorzec peak 2024/HM 1:24). Dwa 5-km repy, **rep 2 szybszy niż rep 1** (negative, 3:58 vs 4:05) = zero fade = mocna wytrzymałość prędkościowa (dokładnie zidentyfikowana słabość!). Pace 3:56-4:08 = **szybciej niż MP cel 4:08-4:12**, HR 173-178 (LTHR 169 +4-9) = próg/VO2 dolny. Power 316-339 W ciągłe. **Świetny wskaźnik formy.**
  ⚠️ **ALE:** plan nd był **LR 26-28 km easy z finishem 4:45-4:55** — NIE full-quality. Tomasz zrobił zamiast tego twardy próg w carbonie → **2. twarda sesja T9** (07.07 próg + 12.07 signature), a korekta 09.07 mówiła explicite **1 twarda, signature → T10**. Pattern „wariant C" (nogi proszą → easy/LR zamienia się w hard) powtarza się. Long aerobowy 26-28 km wypadł (zamieniony na intensywność).
  **Wniosek:** forma NA TAK — speed-endurance rośnie widocznie. Fatigue-koszt: **sprawdzić HRV rano 13.07** — jeśli trzyma ≥49 → double-quality udźwignięty, jedziemy T10 z jakością bez straty. Jeśli spadnie <47 → 2 twarde w tyg po bloku regeneracyjnym były o jedną za dużo, T10 startuje easy.
- URL: https://www.strava.com/activities/19277008158

---

## T8 — REGENERACJA (HRV recovery) + SPECIFICITY (29.06–05.07.2026)

**Kontekst:** 28.06 Garmin markery w czerwieni (HRV noc 38 / 7-dn 43 vs baseline 55-58, RHR 51-52, readiness 1/100 „POOR", sen ~5,7 h). Sygnatura przed-crashowa (post-Chicago było HRV 40/RHR 54). T8 = blok regeneracyjny: sen + easy/basen, ZERO jakości aż HRV wróci >48-50. Root wg Tomasza = sen (budzenie 3-4 + brak resleep), nie trening — potwierdza readiness (ACWR „GOOD", POOR = HRV+sen). Ścieżka: CBT-I ± celowany lek (specjalista snu).

### 2026-06-29 (pn) — T8.pn REST od biegu (2. dzień przerwy)
- Bez biegu. Regeneracja / odespanie (drzemki 1,5 h + 50 min). HRV recovery.

### 2026-06-30 (wt) — T8.wt **SIŁA leg-day (ciężka)** 💪 (bez biegu)
- Leg press **4×10×165 kg (full stack!)**, leg curl + leg ext 4×10×70, sitting calf 4×10×40, marsz wykroczny 4×25 ×20 kg, przysiady ze sztangą 4×10×50 (praca nad TECHNIKĄ: gryf → małe obciążenie, „kolosalna różnica"). Potem sauna.
- **Komentarz:** ✅ **plecy nazajutrz ciche** — poprawa formy squata zadziałała (ból był z formy, nie ciężaru; leg press 165 przy 61 kg = ~2,7× BW = mocarz). ⚠️ Zrobił mimo zaleceń wykroki + squaty (squat teraz z lepszą formą = OK z kontrolą; **wykroki dalej odradzam** — dorsiflexion na Achilles). ⚠️ Duży leg-day w dzień HRV-recovery = **może przydusić HRV** (sprawdzić rano). Lekcja: „8-10 nie męczy" = OK dla biegacza (siła≠burn); jeśli brak wyzwania → za lekko (test „2 w zapasie" + wolny eccentric).

### 2026-07-01 (śr) — T8.śr easy 12.14 km @ 6:08 + 7× strides ✅ (powrót po przerwie)
- 12.14 km @ 6:08/km, HR avg **131 (Z2)** / max 169 (strides), elev 102 m, **Pegasus 42** (Strava błędnie pokazała PrimeX2), + **7×~100 m strides**, start 5:09.
- **Komentarz:** wzorowy easy powrót po 2 dniach przerwy — HR 131 na 6:08 = normalne easy (chłodniej + odpoczynek vs 133.7 w upale 28.06). Buty trainer (nie carbon) = dobrze pod easy + Achilles. Strides = lekki neuromuscular touch, nie rusza HRV-recovery. ✅
- URL: https://www.strava.com/activities/19132520692

### 2026-07-02 (czw) — T8.czw **PRÓG 2×4 km @ 3:58→3:52** ⭐⭐ (13.00 km) — powrót jakości
- 13.00 km total @ 4:54 avg, HR avg 146 / max 179, elev 12 m, **Adios Pro 4**, effort 136.
- Struktura (lapy): WU 3.02 km @ ~5:39 (HR 121) → **4 km ciągłe (2×2 km): 3:58 / 3:57** (HR 166→175) → rec 0.75 km (HR 126) → **4 km ciągłe: 3:55 / 3:52** (HR 169 / 169) → CD 1.15 km (HR 124).
- Komentarz: ⭐⭐ de facto signature cruise T9 (cel 4×4K @ 3:58) — **i pobity** (3:52–3:58). HR do 175 (LTHR 169 +) = próg/VO2 dolny. **ALE: jakość 4 dni po czerwonej fladze HRV (28.06 noc 38).** HRV rano 02.07 = **48** = dokładnie próg „>48–50" z planu regeneracji → powrót borderline-uzasadniony, nie lekkomyślny. HRV po sesji się NIE zapadło (03.07 noc 42, 7-dn stabilne 47). Buty carbon (Adios Pro 4).
- URL: https://www.strava.com/activities/19145974720

### 2026-07-03 (pt) — T8.pt LONG easy 21.13 km @ 5:34 ✅
- 21.13 km @ 5:34/km, HR avg **133 (Z2–Z3)** / max 198 (**spike** — HRmax realne 183), elev 182 m, Nike Air Zoom Tempo Next%, effort 156.
- Komentarz: aerobowy long dzień po progu — HR 133 = dyscyplina easy OK. Max 198 = artefakt czujnika (ignore).
- URL: https://www.strava.com/activities/19159151257

### 2026-07-05 (nd) — T8.nd LONG easy 20.40 km @ 5:33 ✅ (zamyka T8)
- 20.40 km @ 5:33/km, HR avg **135 (Z2–Z3)** / max 198 (spike), elev 272 m, Pegasus Plus, effort 158.
- Komentarz: drugi long w 3 dni (21.13 + 20.40 = 41,5 km) — solidna dawka aerobowa, HR 135 kontrolowane. Domyka blok regeneracyjny T8. + spacer 04.07 3,33 km.
- URL: https://www.strava.com/activities/19184310867

## T7 — SPECIFICITY START / POWRÓT JAKOŚCI (22–28.06.2026)

### 2026-06-23 (wt) — T7.wt **THRESHOLD 8 km @ ~4:00/km** ⭐⭐ (powrót intensywności) — Achilles do potwierdzenia
- 17.49 km total @ 5:03/km avg, HR avg 140 / max **174**, **Adios Pro 4**, suffer 154
- Struktura: ~4 km WU (HR 114-123) → **8 km ciągłego @ ~4:00/km** (HR 153→163→167→171→173→174, power ~340 W, kadencja 100-103) → ~5,5 km CD (HR 127-133)
- **Komentarz:** ⭐ **mocna sesja progowa.** 8 km @ 4:00/km, HR do 174 (= LTHR 169 / lekko nad). **Świetny wskaźnik formy** — 4:00/km SZYBCIEJ niż MP cel 4:08-4:12, utrzymane 8 km. Bezpośrednio kasuje strach „stracę prędkość / 5:00" sprzed kilku dni. ⚠️ **ALE to dokładnie ten threshold, który miał czekać do ciszy gauge'a Achillesa.** Jakość wróciła — kluczowe: czy przyczep był cichy przed i jak zareagował po? Cicho → de facto cleared, jedziemy T7 z intensywnością. Boli → przesadzone. **Czekam na status Achillesa.**
- URL: https://www.strava.com/activities/19030976195

### 2026-06-24 (śr) — T7.śr **SIŁA 1:40 (maszyny + przysiady ze sztangą)** 💪 + spacery ~15 km
- **Siłownia ~1:40** (pierwsza pełna). Maszyny ✓: **leg press (S956), leg extension (S957), leg curl (S959)** — dobrze. Dorzucił (NIE z listy): **marsz wykroczny 20 kg 4×30, przysiady ze sztangą 50 kg 4×10, próba martwego ciągu** (nie umie) → ból dolnego grzbietu nazajutrz.
- Spacery 6.20 + 5.03 + 5.28 = ~15.6 km. Brak biegu. Achilles rano „tylko lekka sztywność".
- **Komentarz:** ⚠️ barbell back squat **NIE był na liście** (beginner-risky dla pleców + deep squat = dorsiflexion pod ciężarem = źle na Achilles). **Korekta: tylko maszyny + hip thrust; zero przysiadów ze sztangą i deadliftów do czasu aż plecy OK.** Ból prawdopodobnie mięśniowy (forma), monitorować red flags (promieniowanie do nogi/mrowienie = lekarz).

### 2026-06-25 (cz) — T7.cz LONG 27.00 km @ 5:38 easy ✅ (Achilles cichnie)
- Morning Run: **27.00 km @ 5:38/km**, HR avg **128.8 (Z2!)**, max 190 (spike na starcie), elev 123 m, kadencja 96.1 (~192 spm), 2:32 h, **Adios Pro 4**, suffer 153.
- **Komentarz:** aerobowo wzorowy long — HR 128.8 = dyscyplina easy A+, drift kontrolowany. Achilles „odpadł" (nie przeszkadza), rano lekka sztywność → udźwignął 27 km easy. ⚠️ buty Adios Pro 4 (carbon) na 27 km easy — bo na wyjeździe ma 1 parę; normalnie trainer lepszy na long. **Objętość wróciła do pełnej (27 km long + wt próg 8 km @4:00) — faza ochronna de facto zamknięta, bo przyczep się wyciszył.** Pilnować poranka.
- URL: https://www.strava.com/activities/19057627266

### 2026-06-26 (pt) — T7.pt siła 1h ogród 💪 (bez biegu)
- Siłownia w ogrodzie ~1h. Bez biegu. (Plan T7.pt = easy+siła → wyszła sama siła.)
- **Komentarz:** OK — recovery po long 27 km z czw. Przypomnienie: bez przysiadów ze sztangą/wykroków (plecy), zostań przy maszynach + hip thrust + izometrie łydki.

### 2026-06-27 (sb) — T7.sb **5×1600 m PROGRESYWNE 3:58→3:38** ⭐⭐ (signature-grade) — płasko
- 15.13 km total @ 5:12 avg (uśrednione), HR avg 152.7 / max **179** (98% HRmax, ostatni rep), elev **3 m**, suffer **210**, PrimeX2.
- **Struktura (lapy — to NIE steady, to interwały):** WU ~3 km → **5×1600: 3:58 / 3:53 / 3:48 / 3:43 / 3:38** (HR rep 166→172, max 179) z ~800 m truchtu (HR→136) → CD ~1,3 km.
- **Ocena:** ⭐⭐ **wzorowa sesja prędkościowo-progowa.** Idealna progresja co ~5 s, finał NAJSZYBSZY (3:38) = pełna kontrola + zapas (3:38 @ HR 171 ≠ max-out). To dokładnie signature/mile-reps — fundament bloku. **3:38/km ≈ ~18:10 pace na 5K** → mocno potwierdza cel 5K 18:30 + sub-2:57. Recovery HR→136 = świetna wydolność. ⚠️ To była JAKOŚĆ (HR do 179) — płasko + kontrolowane repy (nie hill/sprint) = Achilles-OK, ale realny speed → monitoruj przyczep po. **[Korekta: wcześniej błędnie „steady" po samym avg; lapy = interwały.]**
- URL: https://www.strava.com/activities/19080556375

### 2026-06-28 (nd) — T7.nd easy 21.12 km @ 6:01 z Maćkiem 🤝 (Tarnowskie Góry, upał)
- 21.12 km @ 6:01/km, HR avg **133.7** / max 144, elev 172 m, Pegasus Plus, start **04:27**, 2:07 h.
- **Wspólny bieg z Maćkiem** (on 20.89 @ 5:59). Warunki: ~24°C / **74% wilgotności** o świcie.
- **Komentarz:** HR 133.7 @ 6:00 (vs zwykłe ~127) = **podatek cieplno-wilgotnościowy +~6-7 bpm**, NIE utrata formy. Zrobione DOBRZE — max tylko 144, HR prowadził, tempo odpuszczone = wzorowy easy w upale. Resztkowe zmęczenie po quality-tygodniu może dokładać 1-2 bpm → **2 dni przerwy (29-30) w porę**. To był ostatni bieg przed przerwą.
- URL: https://www.strava.com/activities/19093365169

## T6 — DELOAD + OCHRONA ACHILLESA (insertional, 15–21.06.2026)

### 2026-06-15 (pn) — T6.pn **CROSS: 2× rower ~54 km** 🚴 ✅ (Achilles protocol)
- Morning Ride: **27.59 km** / 1:24:50, HR avg **97**/133, 65 W, elev 191 m, suffer 16
- Afternoon Ride: **26.66 km** / 1:48, HR avg **88**/116, 51 W, elev 226 m, suffer 16
- Total **54.25 km roweru**, HR 88-97 = czyste Z1, zero impactu.
- **Komentarz:** ✅✅ **dokładnie wg protokołu Achillesa** — bieg odpuszczony, baza aerobowa na rowerze (zero obciążenia przyczepu). Tomasz posłuchał (po początkowym oporze „forma spadnie do zera"). Wzorowy deload-day.

### 2026-06-16 (wt) — T6.wt brak biegu (rest / off-Strava)
- Brak aktywności w Stravie. Prawdopodobnie rest lub siła/izometrie poza Stravą. Zgodne z protokołem (OFF bieg + izometrie).

### 2026-06-17 (śr) — T6.śr easy 11.49 km @ 5:59 ✅ intensywność / ⚠️ objętość 2×
- Morning Run: **11.49 km @ 5:59/km**, HR avg **129** (Z2)/max 191 (**lap 1 = artefakt paska na zimnym starcie**; laps 2-12 max 129-164), suffer 70
- Buty: **Pegasus 42**, elev **65 m (płasko ✓)**, kadencja 94.6 (~189 spm)
- Splity: równo 5:47-6:41, HR 123-137, **bez driftu** (końcówka 123-127 = spadała). Lap 2 lekko szybszy (5:48/137).
- **Komentarz:** intensywność + buty + płaski profil **wzorowe** (HR 129 Z2, Pegasus 42, 65 m elev = idealnie pod insertional). **ALE plan T6 śr = easy 5-6 km, wykonano 11.5 = ~2× (wariant C).** Easy/flat → strain per km niski, ale to 1. tydzień ochrony przyczepu — liczy się reakcja, nie samopoczucie w trakcie. **Otwarte pytanie: Achilles rano na schodach + po tym biegu?** To jest licznik dawki.
- URL: https://www.strava.com/activities/18952903141

### 2026-06-18 (cz) — T6.cz easy 13.42 km @ 5:57 ✅ intensywność A+ / ⚠️ objętość (plan 8-10)
- Morning Run: **13.42 km @ 5:57/km** + **6×100 m strides** (płaskie, max 20.4 km/h ≈ 2:56/km — lapy 11-12), HR avg **126** (Z2)/max 157 (strides), suffer 73
- **Strides = pierwszy element speed z powrotem** — najłagodniejszy (krótkie, płaskie, kontrolowane). OK przy cichnącym przyczepie, ale to wciąż +strain ścięgna → monitoruj reakcję. Tempo/interwały/podbiegi DALEJ nie.
- Buty: **Pegasus Plus**, elev **78 m (płasko ✓)**, kadencja 95.4 (~191 spm)
- Splity: WU lap 1 HR 95 → ustabilizowane 127-133, **bez driftu** (równo do końca). Czysty Z2.
- **Komentarz:** intensywność wzorowa (HR 126 = pełna dyscyplina). Objętość znów nad plan (13.4 vs 8-10), ALE **easy + płasko + Achilles cichnie** = akceptowalny, wręcz terapeutyczny load (ścięgno goi się przez delikatne obciążenie, nie przez zero). **Korekta trenera: zdejmuję sztywny limit objętości** — easy płaskie km OK wg tolerancji; twarda granica zostaje na INTENSYWNOŚCI (zero tempa/interwałów/podbiegów do ciszy gauge'a). Achilles stanie/gorzej → objętość tniemy pierwsza.
- URL: https://www.strava.com/activities/18966831804

### 2026-06-19 (pt) — T6.pt siła (off-Strava, planowana)
- Siłownia/ogród wg planu (nogi/glute + lekkie seated calf). Brak w Stravie.

### 2026-06-20 (sb) — T6.sb easy 11.62 km @ 5:55 + surge'y ⚠️
- 11.62 km @ 5:55/km, HR avg **139** (Z3 — wyżej niż czysty easy), max 195 (spike artefakt), Pegasus 42, suffer 119.
- Plan: easy 7-10. Wykonano 11.6 z szybszymi fragmentami (max 20.7 km/h = strides/surge). HR 139 = NIE czysty Z2.
- **Komentarz:** lekko ponad „easy 7-10" + akcenty. OK jeśli przyczep cichł — ale to już nie był czysty recovery.

### 2026-06-21 (nd) — T6.nd LONG 19.18 km @ 6:05 easy ✅
- 19.18 km @ 6:05/km, HR avg **131** (Z2/Z3), max 194 (spike), elev 158 m, **Adidas PrimeX2 Strung**, suffer 128. + spacer 9 km.
- **Komentarz:** kontrolowany easy long (HR 131), lekko nad zakresem 14-18. ⚠️ buty PrimeX2 (carbon) zamiast Pegasus — pod Achilles wolałbym trainer; profil 158 m (nie idealnie płasko).

## T5 — SPEED RETURN + THRESHOLD (~85 km, 08–14.06.2026)

### Plan adjustment śr 10.06 — SWAP VO2 → SUSTAINED TEMPO ⭐

**Powód swap:** Tomasz dał 06.06 (sb) spontanicznie 7×400 @ 3:17 = większa intensywność niż planowana T5.śr 6×400 @ 3:30. Speed/VO2 **proven**. Pozostała słabość = **threshold endurance** ("zatyka sustained" feedback z 03.06 tempo 3×2km).

**T5.śr 10.06 NOWY**: SUSTAINED TEMPO 15 min @ 4:20/km ciągłe (NIE split, NIE 4:10!)
- 3 km WU easy → 15 min tempo SUSTAINED @ 4:20 → 3-4 km CD easy
- Total ~12 km
- **HR target 165-172** (Z4 threshold, ~90-94% HRmax)
- Discipline pace! Łatwo pójść 4:10 (zatka znów) lub 4:30 (bez stimulus)
- Buty: Pegasus 42 lub Plus (NIE PrimeX 2)

**Pomiar success:**
- ✅ Cały 15-min blok między 4:18-4:22 (NIE 4:08)
- ✅ HR plateau 165-172 (NIE >175)
- ✅ Płuca komfort sub-progowo (samopoczucie "trudne ale opanowane")
- ⚠️ Jeśli zatyka po 8 min → break w 10 min, finish CD wcześniej. Lepiej 10 min czysto niż 15 min z fade.

**Następne tempo (pt 12.06)**: cruise 3×5 min @ 4:15 z 90s rec (split-format threshold). Razem śr+pt = **threshold endurance focus week**.

### Plan addition wt 09.06 — HILL SPRINTS dodane ⛰️

**Powód:** running economy boost (3-5% realne) — Tomasz pyta o sub-35:30 10K wyzwanie + brak tego stimulus w obecnym planie.

**wt 09.06 NOWY**: Easy 8 km + **3×10 sek HILL SPRINTS** max effort
- Górka **8-12% nachylenie**, długość 80-150 m (10 sek = ~60-70 m biegu)
- Bardzo długa WU 15-20 min easy + drills (A-skip, B-skip, high knees, butt kicks)
- 1. sprint 80% effort (test Achilles), 2-3. max 95-100%
- Recovery: **marsz w dół 90-120 sek** (NIE jog — full recovery)
- CD 1 km easy + rozciąganie łydek + Alfredson eccentric wieczorem
- Buty: **Pegasus 42** (ground feel + cushion)

**Achilles protocol** (post-Chicago 2025 history!):
- Konserwatywnie 3× start (T5)
- T6: 4×, T7: 5×, T8+: 6× cel
- Jeśli bolesność post-workout = STOP, opóźnij progresję

**Cel adaptacja:**
- Tendon stiffness (Achilles + Patellar)
- Neural recruitment (motor unit synchronization)
- Reactive strength = running-specific power

### Wykonane sesje T5

### 2026-06-08 (pn) — REST ✅
- Brak aktywności w Stravie = REST. Po T4.nd 28.28 km long (suffer 189) + T4.sb 7×400 VO2 — idealny dzień wolny.

### 2026-06-09 (wt) — T5.wt easy 9.65 km + **10× HILL SPRINTS** ⛰️ (Achilles protocol sesja 1 — ⚠️ +233% nad plan 3)
- Morning Run: **9.65 km @ 5:59/km**, HR **127**/151, suffer **47**
- Buty: **Pegasus 42** ✓ (zgodnie z planem)
- Elev gain 118m
- Struktura (z lapów):
  - km 1-6: easy Z2, HR 123-130 (czysto, 0 spike'ów)
  - **km 8-9: 10× HILL SPRINTS** (NIE 3 jak plan — **+233%**) — max speed 19.1 → **20.2 km/h (2:58/km)**, progresja **3:33 → 3:12/km** (last rep najszybsza), avg grade 5-8% (max 18%), elev +37.6m i +33.2m, recovery marszem **65-86s** (krótko vs plan 90-120s)
  - km 10: cooldown 0.65 km
- **Komentarz:** ⚠️ **NIE on plan — 10× zamiast 3 = +233% (wariant C).** Format dobry (progresja 3:33→3:12, HR avg 127 = pure neural, suffer 47), ALE **objętość hill sprintów przekroczona ~3×** — a to dokładnie protokół ochronny Achillesa (post-Chicago 9 tyg przerwy). Recovery 65-86s lekko krótkie vs plan 90-120s. Buty Pegasus 42 ✓. **Achilles po sprintach (subiektywne 10.06):** świadomy / „nie 100% jak u 5-latka", bez bólu i bez tkliwości na ucisk = **subclinical stable** — ale to PO 10 sprintach, nie 3. **Decyzja: T6 hill sprinty CIĘCIE do 3× MAX** (cofnięcie z 10, NIE „hold-then-progress"). Progresja do 4× dopiero gdy: (a) trzymasz realnie 3×, (b) ścięgno cicho rano. Alfredson eccentric + pistolet co wieczór.
- URL: https://www.strava.com/activities/18845597251

### 2026-06-10 (śr) — T5.śr **SUSTAINED TEMPO 10 km @ 4:18/km** ⭐⭐ (threshold endurance — dyscyplina A+, ale 3× objętość planu)
- Morning Run: **15.03 km @ 5:02/km avg**, HR **150**/194 (km 1 strap spike), suffer **200**
- Buty: **Adidas Adios Pro 4** (carbon racer; correction — Strava pierwotnie auto-tagowała PrimeX 2, Tomasz poprawił 10.06). Plan sugerował daily (Pegasus 42/Plus), ale crown-jewel pianka PrimeX 2 **oszczędzona** ✓
- Elev gain 90m
- Struktura (z lapów):
  - WU km 1-3 easy (HR real ~108-119; km 1 max 194 = strap spike przy pace 6:28 → fake)
  - **TEMPO km 4-13 = 10 km CIĄGŁE @ 4:15-4:23/km** (~43 min): HR ramp 154 → 170, plateau 165-170 km 7-13
  - CD km 14-15 easy (HR 127-132)
- **Pomiar success vs plan (15 min @ 4:20, HR 165-172):**
  - ✅✅ **Dyscyplina pace IDEALNA** — cały blok 4:15-4:23 (NIE 4:08, NIE 4:30). Ostatni km tempo (13) = 4:15 = najszybszy → **ZERO fade**
  - ✅ HR 165-170 = dokładnie target Z4 threshold (max 173 = 94% HRmax)
  - ⚠️ **Objętość: 10 km tempo zamiast 15 min (~3.5 km) = ~3× plan**
- **Komentarz:** 🔥 **DEFINITYWNIE kasuje narrację "zatyka sustained" z 03.06** — utrzymał 4:18 przez 10 km ciągłych przy HR threshold, bez fade. To dokładnie ten threshold endurance, którego brakowało. Wykonanie wzorcowe pod względem dyscypliny tempa. ⚠️ ALE wariant C znów: 10 km progu zamiast 15-min intro = ogromny stimulus + suffer 200. Buty Adios Pro 4 (carbon racer) = tempo w bucie startowym → **race-specific** (plus, nie minus), ale pace 4:18 lekko wspomagane płytą — surowa forma threshold odrobinę zawyżona względem biegu w daily. Gęstość quality wysoka: 06.06 VO2 → 07.06 28km long → 10.06 43min próg. **Korekta pt 12.06: odpuścić drugi próg** (plan był 3×5min @ 4:15) — po dzisiejszym to za dużo.
- **RPE / kalibracja (subiektywne Tomasz):** „tempo z zapasem, ale NIE na luzie — przebiegłbym dziś spokojnie HM w tym tempie". → 4:18/km ≈ **dzisiejsze HM-effort / próg** (spójne z HR: końcówka 169-170 = AT LTHR 169). Projekcja ~1:29-1:30 HM dziś (vs PB 1:24). **Implikacja kluczowa:** goal Chicago MP **4:08-4:12 jest DZIŚ szybsze** niż pace odczuwany jako HM-effort → MP-fitness jeszcze NIE na celu (oczekiwane w T5, 18 tyg out). To dokładnie **threshold endurance do podniesienia** — recalibracja celu dopiero po T8 5K test (~13-19.07) i T17 30K @ MP.
- ⛰️ **Teren (Tomasz):** blok tempo NIE płaski — **~45 m gain rozłożone na 10 km** (małe rolki co km). Podbija HR przy danym pace o kilka bpm → **flat-equivalent próg pewnie ~4:13-4:16**. HR końcówki 170 = AT LTHR 169, dane czyste (spike 194 tylko km 1 = fake). Chicago jest PŁASKIE → flat-pace to właściwa kalibracja = lekko **optymistyczniej** niż surowe 4:18.
- URL: https://www.strava.com/activities/18860196340

### 2026-06-11 (cz) — T5.cz SIŁA w ogródku 1:10h 💪 (BEZ biegu)
- **Siła ~1:10h**, hantle **15.5 kg total** (trochę więcej niż zwykle), układ standardowy (sesja A), **o 1 serię mniej** — autoregulacja (ciężar↑, objętość↓).
- Plan T5.cz = split easy 10 km + SIŁA HEAVY. Wykonano: **tylko siła** (bieg odpuszczony).
- **Waga: 64 kg rano** (vs baseline 61). +3 kg = **woda, NIE tłuszcz**: (a) **kreatyna** (start 12.05, ~5.5 g/dzień → po ~4 tyg mięśnie nasycone → +1-2 kg wody śródmięśniowej), (b) **glikogen + woda** ze zwiększonych wieczornych węgli (1g glikogenu wiąże ~3g wody). Monitorować TREND, nie pojedynczy odczyt. Opcja: odstawić kreatynę ~2-4 tyg przed Chicago, jeśli optymalizacja race-weight.
- **Komentarz:** ✅ odpuszczenie easy biegu sensowne w kontekście deload + sen/kortyzol. 48h do pt (które i tak = easy) → timing OK. Brak biegu = T5 km niżej, recovery priority.

### 2026-06-12 (pt) — T5.pt **TEMPO 3×5 min @ 4:13/km** ⭐ (WG PLANU — co do sekundy i metra)
- Morning Run: **10.00 km @ 5:38/km avg**, HR **143**/201 (lap 1 max 201 = strap spike przy easy WU = fake), suffer 111
- Buty: **Pegasus Plus** ✓
- Struktura (lapy): WU 3.2 km easy → **3× ~5 min @ 4:13 / 4:14 / 4:14** (HR 158→164→163, max 172) z 90 s trucht rec → CD 2.82 km easy (HR 128)
- **Komentarz:** ✅ **Dokładnie wg planu** (viewer pt 12.06: „TEMPO 3×5 min @ 4:15, Pegasus 42/Plus"). Wykonano 4:13/4:14/4:14, HR 164-172 = Z4 threshold — wzorowo i zdyscyplinowanie (4:13, nie 4:00). **[Korekta trenera: wcześniej błędnie oznaczyłem to jako „wariant C / mimo zalecenia easy". Moja sugestia easy z 10.06 była TYLKO w czacie — nigdy nie trafiła do planu. Tomasz słusznie wykonał ZAPISANY plan, co do sekundy. Lekcja: zmiany planu COMMITOWAĆ, nie tylko mówić.]** T5 miało 2 progi z założenia planu; T6 deload (pn) absorbuje. Pegasus Plus ~15 s/km wolniej niż race → **4:13 ≈ ~3:58 w Adios/PrimeX** (race-day bonus).
- URL: https://www.strava.com/activities/18886319516

### 2026-06-13 (sb) — T5.sb **SIŁA ogród 1:30h** 💪 + easy 13.04 km @ 6:12 (⚠️ stack przed long)
- **Rano: siła w ogrodzie ~1:30h** — standardowy zestaw (jak 11.06: single-leg focus, hantle; zwykle z łydkami eccentric). DOMS czuć dziś (14.06).
- Easy: **13.04 km @ 6:12/km**, HR **130**/157, suffer 88, Pegasus 42, elev 126 m, kadencja 94.6 (~189 spm) — czysty Z2, zero spike'ów (max 157 = pewnie podbieg).
- **Komentarz:** ⚠️ **Brakujący element układanki Achillesa.** Siła 1:30h (single-leg + prawdopodobnie eccentric łydki) + 13 km w sobotę → **28 km w niedzielę**. Naruszona własna reguła z T1: *„NIE siła 24h przed długim biegiem (>12 km); siła DZIEŃ PO long, nie przed"*. Jeśli zestaw miał eccentric łydki (jak zwykle) — bezpośredni load na Achilles dzień przed 28-tką = realny wkład we flarę insertional. Sam bieg czysty (Z2), ale **stack siła+long** = czerwona lampka. Lekcja z 10.05 powtórzona.
- URL (run): https://www.strava.com/activities/18898401690

### 2026-06-14 (nd) — T5.nd **LONG 28.11 km @ 5:35/km** ⭐ aerobowo + ⚠️ **ACHILLES BOLI**
- Morning Run: **28.11 km @ 5:35/km avg**, HR **129**/170, suffer **168**, 2:37:10 moving
- Buty: **Nike Pegasus Plus**, elev 225 m, kadencja 95.7 (~191 spm)
- **Komentarz:** aerobowo IDEALNY long — HR avg **129 (Z2/top)** = dyscyplina easy A+, drift kontrolowany, kadencja 191 = forma OK. Tempo i HR bez zarzutu. **ALE Tomasz zgłasza ból Achillesa po biegu.** ⚠️ Achilles ≠ mięsień, nie "rozbiega się". Kontekst skumulowanego load'u: **09.06 10× hill sprints** (czysta ekscentryka na Achilles) → 5 dni → **28 km** + cały tydzień ~83 km biegu + 2 progi + siła heavy. To nie pace zabił ścięgno, to objętość/ekscentryka. **PROTOKÓŁ Achilles aktywowany** (patrz chat 14.06): bez podbiegów/speed/heavy-calf, izometrie, monitoring porannej sztywności, cross-training jeśli ból >3/10.
- URL: https://www.strava.com/activities/18912141889

---

## T4 — BASE INTRO (~70 km, 01–07.06.2026)

### 2026-06-07 (nd) — T4.nd **LONG 28.28 km @ 5:36/km** ⭐⭐ (drift +1 bpm = ELITE!)
- Morning Run: **28.28 km @ 5:36/km avg**, HR **131**/187 (km 1 strap spike), suffer **189** (najwyższy w T4)
- Elev gain 226 m
- Calories 1719 kcal
- Plan T4.nd = LONG 24 km easy 5:45-6:00. Wykonano **28.28 km @ 5:36** (+4 km, szybciej tempo)
- **HR drift analiza (excluding km 1 strap spike 159):**
  - Q1 (km 2-7): avg HR **~130**
  - Q2 (km 8-14): avg HR **~128**
  - Q3 (km 15-21): avg HR **~130**
  - Q4 (km 22-29): avg HR **~131**
  - **Drift Q1→Q4: +1 bpm** = ELITE aerobic ✅
- **Highlights splitów (mid-run organic surge):**
  - km 13: 5:04 @ HR 128
  - km 14: 5:13 @ HR 124
  - **km 15: 4:54 @ HR 129** ⭐
  - **km 16: 4:54 @ HR 130** ⭐⭐
  - = **sub-tempo @ HR <130** = niesamowita ekonomia
- **Komentarz:** 🔥 **DEFINITIVELY kasuje narrację "katastrofa, zatyka >4:00"** z 03.06:
  - Dzień 06.06: 7×400 @ 3:17 (speed proven)
  - Dzień 07.06: 28 km drift +1 + 2 km @ 4:54 HR <130 (aerobic engine ELITE)
- Co naprawdę brakuje = **threshold endurance** (sustained @ próg) → cel śr 10.06.
- ⚠️ **Cumulative load wysoki** — suffer 189 + dzień po VO2 7×400. Jutro pn REST obowiązkowy. Sprawdzić Achilles + HRV.
- URL: https://www.strava.com/activities/18818451508

### 2026-06-06 (sb) — T4.sb **7×400m @ 3:13-3:21/km** ⚡ (VO2max session!)
- Morning Run: **10.00 km @ 5:36/km avg**, HR **144**/197 (strap spike WU), suffer **123**
- **7×400m intervals** (400m recovery jog 7:00-7:54/km):
  - Rep 1: 3:21 HR 164/176
  - Rep 2: 3:19 HR 165/175
  - Rep 3: 3:17 HR 166/177
  - Rep 4: 3:18 HR 167/178
  - Rep 5: 3:14 HR 168/178
  - Rep 6: 3:18 HR 167/177
  - **Rep 7: 3:13 HR 167/177 ← najszybsza!**
- Avg pace per rep: **3:17/km (= 1:19/400m)**
- Avg HR per rep: **167 (91% HRmax 183)**, HR max 178 (97%)
- WU 3 km + CD 1.77 km easy
- **Komentarz:** ⭐⭐ **VO2max session perfectly executed**. Plan T4.sb był easy 8 + 4×100 strides. Tomasz dał **7×400 @ 3:17 avg z progresją** (każda rep równa lub szybsza). Rep #7 najszybsza = NIE zatkał się. To **definitywnie kasuje** narrację "katastrofa, zatyka >4:00" z 03.06 — Tomasz HAS speed, tempo wt zatykało bo cumulative fatigue (morning combo). HR max 178 = 97% HRmax = engine sięga prawdziwego peaku. Plus po pt sile HEAVY 1.5h i wczoraj REST: świetne że ciało wytrzymało takiej intensywności.
- URL: https://www.strava.com/activities/18804684812

### 2026-06-05 (pt) — T4.pt SIŁA HEAVY 1.5h 💪 (progresja objętości)
- **Siła w ogródku 1.5h** z hantlami 2×5kg (te same co wcześniej):
  - Przysiady jednonóż z obciążeniem: 4×10/nogę
  - **Bułgary 4×15/nogę** (vs poprzednio 3×15 = +1 seria)
  - **Przysiady dwunóż 4×20** (vs 3×20 = +1 seria)
  - **Jaskółki 4×15/nogę** (vs 4×10 = +50% reps!)
  - **Marsz wykroczny 4×32 kroków** (vs 4×30)
  - **Łydki na schodach 4×20/nogę** (vs 3×20 = +1 seria)
  - 3 deski (prosta + 2 boczne) 3×1:30
  - Rozciąganie
- Plan T4.pt = HEAVY 1:30. Wykonano: **dokładnie plan, z progresją objętości** (więcej serii/reps).
- **Komentarz:** ⭐ **progresja przez objętość** (NIE ciężar). Bułgary +1 seria, jaskółki +50% reps, łydki +1 seria. Total 1.5h. To **strength endurance** development = idealne dla maratonu. Po cz 17.10km easy (drift +1 bpm = ELITE) + dzisiejsza siła = silny T4 dotąd. Jutro sb easy + 4×100 strides, ND long 24 km progresywny.

### 2026-06-04 (cz) — T4.cz easy 17.10 km ⭐ (drift +1 bpm)
- Morning Run: **17.10 km @ 5:54/km**, HR **129**/165, suffer 101
- Elev gain 231m
- **Quartile HR: 130/130/126/131 → drift +1 bpm = ELITE** 🔥
- 0 strap spikes
- Plan T4.cz = easy 10 + drills. Wykonano 17.10 km (+71% nad plan).
- **Komentarz:** ⭐ idealne T4.cz — dystans przekroczony ale HR w Z2 strict (129 avg). Drift +1 bpm na 17km z 231m elev = sub-3 forma faktycznie utrwala. Cz po tempo śr (3×2km) z drift +1 bpm = ZNAKOMITA recovery.
- URL: https://www.strava.com/activities/18779129289

### 2026-06-03 (śr) — T4.śr TEMPO **3×2km @ 4:14/4:14/3:58** ⭐ (Tomasz: "katastrofa", obiektywnie OK)
- Morning Run: **11.19 km @ 5:17/km avg**, HR **145**/181, suffer **119**
- **3×2km tempo** (NIE 2×8 min jak skorygowany plan):
  - Rep 1: 2.00 km @ **4:14/km**, HR 162/170
  - Rep 2: 2.00 km @ **4:14/km**, HR 165/173
  - Rep 3: 2.01 km @ **3:58/km**, HR 170/**181** (99% HRmax!)
- Recovery jog 400m @ 7:52-8:18/km między
- WU 3km @ 5:52 + CD 1.35km @ 7:52
- **Tomasz subiektywnie:** "katastrofa, kompletny brak prędkości, zatyka >4:00/km, +1kg więcej, brak speed work ostatnich tygodni"
- **Obiektywnie:** dał plan +50% (6km tempo vs plan 3.8km), ostatnia rep **szybsza niż target** (3:58 vs 4:15). HR max 181 = engine podał maks.
- **Historia Tomasza:** luty 2026 3×5 @ 4:15/4:10/4:05 — zatkał na 4:10. Miesiąc tempo work → 3×5 @ 4:05/4:00/3:55. Speed wraca szybko z regular tempo+interwały.
- **Komentarz:** to NIE katastrofa, to **przeforsowanie po wczorajszym morning combo** (VO2max-strides + siła back-to-back). Plus aerobic base IDEALNA (drift −10 / +1 na long = sub-3 forma). Speed wraca w 2-3 tyg z regular tempo + interwały. Plan T5: śr VO2 8×400 + pt tempo 3×6 @ 4:15. Waga: -1kg w 2-3 tyg via reduce wieczorne kalorie o 300/dzień (NIE w hard week).
- URL: https://www.strava.com/activities/18765040177

### 2026-06-02 (wt) — T4.wt MORNING COMBO: easy 11.9km + **6×150 strides** + siła back-to-back 💪
- Morning Run: **11.90 km @ 5:58/km**, HR **137**/196 (strap spike Q1), suffer **106**
- Elev gain 159m
- Quartile HR: 149 (spike)/130/132/138 → **real drift Q2→Q4: +8 bpm**
- HR ≥180 spikes: 352 punkty (strap glitch warm-up)
- **6×150m strides (NIE strides — de facto VO2max!):**
  - Rep avg dist: 127m × 25s
  - Pace: 3:03-3:12/km (best chwilowy 2:46-2:59!)
  - HR ramping: 145 → 153 (max 165)
  - + 2 dłuższe pre-strides (244m @ 3:35 + 121m @ 3:41)
- **Siła w ogródku (mid-intensity ~45-60 min):**
  - Schodki 3×10/nogę (single-leg step-ups)
  - **Bułgary 3×15/nogę** (więcej reps niż zwykle 10!)
  - Łydki 3×20/nogę eccentric (Alfredson continuation)
  - Deska front 1:30
  - 2 deski boczne 1:30 (P + L)
  - Rozciąganie
- **Komentarz:** plan T4.wt v3 = easy 8 + LIGHT 30 min wieczorem. Wykonano **MORNING COMBO**: bieg 11.9 + 6×150 strides + siła back-to-back (NIE split z 8h przerwy, tylko zaraz po biegu). Drift +8 bpm = nogi nadal trochę po nd 24.80km long. 🎯 **Bułgary 3×15 = większa objętość single-leg** — Tomasz buduje siłę systematycznie. ⚠️ Bieg z VO2max-strides + siła back-to-back = duży CNS + tendon load w jeden poranek. **Plus**: cały dzień na regenerację przed tempo śr. **Minus**: jutro tempo może być nieco zmęczone — sugeruję **2×8 min @ 4:15** zamiast 2×10.

### 2026-06-01 (pn) — REST ✅
- Plan T4.pn = REST obowiązkowy. Wykonano: REST ✓ (po nd 24.80km long, idealnie).

---

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
