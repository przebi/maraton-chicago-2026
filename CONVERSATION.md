# Kontekst rozmowy → kontynuacja w VS Code

Ten plik zawiera streszczenie dotychczasowej rozmowy z Claude w której powstał ten projekt. Otwierając katalog w VS Code i startując nową sesję, Claude przeczyta CLAUDE.md (automatycznie) plus może zerknąć tu po historię ustaleń.

## Skąd się wziął ten projekt

Tomasz pracował z Claude nad planem treningowym **dla syna** (20 lat, HM PB 1:45, plan kontynuacja T5–T8 z istniejącego arkusza Google Sheets). Plik dla syna: `~/Desktop/plan_trening_T5-T8.xlsx`. To skończony temat — nie miesz go z planem Tomasza.

Następnie Tomasz poprosił o plan dla siebie (Maraton Chicago 11.10.2026, cel Sub-3). Pierwsze założenia okazały się błędne — Claude zgadywał że marathon Wiedeń 19.04.**2025** (rok temu), w rzeczywistości był 19.04.**2026** (3 tyg temu). Plus mylnie czytał arkusz syna jako tracker Tomasza.

Po doprecyzowaniu (wariant **C** = po Wiedniu kontynuował akcenty, dziś forma osłabiona, „4:00 zatyka") powstał plan w którym **T1–T2 to wymuszone recovery extension** — żeby ciało dokończyło regenerację po marathonie + skumulowanych akcentach pomarathonowych.

Tomasz poprosił żeby:
1. Stworzyć projekt w osobnym katalogu (zrobione: `~/projects/maraton-chicago-2026/`)
2. Podpiąć Stravę przez MCP, żeby Claude czytał treningi automatycznie (instrukcja w SETUP.md)
3. Zrobić skill który podsumowuje stan formy i koryguje plan (`.claude/skills/coach-update.md`)
4. Przenieść kontekst do projektu (ten plik + CLAUDE.md + plan.md + training_log.md)

## Krytyczne ustalenia

- **HRmax = 182** (potwierdzony przez Tomasza, 2026-05-06). Strefy w CLAUDE.md.
- **Słabość: prędkość i wytrzymałość prędkościowa.** Nawet w formie sub-3 nie schodził pod 19:30 na 5K. To priorytet bloku speed (T7–T11).
- **Lekcja z Wiednia:** ostatni hard 8 dni przed startem (3×5K @ 4:00) był za późno i za mocny. W planie Chicago: **ostatni hard 14 dni przed**.
- **Półmaraton Praski 5.09.2026** (sobota wieczór 20:30, dzielnica Praga w Warszawie) — tune-up race 5 tyg przed Chicago. Cel ~1:23–1:24.
- **80/20 polaryzacja**, easy >6:00/km dopuszczalne.
- **70–90 km/tydz, 4–5 sesji/tydz.**
- **Regeneracja:** sauna, pistolet do masażu (samodzielnie).

## Co zostaje do zrobienia (ze strony Tomasza)

1. **SETUP.md kroki 1–4** — utworzyć Strava API app, sklonować strava-mcp, autoryzować, zarejestrować w Claude Code. ~15 min jednorazowo.
2. Po SETUP: zrestartować Claude Code, sprawdzić `/mcp`, wywołać `/coach-update`.
3. **Tydzień 0 (07–10.05):** 4 dni same easy, ~30 km. Bez akcentów. Cel: schodzenie z fatigue przed startem T1.
4. **T1 startuje 11.05.2026** zgodnie z `plan.md`.

## Co zostaje do zrobienia (ze strony Claude)

- Po podłączeniu Stravy: pierwszy `/coach-update` ściągnie aktywności od ~01.04.2026 (taper Wiedeń + race + post-race) i wypełni baseline w training_log.md.
- Po T4 (pierwsza VO₂max): kalibracja LTHR z HR pod koniec progu.
- Po T8 (TEST 5K): twarde tempa T9–T17, doprecyzowanie z szkic → szczegół.
- Po HM Praskim: projekcja MP Chicago, korekta T18–T22.

## Pytania otwarte (dopytać przy okazji)

- HR rest (poranne) Tomasza? Pomoże w kalibracji recovery markers.
- Sauna — częstotliwość? (heat acclimation może być bonusem przed Chicago)
- Czy Tomasz chce dorzucić siłówkę (nogi, core)? Często niedoceniana u 50+, daje speed reserve.
- Jaki zegarek ma? (Garmin/Polar/Suunto wpływa na jakość HR streams w Stravie)

## Style komunikacji (preferencje Tomasza)

- Polski, bezpośredni, konkretny
- Bez emoji w odpowiedziach Claude (chyba że Tomasz sam ich użyje)
- Krótkie podsumowania, nie przegadane
- Tomasz docenia gdy Claude pyta o doprecyzowanie zamiast zgadywać (lekcja z błędu „Wiedeń 2025 vs 2026")
- Tomasz lubi liczby (km, tempa, BPM, %) zamiast prozy
