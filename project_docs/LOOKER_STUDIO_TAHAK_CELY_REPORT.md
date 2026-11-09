# Tahák pro lektora: PISA - Česko a svět

Jen pro vedení kurzu; soubor leží mimo publikovanou složku `docs/`. Pořadí odpovídá desetistránkovému exportu reportu. **Název stránky** nastavte v navigaci reportu a vložte jej také jako textový nadpis nad obsah. **Název grafu** nastavte u příslušného grafu nebo tabulky. Zdrojové listy: `Vysledky` → `PISA_Vysledky`, `Rozlozeni` → `PISA_Rozlozeni`, `Druhy_skol_CR` → `PISA_Druhy_skol_CR`.

## 1. Česko v kontextu

**Česko v kontextu → Česko: skóre ve třech oblastech, PISA 2025** (kontrolní tabulka)

- **Pole:** dimenze `zeme`, `oblast`; metrika `skore` = Average.
- **Filtr:** `iso3 = CZE` AND `cyklus = 2025`.
- **Kontrola:** přesně 3 řádky, ne 39; matematika **477**, čtení **468**, přírodní vědy **490**.

**Česko v kontextu → tři karty ČR** (Rychlý přehled / Scorecard)

| Název stránky → Název grafu | Další pevná podmínka | Skóre |
| --- | --- | ---: |
| `Česko v kontextu` → `ČR – matematika, PISA 2025` | `oblast = Matematika` | **477** |
| `Česko v kontextu` → `ČR – čtení, PISA 2025` | `oblast = Čtení` | **468** |
| `Česko v kontextu` → `ČR – přírodní vědy, PISA 2025` | `oblast = Přírodní vědy` | **490** |

Všechny tři: zdroj `PISA_Vysledky`, metrika `skore` = Average, filtr `iso3 = CZE` AND `cyklus = 2025` AND příslušná oblast. Zobrazit celé číslo; neponechat kartu bez filtru oblasti.

## 2. Srovnání zemí

**Srovnání zemí → Přírodní vědy: bodové odhady ve vybraných zemích** (vodorovný pruhový graf)

- **Pole:** dimenze `zeme`; bez rozkladové dimenze; metrika `skore` = Average.
- **Filtr:** `typ = Zeme` AND `cyklus = 2025` AND `oblast = Přírodní vědy`.
- **Zapnout:** řazení skóre sestupně, alespoň 10 pruhů, hodnoty u pruhů, počátek osy na nule. **Vypnout:** křížové filtrování, pokud grafy nemají na kliknutí reagovat společně.
- **Kontrola:** Singapur **560**, Estonsko **527**, Česko **490**; celkem 10 zemí.

**Srovnání zemí → Skóre zemí podle oblasti, PISA 2025** (kontingenční tabulka)

- **Pole:** řádky `zeme`; sloupce `oblast`; metrika `skore` = Average.
- **Filtr:** `typ = Zeme` AND `cyklus = 2025`; **bez** filtru jedné oblasti.
- **Zapnout:** číselné hodnoty, volitelně heatmapu. **Vypnout:** řádkové a sloupcové součty.
- **Kontrola:** 10 zemí × 3 oblasti; Česko v matematice **477**. B-S-J-Z do této základní tabulky nepatří; pro region lze vytvořit zvláštní kopii s vlastním názvem.

## 3. Rozdíl vůči OECD: přírodní vědy a čtení

Nejprve v `PISA_Vysledky` vytvořit pole `rozdil_oecd = skore - oecd_skore`, typ Number, agregace Average. Pro každý graf: dimenze `zeme`, bez rozkladu, metrika `rozdil_oecd` = Average; filtr `typ = Zeme` AND `cyklus = 2025` AND jedna oblast. Zapnout 10 pruhů, sestupné řazení, datové popisky, viditelnou nulu a zápornou část osy. Vypnout křížové filtrování pro nezávislé grafy.

| Název stránky → Název grafu | Oblast ve filtru | Kontrola ČR |
| --- | --- | ---: |
| `Rozdíl vůči OECD: přírodní vědy a čtení` → `Rozdíl vůči OECD v bodech, přírodní vědy 2025` | Přírodní vědy | **+8** |
| `Rozdíl vůči OECD: přírodní vědy a čtení` → `Rozdíl vůči OECD v bodech, čtení 2025` | Čtení | **+7** |

## 4. Rozdíl vůči OECD: matematika

**Rozdíl vůči OECD: matematika → Rozdíl vůči OECD v bodech, matematika 2025** (vodorovný pruhový graf)

- **Postup:** kopie předchozího grafu; změnit **filtr oblasti na Matematiku i název**. Ostatní pole, rok, typ země, řazení a zápornou osu zachovat.
- **Kontrola:** Česko **+14**; 10 zemí. B-S-J-Z a běžný průměr OECD nejsou další země v grafu.

## 5. Mapa výsledků

**Mapa výsledků → Skóre patnáctiletých podle země, PISA 2025** (Geo chart nebo Google Maps)

- **Pole:** `iso3` s typem Geo → Země; metrika `skore` = Average. Při chybném zobrazení ČR/SVK v Geo chartu použít vypočtené `map_kod` podle [kapitoly 5](../docs/looker-studio/05-mapa-a-filtry.md#kdyz-geo-chart-vykresli-slovensko-na-miste-ceska).
- **Filtr:** `typ = Zeme` AND `cyklus = 2025`. Po přidání ovladače oblasti **odebrat pevnou oblast jen u mapy**.
- **Ovladač:** dropdown `oblast`, zdroj `PISA_Vysledky`; jediný výběr, výchozí Přírodní vědy, vypnout „Vybrat vše“. Seskupit **mapu + ovladač oblasti**, ne pruhové grafy na jiných stránkách.
- **Druhý ovladač:** dropdown `zeme` je volitelný. Na stránce mapy ovládá jen komponenty na této stránce; pro pruhy na jiné stránce je potřeba samostatný ovladač.
- **Kontrola:** Česko **490 / 468 / 477** po volbě Přírodní vědy / Čtení / Matematika. Hodnota kolem **478** pro ČR nebo legenda sahající k **552,667** značí smíchání tří oblastí, nikoli výsledek jedné oblasti.

## 6. Změna výsledků 2022–2025

**Změna výsledků 2022–2025 → Publikovaná změna v přírodních vědách 2022–2025, body** (vodorovný pruhový graf)

- **Zdroj a pole:** `PISA_Vysledky`; dimenze `zeme`; metrika `zmena_2022_2025` = Average.
- **Filtr:** `typ = Zeme` AND `cyklus = 2025` AND `oblast = Přírodní vědy`.
- **Zapnout:** sestupné řazení, hodnoty u pruhů, viditelnou nulu a zápornou část osy.
- **Kontrola:** Slovensko **+13**, Česko **−7**. Pod grafem ponechat poznámku, že nejde o test statistické významnosti.

## 7. Trendy zemí 2015–2025

**Trendy zemí 2015–2025 → Čtení: průměrné skóre patnáctiletých, 2015–2025** (Časová řada)

- **Zdroj a pole:** `PISA_Vysledky`; dimenze `datum_cyklu` = Date po rocích; metrika `skore` = Average; rozkladová dimenze `zeme`.
- **Filtr:** `oblast = Čtení` AND `zeme` je jedna z hodnot `Česko`, `Finsko`, `Estonsko`, `Průměr OECD (stálých 35)`. Další země lze přidat do výběru, ale počet zobrazených řad musí být dostatečný.
- **Vypnout:** `cyklus = 2025`; nevolit běžný `Průměr OECD`, který zde nemá úplný trend. **Zapnout:** značky bodů; Styl → Chybějící data → Lineární interpolace místo čáry k nule.
- **Kontrola:** Česko **487 → 490 → 489 → 468**; stálý průměr OECD **490 → 488 → 477 → 463**. Naměřené jsou jen roky 2015, 2018, 2022 a 2025.

## 8. Rozložení výsledků 2025

**Společný ovladač:** dropdown `oblast` ze zdroje `PISA_Rozlozeni`; jediný výběr, výchozí Přírodní vědy, vypnout „Vybrat vše“. Seskupit s oběma grafy na stránce. Oba grafy mají pevný rok 2025, nikoli pevnou oblast.

**Rozložení výsledků 2025 → Rozložení výsledků PISA 2025 podle oblasti** (100% skládaný vodorovný pruhový graf)

- **Pole:** dimenze `zeme`; **bez rozkladové dimenze**; tři hlavní metriky `podil_pod_2`, `podil_2_4`, `podil_5_6`, všechny Average a formát Procenta. Nedávat je mezi nepovinné metriky.
- **Filtr:** `cyklus = 2025` AND `typ != Region` AND `typ != Reference_stala`.
- **Zapnout:** 100% skládání, legendu, podíly. **Vypnout:** křížové filtrování, má-li bodový graf stále ukazovat všechny země.
- **Kontrola:** 11 pruhů včetně běžného průměru OECD; Česko při Přírodních vědách **21,3 % / 71,7 % / 7,0 %**.

**Rozložení výsledků 2025 → Průměrné skóre a podíl pod úrovní 2, PISA 2025** (bodový graf)

- **Pole:** dimenze bodů `zeme`; metrika X `skore` = Average; metrika Y `podil_pod_2` = Average, formát Procenta; stejné velikosti bodů.
- **Filtr:** `typ = Zeme` AND `cyklus = 2025`; oblast určuje společný dropdown.
- **Kontrola:** 10 bodů. Pokud zůstane jen Česko, zrušit aktivní výběr pruhu nebo vypnout jeho křížové filtrování. Osy popsat jako body PISA a podíl žáků v %.

## 9. Druhy škol v ČR 2025

**Druhy škol v ČR 2025 → Skóre patnáctiletých podle druhu školy a oblasti, ČR 2025** (kontingenční tabulka)

- **Zdroj a pole:** `PISA_Druhy_skol_CR`; řádky `druh_skoly`; sloupce `oblast`; metrika `skore` = Average.
- **Filtr:** `cyklus = 2025`. **Vypnout:** řádkové a sloupcové součty.
- **Kontrola:** 5 druhů škol × 3 oblasti; víceleté gymnázium v přírodních vědách **595**, SOU v matematice **404**.

**Druhy škol v ČR 2025 → Skóre podle druhu školy ve třech oblastech, ČR 2025** (skupinový vodorovný pruhový graf)

- **Pole:** dimenze `druh_skoly`; rozkladová dimenze `oblast`; jediná metrika `skore` = Average.
- **Filtr:** `cyklus = 2025`. **Vypnout:** Skládané pruhy / Stacked bars. Zobrazit tři pruhy vedle sebe u každého druhu školy, osa v bodech PISA.
- **Pozor:** dropdown `oblast` na této stránce není potřeba pro základní srovnání všech tří oblastí. Pokud jej přidáte, nesmí nechtěně omezit tabulku a skupinový graf na jedinou oblast.

## 10. Trendy druhů škol v ČR

**Trendy druhů škol v ČR → Vývoj skóre podle druhu školy, ČR 2015–2025** (Časová řada)

- **Zdroj a pole:** `PISA_Druhy_skol_CR`; dimenze `datum_cyklu` = Date; metrika `skore` = Average; rozkladová dimenze `druh_skoly`.
- **Ovladač:** dropdown **`oblast`**, nikoli `druh_skoly`; jediný výběr, výchozí Přírodní vědy, vypnout „Vybrat vše“. Bez pevného filtru oblasti a bez `cyklus = 2025`.
- **Zapnout:** všech pět řad, značky měřených bodů, lineární interpolaci pro mezilehlé roky. Ovladač a graf seskupit, pokud jsou na stránce i další pohledy ze stejného zdroje.
- **Kontrola při Přírodních vědách:** víceleté gymnázium **602 → 600 → 605 → 595**; SOU bez maturity **413 → 423 → 417 → 413**.

## Tři rychlé kontroly exportu

1. Na straně 1 má kontrolní tabulka ukázat **3**, nikoli 39 řádků: chybí-li omezení na ČR, doplnit `iso3 = CZE`.
2. Na straně 5 musí být v ovladači vybrána právě jedna oblast; smíšené skóre mapy není platný výsledek PISA.
3. Na straně 10 má dropdown měnit `oblast`. Výběr `druh_skoly` by redukoval pět porovnávaných čar místo přepnutí předmětu.

Podrobné odůvodnění, zdroje a otázky pro účastníky jsou v [učebnici](../docs/looker-studio/index.md). Kratší pracovní list jen pro strany 2–4 je v [taháku Srovnání zemí](LOOKER_STUDIO_TAHAK_SROVNANI_ZEMI.md).
