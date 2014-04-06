# Unikód Braille bevitel #

* Készítők: Mesar Hameed, Patrick Zajda.
* download [stable version][1]
* download [development version][2]

A kiegészítővel braille szöveget konvertálhat át (pl. 1345-1236-145-1)
unikódú braille karakterekre.

Ez a speciállis bővítmény egy új LibLouis tábla elkészítésében, vagy egy már
kész nyelv tesztelésében nyújt nagy segítséget.

## Használat ##

* Nyisson meg egy unicode szövegszerkesztőt (pl. Notepad++)
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu
* gépelje be a braille szöveget numerikus formában.
* Nyomja meg az ok gombot.
* A kívánt unicode karaktersorozat a vágólapra kerül, amit bárhova
  beilleszthet.

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
