# pinkode

A pink-forward VS Code color theme published as a set of **flavors**. This glossary fixes the vocabulary for the palette and its variants so docs, commits, and future themes stay consistent.

## Language

**Flavor**:
One published, selectable theme in the family (appears in the VS Code picker as `pinkode - <flavor>`).
_Avoid_: variant (reserve for the relationship between flavors), mode, scheme.

**Noir**:
The dark flavor — near-black surfaces, neon pink accents, high contrast.

**Light**:
The day flavor — cream/rose surfaces, WCAG-AA syntax, dark text.

**Haze**:
The low-contrast dark flavor — a softened sibling of Noir. Surfaces lifted from black toward grey, primary text pulled off pure-white, and pinks desaturated toward pastel, so the canvas↔text and canvas↔accent deltas are deliberately smaller. Built for longer, lower-strain sessions.
_Avoid_: dim, dusk, smoke, soft-noir (rejected names — see Flagged ambiguities).

**Surface**:
A background tone in the chrome ramp — the window backdrop, editor canvas, sidebar, tab, input, etc. Surfaces carry no semantic meaning; they establish depth.

**Accent**:
A pink that carries the brand. Used for both syntax (keywords, operators, tags) and UI chrome (cursor, active borders, badges, buttons, selection).

**Complement**:
A non-pink syntax color (Lavender, Sky, Mint, Peach, Amber) that extends the palette's range. Several complements double as **signal** colors.

**Signal**:
A color whose job is to alert — error, warning, info, success. Distinct from a Complement in intent even when it shares the same hue (e.g. Sky is both the Types accent and the Info signal). The pure-alert red is signal-only.

**Surface-only**:
A tone permitted as a background but never as text. (In Light, the pastel pink is surface-only.)

## Relationships

- The family ships multiple **Flavors**; today: **Noir**, **Light**, **Haze**.
- **Haze** is derived in spirit from **Noir** — same hue identity, lowered contrast — but is an independent flavor, not a runtime toggle of Noir.
- Every **Flavor** is built from **Surfaces** + **Accents** + **Complements**, with some **Complements** doubling as **Signals**.
- Within a flavor, **Signals** may be exempt from a flavor-wide treatment (e.g. Haze softens accents and complements but keeps error/alert signals at full strength).

## Example dialogue

> **Maintainer:** "Haze softens the pinks — does that include the error red?"
> **Designer:** "No. Error is a **Signal**, not an **Accent**. Signals stay loud in every flavor, otherwise you miss the thing they're warning you about. Haze softens **Accents** and dims **Complements**, but Signals hold."

## Flagged ambiguities

- "variant" was used for both the new flavor and the Noir↔Haze relationship — resolved: a shipped theme is a **Flavor**; "variant" describes how one flavor relates to another.
- Haze name candidates "dusk", "smoke", "soft-noir", "dim" were considered and rejected in favor of **Haze** (foggy / low-contrast connotation, one-word peer to noir/light).
