# -*- coding: utf-8 -*-
# unicodeBrailleInput Global Plugin for NVDA
# Copyright (C) 2013 Mesar Hameed <mesar.hameed@gmail.com>, Patrick ZAJDA <patrick@zajda.fr>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: NVDA+Ctrl+u

import globalPluginHandler
import addonHandler
import gui
import interface
import wx

# We initialize translations.
addonHandler.initTranslation()

try:
	from globalCommands import SCRCAT_TOOLS
except:
	SCRCAT_TOOLS = None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_TOOLS

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.tools = gui.mainFrame.sysTrayIcon.toolsMenu
		self.menuItem = self.tools.Append(wx.ID_ANY, _("Unicode Braille Input"), _("Show a dialog to write letters in numeric braille (e.g. 1345-1236-145-1) separated by dashes, then convert them to unicode braille characters."))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_brailleInput2Unicode, self.menuItem)

	def script_brailleInput2Unicode(self, gesture):
		gui.mainFrame._popupSettingsDialog(interface.B2UDialog)
	# Translators: Message presented when user performs input help for this shortcut.
	script_brailleInput2Unicode.__doc__ = _("Show a dialog to write letters in numeric braille (e.g. 1345-1236-145-1) separated by dashes, then this script will convert them to unicode braille characters.")

	def terminate(self):
		try:
			self.tools.RemoveItem(self.menuItem)
		except wx.PyDeadObjectError:
			pass

	__gestures={
		"kb:NVDA+control+U": "brailleInput2Unicode",
	}
