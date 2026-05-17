"""WCAG contrast ratios for the pinkode light palette."""
from __future__ import annotations

import re
from dataclasses import dataclass

# Six-digit hex only — three-digit shorthand intentionally not accepted
HEX_RE = re.compile(r"^#([0-9A-Fa-f]{6})$")


@dataclass(frozen=True)
class Color:
    name: str
    hex: str

    def channels(self) -> tuple[int, int, int]:
        match = HEX_RE.match(self.hex)
        if not match:
            raise ValueError(f"invalid hex: {self.hex!r}")
        value = match.group(1)
        return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def _linearize(channel: int) -> float:
    c = channel / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(color: Color) -> float:
    r, g, b = (_linearize(c) for c in color.channels())
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg: Color, bg: Color) -> float:
    l1, l2 = sorted((relative_luminance(fg), relative_luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


CANVAS = Color("Whisper", "#FFFAFD")
RASPBERRY = Color("Raspberry", "#BD1B57")


if __name__ == "__main__":
    ratio = contrast_ratio(RASPBERRY, CANVAS)
    target = 4.5
    verdict = "AA" if ratio >= target else "fail"
    print(f"{RASPBERRY.name} on {CANVAS.name}: {ratio:.2f}:1 → {verdict}")
