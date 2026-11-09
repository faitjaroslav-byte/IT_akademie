# Tahák pro lektora: Srovnání zemí

Jen pro práci při vedení kurzu. Soubor je mimo publikovanou složku `docs/`.

**Zdroj pro všechny grafy:** `PISA_Vysledky` (list `Vysledky`). **Pevný rok:** `cyklus = 2025`. Filtry níže nastavujte na úrovni jednotlivých grafů; podmínky v jednom filtru spojujte **AND**. `typ = Zeme` ponechá deset zemí, ale vyřadí region B-S-J-Z i obě reference OECD.

## Strana 2 - Srovnání zemí

**1. Vodorovný pruhový graf - Přírodní vědy: bodové odhady ve vybraných zemích**

| Krok | Nastavení |
| --- | --- |
| Vložit | Běžný vodorovný pruhový graf, ne skládaný. |
| Pole | Dimenze `zeme`; bez rozkladové dimenze; metrika `skore` = Average. |
| Filtr | `typ = Zeme` AND `cyklus = 2025` AND `oblast = Přírodní vědy`. |
| Zobrazit | Řazení podle `skore` sestupně; nejméně 10 pruhů; hodnoty u pruhů; osa od nuly. |
| Vypnout | Křížové filtrování, pokud mají ostatní grafy zůstat nezávislé na kliknutí do pruhu. |
| Kontrola | 10 zemí; Singapur **560**, Estonsko **527**, Česko **490**. |

**2. Kontingenční tabulka - Skóre zemí podle oblasti, PISA 2025**

| Krok | Nastavení |
| --- | --- |
| Vložit | Kontingenční tabulka. |
| Pole | Řádky `zeme`; sloupce `oblast`; metrika `skore` = Average. |
| Filtr | `typ = Zeme` AND `cyklus = 2025`; **bez** filtru jedné oblasti. |
| Zobrazit | Čísla a barevná škála / heatmapa, pokud je dostupná. |
| Vypnout | Řádkové a sloupcové součty; křížové filtrování pro nezávislý pohled. |
| Kontrola | 10 zemí × 3 oblasti; Česko v matematice **477**. |

Region B-S-J-Z ukažte jen v **oddělené kopii** tabulky nazvané `Skóre zemí a regionu B-S-J-Z podle oblasti, PISA 2025`: filtr (`typ = Zeme` OR `typ = Region`) AND `cyklus = 2025`. Popisek regionu není národní výsledek Číny.

## Strany 3 a 4 - Rozdíl vůči OECD

**Strana 3:** `Rozdíl vůči OECD: přírodní vědy a čtení`. **Strana 4:** `Rozdíl vůči OECD: matematika`.

Nejprve ve zdroji `PISA_Vysledky` vytvořte pole `rozdil_oecd = skore - oecd_skore`, typ Number, agregace Average. `oecd_skore` je vyplněné pro rok 2025; starší cykly do těchto grafů nepatří.

**3. Tři vodorovné pruhové grafy - jeden pro každou oblast**

| Krok | Nastavení |
| --- | --- |
| Vložit | Vodorovný pruhový graf; hotový graf zkopírovat ještě dvakrát. |
| Pole | Dimenze `zeme`; bez rozkladové dimenze; metrika `rozdil_oecd` = Average. |
| Filtr | `typ = Zeme` AND `cyklus = 2025` AND právě jedna `oblast`. U kopií změnit **i filtr**, nejen název. |
| Zobrazit | Řazení podle `rozdil_oecd` sestupně; 10 pruhů; popisky hodnot; viditelná nula a záporná část osy. |
| Vypnout | Křížové filtrování pro nezávislé grafy. |

| Strana | Oblast ve filtru | Název grafu | Kontrola ČR |
| --- | --- | --- | ---: |
| 3 | Přírodní vědy | `Rozdíl vůči OECD v bodech, přírodní vědy 2025` | **+8** |
| 3 | Čtení | `Rozdíl vůči OECD v bodech, čtení 2025` | **+7** |
| 4 | Matematika | `Rozdíl vůči OECD v bodech, matematika 2025` | **+14** |

**Rychlá oprava:** Více než 10 zemí = zkontrolovat `typ = Zeme`. Nula není vidět nebo záporné pruhy chybí = upravit osu. Kopie ukazuje hodnoty jiné oblasti = zkontrolovat pevný filtr `oblast`. Kliknutí na pruh mění jiné grafy = vypnout křížové filtrování a resetovat aktivní výběr.

Podrobné vysvětlení a výukové otázky jsou v [kapitole 4](../docs/looker-studio/04-srovnani.md).
