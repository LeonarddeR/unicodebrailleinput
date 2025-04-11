# unicodeBrailleInput Global Plugin for NVDA interface
# Copyright (C) 2013-2025 Mesar Hameed, Patrick Zajda, Leonard de Ruijter
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import os
import re
from collections.abc import Generator
from enum import IntEnum

import addonHandler
import braille
import brailleInput
import gui
import gui.guiHelper
import louis
import wx
from api import copyToClip
from ui import message

# Initialize translations.
addonHandler.initTranslation()


invalidInputRegexp = re.compile(r"[^0-8-]+")


class InputType(IntEnum):
	DOTS = 0
	TEXT_OUTPUT_TABLE = 1
	TEXT_INPUT_TABLE = 2


class OutputType(IntEnum):
	UNICODE = 0
	ASCII = 1


BRF_TABLE = "text_nabcc.dis"


def getTranslationTables(inputType: InputType, outputType: OutputType) -> Generator[str, None, None]:
	if outputType == OutputType.ASCII:
		yield BRF_TABLE
	yield "braille-patterns.cti"
	if inputType == InputType.TEXT_INPUT_TABLE:
		yield brailleInput.handler.table.fileName
	elif inputType == InputType.TEXT_OUTPUT_TABLE:
		yield braille.handler.table.fileName


def translateText(
	text: str,
	tables: list[str],
	mode: int,
	regularSpace: bool = False,
) -> str:
	"""Convert text to Unicode braille
	@param text: the text to convert
	@param regularSpace: if True, space will be replaced by a regular one instead of the braille space
	@return: the result in Unicode
	"""
	text = text.replace("\0", "")
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

		inputTypeChoices = [
			# Translators: the label of an input type
			_("Braille dots (e.g. 1345-1236-145-1)"),
		]
		# Translators: the label of an input type
		label = _("Normal text according to {table}")
		inputTypeChoices.append(label.format(table=braille.handler.table.displayName))
		if brailleInput.handler.table == braille.handler.table and brailleInput.handler.table.output:
			inputTypeChoices.append(label.format(table=brailleInput.handler.table.displayName))
		self._inputTypeComboBox = sizerHelper.addLabeledControl(
			# Translators: the label of the combo box to choose the input type.
			_("Input &type"),
			wx.Choice,
			choices=inputTypeChoices,
		)
		self._inputTypeComboBox.Selection = 0
		outputTypeChoices = [
			# Translators: the label of an output type
			_("Unicode braille"),
			# Translators: the label of an output type
			_("ASCII braille (BRF)"),
		]
		self._outputTypeComboBox = sizerHelper.addLabeledControl(
			# Translators: the label of the radio box to choose the output type.
			_("output type"),
			wx.Choice,
			choices=outputTypeChoices,
		)
		self._outputTypeComboBox.Bind(wx.EVT_CHOICE, self._onOutputTypeChange)
		self._outputTypeComboBox.Selection = 0

		self._regularSpaceChk = wx.CheckBox(
			self,
			# Translators: Label for a checkbox, wether to use a regular space or the Braille unicode space.
			label=_("Convert Unicode Braille &space to ASCII space"),
		)
		self._regularSpaceChk.SetValue(False)
		sizerHelper.addItem(self._regularSpaceChk)

	def _onOutputTypeChange(self, evt: wx.CommandEvent):
		self._regularSpaceChk.Enable(not evt.Selection)

	def _onImport(self, _evt: wx.CommandEvent):
		filename = wx.FileSelector(
			# Translators: Label of a dialog to import a file.
			_("Import File"),
			default_extension="txt",
			flags=wx.FD_OPEN,
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
		regularSpace = self._regularSpaceChk.GetValue()
		try:
			match inputType:
				case InputType.DOTS:
					value = dotsToUnicode(value, regularSpace)
					if outputType == OutputType.ASCII:
						value = louis.translate(
							[BRF_TABLE, "unicode-braille.utb"],
							value,
						)[0]
				case InputType.TEXT_INPUT_TABLE | InputType.TEXT_OUTPUT_TABLE:
					lines = value.splitlines()
					tables = list(getTranslationTables(inputType, outputType))
					mode = louis.dotsIO | louis.ucBrl if outputType == OutputType.UNICODE else 0
					value = os.linesep.join(translateText(line, tables, mode, regularSpace) for line in lines)
				case _:
					raise NotImplementedError
			copyToClip(value)
			# Translators: This is the message when unicode text has been copied to the clipboard.
			wx.CallLater(100, message, _("Result copied to clipboard ready for you to paste."))
		except ValueError as e:
			gui.messageBox(e.args[0], _("Error"), style=wx.OK | wx.ICON_ERROR, parent=self)
			return
		super().onOk(evt)
