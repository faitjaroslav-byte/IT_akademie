# 5. Mapa a interaktivní filtry

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Mapa vybraných zemí a ovládací prvky s ověřeným rozsahem působení.
</div>

## Pohled 5: mapa výsledků

Mapa pomáhá orientaci v prostoru. Pro přesné srovnání ponechte vedle ní pruhový graf: velká země na mapě získává větší vizuální váhu, přestože plocha nevypovídá o výsledku žáků.

1. Ve zdroji `PISA25_Vysledky` nastavte u `iso3` typ **Geo → Country / Země**.
2. Na stránku `Srovnání zemí` vložte **Google Maps**, například vyplněnou mapu, pokud ji rozhraní nabízí. Alternativou je **Geo chart / Geografický graf**.
3. Jako geografickou dimenzi použijte `iso3`, jako barevnou metriku `skore`, Average.
4. Nastavte filtr AND: `typ = Zeme` a `oblast = Přírodní vědy`.
5. Zobrazte svět. Zapněte legendu a zkontrolujte ČR, Singapur, Jižní Koreu i USA.
6. Vedle mapy napište „Bílé/nevyplněné země nejsou v datovém výběru“. Chybějící země nemají nulový výsledek.

ISO kód reference OECD i regionu B-S-J-Z je záměrně prázdný; ani jedno není celá země. Údaje pro mapu a vlastnosti geografických polí popisuje [Google Maps reference](https://docs.cloud.google.com/data-studio/google-maps-reference).

## Přepínání oblasti

Pevný filtr oblasti se musí před přidáním přepínače odstranit, jinak se s ním výběr dostane do konfliktu.

1. U mapy a hlavního pruhového grafu odstraňte pevné omezení `oblast = Přírodní vědy`. Ponechte `typ = Zeme`.
2. Zvolte **Přidat ovládací prvek / Add a control → Rozbalovací seznam / Drop-down list**.
3. Zdroj nastavte na `PISA25_Vysledky` a ovládací pole na `oblast`.
4. Zapněte jediný výběr a jako výchozí vyberte Přírodní vědy. Vypněte možnost vybrat vše, pokud ji rozhraní nabízí.
5. Označte ovladač, mapu a hlavní pruhový graf a seskupte je pomocí **Uspořádat / Arrange → Seskupit / Group**.
6. Kontingenční tabulku nechte mimo skupinu: jejím účelem je zobrazit všechny tři oblasti současně.

Rozsah filtru vychází z jeho zdroje dat a seskupení komponent. Po návratu do režimu zobrazení ověřte skutečné chování. [Google: přidání a rozsah ovladačů](https://docs.cloud.google.com/data-studio/add-edit-controls)

## Filtr zemí

Přidejte druhý rozbalovací seznam pro pole `zeme` a zařaďte ho do stejné skupiny. Umožněte vícenásobný výběr. Porovnejte například pouze ČR a Slovensko. Při resetu filtrů se musí znovu zobrazit deset zemí.

U prvních tří karet ČR na jiné stránce ponechte pevné filtry. Nezměňte ovladače na úroveň celého reportu, pokud nechcete jejich účinek přenášet i tam. Zdroje `Vysledky` a `Rozlozeni` mají samostatné ovladače; shodný název pole sám nezaručuje filtrování přes oba zdroje.

## Zkouška filtrů

| Akce | Očekávané chování |
| --- | --- |
| Vybrat matematiku | ČR na mapě i pruhu ukazuje 477. |
| Vybrat pouze ČR | Zůstane jeden pruh; reference v `oecd_skore` se nezmění. |
| Vrátit všechny země | Deset pruhů, nikoli region B-S-J-Z či reference OECD. |
| Změnit oblast | Kontingenční tabulka mimo skupinu stále ukazuje tři oblasti. |
| Vymazat výběr oblasti | Pokud rozhraní dovolí sloučit oblasti, opravte nastavení; průměr škál neinterpretujte. |

Úkol: požádejte kolegu, aby bez vysvětlování našel české skóre ve čtení a vrátil report do výchozího stavu. Sledujte, zda mu pomohou popisky filtrů.
