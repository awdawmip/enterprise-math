#!/usr/bin/env python3
"""Exact regression for RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE.

The extractor receives only (n, x, Delta). Prime factors are used only by
the regression harness as hidden ground truth.
"""
from __future__ import annotations

from itertools import combinations, product
from math import gcd, lcm


def v2(n: int) -> int:
    a = 0
    while n % 2 == 0 and n:
        a += 1
        n //= 2
    return a


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factor_int(n: int) -> list[tuple[int, int]]:
    out = []
    d = 2
    while d * d <= n:
        if n % d:
            d += 1
            continue
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        out.append((d, e))
        d += 1
    if n > 1:
        out.append((n, 1))
    return out


def order_prime(x: int, p: int) -> int:
    r = p - 1
    for ell, _ in factor_int(r):
        while r % ell == 0 and pow(x, r // ell, p) == 1:
            r //= ell
    return r


def collapse(n: int, x: int, delta: int) -> int | None:
    """Factor from a valid collision difference using no hidden factor/order."""
    if delta <= 0 or gcd(x, n) != 1 or pow(x, delta, n) != 1:
        raise ValueError("not a valid local collision certificate")
    s = v2(delta)
    u = delta >> s
    z = pow(x, u, n)
    if z == 1:
        return None
    for _ in range(s):
        z_next = z * z % n
        if z_next == 1:
            for candidate in (gcd(z - 1, n), gcd(z + 1, n)):
                if 1 < candidate < n:
                    return candidate
            return None
        z = z_next
    raise AssertionError("valid collision did not terminate at one")


def single_failure_probability(A: int, B: int) -> tuple[int, int]:
    m = min(A, B)
    return 4**m + 2, 3 * 2 ** (A + B)


def aggregate_failure_probability(A: int, B: int, k: int) -> tuple[int, int]:
    m = min(A, B)
    numerator = 1
    for t in range(1, m + 1):
        phi = 2 ** (t - 1)
        numerator += phi * (2 ** (t * k) - 2 ** ((t - 1) * k))
    return numerator, 2 ** ((A + B) * k)


def depth_coordinate(a: int, A: int) -> int:
    modulus = 2**A
    a %= modulus
    return 0 if a == 0 else A - v2(a)


def diagonal_barrier(
    generators: tuple[tuple[int, int], ...], A: int, B: int
) -> bool:
    """Ground-truth test: every generated 2-primary element has equal depths."""
    ma, mb = 2**A, 2**B
    horizon = 2 ** max(A, B)
    H = {(0, 0)}
    for x, y in generators:
        cyclic = {(c * x % ma, c * y % mb) for c in range(horizon)}
        H = {
            ((a + c) % ma, (b + d) % mb)
            for a, b in H
            for c, d in cyclic
        }
    return all(
        depth_coordinate(a, A) == depth_coordinate(b, B) for a, b in H
    )


def check_aggregate_formula() -> int:
    cases = 0
    for A in range(1, 4):
        for B in range(1, 4):
            elems = tuple(product(range(2**A), range(2**B)))
            for k in (1, 2):
                count = 0
                for gens in product(elems, repeat=k):
                    if diagonal_barrier(gens, A, B):
                        count += 1
                num, den = aggregate_failure_probability(A, B, k)
                assert count * den == num * len(elems) ** k
                cases += 1
    return cases


def main() -> None:
    primes = [p for p in range(3, 80, 2) if is_prime(p)]
    semiprimes = 0
    units = 0
    for p, q in combinations(primes, 2):
        n = p * q
        A, B = v2(p - 1), v2(q - 1)
        lam = lcm(p - 1, q - 1)
        successes = 0
        local_units = 0
        for x in range(1, n):
            if gcd(x, n) != 1:
                continue
            local_units += 1
            units += 1
            rp, rq = order_prime(x, p), order_prime(x, q)
            a, b = v2(rp), v2(rq)
            delta = lcm(rp, rq)
            got = collapse(n, x, delta) is not None
            assert got == (a != b)
            successes += int(got)
            for multiplier in (1, 2, 3, 6):
                got_global = collapse(n, x, lam * multiplier) is not None
                assert got_global == (a != b)
        fn, fd = single_failure_probability(A, B)
        assert successes * fd == (fd - fn) * local_units
        semiprimes += 1

    # Strict aggregation witness: each local collision fails, product succeeds.
    assert collapse(65, 57, 4) is None
    assert collapse(65, 47, 4) is None
    assert 57 * 47 % 65 == 14
    assert collapse(65, 14, lcm(4, 4)) in (5, 13)

    aggregate_cases = check_aggregate_formula()
    print("SINGLE_COLLISION_THEOREM=PASS")
    print(f"EXHAUSTIVE_SEMIPRIMES={semiprimes}")
    print(f"EXHAUSTIVE_UNITS={units}")
    print("GLOBAL_MULTIPLE_TESTS=PASS")
    print("STRICT_AGGREGATION_WITNESS=n65:x57,x47,delta4->product14")
    print(f"AGGREGATE_FORMULA_CASES={aggregate_cases}")
    print("FINITE_REGRESSION_IS_NOT_A_GENERAL_PROOF=TRUE")


if __name__ == "__main__":
    main()
