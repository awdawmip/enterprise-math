#!/usr/bin/env python3
"""Exact finite check of a historical X6 directed gauge's current native typing.

P000 V5: native signed raw displacements lie in Z^6; can6 is the
relative-observer section of Z^6 / Z(1,1,1,1,1,1).
Not a full GitHub module integration or a native performance benchmark.
"""
from itertools import product
from math import factorial

SIX = (1,) * 6
ZERO = (0,) * 6


def can6(v):
    low = min(v)
    return tuple(x - low for x in v)


def norm2(v):
    return sum(x * x for x in v)


def shortest_brc(v):
    n = sum(abs(x) for x in v)
    answer = factorial(n)
    for x in v:
        answer //= factorial(abs(x))
    return answer


def check():
    native_observer_collisions = 0
    shift_tests = 0
    for v in product(range(-2, 3), repeat=6):
        section = can6(v)
        for t in (-2, -1, 0, 1, 2):
            shifted = tuple(x + t for x in v)
            assert can6(shifted) == section
            shift_tests += 1
            if t and shifted != v:
                native_observer_collisions += 1
    assert shift_tests == 78125
    assert native_observer_collisions == 62500

    # Full signed X6 Cell zero and its nontrivial common-diagonal translate.
    assert can6(ZERO) == can6(SIX) == ZERO
    assert norm2(SIX) == 6
    assert shortest_brc(SIX) == 720
    assert shortest_brc(tuple(-v for v in SIX)) == 720
    for t in (-3, -2, -1, 1, 2, 3):
        delta = tuple(t for _ in range(6))
        assert can6(delta) == ZERO
        assert norm2(delta) == 6 * t * t
        assert shortest_brc(delta) == factorial(6 * abs(t)) // factorial(abs(t)) ** 6

    # Observer asymmetry is not an asymmetric native component norm.
    forward = (1, 0, 0, 0, 0, 0)
    reverse = tuple(-x for x in forward)
    assert norm2(forward) == norm2(reverse) == 1
    assert norm2(can6(forward)) == 1
    assert norm2(can6(reverse)) == 5

    print('PASS X6_LP026_V12_GAUGE_TYPED_CORRECTION')
    print(f'exact shift-invariance checks={shift_tests} native-observer collision witnesses={native_observer_collisions}')
    print('native diagonal witness: delta=(1,1,1,1,1,1), G=6, shortest signed BRC=720, observer squared gauge=0')
    print('native reverse-axis squared norm=(1,1), relative directed squared gauge=(1,5)')


if __name__ == '__main__':
    check()
