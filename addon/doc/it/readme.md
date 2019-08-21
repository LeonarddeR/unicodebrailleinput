# UnicodeBrailleInput #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* download [stable version][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## Utilizzo

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Premere OK.
* I caratteri Unicode richiesti verranno copiati negli appunti pronti per
  essere incollati.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

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
