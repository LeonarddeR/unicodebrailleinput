# Wprowadzanie unikodu brajla / UnicodeBrailleInput #

* autorzy: Mesar Hameed, Patrick Zajda.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Ten dodatek pozwala na konwersję znaków brajlowskich np. 1345-1236-145-1, na
znaki brajla w systemie unicode

celem tego dodatku jest ułatwienie pracy twórcom tablic brajla dla
biblioteki liblouis oraz dodanie automatycznych testów dla języków
narodowych

## użycie ##

* otwórz rozumiejący znaki unicode edytor, np notepad plus plus,
* Naciśnij NVDA+Ctrl+U lub wybierz wprowadzanie unikodu brajla w menu
  Narzędzia NVDA
* wpisz tekst brajlowski w formie numerycznej
* wciśnij ok
* odpowiednie znaki unicode zostaną skopiowane do schowka

## Zmiany dla wersji 1.1-dev ##

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

[1]: http://addons.nvda-project.org/files/get.php?file=ubi

[2]: http://addons.nvda-project.org/files/get.php?file=ubi-dev
