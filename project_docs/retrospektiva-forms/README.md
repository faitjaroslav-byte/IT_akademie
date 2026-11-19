# Ukázkový formulář pro flow Vyhodnocení retrospektivy

Dva soukromé Google Apps Script soubory vytvoří formulář s pěti otázkami z [kapitoly 5](../../docs/workspace-studio/05-retrospektiva.md) a pak do něj odešlou **15 fiktivních odpovědí**. Opakující se slabina v datech se týká Zotero; některé odpovědi jsou naopak jisté. Tato data slouží k demonstraci skupinové analýzy ve Workspace Studio, nikoli k hodnocení skutečných studentů.

1. Otevři [script.google.com](https://script.google.com/) a vytvoř nový projekt.
2. Vlož obsah `01-vytvorit-formular.gs` a `02-vytvorit-mock-odpovedi.gs` jako dva soubory **v témže projektu**.
3. Spusť funkci `vytvoritFormularRetrospektivy`. Při prvním spuštění povol přístup k Forms, Sheets a Script Properties. V protokolu spuštění najdeš odkazy na formulář a propojenou tabulku odpovědí.
4. Spusť funkci `vytvoritMockOdpovediRetrospektivy`. Ve formuláři a v tabulce se objeví 15 odpovědí. Pokud řádky v Sheets nejsou vidět hned, chvíli počkej a obnov tabulku.
5. Ve Workspace Studio nastav `Get sheet contents` na vytvořenou tabulku. Do `Ask Gemini` předej sloupce s pěti odpověďmi podle kapitoly. Flow spusť ručně pomocí `Start on demand`.

První funkci spouštěj jen jednou v jednom Apps Script projektu; ID formuláře a otázek se ukládají do **Script Properties**. Každé další spuštění druhé funkce přidá dalších 15 odpovědí. Skript nesbírá e-mailové adresy.

Programově odeslané odpovědi se uloží do Forms, ale nespouštějí Apps Script trigger `onFormSubmit`. Pro ručně spouštěné flow z kapitoly to nevadí.
