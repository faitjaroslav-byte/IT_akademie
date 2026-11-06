# 2. Příprava dat

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Tři čisté listy v Google Sheets se správně rozpoznanými čísly a jednoznačnými řádky.
</div>

## Připravený datový výběr

Stáhněte [výsledky](data/pisa2025-vysledky.csv), [rozložení ve třech oblastech](data/pisa2025-rozlozeni.csv) a [české druhy škol](data/pisa2025-cesko-druhy-skol.csv). Jedná se o publikované agregace OECD a ČŠI, nikoli o smyšlené žákovské záznamy. Výběr zahrnuje deset zemí z Evropy, Asie a Severní Ameriky, region B-S-J-Z a referenci OECD; nejde o úplnou světovou databázi. Podíly pro region B-S-J-Z v druhém souboru nejsou.

Dlouhá tabulka `Vysledky` má jeden řádek pro kombinaci **entita × cyklus × oblast × populace**. Pro deset zemí, region B-S-J-Z a referenci OECD ve třech oblastech obsahuje 36 řádků. Referenční skóre OECD je navíc v samostatném sloupci každého řádku, aby zůstalo k dispozici i po filtrování země.

Tabulka `Rozlozeni` má 33 řádků: deset zemí a referenci OECD ve třech oblastech. V každém řádku jsou podíly pod úrovní 2, na úrovních 2–4 a na úrovních 5–6. Oblast je součástí klíče řádku; pro jeden graf vždy vyberte právě jednu oblast.

Tabulka `Druhy_skol_CR` má 15 řádků: pět českých druhů škol ve třech oblastech. Čísla pocházejí z grafů národní zprávy ČŠI. Není to členění podle typu školy pro jiné země.

## Import do Google Sheets krok za krokem

1. Na Disku vytvořte novou Tabulku Google s názvem `PISA 2025 – kurz`.
2. Otevřete **Soubor → Importovat → Nahrát** a vyberte první CSV.
3. Zvolte vložení nového listu. Jako oddělovač vyberte **čárku**. Zkontrolujte, že se hlavičky rozdělily do samostatných sloupců.
4. List přejmenujte na `Vysledky`.
5. Druhé CSV importujte do dalšího listu a přejmenujte ho na `Rozlozeni`.
6. Třetí CSV importujte do listu `Druhy_skol_CR`. Ověřte číslo například součtem dvou buněk se skóre. Pokud součet nefunguje, čísla jsou pravděpodobně text.
7. CSV používá desetinnou tečku. Pokud místní nastavení tabulky čísla nepřevede, nastavte pro import **Soubor → Nastavení → Národní prostředí → Spojené státy**, import zopakujte a ověřte čísla. České popisky v datech zůstanou zachovány.
8. Ukotvěte první řádek a zapněte filtr. Nepřidávejte nad hlavičku další nadpis, součtový řádek ani sloučené buňky.

## Důležitá pole

| Pole | Význam | Typ v Looker Studio |
| --- | --- | --- |
| `zeme` | Český popisek země či reference | Text |
| `iso3` | ISO kód; u regionu a reference prázdný | Země / Country |
| `typ` | `Zeme`, `Region` nebo `Reference` | Text |
| `cyklus` | Rok šetření 2025 | Číslo, bez agregace |
| `oblast` | Matematika, Čtení, Přírodní vědy | Text |
| `skore` | Zaokrouhlený publikovaný odhad | Číslo |
| `oecd_skore` | Reference pro tutéž oblast a cyklus | Číslo |
| `zmena_2022_2025` | Publikovaná změna v bodech | Číslo |
| `podil_pod_2` | Podíl pod úrovní 2, např. 0.213 | Procenta |
| `podil_2_4` | Dopočtený podíl na úrovních 2–4 | Procenta |
| `podil_5_6` | Podíl na úrovních 5 a 6 | Procenta |
| `zdroj_url` | Dohledatelný původ výsledku | URL nebo text |

Úplný popis tří souborů najdete v [datovém slovníku](data/README.md).

## Kontrola před připojením

List `Vysledky` má 37 řádků včetně hlavičky. Při filtru `CZE` najdete tři řádky a pro přírodní vědy skóre 490. List `Rozlozeni` má 34 řádků včetně hlavičky a `Druhy_skol_CR` má 16 řádků včetně hlavičky. V `Rozlozeni` jsou pro ČR tři řádky. Podíl pod úrovní 2 činí v matematice **29,0 %**, ve čtení **27,0 %** a v přírodních vědách **21,3 %**. Poslední hodnota je v CSV zapsána jako **0.213**; číslo 21.3 formátované jako procento by zobrazilo 2130 %.

Kontrolní hodnoty vycházejí z [profilu ČR v OECD Education GPS](https://gpseducation.oecd.org/CountryProfile?primaryCountry=CZE&topic=PI&treshold=10) a [tabulek OECD I.B1.2a.10–12](https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/results-for-countries-and-economies_33854635.html).

## Pro vlastní rozšíření

Přidáváte-li země, přebírejte údaje ze stejného cyklu a stejné populace. Chybějící údaj ponechte prázdný; nula znamená skutečnou nulovou hodnotu. Nedoplňujte standardní chybu odhadem. Celkové průměry, odhady pro podskupiny a jednotlivé žáky ukládejte do oddělených zdrojů s vlastní granularitou.

Úkol: vysvětlete kolegovi, proč nelze sečíst tři řádky skóre ČR a výsledek označit jako celkový výkon země.
