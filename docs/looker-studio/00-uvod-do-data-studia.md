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

Pro náš úkol je výchozím bodem **Data Studio**: připojíme Google Sheets a v prohlížeči sestavíme sdílený report. Následující „minus“ neznamená, že je jiný produkt obecně horší; říká, co je **pro tento jednoduchý školní postup** méně přímočaré.

| Produkt | + Oproti Data Studiu | − Oproti Data Studiu v našem kurzu |
| --- | --- | --- |
| **Microsoft Power BI** | Power Query umí rozsáhleji čistit a měnit data; datový model propojuje tabulky a podporuje výpočty v DAX. | Pro plný postup s přípravou a modelem se používá hlavně aplikace Power BI Desktop pro Windows; hotový report se pak publikuje do online služby. Pro tři připravené listy je to více kroků. [Microsoft: Power BI](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview) |
| **Tableau + Tableau Prep** | Tableau podporuje podrobnější analytické výpočty; Tableau Prep umožňuje sestavit opakovatelný postup pro čištění, spojování a přetváření dat. | Příprava dat přes Tableau Prep je další pracovní krok a nástroj. U našich malých, již vyčištěných CSV jej nepotřebujeme. [Tableau: výpočty](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm), [Tableau Prep](https://help.tableau.com/current/prep/en-us/prep_about.htm) |
| **Metabase** | Lze ukládat databázové dotazy včetně SQL a pravidelně posílat výsledky dashboardu e-mailem nebo do Slacku. | Je orientovaný hlavně na databáze. Synchronizace přímo z Google Sheets vyžaduje Metabase Cloud s doplňkem Cloud Storage, takže naše připojení tabulek není tak přímočaré. [Metabase: dotazy](https://www.metabase.com/docs/latest/questions/start), [odběry dashboardů](https://www.metabase.com/docs/latest/dashboards/subscriptions), [Google Sheets](https://www.metabase.com/docs/latest/cloud/google-sheets) |

Pro naše malé, předem připravené výukové tabulky je Data Studio vhodná volba: studenti se mohou soustředit na smysl grafu, filtru a popisku. Nejdříve však potřebujeme rozumět tomu, **co data PISA skutečně měří**. Tomu se věnuje [kapitola 1](01-pisa-a-interpretace.md).
