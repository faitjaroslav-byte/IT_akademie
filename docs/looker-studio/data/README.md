# Data a datový slovník

## Co soubory obsahují

[pisa2025-vysledky.csv](pisa2025-vysledky.csv) a [pisa2025-rozlozeni.csv](pisa2025-rozlozeni.csv) jsou výukový výběr skutečných agregací PISA 2025 publikovaných OECD. [pisa2025-cesko-druhy-skol.csv](pisa2025-cesko-druhy-skol.csv) obsahuje české výsledky podle druhu školy přepsané z grafů národní zprávy ČŠI. Skóre a přírodovědné podíly byly převzaty 5. listopadu 2026; podíly pro čtení a matematiku 6. listopadu 2026. Nejde o úplnou světovou databázi ani mikrodata.

CSV používají UTF-8, čárku mezi poli a desetinnou tečku. Hlavička je na prvním řádku. Podíly jsou po zaokrouhlení na jedno desetinné místo převedeny z procent na zlomky: 21,3 % je uloženo jako 0.213. Skóre a publikované změny jsou převzaty v zaokrouhlené podobě. Ze změn nelze přesně rekonstruovat nezaokrouhlené výsledky roku 2022.

## Společná pole

| Pole | Význam a pravidlo |
| --- | --- |
| `zeme` | Český název země, označení regionu B-S-J-Z nebo Průměr OECD |
| `iso3` | ISO3 pro deset zemí; pro B-S-J-Z a OECD prázdné |
| `typ` | Zeme / Region / Reference; filtr mapy a národních srovnání používá Zeme |
| `cyklus` | 2025, rok šetření |
| `oblast` | Matematika / Čtení / Přírodní vědy |
| `populace` | Všichni patnáctiletí v cílové populaci PISA, ne pouze SŠ |
| `skore` | Publikovaný bodový odhad na škále dané oblasti |
| `zdroj_url` | Profil OECD, ze kterého je údaj převzat |
| `overeno` | Datum kontroly zdroje; není rokem měření |

## Pole tabulky Vysledky

36 datových řádků: deset zemí, jeden region a jedna reference × tři oblasti. Klíč: `zeme + cyklus + oblast + populace`.

| Pole | Význam |
| --- | --- |
| `oecd_skore` | Publikovaná reference OECD pro tutéž oblast a cyklus, opakovaná záměrně u každé země |
| `zmena_2022_2025` | Publikovaný rozdíl mezi odhady 2025 a 2022, v bodech; u B-S-J-Z prázdný, nikoli nula |

## Pole tabulky Rozlozeni

33 datových řádků: deset zemí a reference OECD ve třech oblastech. Klíč: `zeme + cyklus + oblast + populace`. B-S-J-Z chybí, protože pro tento region nemáme ve výběru ověřené podíly. `skore` pro každou kombinaci odpovídá tabulce `Vysledky`; soubory v reportu nespojujte do jedné tabulky, protože byste stejné skóre zdvojili.

| Pole | Význam |
| --- | --- |
| `podil_pod_2` | Podíl žáků pod základní úrovní 2, od 0 do 1 |
| `podil_2_4` | Dopočtený podíl na úrovních 2 až 4, od 0 do 1 |
| `podil_5_6` | Podíl žáků na úrovních 5 a 6, od 0 do 1 |

Podíly pro matematiku a čtení jsou součty příslušných úrovní z [tabulek OECD I.B1.2a.11 a I.B1.2a.12](https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/results-for-countries-and-economies_33854635.html) ([XLSX OECD](https://stat.link/mrq53f)). Přírodovědné podíly z profilů OECD se po zaokrouhlení shodují s tabulkou I.B1.2a.10. Prostřední skupina je ve všech oblastech dopočtena jako `1 - podil_pod_2 - podil_5_6`, proto součet tří sloupců v každém řádku činí 100 %. Drobné rozdíly proti součtu nezaokrouhlených podílů jednotlivých úrovní jsou možné. Skóre, reference, změny a podíly se nesčítají přes země nebo oblasti. Average zachová jeden konkrétní odhad při správném filtru; nezajišťuje automaticky správný průměr populace.

Pokud už máte starý list `Prirodni_vedy`, nahraďte jej novým CSV jako list `Rozlozeni` a v reportu obnovte nebo znovu připojte příslušný datový zdroj. Oba listy současně nepoužívejte jako dvě verze téhož rozložení.
Původní [přírodovědný CSV](pisa2025-prirodni-vedy.csv) zůstává dostupný kvůli starším odkazům, ale další výuka používá společný soubor `pisa2025-rozlozeni.csv`.

## Pole tabulky Druhy_skol_CR

15 datových řádků: pět českých druhů škol × tři oblasti. Klíč: `zeme + cyklus + oblast + druh_skoly`. Pole `druh_skoly` rozlišuje základní školu, víceleté a čtyřleté gymnázium, SOŠ s maturitou a SOU bez maturity. Pole `zdroj_obrazek` uvádí číslo grafu národní zprávy: 2.1.14 (přírodní vědy), 2.3.3 (čtení), 2.4.4 (matematika). Pole `skore` je bodový odhad pro patnáctileté žáky daného druhu školy; standardní chyby a počty respondentů v tomto výběru nejsou. [Národní zpráva ČŠI PISA 2025](https://csi.gov.cz/CSICR/media/Prilohy/2024_p%C5%99%C3%ADlohy/Dokumenty/PISA-2025_final.pdf).

## Zdroje jednotlivých zemí

| Země | Primární zdroj |
| --- | --- |
| Česko a reference OECD | [OECD Education GPS: CZE](https://gpseducation.oecd.org/CountryProfile?primaryCountry=CZE&topic=PI&treshold=10) |
| Slovensko | [OECD Education GPS: SVK](https://gpseducation.oecd.org/CountryProfile?primaryCountry=SVK&topic=PI&treshold=10) |
| Německo | [OECD Education GPS: DEU](https://gpseducation.oecd.org/CountryProfile?primaryCountry=DEU&topic=PI&treshold=10) |
| Rakousko | [OECD Education GPS: AUT](https://gpseducation.oecd.org/CountryProfile?primaryCountry=AUT&topic=PI&treshold=10) |
| Polsko | [OECD Education GPS: POL](https://gpseducation.oecd.org/CountryProfile?primaryCountry=POL&topic=PI&treshold=10) |
| Estonsko | [OECD Education GPS: EST](https://gpseducation.oecd.org/CountryProfile?primaryCountry=EST&topic=PI&treshold=10) |
| Finsko | [OECD Education GPS: FIN](https://gpseducation.oecd.org/CountryProfile?primaryCountry=FIN&topic=PI&treshold=10) |
| Singapur | [OECD Education GPS: SGP](https://gpseducation.oecd.org/CountryProfile?primaryCountry=SGP&topic=PI) |
| Jižní Korea | [OECD Education GPS: KOR](https://gpseducation.oecd.org/CountryProfile?primaryCountry=KOR&topic=PI) |
| USA | [OECD Education GPS: USA](https://gpseducation.oecd.org/CountryProfile?primaryCountry=USA&topic=PI) |
| B-S-J-Z (Čína) | [OECD PISA 2025, executive summary](https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/executive-summary_3701b0ef.html) |

Profily jsou průběžně aktualizované webové stránky. Před dalším školením ověřte, že stále zobrazují cyklus 2025. B-S-J-Z znamená Peking, Šanghaj, Ťiang-su a Če-ťiang, nikoli celou Čínu. OECD upozorňuje, že USA nesplnily některé výběrové standardy, proto jejich srovnání interpretujte opatrně. Přiložené CSV zůstávají výukovým snímkem s uvedeným datem převzetí.

## Nejistota a další zpracování

Ve třech základních výukových CSV výše nejsou standardní chyby, intervaly spolehlivosti ani individuální žáci. Rozpad podle druhu školy je pouze pro ČR. Z rozdílu bodových odhadů bez chyb netestujte statistickou významnost.

## Rozšíření z veřejného žákovského souboru OECD

Nové tabulky byly vypočteny ze souboru `CY09_MS_STU_PUF.sav` (PISA 2025 Public Use File) dne 6. listopadu 2026. Surová mikrodata nejsou součástí webu ani Gitu. Reprodukovatelný postup je v repozitáři v `project_docs/pisa2025_aggregate.py`. Výpočet používá finální žákovskou váhu `W_FSTUWT`, všech deset plausible values pro každou oblast a 80 replikačních vah `W_FSTURWT1` až `W_FSTURWT80`. Standardní chyba kombinuje Fayovu replikační a imputační varianci podle [metodiky OECD](https://www.oecd.org/en/about/programmes/pisa/how-to-prepare-and-analyse-the-pisa-database.html).

- [pisa2025-mikrodata-zeme.csv](pisa2025-mikrodata-zeme.csv): 33 řádků, deset zemí a region B-S-J-Z × tři oblasti. Pole `kod` je kód PISA; `QCI` je B-S-J-Z, ne celá Čína. Neobsahuje průměr OECD.
- [pisa2025-mikrodata-cr-druhy-skol.csv](pisa2025-mikrodata-cr-druhy-skol.csv): 15 řádků, pět českých skupin × tři oblasti. Pole `kody_programu` ukazuje přesné kódy `PROGN` použité při seskupení. Kategorie víceletých gymnázií zahrnuje také konzervatoř, protože tak zní původní kódy 203002 a 203004.
- [pisa2025-mikrodata-cr-programy.csv](pisa2025-mikrodata-cr-programy.csv): detail jednotlivých českých kódů `PROGN`. Skupiny s méně než 30 platnými žáky jsou vynechány; hodnoty ostatních malých skupin interpretujte opatrně.

`skore` je vážený průměr napříč deseti plausible values v bodech; `se_skore` standardní chyba v bodech; `n_zaku` nevážený počet žáků s platnými hodnotami; `vazena_populace` součet vah, nikoli počet respondentů. V Looker Studio nepřepočítávejte z těchto řádků průměr přes různé země nebo školní skupiny. Desetinné hodnoty umožňují kontrolu, ve výukovém grafu zobrazte skóre na celé body.

Národní bodové odhady a chyby se po zaokrouhlení shodují s [přílohou národní zprávy ČŠI](https://csi.gov.cz/CSICR/media/Prilohy/2024_p%C5%99%C3%ADlohy/Dokumenty/PISA-2025_final.pdf). Výjimkou v českých školních kategoriích je například čtení u SOU bez maturity: přepočet z veřejného souboru pro `PROGN=203009` dává 391,270, zatímco graf ČŠI uvádí 392. Nezaměňujte tyto dvě verze dat a nepovažujte odchylku za chybu zaokrouhlení; může souviset s vymezením kategorie nebo verzí analytického souboru. Příčinu bez národního analytického kódu nelze potvrdit.
