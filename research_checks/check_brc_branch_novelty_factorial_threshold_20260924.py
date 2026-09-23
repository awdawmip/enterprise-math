#!/usr/bin/env python3
"""Finite falsification for BRC endpoint-decoration and factorial-entry theorems.
Proof is in research_notes/brc_branch_novelty_thresholds_20260924.md.
"""
from functools import lru_cache


def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def vpfact(m, p):
    s = 0
    while m:
        m //= p
        s += m
    return s


def eps(p, j):
    return 0 if (2 * j) % (p - 1) == 0 else 1


def beta(p, j):
    return 2 * j + eps(p, j) + vp(1 + 4**j, p) - vp(j, p)


@lru_cache(None)
def branch_support(p, N, factorial=True):
    # beta >= 2j-v_p(j), so j>N/2+1 cannot enter these tested horizons.
    js = [j for j in range(1, N // 2 + 2) if beta(p, j) < N]
    out = set()

    def rec(i, used, vec):
        if i == len(js):
            out.add(tuple(vec))
            return
        j = js[i]
        b = beta(p, j)
        m = 0
        while True:
            cost = m * b - (vpfact(m, p) if factorial else 0)
            if used + cost >= N:
                break
            if m:
                vec.append((j, m))
            rec(i + 1, used + cost, vec)
            if m:
                vec.pop()
            m += 1

    rec(0, 0, [])
    return frozenset(out)


@lru_cache(None)
def generic_support(N):
    js = [j for j in range(1, N // 2 + 1) if 2 * j + 1 < N]
    out = set()

    def rec(i, used, vec):
        if i == len(js):
            out.add(tuple(vec))
            return
        j = js[i]
        w = 2 * j + 1
        m = 0
        while used + m * w < N:
            if m:
                vec.append((j, m))
            rec(i + 1, used + m * w, vec)
            if m:
                vec.pop()
            m += 1

    rec(0, 0, [])
    return frozenset(out)


def add(a, b):
    d = {}
    for j, m in a + b:
        d[j] = d.get(j, 0) + m
    return tuple(sorted((j, m) for j, m in d.items() if m))


def residuals(r, j0):
    js = [j for j in range(1, j0) if 2 * j + 1 <= r]
    out = set()

    def rec(i, rem, vec):
        if i == len(js):
            if rem == 0:
                out.add(tuple(vec))
            return
        j = js[i]
        w = 2 * j + 1
        for m in range(rem // w + 1):
            if m:
                vec.append((j, m))
            rec(i + 1, rem - m * w, vec)
            if m:
                vec.pop()

    rec(0, r, [])
    if r == 0:
        out.add(tuple())
    return out


def cancellation_free(p, a):
    return all(vp(1 + 4**j, p) == 0 for j, m in a)


def predicted(p, N):
    j0 = (p - 1) // 2
    out = set()
    if p <= N <= 2 * p - 2:
        r = N - p
    elif N == 2 * p - 1:
        out |= {((p - 1, 1),), ((j0, 2),)}
        r = p - 1
    elif N == 2 * p:
        out |= {((j0, 2),)}
        r = p
    elif N == 2 * p + 1:
        out |= {((p, 1),)}
        r = p + 1
    else:
        raise ValueError(N)
    for a in residuals(r, j0):
        if cancellation_free(p, a):
            out.add(add(((j0, 1),), a))
    return frozenset(out)


def main():
    checks = []
    # Full endpoint window for the two primitive exceptional branches.
    for p in (13, 19):
        for N in range(p, 2 * p + 2):
            actual = branch_support(p, N, True) - generic_support(N)
            want = predicted(p, N)
            assert actual == want, (p, N, actual - want, want - actual)
            checks.append((p, N, len(actual)))

    # Larger-prime spot checks of the transition skeleton.
    for p in (37, 43):
        for N in (p, 2 * p - 2, 2 * p - 1, 2 * p, 2 * p + 1):
            actual = branch_support(p, N, True) - generic_support(N)
            want = predicted(p, N)
            assert actual == want, (p, N, actual - want, want - actual)
            checks.append((p, N, len(actual)))

    # Exact first factorial entry for p=13 and p=19.
    fchecks = {}
    for p in (13, 19):
        assert branch_support(p, 3 * p - 1, True) == branch_support(p, 3 * p - 1, False)
        extra = branch_support(p, 3 * p, True) - branch_support(p, 3 * p, False)
        assert extra == frozenset({((1, p),)}), (p, extra)
        fchecks[p] = {"horizon": 3 * p, "extra": ((1, p),)}

    # Earliest target-family uniform factorial novelty.
    N = 39
    ug = set(generic_support(N))
    uf = set(ug)
    un = set(ug)
    for p in (13, 19, 37):
        uf.update(branch_support(p, N, True))
        un.update(branch_support(p, N, False))
    assert uf - un == {((1, 13),)}

    print(
        {
            "status": "PASS",
            "endpoint_checks": len(checks),
            "sample_differences": checks[-10:],
            "factorial_first_entry": fchecks,
            "uniform_N39_extra": ((1, 13),),
            "uniform_N39_counts": {"with_factorial": len(uf), "without_factorial": len(un)},
        }
    )


if __name__ == "__main__":
    main()
