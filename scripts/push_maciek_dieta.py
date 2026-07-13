#!/usr/bin/env python3
"""
Tworzy/odświeża zakładkę "Dieta" w arkuszu Maćka — praktyczny przewodnik żywieniowy
dla nastoletniego biegacza HM (80-90 km/tydz), który JE ZA MAŁO (ryzyko RED-S).
Treść = źródło prawdy tutaj. Uruchom tak jak push_maciek_sheet.py:
    python3 scripts/push_maciek_dieta.py <SHEET_ID> [KEY_PATH]
"""
import os
import sys
import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
DEFAULT_KEY = os.path.expanduser("~/.config/gcloud/maciek-sa.json")
TAB = "Dieta"

# kind, A (etykieta), B (ile/dlaczego), C (konkretnie / produkty)
ROWS = [
 ("title", "🍽️  DIETA — Maciek (HM sub-1:30 · 80-90 km/tydz · 19 lat)", "", ""),
 ("note", "Problem: je NIEREGULARNIE — albo nic („suchy chleb + zgniła rzodkiewka\"), albo tona makaronu na raz jak neandertalczyk. Oba złe. A on MA 19 LAT (wciąż ROŚNIE) + trenuje intensywnie 85 km/tydz → potrzeby OGROMNE: wzrost + trening naraz. Za mało / na raz = RED-S: spada HRV, rośnie RHR, kontuzje, forma stoi, u młodego cierpią KOŚCI i HORMONY. Priorytet: JEŚĆ DUŻO i RÓWNO (5 posiłków), nie jednym zamachem. Jedzenie = część treningu.", "", ""),

 ("section", "ILE JEŚĆ", "", ""),
 ("row", "Kalorie", "~3000-3800 kcal/dzień (dużo!). Górna granica w dni z longiem/jakością. 57 kg / 175 cm = BMI 18,6 — NA DOLNEJ GRANICY (18,5 to niedowaga). Przy 85 km/tydz + wzroście spokojnie może dołożyć 1-2 kg MIĘŚNI (moc, mniej kontuzji, hormony) — byle nie tłuszcz. NIE bój się jeść.", ""),
 ("row", "Równo, NIE na raz", "Tona makaronu jednym zamachem ≠ 5 posiłków. Białko wchłania się ~25-30 g/posiłek (reszta zmarnowana), glikogen odbudowuje się CAŁY dzień. Jeden wielki posiłek = część leci w kosz + ciężko potem trenować.", ""),
 ("row", "Częstotliwość", "5 posiłków co ~3 h. NIGDY nie pomijaj śniadania. Nie trenuj na pusto (poza krótkim easy rano).", ""),

 ("section", "MAKRO — na każdym talerzu", "", ""),
 ("row", "Węglowodany = PALIWO", "5-8 g/kg = ~285-450 g/dzień (~50-60% kalorii). Najważniejsze dla biegacza — pusty bak = zła jakość + zmęczenie.", "ryż, makaron, ziemniaki, owsianka, pieczywo, kasze, banany, owoce, miód, dżem"),
 ("row", "Białko = REGENERACJA", "1,6-2,0 g/kg = ~95-115 g/dzień (u rosnącego górna granica). Rozłóż na 4-5 posiłków po ~25-30 g (lepiej niż wszystko naraz).", "jaja, kurczak, indyk, ryba, twaróg, jogurt grecki/skyr, mięso, mleko, strączki"),
 ("row", "🥚 JAJA — najpierw przemyć", "Za dobre żeby olewać (kompletne białko, żelazo, cholina, tanie). Nie lubi solo → UKRYJ: jajecznica z serem/szynką/warzywami, omlet, na twardo w kanapce/sałatce, wrzucone do makaronu/ryżu, shakshuka, w naleśnikach/plackach.", ""),
 ("row", "…a jak dalej NIE tknie", "Nie walczcie — pokryj to samo czym innym. NAJŁATWIEJ: odżywka białkowa (whey) do mleka+banana. Dalej: twaróg, skyr/jogurt grecki, dużo mleka, tuńczyk/makrela z puszki, kurczak (batch-cook), hummus, strączki. Białko na śniadanie bez jaj = skyr / twaróg / shake.", ""),
 ("row", "Tłuszcze", "~1 g/kg = ~55-60 g, zdrowe. NIE eliminować — hormony + wchłanianie witamin.", "oliwa, orzechy, masło orzechowe, awokado, tłuste ryby"),

 ("section", "MIKRO — nie olewać", "", ""),
 ("row", "🔴 ŻELAZO (krytyczne)", "Biegacz wytrzymałościowy + nastolatek = grupa ryzyka. Niska ferrytyna = zmęczenie, zadyszka, słabe wyniki MIMO treningu. ZBADAJ (morfologia + ferrytyna). Jedz z witaminą C, unikaj kawy/herbaty do posiłku żelaznego.", "czerwone mięso, wątróbka, jaja, kasza gryczana, strączki, szpinak + papryka/cytrus"),
 ("row", "Wapń + wit. D", "Kości przy dużej objętości (ryzyko złamań przeciążeniowych). D3 suplement, zwł. jesień/zima.", "nabiał, twaróg, jogurt, D3 kapsułki"),
 ("row", "Elektrolity / sód", "Przy poceniu (upał, długie). Sól w jedzeniu OK; izotonik na długie.", "sól, izotonik, banany (potas)"),

 ("section", "TIMING wokół treningu", "", ""),
 ("row", "PRZED", "2-3 h przed: normalny posiłek węglowy. 30-60 min przed: mały szybki węgiel. Jakość rano → MUSISZ coś zjeść (banan+miód ~1 h przed). Krótki easy rano można na czczo. Unikaj tłuszczu/białka/błonnika tuż przed — leży w brzuchu.", "banan, chleb z miodem/dżemem, baton, ryż, płatki, owsianka"),
 ("row", "PO — ZARAZ (do 30 min) ⭐", "NAJWAŻNIEJSZE: jedz OD RAZU po treningu, NIE czekaj do obiadu. Węgle (glikogen) + białko (mięśnie) ~3:1. Normalny posiłek 1-2 h później. Po jakości/longu — obowiązkowo.", "mleko czekoladowe, shake (mleko+banan+masło orzech.+owsianka+miód), jogurt grecki+granola+owoc, twaróg+owoc"),
 ("row", "Long / quality", "Dojedź węglami wcześniej. Bieg >75-90 min → węgle W TRAKCIE 30-60 g/h.", "żele, banan, izotonik, żelki"),

 ("section", "ŁATWE KALORIE (dobijaj bez wysiłku — bo je za mało)", "", ""),
 ("row", "Shake-bomba (codziennie)", "Mleko + banan + 2 łyżki masła orzechowego + garść owsianki + miód = 600+ kcal jednym kubkiem.", ""),
 ("row", "Dodatki do posiłków", "Dolewaj oliwę do obiadu, dokładaj ser, orzechy, awokado. Suszone owoce + orzechy jako przekąska.", ""),
 ("row", "Mleko czekoladowe", "Idealny post-workout: węgle + białko, tanie, je się samo.", ""),

 ("section", "PRZYKŁADOWY DZIEŃ (~3200-3500 kcal)", "", ""),
 ("row", "Śniadanie", "Owsianka (płatki + mleko + banan + masło orzechowe + miód) + białko: jajecznica LUB skyr/twaróg/shake (jak nie tknie jaj)", ""),
 ("row", "II śniadanie", "2-3 kanapki (pełnoziarniste + ser/wędlina/szynka/hummus) + owoc", ""),
 ("row", "Przed treningiem", "Banan / baton / chleb z dżemem", ""),
 ("row", "Po treningu", "Mleko czekoladowe lub shake-bomba + owoc", ""),
 ("row", "Obiad", "Mięso/ryba + DUŻA porcja ryżu/makaronu/ziemniaków + warzywa + oliwa", ""),
 ("row", "Podwieczorek", "Jogurt grecki + granola + owoce + orzechy", ""),
 ("row", "Kolacja", "Twaróg/mięso/ryba (lub jajka jeśli zje) + pieczywo/kasza + warzywa", ""),

 ("section", "🏁 PRASKI NOCNY (start 20:30) — dzień startu", "", ""),
 ("row", "W ciągu dnia", "Normalne posiłki węglowe, NIC nowego/ciężkiego. Śniadanie + obiad węglowy (makaron/ryż) ~13-14.", ""),
 ("row", "Przedstartowo", "Ostatni większy posiłek lekki-węglowy ~17:00-17:30 (3 h przed). Potem mały węgiel ~30-60 min przed (banan/baton).", ""),
 ("row", "W trakcie", "HM ~1:28 → 1-2 żele (~40-50 min i ew. 70 min) + łyk izotoniku. PRZETESTUJ na treningu, nie pierwszy raz na starcie!", ""),

 ("section", "🚩 CZERWONE FLAGI (niedobór energii / RED-S)", "", ""),
 ("row", "Sygnały", "Ciągłe zmęczenie, spadek HRV / wzrost RHR, częste infekcje, kontuzje, brak progresu mimo treningu, marznięcie. U młodych: wpływ na hormony i kości.", ""),
 ("row", "Reakcja", "Dosyp kalorii (zwł. węgli), więcej PO treningu, dzień lżejszy. Utrzymuje się → dietetyk sportowy + badania (ferrytyna, morfologia, wit. D).", ""),
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
                tf = {"italic": True, "fontSize": 10, "foregroundColor": color("5D4037")}
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

    requests = [
        {"repeatCell": {"range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": nrows,
                                   "startColumnIndex": 0, "endColumnIndex": ncols},
                        "cell": {"userEnteredFormat": {"verticalAlignment": "TOP",
                                                        "wrapStrategy": "WRAP"}},
                        "fields": "userEnteredFormat.verticalAlignment,userEnteredFormat.wrapStrategy"}},
        {"updateCells": {"rows": grid,
                         "fields": "userEnteredValue,userEnteredFormat",
                         "start": {"sheetId": sid, "rowIndex": 0, "columnIndex": 0}}},
    ]
    for i, px in enumerate((190, 380, 300)):
        requests.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": i, "endIndex": i + 1},
            "properties": {"pixelSize": px}, "fields": "pixelSize"}})
    for r, (kind, a, b, c) in enumerate(ROWS):
        if kind in ("title", "section"):
            lines = 1
        else:
            lines = max(line_count(a, 27), line_count(b, 60), line_count(c, 46))
        requests.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "ROWS", "startIndex": r, "endIndex": r + 1},
            "properties": {"pixelSize": max(24, lines * 17 + 8)}, "fields": "pixelSize"}})

    sh.batch_update({"requests": requests})
    print(f"OK — zakładka '{TAB}' ({nrows} wierszy) w arkuszu {sheet_id}")


if __name__ == "__main__":
    main()
