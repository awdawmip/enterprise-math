#!/usr/bin/env python3
"""Exact finite regression for the constant-size signed-S4 orbit probe."""
from itertools import permutations

S4 = list(permutations(range(4)))
ID = (0, 1, 2, 3)
H = (1, 0, 2, 3)


def parity(g):
    return (-1) ** sum(g[i] > g[j] for i in range(4) for j in range(i + 1, 4))


def signed_root(g, pair):
    i, j = pair
    return (g[i], g[j]) if parity(g) == 1 else (g[j], g[i])


def marker(n, d):
    q = n - d + 1
    two = lambda r: {(r, (0, 1)), (r, (0, 2))}
    if q >= 2:
        chosen = {(1, (2, 3))} | two(q)
        if d >= 2:
            chosen |= two(q + 1)
    elif n >= 2:
        chosen = two(1) | two(2)
    else:
        chosen = two(1)
    assert 2 <= len(chosen) <= 5
    return chosen


def pushout(n, d, gm, gp, *, upper):
    q = n - d + 1
    out = set()
    for r, root in marker(n, d):
        active = r >= (q+1 if upper else q)
        g = (gp if upper else gm) if active else ID
        out.add((r, signed_root(g, root)))
    return frozenset(out)


def orbit_equal(a, b):
    return a == b or a == frozenset((r, signed_root(H, root)) for r, root in b)


def theorem(n, d, gm, gp):
    q = n - d + 1
    if q >= 2:
        return gm == ID and (d == 1 or gp == ID)
    if n >= 2:
        return gm in (ID, H) and gp == ID
    return gm in (ID, H)


def check(nmax=5):
    counts = {}
    total = 0
    sizes = {}
    for n in range(1, nmax+1):
        for d in range(1, n+1):
            good = 0
            sizes[(n, d)] = len(marker(n, d))
            for gm in S4:
                for gp in S4:
                    x = pushout(n, d, gm, gp, upper=True)
                    y = pushout(n, d, gm, gp, upper=False)
                    observed = orbit_equal(x, y)
                    required = theorem(n, d, gm, gp)
                    if observed != required:
                        raise AssertionError((n, d, gm, gp, x, y))
                    good += int(observed)
                    total += 1
            counts[(n, d)] = good
    assert max(sizes.values()) == 5
    print('PASS', total, 'exact pair/regime comparisons; maximum marker sites', max(sizes.values()))
    print('cases n<=4', {k: v for k, v in counts.items() if k[0] <= 4})
    print('sizes n<=4', {k: v for k, v in sizes.items() if k[0] <= 4})

if __name__ == '__main__':
    check(5)
