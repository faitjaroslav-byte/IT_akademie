# 5. Mapa a interaktivní filtry

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Mapa vybraných zemí a ovládací prvky s ověřeným rozsahem působení.
</div>

## Pohled 5: mapa výsledků

Mapa pomáhá orientaci v prostoru. Pro přesné srovnání ponechte vedle ní pruhový graf: velká země na mapě získává větší vizuální váhu, přestože plocha nevypovídá o výsledku žáků.

1. Ve zdroji `PISA_Vysledky` nastavte u `iso3` typ **Geo → Country / Země**.
2. Na stránku `Srovnání zemí` vložte **Google Maps**, například vyplněnou mapu, pokud ji rozhraní nabízí. Alternativou je **Geo chart / Geografický graf**, ale ten nenabízí stejné interaktivní přibližování a posun mapy.
3. Jako geografickou dimenzi použijte `iso3`, jako barevnou metriku `skore`, Average.
4. Nastavte filtr AND: `typ = Zeme`, `cyklus = 2025` a `oblast = Přírodní vědy`.
5. Zobrazte svět. Zapněte legendu a zkontrolujte ČR, Singapur, Jižní Koreu i USA. U **Google Maps** otevřete **Styl → Ovládací prvky mapy / Map controls** a zapněte **Povolit posun a přiblížení**, **Zobrazit ovládání přiblížení (+/−)** a **Zobrazit celou obrazovku**. V režimu zobrazení pak vyzkoušejte přiblížení Česka i Singapuru a návrat na výchozí pohled. [Google: ovládání mapy](https://docs.cloud.google.com/data-studio/google-maps-reference)
6. Vedle mapy napište „Bílé/nevyplněné země nejsou v datovém výběru“. Chybějící země nemají nulový výsledek.

ISO kód reference OECD i regionu B-S-J-Z je záměrně prázdný; ani jedno není celá země. Údaje pro mapu a vlastnosti geografických polí popisuje [Google Maps reference](https://docs.cloud.google.com/data-studio/google-maps-reference).

Na celosvětové vyplněné mapě jsou některé země pro přesné kliknutí příliš malé. Mapa slouží k prostorové orientaci; pro vyhledání a výběr Česka nebo Singapuru použijte raději níže popsaný **filtr zemí** a pro čtení bodového výsledku pruhový graf. Pokud používáte **Geo chart**, jeho nastavení **Zoom area** omezuje výřez mapy, ale nenahrazuje posun a přibližování v Google Maps. [Google: Geo chart](https://docs.cloud.google.com/data-studio/geo-chart-reference)

### Když Geo chart vykreslí Slovensko na místě Česka

Při ověřování Geo chartu se může stát, že bublina `SVK` ukáže **475** bodů nad tvarem Česka a Slovensko se nevybarví. V přiloženém CSV jsou hodnoty správně: Česko (`CZE`) má v přírodních vědách 2025 **490**, Slovensko (`SVK`) **475**. V takovém případě neměňte původní data. V reportu otevřete **Zdroje → Spravovat přidané zdroje dat → PISA_Vysledky → Upravit**, zvolte **Přidat pole → Přidat vypočtené pole** a vytvořte `map_kod`:

```text
CASE
  WHEN iso3 = "CZE" THEN "CZ"
  WHEN iso3 = "SVK" THEN "SK"
  ELSE iso3
END
```

Uloženému poli nastavte typ **Geo → Země**. Jen v Geo chartu nahraďte geografickou dimenzi `iso3` novým `map_kod`; filtry a metriku `skore` ponechte beze změny. Ověřte obě sousední země: **CZ = 490**, **SK = 475**. Dvoupísmenné i třípísmenné kódy zemí jsou podporované. [Google: vypočtená pole](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields), [geografické kódy](https://docs.cloud.google.com/data-studio/geo-dimension-reference)

## Přepínání oblasti

Máte-li tři samostatné pruhové grafy, každý s pevnou oblastí, ponechte je beze změny. Rozbalovací ovladač `oblast` bude ovládat **jen mapu**. Pevný filtr oblasti u mapy odstraňte **až po nastavení ovladače**. Mapa bez pevného filtru i bez vybrané oblasti zprůměruje tři různé výsledky: pro ČR v roce 2025 zobrazí `AVG skore = (490 + 468 + 477) / 3 = 478,33`, po zaokrouhlení **478**. To není skóre žádné oblasti.

1. Zvolte **Přidat ovládací prvek / Add a control → Rozbalovací seznam / Drop-down list**.
2. Zdroj nastavte na `PISA_Vysledky` a ovládací pole na `oblast`.
3. Zapněte jediný výběr a jako výchozí vyberte Přírodní vědy. Vypněte možnost vybrat vše, pokud ji rozhraní nabízí.
4. Označte **jen mapu a její ovladač oblasti** a seskupte je pomocí **Uspořádat / Arrange → Seskupit / Group**. Tři pruhové grafy ani kontingenční tabulku do této skupiny nepřidávejte.
5. Teprve nyní odstraňte pevné omezení `oblast = Přírodní vědy` **u mapy**. U pruhových grafů jejich pevné filtry ponechte. Na mapě zachovejte `typ = Zeme` **i** `cyklus = 2025`.
6. Ověřte, že mapa při volbě Přírodní vědy ukazuje v ČR **490**, při Čtení **468** a při Matematice **477**. Tři pruhové grafy zůstávají na svých oblastech. Hodnota **478** na mapě znamená, že ji ovladač nefiltruje nebo není vybrána právě jedna oblast.

Rozsah filtru vychází z jeho zdroje dat a seskupení komponent. Po návratu do režimu zobrazení ověřte skutečné chování. [Google: přidání a rozsah ovladačů](https://docs.cloud.google.com/data-studio/add-edit-controls)

## Filtr zemí

Přidejte druhý rozbalovací seznam pro pole `zeme` a ponechte ho **mimo skupinu mapy** na úrovni stránky, aby výběr země působil na mapu i na všechny tři pruhové grafy. Umožněte vícenásobný výběr. Vyhledejte v něm nejprve Česko a Singapur bez klikání na malé plochy mapy; poté porovnejte například pouze ČR a Slovensko. Při resetu filtrů se musí znovu zobrazit deset zemí. Pokud chcete filtrovat země pouze na mapě, přidejte tento ovladač naopak do skupiny mapy.

U prvních tří karet ČR na jiné stránce ponechte pevné filtry. Nezměňte ovladače na úroveň celého reportu, pokud nechcete jejich účinek přenášet i tam. Zdroje `Vysledky` a `Rozlozeni` mají samostatné ovladače; shodný název pole sám nezaručuje filtrování přes oba zdroje.

## Zkouška filtrů

| Akce | Očekávané chování |
| --- | --- |
| Vybrat matematiku v ovladači mapy | ČR na mapě ukazuje 477; tři pruhové grafy se nemění. |
| Vybrat pouze ČR v ovladači země | Na mapě zůstane ČR a v každém pruhovém grafu jeden pruh; reference v `oecd_skore` se nezmění. |
| Vrátit všechny země | V každém pruhovém grafu je deset zemí, nikoli region B-S-J-Z či reference OECD. |
| Změnit oblast na mapě | Kontingenční tabulka mimo skupinu stále ukazuje tři oblasti. |
| Vymazat výběr oblasti | Pokud rozhraní dovolí sloučit oblasti, opravte nastavení; průměr škál neinterpretujte. |

Úkol: požádejte kolegu, aby bez vysvětlování našel české skóre ve čtení a vrátil report do výchozího stavu. Sledujte, zda mu pomohou popisky filtrů.
