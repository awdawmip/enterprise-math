#!/usr/bin/env python3
"""X6 LP011 signed dominance fibre chamber exact regression.

This tests a new typed selected-slice formula, not a recovered historical
execution or full-X6 rotation experiment.
"""
from itertools import product
from math import factorial

def chart(d):
    h = min(d)
    return tuple(x - h for x in d), h

def native_dominant(d):
    magnitude = max(map(abs, d))
    return frozenset(
        (i + 1, 1 if x > 0 else -1)
        for i, x in enumerate(d)
        if magnitude and abs(x) == magnitude
    )

def chamber_dominant(a, h):
    assert len(a) == 3 and min(a) == 0
    m = max(a)
    if m == 0:
        if h == 0:
            return frozenset()
        return frozenset((i + 1, 1 if h > 0 else -1) for i in range(3))
    theta = 2 * h + m
    if theta > 0:
        return frozenset((i + 1, 1) for i, x in enumerate(a) if x == m)
    if theta < 0:
        return frozenset((i + 1, -1) for i, x in enumerate(a) if x == 0)
    return frozenset(
        (i + 1, 1 if x == m else -1)
        for i, x in enumerate(a)
        if x == 0 or x == m
    )

def shortest_brc(d):
    n = [abs(x) for x in d]
    denom = 1
    for x in n:
        denom *= factorial(x)
    return factorial(sum(n)) // denom

def run():
    chambers = ties = fibres = signed_cube = 0
    for a in product(range(7), repeat=3):
        if min(a):
            continue
        m = max(a)
        for h in range(-12, 13):
            d = tuple(x + h for x in a)
            assert chart(d) == (a, h)
            predicted = chamber_dominant(a, h)
            assert predicted == native_dominant(d)
            opposite = tuple(-x for x in d)
            ar, hr = chart(opposite)
            assert ar == tuple(m - x for x in a)
            assert hr == -h - m
            assert native_dominant(opposite) == frozenset(
                (i, -s) for i, s in predicted
            )
            assert shortest_brc(d) == shortest_brc(opposite)
            chambers += 1
            if len(predicted) > 1:
                ties += 1
        dplus = tuple(x + 1 for x in a)
        dminus = tuple(x - m - 1 for x in a)
        assert chart(dplus)[0] == chart(dminus)[0] == a
        assert native_dominant(dplus) != native_dominant(dminus)
        fibres += 1
    for d in product(range(-6, 7), repeat=3):
        a, h = chart(d)
        assert chamber_dominant(a, h) == native_dominant(d)
        signed_cube += 1
    assert chambers == 3175 and ties == 537
    assert fibres == 127 and signed_cube == 2197
    assert chamber_dominant((0, 2, 4), -2) == frozenset(
        ((1, -1), (3, 1))
    )
    assert native_dominant((0, 0, 0)) == frozenset()
    assert chart((-2, 1, 0))[0] == chart((1, 4, 3))[0]
    assert native_dominant((-2, 1, 0)) != native_dominant((1, 4, 3))
    print(
        "PASS X6_LP011_SIGNED_DOMINANT_CHAMBERS "
        f"chambers={chambers} ties={ties} "
        f"nonfactor_fibres={fibres} signed_cube={signed_cube} "
        "observer_inverse=exact reversal=equivariant BRC=symmetric"
    )

if __name__ == "__main__":
    run()
