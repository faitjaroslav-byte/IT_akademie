// Spusťte až po vytvoritFormularRetrospektivy() ve stejném Apps Script projektu.
// Pořadí hodnot odpovídá pěti otázkám v prvním skriptu a v kapitole učebnice.
const RETRO_MOCK_ODPOVEDI = [
  [5, 4, 4, 'Aktualizoval/a bych obsah, prošel/prošla popisky a zkontroloval/a seznam literatury.', 'Potřebuji ještě procvičit změnu citačního stylu.'],
  [4, 4, 2, 'Zkontroloval/a bych nadpisy, obsah a odkazy na obrázky.', 'V Zotero se mi nedaří aktualizovat seznam literatury.'],
  [4, 3, 2, 'Zkontroloval/a bych formátování odstavců a citace.', 'Nevím, jak opravit chybný záznam v Zotero.'],
  [5, 5, 4, 'Aktualizoval/a bych obsah a seznam literatury, pak prošel/prošla celý dokument.', 'Rád/a bych si zopakoval/a popisky obrázků.'],
  [3, 3, 2, 'Asi bych zkontroloval/a pravopis a nadpisy.', 'Potřebuji znovu ukázat vložení citace ze Zotero.'],
  [4, 4, 3, 'Zkontroloval/a bych styly, zalomení stran a obsah.', 'Nejsem si jistý/á změnou citačního stylu.'],
  [5, 4, 5, 'Prošel/prošla bych popisky, citace a aktualizoval/a seznam literatury.', 'Zatím mi stačí procvičit složitější dokument.'],
  [2, 3, 2, 'Zkontroloval/a bych obsah, ale nevím, jak se aktualizuje.', 'Potřebuji procvičit styly nadpisů i Zotero.'],
  [4, 4, 2, 'Zkontroloval/a bych strukturu práce a seznam zdrojů.', 'Zotero mi někdy nevloží správnou citaci.'],
  [5, 5, 4, 'Aktualizoval/a bych všechna automatická pole a ověřil/a citace.', 'Chtěl/a bych si zopakovat práci se seznamem literatury.'],
  [3, 2, 3, 'Zkontroloval/a bych nadpisy a stránky, ale popisky neumím.', 'Potřebuji vysvětlit popisky tabulek.'],
  [4, 3, 2, 'Prošel/prošla bych obsah, odstavce a literaturu.', 'Nevím, jak v Zotero změnit styl pro celý dokument.'],
  [5, 4, 3, 'Zkontroloval/a bych aktualizaci obsahu, popisky a citace.', 'Potřebuji procvičit aktualizaci seznamu literatury.'],
  [3, 4, 2, 'Zkontroloval/a bych vzhled dokumentu a citace.', 'Rád/a bych ještě jednou viděl/a vložení citace.'],
  [4, 4, 4, 'Zkontroloval/a bych styly, automatický obsah a bibliografii.', 'Většinu zvládnu, uvítal/a bych krátké opakování Zotero.'],
];

function vytvoritMockOdpovediRetrospektivy() {
  const vlastnosti = PropertiesService.getScriptProperties();
  const formId = vlastnosti.getProperty('RETRO_FORM_ID');
  const ulozenePolozky = vlastnosti.getProperty('RETRO_ITEMS');
  if (!formId || !ulozenePolozky) {
    throw new Error('Nejprve spusť vytvoritFormularRetrospektivy() ve stejném Apps Script projektu.');
  }

  const formular = FormApp.openById(formId);
  if (!formular.isAcceptingResponses()) {
    throw new Error('Formulář nepřijímá odpovědi. Zapni jejich přijímání ve Forms.');
  }
  const ulozene = JSON.parse(ulozenePolozky);
  const aktualni = formular.getItems();
  const ocekavaneTypy = [FormApp.ItemType.SCALE, FormApp.ItemType.SCALE, FormApp.ItemType.SCALE,
    FormApp.ItemType.PARAGRAPH_TEXT, FormApp.ItemType.PARAGRAPH_TEXT];
  if (ulozene.length !== 5 || aktualni.length !== 5 ||
      ulozene.some((p, i) => p.itemId !== aktualni[i].getId() || aktualni[i].getType() !== ocekavaneTypy[i])) {
    throw new Error('Otázky ve formuláři se změnily. Odpovědi se neodešlou, aby nevznikla neúplná data.');
  }

  RETRO_MOCK_ODPOVEDI.forEach(hodnoty => {
    const odpoved = formular.createResponse();
    aktualni.forEach((polozka, i) => {
      const polozkovaOdpoved = i < 3
        ? polozka.asScaleItem().createResponse(hodnoty[i])
        : polozka.asParagraphTextItem().createResponse(hodnoty[i]);
      odpoved.withItemResponse(polozkovaOdpoved);
    });
    odpoved.submit();
  });

  console.log('Odesláno ' + RETRO_MOCK_ODPOVEDI.length + ' fiktivních odpovědí. Celkem ve formuláři: ' + formular.getResponses().length);
  console.log('Formulář: ' + formular.getEditUrl());
  console.log('Tabulka odpovědí: https://docs.google.com/spreadsheets/d/' + formular.getDestinationId() + '/edit');
}
