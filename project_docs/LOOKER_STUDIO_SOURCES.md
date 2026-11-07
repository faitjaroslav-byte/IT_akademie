# Looker Studio: redakční záznam

Ověřeno 2026-11-05. Kurz rozšiřuje IT akademii jako druhý samostatný kurz. Původní PROJECT_STANDARD je převzatý z jiné učebnice; používáme jeho jazyková a typografická pravidla, nikoli osnovu EL2.

## Rozhodnutí o datech

OECD nyní zveřejňuje PISA 2025. FAQ uvádí první publikaci 8. září 2026. Education GPS zobrazuje profily PISA 2025. Ručně převzatý výběr zahrnuje deset národních profilů: CZE, SVK, DEU, AUT, POL, EST, FIN, SGP, KOR, USA. Údaje B-S-J-Z jsou regionálním výsledkem z OECD executive summary, nikoli národním výsledkem Číny. U každého CSV řádku je zdroj a datum kontroly. Rozložení pro čtení a matematiku bylo 6. listopadu 2026 doplněno z oficiální přílohy OECD I.B1.2a.11 a I.B1.2a.12 (https://stat.link/mrq53f); přírodovědné podíly odpovídají tabulce I.B1.2a.10. Jednotlivé úrovně pod 2 a na 5–6 byly sečteny, zaokrouhleny na jedno desetinné místo a převedeny na zlomek. Podíl úrovní 2–4 je zbytek do 100 % po zaokrouhlení krajních skupin. Výukové dopočty, například rozdíl skóre proti OECD, vznikají v Data Studiu.

Zdroje jsou uvedeny v publikovaném datovém slovníku jako provenance dat. Základní mezinárodní soubory obsahují cykly 2015, 2018, 2022 a 2025, zaokrouhlené skóre a v souboru výsledků také standardní chybu skóre. Neobsahují intervaly spolehlivosti ani odhady podle druhu školy; ty jsou v samostatném českém školním souboru bez standardních chyb. Publikovaná změna 2022–2025 se používá přímo, nikoli k rekonstrukci skóre 2022. ČR science 490 a změna −7 mohou působit odlišně od rozdílu zaokrouhlených výsledků z různých vydání; nepřepisujeme publikované vstupy.

Mezinárodní agregace představují celou věkovou populaci PISA. Třetí CSV přepisuje hodnoty pro pět českých druhů škol z grafů 2.1.14, 2.3.3 a 2.4.4 národní zprávy ČŠI PISA 2025; nebyly doplněny standardní chyby ani podskupiny jiných zemí. Samostatná kapitola vysvětluje hranice srovnatelnosti a přípravu dalších vážených odhadů. Hotový nativní report na účtu Google není součástí dodávky; kurz obsahuje návody a vstupní data. Interní step-by-step postup pro lektora je pouze v repozitáři v `project_docs/LOOKER_STUDIO_MANUAL_PRO_UCITELE.md` a není publikovaný na webu.

## Dokumentace produktu

- Google Sheets: https://docs.cloud.google.com/data-studio/connect-to-google-sheets
- Vypočtená pole: https://docs.cloud.google.com/data-studio/about-calculated-fields
- Ovladače: https://docs.cloud.google.com/data-studio/add-edit-controls
- Pivot: https://docs.cloud.google.com/data-studio/pivot-table-reference
- Mapy: https://docs.cloud.google.com/data-studio/google-maps-reference
- Bodový graf: https://docs.cloud.google.com/data-studio/scatter-chart-reference
- Přístup ke zdroji: https://docs.cloud.google.com/data-studio/data-credentials-article
- Změna názvu na Data Studio: https://docs.cloud.google.com/data-studio/release-notes (2026-04-16).

Návody byly zkontrolovány vůči dokumentaci, nikoli průchodem přihlášenou aplikací. Před živým školením je nutný referenční report a ověření oprávnění školního účtu, jak uvádí manuál.

## Sjednocené časové řady (2026-11-07)

Tři publikované soubory `pisa-vysledky.csv`, `pisa-rozlozeni.csv` a `pisa-cesko-druhy-skol.csv` spojují základní pohled na rok 2025 a trendy 2015–2025. V Google Sheets se importují pouze tři listy a v reportu se používají pouze tři základní datové zdroje. Základní grafy mají pevný filtr `cyklus = 2025`; trendové grafy čtou stejné zdroje bez něj. Původní samostatné snímky 2025 a trendové CSV zůstávají dohledatelné v historii Gitu, nikoli v publikovaném kurzu.

Skript `project_docs/pisa_trends.py` čte oficiální XLSX OECD I.B1.2a.33–38 (https://stat.link/mrq53f) a národní žákovský SAV ČŠI PISA 2022 (https://csicr.cz/cz/Mezinarodni-setreni/PISA/Datove-soubory-a-dotazniky/PISA-2022). Hodnoty českých školních skupin za 2015, 2018 a 2025 jsou v něm zaznamenány z publikovaných zpráv ČŠI. OECD workbook poskytuje skóre, jejich standardní chyby a krajní podíly pro 2015, 2018, 2022 a 2025. Ve výsledkových souborech je běžný průměr OECD pouze pro rok 2025 a pevná reference `OECD average-35` pro všechny čtyři cykly; nesmějí se zaměňovat. B-S-J-Z má jen výsledky 2018 a 2025; v roce 2015 se testovala jiná čtveřice čínských oblastí a v roce 2022 tam sběr neproběhl.

Školní hodnoty 2015 jsou doslova z tabulek 7.3–7.5 národní zprávy ČŠI (https://csi.gov.cz/Csicr/media/Prilohy/PDF_el._publikace/Mezin%C3%A1rodn%C3%AD%20%C5%A1et%C5%99en%C3%AD/NZ_PISA_2015.pdf); hodnoty 2018 jsou z tabulky 1 školní zprávy ČŠI dostupné na webu školy (https://www.gymzl.cz/wcd/articles/2019_2020/2020_02_pisa/gv58_sk_zpr.pdf). Školní hodnoty 2022 jsme vypočítali z proměnné `Druh_skoly`, finální váhy `W_FSTUWT` a všech 10 plausible values pro matematiku, čtení a přírodovědu. Výsledek matematických skupin přesně odpovídá pěti publikovaným číslům v grafu 3.8 národní zprávy ČŠI (https://csi.gov.cz/CSICR/media/Prilohy/2023_p%C5%99%C3%ADlohy/Mezin%C3%A1rodn%C3%AD%20%C5%A1et%C5%99en%C3%AD/PISA_2022_e-verze-9.pdf). V SAV jsme nepočítali standardní chyby skupin a do Gitu se nedostávají surové záznamy.
