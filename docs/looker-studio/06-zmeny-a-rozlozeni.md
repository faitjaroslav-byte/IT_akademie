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

Přepněte zdroj na `PISA25_Prirodni`. Pracujeme pouze s přírodními vědami. Pod úrovní 2 znamená nedosažení základní úrovně; úrovně 5 a 6 označují špičkové výsledky v této oblasti.

1. V tomto zdroji vytvořte pole `podil_2_4`:

```text
1 - podil_pod_2 - podil_5_6
```

2. Typ nastavte na Procenta, agregaci Average. Je to dopočtený zbytek z publikovaných, zaokrouhlených podílů.
3. Přidejte vodorovný skládaný pruhový graf se 100% zobrazením.
4. Dimenze: `zeme`. Metriky v tomto pořadí: `podil_pod_2`, `podil_2_4`, `podil_5_6`. U všech Average.
5. Ponechte 11 řádků včetně OECD, aby bylo rozložení možné porovnat s referencí. B-S-J-Z zde není, protože pro region nemáme ověřené podíly.
6. Použijte stabilní barvy, například červenooranžovou pro pod úrovní 2, šedou pro 2–4 a zelenou pro 5–6. Legendu přejmenujte srozumitelnými popisky.
7. Zobrazte podíly na jedno desetinné místo a přidejte název `Přírodovědná gramotnost: rozložení výsledků 2025`.

Český pruh má 21,3 %, dopočtených 71,7 % a 7,0 %. Součet je 100 %. Hodnota prostřední skupiny je výukový dopočet; drobné rozdíly vůči tabulkám s nezaokrouhlenými daty mohou vzniknout zaokrouhlením. [Zdroj vstupních podílů](https://gpseducation.oecd.org/CountryProfile?primaryCountry=CZE&topic=PI&treshold=10)

Interpretace: dvě země mohou mít podobný průměr, ale jiné podíly slabých a špičkových výsledků. Pro plánování podpory je proto průměr jen část informace.

## Pohled 8: bodový graf

1. Přidejte bodový graf ze zdroje `PISA25_Prirodni`.
2. Dimenze určující jednotlivé body: `zeme`. Filtr: `typ = Zeme`.
3. Metrika osy X: `skore`, Average. Metrika osy Y: `podil_pod_2`, Average.
4. Velikost bodů ponechte stejnou. Nemáme zde údaj o počtu žáků, kterým by bylo vhodné ji řídit.
5. Zapněte názvy zemí nebo jejich zobrazení po najetí a osy pojmenujte včetně jednotek.
6. Nadpis: `Průměrné skóre a podíl pod úrovní 2, přírodní vědy 2025`.

Pokud rozhraní nabídne bublinový graf s povinnou metrikou velikosti, zvolte základní bodový typ. [Google: bodové grafy](https://docs.cloud.google.com/data-studio/scatter-chart-reference)

Otázka: kde leží země s vyšším skóre a nižším podílem slabých výsledků? Očekávejte pravý dolní směr. Z tohoto grafu nevyvozujte účinek konkrétní školské politiky. Oba ukazatele navíc popisují stejné rozdělení výkonu, takže jejich souvislost není nezávislým důkazem příčiny.

## Závěr pro poradu

Vyberte jeden pohled a napište tři věty: co pozorujete, co z dostupných údajů nezjistíte a jakou konkrétní diagnostickou úlohu připravíte pro vlastní žáky. Pedagogický návrh označte jako návrh k ověření, ne jako prokázané řešení národního výsledku.
