# pinkode

> A pink-forward VS Code theme. Three flavors — **Noir** for dark, **Haze** for low-contrast dark, **Light** for day. Raspberry pink does the heavy lifting; a curated complement palette covers the syntax range.

## Preview

| pinkode - noir | pinkode - haze | pinkode - light |
| :---: | :---: | :---: |
| ![pinkode noir](screenshots/noir-tsx.png) | ![pinkode haze](screenshots/haze-tsx.png) | ![pinkode light](screenshots/light-tsx.png) |
| near-black surfaces · bright pink accents | lifted grey surfaces · pastel pinks · low contrast | cream-and-rose surfaces · WCAG-AA syntax |

<details>
<summary>Python preview</summary>

| pinkode - noir | pinkode - haze | pinkode - light |
| :---: | :---: | :---: |
| ![noir · py](screenshots/noir-py.png) | ![haze · py](screenshots/haze-py.png) | ![light · py](screenshots/light-py.png) |

</details>

## Install

1. Open the Extensions view (`Cmd+Shift+X` / `Ctrl+Shift+X`)
2. Search for `Pinkode`
3. Install
4. `Cmd+K Cmd+T` (or `Ctrl+K Ctrl+T`) → pick **pinkode - noir**, **pinkode - haze**, or **pinkode - light**

Or from a `.vsix`:

```sh
code --install-extension pinkode-0.3.0.vsix
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
<summary><strong>Haze</strong> — low-contrast noir: lifted greys, pastel pinks, loud signals</summary>

Noir's hue identity at smaller contrast deltas — surfaces lifted off black, text off pure-white, pinks and complements softened (editor canvas↔text drops from ~15:1 to ~9:1). Status signals (error/warning/info/success, find, diff, git) keep Noir's full-strength values, so a syntax complement and its matching status color **diverge** here — e.g. strings use Peach `#ECAC8E` while a warning stays `#FFB088`.

### Surfaces — lifted greys

| | Token | Hex | Role |
| :-: | --- | --- | --- |
| ![#131318](https://placehold.co/15x15/131318/131318.png) | Void          | `#131318` | Window backdrop        |
| ![#17171D](https://placehold.co/15x15/17171D/17171D.png) | Activity Bar  | `#17171D` | Deepest chrome         |
| ![#1C1C22](https://placehold.co/15x15/1C1C22/1C1C22.png) | Editor        | `#1C1C22` | Main canvas            |
| ![#202027](https://placehold.co/15x15/202027/202027.png) | Sidebar       | `#202027` | File tree, panels      |
| ![#26262E](https://placehold.co/15x15/26262E/26262E.png) | Elevated      | `#26262E` | Active tab, breadcrumb |
| ![#2C2C36](https://placehold.co/15x15/2C2C36/2C2C36.png) | Input / Hover | `#2C2C36` | Form fields, hover     |

### Accents — pastel pinks

| | Token | Hex | Role |
| :-: | --- | --- | --- |
| ![#FF85B5](https://placehold.co/15x15/FF85B5/FF85B5.png) | Hot Pink    | `#FF85B5` | Keywords · selection · brand |
| ![#FF6FBE](https://placehold.co/15x15/FF6FBE/FF6FBE.png) | Magenta     | `#FF6FBE` | Tags · markup                |
| ![#FF96C0](https://placehold.co/15x15/FF96C0/FF96C0.png) | Neon Pink   | `#FF96C0` | Operators                    |
| ![#E58BA8](https://placehold.co/15x15/E58BA8/E58BA8.png) | Rose        | `#E58BA8` | Hover · borders              |
| ![#FFB6D0](https://placehold.co/15x15/FFB6D0/FFB6D0.png) | Blush       | `#FFB6D0` | Parameters · attributes      |
| ![#FFC8DD](https://placehold.co/15x15/FFC8DD/FFC8DD.png) | Pastel Pink | `#FFC8DD` | Properties · selected text   |
| ![#C79FAF](https://placehold.co/15x15/C79FAF/C79FAF.png) | Dust Rose   | `#C79FAF` | Punctuation                  |

### Complements — dimmed, kept distinct

| | Token | Hex | Role |
| :-: | --- | --- | --- |
| ![#B6A0E8](https://placehold.co/15x15/B6A0E8/B6A0E8.png) | Lavender | `#B6A0E8` | Functions · constants · AI |
| ![#93C9EC](https://placehold.co/15x15/93C9EC/93C9EC.png) | Sky      | `#93C9EC` | Types · classes            |
| ![#A6DEC6](https://placehold.co/15x15/A6DEC6/A6DEC6.png) | Mint     | `#A6DEC6` | Regex · escapes (syntax)   |
| ![#ECAC8E](https://placehold.co/15x15/ECAC8E/ECAC8E.png) | Peach    | `#ECAC8E` | Strings (syntax)           |
| ![#E8C794](https://placehold.co/15x15/E8C794/E8C794.png) | Amber    | `#E8C794` | Numbers (syntax)           |
| ![#D8CDD4](https://placehold.co/15x15/D8CDD4/D8CDD4.png) | Whisper  | `#D8CDD4` | Primary text               |

### Semantic — kept at Noir strength

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
<summary><strong>Syntax token map</strong> — role → color, noir & light</summary>

**Haze** maps every role to the same accent _name_ as Noir, at the softened hexes in the Haze palette above — except status signals (diff added/removed/modified, error), which keep Noir's full-strength color. AI ghost text and inline hints soften with the rest.


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
| AI ghost text                 | Lavender     | `#A87890`   |
| Inline hints                  | Lavender     | Plum        |

</details>

## Open source

pinkode is MIT-licensed and lives on GitHub: https://github.com/e-l-l/pinkode

Issues, palette tweaks, and PRs welcome — open a [pull request](https://github.com/e-l-l/pinkode/pulls) or [file an issue](https://github.com/e-l-l/pinkode/issues) with a screenshot of what you'd like changed.

## License

MIT — see [`LICENSE`](./LICENSE).
