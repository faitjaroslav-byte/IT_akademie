// Oba soubory .gs vložte do stejného projektu Google Apps Script.
const RETRO_FORM_ID_KEY = 'RETRO_FORM_ID';
const RETRO_ITEMS_KEY = 'RETRO_ITEMS';

function vytvoritFormularRetrospektivy() {
  const vlastnosti = PropertiesService.getScriptProperties();
  if (vlastnosti.getProperty(RETRO_FORM_ID_KEY)) {
    throw new Error('Formulář již existuje. Jeho ID najdete ve vlastnosti RETRO_FORM_ID.');
  }

  const formular = FormApp.create('Retrospektiva: typografie v MS Word a Zotero', true);
  formular.setDescription('Anonymní reflexe po hodině. U stupnic 1 = vůbec si nevěřím, 5 = zvládnu samostatně.');
  formular.setCollectEmail(false);
  formular.setLimitOneResponsePerUser(false);
  formular.setConfirmationMessage('Děkuji za odpověď.');

  const otazky = [
    { typ: 'scale', text: 'Jak jistě zvládneš používat styly nadpisů a vytvořit z nich automatický obsah?' },
    { typ: 'scale', text: 'Jak jistě zvládneš samostatně upravit delší odborný dokument tak, aby měl konzistentní nadpisy, odstavce, zalomení stránek a popisky?' },
    { typ: 'scale', text: 'Jak jistě zvládneš pomocí Zotero vložit citaci, změnit citační styl a aktualizovat seznam literatury?' },
    { typ: 'text', text: 'Představ si, že máš zítra odevzdat maturitní práci. Co bys před odevzdáním v dokumentu zkontroloval/a nebo aktualizoval/a?' },
    { typ: 'text', text: 'Co z práce ve Wordu nebo Zotero ještě potřebuješ vysvětlit nebo procvičit?' },
  ];

  const polozky = otazky.map(otazka => {
    const polozka = otazka.typ === 'scale'
      ? formular.addScaleItem().setBounds(1, 5).setLabels('Vůbec si nevěřím', 'Zvládnu samostatně')
      : formular.addParagraphTextItem();
    polozka.setTitle(otazka.text).setRequired(true);
    return { typ: otazka.typ, itemId: polozka.getId() };
  });

  const tabulka = SpreadsheetApp.create('Retrospektiva: typografie a Zotero - odpovědi');
  formular.setDestination(FormApp.DestinationType.SPREADSHEET, tabulka.getId());
  vlastnosti.setProperties({
    [RETRO_FORM_ID_KEY]: formular.getId(),
    [RETRO_ITEMS_KEY]: JSON.stringify(polozky),
  });

  console.log('Formulář pro úpravy: ' + formular.getEditUrl());
  console.log('Formulář pro odpovědi: ' + formular.getPublishedUrl());
  console.log('Tabulka odpovědí: ' + tabulka.getUrl());
}
