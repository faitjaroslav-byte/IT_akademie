# 7. Zaměření na střední školy

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut; mezinárodní rozšíření je navazující odborná práce<br>
<strong>Výstup:</strong> Graf skutečných výsledků podle českých druhů škol a přesné vymezení jeho populace.
</div>

## Co čísla popisují

[Národní zpráva ČŠI PISA 2025](https://csi.gov.cz/CSICR/media/Prilohy/2024_p%C5%99%C3%ADlohy/Dokumenty/PISA-2025_final.pdf) publikuje průměrná skóre patnáctiletých žáků podle pěti českých druhů škol. Grafy 2.1.14, 2.3.3 a 2.4.4 pokrývají přírodní vědy, čtení a matematiku. Hodnoty roku 2025 jsou v jediné [tabulce českých druhů škol](data/pisa-cesko-druhy-skol.csv) spolu se staršími cykly. Nejsou to výsledky všech žáků středních škol, ale patnáctiletých v jednotlivých kategoriích; zahrnuta je i základní škola.

| Druh školy | Přírodní vědy | Čtení | Matematika |
| --- | ---: | ---: | ---: |
| Základní škola | 459 | 436 | 448 |
| Víceleté gymnázium | 595 | 567 | 586 |
| Čtyřleté gymnázium | 582 | 564 | 570 |
| SOŠ s maturitou | 510 | 492 | 492 |
| SOU bez maturity | 413 | 392 | 404 |

ČŠI uvádí pro celou českou cílovou populaci 490, 468 a 477. Tento národní průměr **není prostým průměrem pěti školních kategorií**.

Porovnávejte skupiny především v rámci stejné oblasti. Skóre různých oblastí netvoří společnou školní známku.

## Pohled 9: druhy škol v ČR

1. V reportu zvolte **Zdroje / Resource → Spravovat přidané zdroje dat** a připojte list `Druhy_skol_CR` ze stejné tabulky Google Sheets. Zdroj nazvěte `PISA_Druhy_skol_CR`. Je to třetí a poslední základní zdroj.
2. Ověřte typ `skore` jako číslo a jeho agregaci Average. `druh_skoly` a `oblast` jsou textové dimenze. Nepoužívejte součet skóre.
3. Devátou stránku pojmenujte `Druhy škol v ČR 2025`, vložte stejný nadpis nad obsah a přidejte kontingenční tabulku s názvem `Skóre patnáctiletých podle druhu školy a oblasti, ČR 2025`. Řádky: `druh_skoly`, sloupce: `oblast`, metrika: `skore` (Average). Nastavte pevný filtr `cyklus = 2025`.
4. Vypněte součty řádků a sloupců. Tabulka má pět řádků a tři sloupce hodnot. Zkontrolujte 595 u víceletého gymnázia v přírodních vědách a 404 u SOU v matematice.
5. Vedle tabulky vložte skupinový pruhový graf s názvem `Skóre podle druhu školy ve třech oblastech, ČR 2025`. Použijte `druh_skoly` jako dimenzi, `oblast` jako rozkladovou dimenzi a `skore` jako metriku. Nastavte mu také filtr `cyklus = 2025`. Ponechte hodnoty čitelné a popisek osy `body PISA`.
6. Přidejte volič oblasti pouze pro tento zdroj, pokud chcete detailní graf jedné oblasti. Po výběru Čtení ověřte ZŠ 436 a čtyřleté gymnázium 564.
7. Pod graf napište „Patnáctiletí žáci podle druhu školy v ČR, PISA 2025. Bodové odhady z grafů ČŠI 2.1.14, 2.3.3 a 2.4.4; bez standardních chyb v přiloženém výběru.“

!!! warning "Jak čísla číst"
    Rozdíly mezi druhy škol jsou popisné. Odráží také výběr žáků do vzdělávacích drah a jejich sociální zázemí. Z grafu nevyvozujte, že právě druh školy rozdíl způsobil, ani že každá škola daného druhu dosáhne uvedeného průměru.

## Navazující pohled: vývoj podle druhu školy

Tentýž zdroj `PISA_Druhy_skol_CR` obsahuje také roky 2015, 2018 a 2022. Roky 2015 a 2018 jsou publikované odhady ČŠI; rok 2022 je vážený výpočet z [národní žákovské databáze ČŠI](https://csicr.cz/cz/Mezinarodni-setreni/PISA/Datove-soubory-a-dotazniky/PISA-2022) pomocí všech deseti plausible values. Podrobný původ každého řádku je v [datovém slovníku](data/README.md#vysledky-ceskych-druhu-skol).

1. Desátou stránku pojmenujte `Trendy druhů škol v ČR`, vložte stejný nadpis nad obsah a přidejte **jeden nový graf typu Časová řada** ze zdroje `PISA_Druhy_skol_CR`. Ověřte typ `datum_cyklu` jako Date. Základní graf s filtrem 2025 ponechte beze změny.
2. V novém grafu nastavte dimenzi `datum_cyklu`, metriku `skore` (Average) a rozkladovou dimenzi `druh_skoly`.
3. U časové řady **nepoužívejte pevný filtr `oblast` ani `cyklus = 2025`**. Přidejte rozbalovací ovladač ze stejného zdroje `PISA_Druhy_skol_CR` s polem `oblast`. Zapněte jediný výběr, nastavte výchozí hodnotu `Přírodní vědy` a vypněte možnost vybrat vše. [Google: nastavení ovladače](https://docs.cloud.google.com/data-studio/drop-down-list-and-fixed-size-list-control)
4. Graf nadepište `Vývoj skóre podle druhu školy, ČR 2015–2025`; aktuální oblast musí být vidět v ovladači. Zobrazte značky měřených bodů a ponechte v legendě všech pět kategorií včetně ZŠ. Pro chybějící mezilehlé roky nastavte ve **Stylu → Chybějící data** lineární interpolaci místo čáry k nule; spojnice neznamená, že v těchto letech proběhlo měření.
5. Při výběru Přírodní vědy zkontrolujte víceleté gymnázium: **602, 600, 605, 595** bodů. SOU bez maturity: **413, 423, 417, 413** bodů. V roce 2022 je přepočtená hodnota z národního souboru, ostatní jsou převzaté ze zpráv. Potom v ovladači vyzkoušejte Čtení a Matematiku; žádná z voleb nesmí průměrovat různé oblasti.
6. Jsou-li na stejné stránce i další grafy ze zdroje `PISA_Druhy_skol_CR`, seskupte ovladač pouze s touto časovou řadou, aby neměnil jejich oblast. [Google: rozsah ovladače](https://docs.cloud.google.com/data-studio/apply-controls-to-specific-charts)

Čáry spojují výsledky **různých skupin patnáctiletých v různých letech**, nesledují pokrok týchž žáků ani konkrétní školy. Školní kategorie jsou národní české členění; bez další harmonizace je nelze porovnávat s typy škol v jiných zemích. V této výukové tabulce nejsou standardní chyby školních skupin, proto z křivek nevyvozujte statisticky významnou změnu.

## Pro mezinárodní členění podle škol

Přiložený školní výběr pokrývá pouze ČR. Chcete-li doplnit jiné země, potřebujete doložené odhady pro srovnatelně definované skupiny, nejlépe se standardními chybami a počtem respondentů. České názvy „gymnázium“, „SOŠ“ a „SOU“ nelze automaticky přenést do jiných systémů; ověřte programy a ISCED v každé zemi. Zemi bez srovnatelného odhadu vynechte, národní průměr za všechny patnáctileté za něj nedosazujte.

## Pokud zpracováváte mikrodata

PISA používá žákovské váhy, replikační váhy a plausible values. Plausible values jsou vícenásobné odhady pro statistické zpracování, nikoli přesné testové známky jednotlivých žáků. Nevážený průměr jednoho takového sloupce v Looker Studio není správný odhad výsledku populace.

Odborný postup vyžaduje ověřit názvy proměnných v codebooku pro cyklus 2025, definovat skupiny podle národních programů a ISCED, použít všechny předepsané plausible values a váhy a spočítat nejistotu podle technického manuálu. Zpracování podskupin musí respektovat výběrový design. Poté se do Looker Studio importuje hotová tabulka odhadů a standardních chyb. Přehled souborů a technickou dokumentaci poskytuje [OECD PISA 2025 Database](https://www.oecd.org/en/data/datasets/pisa-2025-database.html).

Mezinárodní členění podle typů škol je další analýza; současný graf podle druhu školy je doložený pouze pro ČR.

Chcete-li ve výuce pracovat také se standardními chybami vypočtenými z veřejného žákovského souboru, pokračujte [navazující lekcí](09-nejistota-a-mikrodata.md). Její tabulky jsou oddělené od zaokrouhlených hodnot přepsaných z grafů ČŠI.

## Aktivita pro sborovnu

Vyberte krátkou úlohu na interpretaci grafu nebo odborného textu. Nechte žáky odpověď zdůvodnit a společně s kolegou rozlište chyby ve čtení zadání, argumentaci a oborových znalostech. PISA dodává širší kontext; toto místní zjištění pomůže rozhodnout, co skutečně procvičit v konkrétní třídě.
