# Unicode-Braille-Eingabe #

* Authoren: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* [Stabile Version herunterladen][1]

Mit dieser Erweiterung können Zeichen, deren angezeigte Braillepunkte
numerisch angegeben werden (z. B. 1345-1236-145-1) in Unicode konvertiert
werden.

Der Zweck dieser speziellen Erweiterung ist es, Verbesserung der
Liblouis-Tabellen beizutragen und automatische Tests für Ihre Sprache
hinzuzufügen.  Mit der Hinzufügung der Unicode-Punktschrifttabelle in der
NVDA 2017.3 entfällt dieses Add-on, da der Anwender die Möglichkeit hat, die
Blindenschrift mit der neuen Tabelle einzugeben.  Dieser Erweiterung kann
jedoch trotzdem helfen, normalen Text gemäß einer bestimmten Eingabetabelle
in Unicode-Punktschrift umzuwandeln.

## Verwendung

* Öffnen Sie einen Text-Editor, der Unicode unterstützt (z. B. Notepad++)
* Drücken Sie NVDA+Strg+U oder wählen Sie Unicode-Braille-Eingabe aus dem
  Menü Extras im NVDA-Menü aus.
* Wählen Sie aus, ob Ihre Eingabe aus Braille-Punkten
  (z. B. 1345-1236-145-1) oder normalem Text gemäß der aktuellen
  Braille-Tabelle (z. B. Niederländisch (Niederlande) besteht.
* Geben Sie Ihren Braille-Text in numerischer Form ein.
* Klicken Sie auf OK.
* Die benötigten Unicode-Zeichen werden in die Zwischenablage kopiert, so
  dass Sie diese gleich einfügen können.

## Änderungen in 3.0

* Neuer Betreuer: Leonard de Ruijter.
* Erweiterung ist kompatibel mit Python 3 und daher mit NVDA 2019.3 und
  neuer.
* Es wurde die Möglichkeit hinzugefügt, Unicode-Punktschrift aus normalem
  Text gemäß der aktuell ausgewählten Eingabepunktetabelle zu erstellen.

## Änderungen in 2.0

* Hilfe zur Erweiterung ist in der Erweiterungsverwaltung verfügbar.

## Änderungen in 1.1 ##

* Verbesserte Wartezeiten beim korrekten Ansagen, damit sie besser gehört
  werden können.
* Viele weitere Übersetzungen.
* Dokumentation im NVDA-Hilfe-Menü hinzugefügt.
* Kontrollkästchen zur optionalen Ersetzung des Braille-Leerzeichens
  (Zeichen 0x2800) durch das reguläre Leerzeichen hinzugefügt.
* Tastenkürzel können im Menü Eingabegesten unter Extras von NVDA neu
  zugeordnet werden.

## Änderungen in 1.0 ##

* Ehrstveröffentlichung
* Neue Sprachen: Französisch.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
