import os.path

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.


# Since some strings in `addon_info` are translatable,
# we need to include them in the .po files.
# Gettext recognizes only strings given as parameters to the `_` function.
# To avoid initializing translations in this module we simply roll our own "fake" `_` function
# which returns whatever is given to it as an argument.
def _(arg):
	return arg


# Add-on information variables
addon_info = {
	# add-on Name, internal for nvda
	"addon_name": "unicodeBrailleInput",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on
	# to be shown on installation and add-on information found in Add-ons Manager.
	"addon_summary": _("Unicode Braille Input"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description": _(
		"Displays a text field to type numeric braille "
		"(e.g. 1345-1236-145-1) and converts it into unicode braille characters."
	),
	# version
	"addon_version": "4.1.0",
	# Author(s)
	"addon_author": (
		"Mesar Hameed <mhameed@src.gnome.org>, "
		"Patrick ZAJDA <patrick@zajda.fr>, "
		"Leonard de Ruijter <alderuijter@gmail.com>"
	),
	# URL for the add-on documentation support
	"addon_url": "https://github.com/leonardder/unicodebrailleinput",
	# URL for the add-on repository where the source code can be found
	"addon_sourceURL": "https://github.com/leonardder/unicodebrailleinput",
	# Documentation file name
	"addon_docFileName": "readme.html",
	# Minimum NVDA version supported
	"addon_minimumNVDAVersion": "2023.1",
	# Last NVDA version supported/tested
	"addon_lastTestedNVDAVersion": "2025.1",
	# Add-on update channel (default is None, denoting stable releases,
	# and for development releases, use "dev".)
	# Do not change unless you know what you are doing!
	"addon_updateChannel": None,
	# Add-on license such as GPL 2
	"addon_license": None,
	# URL for the license document the ad-on is licensed under
	"addon_licenseURL": None,
}

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "unicodeBrailleInput", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []

# Base language for the NVDA add-on
baseLanguage = "en"

# Markdown extensions for add-on documentation
# Most add-ons do not require additional Markdown extensions.
# If you need to add support for markup such as tables, fill out the below list.
# Extensions string must be of the form "markdown.extensions.extensionName"
# e.g. "markdown.extensions.tables" to add tables.
markdownExtensions = []
