# UnicodeBrailleInput #

* Autori: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* stiahnuť [stabilnú verziu][1]

Tento doplnok umožňuje konvertovať text z brailu (napríklad 1345-1236-145-1)
na brailovské Unicode znaky. Takisto umožňuje konvertovať text podľa
vybratej braillovskej tabuľky.

Cieľom doplnku je pomôcť pri zlepšovaní liblouis tabuliek a poskytnúť
automatické jazykové testovanie. V NVDA od verzie 2017.3 je možné priamo na
vstup použiť braillovskú tabuľku unicode. Doplnok však môže byť užitočný na
konvertovanie znakov unicode pre ostatné existujúce jazykové tabuľky.

## použitie

* Otvorte editor, ktorý vie spracovať unicode znaky (napríklad Notepad plus
  plus).
* Stlačte nvda+ctrl+u alebo aktivujte položku Unicode braille imput v menu
  nástroje v NVDA.
* Rozhodnite sa, či budete na vstup používať braillovské body
  1345-1236-145-1) alebo normálny text podľa aktuálnej braillovskej tabuľky
  (napríklad Slovenčina plnopis).
* Zadajte reťazec v numerickom tvare alebo ako text.
* Aktivujte tlačidlo OK.
* Unicode znaky sa vložia do schránky a môžete ich prilepiť do editora.

## Zmeny vo verzii 3.0

* Doplnok od teraz spravuje Leonard de Ruijter.
* Doplnok je kompatibilný s Python 3 a teda s NVDA od verzie 2019.3.
* Pridaná možnosť vytvoriť unicode vstup zo zadaného textu podľa vybratej
  tabuľky.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
