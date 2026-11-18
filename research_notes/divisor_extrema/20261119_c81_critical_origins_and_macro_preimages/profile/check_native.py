"""Direct original rational H, true breakpoints, and every physical phase cell."""
from collections import Counter
from fractions import Fraction as F
from itertools import pairwise
import json

from mpmath import mp

from native_paths import native_tail_ratios
from phase_components import summarize

mp.dps = 75
SCALE = 10**14
MODES = {"x": (1, 0), "y": (0, 1), "plus": (1, 1), "minus": (1, -1)}


def scaled_readout(n, v, w, p):
    tails = native_tail_ratios(n, v, w)
    return (1 << p) * max(tails) / min(tails)


def true_cells(values):
    cuts = sorted({F(0), F(1), *((-z) % 1 for z in values)})
    return list(pairwise(cuts))


def fourier_factors(cells, frequency):
    def mp_value(z):
        return mp.mpf(z.numerator) / z.denominator
    if frequency == 0:
        return [mp_value(b-a) for a, b in cells]
    t = 2j * mp.pi * frequency
    return [(mp.exp(t*mp_value(b)) - mp.exp(t*mp_value(a)))/t for a, b in cells]


def check(c):
    report = summarize(c)
    p = report["p"]
    points = [(scaled_readout(c, v, w, p), scaled_readout(c+1, v, w, p))
              for v in range(2, c+1) for w in range(2, v+1)]
    xcells = true_cells(x for x, _ in points)
    ycells = true_cells(y for _, y in points)
    count = []
    for xa, xb in xcells:
        row = []
        for ya, yb in ycells:
            buckets = Counter(((x+(xa+xb)/2)//1, (y+(ya+yb)/2)//1) for x, y in points)
            row.append(sum(value == 1 for value in buckets.values()))
        count.append(row)

    assert report["phase_rectangles"] == len(xcells)*len(ycells)
    assert report["extrema"] == [min(map(min, count)), max(map(max, count))]
    n = len(points)
    dx = [b-a for a, b in xcells]
    dy = [b-a for a, b in ycells]
    row_means = [sum(w*k for w, k in zip(dy, row))/n for row in count]
    col_means = [sum(w*k for w, k in zip(dx, col))/n for col in zip(*count)]
    mean = sum(v*w for v, w in zip(row_means, dx))
    variance = sum(wx * sum(wy*(F(k,n)-mean)**2 for wy, k in zip(dy, row))
                   for wx, row in zip(dx, count))
    comp1 = sum(w*(v-mean)**2 for w, v in zip(dx, row_means))
    comp2 = sum(w*(v-mean)**2 for w, v in zip(dy, col_means))
    for value, bounds in [(mean, report["mean_1e14"]),
                          (variance, report["variance_1e14"])]:
        assert bounds[0] <= SCALE*value <= bounds[1]
    for name, value in [("first", comp1), ("second", comp2),
                        ("interaction", variance-comp1-comp2)]:
        low, high = report["component_variance_1e14"][name]
        assert low <= SCALE*value <= high
    for name, (kx, ky) in MODES.items():
        zx = fourier_factors(xcells, kx)
        zy = fourier_factors(ycells, ky)
        magnitude = abs(sum(a * sum(b*k for b,k in zip(zy,row)) for a,row in zip(zx,count))/n)
        low, high = report["amplitude_1e14"][name]
        assert low <= SCALE*magnitude <= high
    return {"c": c, "templates": n, "exact_rectangles": len(dx)*len(dy)}


if __name__ == "__main__":
    print(json.dumps([check(c) for c in (4, 6, 8)], indent=2))
