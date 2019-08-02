# UnicodeBrailleInput #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Download [stabil version][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## Brug

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Tryk OK.
* De ønskede Unicode-tegn vil blive kopieret til udklipsholderen, så du kan
  indsætte dem.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Ændringer i 2.0

* Hjælp til tilføjelsesprogrammet er til rådighed fra styring af
  tilføjelsesprogrammer.

## Ændringer i 1.1 ##

* Forbedret forsinkelse, så annonceringer kan høres korrekt.
* Mange nye oversættelser.
* Tilføjet dokumentation under NVDAs hjælpemenu.
* Tilføjet en checkboks, så man kan vælge at erstatte Braille-mellemrum
  (tegn 0x2800) med det almindelige mellemrum.
* Genvejstaster kan nu ændres ved hjælp af dialogen Inputbevægelser under
  kategorien Værktøjer.

## Ændringer i 1.0 ##

* Første udgivelse
* Nye sprog: Fransk.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
