# UnicodeBrailleInput

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Download [stable version][1]

This add-on allows you to perform several Braille conversion tasks.
For example, you can convert text from braille dot notation (E.G. 1345-1236-145-1) to Unicode or ASCII braille characters.
You can also convert text according to the currently selected input or output braille table, either by typing or pasting it into an input field, or by importing a text file.
The result can either be copied to the clipboard or exported into a text or BRF file.

The initial purpose of this specialized addon was to make it easier to help to improve liblouis tables and to add automatic tests for your language.
However, with the addition of the unicode braille table in NVDA 2017.3, this add-on is no longer required for that.
Users can now choose to input braille with that table, either via a Braille keyboard or the [PC Keyboard Braille Input add-on][2].

## Usage example

* Open a text editor (for example Notepad plus plus).

* Press NVDA+Ctrl+i or choose Unicode Braille Input found under NVDA tools menu.

* Type your braille text in numeric form or your normal text, respectively. You can also import from a text file if desired.

* Select whether your input consists of braille dots (e.g. 1345-1236-145-1) or normal text according to a current braille table (e.g. Dutch (Netherlands).

* Select the output type. Leave it to Unicode braille, or change it to BRF or NABC if desired.

* Select the export type:
  * When set to `Clipboard`, The result will be copied to your clipboard ready for you to  paste after pressing OK.
  * When set to `File`, after pressing OK, a save window will appear.

## Changes

### Changes for 5.0

* The add-on now requires NVDA 2024.3 or newer
* Changed radio buttons into combo boxes
* Added output types for ASCII braille (BRF) and NABC (North American Braille Computer Code with full Latin1 character set)

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

[2]: https://github.com/nvdaes/pcKbBrl
