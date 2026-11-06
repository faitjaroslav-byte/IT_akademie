# Data Studio: step-by-step manuál pro učitele

Tento pracovní materiál je uložen pouze v repozitáři. Není součástí publikované učebnice ani navigace MkDocs.

<div class="lesson-meta">
<strong>Plná varianta:</strong> 8 × 45 minut (kapitoly 0–7)<br>
<strong>Zkrácená varianta:</strong> 180 minut<br>
<strong>Výstup:</strong> Vlastní report, ověřené filtry a komentář použitelný při pedagogické poradě.
</div>

## Před kurzem

Vyzkoušejte školní účet na Data Studio (dříve Looker Studio) a připojení Google Sheets. Pokud doména službu nepovoluje, ověřte přístup se správcem školy před školením. Připravte kopii tabulky se třemi listy podle [kapitoly 2](../docs/looker-studio/02-priprava-dat.md). Lektor si dopředu vytvoří jeden referenční report podle následujícího postupu. Každý účastník pracuje se svou kopií dat.

Před první hodinou otevřete všechny tři CSV z [přehledu kurzu](../docs/looker-studio/index.md), ověřte jejich oddělovač a desetinné hodnoty a připravte záložní kopii v Google Sheets. Ujistěte se, že máte oprávnění vytvářet a sdílet reporty, a rozhodněte, zda účastníci budou pracovat samostatně, nebo ve dvojicích. Referenční report používejte ke kontrole, ne jako náhradu jejich vlastní práce.

## Přesný sled práce

| Hodina | Činnost | Hotový výstup |
| --- | --- | --- |
| 0 | Vysvětlit zdroj → report, porovnat Data Studio s Power BI a Snowflake | Účastník odliší BI report od datového skladu |
| 1 | Vysvětlit PISA: cyklus, výběr, oblasti, populaci a meze interpretace | Účastník správně popíše, koho výsledek reprezentuje |
| 2 | Importovat tři CSV, zkontrolovat čísla a řádky | Listy Vysledky, Prirodni_vedy a Druhy_skol_CR |
| 3 | Připojit Sheets, ověřit tabulku ČR, vytvořit karty | Stránka Česko v kontextu |
| 4 | Pruhový graf, pivot a rozdíl proti OECD | Stránka Srovnání zemí |
| 5 | Mapa, přepínač oblasti, filtr zemí | Ověřené interaktivní pohledy |
| 6 | Změna, skládaný a bodový graf | Stránka Změny a rozložení |
| 7 | Připojit české druhy škol, vytvořit tabulku a graf, shrnout omezení | Stránka Druhy škol v ČR a hotový komentář |

Pro 180minutový workshop věnujte 15 minut představení nástroje a PISA, 30 minut importu a připojení, 45 minut kartám a srovnání, 35 minut filtrům a rozložení, 25 minut interpretaci školních skupin a 30 minut dokončení a sdílení. Bodový graf a rozšíření o vlastní data mohou účastníci dokončit samostatně.

## Vedení jednotlivých hodin

1. **Hodina 0:** Na jedné tabulce ukažte rozdíl mezi uloženými daty a reportem. Otevřete [úvod do Data Studia](../docs/looker-studio/00-uvod-do-data-studia.md). Nechte účastníky určit, co je zdroj, co vizualizace a co by vyžadovalo samostatné zpracování dat.
2. **Hodina 1:** Projděte [popis PISA](../docs/looker-studio/01-pisa-a-interpretace.md). Zeptejte se, proč nelze celou českou populaci PISA označit za středoškoláky a proč bodový rozdíl sám o sobě nedokazuje účinek výuky. Není potřeba zadávat závěrečný písemný úkol.
3. **Hodina 2:** Podle [přípravy dat](../docs/looker-studio/02-priprava-dat.md) nechte vytvořit tři listy. Před pokračováním každý účastník ukáže počty řádků 36, 11 a 15 a číselný typ skóre.
4. **Hodina 3:** Veďte účastníky podle [prvního reportu](../docs/looker-studio/03-prvni-report.md). Po vytvoření tří karet zkontrolujte ČR 477 / 468 / 490. Nesprávné hodnoty nejprve řešte filtrem oblasti a agregací.
5. **Hodina 4:** Na [srovnání zemí](../docs/looker-studio/04-srovnani.md) nechte vytvořit pruhový graf, pivot a rozdíl proti OECD. Ověřte, že OECD není další země v žebříčku a B-S-J-Z není celá Čína.
6. **Hodina 5:** Podle [mapy a filtrů](../docs/looker-studio/05-mapa-a-filtry.md) ověřte na dvou různých volbách, že ovladače skutečně mění zamýšlené grafy. Zkontrolujte mapový typ pole pro země.
7. **Hodina 6:** Podle [změn a rozložení](../docs/looker-studio/06-zmeny-a-rozlozeni.md) oddělte bodový průměr od podílů žáků. Připomeňte, že změna mezi cykly nesleduje stejné jednotlivce.
8. **Hodina 7:** Podle [školních skupin](../docs/looker-studio/07-stredni-skoly.md) doplňte poslední zdroj, stránku a krátký komentář. Na závěr otevřete report v režimu čtenáře, vyzkoušejte sdílení s kolegou a vraťte filtry do výchozího stavu.

## Od prázdného reportu k hotovému výsledku

1. Stáhněte tři CSV z [přehledu kurzu](../docs/looker-studio/index.md) a importujte je do Sheets. Ověřte 36, 11 a 15 datových řádků.
2. Připojte `Vysledky`, nastavte typy a Average u metrik. Zkontrolujte tři české výsledky v tabulce.
3. Na stránce `Česko v kontextu` vytvořte tři karty podle oblasti, každou s pevnou podmínkou ČR.
4. Přidejte stránku `Srovnání zemí`. Vytvořte pruhový graf přírodních věd, pivot bez součtů a pole `rozdil_oecd`.
5. Přidejte mapu a přepínače. Odstraňte pevné omezení oblasti pouze u komponent, které mají reagovat na ovladač. Seskupte je.
6. Na stránce `Změny a rozložení` vytvořte graf publikované změny. Připojte druhý zdroj pro podíly a bodový graf.
7. Připojte `Druhy_skol_CR` jako třetí zdroj. Na stránce `Druhy škol v ČR` vytvořte pivot a graf podle [kapitoly 7](../docs/looker-studio/07-stredni-skoly.md).
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

Pro skupinu, která už zvládla osm základních lekcí, použijte [lekci o nejistotě a mikrodatech](../docs/looker-studio/09-nejistota-a-mikrodata.md). Připravte dva další listy `Odhady_zeme` a `Odhady_skoly`; nevkládejte jejich řádky do původních listů. Účastníci vytvoří tabulku skóre a standardních chyb a přibližné intervaly. Kontrolní hodnoty: ČR v přírodních vědách 490,278 ± 2,586 bodu; základní škola v ČR 459,016 ± 2,955 bodu. Znaménko ± zde označuje **jednu standardní chybu**, nikoli 95% interval. Výstup musí rozlišovat deset zemí, region B-S-J-Z a české školní skupiny.
