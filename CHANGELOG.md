# Change Log

All notable changes to the "pinkode" extension will be documented in this file.

Check [Keep a Changelog](http://keepachangelog.com/) for recommendations on how to structure this file.

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

- Light variant (`Pinkode — Hot Pink Day`) deferred.
- Marketplace icon PNG + gallery banner.
- Screenshots captured + committed under `screenshots/`.
- Italic-haters toggle (variant without italics).

## [Unreleased]

- Initial scaffold.
