# 8. Manuál pro učitele

<div class="lesson-meta">
<strong>Plná varianta:</strong> 8 × 45 minut<br>
<strong>Zkrácená varianta:</strong> 180 minut<br>
<strong>Výstup:</strong> Vlastní report, ověřené filtry a komentář použitelný při pedagogické poradě.
</div>

## Před kurzem

Vyzkoušejte školní účet na Looker Studio a připojení Google Sheets. Pokud doména službu nepovoluje, ověřte přístup se správcem školy před školením. Připravte kopii tabulky se třemi listy podle [kapitoly 2](02-priprava-dat.md). Lektor si dopředu vytvoří jeden referenční report podle následujícího postupu. Každý účastník pracuje se svou kopií dat.

## Přesný sled práce

| Hodina | Činnost | Hotový výstup |
| --- | --- | --- |
| 1 | Vymezit populaci PISA, opravit interpretační výroky | Dvě výzkumné otázky a popis populace |
| 2 | Importovat tři CSV, zkontrolovat čísla a řádky | Listy Vysledky, Prirodni_vedy a Druhy_skol_CR |
| 3 | Připojit Sheets, ověřit tabulku ČR, vytvořit karty | Stránka Česko v kontextu |
| 4 | Pruhový graf, pivot a rozdíl proti OECD | Stránka Srovnání zemí |
| 5 | Mapa, přepínač oblasti, filtr zemí | Ověřené interaktivní pohledy |
| 6 | Změna, skládaný a bodový graf | Stránka Změny a rozložení |
| 7 | Připojit české druhy škol, vytvořit tabulku a graf | Stránka Druhy škol v ČR |
| 8 | Napsat komentář, otestovat sdílení a obhájit závěr | Finální report pro kolegu |

Pro 180minutový workshop věnujte 20 minut metodice, 30 minut importu a připojení, 45 minut kartám a srovnání, 35 minut filtrům a rozložení, 20 minut interpretaci SŠ a 30 minut dokončení a sdílení. Bodový graf a rozšíření o vlastní data mohou účastníci dokončit samostatně.

## Od prázdného reportu k hotovému výsledku

1. Stáhněte tři CSV z [přehledu kurzu](index.md) a importujte je do Sheets. Ověřte 36, 11 a 15 datových řádků.
2. Připojte `Vysledky`, nastavte typy a Average u metrik. Zkontrolujte tři české výsledky v tabulce.
3. Na stránce `Česko v kontextu` vytvořte tři karty podle oblasti, každou s pevnou podmínkou ČR.
4. Přidejte stránku `Srovnání zemí`. Vytvořte pruhový graf přírodních věd, pivot bez součtů a pole `rozdil_oecd`.
5. Přidejte mapu a přepínače. Odstraňte pevné omezení oblasti pouze u komponent, které mají reagovat na ovladač. Seskupte je.
6. Na stránce `Změny a rozložení` vytvořte graf publikované změny. Připojte druhý zdroj pro podíly a bodový graf.
7. Připojte `Druhy_skol_CR` jako třetí zdroj. Na stránce `Druhy škol v ČR` vytvořte pivot a graf podle [kapitoly 7](07-stredni-skoly.md).
8. Poslední stránku pojmenujte `Co z dat vyplývá`. Vložte tři části: zjištění, omezení, návrh aktivity pro vlastní třídu. Doplňte populaci, cyklus, jednotky, zdroj a datum převzetí dat. Uveďte, že jde o deset vybraných zemí, jeden čínský region a české druhy škol.
9. V režimu zobrazení projděte všechny ovladače. Vraťte je do výchozího stavu.
10. Otevřete **Sdílet / Share**, přidejte konkrétního kolegu jako čtenáře a vyzkoušejte přístup z jeho účtu. Odkaz do kurzu přidávejte až po ověření přístupu.

Při sdílení zkontrolujte také přihlašovací údaje datového zdroje. Při použití údajů vlastníka může čtenář získat údaje přes report bez přímého přístupu k tabulce; při údajích čtenáře potřebuje vlastní oprávnění ke zdroji. Pro cvičení používáme veřejné národní agregace. Pokud později přidáte školní data, nastavte sdílení podle skutečného obsahu.

Nastavení popisuje [Google: přihlašovací údaje datových zdrojů](https://docs.cloud.google.com/data-studio/data-credentials-article).

## Kontrolní hodnoty

| Kontrola | Očekávaný výsledek |
| --- | --- |
| Karta ČR, matematika | 477 |
| Karta ČR, čtení | 468 |
| Karta ČR, přírodní vědy | 490 |
| Rozdíl ČR proti OECD, přírodní vědy | +8 bodů |
| Publikovaná změna ČR, přírodní vědy | −7 bodů; bez závěru o průkazném poklesu |
| Český pruh rozložení | 21,3 % / 71,7 % / 7,0 % |
| Základní graf zemí | Deset zemí bez regionu B-S-J-Z a reference OECD |
| Český graf druhů škol | Pět druhů × tři oblasti; víceleté gymnázium 595 v přírodních vědách |

Kontrolní hodnoty vycházejí z [OECD Education GPS: ČR](https://gpseducation.oecd.org/CountryProfile?primaryCountry=CZE&topic=PI&treshold=10) a [národní zprávy ČŠI](https://csi.gov.cz/CSICR/media/Prilohy/2024_p%C5%99%C3%ADlohy/Dokumenty/PISA-2025_final.pdf). Prostřední podíl a rozdíl proti OECD jsou výpočty z přiložených zaokrouhlených vstupů.

## Když se výsledek neshoduje

| Potíž | Náprava |
| --- | --- |
| Skóre je součet nebo překvapivě vysoké | Nastavte Average, doplňte oblast a zkontrolujte duplicity klíče. |
| Karta ukazuje průměr více oblastí | Přidejte přesný filtr oblasti. |
| Podíl je 2130 % | Zkontrolujte vstup 0.213; procentní formát násobí zobrazení stem. |
| Číslo je text | Opravte import a desetinný oddělovač v Sheets, pak aktualizujte pole zdroje. |
| Filtr vyprázdní graf | Hledejte konflikt pevného filtru a ovladače, zdroj nebo nesprávnou skupinu. |
| Nový sloupec chybí | V editaci zdroje obnovte pole / Refresh fields. |
| Mapa nezobrazuje zemi | Ověřte ISO3 a geografický typ Country. OECD ani region B-S-J-Z na mapu zemí nepatří. |
| Kolega nevidí data | Ověřte sdílení reportu i nastavení přihlašovacích údajů zdroje. |

## Zadání a kritéria dokončení

Připravte krátký report pro pedagogickou poradu. Ukažte alespoň čtyři pohledy včetně rozložení, jednu interakci a srovnání s OECD. Každé zjištění doložte konkrétním grafem. Výstup posuzujte podle následujících kritérií:

- Správná čísla a granularita: 0–2 body.
- Funkční a ověřené filtry: 0–2 body.
- Čitelné grafy, jednotky a popisky: 0–2 body.
- Přesná populace, zdroj a omezení interpretace: 0–2 body.
- Konkrétní pedagogický návrh navazující na otázku: 0–2 body.

Příklad přijatelného závěru: „Rozložení výsledků nám připomíná potřebu sledovat také žáky pod základní úrovní. V naší třídě ověříme porozumění grafům krátkou úlohou a rozebereme typy chyb.“ Nepřijatelný závěr by z národního průměru přímo určoval schopnosti jednotlivého studenta.

## Volitelné pokračování: 45 minut

Pro skupinu, která už zvládla osm základních lekcí, použijte [lekci o nejistotě a mikrodatech](09-nejistota-a-mikrodata.md). Připravte dva další listy `Odhady_zeme` a `Odhady_skoly`; nevkládejte jejich řádky do původních listů. Účastníci vytvoří tabulku skóre a standardních chyb a přibližné intervaly. Kontrolní hodnoty: ČR v přírodních vědách 490,278 ± 2,586 bodu; základní škola v ČR 459,016 ± 2,955 bodu. Znaménko ± zde označuje **jednu standardní chybu**, nikoli 95% interval. Výstup musí rozlišovat deset zemí, region B-S-J-Z a české školní skupiny.
