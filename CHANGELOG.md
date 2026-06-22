# Change Log

All notable changes to the "pinkode" extension will be documented in this file.

Check [Keep a Changelog](http://keepachangelog.com/) for recommendations on how to structure this file.

## [0.3.0] - 2026-06-23

### Added

- **pinkode - haze**: a third flavor — a low-contrast sibling of Noir for longer, lower-strain sessions. Same hue identity, deliberately smaller contrast deltas. Hand-authored as an independent theme (no build step); see `CONTEXT.md` for the flavor vocabulary.
  - Surfaces lifted off black toward grey: editor canvas `#0D0D11` → `#1C1C22`, ramp from Void `#131318` up to Input/Hover `#2C2C36`.
  - Primary text pulled off pure-white: `#F4E4EC` → `#D8CDD4` (~9:1 on canvas, down from ~15:1).
  - Pinks desaturated to pastel across syntax **and** chrome (cursor, badges, borders, buttons, selection): Hot Pink `#FF3D8C` → `#FF85B5`, Magenta tags `#FF2DA0` → `#FF6FBE`, Neon `#FF5FA8` → `#FF96C0`, Blush `#FF9CC2` → `#FFB6D0`, Pastel `#FFB3D1` → `#FFC8DD`, Dust Rose `#D18BA7` → `#C79FAF`.
  - Complements dimmed but kept distinct: Lavender `#C4A3FF` → `#B6A0E8`, Sky `#8DD6FF` → `#93C9EC`, Mint `#9EEBCF` → `#A6DEC6`, Peach `#FFB088` → `#ECAC8E`, Amber `#FFD28A` → `#E8C794`.
  - Status signals stay at full Noir strength — error/warning/info/success, find match, git decorations, and diff colors are exempt from softening so alerts still register.
- Third registered theme under `contributes.themes` — `pinkode - haze` (`vs-dark`).
- New keywords: `haze`, `low contrast`.

## [0.2.3] - 2026-05-18

### Changed

- Dark theme: softened active list selection in tree views (Source Control, Explorer). `list.focusOutline` dropped from solid `#FF3D8C` to 40% alpha `#FF3D8C66`, and `list.activeSelectionBackground` from `#FF3D8C1F` to `#FF3D8C14`. Selection remains legible without dominating the row.

## [0.2.2] - 2026-05-17

### Fixed

- Light theme: SCM commit message placeholder no longer renders in saturated Plum. `editorGhostText.foreground` retoned to muted rose `#A87890` so the placeholder (and inline-completion ghost text) recedes against the pink canvas. `editorHint.foreground` unchanged.

## [0.2.1] - 2026-05-16

### Changed

- Theme labels simplified: `Pinkode — Hot Pink Noir` → `pinkode - noir`, `Pinkode — Hot Pink Light` → `pinkode - light`.
- `displayName` → `pinkode`.
- Tightened extension description and README intro.
- README: new "Open source" section linking the GitHub repo and inviting contributions.

## [0.2.0] - 2026-05-16

### Added

- **Pinkode — Hot Pink Light**: a sibling light theme with WCAG-AA syntax tokens against the `#FFFAFD` editor canvas. Every accent annotated with its contrast ratio.
- Six AA-tuned pink accents: Raspberry `#BD1B57` (5.88:1), Magenta `#B8175A` (6.15:1), Neon Pink `#C42466` (5.37:1), Rose `#BE2E5E` (5.44:1, status bar with white fg), Blush `#9E3F66` (6.06:1), Dust Rose `#82475E` (6.75:1). Pastel Pink `#F4A8C2` reserved for surface use only — never text.
- Complement palette unchanged from dark: Plum `#7C3AED`, Teal `#0E7490`, Forest `#15803D`, Burnt `#B45309`, Amber `#92400E`, Ink `#2A0A17` (17.6:1 primary text).
- Surfaces layered cream-and-rose: Petal `#F9E1EA`, Activity Bar `#F7DDE8`, Whisper `#FFFAFD`, Sidebar `#FBECF2`, Panel `#FDF2F6`, Elevated `#FFFFFF`, Input/Hover `#F4DBE5`.
- Status bar uses Rose `#BE2E5E` with white foreground (5.44:1) — replaces the dark variant's near-black status bar so the light theme has a distinct identity.
- Bracket pair colorization (6 levels) using mock complements: raspberry → plum → teal → forest → burnt → amber.
- Terminal ANSI 16 derived from the AA palette; every slot ≥ 4.5:1 on terminal bg `#FDF2F6`.
- Selection / line-highlight tints kept subtle per design comp: `~7%` line, `~12%` selection.
- Italics carry from the dark family: comments, `variable.language` (this/self/super), parameters, decorators.

### Changed

- `displayName` description updated to cover both themes.
- New keywords: `light`, `wcag`.
- Package `version` → `0.2.0`.

### Metadata

- Two registered themes under `contributes.themes` — Pinkode — Hot Pink Noir (`vs-dark`) and Pinkode — Hot Pink Light (`vs`).

## [0.1.0] - 2026-05-15

### Changed

- Full theme rewrite to **Hot Pink Noir** spec: 6 surfaces, 6 pinks, 6 complements.
- Comprehensive workbench colors (~150 keys) including activity bar, sidebar, tabs, status bar, terminal ANSI 16, git decorations, diff editor, peek view, quick input, notifications, minimap, symbol icons.
- Syntax token rewrite: keywords hot pink, functions lavender, types sky, strings peach, regex mint, parameters blush italic, comments fg-muted italic, language vars (`this`/`self`) hot pink italic.
- Bracket pair colorization with 6-step palette: hot pink → lavender → sky → blush → mint → amber.
- Cursor color hot pink `#FF3D8C`.
- Selection: subtle pink tints. Line highlight: rgba(255, 61, 140, 0.06).
- Search match: amber border + amber range highlight.
- AI ghost text / inline suggestions: lavender.
- Status bar: near-black background, pink accents on remote / prominent / error items only.
- Terminal ANSI 16 fully themed (magenta=hot pink, cyan=lavender, green=mint, yellow=amber).
- Activity bar badge: hot pink with dark text (replaces previous `#007acc` blue).

### Metadata

- `displayName` → `Pinkode — Hot Pink Noir`.
- New keywords: `theme`, `dark`, `pink`, `hot pink`, `noir`, `color-theme`.

### Future

- Marketplace icon PNG + gallery banner.
- Screenshots captured + committed under `screenshots/` (Noir + Light).
- Italic-haters toggle (variant without italics).
- `hc-light` high-contrast variant.

## [Unreleased]

- Initial scaffold.
