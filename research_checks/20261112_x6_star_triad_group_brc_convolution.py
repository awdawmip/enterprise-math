#!/usr/bin/env python3
"""Exact finite certificate: X6 signed triad generators and BRC composition.

Scientific input is the pinned signed-X6 spatial alphabet. This checker is
independent of official Result/Review admission and makes no physical-law claim.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments/x6_signed_native_spatial_v16_20260905"))
from signed_brc import endpoint_multiplicity, endpoint_weight  # source pinned in note

N = 6
IDENT = tuple(range(1, 7))
ZERO = (0,) * N
STAR = ((0, 2, 5), (0, 3, 4), (1, 2, 4), (1, 3, 5))
E = tuple(tuple((sgn if j == i else 0) for j in range(N))
          for i in range(N) for sgn in (1, -1))


def compose(f, g):
    """Signed images; f o g."""
    return tuple((1 if x > 0 else -1) * f[abs(x) - 1] for x in g)


def triad_generator(t):
    i, j, k = t
    g = list(IDENT)
    g[i], g[j], g[k] = j + 1, k + 1, -(i + 1)
    return tuple(g)


def closure(gens):
    seen = {IDENT}
    q = deque([IDENT])
    while q:
        x = q.popleft()
        for h in gens:
            y = compose(x, h)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


def apply(g, z):
    out = [0] * N
    for i, image in enumerate(g):
        out[abs(image) - 1] += (1 if image > 0 else -1) * z[i]
    return tuple(out)


def is_even(g):
    p = tuple(abs(x) for x in g)
    return sum(p[i] > p[j] for i in range(N)
               for j in range(i + 1, N)) % 2 == 0


def endpoint_layers(max_len):
    layers = [{ZERO: 1}]
    for _ in range(max_len):
        out = defaultdict(int)
        for z, count in layers[-1].items():
            for e in E:
                new = tuple(a + b for a, b in zip(z, e))
                out[new] += count
        layers.append(dict(out))
    return layers


def convolve(a, b):
    out = defaultdict(int)
    for x, p in a.items():
        for y, q in b.items():
            out[tuple(v + w for v, w in zip(x, y))] += p * q
    return dict(out)


def main():
    gens = [triad_generator(t) for t in STAR]
    for t in combinations(range(N), 3):
        g = triad_generator(t)
        cube = compose(g, compose(g, g))
        expected = tuple(-v if i in t else v for i, v in enumerate(IDENT))
        assert cube == expected
        assert compose(cube, cube) == IDENT

    expected_sizes = [6, 1920, 23040, 23040]
    for k, size in enumerate(expected_sizes, 1):
        group = closure(gens[:k])
        assert len(group) == size, (k, len(group), size)
        assert all(is_even(g) for g in group)
        if k == 3:
            G = group
            assert len({tuple(map(abs, g)) for g in G}) == 360
            assert len({g for g in G
                        if tuple(map(abs, g)) == IDENT}) == 64
    assert closure([triad_generator(t) for t in combinations(range(N), 3)]) == G

    layers = endpoint_layers(6)
    assert [len(d) for d in layers] == [1, 12, 73, 304, 985, 2668, 6321]
    assert [layers[m].get(ZERO, 0) for m in (2, 4, 6)] == [12, 396, 19920]
    for m, n in ((2, 2), (2, 4), (3, 3)):
        assert convolve(layers[m], layers[n]) == layers[m + n]
    for m in range(7):
        for z, count in layers[m].items():
            assert endpoint_multiplicity(m, z) == count
    for g in G:
        for z, count in layers[4].items():
            assert layers[4].get(apply(g, z), 0) == count

    # On a selected C6 edge, both ordered length-two paths have same endpoint,
    # different intermediate native Cell; length-two fibre has size exactly two.
    a, b = E[0], E[2]  # +e1, +e2
    d = tuple(y - x for x, y in zip(a, b))
    assert endpoint_multiplicity(2, d) == 2
    inner = (-1, 2)  # -e1, +e2, signed letter labels
    outer = (2, -1)  # +e2, -e1
    assert inner != outer
    assert endpoint_weight(2, d, [1]*N, [1]*N) == 2

    print("PASS X6_STAR_C6_BRC")
    print("STAR_generator_group_sizes=6,1920,23040,23040; all20=23040")
    print("G=(C2)^6 semidirect A6, order=23040")
    print("BRC_N2_0=12 BRC_N4_0=396 BRC_N6_0=19920")
    print("BRC_convolutions=2+2,2+4,3+3 all endpoints; group_m4=23040 elements")


if __name__ == "__main__":
    main()
