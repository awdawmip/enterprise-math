#!/usr/bin/env python3
"""Exact signed-X6 unit-norm probe completeness for endpoint vs shortest BRC.

Coordinates are signed native chart displacements on one fixed X6 Cell torsor.
A single common radius is known; native path words are unweighted coordinate
shortest paths, with positive integer multinomial multiplicities.
"""
from collections import defaultdict
from functools import lru_cache
from math import factorial, isqrt
from itertools import combinations


@lru_cache(None)
def sphere(dim, r2):
    if dim == 0:
        return ((),) if r2 == 0 else ()
    out = []
    for x in range(-isqrt(r2), isqrt(r2) + 1):
        for tail in sphere(dim - 1, r2 - x*x):
            out.append((x,)+tail)
    return tuple(out)


def brc(d):
    n = sum(map(abs, d))
    denom = 1
    for x in d:
        denom *= factorial(abs(x))
    return n, factorial(n) // denom


def probe(d, i, r2):
    v = list(d)
    v[i] += 1
    return sum(x*x for x in v)


def check(n, r):
    points = sphere(n, r*r)
    assert points
    allaxes = tuple(range(n))
    for d in points:
        p = tuple(probe(d, i, r*r) for i in allaxes)
        assert all(p[i] == r*r + 1 + 2*d[i] for i in allaxes)
        assert tuple((q-r*r-1)//2 for q in p) == d
    for omitted in allaxes:
        keep = tuple(i for i in allaxes if i != omitted)
        groups = defaultdict(set)
        for d in points:
            groups[tuple(probe(d, i, r*r) for i in keep)].add(brc(d))
        assert all(len(values) == 1 for values in groups.values())
        # +r and -r on the unprobed axis are always observationally paired.
        d = tuple(r if j == omitted else 0 for j in allaxes)
        dn = tuple(-x for x in d)
        assert tuple(probe(d,i,r*r) for i in keep) == tuple(probe(dn,i,r*r) for i in keep)
    if r == 5:
        for a,b in combinations(allaxes, 2):
            keep = tuple(i for i in allaxes if i not in (a,b))
            da = tuple(5 if i == a else 0 for i in allaxes)
            db = tuple(3 if i == a else (4 if i == b else 0) for i in allaxes)
            assert tuple(probe(da,i,25) for i in keep) == tuple(probe(db,i,25) for i in keep)
            assert brc(da) == (5, 1)
            assert brc(db) == (7, 35)
    return len(points)


def main():
    observations = {}
    for n in (3,6):
        observations[n] = {r: check(n, r) for r in range(1,7)}
    assert brc((0,0,0,0,5,0)) == (5,1)
    assert brc((0,0,0,0,3,4)) == (7,35)
    print({"status":"PASS", "dimensions": [3,6], "radii": [1,2,3,4,5,6],
           "exhaustive_points":observations,
           "full_endpoint_probes": 6, "universal_shortest_brc_probes": 5,
           "two_unprobed_r5_brc_witness":[1,35]})


if __name__ == "__main__":
    main()
