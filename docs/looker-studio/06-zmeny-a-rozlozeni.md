# 6. Změny a rozložení výsledků

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Graf publikované změny, skládaný graf rozložení a bodový graf.
</div>

Vytvořte stránku `Změny a rozložení`. Každý pohled odpovídá jiné otázce, proto u něj uveďte oblast a populaci přímo v názvu.

## Pohled 6: změna 2022–2025

1. Přidejte vodorovný pruhový graf ze zdroje `PISA_Vysledky`.
2. Dimenze: `zeme`. Metrika: `zmena_2022_2025`, Average.
3. Filtr AND: `typ = Zeme`, `cyklus = 2025`, `oblast = Přírodní vědy`.
4. Řaďte metriku sestupně, zapněte datové popisky a viditelnou nulu.
5. Nadpis: `Publikovaná změna v přírodních vědách 2022–2025, body`.
6. Doplňte poznámku: „Různé kohorty patnáctiletých. Graf nevyhodnocuje statistickou významnost změny.“

Kontrola: ČR −7, Slovensko +13. OECD výslovně popisuje českou změnu jako statisticky nevýznamnou. Samotná délka pruhu neprokazuje změnu. [OECD: ČR](https://gpseducation.oecd.org/CountryProfile?primaryCountry=CZE&topic=PI&treshold=10), [Slovensko](https://gpseducation.oecd.org/CountryProfile?primaryCountry=SVK&topic=PI&treshold=10).

Pole `zmena_2022_2025` obsahuje publikovaný rozdíl pouze u roku 2025. Časová řada `skore` je ve **stejném** zdroji; nevznikla zpětným dopočtem z rozdílu. Chybějící cykly nejsou nuly.

## Navazující pohled: časová řada 2015–2025

Po zvládnutí základního reportu použijte stejný list [Vysledky](data/pisa-vysledky.csv), tentokrát bez filtru `cyklus = 2025`. Skóre jednotlivých cyklů je převzaté přímo z [tabulek OECD](https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/results-for-countries-and-economies_33854635.html), není dopočítané z publikované změny.

1. Vytvořte **nový** graf ze zdroje `PISA_Vysledky`. Nekopírujte graf s pevným filtrem 2025, pokud jeho filtr sami neodstraníte.
2. Vytvořte stránku `Trendy zemí`. Vložte graf typu **Časová řada**. Dimenze: `datum_cyklu` (Date, zobrazení po rocích). Metrika: `skore` (Average). Rozkladová dimenze: `zeme`.
3. Nastavte filtr `oblast = Čtení` a vyberte čtyři řady: `Česko`, `Finsko`, `Estonsko`, `Průměr OECD (stálých 35)`. Ostatní země lze porovnat v kopii grafu. Region B-S-J-Z do hlavního trendu nezařazujte.
4. Zapněte značky měřených bodů a v názvu uveďte `Čtení: průměrné skóre patnáctiletých, 2015–2025`. Osa Y je v bodech PISA, nikoli v procentech. Na časové ose je mezi 2018 a 2022 správně čtyřletá mezera.
5. Zkontrolujte českou řadu: **487 → 490 → 489 → 468**. Trendovou referenci OECD neoznačujte jako běžný průměr všech současných členů; jde o stálou skupinu 35 zemí.

Chcete-li sledovat složení výsledků, použijte již připojený zdroj `PISA_Rozlozeni`. Pro filtr `zeme = Česko` a `oblast = Matematika` vložte 100% skládaný sloupcový graf: dimenze `cyklus`, metriky `podil_pod_2`, `podil_2_4`, `podil_5_6` (všechny Average a formát Procenta). Vypněte součty přes roky. Každý ze čtyř sloupců se musí rovnat 100 %; rozlišujte změnu podílu od změny skóre.

!!! warning "Trend není test významnosti"
    Body představují různé kohorty patnáctiletých. Pole `se_skore` udává nejistotu jednotlivého odhadu, nikoli přímo chybu rozdílu mezi dvěma roky. O statistické významnosti rozhodujte podle publikovaných trendových testů OECD, ne podle tvaru křivky. `datum_cyklu` je technické datum 1. ledna pro vykreslení časové osy, ne den testu.

## Pohled 7: podíl slabých, středních a špičkových výsledků

Přepněte zdroj na `PISA_Rozlozeni`. Pod úrovní 2 znamená nedosažení základní úrovně; úrovně 5 a 6 označují špičkové výsledky. Podíly jsou připravené pro přírodní vědy, čtení i matematiku. Jednotlivé oblasti ani cykly se nesmějí v jednom pruhu zprůměrovat.

1. Přidejte rozbalovací seznam ze zdroje `PISA_Rozlozeni` s ovládacím polem `oblast`.
2. Zapněte **jediný výběr**, nastavte výchozí hodnotu `Přírodní vědy` a vypněte možnost vybrat vše. Bez jediné vybrané oblasti by graf smísil tři různé výsledky. [Google: nastavení rozbalovacího seznamu](https://docs.cloud.google.com/data-studio/drop-down-list-and-fixed-size-list-control)
3. Přidejte vodorovný skládaný pruhový graf se 100% zobrazením a zdrojem `PISA_Rozlozeni`. Nastavte mu pevný filtr `cyklus = 2025`, `typ != Region` a `typ != Reference_stala`.
4. Dimenze: `zeme`. Metriky v tomto pořadí: `podil_pod_2`, `podil_2_4`, `podil_5_6`. U všech nastavte typ Procenta a agregaci Average. Prostřední podíl už v CSV je; vznikl jako `1 - podil_pod_2 - podil_5_6`.
5. Při jediné vybrané oblasti se zobrazí 11 řádků včetně běžného průměru OECD. B-S-J-Z a stálou trendovou referenci filtr tohoto základního grafu vylučuje; jejich podíly však ve zdroji jsou.
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

1. Přidejte bodový graf ze zdroje `PISA_Rozlozeni`.
2. Dimenze určující jednotlivé body: `zeme`. Filtr AND: `typ = Zeme`, `cyklus = 2025`.
3. Metrika osy X: `skore`, Average. Metrika osy Y: `podil_pod_2`, Average.
4. Velikost bodů ponechte stejnou. Nemáme zde údaj o počtu žáků, kterým by bylo vhodné ji řídit.
5. Zapněte názvy zemí nebo jejich zobrazení po najetí a osy pojmenujte včetně jednotek.
6. Nadpis: `Průměrné skóre a podíl pod úrovní 2, PISA 2025`.
7. Označte ovladač oblasti, skládaný graf a bodový graf a seskupte je. Vyzkoušejte postupně všechny tři oblasti; graf změny ze zdroje `PISA_Vysledky` ponechte mimo skupinu. U obou grafů ověřte filtr 2025; v žádném pohledu se nesmí objevit průměr přes více oblastí ani cyklů.

Pokud rozhraní nabídne bublinový graf s povinnou metrikou velikosti, zvolte základní bodový typ. [Google: bodové grafy](https://docs.cloud.google.com/data-studio/scatter-chart-reference)

Otázka: kde leží země s vyšším skóre a nižším podílem slabých výsledků? Očekávejte pravý dolní směr. Z tohoto grafu nevyvozujte účinek konkrétní školské politiky. Oba ukazatele navíc popisují stejné rozdělení výkonu, takže jejich souvislost není nezávislým důkazem příčiny.

## Závěr pro poradu

Vyberte jeden pohled a napište tři věty: co pozorujete, co z dostupných údajů nezjistíte a jakou konkrétní diagnostickou úlohu připravíte pro vlastní žáky. Pedagogický návrh označte jako návrh k ověření, ne jako prokázané řešení národního výsledku.
