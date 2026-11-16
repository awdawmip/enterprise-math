"""All grid translations for the original pair of adjacent physical readings."""
from collections import Counter
from fractions import Fraction as F
from itertools import groupby
from math import lcm
import json

from check_finite import native_tail_ratios


def axis_intervals(values):
    """For each interval give its exact length, and words moving at its left end."""
    jumps = sorted((1 - value % 1, word) for word, value in enumerate(values))
    inside = [(t, [w for _, w in group]) for t, group in groupby(jumps, lambda a:a[0]) if t < 1]
    starts = [(F(0), [])] + inside
    ends = [t for t, _ in inside] + [F(1)]
    widths = [b-a for (a, _), b in zip(starts, ends)]
    den = lcm(*(v.denominator for v in widths))
    return den, [(int(v*den), movers) for v, (_, movers) in zip(widths, starts)]


def averaged_profile(values):
    """Return extrema and the mean over the full unit torus. All steps are exact."""
    x, y = zip(*values)
    dx, strips = axis_intervals(x)
    dy, rows = axis_intervals(y)
    xs, ybase = [int(t) for t in x], [int(t) for t in y]
    lo, hi, mass = len(y), 0, 0
    for width, left in strips:
        for i in left:
            xs[i] += 1
        ys = ybase.copy()
        counts = Counter(zip(xs, ys))
        n = sum(k == 1 for k in counts.values())
        column_mass = 0
        for height, moving in rows:
            for i in moving:
                old = xs[i], ys[i]
                n += int(counts[old] == 2) - int(counts[old] == 1)
                counts[old] -= 1
                ys[i] += 1
                new = xs[i], ys[i]
                n += int(counts[new] == 0) - int(counts[new] == 1)
                counts[new] += 1
            lo, hi = min(lo,n), max(hi,n)
            column_mass += height*n
        mass += width*column_mass
    return lo, hi, F(mass, dx*dy), len(strips)*len(rows)


def run():
    toy = [(F(4,3),F(3,2)),(F(5,3),F(3,2))]
    assert averaged_profile(toy)[:3] == (0,2,F(2,3))
    # Coincident breakpoints cross simultaneously with half-open boundaries.
    assert averaged_profile([(F(0),F(0)),(F(0),F(0))])[:3] == (0,0,0)
    out=[]
    for c in (8,16,24):
        p=((c**9).bit_length()-1)//4
        vals=[]
        for v in range(2,c+1):
            for w in range(2,v+1):
                pair=[]
                for n in (c,c+1):
                    tails=native_tail_ratios(n,v,w)
                    pair.append((1<<p)*max(tails)/min(tails))
                vals.append(pair)
        low, high, mean, regions=averaged_profile(vals)
        scale=10**8
        lower=int(mean*scale//len(vals))
        out.append(dict(c=c,p=p,templates=len(vals),translation_rectangles=regions,
                        min_unique=low,max_unique=high,
                        mean_unique_rate_times_1e8_floor=lower,
                        mean_unique_rate_times_1e8_ceil=-int(-mean*scale//len(vals))))
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    run()
