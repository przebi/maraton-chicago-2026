#!/usr/bin/env python3
"""
Zakładka "Dieta" w arkuszu Maćka — napisana DO NIEGO (per "Ty"): po co i jak jeść.
Nastoletni biegacz HM (85 km/tydz, 19 lat, wciąż rośnie, 57 kg), który je za mało.
Uruchom:  python3 scripts/push_maciek_dieta.py <SHEET_ID> [KEY_PATH]
"""
import os
import sys
import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
DEFAULT_KEY = os.path.expanduser("~/.config/gcloud/maciek-sa.json")
TAB = "Dieta"

# kind, A (etykieta), B (po co + jak), C (konkretnie / produkty)
ROWS = [
 ("title", "🍽️  DIETA MACIEJA — jak zamienić trening w wynik (przeczytaj do końca)", "", ""),
 ("note", "Maciek — jesteś bystry (2 kierunki, średnia prawie 5.0), więc bez ściemy, na argumenty. Właśnie zrobiłeś 5K w 19:49 ASEKURUJĄC start (pierwsze 3 km wolniej, potem 3:38 — miałeś zapas). Masz silnik, ale zostawiłeś wynik na stole. Z jedzeniem robisz DOKŁADNIE to samo: harujesz na ciężkich kilometrach, a potem nie dowozisz paliwa i białka — więc połowa adaptacji leci w kosz. To jak trenować i kasować sobie połowę efektu. Jedzenie to jedyna DARMOWA PRĘDKOŚĆ jaką masz: nie kosztuje ani jednego treningu więcej, a daje wynik. 3 minuty czytania — a decyduje o Twoim PB.", "", ""),

 ("section", "DLACZEGO WARTO — Twój rachunek", "", ""),
 ("row", "Co ZYSKUJESZ", "Mocniejsza końcówka (pełny bak = nie gaśniesz na 16. km), szybsza regeneracja (trenujesz częściej bez zajechania), mniej kontuzji i infekcji. Konkret: z sub-1:30 robi się 1:27, a cały blok idzie bez przerw.", ""),
 ("row", "Co TRACISZ jak olewasz", "Niedojadanie przy 85 km/tydz = RED-S: spada HRV, rośnie tętno spoczynkowe, forma STOI mimo treningu, łapiesz każdą infekcję, a u 19-latka cierpią kości i hormony. To dokładnie to, co kończy zapowiadające się kariery — nie brak talentu, tylko głód i przerwy.", ""),
 ("row", "Twoja przewaga TERAZ", "Masz 19 lat i rośniesz — Twoje ciało chce budować mięśnie i formę jak nigdy później w życiu. Dokarm je teraz i zrobisz skok, na który starsi haruja latami. To okno się nie powtórzy.", ""),

 ("section", "ILE I JAK CZĘSTO", "", ""),
 ("row", "Ile jeść", "Potrzebujesz ~3000-3800 kcal dziennie — dużo, bo biegasz i rośniesz. Ważysz 57 kg przy 175 cm (chudo). Nie bój się jeść — spokojnie możesz dołożyć 1-2 kg mięśni, będziesz mocniejszy i mniej podatny na kontuzje.", ""),
 ("row", "Jedz co ~3 h (5 posiłków)", "PO CO: białko wchłaniasz po ~25-30 g na raz, a paliwo (glikogen) odbudowujesz przez CAŁY dzień. Zjesz wszystko naraz = połowa się marnuje i potem ciężko biec. JAK: śniadanie → II śniadanie → obiad → podwieczorek → kolacja. NIGDY nie pomijaj śniadania.", ""),

 ("section", "CO JEŚĆ I PO CO", "", ""),
 ("row", "Węglowodany = TWOJE PALIWO", "PO CO: to benzyna do biegania. Pusty bak = słaby trening i zmęczenie. JAK: dokładaj do KAŻDEGO posiłku, spora porcja.", "ryż, makaron, ziemniaki, owsianka, pieczywo, kasze, banany, owoce, miód, dżem"),
 ("row", "Białko = ODBUDOWA", "PO CO: naprawia mięśnie po treningu i buduje nowe (przecież rośniesz). JAK: trochę w każdym posiłku (porcja ~jak Twoja dłoń).", "kurczak, ryba, twaróg, jogurt grecki/skyr, mięso, mleko, strączki, jaja"),
 ("row", "Jaja — po prostu je jedz", "PO CO: najlepsze białko jakie jest + żelazo, tanie i szybkie. JAK, jak nie lubisz solo: jajecznica z serem/szynką/warzywami, omlet, wrzuć do makaronu/ryżu, na twardo do kanapki. Jak NAPRAWDĘ nie możesz — zamień na odżywkę białkową (whey) do mleka, twaróg albo skyr. Ale najpierw spróbuj.", ""),
 ("row", "Tłuszcze", "PO CO: hormony i wchłanianie witamin — nie wycinaj ich. JAK: garść orzechów, łyżka oliwy, kawałek awokado dziennie.", "oliwa, orzechy, masło orzechowe, awokado, tłuste ryby"),

 ("section", "⭐ PRZED TRENINGIEM — co i po co", "", ""),
 ("row", "Po co jeść przed", "Żebyś miał paliwo na cały trening i nie padł w połowie.", ""),
 ("row", "2-3 h przed", "Normalny posiłek z węglami.", "owsianka, makaron, kanapki, ryż"),
 ("row", "30-60 min przed", "Coś małego i szybkiego.", "banan, chleb z miodem, baton"),
 ("row", "Rano na jakość / long", "MUSISZ coś zjeść (choćby banan z miodem ~1 h wcześniej) — na pusto nie pociągniesz mocnej sesji. Krótki, spokojny bieg rano możesz zrobić na czczo.", ""),
 ("row", "Czego NIE jeść tuż przed", "Dużo tłustego, dużo białka albo błonnika — będzie Ci leżeć w brzuchu i odbijać.", ""),

 ("section", "⭐⭐ ZARAZ PO TRENINGU — najważniejsze!", "", ""),
 ("row", "Po co", "Zaraz po treningu Twoje mięśnie są jak gąbka — najlepiej wchłaniają paliwo i białko. To okno regeneracji, nie zmarnuj go.", ""),
 ("row", "Kiedy", "W ciągu 30 MINUT po treningu. NIE czekaj do obiadu.", ""),
 ("row", "Co najłatwiej", "Mleko czekoladowe — idealne (węgle + białko), smaczne, samo się pije. Albo shake: mleko + banan + masło orzechowe + płatki + miód.", ""),
 ("row", "Inne opcje", "Jogurt grecki + granola + owoc, albo twaróg + owoc. A normalny obiad zjedz normalnie 1-2 h później.", ""),

 ("section", "JAK ZJEŚĆ WIĘCEJ bez wysiłku", "", ""),
 ("row", "Shake codziennie", "Mleko + banan + 2 łyżki masła orzechowego + garść płatków + miód = 600 kcal jednym kubkiem. Zrób blenderem i wypij.", ""),
 ("row", "Dokładaj do posiłków", "Polej obiad oliwą, dorzuć ser, orzechy, awokado. Przekąska w ciągu dnia: orzechy + suszone owoce.", ""),

 ("section", "TWÓJ DZIEŃ (przykład, ~3200-3500 kcal)", "", ""),
 ("row", "Śniadanie", "Owsianka (płatki + mleko + banan + masło orzechowe + miód) + białko: jajecznica LUB skyr/twaróg/shake", ""),
 ("row", "II śniadanie", "2-3 kanapki (pełnoziarniste + ser/wędlina/szynka/hummus) + owoc", ""),
 ("row", "Przed treningiem", "Banan / baton / chleb z miodem", ""),
 ("row", "ZARAZ po treningu", "Mleko czekoladowe lub shake + owoc", ""),
 ("row", "Obiad", "Mięso/ryba + DUŻA porcja ryżu/makaronu/ziemniaków + warzywa + oliwa", ""),
 ("row", "Podwieczorek", "Jogurt grecki + granola + owoce + orzechy", ""),
 ("row", "Kolacja", "Twaróg/mięso/ryba (lub jajka) + pieczywo/kasza + warzywa", ""),

 ("section", "🔴 ŻELAZO — zbadaj to", "", ""),
 ("row", "Po co i jak", "Żelazo nosi tlen we krwi. Za mało (a biegacze często mają) = jesteś zmęczony i zadyszany MIMO formy. Zbadaj ferrytynę (proste badanie krwi). Jedz z witaminą C, a bez kawy/herbaty do tego posiłku (blokują wchłanianie).", "czerwone mięso, wątróbka, kasza gryczana, strączki, szpinak, buraki + papryka/cytrus"),

 ("section", "🏁 PRASKI (nocny start 20:30) — dzień wyścigu", "", ""),
 ("row", "W ciągu dnia", "Normalnie jedz węgle, nic nowego ani ciężkiego. Obiad węglowy (makaron/ryż) ~13-14.", ""),
 ("row", "Przed startem", "Ostatni większy, lekki posiłek ~17:00-17:30 (3 h przed). Potem mały węgiel ~30-60 min przed startem (banan/baton).", ""),
 ("row", "W trakcie", "Weź 1-2 żele (ok. 40-50 min i ~70 min) + łyk izotoniku. PRZETESTUJ je wcześniej na treningu — nie pierwszy raz na wyścigu!", ""),

 ("section", "🚩 UWAŻAJ — znaki że jesz za mało", "", ""),
 ("row", "Sygnały i co robić", "Ciągłe zmęczenie, częste przeziębienia, kontuzje, forma stoi, marzniesz. Jak to widzisz — jedz WIĘCEJ, zwłaszcza zaraz po treningu i węgli. Nie ustępuje → powiedz tacie, zróbcie badania (ferrytyna, morfologia, wit. D).", ""),

 ("section", "✅ ZACZNIJ OD JEDNEGO", "", ""),
 ("row", "Nie musisz wszystkiego naraz", "Zacznij od JEDNEJ rzeczy: mleko czekoladowe albo shake ZARAZ po każdym treningu. Tydzień i sam poczujesz różnicę (lepsza regeneracja, więcej energii, mocniejsze biegi). Jak zadziała — dokładasz resztę. To eksperyment, który sam sobie zweryfikujesz — a lubisz mieć rację.", ""),
 ("note", "Podsumowanie: masz talent na dużo więcej niż sub-1:30. Jedyne czego brakuje to paliwo. Trening masz zrobiony — nie wyrzucaj połowy efektu przez pusty talerz. Jedz jak zawodnik, którym już jesteś.", "", ""),
]


def main():
    sheet_id = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("MACIEK_SHEET_ID")
    key = os.path.expanduser(sys.argv[2] if len(sys.argv) > 2
                             else os.environ.get("MACIEK_SA_KEY", DEFAULT_KEY))
    if not sheet_id or not os.path.exists(key):
        sys.exit("Podaj SHEET_ID i ścieżkę do klucza SA.")
    gc = gspread.authorize(Credentials.from_service_account_file(key, scopes=SCOPES))
    sh = gc.open_by_key(sheet_id)

    nrows, ncols = len(ROWS), 3
    try:
        ws = sh.worksheet(TAB)
        ws.clear()
        ws.resize(rows=nrows, cols=ncols)
    except gspread.WorksheetNotFound:
        ws = sh.add_worksheet(title=TAB, rows=nrows, cols=ncols)
    sid = ws.id

    def color(hex6):
        return {"red": int(hex6[0:2], 16) / 255, "green": int(hex6[2:4], 16) / 255,
                "blue": int(hex6[4:6], 16) / 255}

    grid = []
    for kind, a, b, c in ROWS:
        cells = []
        for col, val in enumerate((a, b, c)):
            fmt = {}
            tf = {}
            if kind == "title":
                fmt["backgroundColor"] = color("1F2A37")
                tf = {"bold": True, "fontSize": 13, "foregroundColor": color("FFFFFF")}
            elif kind == "section":
                fmt["backgroundColor"] = color("2E7D32")
                tf = {"bold": True, "fontSize": 11, "foregroundColor": color("FFFFFF")}
            elif kind == "note":
                fmt["backgroundColor"] = color("FFF8E1")
                tf = {"fontSize": 10, "foregroundColor": color("5D4037")}
            else:  # row
                fmt["backgroundColor"] = color("FFFFFF")
                if col == 0:
                    tf = {"bold": True, "fontSize": 10, "foregroundColor": color("2E7D32")}
                elif col == 2:
                    tf = {"fontSize": 10, "foregroundColor": color("6B7280"), "italic": True}
                else:
                    tf = {"fontSize": 10, "foregroundColor": color("374151")}
            if tf:
                fmt["textFormat"] = tf
            cells.append({"userEnteredValue": {"stringValue": val} if val else {"stringValue": ""},
                          "userEnteredFormat": fmt})
        grid.append({"values": cells})

    def line_count(t, cpl):
        return max(1, -(-len(t) // cpl)) if t else 1

    full = {"sheetId": sid, "startRowIndex": 0, "endRowIndex": nrows,
            "startColumnIndex": 0, "endColumnIndex": ncols}
    requests = [
        {"unmergeCells": {"range": full}},
        {"repeatCell": {"range": full,
                        "cell": {"userEnteredFormat": {"verticalAlignment": "TOP",
                                                        "wrapStrategy": "WRAP"}},
                        "fields": "userEnteredFormat.verticalAlignment,userEnteredFormat.wrapStrategy"}},
        {"updateCells": {"rows": grid,
                         "fields": "userEnteredValue,userEnteredFormat",
                         "start": {"sheetId": sid, "rowIndex": 0, "columnIndex": 0}}},
    ]
    # scal A:C dla nagłówków/noty — długi tekst na całą szerokość, nie w słupek
    for r, (kind, *_rest) in enumerate(ROWS):
        if kind in ("title", "section", "note"):
            requests.append({"mergeCells": {
                "range": {"sheetId": sid, "startRowIndex": r, "endRowIndex": r + 1,
                          "startColumnIndex": 0, "endColumnIndex": ncols},
                "mergeType": "MERGE_ALL"}})
    for i, px in enumerate((210, 400, 280)):
        requests.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": i, "endIndex": i + 1},
            "properties": {"pixelSize": px}, "fields": "pixelSize"}})
    for r, (kind, a, b, c) in enumerate(ROWS):
        if kind == "title":
            lines = 1
        elif kind == "section":
            lines = 1
        elif kind == "note":
            lines = line_count(a, 130)  # scalone A:C (~890 px)
        else:
            lines = max(line_count(a, 30), line_count(b, 63), line_count(c, 42))
        requests.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "ROWS", "startIndex": r, "endIndex": r + 1},
            "properties": {"pixelSize": max(26, lines * 17 + 9)}, "fields": "pixelSize"}})

    sh.batch_update({"requests": requests})
    print(f"OK — zakładka '{TAB}' ({nrows} wierszy, do Maćka) w arkuszu {sheet_id}")


if __name__ == "__main__":
    main()
