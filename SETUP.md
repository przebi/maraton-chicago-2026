# Setup — Strava MCP + projekt

## 1. Strava API (jednorazowo)

1. Otwórz https://www.strava.com/settings/api
2. Wypełnij formularz „Create & Manage Your App":
   - **Application Name:** Claude Coach (cokolwiek)
   - **Category:** Training
   - **Club:** zostaw puste
   - **Website:** http://localhost
   - **Authorization Callback Domain:** `localhost`
3. Kliknij Create. Po utworzeniu zobaczysz:
   - **Client ID** (numerek ~6 cyfr)
   - **Client Secret** (długi hash) → kliknij „Show" żeby zobaczyć

Zapisz te wartości — potrzebne w kroku 3.

## 2. Klonowanie Strava MCP

```bash
cd ~/projects/maraton-chicago-2026
git clone https://github.com/r-huijts/strava-mcp.git
cd strava-mcp
npm install
npm run build
```

## 3. Konfiguracja tokena

W katalogu `strava-mcp` utwórz plik `.env`:

```
STRAVA_CLIENT_ID=<twój client id>
STRAVA_CLIENT_SECRET=<twój client secret>
```

Następnie uruchom one-time auth (otworzy przeglądarkę, zalogujesz się przez Stravę, wygeneruje refresh token):

```bash
npm run auth
```

Skrypt powinien dopisać `STRAVA_REFRESH_TOKEN=...` i `STRAVA_ACCESS_TOKEN=...` do `.env`.

## 4. Rejestracja MCP w Claude Code

W katalogu projektu:

```bash
claude mcp add strava --scope project node /Users/tomaszprzebieracz/projects/maraton-chicago-2026/strava-mcp/dist/server.js
```

Lub edytuj `.claude/settings.json` ręcznie (przykład w pliku poniżej).

## 5. Test

Restart Claude Code w tym katalogu. Wpisz:

```
/mcp
```

Powinno pokazać `strava` jako connected. Następnie:

```
Pobierz moje 5 ostatnich aktywności ze Stravy
```

Jeśli zwróci listę → działa. Wtedy używasz `/coach-update` przy każdej rozmowie.

## 6. Refresh tokenów

Strava access token wygasa po 6h, refresh token jest wieczny (do dezautoryzacji). MCP server (r-huijts/strava-mcp) sam odświeża access tokeny przy każdym wywołaniu, więc nie musisz nic robić.

Jeśli kiedyś dostaniesz błąd „401 unauthorized" → wygenerowano nowy refresh token, powtórz krok 3 (`npm run auth`).

## Troubleshooting

- **„Cannot connect to Strava":** sprawdź czy `.env` ma wszystkie 4 zmienne (CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, ACCESS_TOKEN)
- **MCP nie pojawia się w `/mcp`:** restart Claude Code (zamknij wszystkie okna), `claude mcp list` żeby sprawdzić rejestrację
- **Brak HR w danych:** w aplikacji Strava na telefonie sprawdź czy aktywności mają HR (jeśli zegarek nie sparowany z Stravą, HR nie zostanie zaimportowany)

## Co Claude może po podpięciu

- Pobierać listę aktywności z dowolnego okresu
- Pobierać szczegóły jednego treningu (laps, splits)
- Pobierać streams: HR, pace, altitude, cadence — minutowo
- Liczyć strefy HR (% czasu w Z1–Z5)
- Wykrywać HR drift na long runach
- Komentować treningi vs plan i sugerować korekty

## Co Claude NIE może

- Pisać do Stravy (np. dodawać aktywności, edytować nazwy) — MCP jest read-only
- Czytać aktywności znajomych
- Czytać segmentów / Strava clubs
