# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import (
	AddonInfo,
	BrailleTables,
	SpeechDictionaries,
	SymbolDictionaries,
)
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name="unicodeBrailleInput",
	addon_summary=_("Unicode Braille Input"),
	addon_description=_("Utilities to convert text to Unicode braille"),
	addon_version="5.0.2",
	addon_changelog=_(""),
	addon_author=(
		"Leonard de Ruijter <alderuijter@gmail.com>, "
		"Mesar Hameed <mhameed@src.gnome.org>, "
		"Patrick ZAJDA <patrick@zajda.fr>"
	),
	addon_url="https://github.com/leonardder/unicodebrailleinput",
	addon_sourceURL="https://github.com/leonardder/unicodebrailleinput",
	addon_docFileName="readme.html",
	addon_minimumNVDAVersion="2024.3",
	addon_lastTestedNVDAVersion="2026.1",
	addon_updateChannel=None,
	addon_license=None,
	addon_licenseURL=None,
)

pythonSources: list[str] = ["addon/globalPlugins/unicodeBrailleInput/*.py"]
i18nSources: list[str] = pythonSources + ["buildVars.py"]
excludedFiles: list[str] = []
baseLanguage: str = "en"
markdownExtensions: list[str] = []
brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}
speechDictionaries: SpeechDictionaries = {}
