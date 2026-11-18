"""Independent labeled-degree coverage check for the 15-vertex Q30 census.

Run directly to print each sector. Pass the C++ checker's text output to
compare independently computed counts with its accumulated orbit masses.
"""

from argparse import ArgumentParser
from functools import cache
from math import comb
from pathlib import Path
import re


@cache
def labeled(ones, twos, threes):
    """Graphs on a fixed assignment of degrees; isolated labels are implicit."""
    counts = [0, ones, twos, threes]
    degree = next((k for k in (3, 2, 1) if counts[k]), 0)
    if degree == 0:
        return 1
    counts[degree] -= 1
    total = 0
    for k1 in range(min(degree, counts[1]) + 1):
        for k2 in range(min(degree - k1, counts[2]) + 1):
            k3 = degree - k1 - k2
            if k3 <= counts[3]:
                choices = comb(counts[1], k1) * comb(counts[2], k2) * comb(counts[3], k3)
                total += choices * labeled(counts[1] - k1 + k2,
                                            counts[2] - k2 + k3,
                                            counts[3] - k3)
    return total


@cache
def connected(twos, threes):
    """Subtract the proper connected component of a specified degree-3 label."""
    if threes == 0:
        raise ValueError("connected() is used only on branching components")
    total = labeled(0, twos, threes)
    for a in range(twos + 1):
        for b in range(2, threes + 1, 2):
            if (a, b) == (twos, threes):
                continue
            choices = comb(twos, a) * comb(threes - 1, b - 1)
            total -= choices * connected(a, b) * labeled(0, twos - a, threes - b)
    return total


def sectors(n):
    return {r: connected(n - r, r) for r in range(2, n + 1, 2)}


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, nargs="?", help="C++ census stdout")
    args = parser.parse_args()
    n14 = [12414124800, 38690265600, 120607023600, 393165964800,
           1358543793600, 4991840330400, 19491385914000]
    if list(sectors(14).values()) != n14:
        raise AssertionError("n=14 published recovery benchmark differs")
    expected = sectors(15)
    for r, mass in expected.items():
        print(f"r={r} fixed-degree-label count={mass}")
    if args.output is not None:
        rows = re.findall(r"^r=(\d+)\b.*?\borbit=(\d+)\b",
                          args.output.read_text(encoding="utf-8"), re.MULTILINE)
        observed = {int(r): int(mass) for r, mass in rows}
        if len(rows) != len(expected) or observed != expected:
            raise AssertionError(f"orbit coverage differs: {observed}")
        print("All seven n=15 masses match the representative orbit sums.")


if __name__ == "__main__":
    main()
