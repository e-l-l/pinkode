# CLAUDE.md

Context for future Claude sessions working on this repo.

## Project

VS Code color theme extension. Publishes three themes:

- `pinkode - noir` (dark, `vs-dark`)
- `pinkode - haze` (low-contrast dark, `vs-dark`) — hand-authored soft sibling of noir; lifted grey surfaces, pastel pinks, dimmed complements, but status signals stay loud
- `pinkode - light` (light, `vs`, WCAG-AA syntax)

No source code, no build step, no tests — just JSON themes + manifest.

## Layout

- `themes/Pinkode - Pink color theme-color-theme.json` — noir theme
- `themes/Pinkode - Haze-color-theme.json` — haze theme (low-contrast noir)
- `themes/Pinkode - Hot Pink Light-color-theme.json` — light theme
- `CONTEXT.md` — glossary: flavor vocabulary (Flavor / Surface / Accent / Complement / Signal) and the noir↔haze relationship
- `package.json` — `contributes.themes[]` registers both files; `version` is the published version
- `README.md` — palette tables: every named color, role, and (for light) contrast ratio
- `CHANGELOG.md` — Keep-a-Changelog format
- `screenshots/` — preview images referenced by README

## Common tasks

- **Test locally**: open repo in VS Code → press `F5` to launch Extension Development Host → `Cmd+K Cmd+T` to switch themes. Edits to the theme JSON apply live in the host window.
- **Package**: `vsce package` → produces `pinkode-<version>.vsix`. Install with `code --install-extension pinkode-<version>.vsix`.
- **Release**: bump `version` in `package.json`, add a CHANGELOG entry, commit, then `vsce publish`.

## Conventions

- Light theme syntax tokens must clear **WCAG-AA (≥4.5:1)** on the editor canvas `#FFFAFD`. README annotates the ratio for every accent.
- Pastel `#F4A8C2` is **surface only** — never used as text.
- Both themes share the complement palette (Plum/Teal/Forest/Burnt/Amber/Ink). Pink accents differ per variant.
- The SCM commit-message input is a mini-editor: its placeholder is styled by `editorGhostText.foreground`, **not** `input.placeholderForeground`.

## Doc-sync rule

After any change, scan and update docs if — and only if — the change actually contradicts or adds to what's written.

**Update docs when:**

- A documented color hex / token name / role in `README.md` is changing.
- A user-visible behavior is added, fixed, or removed → add an Unreleased entry in `CHANGELOG.md`.
- The user explicitly asks for a doc change / addition / deletion.
- A file path, command, or version referenced in `README.md` or `package.json` changes.

**Do not touch docs when:**

- Editing workbench color keys that aren't listed in the README palette tables.
- Reformatting JSON with no semantic change.
- Swapping screenshots or other non-doc assets.

**Workflow**: after editing code, grep `README.md` and `CHANGELOG.md` for any hex / key / term being changed. If a match is found, update the matching prose; otherwise leave docs alone.

## Gotchas

- Theme filenames contain spaces — quote paths when scripting.
- Old `.vsix` artifacts may sit at repo root from prior packaging. Don't re-commit them unless deliberate.
