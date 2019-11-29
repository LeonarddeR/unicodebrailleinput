# UnicodeBrailleInput #

* Autori: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* download [stable version][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

Lo scopo di questo componente aggiuntivo specifico è di facilitare lo
sviluppo delle tabelle di Liblouis ed aggiungere test automatici per la
propria lingua. Con l'introduzione della tabella braille unicode in NVDA
2017.3, questo componente aggiuntivo non risulta più necessario in quanto
gli utenti possono scegliere di inserire il braille con la nuova
tabella. Tuttavia, questo componente aggiuntivo può ancora aiutare a
convertire il testo normale in unicode braille secondo una particolare
tabella di input.

## Utilizzo

* Aprire un editor che supporti Unicode (ad esempio Notepad++)
* Premere NVDA+Ctrl+U o selezionare Unicode Braille Input situato sotto la
  voce strumenti di NVDA
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Digitare il testo braille in valori numerici o normalmente.
* Premere OK.
* I caratteri Unicode richiesti verranno copiati negli appunti pronti per
  essere incollati.

## Modifiche per la 3.0

* Nuovo sviluppatore: Leonard de Ruijter.
* Il componente aggiuntivo è compatibile con Python 3 e quindi con NVDA
  2019.3 e versioni successive.
* Aggiunta la possibilità di creare Braille Unicode dal testo normale in
  base alla tabella Braille di input attualmente selezionata.

## Modifiche per la 2.0

* L'aiuto del componente aggiuntivo è disponibile nel gestore componenti
  aggiuntivi

## Modifiche per la 1.1 ##

* Migliorato il ritardo in modo da ascoltare gli annunci correttamente
* Molte traduzioni aggiunte
* Aggiunta la documentazione sul menu aiuto di NVDA
* Aggiunta una casella di controllo per sostituire lo spazio in braille
  (carattere 0x2800) con il carattere spazio standard
* I tasti di scelta rapida possono ora essere riassegnati utilizzando la
  finestra gesti e tasti di immissione di NVDA, sotto la categoria
  Strumenti.

## Novità per 1.0 ##

* Prima versione
* Nuova lingua: francese

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
