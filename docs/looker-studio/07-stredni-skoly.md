# 7. Zaměření na střední školy

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut; mezinárodní rozšíření je navazující odborná práce<br>
<strong>Výstup:</strong> Graf skutečných výsledků podle českých druhů škol a přesné vymezení jeho populace.
</div>

## Co čísla popisují

[Národní zpráva ČŠI PISA 2025](https://csi.gov.cz/CSICR/media/Prilohy/2024_p%C5%99%C3%ADlohy/Dokumenty/PISA-2025_final.pdf) publikuje průměrná skóre patnáctiletých žáků podle pěti českých druhů škol. Grafy 2.1.14, 2.3.3 a 2.4.4 pokrývají přírodní vědy, čtení a matematiku. Hodnoty jsme přepsali do samostatného [CSV](data/pisa2025-cesko-druhy-skol.csv). Nejsou to výsledky všech žáků středních škol, ale patnáctiletých v jednotlivých kategoriích; zahrnuta je i základní škola.

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

1. V reportu zvolte **Zdroje / Resource → Spravovat přidané zdroje dat** a připojte list `Druhy_skol_CR` ze stejné tabulky Google Sheets. Zdroj nazvěte `PISA25_Druhy_skol_CR`.
2. Ověřte typ `skore` jako číslo a jeho agregaci Average. `druh_skoly` a `oblast` jsou textové dimenze. Nepoužívejte součet skóre.
3. Vytvořte stránku `Druhy škol v ČR` a vložte kontingenční tabulku. Řádky: `druh_skoly`, sloupce: `oblast`, metrika: `skore` (Average).
4. Vypněte součty řádků a sloupců. Tabulka má pět řádků a tři sloupce hodnot. Zkontrolujte 595 u víceletého gymnázia v přírodních vědách a 404 u SOU v matematice.
5. Vedle tabulky vložte skupinový pruhový graf, který používá `druh_skoly` jako dimenzi, `oblast` jako rozkladovou dimenzi a `skore` jako metriku. Ponechte hodnoty čitelné a popisek osy `body PISA`.
6. Přidejte volič oblasti pouze pro tento zdroj, pokud chcete detailní graf jedné oblasti. Po výběru Čtení ověřte ZŠ 436 a čtyřleté gymnázium 564.
7. Pod graf napište „Patnáctiletí žáci podle druhu školy v ČR, PISA 2025. Bodové odhady z grafů ČŠI 2.1.14, 2.3.3 a 2.4.4; bez standardních chyb v přiloženém výběru.“

!!! warning "Jak čísla číst"
    Rozdíly mezi druhy škol jsou popisné. Odráží také výběr žáků do vzdělávacích drah a jejich sociální zázemí. Z grafu nevyvozujte, že právě druh školy rozdíl způsobil, ani že každá škola daného druhu dosáhne uvedeného průměru.

## Pro mezinárodní členění podle škol

Přiložený školní výběr pokrývá pouze ČR. Chcete-li doplnit jiné země, potřebujete doložené odhady pro srovnatelně definované skupiny, nejlépe se standardními chybami a počtem respondentů. České názvy „gymnázium“, „SOŠ“ a „SOU“ nelze automaticky přenést do jiných systémů; ověřte programy a ISCED v každé zemi. Zemi bez srovnatelného odhadu vynechte, národní průměr za všechny patnáctileté za něj nedosazujte.

## Pokud zpracováváte mikrodata

PISA používá žákovské váhy, replikační váhy a plausible values. Plausible values jsou vícenásobné odhady pro statistické zpracování, nikoli přesné testové známky jednotlivých žáků. Nevážený průměr jednoho takového sloupce v Looker Studio není správný odhad výsledku populace.

Odborný postup vyžaduje ověřit názvy proměnných v codebooku pro cyklus 2025, definovat skupiny podle národních programů a ISCED, použít všechny předepsané plausible values a váhy a spočítat nejistotu podle technického manuálu. Zpracování podskupin musí respektovat výběrový design. Poté se do Looker Studio importuje hotová tabulka odhadů a standardních chyb. Přehled souborů a technickou dokumentaci poskytuje [OECD PISA 2025 Database](https://www.oecd.org/en/data/datasets/pisa-2025-database.html).

Mezinárodní členění podle typů škol je další analýza; současný graf podle druhu školy je doložený pouze pro ČR.

Chcete-li ve výuce pracovat také se standardními chybami vypočtenými z veřejného žákovského souboru, pokračujte [navazující lekcí](09-nejistota-a-mikrodata.md). Její tabulky jsou oddělené od zaokrouhlených hodnot přepsaných z grafů ČŠI.

## Aktivita pro sborovnu

Vyberte krátkou úlohu na interpretaci grafu nebo odborného textu. Nechte žáky odpověď zdůvodnit a společně s kolegou rozlište chyby ve čtení zadání, argumentaci a oborových znalostech. PISA dodává širší kontext; toto místní zjištění pomůže rozhodnout, co skutečně procvičit v konkrétní třídě.
