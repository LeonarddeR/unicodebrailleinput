# -*- coding: utf-8 -*-
# unicodeBrailleInput Global Plugin for NVDA interface
# Copyright (C) 2013 Mesar Hameed <mesar.hameed@gmail.com>, Patrick ZAJDA <patrick@zajda.fr>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import sys
import addonHandler
import gui
import wx
from re import compile
from ui import message
from api import copyToClip

# Initialize translations.
addonHandler.initTranslation()

# Check python version.
PY2 = sys.version_info[0] == 2

conv=None
# name of function is unichr for python2 and chr for python3.
if PY2:
	conv = unichr
else:
	conv = chr

invalidInputRegexp = compile('[^0-8-]+')
def dots2uni(cells, regularSpace = False):
	""" Convert a braille to Unicode
	@param cells the braille cells (I.E. 13457-12367-1457-17)
	@param regularSpace boolean if True, space will be replaced by a regulare one instead of the braille space
	@return the result in Unicode (NVDA in our example)
	"""
	cells = cells.strip()
	invalidStrings = invalidInputRegexp.findall(cells)
	if cells.isspace() or cells == "":
		# Translators: the user entered an empty string or only whitespace and this is the error message to show the mistakes.
		raise ValueError(_("Unexpected input: '%s', whitespace or empty string is not allowed.") % "', '".join(invalidStrings))
	if invalidStrings:
		# Translators: the user entered an unexpected string and this is the error message to show the mistakes.
		raise ValueError(_("Unexpected input: '%s', only dots 0 to 8 and - are allowed.") % "', '".join(invalidStrings))
	cells = cells.split('-')
	out = []
	for cell in cells:
		val = 0
		if '1' in cell: val |= 1
		if '2' in cell: val |= 2
		if '3' in cell: val |= 4
		if '4' in cell: val |= 8
		if '5' in cell: val |= 0x10
		if '6' in cell: val |= 0x20
		if '7' in cell: val |= 0x40
		if '8' in cell: val |= 0x80
		if val:
			val |= 0x2800
			out.append(conv(val))
		else:
			out.append(u" " if regularSpace else conv(0x2800))
	return "".join(out)

class B2UDialog(gui.SettingsDialog):
	# Translators: The title of the dialog.
	title = _("Convert Braille to Unicode")
	def __init__(self, parent):
		super(B2UDialog, self).__init__(parent)

	def makeSettings(self, sizer):
		brailleTextSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label of the edit field.
		brailleTextLabel = wx.StaticText(self, label=_("Enter text in numeric braille:"))
		brailleTextSizer.Add(brailleTextLabel)
		self._brailleTextEdit = wx.TextCtrl(self, -1)
		brailleTextSizer.Add(self._brailleTextEdit)
		self._regularSpaceChk = wx.CheckBox(self,
		# Translators: wether to use a regular space or the Braille one
			label = _("Convert Unicode Braille space to ASCII space"))
		self._regularSpaceChk.SetValue(False)
		brailleTextSizer.Add(self._regularSpaceChk)
		sizer.Add(brailleTextSizer)

	def postInit(self):
		self._brailleTextEdit.SetFocus()

	def onOk(self, event):
		super(B2UDialog, self).onOk(event)
		value = self._brailleTextEdit.GetValue()
		regularSpace = self._regularSpaceChk.GetValue()
		try:
			value = dots2uni(value, regularSpace)
			copyToClip(value)
			# Translators: This is the message when unicode text has been copied to the clipboard.
			wx.CallLater(100, message, _("Unicode text copied to clipboard ready for you to paste."))
		except ValueError as e:
			wx.CallLater(100, message, e.message)
