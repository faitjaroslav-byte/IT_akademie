# Looker Studio: Česko a svět v PISA 2025

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 8 × 45 minut; zkrácený workshop 180 minut; volitelné rozšíření 45 minut<br>
<strong>Výstup:</strong> Interaktivní report se srovnáním výsledků, filtry a věcným komentářem pro pedagogickou poradu.<br>
<strong>Vstupní znalosti:</strong> Základní práce s tabulkou a školní účet Google.
</div>

Jak si vedou čeští žáci ve srovnání se sousedními zeměmi? Co skrývá průměrné skóre? Jaké otázky mají smysl pro plánování výuky? Na těchto otázkách si osvojíte tvorbu reportu v Google Looker Studio. Postupy používají běžný konektor Google Sheets a nevyžadují programování.

Google v dubnu 2026 službu přejmenoval na **Data Studio**. V kurzu ponecháváme známý název Looker Studio; v rozhraní a odkazované dokumentaci můžete potkat nový název. [Google: změna názvu služby](https://docs.cloud.google.com/data-studio/release-notes)

Kurz pracuje s **PISA 2025**. OECD uvádí zveřejnění prvního svazku výsledků 8. září 2026. Přiložená data jsou malý výukový výběr publikovaných agregací, ověřený k 5. listopadu 2026. [OECD: PISA FAQ](https://www.oecd.org/en/about/programmes/pisa/pisa-frequently-asked-questions-faqs.html)

!!! important "Koho výsledky popisují"
    PISA sleduje patnáctileté žáky napříč typy škol. Mezinárodní report popisuje celou cílovou populaci vybraných zemí; samostatná tabulka z české národní zprávy ukazuje výsledky podle druhů škol v ČR. B-S-J-Z představuje čtyři oblasti Číny, nikoli celou Čínu. Podrobnosti najdete v [kapitole o středních školách](07-stredni-skoly.md).

## Co vytvoříte

Report bude mít pět stránek: **Česko v kontextu**, **Srovnání zemí**, **Změny a rozložení**, **Druhy škol v ČR** a **Co z dat vyplývá**. V tomto kurzu znamená *data view* konkrétní pohled na data v reportu, například tabulku, mapu nebo graf. Nejde o databázový SQL view.

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
| Tabulka s nejistotou | Jak přesné jsou odhady z veřejných mikrodat? | [Nejistota a mikrodata](09-nejistota-a-mikrodata.md) |

## Postup kurzu

1. [Pochopte populaci, skóre a hranice interpretace](01-pisa-a-interpretace.md).
2. [Importujte připravená data a zkontrolujte jejich strukturu](02-priprava-dat.md).
3. [Připojte Google Sheets a vytvořte první report](03-prvni-report.md).
4. [Sestavte srovnávací pohledy](04-srovnani.md).
5. [Přidejte mapu a ověřte filtry](05-mapa-a-filtry.md).
6. [Prozkoumejte změny a rozložení výsledků](06-zmeny-a-rozlozeni.md).
7. [Sestavte pohled podle českých druhů škol a posuďte srovnatelnost](07-stredni-skoly.md).
8. [Dokončete report podle manuálu pro učitele](08-manual-pro-ucitele.md).
9. [Rozšiřte report o standardní chyby z veřejných mikrodat](09-nejistota-a-mikrodata.md).

## Data ke stažení

- [Výsledky podle země a oblasti, CSV](data/pisa2025-vysledky.csv): 36 řádků, deset zemí, B-S-J-Z a reference OECD ve třech oblastech.
- [Rozložení v přírodních vědách, CSV](data/pisa2025-prirodni-vedy.csv): 11 řádků pro skládaný a bodový graf.
- [Česko podle druhu školy, CSV](data/pisa2025-cesko-druhy-skol.csv): 15 řádků, pět druhů škol ve třech oblastech.
- [Rozšíření vypočtené z veřejných mikrodat PISA 2025](data/README.md#rozsireni-z-verejneho-zakovskeho-souboru-oecd): země, české druhy škol a programy včetně standardních chyb a počtů žáků.
- [Datový slovník a původ údajů](data/README.md).

Všechny konkrétní kontrolní hodnoty v návodech odpovídají tomuto výběru. Pořadí v reportu nepředstavuje úplný světový žebříček ani test statistické významnosti.
