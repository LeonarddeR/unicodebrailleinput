# UnicodeBrailleInput #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Pobierz [wersja stabilna][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## użycie

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* wciśnij ok
* odpowiednie znaki unicode zostaną skopiowane do schowka

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Zmiany dla wersji 2.0

* Pomoc dodatku dostępna w managerze dodatków.

## Zmiany dla wersji 1.1 ##

* Poprawione opóźnienie, aby powiadomienia były wypowiadane prawidłowo.
* Wiele nowych tłumaczeń.
* Dodano dokumentację w menu pomocy NVDA.
* Dodane pole wyboru umożliwiające opcjonalne zastępowanie brajlowskiej
  spacji (znak 0x2800) zwykłym znakiem spacji.
* Klawisze skrótów mogą być zmieniane przy użyciu okna "Zdarzenia wejścia" w
  kategorii Narzędzia.

## Zmiany dla wersji 1.0 ##

* Pierwsze wydanie
* Nowe języki: francuski

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
