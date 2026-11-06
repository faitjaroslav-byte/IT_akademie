# 3. První report krok za krokem

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Report se zdrojem Google Sheets, kontrolní tabulkou a třemi kartami ČR.
</div>

## Připojení zdroje

1. Otevřete [Looker Studio](https://lookerstudio.google.com/) a přihlaste se školním účtem.
2. Zvolte **Vytvořit / Create → Zdroj dat / Data source**.
3. Vyberte konektor **Google Sheets** a povolte požadovaný přístup ke svým tabulkám.
4. Vyberte tabulku `PISA 2025 – kurz` a list `Vysledky`.
5. Nechte zapnuté použití prvního řádku jako názvů polí a klikněte na **Připojit / Connect**.
6. Zdroj pojmenujte `PISA25_Vysledky`.
7. Zkontrolujte typy polí podle [přípravy dat](02-priprava-dat.md). `cyklus` je číslo, nikoli datum příjmu odpovědi.
8. U `skore`, `oecd_skore` a `zmena_2022_2025` změňte výchozí agregaci na **Průměr / Average**. U kategorií a roku použijte bez agregace, pokud je tato volba dostupná.
9. Klikněte na **Vytvořit přehled / Create report** a potvrďte vložení zdroje do reportu.
10. Report pojmenujte `PISA 2025 – Česko a svět`.

Některé názvy položek závisí na jazyku a verzi rozhraní. Postup připojení jednoho listu odpovídá [dokumentaci konektoru Google Sheets](https://docs.cloud.google.com/data-studio/connect-to-google-sheets).

## Kontrolní tabulka

1. V režimu úprav zvolte **Přidat graf / Add a chart → Tabulka / Table**.
2. V panelu nastavení nastavte dimenze `zeme`, `oblast` a metriku `skore` s agregací **Average**.
3. V části **Filtr → Přidat filtr → Vytvořit filtr** zadejte zahrnutí `iso3` rovná se `CZE`.
4. Ověřte tři řádky: Matematika 477, Čtení 468, Přírodní vědy 490. [Zdroj OECD](https://gpseducation.oecd.org/CountryProfile?primaryCountry=CZE&topic=PI&treshold=10)

Průměr zde pouze zachovává hodnotu jednoho odpovídajícího řádku. Správnou granularitu musíte hlídat i při použití Average. Pokud vidíte jedinou hodnotu místo tří, doplňte dimenzi `oblast`.

## Pohled 1: karty ukazatelů

1. První stránku pojmenujte `Česko v kontextu`.
2. Přidejte graf typu **Karta skóre / Scorecard**.
3. Nastavte metriku `skore`, agregaci Average a filtr `iso3 = CZE`.
4. Do stejného filtru přidejte další podmínku **AND**: `oblast = Matematika`.
5. Kartu nadepište `ČR – matematika, PISA 2025` a zobrazte celé číslo.
6. Kartu dvakrát zkopírujte. U kopií změňte podmínku oblasti a nadpis na Čtení a Přírodní vědy.
7. Pod karty vložte text: „Patnáctiletí napříč typy škol. Zaokrouhlené bodové odhady.“

Výsledkem musí být 477, 468 a 490. Samotný filtr země nestačí: karta bez filtru oblasti by ukázala průměr tří různých škál. Taková hodnota nemá zamýšlený význam.

## Druhý datový zdroj

1. V reportu otevřete **Zdroje / Resource → Spravovat přidané zdroje dat / Manage added data sources**.
2. Přidejte konektor Google Sheets pro list `Rozlozeni` a pojmenujte ho `PISA25_Rozlozeni`.
3. Pro všechny tři podíly nastavte typ Procenta a agregaci Average, pro skóre Number a Average. Grafy budou vždy filtrované na jedinou oblast.
4. Vraťte se do reportu. Zdroj bude potřeba v [kapitole 6](06-zmeny-a-rozlozeni.md).

## Uložení a první zkouška

Přepněte do režimu **Zobrazit / View**. Report se průběžně ukládá. Ověřte, že jsou popisky čitelné a že každá karta má uvedenou oblast. Úkol pro dvojici: jeden účastník omylem odebere filtr oblasti, druhý má chybu odhalit podle kontrolní tabulky.
