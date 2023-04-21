# UnicodeBrailleInput #

* Forfattere: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Download [stabil version][1]

Denne tilføjelse giver dig mulighed for at konvertere tekst fra braille
(f.eks. 1345-1236-145-1) til Unicode-brailletegn. Du kan også konvertere
tekst i henhold til den aktuelt valgte input-brailletabel.

Formålet med denne specialiserede tilføjelse er at gøre det lettere at
hjælpe med at forbedre liblouis-tabeller og tilføje automatiske test til dit
sprog. Med tilføjelsen af unicode-brailletabel i NVDA 2017.3 er denne
tilføjelse ikke længere nødvendig for dette, da brugere kan vælge at
indtaste braille med den nye tabel. Denne tilføjelse kan dog stadig hjælpe
med at konvertere normal tekst til unicode-braille i henhold til en bestemt
inputtabel.

## Brug

* Åbn en tekst-editor, som kan behandle Unicode-tegn, f.eks. Notepad Plus
  Plus.
* Tryk NVDA+Ctrl+u eller vælg "Unicode Braille input", som findes i
  NVDA-menuen under værktøjer.
* Vælg, om dit input består af punktskriftspunkter (f.eks. 1345-1236-145-1)
  eller normal tekst i henhold til den aktuelle punktskriftstabel
  (f.eks. hollandsk (Holland).
* Indtast din punktskrift i henholdsvis numerisk format eller normal tekst.
* Tryk OK.
* De ønskede Unicode-tegn vil blive kopieret til udklipsholderen, så du kan
  indsætte dem.

## Ændringer i 3.0

* Ny vedligeholder: Leonard de Ruijter.
* Add-on er kompatibel med Python 3 og derfor med NVDA 2019.3 og nyere.
* Tilføjet muligheden for at oprette unicode-braille fra normal tekst i
  henhold til den aktuelt valgte indtastningstabel for punktskrift.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
