# 6. Změny a rozložení výsledků

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Graf publikované změny, skládaný graf rozložení a bodový graf.
</div>

Vytvořte stránku `Změny a rozložení`. Každý pohled odpovídá jiné otázce, proto u něj uveďte oblast a populaci přímo v názvu.

## Pohled 6: změna 2022–2025

1. Přidejte vodorovný pruhový graf ze zdroje `PISA25_Vysledky`.
2. Dimenze: `zeme`. Metrika: `zmena_2022_2025`, Average.
3. Filtr AND: `typ = Zeme`, `oblast = Přírodní vědy`.
4. Řaďte metriku sestupně, zapněte datové popisky a viditelnou nulu.
5. Nadpis: `Publikovaná změna v přírodních vědách 2022–2025, body`.
6. Doplňte poznámku: „Různé kohorty patnáctiletých. Graf nevyhodnocuje statistickou významnost změny.“

Kontrola: ČR −7, Slovensko +13. OECD výslovně popisuje českou změnu jako statisticky nevýznamnou. Samotná délka pruhu neprokazuje změnu. [OECD: ČR](https://gpseducation.oecd.org/CountryProfile?primaryCountry=CZE&topic=PI&treshold=10), [Slovensko](https://gpseducation.oecd.org/CountryProfile?primaryCountry=SVK&topic=PI&treshold=10).

Tento soubor poskytuje publikované rozdíly, ne plnou časovou řadu. Pro spojnicový graf nejprve stáhněte skóre pro jednotlivé cykly ze zdrojových tabulek OECD a srovnatelnost ověřte. Nezapisujte chybějící cykly jako nuly a nevytvářejte umělé hodnoty zpětným dopočtem.

## Pohled 7: podíl slabých, středních a špičkových výsledků

Přepněte zdroj na `PISA25_Rozlozeni`. Pod úrovní 2 znamená nedosažení základní úrovně; úrovně 5 a 6 označují špičkové výsledky. Podíly jsou připravené pro přírodní vědy, čtení i matematiku. Jednotlivé oblasti se ale nesmějí v jednom pruhu zprůměrovat.

1. Přidejte rozbalovací seznam ze zdroje `PISA25_Rozlozeni` s ovládacím polem `oblast`.
2. Zapněte **jediný výběr**, nastavte výchozí hodnotu `Přírodní vědy` a vypněte možnost vybrat vše. Bez jediné vybrané oblasti by graf smísil tři různé výsledky. [Google: nastavení rozbalovacího seznamu](https://docs.cloud.google.com/data-studio/drop-down-list-and-fixed-size-list-control)
3. Přidejte vodorovný skládaný pruhový graf se 100% zobrazením a zdrojem `PISA25_Rozlozeni`.
4. Dimenze: `zeme`. Metriky v tomto pořadí: `podil_pod_2`, `podil_2_4`, `podil_5_6`. U všech nastavte typ Procenta a agregaci Average. Prostřední podíl už v CSV je; vznikl jako `1 - podil_pod_2 - podil_5_6`.
5. Při jediné vybrané oblasti se zobrazí 11 řádků včetně OECD, aby bylo rozložení možné porovnat s referencí. B-S-J-Z zde není, protože pro region nemáme ověřené podíly.
6. Použijte stabilní barvy, například červenooranžovou pro pod úrovní 2, šedou pro 2–4 a zelenou pro 5–6. Legendu přejmenujte srozumitelnými popisky.
7. Zobrazte podíly na jedno desetinné místo a přidejte název `Rozložení výsledků PISA 2025 podle oblasti`. Aktuální oblast musí být vidět v ovladači.

Kontrola pro ČR v pořadí pod úrovní 2 / úrovně 2–4 / úrovně 5–6:

| Oblast | Český pruh |
| --- | --- |
| Přírodní vědy | 21,3 % / 71,7 % / 7,0 % |
| Čtení | 27,0 % / 67,9 % / 5,1 % |
| Matematika | 29,0 % / 61,2 % / 9,8 % |

Každý pruh má součet 100 %. Prostřední skupina je výukový dopočet ze zaokrouhlených krajních podílů; drobné rozdíly vůči nezaokrouhleným tabulkám mohou vzniknout zaokrouhlením. [OECD: tabulky I.B1.2a.10–12](https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/results-for-countries-and-economies_33854635.html).

Interpretace: dvě země mohou mít podobný průměr, ale jiné podíly slabých a špičkových výsledků. Pro plánování podpory je proto průměr jen část informace.

## Pohled 8: bodový graf

1. Přidejte bodový graf ze zdroje `PISA25_Rozlozeni`.
2. Dimenze určující jednotlivé body: `zeme`. Filtr: `typ = Zeme`.
3. Metrika osy X: `skore`, Average. Metrika osy Y: `podil_pod_2`, Average.
4. Velikost bodů ponechte stejnou. Nemáme zde údaj o počtu žáků, kterým by bylo vhodné ji řídit.
5. Zapněte názvy zemí nebo jejich zobrazení po najetí a osy pojmenujte včetně jednotek.
6. Nadpis: `Průměrné skóre a podíl pod úrovní 2, PISA 2025`.
7. Označte ovladač oblasti, skládaný graf a bodový graf a seskupte je. Vyzkoušejte postupně všechny tři oblasti; graf změny ze zdroje `PISA25_Vysledky` ponechte mimo skupinu. V žádném pohledu se nesmí objevit průměr přes více oblastí.

Pokud rozhraní nabídne bublinový graf s povinnou metrikou velikosti, zvolte základní bodový typ. [Google: bodové grafy](https://docs.cloud.google.com/data-studio/scatter-chart-reference)

Otázka: kde leží země s vyšším skóre a nižším podílem slabých výsledků? Očekávejte pravý dolní směr. Z tohoto grafu nevyvozujte účinek konkrétní školské politiky. Oba ukazatele navíc popisují stejné rozdělení výkonu, takže jejich souvislost není nezávislým důkazem příčiny.

## Závěr pro poradu

Vyberte jeden pohled a napište tři věty: co pozorujete, co z dostupných údajů nezjistíte a jakou konkrétní diagnostickou úlohu připravíte pro vlastní žáky. Pedagogický návrh označte jako návrh k ověření, ne jako prokázané řešení národního výsledku.
