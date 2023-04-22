# UnicodeBraille-invoer #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* download [stabiele versie][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## Gebruik

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Druk op OK.
* De benodigde unicode-karakters zullen naar het klembord worden gekopieerd,
  klaar om geplakt te worden.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Veranderingen in 2.0

* Help voor de add-on is beschikbaar vanuit het venster Add-ons beheren.

## Veranderingen in 1.1 ##

* Vertraging verbeterd zodat mededelingen correct gehoord kunnen worden.
* Diverse nieuwe vertalingen.
* Documentatie toegevoegd in het NVDA help menu.
* Selectievakje toegevoegd om het brailleteken voor spatie (teken 0x2800) te
  vervangen door het reguliere teken voor spatie.
* Sneltoetsen kunnen nu opnieuw toegewezen worden in het NVDA venster
  Invoerhandelingen koppelen, onder de categorie Extra.

## Veranderingen in 1.0 ##

* Eerste versie
* Nieuwe vertalingen: Frans

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
