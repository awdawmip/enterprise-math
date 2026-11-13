#!/usr/bin/env python3
"""Exact signed six-axis G=25 PathSqrt pair-chart observer-boundary test.

Native coordinates, min-zero observer and shortest signed primitive-axis
BRC words are different types.  Does not rerun any original native benchmark.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, factorial, isqrt

D, G = 6, 25

def shell(prefix=(), remaining=G):
    if len(prefix) == D:
        if remaining == 0:
            yield prefix
        return
    bound = isqrt(remaining)
    for v in range(-bound, bound + 1):
        yield from shell(prefix + (v,), remaining - v * v)

def rho(z):
    m = min(z)
    return tuple(t-m for t in z)

def brc(z):
    t = sum(abs(v) for v in z)
    d = 1
    for v in z:
        d *= factorial(abs(v))
    return factorial(t) // d

def support(z):
    return sum(t != 0 for t in z)

def abs_type(z):
    return tuple(sorted((abs(t) for t in z if t), reverse=True))

def signed_chart_union():
    roots = [(a, b) for a in range(6) for b in range(6) if a*a + b*b == G]
    assert roots == [(0, 5), (3, 4), (4, 3), (5, 0)]
    out = set()
    for i, j in combinations(range(D), 2):
        for a, b in roots:
            for sa, sb in product((-1, 1), repeat=2):
                z = [0] * D
                z[i], z[j] = sa*a, sb*b
                out.add(tuple(z))
    return out

def main():
    full = set(shell())
    assert len(full) == 7812
    pairs = signed_chart_union()
    assert len(pairs) == 132 and sum(brc(z) for z in pairs) == 4212
    assert pairs == {z for z in full if support(z) <= 2}
    by_observer = defaultdict(list)
    for z in full:
        by_observer[rho(z)].append(z)
    assert len(by_observer) == 6372
    assert Counter(map(len, by_observer.values())) == {1: 4932, 2: 1440}

    collision_support = Counter()
    type_count = Counter()
    gaps = Counter()
    for fiber in by_observer.values():
        if len(fiber) != 2:
            continue
        x, y = sorted(fiber, key=lambda z: min(z))
        assert rho(x) == rho(y)
        k = min(y) - min(x)
        assert k in (1, 3)
        assert all(b-a == k for a,b in zip(x,y))
        assert brc(x) != brc(y)
        gaps[k] += 1
        collision_support[tuple(sorted((support(x), support(y))))] += 1
        type_count[(k, abs_type(x), abs_type(y))] += 1
    assert gaps == {1: 1080, 3: 360}
    assert collision_support == {(4,6):1080, (5,6):360}
    assert sorted(type_count.values()) == [180,180,180,180,360,360]

    # A fixed R063 signed pair-chart endpoint is never merged with any *other*
    # native G25 endpoint under min-zero observation, even outside pair support.
    assert len({rho(z) for z in pairs}) == len(pairs)
    assert all(len(by_observer[rho(z)]) == 1 for z in pairs)
    assert sum(brc(z) for z in full) == 2538954612
    print('PASS_X6_LP028_G25_PATHSQRT_NATIVE_OBSERVER_COLLISION_BOUNDARY')
    print('full_native=7812; full_observers=6372; double_fibers=1440')
    print('collision_support=(4,6):1080,(5,6):360; depth_gaps=1:1080,3:360')
    print('current_R063_signed_pair_chart_endpoints=132; native_BRC=4212')
    print('pair_endpoints_with_global_observer_collision=0')
    print('scope=SIGNED_NATIVE_G25_ONLY; not full PathSqrt operator or Result review')

if __name__ == '__main__':
    main()
