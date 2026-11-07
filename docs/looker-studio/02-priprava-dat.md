# 2. Příprava dat

<div class="lesson-meta">
<strong>Čas:</strong> 45 minut<br>
<strong>Výstup:</strong> Tři čisté listy v Google Sheets pro pohledy na rok 2025 i časové řady.
</div>

## Tři datové tabulky

Stáhněte [výsledky zemí](data/pisa-vysledky.csv), [rozložení ve třech oblastech](data/pisa-rozlozeni.csv) a [české druhy škol](data/pisa-cesko-druhy-skol.csv). Každou tabulku importujete **jen jednou**. Z týchž tří listů pak vytvoříte základní pohledy na rok 2025 i grafy vývoje v letech 2015, 2018, 2022 a 2025. Nejde o individuální žákovská data ani o úplnou světovou databázi.

`Vysledky` a `Rozlozeni` mají po **141 datových řádcích**. V každém je deset zemí ve čtyřech cyklech, region B-S-J-Z v letech 2018 a 2025, stálá reference OECD ve čtyřech cyklech a běžný průměr OECD pouze pro rok 2025. Klíčem řádku je **entita × cyklus × oblast × populace**. `Rozlozeni` obsahuje podíly pod úrovní 2, na úrovních 2–4 a na úrovni 5 nebo výše. `Druhy_skol_CR` má **60 datových řádků**: pět českých druhů škol × tři oblasti × čtyři cykly. Její populace zahrnuje patnáctileté žáky daného druhu školy, nikoli všechny středoškoláky.

## Import do Google Sheets krok za krokem

1. Na Disku vytvořte novou Tabulku Google s názvem `PISA 2015–2025 – kurz`. **Ještě před importem** otevřete **Soubor → Nastavení → Obecné**. V rozbalovacím poli **Jazyk** (země tabulky; někdy označené jako národní prostředí) změňte **Česko** na **Spojené státy** a klikněte na **Uložit nastavení**. Položku **Jazyk zobrazení: Čeština** neměňte. CSV používají desetinnou tečku; při českém prostředí se například `2.09` ve sloupci `se_skore` může omylem načíst jako datum.
2. Otevřete **Soubor → Importovat → Nahrát** a vyberte `pisa-vysledky.csv`. Importujte jej jako nový list, oddělovač nastavte na **čárku** a list přejmenujte na `Vysledky`.
3. Stejně importujte `pisa-rozlozeni.csv` do listu `Rozlozeni` a `pisa-cesko-druhy-skol.csv` do listu `Druhy_skol_CR`.
4. České popisky zůstanou zachovány. Po importu ověřte, že `se_skore` obsahuje čísla (například estonské přírodní vědy 2015: `2.09`) a podíly jsou číselné zlomky (například české přírodní vědy 2025: `0.213`), nikoli datum či text.
5. Ukotvěte první řádek a zapněte filtr. Nepřidávejte nad hlavičku další nadpis, součtový řádek ani sloučené buňky.
6. Zkontrolujte `cyklus` jako celé číslo, `skore` jako číslo, podíly jako procenta a `datum_cyklu` jako datum. U posledního pole případně zvolte **Formát → Číslo → Datum**; v Data Studiu nastavte typ **Date**.

`datum_cyklu` je technický zástupný den **1. ledna** daného roku pro správné rozestupy na časové ose. Nejde o skutečný den testování. Mezi cykly 2018 a 2022 jsou čtyři roky.

Pokud jste už CSV importovali s českým prostředím a některé hodnoty se změnily na datum, **nestačí pouze přepnout formát buňky na Číslo**: datum už má jinou podkladovou hodnotu. V poli **Jazyk** nastavte nejprve **Spojené státy** a postižený CSV importujte znovu jako nový list; chybný list pak nahraďte. Pokud jste jej již připojili do Data Studia, ověřte po výměně listu také typy polí a aktualizujte zdroj. [Google: nastavení národního prostředí tabulky](https://support.google.com/docs/answer/58515)

## Důležitá pole

| Pole | Význam | Typ v Data Studiu |
| --- | --- | --- |
| `zeme`, `iso3`, `typ` | Popisek, kód země a druh entity (`Zeme`, `Region`, `Reference`, `Reference_stala`) | Text; `iso3` pro mapu jako Country |
| `cyklus`, `datum_cyklu` | Rok šetření a technické datum pro časovou osu | Číslo bez agregace; Date |
| `oblast` | Matematika, Čtení, Přírodní vědy | Text |
| `skore`, `se_skore` | Bodový odhad a jeho standardní chyba; druhé pole je jen ve `Vysledky` | Číslo, Average |
| `oecd_skore` | Běžný průměr OECD pro stejnou oblast; vyplněn jen pro rok 2025 | Číslo, Average |
| `zmena_2022_2025` | Publikovaná změna v bodech, vyplněná jen pro rok 2025, nikoli dopočet ze zaokrouhlených skóre | Číslo, Average |
| `podil_pod_2`, `podil_2_4`, `podil_5_6` | Podíly žáků na úrovních, uložené jako zlomky | Procenta, Average |
| `druh_skoly` | České členění škol, pouze v `Druhy_skol_CR` | Text |
| `zdroj_url` | Dohledatelný původ výsledku | URL nebo text |

Stálá referenční řada `Průměr OECD (stálých 35)` má `typ = Reference_stala`. **Není totožná** s běžným `Průměr OECD` pro rok 2025 (`typ = Reference`). V grafech vývoje použijte stálou řadu; v základním pohledu na rok 2025 běžnou referenci. Pole `oecd_skore` pro starší roky zůstává prázdné záměrně. Úplná metodika je v [datovém slovníku](data/README.md).

## Kontrola před připojením

Listy `Vysledky` a `Rozlozeni` mají každý **142 řádků včetně hlavičky**; `Druhy_skol_CR` má **61 řádků**. Při filtru `zeme = Česko`, `cyklus = 2025` jsou v každém z prvních dvou listů tři řádky, v českém školním listu patnáct.

Česká skóre v matematice pro cykly 2015, 2018, 2022 a 2025 jsou **492, 499, 487, 477**. V roce 2025 činí podíl pod úrovní 2 v matematice **29,0 %**, ve čtení **27,0 %** a v přírodních vědách **21,3 %**. Poslední podíl je v CSV zapsán jako `0.213`; číslo `21.3` formátované jako procento by zobrazilo 2130 %. Víceleté gymnázium má v matematice v uvedených cyklech **594, 596, 591, 586** bodů.

## Pravidlo pro grafy

V kapitolách 3–7 má každý graf označený **PISA 2025** pevný filtr `cyklus = 2025`. Nezrušte jej při kopírování grafu ani při přidání ovladače oblasti nebo země. Grafy trendu naopak používají všechna čtyři měření ze **stejných tří zdrojů**. Nikdy nesčítejte ani neprůměrujte skóre přes různé roky, země či oblasti. Chybějící rok B-S-J-Z není nula.

Úkol: vysvětlete kolegovi, proč by karta ČR bez filtru `cyklus` mohla vypadat věrohodně, přestože průměruje čtyři různá šetření.
