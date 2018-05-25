# UnicodeBrailleInput #

* Autori: Mesar Hameed, Patrick Zajda.
* download [stable version][1]
* download [development version][2]

Questo componente aggiuntivo permette di convertire il testo da braille (ad
esempio 1345-1236-145-1) in caratteri braille Unicode.

Lo scopo di questo componente aggiuntivo specifico è di facilitare lo
sviluppo delle tabelle di Liblouis ed aggiungere test automatici per la
propria lingua. Con l'introduzione della tabella braille unicode in NVDA
2017.3, questo componente aggiuntivo non risulta più necessario in quanto
gli utenti possono scegliere di inserire il braille con la nuova tabella.

## Utilizzo ##

* Aprire un editor che supporti Unicode (ad esempio Notepad++)
* Premere NVDA+Ctrl+U o selezionare Unicode Braille Input situato sotto la
  voce strumenti di NVDA
* Digitare il testo braille in valori numerici.
* Premere OK.
* I caratteri Unicode richiesti verranno copiati negli appunti pronti per
  essere incollati.

## Modifiche per la 2.0 ##

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

[2]: https://addons.nvda-project.org/files/get.php?file=ubi-dev
