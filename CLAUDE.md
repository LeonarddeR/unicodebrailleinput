# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Unicode Braille Input: NVDA add-on that converts typed braille into Unicode braille, ASCII braille (BRF) or NABCC, and copies the result to the clipboard or writes it to a file. Input is either numeric dot patterns (`1345-1236-145-1`) or normal text translated through the current braille input or output table. Min NVDA 2024.3, Python 3.13.

Sibling source repos (paths relative to this repo):

* `..\nvda` — NVDA source. Required, not optional: `ty` resolves every NVDA import (`braille`, `brailleInput`, `brailleTables`, `louis`, `gui`, `scriptHandler`, …) against `..\nvda\source`, and picks up the `_()` / `pgettext()` translation builtins from `..\nvda\source\__builtins__.pyi`. Look there for any NVDA API signature before guessing.

## Build / Lint

Toolchain: `uv` + SCons. Run from repo root.

| Task | Command |
|---|---|
| Install dev deps | `uv sync` |
| Build add-on (`.nvda-addon`) | `uv run scons` |
| Translation template | `uv run scons pot` |
| Merge POT | `uv run scons mergePot` |
| Dev (timestamped) build | `uv run scons dev=1` |
| Lint + format + type check | `uv run prek run --all-files` (ruff + ty, configured in `prek.toml` / `pyproject.toml`) |
| Type check only | `uv run ty check` |
| Clean | `uv run scons -c` |

Git hooks run via **prek** (Rust pre-commit alternative; config in `prek.toml`). Run `uv run prek install -f` once to wire the git hooks.

Type checking uses **ty** (`[tool.ty]` in `pyproject.toml`), scoped to `addon/` + `buildVars.py`. `wx` resolves from the `wxPython` dev dependency, pinned to the 4.2.x series NVDA bundles rather than the latest release.

Indentation is **tabs** (ruff `indent-style=tab`, `W191` ignored). Line length 110.

## Layout

Two source files under `addon/globalPlugins/unicodeBrailleInput/`:

* `__init__.py` — `GlobalPlugin`: adds the Tools menu item, binds the `NVDA+control+i` gesture, and pops up the dialog. Returns early on secure screens.
* `interface.py` — `BrailleInputDialog` (a `gui.SettingsDialog`) plus the conversion functions `dotsToUnicode`, `translateText` and `postProcessUnicode`, and the three `DisplayStringIntEnum` subclasses (`InputType`, `OutputType`, `ExportType`) that populate the dialog's combo boxes and carry their own translated labels.

The conversion functions take and return plain strings and touch no wx or NVDA GUI state; keep them that way.

`braille.handler` is typed `BrailleHandler | None` in NVDA, so narrow it with `assert braille.handler is not None` before use. Reserve `# ty: ignore[rule]` for genuine stub imprecision.

## buildVars / manifest

`buildVars.py` is the single source of truth for add-on metadata (name, version, NVDA min/lastTested, included files). `manifest.ini.tpl` and `manifest-translated.ini.tpl` are rendered by SCons via `site_scons/site_tools/NVDATool`. Bump `addon_version` and `addon_lastTestedNVDAVersion` here, not in the generated `manifest.ini`.

## Translations

User-facing strings via `_()` / `pgettext()` / `ngettext()` / `npgettext()` with a preceding `# Translators:` comment. `uv run scons pot` regenerates `unicodeBrailleInput.pot`.

Translations round-trip weekly through the shared [nvdaAddons Crowdin project](https://crowdin.com/project/nvdaaddons) via `.github/workflows/crowdinL10n.yml`. The workflow uploads `unicodeBrailleInput.pot` (interface) and `unicodeBrailleInput.xliff` (generated from `readme.md`), then commits anything translated past 50% back into `addon/locale/` and `addon/doc/`. It runs only from the default branch and needs the `CROWDIN_TOKEN` repository secret.
