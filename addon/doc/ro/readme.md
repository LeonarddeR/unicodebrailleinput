# UnicodeBrailleInput #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Descărcați [versiunea stabilă][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## Utilizare

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Apăsați OK
* Caracterele unicode necesare vor fi copiate pe planșetă, gata să le
  lipiți.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Modificări aduse în versiunea 2.0

* Ghidul add-on-ului este disponibil în managerul de add-onuri.

## Modificări aduse în versiunea 1.1 ##

* A fost îmbunătățit delay-ul pentru a permite anunțurile să fie auzite
  corect.
* Multe traduceri noi.
* A fost adăugată documentația în meniul NVDA, secțiunea ajutor.
* A fost adăugată o casetă de bifat pentru a înlocui opțional spațiul
  braille (caracter 0x2800) de spațiul regulat al caracterului.
* Comenzile rapide pot fi acum realocate folosind dialogul gestului de
  intrare NVDA, în secțiunea Instrumente.

## Modificări aduse în versiunea 1.0 ##

* Versiunea inițială
* Limbi noi: Franceză

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
