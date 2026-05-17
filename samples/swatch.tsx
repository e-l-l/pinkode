// @ts-nocheck — sample file for theme screenshots, not a build target
import { useMemo } from "react";

interface Color {
  name: string;
  hex: string;
  role: string;
}

interface SwatchGridProps {
  colors: Color[];
  size?: number;
}

const PALETTE: Color[] = [
  { name: "Raspberry", hex: "#BD1B57", role: "Keywords" },
  { name: "Plum",      hex: "#7C3AED", role: "Functions" },
  { name: "Teal",      hex: "#0E7490", role: "Types" },
  { name: "Forest",    hex: "#15803D", role: "Regex" },
  { name: "Burnt",     hex: "#B45309", role: "Strings" },
  { name: "Amber",     hex: "#92400E", role: "Numbers" },
];

// Six-digit hex per channel — three-digit shorthand intentionally rejected
const isValidHex = (hex: string): boolean => /^#[0-9A-F]{6}$/i.test(hex);

export function SwatchGrid({ colors, size = 24 }: SwatchGridProps) {
  const valid = useMemo(
    () => colors.filter((c) => isValidHex(c.hex)),
    [colors]
  );

  return (
    <ul className="swatch-grid" role="list">
      {valid.map((color, index) => (
        <li key={color.hex} data-index={index}>
          <span
            className="chip"
            style={{ background: color.hex, width: size, height: size }}
            aria-label={`${color.name} — ${color.role}`}
          />
          <strong>{color.name}</strong>
          <code>{color.hex}</code>
          <em>{color.role}</em>
        </li>
      ))}
    </ul>
  );
}

export default function Demo() {
  return <SwatchGrid colors={PALETTE} size={32} />;
}
