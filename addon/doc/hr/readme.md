# UnicodeBrailleInput #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Preuzmi [stabilnu inačicu][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## korištenje

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Pritisnite u redu.
* Zahtjevani će znakovi biti kopirani u međuspremnik spremni da ih
  zalijepite

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Izmjene u inačici 2.0

* pomoć za dodatak dostupna je u upravitelju dodataka.

## Promjene u inačici 1.1 ##

* Unaprijeđeno kašnjenje tako da se obavjesti mogu točno čuti.
* Puno novih prijevoda.
* Dodana dokumentacija u NVDA izborniku pomoć.
* Dodan potvrdni okvir koji omogućuje neobaveznu zamjenu znaka brajičnog
  razmaka (znak 0x2800) sa normalnim znakom razmaka.
* Prečaci sada mogu biti promijenjeni koristeći NVDA dijaloški okvir ulaznih
  gesti, pod kategorijom alati.

## promjene u inačici 1.0 ##

* Prva inačica
* Novi jezici: francuski

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
