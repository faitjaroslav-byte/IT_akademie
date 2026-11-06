# Looker Studio: redakční záznam

Ověřeno 2026-11-05. Kurz rozšiřuje IT akademii jako druhý samostatný kurz. Původní PROJECT_STANDARD je převzatý z jiné učebnice; používáme jeho jazyková a typografická pravidla, nikoli osnovu EL2.

## Rozhodnutí o datech

OECD nyní zveřejňuje PISA 2025. FAQ uvádí první publikaci 8. září 2026. Education GPS zobrazuje profily PISA 2025. Ručně převzatý výběr zahrnuje deset národních profilů: CZE, SVK, DEU, AUT, POL, EST, FIN, SGP, KOR, USA. Údaje B-S-J-Z jsou regionálním výsledkem z OECD executive summary, nikoli národním výsledkem Číny. U každého CSV řádku je zdroj a datum kontroly. Rozložení pro čtení a matematiku bylo 6. listopadu 2026 doplněno z oficiální přílohy OECD I.B1.2a.11 a I.B1.2a.12 (https://stat.link/mrq53f); přírodovědné podíly odpovídají tabulce I.B1.2a.10. Jednotlivé úrovně pod 2 a na 5–6 byly sečteny, zaokrouhleny na jedno desetinné místo a převedeny na zlomek. Podíl úrovní 2–4 je zbytek do 100 % po zaokrouhlení krajních skupin. Výukové dopočty, například rozdíl skóre proti OECD, vznikají v Data Studiu.

Zdroje jsou uvedeny v publikovaném datovém slovníku jako provenance dat. Mezinárodní soubor neobsahuje přesné skóre 2022, intervaly spolehlivosti ani odhady podle druhu školy. Publikovaná změna se používá přímo, nikoli jako cesta k rekonstrukci skóre 2022. ČR science 490 a změna −7 mohou působit odlišně od rozdílu zaokrouhlených výsledků z různých vydání; nepřepisujeme publikované vstupy.

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
