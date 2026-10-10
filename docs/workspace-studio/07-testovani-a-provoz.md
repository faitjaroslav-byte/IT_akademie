# 7. Testování a provoz

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 45-60 minut<br>
<strong>Výstup kapitoly:</strong> Dokážeš bezpečně otestovat flow, najít chybu v historii běhů a rozhodnout, zda je flow připravené k běžnému používání.
</div>

## Motivace

Automatizace je užitečná jen tehdy, když jí rozumíme. Testování není poslední formalita, ale běžná součást návrhu. U školních dat to platí dvojnásob.

## Test run není jen simulace

V prostředí Workspace Studio může `Test run` opravdu spustit akční kroky. To znamená, že může:

- poslat e-mail,
- odeslat zprávu do Chatu,
- vytvořit nebo změnit objekt,
- upravit data.

Proto testuj na bezpečných datech a s bezpečnými příjemci.

## Bezpečný testovací postup

1. Začni s testovacími daty.
2. Posílej výstup jen sobě.
3. Použij zřetelný předmět, například `TEST - souhrn e-mailu`.
4. Zkontroluj historii běhu v Activity.
5. Teprve potom uprav příjemce nebo zapni pravidelné spouštění.

## Activity

Historii běhů najdeš v:

```text
Workspace Studio → Activity
```

U jednotlivých běhů lze ověřit:

- který krok proběhl,
- který krok byl přeskočen,
- jaký byl výsledek některých AI kroků,
- kde vznikla chyba.

## Kontrolní seznam před zapnutím

| Kontrola | Otázka |
| --- | --- |
| Název | Poznám podle názvu, k čemu flow slouží? |
| Starter | Spouští se flow ve správný okamžik? |
| Data | Pracuje flow se správnými proměnnými? |
| Prompt | Obsahuje jasná kritéria a omezení? |
| Akce | Posílá nebo mění data jen tam, kde má? |
| Test | Vyzkoušel/a jsem běžný případ i okrajový případ? |
| Activity | Umím najít poslední běh a přečíst jeho výsledek? |

## Typické chyby

| Chyba | Projev | Řešení |
| --- | --- | --- |
| Špatná proměnná | Gemini zpracuje prázdný nebo nesprávný text. | Zkontroluj vstupy kroku. |
| Příliš obecný prompt | Výstup je dlouhý, neurčitý nebo domýšlí informace. | Přidej kritéria, formát a omezení. |
| Nevhodný starter | Flow se spouští příliš často. | Změň trigger nebo přidej rozhodovací krok. |
| Akce v testu posílá zprávy ostatním | Test omylem doručí výstup dalším lidem. | Nejdřív posílej jen sobě. |
| Příliš mnoho štítků | Inbox je méně přehledný než předtím. | Slouč nebo odstraň málo užitečné štítky. |

## Studio není Make

Workspace Studio je silné v modelu:

```text
Spusť → pochop obsah → rozhodni → proveď Workspace akci
```

Je slabší v obecných transformacích dat, například:

- parsování datumu z volného textu,
- převody datových typů,
- formátování čísel,
- složité funkce typu `parseDate()` nebo `formatNumber()`.

Při návrhu flow proto vybírej scénáře, ve kterých data už přicházejí ve formátu, který cílový krok umí přímo použít.

## Kdy flow vypnout

Flow vypni nebo pozastav, pokud:

- posílá příliš mnoho výstupů,
- často pracuje s nesprávnými daty,
- dělá akce, které musíš pravidelně opravovat,
- změnil se školní proces, ze kterého flow vycházelo,
- už neumíš vysvětlit, proč flow existuje.

Dobrá automatizace má stále jasný účel. Pokud účel zmizí, flow se má změnit nebo skončit.

## Praktický úkol

Vyber jedno flow z předchozích kapitol a proveď kontrolu:

| Kontrola | Splněno |
| --- | --- |
| Testovací data jsou bezpečná. |  |
| Výstup jde jen učiteli. |  |
| Prompt zakazuje domýšlení. |  |
| Activity obsahuje úspěšný běh. |  |
| Vím, jak flow vypnout. |  |

## Shrnutí

Testování není známka nedůvěry k nástroji. Je to způsob, jak si udržet kontrolu nad procesem. Workspace Studio má pomáhat, ne se stát další neviditelnou vrstvou, kterou nikdo nespravuje.
