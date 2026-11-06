# 4. Srovnání zemí a oblastí

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Pruhový graf, kontingenční tabulka a graf rozdílů vůči OECD.
</div>

Všechny tři pohledy čerpají ze zdroje `PISA25_Vysledky`. Vytvořte stránku `Srovnání zemí`. Na stránce ponechte poznámku „Výběr deseti zemí, patnáctiletí, PISA 2025; B-S-J-Z zvlášť jako region“.

## Pohled 2: srovnávací pruhový graf

1. Přidejte vodorovný pruhový graf.
2. Nastavte dimenzi `zeme`, metriku `skore` a agregaci Average.
3. Vytvořte filtr se dvěma podmínkami AND: `typ = Zeme`, `oblast = Přírodní vědy`.
4. Řazení nastavte podle `skore` sestupně. Počet pruhů nastavte nejméně na deset.
5. Zapněte hodnoty u pruhů a zvolte jednu barvu. ČR lze zvýraznit ručně nebo podmíněným barvením, pokud ho daný typ grafu nabízí.
6. V nastavení osy ponechte počátek na nule. Pro detailnější rozdíly použijte samostatnou tabulku nebo graf odchylek.
7. Nadpis změňte na `Přírodní vědy: bodové odhady ve vybraných zemích`.

Kontrola: deset pruhů, ČR 490, Estonsko 527 a Singapur 560. Vzájemné pořadí je pořadím bodových odhadů v tomto výběru, nikoli testem významnosti. [OECD: ČR](https://gpseducation.oecd.org/CountryProfile?primaryCountry=CZE&topic=PI&treshold=10), [Estonsko](https://gpseducation.oecd.org/CountryProfile?primaryCountry=EST&topic=PI&treshold=10), [Singapur](https://gpseducation.oecd.org/CountryProfile?primaryCountry=SGP&topic=PI).

Otázka do výuky: jak se změní dojem z rozdílu po oříznutí osy například od 450? Proč musí být taková změna jasně označena?

## Pohled 3: kontingenční tabulka s barevnou škálou

1. Přidejte **Kontingenční tabulku / Pivot table**.
2. Řádková dimenze: `zeme`. Sloupcová dimenze: `oblast`.
3. Metrika: `skore`, Average. Filtr: `typ = Zeme`.
4. Vypněte řádkové i sloupcové součty. Ani součet, ani průměr různých škál nechceme interpretovat jako celkový výkon.
5. V panelu Style zapněte heatmapové zobrazení metriky, pokud je dostupné, případně přidejte podmíněné formátování barevnou škálou.
6. Nechte zobrazit i číselné hodnoty. Barva pouze pomáhá orientaci.

Kontrola: deset řádků a tři sloupce oblastí. Pole pro matematiku v ČR má 477. Porovnávejte primárně země **uvnitř stejného sloupce**. Shodná bodová hodnota v různých oblastech neznamená stejnou obtížnost nebo totožnou úroveň zvládnutí.

Tento pohled dobře odhaluje, proč jeden celkový žebříček skrývá různé profily zemí. Pro nastavení řádkových a sloupcových dimenzí viz [Google: kontingenční tabulky](https://docs.cloud.google.com/data-studio/pivot-table-reference).

### Region B-S-J-Z

Pokud chcete zahrnout čínská data, zkopírujte tabulku a vytvořte filtr zahrnující `typ = Zeme` nebo `typ = Region`. Popisek musí znít `B-S-J-Z (Peking, Šanghaj, Ťiang-su, Če-ťiang)`, nikoli `Čína`. Region je v této tabulce pro srovnání bodových odhadů, ale nepatří do mapy zemí ani do souhrnu národních výsledků. Pro B-S-J-Z chybí v přiloženém souboru změna i podíly úrovní, proto je nezobrazujeme v příslušných grafech.

## Pohled 4: rozdíl proti OECD

Referenční údaj je uložen u každého řádku, takže nemusíme slučovat zdroje. Výpočet vzniká ve zdroji `PISA25_Vysledky`:

1. Otevřete editaci zdroje a zvolte **Přidat pole / Add a field**.
2. Pole pojmenujte `rozdil_oecd` a vložte vzorec:

```text
skore - oecd_skore
```

3. Uložte pole jako Number s agregací Average.
4. Zkopírujte pruhový graf přírodních věd a metriku změňte na `rozdil_oecd`.
5. Zachovejte filtr zemí a jedné oblasti. Nastavte viditelnou nulu a osu umožňující záporné hodnoty.
6. Nadpis: `Rozdíl vůči OECD v bodech, přírodní vědy 2025`.

Pro ČR vychází `490 − 482 = 8`. Výsledek označte „o 8 bodů nad publikovanou referencí OECD“, nikoli „o 8 % lepší“. Nula znamená shodný zaokrouhlený bodový odhad. [OECD: ČR a reference](https://gpseducation.oecd.org/CountryProfile?primaryCountry=CZE&topic=PI&treshold=10)

Návod na vytvoření pole vychází z [dokumentace vypočtených polí](https://docs.cloud.google.com/data-studio/about-calculated-fields).

## Samostatná práce

Zkopírujte srovnávací graf pro matematiku a čtení. U každého napište jednu přesnou větu s populací, cyklem a jednotkou. Potom vyberte větu, u které byste pro silnější závěr potřebovali standardní chyby nebo národní zprávu.
