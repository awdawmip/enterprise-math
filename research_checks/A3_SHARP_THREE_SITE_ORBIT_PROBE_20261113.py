#!/usr/bin/env python3
"""Exact signed-S4 regression for the sharp unrestricted-site A3 binary probe."""
from itertools import permutations

G = list(permutations(range(4)))
E = (0, 1, 2, 3)
H = (1, 0, 2, 3)


def action(g, x):
    parity = (-1) ** sum(g[i] > g[j] for i in range(4) for j in range(i + 1, 4))
    y = [0] * 4
    for i in range(4):
        y[g[i]] = parity * x[i]
    return tuple(y)


def root(i, j):
    x = [0] * 4
    x[i] = 1
    x[j] = -1
    return tuple(x)


def free_point(r):
    assert r >= 2
    return (r, r - 1, 1 - r, -r)


def probe(n, d):
    q = n - d + 1
    assert 1 <= d <= n
    if q >= 2:
        m = {root(2, 3), free_point(q)}
        if d >= 2:
            m.add(free_point(q + 1))
        return frozenset(m)
    if n >= 2:
        return frozenset({root(0, 1), root(0, 2), free_point(2)})
    return frozenset({root(0, 1)})


def output(n, d, minus, plus, upper):
    q = n - d + 1
    cutoff = q + (1 if upper else 0)
    g = plus if upper else minus
    return frozenset(action(g if max(map(abs, x)) >= cutoff else E, x)
                     for x in probe(n, d))


def predicted(n, d, minus, plus):
    q = n - d + 1
    if q >= 2:
        return minus == E and (d == 1 or plus == E)
    if n >= 2:
        return minus in (E, H) and plus == E
    return minus in (E, H)


def check(nmax=8):
    comparisons = 0
    counts = {}
    for n in range(1, nmax + 1):
        for d in range(1, n + 1):
            size = len(probe(n, d))
            counts[(n, d)] = size
            assert 1 <= size <= 3
            for minus in G:
                for plus in G:
                    a = output(n, d, minus, plus, upper=True)
                    b = output(n, d, minus, plus, upper=False)
                    orbit_equal = a == b or a == frozenset(action(H, x) for x in b)
                    assert orbit_equal == predicted(n, d, minus, plus), (
                        n, d, minus, plus, a, b
                    )
                    comparisons += 1
    assert [g for g in G if action(g, root(0, 1)) == root(0, 1)] == [E, H]
    for r in range(2, nmax + 2):
        assert [g for g in G if action(g, free_point(r)) == free_point(r)] == [E]
    print("PASS", comparisons, "exact alignment cases; max marked sites", max(counts.values()))
    print("probe sizes n<=4:", {k: v for k, v in counts.items() if k[0] <= 4})


if __name__ == "__main__":
    check()
