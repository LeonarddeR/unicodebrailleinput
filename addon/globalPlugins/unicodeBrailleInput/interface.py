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

def dots2uni(cells):
    """ Convert a braille to Unicode
	@param cells the braille cells (I.E. 13457-12367-1457-17)
	@return the result in Unicode (NVDA in our example)
	"""
    cells = cells.strip().split('-')
    out = []
    for cell in cells:
        val = 0x2800
        if '1' in cell: val |= 1
        if '2' in cell: val |= 2
        if '3' in cell: val |= 4
        if '4' in cell: val |= 8
        if '5' in cell: val |= 0x10
        if '6' in cell: val |= 0x20
        if '7' in cell: val |= 0x40
        if '8' in cell: val |= 0x80
        out.append(conv(val))
    return "".join(out)

class B2UDialog(gui.SettingsDialog):
	# Translators: The title of the dialog.
	title = _("Convert Braille to Unicode")
	def __init__(self, parent):
		super(B2UDialog, self).__init__(parent)

	def makeSettings(self, sizer):
		brailleTextSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label of the edit field.
		brailleTextLabel = wx.StaticText(self, label=_("Enter text in braille:"))
		brailleTextSizer.Add(brailleTextLabel)
		self._brailleTextEdit = wx.TextCtrl(self, -1)
		brailleTextSizer.Add(self._brailleTextEdit)
		sizer.Add(brailleTextSizer)

	def postInit(self):
		self._brailleTextEdit.SetFocus()

	def onOk(self, event):
		super(B2UDialog, self).onOk(event)
