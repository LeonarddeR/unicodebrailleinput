# unicodeBrailleInput Global Plugin for NVDA interface
# Copyright (C) 2013-2025 Mesar Hameed, Patrick Zajda, Leonard de Ruijter
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import os
import re

import addonHandler
import braille
import brailleInput
import brailleTables
import gui
import gui.guiHelper
import louis
import wx
from api import copyToClip
from ui import message
from utils.displayString import DisplayStringIntEnum

# Initialize translations.
addonHandler.initTranslation()


invalidInputRegexp = re.compile(r"[^0-8-]+")


class InputType(DisplayStringIntEnum):
	DOTS = 0
	TEXT_OUTPUT_TABLE = 1
	TEXT_INPUT_TABLE = 2

	@property
	def _displayStringLabels(self) -> dict:
		return {
			# Translators: the label of an input type
			self.DOTS: _("Braille dots (e.g. 1345-1236-145-1)"),
			# Translators: the label of an input type
			self.TEXT_OUTPUT_TABLE: _("Normal text according to {table}").format(
				table=braille.handler.table.displayName
			),
			# Translators: the label of an input type
			self.TEXT_INPUT_TABLE: _("Normal text according to {table}").format(
				table=brailleInput.handler.table.displayName
			),
		}


class OutputType(DisplayStringIntEnum):
	UNICODE = 0
	BRF = 1
	NABC = 2

	@property
	def _displayStringLabels(self) -> dict:
		return {
			# Translators: the label of an output type
			self.UNICODE: _("Unicode braille"),
			# Translators: the label of an output type
			self.BRF: _("ASCII braille (BRF)"),
			# Translators: the label of an output type
			self.NABC: _("NABCC"),
		}


class ExportType(DisplayStringIntEnum):
	CLIPBOARD = 0
	FILE = 1

	@property
	def _displayStringLabels(self) -> dict:
		return {
			# Translators: the label of an export type
			self.CLIPBOARD: _("Clipboard"),
			# Translators: the label of an export type
			self.FILE: _("File"),
		}


class _Cache:
	inputType: InputType = InputType.DOTS
	outputType: OutputType = OutputType.UNICODE
	regularSpace: bool = False
	exportType: ExportType = ExportType.CLIPBOARD


BRF_TABLE = "en-us-brf.dis"
NABC_TABLE = "text_nabcc.dis"
UNICODE_TABLE = "braille-patterns.cti"


def getTranslationTable(inputType: InputType) -> brailleTables.BrailleTable:
	match inputType:
		case InputType.TEXT_INPUT_TABLE:
			return brailleInput.handler.table
		case InputType.TEXT_OUTPUT_TABLE:
			return braille.handler.table
		case _:
			raise NotImplementedError


def postProcessUnicode(text: str, outputType: OutputType) -> str:
	match outputType:
		case OutputType.UNICODE:
			return text
		case OutputType.BRF:
			text = "".join(chr(ord(c) & 0x283F) for c in text)
			table = BRF_TABLE
		case OutputType.NABC:
			table = NABC_TABLE
		case _:
			raise NotImplementedError
	return translateText(
		text,
		[
			table,
			UNICODE_TABLE,
		],
		0,
	)


def translateText(
	text: str,
	tables: list[str],
	mode: int,
	regularSpace: bool = False,
) -> str:
	"""
	Translates the given text using the specified Liblouis translation tables and mode.

	Args:
		text: The input text to be translated.
		tables: A list of Liblouis translation table names to use for translation.
		mode: The translation mode to be used by Liblouis.
		regularSpace: If True, replaces Braille space characters (U+2800)
			with regular space characters (U+0020). Defaults to False.

	Returns:
		The translated text, optionally with Braille spaces replaced by regular spaces.
	"""
	text = louis.translate(
		tables,
		text,
		mode=mode,
	)[0]
	out = text
	if regularSpace:
		out = out.replace("\u2800", " ")
	return out


def dotsToUnicode(
	cells: str,
	regularSpace: bool = False,
) -> str:
	"""Convert braille to Unicode
	@param cells: the braille cells (I.E. 13457-12367-1457-17)
	@param regularSpace: if True, space will be replaced by a regular one instead of the braille space
	@return: the result in Unicode (NVDA in our example)
	"""
	cells = cells.translate({
		ord("f"): "1",
		ord("d"): "2",
		ord("s"): "3",
		ord("j"): "4",
		ord("k"): "5",
		ord("l"): "6",
		ord("a"): "7",
		ord(";"): "8",
	}).strip()
	invalidStrings = invalidInputRegexp.findall(cells)
	# Translators: Error message displayed when the user enters invalid input.
	msg = _("Unexpected input: '%s', only dots 0 to 8 and - are allowed.") % "', '".join(invalidStrings)
	if not cells or cells.isspace() or invalidStrings:
		raise ValueError(msg)
	cellsList = cells.split("-")
	out = []
	for cell in cellsList:
		val = 0
		if "1" in cell:
			val |= 1
		if "2" in cell:
			val |= 2
		if "3" in cell:
			val |= 4
		if "4" in cell:
			val |= 8
		if "5" in cell:
			val |= 0x10
		if "6" in cell:
			val |= 0x20
		if "7" in cell:
			val |= 0x40
		if "8" in cell:
			val |= 0x80
		if val:
			val |= 0x2800
			out.append(chr(val))
		else:
			out.append(" " if regularSpace else chr(0x2800))
	return "".join(out)


class BrailleInputDialog(gui.SettingsDialog):
	# Translators: The title of the dialog.
	title = _("Convert Braille")

	def makeSettings(self, sizer):
		sizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=sizer)
		self._brailleTextEdit = sizerHelper.addLabeledControl(
			# Translators: the label of the edit field.
			_("&Input:"),
			wx.TextCtrl,
			style=wx.TE_MULTILINE,
		)

		self.importButton = wx.Button(
			self,
			# Translators: The label for a button to import text.
			label=_("I&mport..."),
		)
		self.importButton.Bind(wx.EVT_BUTTON, self._onImport)

		inputTypeChoices = [t.displayString for t in InputType]
		if brailleInput.handler.table == braille.handler.table or brailleInput.handler.table.output:
			inputTypeChoices.pop()
		self._inputTypeComboBox = sizerHelper.addLabeledControl(
			# Translators: the label of the combo box to choose the input type.
			_("Input &type:"),
			wx.Choice,
			choices=inputTypeChoices,
		)
		self._inputTypeComboBox.Selection = _Cache.inputType
		outputTypeChoices = [t.displayString for t in OutputType]
		self._outputTypeComboBox = sizerHelper.addLabeledControl(
			# Translators: the label of the radio box to choose the output type.
			_("&Output type:"),
			wx.Choice,
			choices=outputTypeChoices,
		)
		self._outputTypeComboBox.Bind(wx.EVT_CHOICE, self._onOutputTypeChange)
		self._outputTypeComboBox.Selection = _Cache.outputType

		self._regularSpaceChk = wx.CheckBox(
			self,
			# Translators: Label for a checkbox, wether to use a regular space or the Braille unicode space.
			label=_("Convert Unicode Braille &space to ASCII space"),
		)
		self._regularSpaceChk.SetValue(_Cache.regularSpace)
		self._regularSpaceChk.Enable(not self._outputTypeComboBox.Selection)
		sizerHelper.addItem(self._regularSpaceChk)

		exportTypeChoices = [t.displayString for t in ExportType]
		self._exportTypeComboBox = sizerHelper.addLabeledControl(
			# Translators: the label of the combo box to choose the export type.
			_("&Export to:"),
			wx.Choice,
			choices=exportTypeChoices,
		)
		self._exportTypeComboBox.Selection = _Cache.exportType

	def _onOutputTypeChange(self, evt: wx.CommandEvent):
		self._regularSpaceChk.Enable(not evt.Selection)

	def _onImport(self, _evt: wx.CommandEvent):
		filename = wx.FileSelector(
			# Translators: Label of a dialog to import a file.
			_("Import File"),
			wildcard="Text files (*.txt)|*.txt",  # Limit to .txt files
			flags=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
			parent=self,
		)
		if not filename:
			return
		try:
			with open(filename, encoding="UTF-8") as f:
				val = f.read()
		except OSError as e:
			gui.messageBox(
				# Translators: Dialog text presented when NVDA can't import a file.
				_("Error importing file: {e}").format(e.strerror),
				# Translators: the title of an error message dialog
				_("Error"),
				style=wx.OK | wx.ICON_ERROR,
				parent=self,
			)
			return
		else:
			self._brailleTextEdit.SetValue(val)
			self._inputTypeComboBox.Selection = 1

	def _exportToFile(self, contents: str, outputType: OutputType):
		wildcard = (
			"braille files (*.brf)|*.brf" if outputType == OutputType.BRF else "Text files (*.txt)|*.txt"
		)
		filename = wx.FileSelector(
			# Translators: Label of a dialog to export a file.
			_("Export File"),
			wildcard=wildcard,
			flags=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
			parent=self,
		)
		if not filename:
			return None
		encoding = "LATIN-1" if outputType != OutputType.UNICODE else "UTF-8"
		try:
			with open(filename, "wb") as f:
				f.write(contents.encode(encoding))
		except OSError as e:
			gui.messageBox(
				# Translators: Dialog text presented when NVDA can't export a file.
				_("Error exporting file: {e}").format(e.strerror),
				# Translators: the title of an error message dialog
				_("Error"),
				style=wx.OK | wx.ICON_ERROR,
				parent=self,
			)
			return None
		return filename

	def _enterActivatesOk_ctrlSActivatesApply(self, evt):
		if self._inputTypeComboBox.Selection > 0 and evt.KeyCode in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
			evt.Skip()
			return
		super()._enterActivatesOk_ctrlSActivatesApply(evt)

	def postInit(self):
		self._brailleTextEdit.SetFocus()

	def onOk(self, evt):
		value = self._brailleTextEdit.GetValue()
		inputType = InputType(self._inputTypeComboBox.GetSelection())
		outputType = OutputType(self._outputTypeComboBox.GetSelection())
		exportType = ExportType(self._exportTypeComboBox.GetSelection())
		regularSpace = self._regularSpaceChk.GetValue()
		try:
			match inputType:
				case InputType.DOTS:
					value = dotsToUnicode(value, regularSpace)
					value = postProcessUnicode(value, outputType)
				case InputType.TEXT_INPUT_TABLE | InputType.TEXT_OUTPUT_TABLE:
					lines = value.splitlines()
					table = getTranslationTable(inputType).fileName
					mode = louis.dotsIO | louis.ucBrl
					value = os.linesep.join(
						postProcessUnicode(translateText(line, [table], mode, regularSpace), outputType)
						for line in lines
					)
				case _:
					raise NotImplementedError
			if exportType == ExportType.FILE:
				_filename = self._exportToFile(value, outputType)
			else:
				copyToClip(value)
				# Translators: This is the message when unicode text has been copied to the clipboard.
				wx.CallLater(100, message, _("Result copied to clipboard ready for you to paste."))
		except ValueError as e:
			gui.messageBox(e.args[0], _("Error"), style=wx.OK | wx.ICON_ERROR, parent=self)
			return
		_Cache.inputType = inputType
		_Cache.outputType = outputType
		_Cache.regularSpace = regularSpace
		_Cache.exportType = exportType
		super().onOk(evt)
