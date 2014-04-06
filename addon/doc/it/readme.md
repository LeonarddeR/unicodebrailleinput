# UnicodeBrailleInput #

* Autori: Mesar Hameed, Patrick Zajda.
* download [stable version][1]
* download [development version][2]

Questo componente aggiuntivo permette di convertire il testo da braille (ad
esempio 1345-1236-145-1) in caratteri braille Unicode.

Lo scopo di questo componente aggiuntivo specifico è di facilitare lo
sviluppo delle tabelle di Liblouis ed aggiungere test automatici per la
propria lingua.

## Utilizzo ##

* Aprire un editor che supporti Unicode (ad esempio Notepad++)
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu
* Digitare il testo braille in valori numerici.
* Premere OK.
* I caratteri Unicode richiesti verranno copiati negli appunti pronti per
  essere incollati.

## Changes for 1.1-dev ##

* Improve delay to allow announcements to be heard correctly.
* Many new translations.
* Added documentation under NVDA help menu.
* Added a checkbox to optionally replace the space braille (character
  0x2800) by the regular space character.
* Shortcuts can now be reassigned using the NVDA gesture input dialog, under
  the Tools category.

## Changes for 1.0 ##

* Initial release
* New Languages: French

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ubi

[2]: http://addons.nvda-project.org/files/get.php?file=ubi-dev
