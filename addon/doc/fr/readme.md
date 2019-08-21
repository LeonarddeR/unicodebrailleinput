# UnicodeBrailleInput #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Télécharger [version stable][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## Utilisation

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Cliquez sur OK.
* Les caractères unicodes requis seront copiés dans votre presse-papiers
  pour être collés.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Changements pour la version 2.0

* L'aide de l'extension est disponible à partir du Gestionnaire
  d'extensions.

## Changements pour la version 1.1 ##

* Améliore le délai pour permettre aux annonces  d'être écouter
  correctement.
* Plusieurs nouvelles traductions.
* Ajout de la Documentation dans le sous-menu aide de NVDA.
* Ajout d'une case à cocher pour éventuellement remplacer l'espace braille
  (caractère 0x2800) par le caractère d'espace régulier.
* Les raccourcis clavier peuvent maintenant être réaffectées à l'aide de la
  boîte de dialogue gestes d'entrée de NVDA , sous la catégorie Outils.

## Changements pour la version 1.0 ##

* Première version
* Nouvelles Langues : Français

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
