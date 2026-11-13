"""Exact six-phase native X6 N-BRC two-branch path-fiber census.
Only the previously proved INNER/OUTER two-shortest-native-step interface is used.
No pi/trigonometric propagation, classical rotation matrix or numerical approximation.
"""
from collections import Counter
from itertools import product


N = 6


def unit(axis, sign=1):
    a = [0] * N
    a[axis] = sign
    return tuple(a)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def check():
    phases = [
        unit(0), unit(1), unit(2),
        unit(0, -1), unit(1, -1), unit(2, -1)
    ]
    zero = (0,) * N
    seen = set()
    inner_counts = Counter()
    nonbacktracking_count = 0
    spur_count = 0

    # Exact typed N-BRC fiber: 0=INNER, 1=OUTER.
    for branches in product((0, 1), repeat=6):
        cells = [phases[0]]
        for i, branch in enumerate(branches):
            a, b = phases[i], phases[(i + 1) % 6]
            middle = zero if branch == 0 else add(a, b)
            cells.extend((middle, b))

        assert cells[0] == cells[-1]
        assert len(cells) == 13
        edges = [add(cells[i + 1], neg(cells[i]))
                 for i in range(12)]
        assert all(sum(abs(x) for x in edge) == 1 for edge in edges)

        # Includes the end-to-start edge transition of this closed walk.
        no_spur = all(edges[(j + 1) % 12] != neg(edges[j])
                      for j in range(12))
        no_adjacent_inners = all(
            branches[j] != 0 or branches[(j + 1) % 6] != 0
            for j in range(6)
        )
        assert no_spur == no_adjacent_inners
        seen.add(tuple(cells))
        if no_spur:
            nonbacktracking_count += 1
            inner_counts[branches.count(0)] += 1
        else:
            spur_count += 1

        if branches == (1,) * 6:
            assert len(set(cells[:-1])) == 12

    assert len(seen) == 64
    assert nonbacktracking_count == 18
    assert spur_count == 46
    assert inner_counts == {0: 1, 1: 6, 2: 9, 3: 2}

    print({
        "PASS": True,
        "ambient_X6_axes": 6,
        "local_triads": (0, 1, 2),
        "macro_phases": 6,
        "native_microsteps": 12,
        "branch_words": 64,
        "distinct_closed_native_paths": len(seen),
        "cyclically_nonbacktracking": nonbacktracking_count,
        "cyclically_backtracking": spur_count,
        "nonbacktracking_by_inner_count": dict(sorted(inner_counts.items())),
        "all_outer_distinct_native_cells": 12,
    })


if __name__ == "__main__":
    check()
