# PROJECT STANDARD

**Informatika EL2 - práce s daty**

*Verze 1.0 - aktuální provedení projektu, autorská pravidla a pracovní standard pro tuto učebnici*

| Hlavní záměr | Vytvořit moderní webovou učebnici informatiky pro žáky 2. ročníku střední odborné školy s ekonomickým zaměřením. Učebnice má být publikovaná v MkDocs Material na Cloudflare Pages a obsahově pokrývat požadavky ŠVP pro 2. ročník. |
| --- | --- |

| Charakter projektu | Nejde o akademickou skriptařinu ani o technickou dokumentaci. Výsledkem má být přehledná praktická učebnice, která žáka vede od získání a posouzení informací přes jejich zpracování až k tabulkovým a databázovým výstupům použitelným v ekonomické praxi. |
| --- | --- |

## 1. Účel a rozsah projektu

Cílem je vytvořit profesionálně působící online učebnici pro žáky 2. ročníku střední odborné školy s ekonomickým zaměřením. Učebnice má pokrýt 76 vyučovacích hodin informatiky.

Učebnice má vysvětlovat:

- jak Internet funguje jako informační prostředí,
- jak vybírat vhodné informační zdroje,
- jak informace vyhledávat, třídit, ověřovat a interpretovat,
- jak zpracovat informace v profesionálním textovém dokumentu,
- jak používat hromadnou korespondenci, formuláře a jednoduchá makra,
- jak využít tabulkový procesor pro práci s daty,
- jak vytvořit kontingenční tabulku a graf,
- jak navrhnout jednoduchou databázi,
- jak v databázi vyhledávat, filtrovat, tvořit dotazy a sestavy,
- jak propojit jednotlivé dovednosti v praktickém ekonomickém úkolu.

| Klíčový požadavek | Učebnice má být praktická, srozumitelná a přiměřená žákům 2. ročníku. Nemá působit jako generický návod k aplikaci ani jako slovník pojmů. |
| --- | --- |

## 2. Závazné zdrojové materiály

Obsah učebnice stojí na těchto podkladech:

| Zdroj | Role v projektu |
| --- | --- |
| `resources/EL_osnovy_2024.pdf` | Závazný rámec pro výstupy a učivo. Pro tuto učebnici se používají pouze strany 114-115 PDF. |
| `project-docs/PROJECT_STANDARD.md` | Interní autorský standard pro strukturu, tón a publikační pravidla. |

| Důležitý princip | ŠVP neurčuje přesné znění kapitol. Určuje požadované výstupy a učivo, které je potřeba převést do srozumitelné a praktické učebnice. |
| --- | --- |

## 3. Hlavní didaktický princip

Celá učebnice je postavená na tomto sledu:

1. najít a posoudit informace,
2. uspořádat je a správně interpretovat,
3. vytvořit srozumitelný textový výstup,
4. zpracovat data v tabulkovém procesoru,
5. vyhodnotit data pomocí souhrnů a grafů,
6. navrhnout jednoduchou databázi,
7. připravit dotazy, sestavy a závěrečný praktický výstup.

| Hlavní pravidlo | Nejdřív pochopit informační potřebu a data, až potom volit nástroj. Textový dokument, tabulka i databáze mají být odpovědí na konkrétní úkol. |
| --- | --- |

## 4. Charakter výsledné učebnice

Výsledná učebnice má působit jako soudobá školní publikace, ne jako interní firemní dokument nebo technická dokumentace.

Požadované vlastnosti:

- srozumitelná čeština,
- krátké a přehledné odstavce,
- jasné vysvětlení motivace tématu,
- ekonomické a školní příklady,
- postupné praktické úkoly,
- střídmé, ale účelné tabulky a diagramy,
- jednotná struktura napříč kapitolami,
- praktické úkoly propojující více dovedností.

Nepoužívat:

- přehnaně marketingový nebo "AI-like" tón,
- zbytečně abstraktní definice bez příkladu,
- příliš hutný text bez vizuálního členění,
- poznámky ke zdrojům v publikované části knihy,
- dlouhé návody k tlačítkům bez vysvětlení smyslu činnosti.

## 5. Aktuální struktura kurzu

Kniha je rozdělena do 10 hlavních kapitol:

1. Internet a informační zdroje
2. Práce s informacemi
3. Tabulkový procesor (MS Excel, Google Sheets)
4. Analýza dat
5. Textový procesor (MS Word, Google Docs) - opakování
6. Úvod do DB
7. Práce s databází
8. Hromadná korespondence, formuláře a makra
9. Kontingenční tabulky a grafy
10. Úkoly

| Poznámka ke struktuře | Kapitol je záměrně méně. Orientace v knize má být jednoduchá, ale uvnitř kapitol je možné pracovat s kratšími podkapitolami a praktickými úkoly. |
| --- | --- |

## 6. Lesson Authoring Guide

Při tvorbě nové kapitoly musí autor nebo AI nejdříve určit:

- jakou praktickou situaci kapitola řeší,
- jakou dovednost nebo pojem zavádí,
- na co kapitola navazuje,
- jaké výstupy ze ŠVP pokrývá,
- co má žák po přečtení umět vytvořit, vysvětlit nebo rozhodnout.

Kapitola má být psaná jako vedený výklad s praktickými příklady, ne jako encyklopedické heslo ani jako mechanický návod k programu.

### 6.1 Doporučený postup při tvorbě kapitoly

1. Projít relevantní požadavky ze ŠVP.
2. Ujasnit si praktický ekonomický nebo školní kontext.
3. Sepsat motivaci a výstup kapitoly.
4. Připravit výklad po menších logických blocích.
5. Doplnit tabulku, diagram, ukázková data nebo praktický úkol tam, kde opravdu pomůže.
6. Uzavřít kapitolu tahákem, checklistem a krátkým shrnutím.

### 6.2 Jazyk a styl

- Psát česky.
- Používat přirozený učebnicový tón.
- Upřednostňovat konkrétní formulace před frázemi.
- Vysvětlovat pojmy jednoduše, ale ne zjednodušeně.
- Volit příklady z ekonomické, administrativní a školní praxe.
- U moderních témat doplnit současný kontext, pokud je ŠVP formulováno obecně.

## 7. Šablona kapitoly

Aktuální standard kapitoly:

```markdown
# Kapitola X - Název

<div class="lesson-meta">
<strong>Doporučený čas:</strong> 6-8 vyučovacích hodin<br>
<strong>Výstup kapitoly:</strong> Jednou větou popiš, co má žák po kapitole umět.
</div>

## Motivace

Krátké vysvětlení, proč se téma učíme a k čemu je potřeba.

## Doporučený obsah

- bod 1
- bod 2
- bod 3

## Doporučené aktivity

- praktická aktivita 1
- praktická aktivita 2

## Návaznost na ŠVP

- výstup nebo učivo ze ŠVP
- výstup nebo učivo ze ŠVP
```

Při rozepisování plné kapitoly lze přidat:

- `## Co se naučíš`
- `## Výklad`
- `## Ukázka`
- `## Praktický úkol`
- `## Tahák`
- `## Co už umím`
- `## Shrnutí`

## 8. Vizuální a typografický standard

Vizuální provedení je záměrně střídmé a školní.

Aktuální principy:

- theme `Material for MkDocs`,
- primární barva `blue`,
- akcent `teal`,
- přepínač `light / dark mode`,
- jednotné boxy, tabulky a odsazení,
- dobrá čitelnost na notebooku, tabletu i mobilu.

Sdílené CSS je v:

- `docs/assets/stylesheets/extra.css`

Používané prvky:

| Prvek | Účel |
| --- | --- |
| `.lesson-meta` | horní informační box kapitoly |
| markdown tabulky | přehledy, srovnání a shrnutí |
| Mermaid diagramy | jednoduchá schémata procesů, toků nebo databázových vztahů |

| Vizuální princip | Text musí být dobře čitelný, vzdušný a pravidelně členěný. Tabulky a diagramy mají výklad zpřehlednit, ne ho nahrazovat. |
| --- | --- |

## 9. Diagramy, tabulky a další výstupy

Pro tuto knihu platí:

- jednoduché procesy lze kreslit v Mermaid,
- databázové vztahy lze kreslit v Mermaid ER diagramem,
- tabulky používat pro srovnání, kontrolní seznamy a shrnutí,
- ukázková data držet malá a čitelná,
- obrázky používat jen tam, kde opravdu pomáhají.

| Doporučení | Pokud lze výstup rozumně vytvořit v Markdownu nebo Mermaid, má to přednost před rastrovým obrázkem. |
| --- | --- |

## 10. Standard praktických úkolů

Praktické úkoly mají propojit hlavní oblasti učiva:

1. informační zdroje,
2. validitu informací,
3. textový dokument,
4. tabulkovou analýzu,
5. kontingenční tabulku nebo graf,
6. jednoduchou databázi,
7. dotaz,
8. sestavu nebo tiskový výstup,
9. prezentaci výsledků.

Úkoly mají být přiměřené žákům 2. ročníku. Nemají suplovat velkou ročníkovou práci, ale mají ukázat, že žák dokáže použít více nástrojů v jedné praktické situaci.

## 11. Zásady pro zdroje a interní poznámky

Pro tuto knihu platí:

- zdrojové a metodické poznámky evidovat pouze v `project-docs/` nebo `README.md`,
- v publikované učebnici neuvádět interní redakční komentáře,
- zdroje používat jako podklad, ne jako text k přepisu,
- studentský text má být čistý a srozumitelný.

| Redakční hranice | Co je interní podklad pro autora, nemá se automaticky objevovat v textu pro žáka. |
| --- | --- |

## 12. Repozitář a publikační konvence

Repo konvence:

| Cesta | Význam |
| --- | --- |
| `docs/` | publikovaná učebnice |
| `docs/cs/` | české kapitoly |
| `docs/assets/stylesheets/extra.css` | sdílené vizuální úpravy |
| `project-docs/` | interní projektová a autorská dokumentace |
| `resources/` | zdrojové podklady |

Publikace na Cloudflare Pages:

| Nastavení | Hodnota |
| --- | --- |
| Build command | `mkdocs build --strict` |
| Build output directory | `site` |
| Root directory | `/` |

Pokud Cloudflare Pages v build logu nenainstaluje Python závislosti z `requirements.txt`, použít explicitní build command:

```bash
pip install -r requirements.txt && mkdocs build --strict
```

Ochrana přístupu:

- web používá Cloudflare Pages Functions middleware v `functions/_middleware.js`,
- přístup je chráněný pomocí Basic Auth,
- přihlašovací údaje jsou v Cloudflare Pages environment variables `BASIC_USER` a `BASIC_PASS`,
- pokud proměnné nejsou nastavené, middleware má selhat uzavřeně a web nezpřístupnit.

Technické nastavení:

- `strict: true` se používá při buildu příkazem `mkdocs build --strict`,
- verze Pythonu je určena souborem `.python-version`,
- `use_directory_urls` zůstává ve výchozím režimu MkDocs,
- `Material for MkDocs`,
- `pymdownx.superfences` pro Mermaid.

## 13. AI / Codex pravidla

Při práci na této učebnici platí:

- nejdříve analyzovat ŠVP a existující stav repozitáře,
- držet schválenou osnovu 10 kapitol,
- držet jednotný tón napříč kapitolami,
- nevkládat do publikované části interní autorské poznámky,
- nerozšiřovat osnovu bez důvodu,
- při větší změně osnovy nejdříve navrhnout úpravu v chatu.

| Důležitá zkušenost | U učebnic je konzistence důležitější než kreativní vylepšování každé kapitoly jiným stylem. |
| --- | --- |

## 14. Definition of Done

Kapitola nebo větší blok práce je hotový tehdy, když:

- odpovídá obsahovému cíli,
- pokrývá příslušné části ŠVP,
- drží se stejné struktury jako zbytek knihy,
- používá správný tón a terminologii,
- má dostatečné členění, spacing a vizuální přehlednost,
- případné diagramy nebo tabulky skutečně pomáhají výkladu,
- build `mkdocs build --strict` projde bez chyby,
- změna je zařazená do navigace.

## 15. Shrnutí hlavního principu

Tato kniha stojí na jednoduché myšlence:

**Žák se nemá učit izolovaná tlačítka v aplikacích, ale chápat, jak informace a data proměnit v použitelný pracovní výstup.**

Proto má učebnice vést od:

- informační potřeby,
- přes vyhledání, ověření a interpretaci informací,
- k dokumentům, tabulkám a databázím,
- a nakonec k praktickým úkolům z ekonomické praxe.
