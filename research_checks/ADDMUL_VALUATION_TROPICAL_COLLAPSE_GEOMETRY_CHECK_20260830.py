#!/usr/bin/env python3
"""Exact regression for RS-ADDMUL-VALUATION-TROPICAL-COLLAPSE-GEOMETRY.

No floating point, no p-adic completion, no probabilistic checks.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import product
from math import inf

PRIMES = (2, 3, 5, 7, 11)


def vp(n: int, p: int):
    if n == 0:
        return inf
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def p_unit(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("zero has no p-unit")
    return n // (p ** int(vp(n, p)))


def kappa(x: int, y: int, p: int):
    """Return finite kappa, inf for nontrivial exact cancellation, None for (0,0)."""
    if x == 0 and y == 0:
        return None
    baseline = min(vp(x, p), vp(y, p))
    if x + y == 0:
        return inf
    return vp(x + y, p) - baseline


def factor_vector(n: int, primes=PRIMES):
    if n == 0:
        return None
    return tuple(int(vp(n, p)) for p in primes)


def global_excess(xs: tuple[int, ...], p: int):
    if not xs or all(x == 0 for x in xs):
        return None
    baseline = min(vp(x, p) for x in xs)
    total = sum(xs)
    if total == 0:
        return inf
    return vp(total, p) - baseline


def tree_evaluations(xs: tuple[int, ...], p: int):
    """All ordered binary bracketings; each row=(sum, global excess, local kappa ledger)."""
    @lru_cache(None)
    def rec(lo: int, hi: int):
        if hi - lo == 1:
            x = xs[lo]
            mu = vp(x, p)
            e = 0 if x != 0 else None
            return ((x, mu, e, ()),)
        rows = []
        for cut in range(lo + 1, hi):
            for lsum, lmu, le, lledger in rec(lo, cut):
                for rsum, rmu, re, rledger in rec(cut, hi):
                    mu = min(lmu, rmu)
                    total = lsum + rsum
                    kk = kappa(lsum, rsum, p)
                    if mu == inf:
                        e = None
                    elif total == 0:
                        e = inf
                    else:
                        e = vp(total, p) - mu
                    rows.append((total, mu, e, lledger + rledger + (kk,)))
        return tuple(rows)
    return rec(0, len(xs))


def crt(congruences: list[tuple[int, int]]) -> int:
    """Pairwise-coprime CRT, returning the least nonnegative solution."""
    x = 0
    modulus = 1
    for residue, m in congruences:
        if m <= 0:
            raise ValueError
        # m is coprime to the accumulated modulus in all task uses.
        inv = pow(modulus, -1, m)
        t = ((residue - x) * inv) % m
        x += modulus * t
        modulus *= m
        x %= modulus
    return x


def prescribed_unit_input(depths: dict[int, int]) -> int:
    """Construct y with vp(y)=0 and kappa_p(1,y)=requested finite depth."""
    congruences = []
    for p, k in depths.items():
        if k == 0:
            if p == 2:
                raise ValueError("two odd 2-adic units cannot have tied kappa 0")
            residue, modulus = 1, p
        else:
            modulus = p ** (k + 1)
            residue = p**k - 1  # 1+y == p^k mod p^(k+1)
        congruences.append((residue, modulus))
    return crt(congruences)


def run():
    counts = {
        "single_p_classification": 0,
        "vector_laws": 0,
        "finite_precision_budget": 0,
        "tree_coherence": 0,
        "crt_depth_witness": 0,
    }

    # 1. Complete single-p classification on a dense signed integer box.
    for p in PRIMES:
        for x in range(-96, 97):
            for y in range(-96, 97):
                if x == 0 and y == 0:
                    continue
                a, b = vp(x, p), vp(y, p)
                kk = kappa(x, y, p)
                if x == 0 or y == 0:
                    assert kk == 0
                elif a != b:
                    assert kk == 0
                else:
                    u, v = p_unit(x, p), p_unit(y, p)
                    if u == -v:
                        assert kk == inf
                    else:
                        assert kk == vp(u + v, p)
                        if kk == 0:
                            assert (u + v) % p != 0
                        else:
                            k = int(kk)
                            assert (u + v) % (p**k) == 0
                            assert (u + v) % (p ** (k + 1)) != 0
                counts["single_p_classification"] += 1

    # 2. Multiplication is coordinatewise additive; ordinary addition is min + K.
    for x in range(-64, 65):
        for y in range(-64, 65):
            if x != 0 and y != 0:
                for p in PRIMES:
                    assert vp(x * y, p) == vp(x, p) + vp(y, p)
                    counts["vector_laws"] += 1
            if not (x == 0 and y == 0) and x + y != 0:
                for p in PRIMES:
                    kk = kappa(x, y, p)
                    assert kk not in (None, inf)
                    assert vp(x + y, p) == min(vp(x, p), vp(y, p)) + kk
                    counts["vector_laws"] += 1

    # 3. Arbitrarily deep tied cancellation with identical valuation inputs.
    for p in PRIMES:
        start = 1 if p == 2 else 0
        for k in range(start, 8):
            if k == 0:
                x, y = 1, 1
            else:
                x, y = 1, p**k - 1
            assert vp(x, p) == vp(y, p) == 0
            assert kappa(x, y, p) == k
            counts["crt_depth_witness"] += 1
        assert kappa(1, -1, p) == inf
        counts["crt_depth_witness"] += 1

    # 4. Independent finite-window cancellation depths by CRT.
    profiles = (
        {2: 1, 3: 0, 5: 2},
        {2: 3, 3: 2, 5: 0},
        {2: 5, 3: 1, 5: 4, 7: 2},
    )
    for profile in profiles:
        y = prescribed_unit_input(profile)
        for p, expected in profile.items():
            assert vp(1, p) == vp(y, p) == 0
            assert kappa(1, y, p) == expected
            counts["crt_depth_witness"] += 1

    # 5. Finite residue depth D: tied cancellation consumes exactly k digits.
    #    If k >= D (or exact zero), D input digits can only report overflow.
    for p in (2, 3, 5, 7):
        units = [u for u in range(-50, 51) if u and u % p]
        for D in range(1, 7):
            mod = p**D
            for u in units:
                for v in units:
                    s = u + v
                    left = (u % mod + v % mod) % mod
                    if s == 0:
                        assert left == 0
                    else:
                        k = int(vp(s, p))
                        if k < D:
                            assert left != 0
                            assert int(vp(left, p)) == k
                            exact_tail = (s // (p**k)) % (p ** (D - k))
                            projected_tail = (left // (p**k)) % (p ** (D - k))
                            assert exact_tail == projected_tail
                        else:
                            assert left == 0
                    counts["finite_precision_budget"] += 1

    # 6. All bracketings preserve the root global excess, but local kappa ledgers do not.
    cases = (
        (1, 1, 1, 3),
        (1, 1, 1, 2),
        (1, -1, 2),
        (3, 5, 7, 9),
        (2, 6, 10, 14),
    )
    for p in (2, 3, 5):
        for xs in cases:
            expected = global_excess(xs, p)
            for total, mu, e, ledger in tree_evaluations(xs, p):
                assert total == sum(xs)
                assert e == expected
                counts["tree_coherence"] += 1

    # Explicit path-dependence witness with finite local ledgers.
    xs = (1, 1, 1, 3)
    rows = tree_evaluations(xs, 2)
    finite_sums = {
        sum(k for k in ledger if k not in (None, inf))
        for _, _, _, ledger in rows
        if all(k != inf for k in ledger)
    }
    assert finite_sums == {2, 3}
    assert global_excess(xs, 2) == 1

    # Explicit path-dependence witness where one bracketing hits exact zero and another does not.
    rows = tree_evaluations((1, -1, 2), 2)
    assert any(inf in ledger for _, _, _, ledger in rows)
    assert any(inf not in ledger for _, _, _, ledger in rows)
    assert global_excess((1, -1, 2), 2) == 1

    total_checks = sum(counts.values())
    print("PASS", counts, "total=", total_checks)
    return counts, total_checks


if __name__ == "__main__":
    run()
