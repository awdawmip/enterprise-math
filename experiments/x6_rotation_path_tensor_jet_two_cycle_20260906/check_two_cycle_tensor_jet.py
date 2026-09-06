#!/usr/bin/env python3
"""Exact two-cycle extension of the X6 triadic branch tensor-jet census.

For two ordered complete shortest Q cycles there are 64^2=4096 branch
histories.  In the intrinsic selected-triad 3D coordinate basis the truncated
noncommutative path-jet class counts are exactly:
  depth 1:    1
  depth 2:  125 = 5^3
  depth 3:  729 = 3^6
  depth 4: 3860 (236 double collision fibers)
  depth 5: 4096
Thus depth five is the first lossless jet order for the ordered two-cycle
population.
"""

from __future__ import annotations

from itertools import product

DIM = 3
INNER = 0
OUTER = 1

PHASES = (
    (1, 0, 0),
    (0, -1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, 1, 0),
    (0, 0, -1),
)
WORDS = tuple(product((INNER, OUTER), repeat=6))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def kron(a, b):
    return tuple(x * y for x in a for y in b)


def branch_steps(a, b, bit):
    minus_a = tuple(-x for x in a)
    return (minus_a, b) if bit == INNER else (b, minus_a)


def cycle_steps(word):
    out = []
    for r, bit in enumerate(word):
        out.extend(branch_steps(PHASES[r], PHASES[(r + 1) % 6], bit))
    return tuple(out)


def jet(steps, order):
    levels = [(1,)]
    for degree in range(1, order + 1):
        levels.append((0,) * (DIM**degree))
    for step in steps:
        for degree in range(order, 0, -1):
            levels[degree] = add(levels[degree], kron(levels[degree - 1], step))
    return tuple(levels)


def product_jet(left, right, order):
    out = [(1,)]
    for degree in range(1, order + 1):
        value = (0,) * (DIM**degree)
        for p in range(degree + 1):
            value = add(value, kron(left[p], right[degree - p]))
        out.append(value)
    return tuple(out)


def key(j):
    return tuple(j[1:])


def class_census(order):
    one = {word: jet(cycle_steps(word), order) for word in WORDS}
    fibers = {}
    for first in WORDS:
        for second in WORDS:
            total = product_jet(one[first], one[second], order)
            fibers.setdefault(key(total), []).append((first, second))
    return fibers


def check_counts():
    expected = {1: 1, 2: 125, 3: 729, 4: 3860, 5: 4096}
    cached = {}
    for order, count in expected.items():
        fibers = class_census(order)
        cached[order] = fibers
        assert len(fibers) == count

    assert max(len(v) for v in cached[4].values()) == 2
    assert sum(len(v) == 2 for v in cached[4].values()) == 236
    assert all(len(v) == 1 for v in cached[5].values())


def check_order2_and_order3_meanings():
    # Order two: each single cycle remembers three antipodal pair counts in
    # {0,1,2}; summing two cycles gives three counts in {0,...,4} -> 5^3.
    seen2 = {}
    seen3 = {}
    one2 = {word: jet(cycle_steps(word), 2) for word in WORDS}
    one3 = {word: jet(cycle_steps(word), 3) for word in WORDS}

    for first in WORDS:
        for second in WORDS:
            antipodal_counts = tuple(
                first[r] + first[r + 3] + second[r] + second[r + 3]
                for r in range(3)
            )
            edge_counts = tuple(first[r] + second[r] for r in range(6))

            k2 = key(product_jet(one2[first], one2[second], 2))
            k3 = key(product_jet(one3[first], one3[second], 3))

            seen2.setdefault(k2, set()).add(antipodal_counts)
            seen3.setdefault(k3, set()).add(edge_counts)

    assert len(seen2) == 125
    assert len(seen3) == 729
    assert all(len(values) == 1 for values in seen2.values())
    assert all(len(values) == 1 for values in seen3.values())


def check_explicit_order4_collision_resolved_at5():
    edge5 = (0, 0, 0, 0, 0, 1)
    edge2 = (0, 0, 1, 0, 0, 0)

    j4 = {word: jet(cycle_steps(word), 4) for word in (edge5, edge2)}
    left4 = product_jet(j4[edge5], j4[edge2], 4)
    right4 = product_jet(j4[edge2], j4[edge5], 4)
    assert left4 == right4

    j5 = {word: jet(cycle_steps(word), 5) for word in (edge5, edge2)}
    left5 = product_jet(j5[edge5], j5[edge2], 5)
    right5 = product_jet(j5[edge2], j5[edge5], 5)
    assert left5 != right5


def main():
    check_counts()
    check_order2_and_order3_meanings()
    check_explicit_order4_collision_resolved_at5()

    print("PASS: two-cycle X6 triadic tensor-jet threshold")
    print("ordered_two_cycle_histories", 4096)
    print("depth1_classes", 1)
    print("depth2_classes", 125)
    print("depth3_classes", 729)
    print("depth4_classes", 3860)
    print("depth4_double_collision_fibers", 236)
    print("depth5_classes", 4096)
    print("first_lossless_two_cycle_jet_order", 5)


if __name__ == "__main__":
    main()
