# UnicodeBrailleInput #

* autorzy: Mesar Hameed, Patrick Zajda.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Ten dodatek pozwala na konwersję znaków brajlowskich np. 1345-1236-145-1, na
znaki brajla w systemie unicode

celem tego dodatku jest ułatwienie pracy twórcom tablic brajlowskich dla
biblioteki liblouis oraz dodanie automatycznych testów dla języków
narodowych. Ten dodatek więcej nie jest potrzebny, dla tego że uniodowa
tablica brajlowska jest dodana w NVDA 2017.3, Ten dodatek więcej nie jest
wymagany, dla tego, że użytkownicy mogą wprowadzać braj unikodowy za pomocą
nowej tablicy.

## użycie ##

* otwórz rozumiejący znaki unicode edytor, np notepad plus plus,
* Naciśnij NVDA+Ctrl+U lub wybierz wprowadzanie unikodu brajla w menu
  Narzędzia NVDA
* wpisz tekst brajlowski w formie numerycznej
* wciśnij ok
* odpowiednie znaki unicode zostaną skopiowane do schowka

## Zmiany dla wersji 2.0 ##

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

[1]: https://addons.nvda-project.org/files/get.php?file=ubi

[2]: https://addons.nvda-project.org/files/get.php?file=ubi-dev
