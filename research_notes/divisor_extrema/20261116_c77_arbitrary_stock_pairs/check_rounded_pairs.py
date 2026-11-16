"""Small exact triangular checks, ordinary uniformly shifted dyadic bins."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement
import json

from check_three_precision import physical


def isolated(widths, p, offsets):
    cells = [tuple((int((q * (1 << p) + off) // 1))
                   for q, off in zip(pair, offsets)) for pair in widths]
    return sum(v == 1 for v in Counter(cells).values())


def run():
    out = []
    for c in (16, 32, 64):
        templates = [(v, w) for w, v in
                     combinations_with_replacement(range(2, c+1), 2)]
        triples = [(physical(c, v, w), physical(c+1, v, w), physical(2*c, v, w))
                   for v, w in templates]
        pairs = [[(r[0], r[i]) for r in triples] for i in (1, 2)]
        assert all(len(set(pair)) == len(templates) for pair in pairs)
        l = c.bit_length() - 1
        results = []
        for p in sorted(set((7*l//4, 9*l//4, 3*l, 4*l))):
            for off in ((F(0), F(0)), (F(1, 3), F(2, 5))):
                results.append(dict(bits=p, offsets=[str(o) for o in off],
                               isolated_adjacent=isolated(pairs[0], p, off),
                               isolated_doubled=isolated(pairs[1], p, off)))
        out.append(dict(c=c, total=len(templates), rows=results))
    return out


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
