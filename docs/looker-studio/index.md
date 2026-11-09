# Data Studio: Česko a svět v PISA 2025

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 8 × 45 minut; zkrácený workshop 180 minut; volitelné rozšíření 45 minut<br>
<strong>Výstup:</strong> Interaktivní report se srovnáním výsledků, filtry a věcným komentářem pro pedagogickou poradu.<br>
<strong>Vstupní znalosti:</strong> Základní práce s tabulkou a školní účet Google.
</div>

Jak si vedou čeští žáci ve srovnání se sousedními zeměmi? Co skrývá průměrné skóre? Jaké otázky mají smysl pro plánování výuky? Na těchto otázkách si osvojíte tvorbu reportu v Google Data Studiu. Postupy používají běžný konektor Google Sheets a nevyžadují programování.

Google v dubnu 2026 přejmenoval **Looker Studio na Data Studio**. Oba názvy proto můžete v návodech a rozhraní potkat. [Google: změna názvu služby](https://docs.cloud.google.com/data-studio/release-notes)

Základní pohledy pracují s **PISA 2025**, časové řady přidávají cykly **2015, 2018 a 2022**. Vše vzniká ze stejných tří tabulek. OECD uvádí zveřejnění prvního svazku výsledků PISA 2025 dne 8. září 2026. Přiložená data jsou malý výukový výběr skutečných agregací, nikoli úplná databáze. [OECD: PISA FAQ](https://www.oecd.org/en/about/programmes/pisa/pisa-frequently-asked-questions-faqs.html)

!!! important "Koho výsledky popisují"
    PISA sleduje patnáctileté žáky napříč typy škol. Mezinárodní report popisuje celou cílovou populaci vybraných zemí; samostatná tabulka z české národní zprávy ukazuje výsledky podle druhů škol v ČR. B-S-J-Z představuje čtyři oblasti Číny, nikoli celou Čínu. Podrobnosti najdete v [kapitole o středních školách](07-stredni-skoly.md).

## Co vytvoříte

Základní report má **deset stránek** v pořadí odpovídajícím [kapitolám 3–7](03-prvni-report.md). Název stránky nastavte v navigaci reportu a stejné znění vložte jako viditelný nadpis nad její obsah. Názvy jednotlivých grafů jsou samostatné a upřesňují oblast, cyklus a jednotku. V tomto kurzu znamená *data view* konkrétní pohled na data v reportu, například tabulku, mapu nebo graf. Nejde o databázový SQL view.

| Stránka reportu | Obsah |
| --- | --- |
| 1. **Česko v kontextu** | Kontrolní tabulka a tři karty skóre ČR. |
| 2. **Srovnání zemí** | Pruhové srovnání a kontingenční tabulka. |
| 3. **Rozdíl vůči OECD: přírodní vědy a čtení** | Dva pruhové grafy rozdílů. |
| 4. **Rozdíl vůči OECD: matematika** | Třetí graf rozdílů. |
| 5. **Mapa výsledků** | Mapa a ovladače oblasti a země. |
| 6. **Změna výsledků 2022–2025** | Publikovaná změna v přírodních vědách. |
| 7. **Trendy zemí 2015–2025** | Časová řada skóre zemí a stálé reference OECD. |
| 8. **Rozložení výsledků 2025** | Skládané podíly a bodový graf. |
| 9. **Druhy škol v ČR 2025** | Kontingenční tabulka a skupinový pruhový graf. |
| 10. **Trendy druhů škol v ČR** | Časová řada s výběrem oblasti. |

Závěrečná interpretace patří do výuky a komentáře k reportu; samostatnou jedenáctou stránku v základním postupu nevyžadujeme.

| Pohled | Otázka | Návod |
| --- | --- | --- |
| Karty ukazatelů | Jakého skóre dosáhlo Česko? | [První report](03-prvni-report.md) |
| Pruhový graf | Jak se liší vybrané země? | [Srovnání](04-srovnani.md) |
| Kontingenční tabulka s barvami | Ve které oblasti se profil země liší? | [Srovnání](04-srovnani.md) |
| Rozdíl vůči OECD | O kolik bodů se výsledek liší od reference? | [Srovnání](04-srovnani.md) |
| Mapa | Kde leží sledované země a jakého skóre dosahují? | [Mapa a filtry](05-mapa-a-filtry.md) |
| Graf změny | Jak se výsledek změnil mezi cykly? | [Změny](06-zmeny-a-rozlozeni.md) |
| Skládaný graf | Jaký podíl žáků má slabé nebo špičkové výsledky? | [Rozložení](06-zmeny-a-rozlozeni.md) |
| Bodový graf | Jak se potkává průměr a podíl slabých výsledků? | [Rozložení](06-zmeny-a-rozlozeni.md) |
| Graf podle druhu školy | Jak se liší výsledky českých patnáctiletých v pěti druzích škol? | [Střední školy](07-stredni-skoly.md) |
| Časové řady | Jak se vyvíjelo skóre, podíly a výsledky českých druhů škol od roku 2015? | [Trendy zemí](06-zmeny-a-rozlozeni.md#navazujici-pohled-casova-rada-20152025), [trendy škol](07-stredni-skoly.md#navazujici-pohled-vyvoj-podle-druhu-skoly) |
| Tabulka s nejistotou | Jak přesné jsou odhady z veřejných mikrodat? | [Nejistota a mikrodata](09-nejistota-a-mikrodata.md) |

## Postup kurzu

- **0.** [Seznamte se s Data Studiem a jeho alternativami](00-uvod-do-data-studia.md).
- **1.** [Pochopte šetření PISA, populaci a hranice interpretace](01-pisa-a-interpretace.md).
- **2.** [Importujte připravená data a zkontrolujte jejich strukturu](02-priprava-dat.md).
- **3.** [Připojte Google Sheets a vytvořte první report](03-prvni-report.md).
- **4.** [Sestavte srovnávací pohledy](04-srovnani.md).
- **5.** [Přidejte mapu a ověřte filtry](05-mapa-a-filtry.md).
- **6.** [Prozkoumejte změny a rozložení výsledků](06-zmeny-a-rozlozeni.md).
- **7.** [Sestavte pohled podle českých druhů škol a posuďte srovnatelnost](07-stredni-skoly.md).

Volitelné pokračování: [nejistota a mikrodata](09-nejistota-a-mikrodata.md).

## Data ke stažení

- [Výsledky podle země, oblasti a roku, CSV](data/pisa-vysledky.csv): 141 řádků včetně obou jasně rozlišených referencí OECD.
- [Rozložení výsledků, CSV](data/pisa-rozlozeni.csv): 141 řádků s podíly pod úrovní 2, na úrovních 2–4 a na úrovni 5 nebo výše.
- [Česko podle druhu školy, CSV](data/pisa-cesko-druhy-skol.csv): 60 řádků, pět druhů škol ve třech oblastech a čtyřech cyklech.
- [Rozšíření vypočtené z veřejných mikrodat PISA 2025](data/README.md#rozsireni-z-verejneho-zakovskeho-souboru-oecd): země, české druhy škol a programy včetně standardních chyb a počtů žáků.
- [Datový slovník a původ údajů](data/README.md).

Všechny konkrétní kontrolní hodnoty v návodech odpovídají tomuto výběru. Pořadí v reportu nepředstavuje úplný světový žebříček ani test statistické významnosti.
