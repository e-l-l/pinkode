# Pinkode — A Pink color theme

Two VS Code themes built around **raspberry pink** as the load-bearing accent — a near-black noir and a WCAG-AA cream-and-rose light, sharing a common identity.

- **Pinkode — Noir** · designed for late nights.
- **Pinkode — Light** · AA-tuned, designed for morning light.

## Install

1. Open the Extensions view (`Cmd+Shift+X` / `Ctrl+Shift+X`)
2. Search for `Pinkode`
3. Install
4. `Cmd+K Cmd+T` (or `Ctrl+K Ctrl+T`) → pick **Pinkode — Noir** or **Pinkode — Light**

Or from a `.vsix`:

```sh
code --install-extension pinkode-0.2.0.vsix
```

## Noir — palette

### Surfaces — black + greys

| Token         | Hex       | Role                         |
| ------------- | --------- | ---------------------------- |
| Void          | `#050507` | Window backdrop              |
| Activity Bar  | `#08080B` | Deepest chrome               |
| Editor        | `#0D0D11` | Main canvas                  |
| Sidebar       | `#101015` | File tree, panels            |
| Elevated      | `#15151B` | Active tab, breadcrumb       |
| Input / Hover | `#1A1A22` | Form fields, hover           |

### Accents — the pinks

| Token       | Hex       | Role                          |
| ----------- | --------- | ----------------------------- |
| Hot Pink    | `#FF3D8C` | Keywords · selection · brand  |
| Magenta     | `#FF2DA0` | Tags · markup                 |
| Neon Pink   | `#FF5FA8` | Operators                     |
| Rose        | `#F06292` | Hover · borders               |
| Blush       | `#FF9CC2` | Parameters · attributes       |
| Pastel Pink | `#FFB3D1` | Properties · selected text    |
| Dust Rose   | `#D18BA7` | Punctuation                   |

### Complements — for syntax range

| Token    | Hex       | Role                        |
| -------- | --------- | --------------------------- |
| Lavender | `#C4A3FF` | Functions · constants · AI  |
| Sky      | `#8DD6FF` | Types · classes             |
| Mint     | `#9EEBCF` | Regex · added · success     |
| Peach    | `#FFB088` | Strings · warnings          |
| Amber    | `#FFD28A` | Numbers · modified · find   |
| Whisper  | `#F4E4EC` | Primary text                |

### Semantic

| Token   | Hex       |
| ------- | --------- |
| Error   | `#FF3D6D` |
| Warning | `#FFB088` |
| Info    | `#8DD6FF` |
| Success | `#9EEBCF` |

## Light — palette (AA)

Every syntax token clears WCAG AA (≥4.5:1) against the editor canvas `#FFFAFD`. Pastel pink is reserved for surfaces — never used as text.

### Surfaces — cream + rose

| Token         | Hex       | Role                           |
| ------------- | --------- | ------------------------------ |
| Petal         | `#F9E1EA` | Window backdrop                |
| Activity Bar  | `#F7DDE8` | Deepest chrome                 |
| Whisper       | `#FFFAFD` | Main editor canvas             |
| Sidebar       | `#FBECF2` | File tree                      |
| Panel         | `#FDF2F6` | Panel · terminal               |
| Elevated      | `#FFFFFF` | Active tab inner · breadcrumb  |
| Input / Hover | `#F4DBE5` | Form fields, hover             |

### Accents — the pinks (AA-safe except pastel)

| Token       | Hex       | Role · Contrast on `#FFFAFD`           |
| ----------- | --------- | -------------------------------------- |
| Raspberry   | `#BD1B57` | Keywords · brand · cursor · 5.88:1     |
| Magenta     | `#B8175A` | Tags · properties · 6.15:1             |
| Neon Pink   | `#C42466` | Operators · 5.37:1                     |
| Rose        | `#BE2E5E` | Status bar (white fg) · 5.44:1         |
| Blush       | `#9E3F66` | Parameters · attributes · 6.06:1       |
| Pastel Pink | `#F4A8C2` | **Surface only** — never used as text  |
| Dust Rose   | `#82475E` | Punctuation · 6.75:1                   |

### Complements — for syntax range

| Token  | Hex       | Role                       |
| ------ | --------- | -------------------------- |
| Plum   | `#7C3AED` | Functions · constants · AI |
| Teal   | `#0E7490` | Types · classes            |
| Forest | `#15803D` | Regex · added · success    |
| Burnt  | `#B45309` | Strings · warnings · find  |
| Amber  | `#92400E` | Numbers · modified         |
| Ink    | `#2A0A17` | Primary text · 17.6:1      |

### Semantic

| Token   | Hex       |
| ------- | --------- |
| Error   | `#C81E3A` |
| Warning | `#B45309` |
| Info    | `#0E7490` |
| Success | `#15803D` |

## Syntax token map (both variants)

| Role                          | Noir         | Light       |
| ----------------------------- | ------------ | ----------- |
| Keywords, control flow        | Hot Pink     | Raspberry   |
| `this` / `self` (italic)      | Hot Pink     | Raspberry   |
| Functions, function calls     | Lavender     | Plum        |
| Types, classes, interfaces    | Sky          | Teal        |
| Properties (`.scrollLeft`)    | Pastel Pink  | Magenta     |
| Parameters (italic)           | Blush        | Blush (dk)  |
| Strings                       | Peach        | Burnt       |
| Numbers                       | Amber        | Amber (dk)  |
| Language constants            | Lavender     | Plum        |
| Operators                     | Neon Pink    | Neon (dk)   |
| Punctuation                   | Dust Rose    | Dust Rose   |
| Comments (italic)             | `#6A5A64`    | `#8E5C70`   |
| Regex, escapes                | Mint         | Forest      |
| Tags                          | Magenta      | Magenta     |
| Attributes                    | Blush        | Blush (dk)  |
| Diff added                    | Mint         | Forest      |
| Diff removed                  | Error        | Error       |
| Diff modified                 | Amber        | Amber (dk)  |
| AI ghost text / inline hints  | Lavender     | Plum        |

## Screenshots

> Screenshots TODO. Add captures to `screenshots/preview.png` (Noir) and `screenshots/preview-light.png` (Light) and reference here.

## License

MIT — see [`LICENSE`](./LICENSE).
