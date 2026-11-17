#!/usr/bin/env python3
"""Exact signed-X6 BRC root/closed-loop tensor-jet information test; finite scope."""
from collections import Counter, defaultdict
from itertools import combinations, product
from json import dumps

N = 6
ZERO = (0,) * N


def e(i, sign=1):
    return tuple(sign if a == i else 0 for a in range(N))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def phases(i, j, k, orientation):
    if orientation == 1:
        return (e(i), e(j, -1), e(k), e(i, -1), e(j), e(k, -1))
    return (e(i), e(k, -1), e(j), e(i, -1), e(k), e(j, -1))


def jet(steps, order):
    levels = [(1,)] + [(0,) * (N ** degree) for degree in range(1, order + 1)]
    for step in steps:
        for degree in range(order, 0, -1):
            extension = tuple(x * y for x in levels[degree - 1] for y in step)
            levels[degree] = tuple(x + y for x, y in zip(levels[degree], extension))
    return tuple(levels)


def main():
    samples = []
    for i, j, k in combinations(range(N), 3):
        for orientation in (-1, 1):
            p = phases(i, j, k, orientation)
            for bits in product((0, 1), repeat=6):
                if bits[1] != 1:
                    continue  # exactly the Unit79 nonzero root population
                mids = tuple(add(p[t], p[(t + 1) % 6]) if bits[t] else ZERO for t in range(6))
                root = mids[1]
                assert root != ZERO
                primitive_steps = tuple(s for t in range(6)
                                        for s in ((neg(p[t]), p[(t + 1) % 6])
                                                  if bits[t] == 0 else
                                                  (p[(t + 1) % 6], neg(p[t]))))
                if any(sum(step[a] for step in primitive_steps) for a in range(N)):
                    raise ValueError('closed path lost signed displacement')
                jt = jet(primitive_steps, 3)
                diagonal = tuple(jt[2][a * N + a] for a in range(N))
                if diagonal != tuple(-2 if a in (i, j, k) else 0 for a in range(N)):
                    raise ValueError('diagonal S2 does not recover frame support')
                c = (bits[0] + bits[3], bits[1] + bits[4], bits[2] + bits[5])
                if orientation == 1:
                    expected = {(i, j): -c[0], (j, k): -c[1], (i, k): c[2]}
                else:
                    expected = {(i, k): -c[0], (j, k): c[1], (i, j): c[2]}
                for (a, b), value in expected.items():
                    if jt[2][a * N + b] != value or jt[2][b * N + a] != -value:
                        raise ValueError('S2 does not encode pairwise OUTER counts')
                samples.append((root, p[2], mids[2], p[3], (i, j, k), orientation, bits, jt[2], jt[3]))

    if len(samples) != 1280:
        raise ValueError('wrong exact population size')

    def census(level):
        groups = defaultdict(list)
        for s in samples:
            signature = s[0] if level == 0 else (s[0], s[7] if level == 2 else s[8])
            groups[signature].append(s)
        ambiguous = [rows for rows in groups.values() if len({r[2] for r in rows}) > 1]
        return dict(signatures=len(groups), ambiguous_signatures=len(ambiguous),
                    ambiguous_histories=sum(map(len, ambiguous)),
                    maximum_future_values=max(len({r[2] for r in rows}) for rows in groups.values()),
                    fiber_sizes=dict(sorted(Counter(map(len, groups.values())).items())))

    root = census(0)
    order2 = census(2)
    order3 = census(3)
    if root != {'signatures': 20, 'ambiguous_signatures': 20,
                'ambiguous_histories': 1280, 'maximum_future_values': 5,
                'fiber_sizes': {32: 8, 64: 6, 96: 4, 128: 2}}:
        raise ValueError('unexpected root-only census')
    if order2 != {'signatures': 720, 'ambiguous_signatures': 240,
                  'ambiguous_histories': 640, 'maximum_future_values': 2,
                  'fiber_sizes': {1: 320, 2: 320, 4: 80}}:
        raise ValueError('unexpected exact degree-two census')
    if order3 != {'signatures': 1280, 'ambiguous_signatures': 0,
                  'ambiguous_histories': 0, 'maximum_future_values': 1,
                  'fiber_sizes': {1: 1280}}:
        raise ValueError('unexpected exact degree-three census')

    x = {'schema': 'X6_UNIT80_EXACT_SIGNED_ROOT_TENSOR_JET_CENSUS_V1',
         'population': '20 signed nonzero roots; all 20 ascending triads, both orientations, 32 of 64 BRC branch words per oriented triad',
         'history_count': len(samples), 'source_frames': 40, 'signed_roots': 20,
         'root_only': root, 'root_plus_full_closed_path_S2': order2,
         'root_plus_full_closed_path_S3': order3,
         'caveat': 'full-closed-loop jet is an offline observer after all twelve primitive steps; not a causal predictor of x5',
         'failures': 0}
    print(dumps(x, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
