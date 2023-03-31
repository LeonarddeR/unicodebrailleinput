# UnicodeBrailleInput #

* Auteurs : Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Télécharger [version stable][1]

Cette extension permet de convertir du texte depuis du braille (ex :
1345-1236-145-1) en caractères braille Unicode.  Vous pouvez également
convertir du texte en fonction de la table braille d'entrée actuellement
sélectionnée.

Le but de cette extension spécialisée est de rendre plus simple l'aide à
l'amélioration des tables liblouis et la création de tests automatiques pour
votre langue.  Avec l'ajout de la table braille Unicode dans NVDA 2017.3,
cette extension n'est plus requise, car les utilisateurs peuvent choisir la
saisie braille avec la nouvelle table.  Cependant, cete extension peut
toujours aider à convertir du texte normal en braille unicode en fonction
d'une table d'entrée particulière.

## Utilisation

* Ouvrez un éditeur de texte qui supporte l'Unicode (comme Notepad++)
* Appuyez sur NVDA+Ctrl+U ou choisir Saisie Braille Unicode situé dans le
  sous-menu Outils de NVDA.
* Choisissez si votre saisie consiste en des points braille (par
  ex. 1345-1236-145-1) ou en du texte normal interprété avec la table
  braille actuelle (par ex. néerlandais (Pays-Bas).
* Saisissez votre texte en braille sous forme numérique ou de texte normal
  respectivement.
* Cliquez sur OK.
* Les caractères Unicode requis seront copiés dans votre presse-papiers pour
  être collés.

## Changements pour la version 3.0

* Nouveau responsable : Leonard de Ruijter.
* L'extension est compatible avec Python 3 et donc avec NVDA 2019.3 et
  supérieur.
* Ajout de la possibilité de créer du braille Unicode à partir de texte
  normal en fonction de la table braille d'entrée actuellement sélectionnée.

## Changements pour la version 2.0

* L'aide de l'extension est disponible à partir du Gestionnaire
  d'extensions.

## Changements pour la version 1.1 ##

* Améliore le délai pour permettre aux annonces  d'être écoutées
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
