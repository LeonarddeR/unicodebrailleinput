# Wprowadzanie unikodu brajla / UnicodeBrailleInput #

* autorzy: Mesar Hameed, Patrick Zajda.
* download [stable version][1]
* download [development version][2]

Ten dodatek pozwala na konwersję znaków brajlowskich np. 1345-1236-145-1, na
znaki brajla w systemie unicode

celem tego dodatku jest ułatwienie pracy twórcom tablic brajla dla
biblioteki liblouis oraz dodanie automatycznych testów dla języków
narodowych

## użycie ##

* otwórz rozumiejący znaki unicode edytor, np notepad plus plus,
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu
* wpisz tekst brajlowski w formie numerycznej
* wciśnij ok
* odpowiednie znaki unicode zostaną skopiowane do schowka

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
