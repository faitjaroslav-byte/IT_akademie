# 0. Úvod do Data Studia

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Vysvětlíte, k čemu slouží datový report, a rozlišíte vizualizační nástroj od úložiště dat.
</div>

## Od tabulky k reportu

Tabulka uchovává řádky a sloupce. Report z nich skládá pohledy pro konkrétní otázky: například skóre ČR, srovnání zemí nebo podíl žáků pod základní úrovní. Čtenář může měnit filtr a vidět související grafy bez úprav původní tabulky. Report však nezlepší chybná vstupní data ani sám nevysvětlí, proč rozdíl vznikl.

**Google Data Studio** je webový nástroj pro tvorbu interaktivních reportů. Do dubna 2026 se jmenoval **Looker Studio**. V tomto kurzu pracujeme s týmž produktem, i když se starší název může objevovat na obrazovkách nebo v odkazech. [Google: poznámky k vydání](https://docs.cloud.google.com/data-studio/release-notes)

## Jak funguje

```text
CSV s výsledky PISA → Google Sheets → datový zdroj → report → čtenář
```

**Konektor** propojí report s tabulkou nebo jinou službou. **Datový zdroj** určuje, které sloupce jsou dimenze (například země a oblast) a které metriky (například bodové skóre). V **reportu** pak použijete tabulky, karty, grafy, mapy a ovládací prvky. Zdroj může obsahovat i vypočtená pole; více zdrojů lze pro vybrané pohledy spojovat. Většina zdrojů zůstává uložena mimo Data Studio a report si potřebná data průběžně načítá. [Google: datové zdroje](https://docs.cloud.google.com/data-studio/about-data-sources), [Google: spojování dat](https://docs.cloud.google.com/data-studio/how-blends-work)

V praxi můžete:

- připojit Google Sheets, BigQuery či další podporované zdroje;
- vytvořit grafy, tabulky, mapy a více stránek jednoho reportu;
- filtrovat data podle země, oblasti nebo období;
- přidat jednoduchý výpočet, například rozdíl vůči referenci OECD;
- sdílet report s kolegy a nastavit, kdo jej může zobrazit nebo upravit.

Při sdílení nestačí poslat odkaz: přístup k datům závisí také na oprávněních a přihlašovacích údajích zdroje. [Google: rychlý úvod a sdílení](https://docs.cloud.google.com/data-studio/quick-start-guide)

## Kde jsou hranice nástroje

Data Studio je především **vrstva pro analýzu a prezentaci**, nikoli náhrada za čištění rozsáhlých surových dat, statistický software nebo datový sklad. V kurzu proto nepřipojujeme dvougigabajtový žákovský soubor PISA přímo do reportu. Používáme malé, připravené agregované tabulky s popsaným původem. Pokročilé odhady z mikrodat se počítají předem a do reportu vstupují až jako výsledná tabulka.

## Alternativy a doplňky

| Produkt | Hlavní role | Kdy by dával smysl v tomto kurzu |
| --- | --- | --- |
| **Data Studio** | Webový report nad připojenými zdroji | Chceme rychle vytvořit a sdílet interaktivní pohledy z Google Sheets. |
| **Microsoft Power BI** | BI platforma pro přípravu dat, datové modely, výpočty a reporty | Škola už pracuje v prostředí Microsoftu nebo potřebuje rozsáhlejší modelování více tabulek. |
| **Tableau** | Vizuální průzkum dat a tvorba interaktivních dashboardů | Potřebujeme intenzivně zkoumat vzorce v datech a připravovat bohaté vizualizace. |
| **Metabase** | Otázky nad databází, jednoduché dashboardy a sdílení | Data máme v databázi a chceme rychlé dotazy a přehledy. |
| **Snowflake** | Cloudová datová platforma pro ukládání a zpracování dat | Zpracováváme velké soubory a tým potřebuje společný datový základ; hotové souhrny pak lze zobrazit v BI nástroji. |

Power BI nabízí mimo jiné Power Query a datové modelování; Snowflake má ve svém rozhraní Snowsight také grafy a dashboardy, ale jeho hlavní úloha je širší než tvorba reportů. Proto nejde o zcela zaměnitelné produkty: Snowflake může připravovat data, která se následně vizualizují v Data Studiu nebo Power BI. [Microsoft: Power BI](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview), [Tableau: dashboardy](https://help.tableau.com/current/pro/desktop/en-us/dashboards.htm), [Metabase: dashboardy](https://www.metabase.com/docs/latest/dashboards/introduction), [Snowflake: platforma](https://docs.snowflake.com/en/user-guide/intro-key-concepts), [Snowflake: Snowsight](https://docs.snowflake.com/en/user-guide/ui-snowsight)

Pro naše malé, předem připravené výukové tabulky je Data Studio vhodná volba: studenti se mohou soustředit na smysl grafu, filtru a popisku. Nejdříve však potřebujeme rozumět tomu, **co data PISA skutečně měří**. Tomu se věnuje [kapitola 1](01-pisa-a-interpretace.md).
