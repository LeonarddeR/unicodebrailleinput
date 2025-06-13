# unicodeBrailleInput Global Plugin for NVDA
# Copyright (C) 2013-2025 Mesar Hameed, Patrick Zajda, Leonard de Ruijter
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: NVDA+Ctrl+i

import addonHandler
import globalPluginHandler
import globalVars
import gui
import wx
from globalCommands import SCRCAT_TOOLS
from scriptHandler import script

from . import interface

# We initialize translations.
addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = SCRCAT_TOOLS

	def __init__(self):
		super().__init__()
		if globalVars.appArgs.secure:
			return
		self.tools = gui.mainFrame.sysTrayIcon.toolsMenu
		self.menuItem = self.tools.Append(
			wx.ID_ANY,
			# Translators: name of menu item.
			_("Un&icode Braille Input..."),
			# Translators: menu item tool tip text.
			_("Displays a dialog to enter braille in numeric form."),
		)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_brailleInput2Unicode, self.menuItem)

	@script(
		# Translators: Message presented when user performs input help for this shortcut.
		description=_("Displays a dialog to enter braille in numeric form."),
		gesture="kb:NVDA+control+i",
	)
	def script_brailleInput2Unicode(self, gesture):  # noqa: ARG002
		gui.mainFrame._popupSettingsDialog(interface.BrailleInputDialog)

	def terminate(self):
		try:
			self.tools.Remove(self.menuItem)
		except Exception:
			pass
		super().terminate()
