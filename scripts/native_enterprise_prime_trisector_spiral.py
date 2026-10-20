#!/usr/bin/env python3
"""Native Enterprise tri-sector prime allocation experiment.

Research status: FREE computational exploration; NOT canonical foundation.

The allocation rule uses only the current Enterprise address atlas
    (a,b,c) in N_0^3, min(a,b,c)=0
and the three-sector cyclic order.  It does NOT use primality to choose a
coordinate and does NOT introduce negative axes.

Primary shell:
    h(a,b,c) = a+b+c = r.
Because min(a,b,c)=0, shell r is the union of the three sector segments
S12, S23, S31 and contains exactly 3r addresses.

Integers are assigned consecutively shell by shell.  The optional
'alternating' orientation reverses the cyclic traversal on even shells while
keeping the same shell and the same E1 start presentation.

The SVG output is a carrier/address portrait only.  Its 120-degree drawing is
NOT used as the native metric and is not a claim about the unresolved
cross-sector point-to-point metric.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def sieve(nmax: int) -> list[bool]:
    p = [True] * (nmax + 1)
    if nmax >= 0:
        p[0] = False
    if nmax >= 1:
        p[1] = False
    q = 2
    while q * q <= nmax:
        if p[q]:
            for m in range(q * q, nmax + 1, q):
                p[m] = False
        q += 1
    return p


def fixed_shell(r: int) -> list[tuple[int, int, int]]:
    """Cyclic E1 -> E2 -> E3 -> E1 shell, exactly 3r addresses."""
    out: list[tuple[int, int, int]] = []
    # S12: E1 inclusive, E2 excluded.
    out.extend((r - j, j, 0) for j in range(r))
    # S23: E2 inclusive, E3 excluded.
    out.extend((0, r - j, j) for j in range(r))
    # S31: E3 inclusive, E1 excluded.
    out.extend((j, 0, r - j) for j in range(r))
    assert len(out) == 3 * r
    assert len(set(out)) == 3 * r
    return out


def shell(r: int, orientation: str) -> list[tuple[int, int, int]]:
    ring = fixed_shell(r)
    if orientation == "fixed" or r % 2 == 1:
        return ring
    if orientation == "alternating":
        # Keep E1 as the presentation start; reverse the remaining cyclic order.
        return [ring[0]] + list(reversed(ring[1:]))
    raise ValueError(orientation)


def sector(addr: tuple[int, int, int]) -> str:
    a, b, c = addr
    positive = sum(x > 0 for x in addr)
    if positive == 1:
        return "AXIS"
    if c == 0:
        return "S12"
    if a == 0:
        return "S23"
    if b == 0:
        return "S31"
    raise AssertionError(addr)


def axis(addr: tuple[int, int, int]) -> str:
    a, b, c = addr
    if a > 0 and b == 0 and c == 0:
        return "E1"
    if b > 0 and a == 0 and c == 0:
        return "E2"
    if c > 0 and a == 0 and b == 0:
        return "E3"
    return ""


def carrier_xy(addr: tuple[int, int, int]) -> tuple[float, float]:
    """Visualization-only 120-degree carrier presentation."""
    a, b, c = addr
    x = a - 0.5 * b - 0.5 * c
    y = (math.sqrt(3.0) / 2.0) * (b - c)
    return x, y


def build(rmax: int, orientation: str):
    rows = []
    n = 0
    for r in range(1, rmax + 1):
        for addr in shell(r, orientation):
            n += 1
            rows.append((n, r, addr))
    expected = 3 * rmax * (rmax + 1) // 2
    assert n == expected
    return rows


def write_svg(path: Path, rows, is_prime: list[bool]) -> None:
    pts = []
    xs, ys = [], []
    for n, _r, addr in rows:
        x, y = carrier_xy(addr)
        xs.append(x)
        ys.append(y)
        if is_prime[n]:
            pts.append((x, y))
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    margin = 5.0
    width = 900.0
    height = 900.0
    sx = (width - 2 * margin) / max(xmax - xmin, 1.0)
    sy = (height - 2 * margin) / max(ymax - ymin, 1.0)
    s = min(sx, sy)

    def px(x: float) -> float:
        return margin + (x - xmin) * s

    def py(y: float) -> float:
        return height - margin - (y - ymin) * s

    circles = "\n".join(
        f'<circle cx="{px(x):.3f}" cy="{py(y):.3f}" r="1.65" />'
        for x, y in pts
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="900" viewBox="0 0 900 900">
<title>Enterprise tri-sector prime allocation — address portrait only</title>
<desc>Primes under h=a+b+c shell allocation. Carrier drawing is visualization only, not native metric.</desc>
<rect width="100%" height="100%" fill="white"/>
<g fill="black">{circles}</g>
</svg>\n'''
    path.write_text(svg, encoding="utf-8")


def run(rmax: int, orientation: str, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    rows = build(rmax, orientation)
    nmax = rows[-1][0]
    prime = sieve(nmax)

    counts = {"E1": [0, 0], "E2": [0, 0], "E3": [0, 0],
              "S12": [0, 0], "S23": [0, 0], "S31": [0, 0]}

    csv_path = out / f"trisector_{orientation}_r{rmax}.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, lineterminator="\n")
        writer.writerow(["n", "prime", "shell", "a", "b", "c", "sector", "axis"])
        for n, r, addr in rows:
            s = sector(addr)
            ax = axis(addr)
            label = ax if ax else s
            counts[label][0] += 1
            counts[label][1] += int(prime[n])
            writer.writerow([n, int(prime[n]), r, *addr, s, ax])

    svg_path = out / f"trisector_{orientation}_r{rmax}_primes.svg"
    write_svg(svg_path, rows, prime)

    prime_count = sum(prime)
    print(f"RMAX={rmax}")
    print(f"NMAX={nmax}")
    print(f"PRIMES={prime_count}")
    print(f"GLOBAL_DENSITY={prime_count / nmax:.12f}")
    for key in ["E1", "E2", "E3", "S12", "S23", "S31"]:
        total, pcount = counts[key]
        print(f"{key}={pcount}/{total}={pcount / total:.12f}")
    axis_total = sum(counts[k][0] for k in ["E1", "E2", "E3"])
    axis_primes = sum(counts[k][1] for k in ["E1", "E2", "E3"])
    print(f"AXIS_DENSITY={axis_primes / axis_total:.12f}")
    print(f"AXIS_ENRICHMENT={(axis_primes / axis_total) / (prime_count / nmax):.12f}")
    print(f"CSV={csv_path}")
    print(f"SVG={svg_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--shells", type=int, default=114)
    parser.add_argument("--orientation", choices=["fixed", "alternating"], default="fixed")
    parser.add_argument("--out", type=Path, default=Path("native_enterprise_prime_out"))
    args = parser.parse_args()
    run(args.shells, args.orientation, args.out)
