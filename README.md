# Pinkode — Hot Pink Noir

A near-black VS Code theme with **hot pink** as the load-bearing accent, **pastel pink** for highlights, and a curated set of **lavender**, **sky** and **peach** tokens for syntax.

Designed for late nights.

## Install

1. Open the Extensions view (`Cmd+Shift+X` / `Ctrl+Shift+X`)
2. Search for `Pinkode`
3. Install
4. `Cmd+K Cmd+T` (or `Ctrl+K Ctrl+T`) → **Pinkode — Hot Pink Noir**

Or from a `.vsix`:

```sh
code --install-extension pinkode-0.1.0.vsix
```

## Palette

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

## Syntax token map

| Role                          | Color       |
| ----------------------------- | ----------- |
| Keywords, control flow        | Hot Pink    |
| `this` / `self` (italic)      | Hot Pink    |
| Functions, function calls     | Lavender    |
| Types, classes, interfaces    | Sky         |
| Properties (`.scrollLeft`)    | Pastel Pink |
| Parameters (italic)           | Blush       |
| Strings                       | Peach       |
| Numbers                       | Amber       |
| Language constants            | Lavender    |
| Operators                     | Neon Pink   |
| Punctuation                   | Dust Rose   |
| Comments (italic)             | `#6A5A64`   |
| Regex, escapes                | Mint        |
| Tags                          | Magenta     |
| Attributes                    | Blush       |
| Diff added                    | Mint        |
| Diff removed                  | Error       |
| Diff modified                 | Amber       |
| AI ghost text / inline hints  | Lavender    |

## Screenshots

> Screenshots TODO. Add captures to `screenshots/preview.png` and reference here.

```
![Editor preview](screenshots/preview.png)
```

## License

See `LICENSE` (TODO).
