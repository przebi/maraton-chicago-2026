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
 ("note", "Maciek — jesz dużo i bazę masz opanowaną, szacun. Rzecz w tym, że dość MONOTONNIE, a przy 85 km/tydz to właśnie różnorodność robi różnicę. Pomyśl o swoim 5K: 19:49 z asekuracją startu = miałeś zapas, zostawiłeś wynik na stole. Z jedzeniem jest podobnie — nie brakuje Ci ILOŚCI, tylko RÓŻNORODNOŚCI. Każdy produkt niesie co innego: żelazo, różne aminokwasy, witaminy, antyoksydanty, błonnik dla jelit. Jedząc w kółko to samo — nawet dużo — zostawiasz ciche luki, które obcinają regenerację i formę. To najtańszy sposób na ostatnie parę procent: nie jedz WIĘCEJ, jedz RÓŻNIEJ.", "", ""),

 ("section", "DLACZEGO RÓŻNORODNOŚĆ — Twój rachunek", "", ""),
 ("row", "Co ZYSKUJESZ", "Pełen komplet mikroskładników = lepsza regeneracja, stabilna energia, mocniejsza odporność. Różnorodna dieta domyka luki (żelazo, witaminy), które przy monotonnej cicho Cię hamują. To bywa różnica między 1:30 a 1:27.", ""),
 ("row", "Co daje MONOTONIA", "Nawet dużo jedzenia, ale wciąż to samo = powtarzalne braki (np. żelazo, część witamin), uboższa flora jelitowa, znużenie jedzeniem. Ciało nie ma z czego zbudować pełnej regeneracji — i forma stoi mimo treningu.", ""),
 ("row", "Twoja przewaga TERAZ", "Masz 19 lat i rośniesz — Twoje ciało chce budować formę jak nigdy później. Dostarcz mu PEŁNE spektrum budulca, a wykorzystasz to okno maksymalnie. Ono się nie powtórzy.", ""),

 ("section", "🍝 TWOJE DANIA — ubierz je, nie zmniejszaj", "", ""),
 ("row", "Zasada", "Nie musisz jeść MNIEJ — masz jeść PEŁNIEJ. Twoje węglowe bomby zostają, tylko dorzuć do nich białko i warzywa. To samo jedzenie, 2-3x więcej wartości. Węgli masz aż nadto — brakuje tego, co się na nie kładzie.", ""),
 ("row", "8 naleśników z dżemem", "Same węgle i cukier, zero białka. FIX: do środka twaróg / serek homogenizowany, obok jogurt grecki albo szklanka mleka. Dżem zostaje — dorzucasz tylko białko na regenerację.", ""),
 ("row", "2 kg makaronu… samego", "Makaron to BAZA, nie danie. Sam = puste węgle. FIX: sos z mięsem mielonym / tuńczykiem / kurczakiem + warzywa (choćby mrożonka) + oliwa + ser. Tyle samo makaronu, 3x więcej wartości.", ""),
 ("row", "Rosół (sama woda)", "Woda to nie posiłek. FIX: wrzuć mięso z rosołu, marchewkę i inne warzywa, makaron albo lane kluski. Dopiero wtedy to jest posiłek, a nie napój.", ""),
 ("row", "4 kromki chleba + 1 zgniła rzodkiewka", "Legendarne. Kanapka to nośnik na BIAŁKO, nie na samotną (zwłoki) rzodkiewkę. FIX: na chleb ser / wędlina / hummus / tuńczyk / twarożek + świeże warzywo (pomidor, ogórek, papryka — i tak, świeża rzodkiewka może zostać).", ""),

 ("section", "ILE I JAK CZĘSTO", "", ""),
 ("row", "Kalorie masz ogarnięte", "Jesz DUŻO i to dobrze — o ilość się nie martwimy. Jesteś szczupły (57/175), co jest OK. Cała gra toczy się o RÓŻNORODNOŚĆ i o to, co dokładasz do węgli (patrz wyżej).", ""),
 ("row", "Jedz co ~3 h (5 posiłków)", "PO CO: białko wchłaniasz po ~25-30 g na raz. Wal 2 kg makaronu za jednym zamachem = dużo węgli naraz i tak czy siak potem głód. Lepiej rozłożyć na 5 posiłków — każdy z białkiem. NIGDY nie pomijaj śniadania.", ""),

 ("section", "CO DOKŁADAĆ I PO CO", "", ""),
 ("row", "Węglowodany = masz ich w bród", "To Twoje paliwo i masz go pod dostatkiem (naleśniki, makaron, chleb). Problem nie w węglach — tylko w tym, że jesz je SAME. Zostają, dokładamy resztę.", "ryż, makaron, ziemniaki, owsianka, pieczywo, kasze, banany, owoce"),
 ("row", "Białko = TEGO Ci brakuje", "PO CO: naprawia mięśnie po treningu i buduje nowe (rośniesz). To brakujący element w Twoich daniach. JAK: dorzuć do KAŻDEGO posiłku porcję ~jak Twoja dłoń.", "kurczak, ryba, twaróg, jogurt grecki/skyr, mięso, mleko, strączki, jaja"),
 ("row", "Jaja — po prostu je jedz", "PO CO: najlepsze białko jakie jest + żelazo, tanie i szybkie. JAK, jak nie lubisz solo: jajecznica z serem/szynką/warzywami, omlet, wrzuć do makaronu/ryżu, na twardo do kanapki. Jak NAPRAWDĘ nie możesz — zamień na odżywkę białkową (whey) do mleka, twaróg albo skyr. Ale najpierw spróbuj.", ""),
 ("row", "Tłuszcze", "PO CO: hormony i wchłanianie witamin — nie wycinaj ich. JAK: garść orzechów, łyżka oliwy, kawałek awokado dziennie.", "oliwa, orzechy, masło orzechowe, awokado, tłuste ryby"),

 ("section", "⭐ PRZED TRENINGIEM — co i po co", "", ""),
 ("row", "Po co jeść przed", "Żebyś miał paliwo na cały trening i nie padł w połowie.", ""),
 ("row", "2-3 h przed", "Normalny posiłek z węglami.", "owsianka, makaron, kanapki, ryż"),
 ("row", "30-60 min przed", "Coś małego i szybkiego.", "banan, chleb z miodem, baton"),
 ("row", "Rano na jakość / long", "MUSISZ coś zjeść (choćby banan z miodem ~1 h wcześniej) — na pusto nie pociągniesz mocnej sesji. Krótki, spokojny bieg rano możesz zrobić na czczo.", ""),
 ("row", "Czego NIE jeść tuż przed", "Dużo tłustego, dużo białka albo błonnika — będzie Ci leżeć w brzuchu i odbijać.", ""),

 ("section", "⭐⭐ ZARAZ PO TRENINGU — Twój największy błąd", "", ""),
 ("row", "Twój błąd nr 1", "Węgli ładujesz dużo — ale NIE zaraz po treningu, tylko później. I to jest błąd. Tuż po wysiłku mięśnie są jak gąbka: chłoną paliwo i białko najlepiej. Zjesz makaron dopiero 2-3 h potem = okno regeneracji w plecy.", ""),
 ("row", "Jak naprawić", "W ciągu 30 MINUT po treningu wrzuć coś z węglami + białkiem. Duży posiłek (Twój makaron) zjedz normalnie 1-2 h później — ale najpierw zamknij okno.", ""),
 ("row", "Co najłatwiej", "Mleko czekoladowe — idealne (węgle + białko), smaczne, samo się pije. Albo shake: mleko + banan + masło orzechowe + płatki + miód.", ""),
 ("row", "Inne opcje", "Jogurt grecki + granola + owoc, albo twaróg + owoc, albo baton białkowy + banan.", ""),

 ("section", "UROZMAICAJ — proste sposoby", "", ""),
 ("row", "Rotuj białko", "Nie w kółko to samo — zmieniaj: raz kurczak, raz ryba, raz twaróg, raz strączki, raz wołowina. Różne źródła = pełen zestaw aminokwasów + żelazo z mięsa.", ""),
 ("row", "Jedz kolory", "Różnokolorowe warzywa/owoce = różne witaminy i antyoksydanty (regeneracja, odporność). Minimum: coś zielonego + coś kolorowego codziennie. Mrożonki się liczą.", ""),
 ("row", "Zmieniaj węgle", "Nie tylko makaron i chleb — rotuj ryż, kasze (gryczana ma żelazo!), ziemniaki, owsianka. Różne = więcej mikroskładników i błonnika.", ""),
 ("row", "Ryby 2x w tygodniu", "Omega-3 = przeciwzapalne, wspiera regenerację. Łosoś, makrela, sardynki — nawet z puszki się liczą.", ""),
 ("row", "Shake jako dodatek", "Mleko + banan + masło orzechowe + płatki + miód. Wygodny sposób, żeby wcisnąć białko i owoc — zwłaszcza po treningu.", ""),

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

 ("section", "🚩 UWAŻAJ — luki mimo pełnego brzucha", "", ""),
 ("row", "Sygnały i co robić", "Ciągłe zmęczenie, częste przeziębienia, kontuzje, forma stoi mimo treningu — to mogą być BRAKI (żelazo, witaminy), nie brak kalorii. Fix: urozmaić + domknij okno po treningu. Nie ustępuje → powiedz tacie, zróbcie badania (ferrytyna, morfologia, wit. D).", ""),

 ("section", "✅ ZACZNIJ OD JEDNEGO", "", ""),
 ("row", "Nie musisz wszystkiego naraz", "Zacznij od JEDNEJ rzeczy: mleko czekoladowe albo shake ZARAZ po każdym treningu. Tydzień i sam poczujesz różnicę (lepsza regeneracja, więcej energii, mocniejsze biegi). Jak zadziała — dokładasz resztę. To eksperyment, który sam sobie zweryfikujesz — a lubisz mieć rację.", ""),
 ("note", "Podsumowanie: masz talent i jesz dużo — brakuje tylko RÓŻNORODNOŚCI, białka NA węglach i jedzenia ZARAZ po treningu. Węgle zostają, dokładasz resztę. Tyle dzieli Cię od pełnego wykorzystania tego, co już robisz na treningu. Jedz jak zawodnik, którym jesteś.", "", ""),
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
        if kind == "row" and c:  # zwiń przykłady do tekstu → układ 2-kol (etykieta | tekst)
            b, c = f"{b}   ·   Np.: {c}", ""
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
                         "fields": "userEnteredValue,userEnteredFormat.backgroundColor,userEnteredFormat.textFormat",
                         "start": {"sheetId": sid, "rowIndex": 0, "columnIndex": 0}}},
    ]
    # scalanie: nagłówki/nota = A:C (cała szerokość); wiersze = B:C (etykieta | szeroki tekst)
    for r, (kind, *_rest) in enumerate(ROWS):
        c0 = 0 if kind in ("title", "section", "note") else 1
        requests.append({"mergeCells": {
            "range": {"sheetId": sid, "startRowIndex": r, "endRowIndex": r + 1,
                      "startColumnIndex": c0, "endColumnIndex": ncols},
            "mergeType": "MERGE_ALL"}})
    for i, px in enumerate((200, 480, 220)):  # A=etykieta, B:C scalone = ~700 px
        requests.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": i, "endIndex": i + 1},
            "properties": {"pixelSize": px}, "fields": "pixelSize"}})
    for r, (kind, a, b, c) in enumerate(ROWS):
        if kind in ("title", "section"):
            lines = 1
        elif kind == "note":
            lines = line_count(a, 132)  # scalone A:C (~900 px)
        else:
            txt = f"{b}   ·   Np.: {c}" if c else b  # tekst w scalonym B:C (~700 px)
            lines = max(line_count(a, 27), line_count(txt, 108))
        requests.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "ROWS", "startIndex": r, "endIndex": r + 1},
            "properties": {"pixelSize": max(26, lines * 17 + 9)}, "fields": "pixelSize"}})

    sh.batch_update({"requests": requests})
    print(f"OK — zakładka '{TAB}' ({nrows} wierszy, do Maćka) w arkuszu {sheet_id}")


if __name__ == "__main__":
    main()
