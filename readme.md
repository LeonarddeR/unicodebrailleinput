# UnicodeBrailleInput

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Download [stable version][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1) to Unicode braille characters.
You can also convert text according to the currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to improve liblouis tables and to add automatic tests for your language.
With the addition of unicode braille table in NVDA 2017.3, this add-on is no longer required for this, as users can choose to input braille with the new table.
However, this add-on can still aid in converting normal text to unicode braille according to a particular input table.

## Usage

* Open a unicode aware text editor (for example Notepad plus plus).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1) or normal text according to the current braille table (e.g. Dutch (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Press OK.
* The required unicode characters will be copied to your clipboard ready for you to  paste.

## Changes

### Changes for 4.1

* The add-on now requires NVDA 2023.1 or newer
* Added support for custom braille tables as input table

### Changes for 4.0

* Add-on is compatible with NVDA 2024.1
* Changed the gesture to open the Unicode Braille dialog from NVDA+control+u to NVDA+control+i

### Changes for 3.4

* Add-on is compatible with NVDA 2023.1

### Changes for 3.3

* Add-on is compatible with NVDA 2022.1

### Changes for 3.2

* Add-on is compatible with NVDA 2021.1
* Fixed an issue that caused a traceback when wrong input was provided in dot input mode. A friendly message box is now shown instead
* Updated translations.

### Changes for 3.1

* The tab order for the radio buttons and the input edit control has been swapped.
* Updated translations.

### Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and above.
* Added the ability to create unicode braille from normal text according to the currently selected input braille table.

### Changes for 2.0

* Add-on help is available from the Add-ons Manager.

### Changes for 1.1

* Improve delay to allow announcements to be heard correctly.
* Many new translations.
* Added documentation under NVDA help menu.
* Added a checkbox to optionally replace the space braille (character 0x2800) by the regular space character.
* Shortcuts can now be reassigned using the NVDA gesture input dialog, under the Tools category.

### Changes for 1.0

* Initial release
* New Languages: French

[1]: http://addons.nvda-project.org/files/get.php?file=ubi
