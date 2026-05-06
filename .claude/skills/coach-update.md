---
name: coach-update
description: Cotygodniowy raport — pobiera ze Stravy aktywności, pyta Tomasza o dane Garmin/subiektywne, analizuje progres + zmęczenie, proponuje korekty planu na kolejny tydzień. Używać niedziela wieczór / poniedziałek rano.
---

# /coach-update — cotygodniowy raport progresu i zmęczenia

## Cel

Cotygodniowy punkt decyzji:
- Czy plan działa (progres)
- Czy organizm wytrzymuje (zmęczenie)
- Co skorygować w nadchodzącym tygodniu

**Monitoring zmęczenia jest priority #1** (Tomasz primary fear: chronic fatigue → regres). Plan jest dynamic, aktualizowany co tydzień.

## Workflow

### Krok 1: Strava auto-pull (Claude)

Pobierz aktywności od ostatniego raportu do dziś:
- `mcp__strava__get_recent_activities` lub bezpośrednio API curl z `.env`
- Filtruj: tylko Run + Walk (cross-training jako notatka)
- Wyciągnij dla każdej: data, dystans, czas, pace avg, HR avg/max, suffer, splits/laps

### Krok 2: Pytanie Tomasza o Garmin + subiektywne

Zapytaj 6 pytań w jednej wiadomości:

```
Daj liczby z Garmina za ostatnie 7 dni:
1. Średni sen (h)?
2. Najsłabsza noc (h)?
3. Średnie HRV (jeśli pokazuje)?
4. Średnie HR rest poranne?
5. Body Battery min / avg (jeśli mierzysz)?

I subiektywne (1-10):
6. Motivation / energia? Apetyt? RPE easy biegów? Coś bolało?
```

Czekaj na odpowiedź zanim analizujesz.

### Krok 3: Analiza (Claude)

#### Progres
- **Easy pace @ HR 120-125** — porównaj do poprzednich tygodni
- **HR drift na long >15 km** — Q1 vs Q4
- **Quality session paces vs plan** — czy hit'owane targets
- **Tygodniowy total km** — vs plan

#### Zmęczenie
| Marker | Norma | Czerwona flaga |
|---|---|---|
| HR rest poranne | ±3 bpm baseline | +5 bpm 3+ dni |
| Sleep avg | 6h+ | <6h 3+ noce |
| Sleep quality 1-10 | 6-8 | ≤4 trzy noce |
| HRV trend | stable / rosnący | spadek 7+ dni |
| RPE easy | 3-4/10 | 6+/10 |
| Suffer score easy | <60/sesja | >100/sesja (grey zone) |
| Body Battery | regen do 70+ rano | start dnia <30 |

**Auto-reset:** jeśli **2+ markery w czerwonym przez 7 dni** → propozycja deload (50% volumen, 0 quality, 3-4 dni rest, plan przesunięty 1 tydzień).

#### Strefy HR (HRmax 182)

| Strefa | BPM | Charakter |
|---|---|---|
| Z1 | 91–109 | Recovery |
| Z2 | 110–127 | Easy / aerobic base |
| Z3 | 128–146 | Steady / marathon |
| Z4 | 147–164 | Threshold |
| Z5 | 165–182 | VO₂max |

### Krok 4: Werdykt + korekty planu

Trzy poziomy:
- ✅ **Postęp na track** — plan utrzymany, ewentualnie minor tuning
- ⚠️ **Ostrzeżenie** — 1-2 markery żółte → konserwatywniejsze paces / mniejszy volumen tego tyg
- 🛑 **Auto-reset / deload** — 2+ markery czerwone → 50% volumen, 0 quality

### Krok 5: Update plików + commit

Po akceptacji korekty przez Tomasza:
- `training_log.md` — dopisz wykonane sesje + summary tygodnia
- `plan.md` — skoryguj sesje na bieżący tydzień (jeśli zmiany)
- `viewer.html` — odśwież tabele jeśli istotne zmiany
- `git add . && git commit -m "Weekly report TX..." && git push`

## Output format dla Tomasza

```markdown
## Weekly Report — T<X> (<daty>)

### Wykonanie vs plan
- km plan: X / wykonane: Y (<delta>%)
- Quality sessions: <N>/<plan> ✓/✗
- Easy: <%> czasu w Z1-Z2 (cel ≥80%)

### Progres
- Easy pace @ HR 120-125: <pace> (vs <prev> tydz temu) <↑↓→>
- Long HR drift: <bpm> (vs <prev>)
- Najlepsza sesja: <opis>
- VO2 / signature paces vs plan: <hit / lekko poniżej / przekroczone>

### Zmęczenie
- Sleep avg: <h>h <flag>
- Resting HR: <bpm> (baseline <bpm>) <flag>
- HRV trend: <↑↓→>
- Suffer easy total: <suma> (norma ~<expected>)
- RPE easy: <X>/10
- Subiektywnie: <co Tomasz powiedział>

### Werdykt
<✅/⚠️/🛑> <jednoliniowo>

### Korekty na T<X+1>
1. <konkretna zmiana w sesji + powód>
2. <...>
3. <...>

### Najbliższe 3 sesje
1. <data>: <trening + tempo + HR cel>
2. <data>: <...>
3. <data>: <...>

### Decyzje przyszłe
- <event upcoming i co od niego zależy>
```

Krótko, liczbowo, czytelne w 60 sek.

## Reguły wnioskowania (po fazach)

- **Po T1-T2 (recovery extension):** sprawdź czy easy pace przy HR Z2 schodzi (np. z 6:00 do 5:50). Jeśli nie schodzi po 2 tyg = za duży tonaż.
- **Po pierwszej VO₂max (T4):** sprawdź czy szczytowe HR sięgnęły Z5 (>164). Jeśli nie — albo trening za lekki, albo HRmax niższy niż 182 (re-test).
- **W T7-T11:** pace na easy stabilizuje się ~5:30–5:45 przy HR Z2. Jeśli rośnie z tygodnia na tydzień przy tym samym HR = przemęczenie.
- **Przed T8 test 5K:** ostatnie 4 dni HR strict Z1–Z2, żadnych intencjonalnych „push".
- **Po T17 30K TT:** 7 dni czysto easy + recovery, niezależnie od samopoczucia. Wynik 30K przeskaluje cel Chicago.
- **W T19 LR z 24 km @ MP:** w PrimeX 2 para B (race shoe). HR ostatnich 5 km MP <175 = OK. >180 = koryguj cel MP.

## Benchmark schedule (key tests)

| Tydz. | Test | Cel pomiarowy |
|---|---|---|
| T4 | VO₂max 5×800 intro | Pace przy 5K-effort |
| **T8** | **TEST 5K (TT)** | **Czas → kalibracja paces** |
| T11 | 3K TT mid-block | Pace vs T8 |
| T14 | 8 km @ HM-effort | Pace + HR drift |
| **T17** | **SOLO 30K @ MP** | **Czas → cel Chicago confirm** |
| T19 | LR 32 z 24 @ MP | HR last 5 km MP |

## Cadence

- **Główny raport: niedziela wieczór** (lub poniedziałek rano przed treningiem)
- **Mid-week check** opcjonalny (jeśli Tomasz pyta lub coś istotnego się dzieje — ból, infekcja, nieprzewidziana sesja)
- **Po każdym key benchmark** (T8, T17): osobny analytical update z rekomendacjami planu

## Format zapisu w training_log.md

Każda nowa aktywność jako blok markdown. Zachowaj chronologię. Jeśli tydzień jeszcze nie ma sekcji — utwórz nagłówek `## TX — NAZWA (km, daty)` zgodnie z `plan.md`.

Tygodniowe podsumowanie po wszystkich sesjach tygodnia:
```
### Tydzień TX — podsumowanie
- km wykonane: X (plan Y)
- Sesji wykonanych: N (plan M)
- Średni HR easy: X
- Highlights: <co poszło dobrze>
- Lowlights: <co nie poszło>
- Avg sleep: Xh, RPE: Y/10
```
