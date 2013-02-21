# -*- coding: utf-8 -*-
# unicodeBrailleInput Global Plugin for NVDA
# Copyright (C) 2013 Mesar Hameed <mesar.hameed@gmail.com>, Patrick ZAJDA <patrick@zajda.fr>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: NVDA+Ctrl+u

import sys
import globalPluginHandler
import addonHandler

# We initialize translations.
addonHandler.initTranslation()

def dots2uni(cells):
    """ Convert a braille to Unicode
	@param cells the braille cellules (I.E. 13457-12367-1457-17)
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
        out.append(chr(val))
    return "".join(out)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_brailleInput2Unicode(self, gesture):
		import interface
		import gui
		gui.mainFrame._popupSettingsDialog(interface.B2UDialog)
	script_brailleInput2Unicode.__doc__ = _("Enter letters in braille separated by a dash, then this script will convert them to text.")

	__gestures={
		"kb:NVDA+control+U": "brailleInput2Unicode",
	}
