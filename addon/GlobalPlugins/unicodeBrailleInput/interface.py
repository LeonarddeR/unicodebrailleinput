# -*- coding: utf-8 -*-
# unicodeBrailleInput Global Plugin for NVDA interface
# Copyright (C) 2013 Mesar Hameed <mesar.hameed@gmail.com>, Patrick ZAJDA <patrick@zajda.fr>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import addonHandler
import gui
import wx

# We initialize translations.
addonHandler.initTranslation()

class B2UDialog(gui.SettingsDialog):
	title = _("Convert Braille to Unicode")
	def __init__(self, parent):
		super(B2UDialog, self).__init__(parent)

	def makeSettings(self, sizer):
		brailleTextSizer = wx.BoxSizer(wx.HORIZONTAL)
		brailleTextLabel = wx.StaticText(self, label=_("Enter text in braille:"))
		brailleTextSizer.Add(brailleTextLabel)
		self._brailleTextEdit = wx.TextCtrl(self, -1)
		brailleTextSizer.Add(self._brailleTextEdit)
		sizer.Add(brailleTextSizer)

	def postInit(self):
		self._brailleTextEdit.SetFocus()

	def onOk(self, event):
		super(B2UDialog, self).onOk(event)
