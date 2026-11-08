# Rozšíření: nejistota a mikrodata

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut navazující práce<br>
<strong>Výstup:</strong> Tabulka skóre se standardními chybami a věcný komentář k rozdílům mezi zeměmi a školními skupinami.
</div>

V základní části kurzu pracujete s publikovanými zaokrouhlenými hodnotami OECD a ČŠI. Nyní použijete **samostatné agregace z veřejného žákovského souboru PISA 2025**. Nejde o další řádky ke spojení s původními tabulkami: stejné výsledky byste tím zdvojili. Postup výpočtu a původ polí jsou v [datovém slovníku](data/README.md#rozsireni-z-verejneho-zakovskeho-souboru-oecd).

## Připravte dva nové listy

1. Stáhněte [výsledky zemí](data/pisa2025-mikrodata-zeme.csv) a [české druhy škol](data/pisa2025-mikrodata-cr-druhy-skol.csv).
2. Ve své tabulce `PISA 2025 – kurz` importujte první CSV jako **nový list** `Odhady_zeme` a druhý jako `Odhady_skoly`. Použijte čárku jako oddělovač.
3. Ověřte 33 datových řádků v `Odhady_zeme` a 15 v `Odhady_skoly`. Číselná pole `skore`, `se_skore`, `n_zaku` a `vazena_populace` nesmějí být text.
4. V `Odhady_zeme` zkontrolujte řádek `CZE` + `Přírodní vědy`: skóre **490,278**, standardní chyba **2,586**. Kód `QCI` označuje B-S-J-Z, nikoli celou Čínu.
5. V `Odhady_skoly` zkontrolujte základní školu v přírodních vědách: skóre **459,016**, standardní chyba **2,955**, nevážený počet **3 402**. `vazena_populace` není počet otestovaných žáků.

CSV ponechte jako dva samostatné zdroje. Školní skupiny jsou jen pro ČR; zemský soubor nemá sloupec pro druh školy. Názvy a význam jednotlivých českých kódů `PROGN` můžete zkontrolovat v [detailní tabulce programů](data/pisa2025-mikrodata-cr-programy.csv).

## Pohled 10: srovnání s nejistotou

1. V reportu přidejte zdroj Google Sheets pro list `Odhady_zeme` a nazvěte jej `PISA25_Odhady_zeme`.
2. U `skore` a `se_skore` nastavte typ **Number** a agregaci **Average**. Totéž platí pro `n_zaku`; jeho součet přes země nepoužívejte jako odhad populace.
3. Vytvořte stránku `Odhady a nejistota`. Vložte tabulku s názvem `Přírodní vědy: skóre a nejistota podle země, PISA 2025`, dimenzí `zeme` a metrikami `skore`, `se_skore`, `n_zaku`. Přidejte pevný filtr `oblast = Přírodní vědy`.
4. Vypněte souhrnný řádek. Tabulka musí mít jeden řádek na zemi nebo systém. Pro srovnání **zemí** přidejte filtr `typ = Zeme`; B-S-J-Z pak zobrazte ve zvláštní kopii tabulky s názvem `Přírodní vědy: region B-S-J-Z, PISA 2025`.
5. Zkopírujte tabulku pro matematiku nebo čtení a kopii nadepište `Matematika: skóre a nejistota podle země, PISA 2025` nebo `Čtení: skóre a nejistota podle země, PISA 2025`. V každé kopii zachovejte právě jednu oblast; průměr přes různé škály nemá význam.

### Orientační interval

V editaci zdroje zvolte **Add a field / Přidat pole**. Pole `dolni_95` má vzorec:

```text
skore - 1.96 * se_skore
```

Pole `horni_95` má vzorec:

```text
skore + 1.96 * se_skore
```

Do tabulky přidejte oba sloupce s agregací Average. Výpočet probíhá po řádcích a dává **orientační 95% interval** za předpokladu přibližně normálního rozdělení odhadu. Pro ČR v přírodních vědách vyjde přibližně **485,2 až 495,3 bodu**. Interval není rozsahem skóre jednotlivých žáků. Pouhé překrytí či nepřekrytí dvou intervalů nenahrazuje správný test rozdílu. [Google: vypočtená pole](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields), [OECD: nejistota v PISA](https://www.oecd.org/en/about/programmes/pisa/how-to-prepare-and-analyse-the-pisa-database.html).

!!! warning "USA"
    Výsledek USA zobrazujte s poznámkou, že OECD upozorňuje na nesplněné výběrové standardy. Přítomnost standardní chyby toto omezení neodstraňuje. [OECD: PISA 2025, reader's guide](https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/reader-s-guide_0364240f.html)

## Pohled 11: české školní skupiny

1. Připojte list `Odhady_skoly` jako zdroj `PISA25_Odhady_skoly`.
2. Na téže stránce vytvořte druhou tabulku s názvem `Čtení: skóre a nejistota podle druhu školy, ČR 2025`, dimenzí `druh_skoly`, metrikami `skore`, `se_skore`, `n_zaku` a filtrem `oblast = Čtení`.
3. Ověřte pět řádků. Například SOU bez maturity má z veřejného souboru **391,270 bodu** a standardní chybu přibližně **5,5 bodu**.
4. Do popisku napište „Patnáctiletí v českých školních programech, PISA 2025 Public Use File; odhady s výběrovou nejistotou.“
5. Vedle tabulky můžete přidat pruhový graf s jednou oblastí, například `Čtení: skóre podle druhu školy, ČR 2025 (mikrodata)`. Standardní chybu ponechte v tabulce; samotné pruhy rozdíly statisticky netestují.

Pozor na vymezení: skupina `Víceleté gymnázium / konzervatoř` je vytvořena z kódů `203002` až `203005`, z nichž některé v codebooku zahrnují konzervatoř. Není automaticky totožná s kategorií ve všech národních publikacích. V grafu ČŠI je pro SOU ve čtení **392**; přepočet z veřejného souboru dává **391,270**. Nezaměňujte verze ani z rozdílu nevyvozujte chybu měření. [ČŠI: národní zpráva, obrázek 2.3.3](https://csi.gov.cz/CSICR/media/Prilohy/2024_p%C5%99%C3%ADlohy/Dokumenty/PISA-2025_final.pdf).

## Úkol pro učitele

Napište dvě věty ke srovnání ČR a Německa v přírodních vědách: první popisuje bodové odhady, druhá vysvětluje, proč samotné pořadí nestačí k závěru o průkazném rozdílu. Uveďte cyklus, populaci, oblast a zdroj. Poté vyberte jednu českou školní skupinu a vysvětlete, proč její průměr nepředpovídá výsledek konkrétního žáka ani účinek daného typu školy.
