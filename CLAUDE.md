# Maraton Chicago 2026 — projekt treningowy

## Profil zawodnika

- **Imię:** Tomasz Przebieracz
- **Wiek:** 51
- **Wzrost / waga:** 173 cm / 61 kg (BMI ~20.4)
- **HRmax:** **183** (Garmin biometric, 2026-05-06)
- **LTHR:** **169** (Garmin biometric)
- **RHR baseline:** 47 (Garmin)
- **VO₂max:** 57.6 (Garmin estimate, top 5% w wieku 51 lat)
- **Strava:** https://www.strava.com/athletes/24659157
- **Garmin device:** fenix 7 Pro Sapphire Solar

## Cel sezonu

- **A-race: Chicago Marathon — 11.10.2026**, cel **2:55-2:57** (4:08-4:12/km)
- **HM Praski 5.09.2026: ODPUSZCZONY** — single-focus Chicago
- **Start bloku:** 11.05.2026 (T1)
- **Tygodni do A:** 22

## Życiówki

| Dystans | Czas | Tempo /km | Rok |
|---|---|---|---|
| Maraton | 2:59:32 (Hannover) | 4:15 | wiosna 2025 |
| Półmaraton | 1:24:11 (Warszawa) | 3:59 | 2024 |
| 5K (track, controlled) | 19:08 (target był 18:45) | 3:50 | 2023 |

## Ostatni start

- **Maraton Wiedeń, 19.04.2026 — 3:11** (odpuszczony bieg od 15 km, ciepło 20+°C)
- 8 dni przed startem: 3×5 km @ 4:05 / 4:00 / 3:55 (przerwy 1 km truchtu) — trening trudny, prawdopodobnie zbyt ciężki tak blisko startu
- Po marathonie kontynuował akcenty (wariant C) — recovery niedopełniony
- Stan na 6.05.2026: „4:00 zatyka", trening idzie słabo, planowany start za tydzień **odpuszczony**

## Słabość zidentyfikowana (priorytet treningu)

**Wytrzymałość prędkościowa**. Speed cap historyczny ~19:00-19:08 na 5K (track, controlled). Po 7 tyg specific block T8 cel: 18:30-18:45. Plan signature workouts (3-4×4-5K progresywne) buduje to.

## Założenia treningowe

- **Wolumen:** 70–100 km/tydz (T1–T2 niżej recovery, peak T10/T15/T19 = 95-100)
- **Sesje:** 5–6 / tydz
- **Polaryzacja:** 80/20, wolne biegi naprawdę wolno (>6:00/km dopuszczalne)
- **Regeneracja:** sauna, pistolet do masażu (10-15 min/dzień, focus łydki)

## Strefy HR (HRmax 183, LTHR 169 — z Garmin biometric)

| Strefa | % HRmax | BPM | Charakter |
|---|---|---|---|
| Z1 | 52–59% | 95–108 | Recovery |
| Z2 | 60–70% | 109–127 | Easy / aerobic base |
| Z3 | 70–80% | 128–146 | Steady / marathon |
| Z4 | 80–90% | 147–164 | Threshold |
| Z5 | 90–100% | 165–183 | VO₂max |

**LTHR z Garmin: 169** (~92% HRmax). Próg → HR ~165–170. Wcześniejsza estymata 160–165 była **za nisko**.

## Fatigue markers baseline (z 365 dni Garmin)

| Marker | Baseline | Czerwona flaga | Auto-reset |
|---|---|---|---|
| HRV | 55-58 ms | <50 ms | <45 ms 5+ dni |
| RHR | 45-48 bpm | >50 bpm 3+ dni | >52 bpm 3+ dni |
| Sleep avg | 6.2h | <6h tydzień | <5.5h 3 noce |

**Lekcja z 2025 Q4:** post-Chicago crash (HRV 40, RHR 54) trwał **2 miesiące**. Tego unikamy w 2026.

## Faza obecna

**Recovery extension** — T1–T2 (11–24.05) tylko easy + strides + drills, **zero** progów, interwałów, hill sprintów. Cel: schodzenie z fatigue post-Wiedeń.

## Pliki projektu

- [plan.md](plan.md) — makro 22 tyg + bieżąca rozpiska tygodniowa
- [training_log.md](training_log.md) — log treningów ze Stravy + komentarze
- [SETUP.md](SETUP.md) — instrukcja podpięcia Strava MCP (jednorazowo)
- [.claude/skills/coach-update.md](.claude/skills/coach-update.md) — skill `/coach-update` do statusu formy
- [data/](data/) — eksporty CSV / dane surowe

## Workflow

1. Przed sesją z trenerem-Claude: powiedz `/coach-update` — Claude pobierze ze Stravy aktywności od ostatniej rozmowy, zaktualizuje `training_log.md`, oceni czy plan trzymany / odchylenia / fatigue markers (HR drift, niski/wysoki HR na easy)
2. Claude proponuje korekty planu (jeśli potrzebne) i potwierdza kolejne sesje na bieżący tydzień
3. Po każdym tygodniu: krótki review (km, jakość, HR trends, samopoczucie)
4. Co 4 tyg deload — review większy, ewentualnie test 5K

## Nie zapominać

- **Każda sesja w T1–T2 = easy.** Nawet jeśli „nogi proszą".
- Pierwsza VO₂max **dopiero T4** (nie wcześniej niż 6 tyg po Wiedniu).
- Pierwszy prawdziwy benchmark: **TEST 5K w T8** (~13–19.07).
- Ostatni hard trening **14 dni przed Chicago**, nie 8 (lekcja z Wiednia).
