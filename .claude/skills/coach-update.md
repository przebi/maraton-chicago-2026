---
name: coach-update
description: Pobiera ze Stravy ostatnie aktywności (od ostatniej aktualizacji w training_log.md), uzupełnia log, analizuje vs plan, sygnalizuje fatigue markers i proponuje korekty na bieżący tydzień. Używać na początku każdej rozmowy treningowej w projekcie maraton-chicago-2026.
---

# /coach-update — bieżąca aktualizacja stanu treningu

## Co robi ten skill

1. **Pobiera ze Stravy** wszystkie aktywności od ostatniego wpisu w `training_log.md` do dziś (tylko biegowe; rowerowe/spacerowe pomija lub odnotowuje pod „cross-training").
2. **Wyciąga dla każdej:** dystans, czas, pace, HR avg/max, % czasu w strefach Z1–Z5, splity (jeśli interwał), URL aktywności.
3. **Dopisuje do `training_log.md`** w kolejności chronologicznej, w sekcji bieżącego tygodnia.
4. **Aktualizuje tabelę „Statystyki tygodniowe"** — sumuje km, sesje, średni HR easy.
5. **Porównuje z `plan.md`** dla danego tygodnia — co miało być vs co było.
6. **Wykrywa fatigue markers:**
   - HR drift na long: porównuje HR pierwszej i ostatniej ćwiartki — flag jeśli >10 bpm
   - Easy zbyt szybko: jeśli > 10% czasu w Z3+ na biegu oznaczonym jako easy
   - Easy zbyt wolno przy wysokim HR: jeśli pace 6:00+ ale HR > Z2 = fatigue/illness
   - Sesja jakościowa nie domknęła zakresu tempa — flag, sugestia korekty na kolejny tydzień
7. **Wnioskuje:** czy zostać przy planie, czy korygować (np. dodatkowy easy day, deload tydzień wcześniej, zmiana tempa next session)
8. **Zwraca user-facing summary** z 3 sekcjami:
   - **Co się działo** (1–3 bullety, krótko)
   - **Sygnały** (fatigue / pozytywne — jeśli są; jeśli wszystko OK, „nic istotnego")
   - **Następne 3 sesje** (z datami + co konkretnie + tempo + cel HR)

## Jak wywołać Strava MCP

Zakładamy że MCP server jest podłączony jako `strava` (po SETUP.md).

Typowe wywołania:
- `mcp__strava__get_recent_activities` z parametrem `before` (timestamp ostatniego wpisu) i `after` (now) — lista aktywności
- `mcp__strava__get_activity` po ID — szczegóły
- `mcp__strava__get_activity_streams` po ID z `keys=heartrate,velocity_smooth,altitude` — minutowe streamy do analizy stref i drift

(Konkretne nazwy tools potwierdzić po pierwszym `/mcp` po podłączeniu — różne implementacje strava-mcp mogą używać innych prefixów.)

## Obliczenia stref HR (HRmax 182)

| Strefa | BPM |
|---|---|
| Z1 | 91–109 |
| Z2 | 110–127 |
| Z3 | 128–146 |
| Z4 | 147–164 |
| Z5 | 165–182 |

Dla każdej aktywności z HR stream: zlicz % czasu w każdej strefie (sample-by-sample lub minutowy avg).

## HR drift — algorytm

Dla biegów ≥ 75 min:
1. Podziel HR stream na 4 ćwiartki czasowe.
2. Średnie HR w Q1 i Q4. Różnica = drift.
3. < 5 bpm: dobra forma aerobowa (efficient).
4. 5–10 bpm: norma dla long.
5. > 10 bpm: fatigue, undertraining lub odwodnienie.
6. > 15 bpm: red flag, sugeruj recovery day.

## Reguły wnioskowania

- **Po 2 łatwych tygodniach (T1–T2):** sprawdź czy easy pace przy HR Z2 schodzi (np. z 6:00 do 5:50). Jeśli nie schodzi po 2 tyg = za duży tonaż lub niedopełniony recovery.
- **Po pierwszej VO₂max (T4):** sprawdź czy szczytowe HR sięgnęły Z5 (>164). Jeśli nie — albo trening za lekki, albo masz pułap niższy niż 182 (re-test HRmax).
- **W okresie speed (T7–T11):** pace na easy powinien się stabilizować ~5:30–5:45 przy HR Z2. Jeśli rośnie z tygodnia na tydzień przy tym samym HR = przemęczenie.
- **Przed testem 5K (T8):** ostatnie 4 dni HR strict Z1–Z2, żadnych intencjonalnych „push".
- **Po HM Praskim:** 7 dni czysto easy + recovery, niezależnie od samopoczucia. Wynik HM przeskaluje MP Chicago.

## Format zapisu w training_log.md

Każda nowa aktywność jako blok markdown (zob. format w `training_log.md`). Zachowaj chronologię. Jeśli tydzień jeszcze nie ma sekcji — utwórz nagłówek `## TX — NAZWA (km, daty)` zgodnie z `plan.md`.

## Output format dla user'a (po wywołaniu)

```
## Status na <data>

### Co się działo (od <ostatnia rozmowa>)
- <bullet>
- <bullet>

### Sygnały
- <fatigue marker / nic istotnego>

### Plan na najbliższe sesje
1. <data>: <trening> (<tempo>, HR cel <strefa>)
2. <data>: <trening>
3. <data>: <trening>

### Korekty planu (jeśli)
- <co zmieniam i dlaczego>
```

Krótko i konkretnie — ma być czytelne w 30 s.
