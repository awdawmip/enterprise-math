#!/usr/bin/env python3
"""Exact finite regression for the A3 universal binary naturality witness.

Mathematical proof of the all-radius result is in the corresponding Driver note.
The checker enumerates the 24^2 aligner pairs at all 1 <= d <= n <= 4.
No floating arithmetic or external dependencies are used.
"""
from itertools import permutations

S4 = list(permutations(range(4)))
E = (0, 1, 2, 3)
H = (1, 0, 2, 3)


def sign(p):
    return -1 if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 else 1


def act(p, root):
    """Signed-S4 action on a root e_i - e_j, represented as (i,j)."""
    i, j = root
    return (p[i], p[j]) if sign(p) == 1 else (p[j], p[i])


def pair_on_shell(r):
    return {(r, (0, 1)), (r, (0, 2))}


def path_support(n, d, g_minus, g_plus, *, upper):
    """Support of output after upper-then-restrict or restrict-then-lower."""
    out = set()
    q = n - d + 1
    for r in range(1, n + 1):
        active = r >= (q + 1 if upper else q)
        g = (g_plus if upper else g_minus) if active else E
        out.update((r, act(g, root)) for _, root in pair_on_shell(r))
    return frozenset(out)


def global_h(support):
    return frozenset((r, act(H, root)) for r, root in support)


def theorem(n, d, gm, gp):
    q = n - d + 1
    if q >= 2:
        return gm == E and (d == 1 or gp == E)
    if n >= 2:
        return gm in {E, H} and gp == E
    return gm in {E, H}


def main():
    # The two-root support has trivial signed S4 set-stabilizer.
    markers = {(0, 1), (0, 2)}
    assert [g for g in S4 if {act(g, p) for p in markers} == markers] == [E]
    # A single oriented root does not have a trivial stabilizer.
    assert len([g for g in S4 if act(g, (0, 1)) == (0, 1)]) == 2

    counts = {}
    checks = 0
    for n in range(1, 5):
        for d in range(1, n + 1):
            accepted = 0
            for gm in S4:
                for gp in S4:
                    upper = path_support(n, d, gm, gp, upper=True)
                    lower = path_support(n, d, gm, gp, upper=False)
                    detected = lower == upper or lower == global_h(upper)
                    assert detected == theorem(n, d, gm, gp), (n, d, gm, gp)
                    accepted += detected
                    checks += 1
            counts[(n, d)] = accepted
    assert checks == 5760
    assert counts == {
        (1, 1): 48, (2, 1): 24, (2, 2): 2,
        (3, 1): 24, (3, 2): 1, (3, 3): 2,
        (4, 1): 24, (4, 2): 1, (4, 3): 1, (4, 4): 2,
    }
    print(f"PASS {checks} exact aligner/regime comparisons; {sum(counts.values())} positive")
    print(counts)


if __name__ == "__main__":
    main()
