# pinkode

[![Version](https://img.shields.io/visual-studio-marketplace/v/e-l-l.pinkode?color=BD1B57&label=marketplace)](https://marketplace.visualstudio.com/items?itemName=e-l-l.pinkode)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/e-l-l.pinkode?color=BD1B57&label=installs)](https://marketplace.visualstudio.com/items?itemName=e-l-l.pinkode)
[![License: MIT](https://img.shields.io/badge/license-MIT-BD1B57.svg)](./LICENSE)

> A pink-forward VS Code theme. Two flavors — **Noir** for dark, **Light** for day. Raspberry pink does the heavy lifting; a curated complement palette covers the syntax range.

## Preview

| pinkode - noir | pinkode - light |
| :---: | :---: |
| ![pinkode noir](screenshots/preview-noir.png) | ![pinkode light](screenshots/preview-light.png) |
| near-black surfaces · bright pink accents | cream-and-rose surfaces · WCAG-AA syntax |

## Install

1. Open the Extensions view (`Cmd+Shift+X` / `Ctrl+Shift+X`)
2. Search for `Pinkode`
3. Install
4. `Cmd+K Cmd+T` (or `Ctrl+K Ctrl+T`) → pick **pinkode - noir** or **pinkode - light**

Or from a `.vsix`:

```sh
code --install-extension pinkode-0.2.1.vsix
```

## Palette

<details>
<summary><strong>Noir</strong> — six surfaces, six pinks, six complements</summary>

### Surfaces — black + greys

| | Token | Hex | Role |
| :-: | --- | --- | --- |
| ![#050507](https://placehold.co/15x15/050507/050507.png) | Void          | `#050507` | Window backdrop         |
| ![#08080B](https://placehold.co/15x15/08080B/08080B.png) | Activity Bar  | `#08080B` | Deepest chrome          |
| ![#0D0D11](https://placehold.co/15x15/0D0D11/0D0D11.png) | Editor        | `#0D0D11` | Main canvas             |
| ![#101015](https://placehold.co/15x15/101015/101015.png) | Sidebar       | `#101015` | File tree, panels       |
| ![#15151B](https://placehold.co/15x15/15151B/15151B.png) | Elevated      | `#15151B` | Active tab, breadcrumb  |
| ![#1A1A22](https://placehold.co/15x15/1A1A22/1A1A22.png) | Input / Hover | `#1A1A22` | Form fields, hover      |

### Accents — the pinks

| | Token | Hex | Role |
| :-: | --- | --- | --- |
| ![#FF3D8C](https://placehold.co/15x15/FF3D8C/FF3D8C.png) | Hot Pink    | `#FF3D8C` | Keywords · selection · brand |
| ![#FF2DA0](https://placehold.co/15x15/FF2DA0/FF2DA0.png) | Magenta     | `#FF2DA0` | Tags · markup                |
| ![#FF5FA8](https://placehold.co/15x15/FF5FA8/FF5FA8.png) | Neon Pink   | `#FF5FA8` | Operators                    |
| ![#F06292](https://placehold.co/15x15/F06292/F06292.png) | Rose        | `#F06292` | Hover · borders              |
| ![#FF9CC2](https://placehold.co/15x15/FF9CC2/FF9CC2.png) | Blush       | `#FF9CC2` | Parameters · attributes      |
| ![#FFB3D1](https://placehold.co/15x15/FFB3D1/FFB3D1.png) | Pastel Pink | `#FFB3D1` | Properties · selected text   |
| ![#D18BA7](https://placehold.co/15x15/D18BA7/D18BA7.png) | Dust Rose   | `#D18BA7` | Punctuation                  |

### Complements — for syntax range

| | Token | Hex | Role |
| :-: | --- | --- | --- |
| ![#C4A3FF](https://placehold.co/15x15/C4A3FF/C4A3FF.png) | Lavender | `#C4A3FF` | Functions · constants · AI |
| ![#8DD6FF](https://placehold.co/15x15/8DD6FF/8DD6FF.png) | Sky      | `#8DD6FF` | Types · classes            |
| ![#9EEBCF](https://placehold.co/15x15/9EEBCF/9EEBCF.png) | Mint     | `#9EEBCF` | Regex · added · success    |
| ![#FFB088](https://placehold.co/15x15/FFB088/FFB088.png) | Peach    | `#FFB088` | Strings · warnings         |
| ![#FFD28A](https://placehold.co/15x15/FFD28A/FFD28A.png) | Amber    | `#FFD28A` | Numbers · modified · find  |
| ![#F4E4EC](https://placehold.co/15x15/F4E4EC/F4E4EC.png) | Whisper  | `#F4E4EC` | Primary text               |

### Semantic

| | Token | Hex |
| :-: | --- | --- |
| ![#FF3D6D](https://placehold.co/15x15/FF3D6D/FF3D6D.png) | Error   | `#FF3D6D` |
| ![#FFB088](https://placehold.co/15x15/FFB088/FFB088.png) | Warning | `#FFB088` |
| ![#8DD6FF](https://placehold.co/15x15/8DD6FF/8DD6FF.png) | Info    | `#8DD6FF` |
| ![#9EEBCF](https://placehold.co/15x15/9EEBCF/9EEBCF.png) | Success | `#9EEBCF` |

</details>

<details>
<summary><strong>Light</strong> — AA-tuned, contrast ratios annotated</summary>

Every syntax token clears WCAG AA (≥4.5:1) on `#FFFAFD`. Every accent annotated with its contrast ratio. Pastel stays on surfaces — never text.

### Surfaces — cream + rose

| | Token | Hex | Role |
| :-: | --- | --- | --- |
| ![#F9E1EA](https://placehold.co/15x15/F9E1EA/F9E1EA.png) | Petal         | `#F9E1EA` | Window backdrop               |
| ![#F7DDE8](https://placehold.co/15x15/F7DDE8/F7DDE8.png) | Activity Bar  | `#F7DDE8` | Deepest chrome                |
| ![#FFFAFD](https://placehold.co/15x15/FFFAFD/FFFAFD.png) | Whisper       | `#FFFAFD` | Main editor canvas            |
| ![#FBECF2](https://placehold.co/15x15/FBECF2/FBECF2.png) | Sidebar       | `#FBECF2` | File tree                     |
| ![#FDF2F6](https://placehold.co/15x15/FDF2F6/FDF2F6.png) | Panel         | `#FDF2F6` | Panel · terminal              |
| ![#FFFFFF](https://placehold.co/15x15/FFFFFF/FFFFFF.png) | Elevated      | `#FFFFFF` | Active tab inner · breadcrumb |
| ![#F4DBE5](https://placehold.co/15x15/F4DBE5/F4DBE5.png) | Input / Hover | `#F4DBE5` | Form fields, hover            |

### Accents — the pinks (AA-safe except pastel)

| | Token | Hex | Role · Contrast on `#FFFAFD` |
| :-: | --- | --- | --- |
| ![#BD1B57](https://placehold.co/15x15/BD1B57/BD1B57.png) | Raspberry   | `#BD1B57` | Keywords · brand · cursor · 5.88:1    |
| ![#B8175A](https://placehold.co/15x15/B8175A/B8175A.png) | Magenta     | `#B8175A` | Tags · properties · 6.15:1            |
| ![#C42466](https://placehold.co/15x15/C42466/C42466.png) | Neon Pink   | `#C42466` | Operators · 5.37:1                    |
| ![#BE2E5E](https://placehold.co/15x15/BE2E5E/BE2E5E.png) | Rose        | `#BE2E5E` | Status bar (white fg) · 5.44:1        |
| ![#9E3F66](https://placehold.co/15x15/9E3F66/9E3F66.png) | Blush       | `#9E3F66` | Parameters · attributes · 6.06:1      |
| ![#F4A8C2](https://placehold.co/15x15/F4A8C2/F4A8C2.png) | Pastel Pink | `#F4A8C2` | **Surface only** — never used as text |
| ![#82475E](https://placehold.co/15x15/82475E/82475E.png) | Dust Rose   | `#82475E` | Punctuation · 6.75:1                  |

### Complements — for syntax range

| | Token | Hex | Role |
| :-: | --- | --- | --- |
| ![#7C3AED](https://placehold.co/15x15/7C3AED/7C3AED.png) | Plum   | `#7C3AED` | Functions · constants · AI |
| ![#0E7490](https://placehold.co/15x15/0E7490/0E7490.png) | Teal   | `#0E7490` | Types · classes            |
| ![#15803D](https://placehold.co/15x15/15803D/15803D.png) | Forest | `#15803D` | Regex · added · success    |
| ![#B45309](https://placehold.co/15x15/B45309/B45309.png) | Burnt  | `#B45309` | Strings · warnings · find  |
| ![#92400E](https://placehold.co/15x15/92400E/92400E.png) | Amber  | `#92400E` | Numbers · modified         |
| ![#2A0A17](https://placehold.co/15x15/2A0A17/2A0A17.png) | Ink    | `#2A0A17` | Primary text · 17.6:1      |

### Semantic

| | Token | Hex |
| :-: | --- | --- |
| ![#C81E3A](https://placehold.co/15x15/C81E3A/C81E3A.png) | Error   | `#C81E3A` |
| ![#B45309](https://placehold.co/15x15/B45309/B45309.png) | Warning | `#B45309` |
| ![#0E7490](https://placehold.co/15x15/0E7490/0E7490.png) | Info    | `#0E7490` |
| ![#15803D](https://placehold.co/15x15/15803D/15803D.png) | Success | `#15803D` |

</details>

<details>
<summary><strong>Syntax token map</strong> — role → color, both variants</summary>

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

</details>

## Open source

pinkode is MIT-licensed and lives on GitHub: https://github.com/e-l-l/pinkode

Issues, palette tweaks, and PRs welcome — open a [pull request](https://github.com/e-l-l/pinkode/pulls) or [file an issue](https://github.com/e-l-l/pinkode/issues) with a screenshot of what you'd like changed.

## License

MIT — see [`LICENSE`](./LICENSE).
