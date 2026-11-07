# Data a datový slovník

## Tři zdroje pro celý kurz

Pro základní report PISA 2025 i trendy 2015–2025 importujte **pouze tyto tři CSV**, každé do jednoho listu Google Sheets. Starší snímky za samotný rok 2025 a zvláštní trendové kopie už nejsou potřeba.

| List | Soubor | Datových řádků | Klíč |
| --- | --- | ---: | --- |
| `Vysledky` | [pisa-vysledky.csv](pisa-vysledky.csv) | 141 | `zeme + cyklus + oblast + populace` |
| `Rozlozeni` | [pisa-rozlozeni.csv](pisa-rozlozeni.csv) | 141 | `zeme + cyklus + oblast + populace` |
| `Druhy_skol_CR` | [pisa-cesko-druhy-skol.csv](pisa-cesko-druhy-skol.csv) | 60 | `zeme + cyklus + oblast + druh_skoly` |

První dvě tabulky obsahují deset vybraných zemí × čtyři cykly × tři oblasti, region B-S-J-Z jen v letech 2018 a 2025, stálou referenci 35 zemí OECD ve všech cyklech a běžný průměr OECD pouze v roce 2025. Školní tabulka obsahuje pět českých druhů škol × čtyři cykly × tři oblasti. Nejde o úplnou světovou databázi ani o individuální žáky. CSV jsou v UTF-8, oddělovačem je čárka a desetinným znakem tečka.

## Společná pole

| Pole | Význam |
| --- | --- |
| `zeme`, `iso3` | Český popisek entity a ISO3 pro deset zemí; region a reference nemají ISO3 |
| `typ` | `Zeme`, `Region`, `Reference` (běžný průměr OECD 2025), `Reference_stala` (stálých 35 zemí); ve školní tabulce není |
| `cyklus` | Rok měření: 2015, 2018, 2022, 2025 |
| `datum_cyklu` | Technické datum 1. ledna příslušného roku pro skutečné rozestupy na časové ose; **není to den testování** |
| `oblast` | Matematika, Čtení, Přírodní vědy |
| `populace` | Mezinárodní tabulky: patnáctiletí v cílové populaci PISA; školní tabulka: patnáctiletí žáci daného druhu školy |
| `skore` | Zaokrouhlený bodový odhad výkonu, nikoli procento ani školní známka |
| `zdroj_url` | Odkaz na původ konkrétního řádku |

Rok 2018 až 2022 je **čtyřletý interval**. Nikdy neprůměrujte skóre přes roky, oblasti nebo země. Původní datové zdroje mají odlišnou populaci od české školní tabulky.

## Výsledky zemí

Skóre a `se_skore` pro všechny čtyři cykly jsou z [trendových tabulek OECD I.B1.2a.36–38](https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/results-for-countries-and-economies_33854635.html) ([XLSX OECD](https://stat.link/mrq53f)). Standardní chyba `se_skore` se vztahuje k **jednomu** odhadu; není chybou rozdílu dvou let. Významnost trendu ověřujte v publikovaných testech OECD.

| Pole | Význam |
| --- | --- |
| `oecd_skore` | Běžný průměr OECD pro stejnou oblast **roku 2025**, opakovaný u všech zemí a regionu pro jednoduchý výpočet rozdílu; v letech 2015–2022 a u stálé reference prázdný |
| `zmena_2022_2025` | Publikovaná změna 2022–2025 v bodech, jen na řádcích roku 2025; u B-S-J-Z a stálé reference prázdná, nikdy nula jako náhrada chybějících dat |
| `se_skore` | Standardní chyba bodového odhadu v bodech |

Průměr `Průměr OECD (stálých 35)` je časová řada se stejným složením zemí. **Není totožný** s běžným `Průměr OECD` pro rok 2025: například v přírodních vědách mají 484, resp. 482 bodů. Pro trendový graf použijte stálou referenci; pro základní graf roku 2025 běžnou. `oecd_skore` ze starších cyklů záměrně nevyplňujeme smíšeným průměrem.

## Rozložení výsledků

Podíly pod úrovní 2 a na úrovni 5 nebo vyšší jsou z [tabulek OECD I.B1.2a.33–35](https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/results-for-countries-and-economies_33854635.html). Jsou zaokrouhleny na jedno desetinné místo procenta a uloženy jako zlomky: **21,3 % = 0.213**. `podil_2_4` je dopočet `1 - podil_pod_2 - podil_5_6`, aby měl každý řádek přesně 100 %. Procentní podíly se nesčítají mezi zeměmi ani mezi roky.

`skore` se v `Rozlozeni` opakuje pro možnost bodového grafu; odpovídá stejnému řádku ve `Vysledky`. Oba listy v reportu nespojujte do jedné tabulky, jinak můžete hodnoty zdvojit. Region B-S-J-Z má ve sjednocené tabulce ověřené podíly pro roky 2018 a 2025, ale v základním grafu zemí se zobrazuje odděleně.

## Výsledky českých druhů škol

Pole `druh_skoly` rozlišuje základní školu, víceleté a čtyřleté gymnázium, SOŠ s maturitou a SOU bez maturity. `zdroj_metoda` zaznamenává původ odhadu v každém cyklu:

- **2015:** tabulky 7.3–7.5 [národní zprávy ČŠI](https://csi.gov.cz/Csicr/media/Prilohy/PDF_el._publikace/Mezin%C3%A1rodn%C3%AD%20%C5%A1et%C5%99en%C3%AD/NZ_PISA_2015.pdf).
- **2018:** tabulka 1 [školní zprávy PISA 2018 vytvořené ČŠI](https://www.gymzl.cz/wcd/articles/2019_2020/2020_02_pisa/gv58_sk_zpr.pdf), obsahující společné výsledky podle druhů škol.
- **2022:** vážený průměr všech deseti plausible values pro každou oblast z [národní žákovské databáze ČŠI](https://csicr.cz/cz/Mezinarodni-setreni/PISA/Datove-soubory-a-dotazniky/PISA-2022), podle proměnné `Druh_skoly` a váhy `W_FSTUWT`. Kontrola výpočtu: publikované hodnoty matematiky jsou 457, 591, 568, 502 a 408 bodů.
- **2025:** grafy 2.1.14, 2.3.3 a 2.4.4 [národní zprávy ČŠI](https://csi.gov.cz/CSICR/media/Prilohy/2024_p%C5%99%C3%ADlohy/Dokumenty/PISA-2025_final.pdf).

Školní skupiny představují **různé kohorty patnáctiletých žáků**, nikoli tytéž žáky v čase. Výsledky skupin ovlivňuje i jejich složení; nepřisuzujte rozdíly automaticky účinku školy. Školní tabulka nemá standardní chyby ani počty respondentů. Nevyvozujte z ní významnost malých změn a nesčítejte pět skupin do prostého celostátního průměru.

## Chybějící hodnoty a kontrola

B-S-J-Z znamená Peking, Šanghaj, Ťiang-su a Če-ťiang, **ne celou Čínu**. [OECD uvádí](https://www.oecd.org/en/about/programmes/pisa/pisa-frequently-asked-questions-faqs.html), že v roce 2022 tam neproběhl sběr; v roce 2015 měly zúčastněné čínské oblasti jiné složení. Proto pro B-S-J-Z nejsou řádky 2015 a 2022. Nepřipojujte čáru přes chybějící rok bez vysvětlení. USA mají v [tabulkách OECD](https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/results-for-countries-and-economies_33854635.html) upozornění na výběrové standardy; srovnání interpretujte opatrně.

Reprodukovatelný postup je v `project_docs/pisa_trends.py`. Používá oficiální [XLSX OECD](https://stat.link/mrq53f) a český žákovský SAV z [národní databáze ČŠI PISA 2022](https://csicr.cz/cz/Mezinarodni-setreni/PISA/Datove-soubory-a-dotazniky/PISA-2022); vyžaduje balíčky `openpyxl` a `pyreadstat`. Parametry `--oecd-xlsx` a `--csi-2022-sav` zadávají místní soubory, `--check` ověřuje uložená CSV bez přepsání. Surové žákovské soubory nejsou součástí Gitu.

## Rozšíření z veřejného žákovského souboru OECD

Samostatná odborná kapitola používá tři **volitelné** tabulky vypočtené z `CY09_MS_STU_PUF.sav` (PISA 2025 Public Use File) dne 6. listopadu 2026. Nejsou součástí tří základních zdrojů. Reprodukovatelný postup je v `project_docs/pisa2025_aggregate.py`; surová mikrodata se nepublikují. Výpočet používá finální žákovskou váhu `W_FSTUWT`, všech deset plausible values a 80 replikačních vah `W_FSTURWT1` až `W_FSTURWT80`. Standardní chyba kombinuje Fayovu replikační a imputační varianci podle [metodiky OECD](https://www.oecd.org/en/about/programmes/pisa/how-to-prepare-and-analyse-the-pisa-database.html).

- [pisa2025-mikrodata-zeme.csv](pisa2025-mikrodata-zeme.csv): deset zemí a B-S-J-Z × tři oblasti, bez průměru OECD. Kód `QCI` znamená B-S-J-Z, ne celou Čínu.
- [pisa2025-mikrodata-cr-druhy-skol.csv](pisa2025-mikrodata-cr-druhy-skol.csv): pět českých skupin × tři oblasti; pole `kody_programu` ukazuje původní kódy `PROGN`.
- [pisa2025-mikrodata-cr-programy.csv](pisa2025-mikrodata-cr-programy.csv): podrobnosti českých kódů `PROGN`; skupiny s méně než 30 platnými žáky jsou vynechány.

`skore` je vážený průměr napříč plausible values, `se_skore` standardní chyba v bodech, `n_zaku` nevážený počet platných žáků a `vazena_populace` součet vah. Tyto nezaokrouhlené výpočty nezaměňujte s hodnotami přepsanými z grafů ČŠI. Například čtení u SOU bez maturity dává z veřejného souboru 391,270 bodu, zatímco graf ČŠI uvádí 392; příčina rozdílu bez národního analytického kódu není potvrzena.
