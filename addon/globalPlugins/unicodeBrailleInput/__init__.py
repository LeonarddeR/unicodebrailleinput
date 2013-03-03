# -*- coding: utf-8 -*-
# unicodeBrailleInput Global Plugin for NVDA
# Copyright (C) 2013 Mesar Hameed <mesar.hameed@gmail.com>, Patrick ZAJDA <patrick@zajda.fr>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: NVDA+Ctrl+u

import globalPluginHandler
import addonHandler

# We initialize translations.
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_brailleInput2Unicode(self, gesture):
		import interface
		import gui
		gui.mainFrame._popupSettingsDialog(interface.B2UDialog)
	# Translators: Message presented when user performs input help for this shortcut.
	script_brailleInput2Unicode.__doc__ = _("Show a dialog to write letters in numeric braille (e.g. 1345-1236-145-1) separated by dashes, then this script will convert them to unicode braille characters.")

	__gestures={
		"kb:NVDA+control+U": "brailleInput2Unicode",
	}
