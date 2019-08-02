# UnicodeBrailleInput #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* stiahnuť [stabilnú verziu][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## použitie

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Aktivujte tlačidlo OK.
* Unicode znaky sa vložia do schránky a môžete ich prilepiť do editora.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Zmeny vo verzii 2.0

* Návod k doplnku nájdete v správcovi doplnkov.

## Zmeny vo verzii 1.1 ##

* Predĺžený čas tak, aby bolo počuť celé hlásenia.
* Nové preklady.
* V menu pomocník pridaná dokumentácia k doplnku.
* pridané začiarkávacie pole, po ktorého začiarknutí je možné nahradiť znak
  medzera (znak 0x2800) normálnou medzerou.
* Skratky je možné zmeniť pomocou nastavení skratiek v NVDA, pozrite strom
  nástroje.

## Zmeny vo verzii 1.0 ##

* prvé vydanie
* Preklad do Francúzštiny

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
