# Unikód Braille bevitel #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Letöltés: [Stabil verzió][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## Használat

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Nyomja meg az ok gombot.
* A kívánt unicode karaktersorozat a vágólapra kerül, amit bárhova
  beilleszthet.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Az 1.0 verzió változásai

* A kiegészítő súgója elérhető a bővítmények párbeszédablakáról is.

## Az 1.1 verzió változásai ##

* Fejlesztett késleltetés a bejelentések megfelelő hallhatósága érdekében.
* Sok új fordítás.
* A dokumentáció már elérhető az NVDA Súgó menüjéből.
* Hozzáadtak egy jelölőnégyzetet, aminek a bejelölésével felülírhatók a
  Braille szóköz (0x2800) karakterek a normál szóköz karakterrel.
* A billentyűparancsok már módosíthatók az NVDA Beviteli parancsok
  párbeszédablakában, az Eszközök kategóriában.

## Az 1.0 verzió változásai ##

* Első kiadás
* Új nyelvek: francia

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
