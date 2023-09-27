# unicodeBrailleInput Global Plugin for NVDA interface
# Copyright (C) 2013-2023 Mesar Hameed, Patrick Zajda, Leonard de Ruijter
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import addonHandler
import gui
import wx
from re import compile
from ui import message
from api import copyToClip
import config
import os
import louis
import brailleTables


# Initialize translations.
addonHandler.initTranslation()


invalidInputRegexp = compile("[^0-8-]+")


def textToUnicode(text: str, regularSpace: bool = False) -> str:
	"""Convert text to Unicode braille
	@param text: the text to convert
	@param regularSpace: if True, space will be replaced by a regular one instead of the braille space
	@return: the result in Unicode
	"""
	text = text.replace("\0", "")
	text = louis.translate(
		[
			os.path.join(brailleTables.TABLES_DIR, config.conf["braille"]["inputTable"]),
			"braille-patterns.cti",
		],
		text,
		mode=louis.dotsIO,
	)[0]
	out = "".join(chr(0x2800 | ord(cell) & 255) for cell in text)
	if regularSpace:
		out = out.replace("\u2800", " ")
	return out


def dotsToUnicode(cells: str, regularSpace: bool = False) -> str:
	"""Convert braille to Unicode
	@param cells: the braille cells (I.E. 13457-12367-1457-17)
	@param regularSpace: if True, space will be replaced by a regular one instead of the braille space
	@return: the result in Unicode (NVDA in our example)
	"""
	cells = cells.translate(
		{
			ord("f"): "1",
			ord("d"): "2",
			ord("s"): "3",
			ord("j"): "4",
			ord("k"): "5",
			ord("l"): "6",
			ord("a"): "7",
			ord(";"): "8",
		}
	).strip()
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
	title = _("Convert Braille to Unicode")

	def makeSettings(self, sizer):
		sizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=sizer)
		self._brailleTextEdit = sizerHelper.addLabeledControl(
			# Translators: the label of the edit field.
			_("&Input:"),
			wx.TextCtrl,
		)

		inputTypeChoices = [
			# Translators: the label of an input type
			_("Braille &dots (e.g. 1345-1236-145-1)"),
			# Translators: the label of an input type
			_("Normal &text according to %s")
			% (brailleTables.getTable(config.conf["braille"]["inputTable"]).displayName),
		]
		self._inputTypeRadioBox = sizerHelper.addItem(
			wx.RadioBox(
				self,
				# Translators: the label of the radio box to choose the input type.
				label=_("Input type"),
				choices=inputTypeChoices,
			)
		)

		self._regularSpaceChk = wx.CheckBox(
			self,
			# Translators: Label for a checkbox, wether to use a regular space or the Braille unicode space.
			label=_("Convert Unicode Braille &space to ASCII space"),
		)
		self._regularSpaceChk.SetValue(False)
		sizerHelper.addItem(self._regularSpaceChk)

	def postInit(self):
		self._brailleTextEdit.SetFocus()

	def onOk(self, event):
		value = self._brailleTextEdit.GetValue()
		type = self._inputTypeRadioBox.GetSelection()
		regularSpace = self._regularSpaceChk.GetValue()
		try:
			if not type:
				value = dotsToUnicode(value, regularSpace)
			else:
				value = textToUnicode(value, regularSpace)
			copyToClip(value)
			# Translators: This is the message when unicode text has been copied to the clipboard.
			wx.CallLater(100, message, _("Unicode text copied to clipboard ready for you to paste."))
		except ValueError as e:
			gui.messageBox(e.args[0], _("Error"), style=wx.OK | wx.ICON_ERROR, parent=self)
			return
		super().onOk(event)
