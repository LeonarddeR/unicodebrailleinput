# UnicodeBrailleInput #

* Autori: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Scarica [versione stabile][1]

Questo componente aggiuntivo permette di convertire il testo da braille (ad
esempio 1345-1236-145-1) in caratteri braille Unicode. E' anche possibile
convertire il testo utilizzando la tabella Braille di input al momento
selezionata.

Lo scopo di questo componente aggiuntivo specifico è di facilitare lo
sviluppo delle tabelle di Liblouis ed aggiungere test automatici per la
propria lingua. Con l'introduzione della tabella braille unicode in NVDA
2017.3, questo componente aggiuntivo non risulta più necessario, in quanto
gli utenti possono scegliere di inserire il braille con la nuova
tabella. Tuttavia, questo componente aggiuntivo può ancora aiutare a
convertire il testo normale in unicode braille secondo una particolare
tabella di input.

## Utilizzo

* Aprire un editor di testi che supporti Unicode (ad esempio Notepad++)
* Premere NVDA+Ctrl+U o selezionare Unicode Braille Input situato sotto la
  voce strumenti di NVDA.
* Selezionare se l'input consiste di punti Braille (Ad esempio
  1345-1236-145-1) o di testo normale inserito utilizzando la tabella
  Braille corrente (ad esempio Dutch (Netherlands)).
* Digitare il testo braille in valori numerici o il testo normale, a seconda
  della scelta effettuata in precedenza.
* Premere OK.
* I caratteri Unicode richiesti verranno copiati negli appunti pronti per
  essere incollati.

## Novità nella versione 3.0

* Nuovo sviluppatore: Leonard de Ruijter.
* Il componente aggiuntivo è compatibile con Python 3 e quindi con NVDA
  2019.3 e versioni successive.
* Aggiunta la possibilità di creare Braille Unicode da testo normale in base
  alla tabella Braille di input attualmente selezionata.

## Novità nella versione 2.0

* L'aiuto del componente aggiuntivo è disponibile nel gestore componenti
  aggiuntivi

## Novità nella versione 1.1 ##

* Migliorato il ritardo in modo da ascoltare gli annunci correttamente.
* Molte traduzioni aggiunte
* Aggiunta la documentazione nel menu aiuto di NVDA
* Aggiunta una casella di controllo per sostituire lo spazio in braille
  (carattere 0x2800) con il carattere spazio standard
* I tasti di scelta rapida possono ora essere riassegnati utilizzando la
  finestra gesti e tasti di immissione di NVDA, sotto la categoria
  Strumenti.

## Novità nella versione 1.0 ##

* Prima versione
* Nuova lingua: francese

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
