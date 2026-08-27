#!/usr/bin/env python3
"""Independent Phase-A checker for the N-only valuation-wall gcd extractor.

Constructor-side functions receive N and public indices only. Hidden factors are
used only by the regression oracle in `run_regression`.
"""
from __future__ import annotations

import argparse
import json
from math import comb, gcd, isqrt


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [p for p in range(5, limit + 1) if sieve[p]]


def factorial_mod(k: int, n: int) -> int:
    z = 1 % n
    for j in range(2, k + 1):
        z = (z * j) % n
    return z


def a_mod_n(s: int, n: int) -> int:
    """Compute A_s=(2s)!(3s)!/(s!)^5 mod n when gcd(s!,n)=1."""
    fs = factorial_mod(s, n)
    if gcd(fs, n) != 1:
        raise ArithmeticError("constructor denominator is not invertible")
    return (
        factorial_mod(2 * s, n)
        * factorial_mod(3 * s, n)
        * pow(pow(fs, -1, n), 5, n)
    ) % n


def a_exact(s: int) -> int:
    return comb(2 * s, s) ** 2 * comb(3 * s, s)


def a_mod_recurrence(s: int, n: int) -> int:
    """Equivalent recurrence, valid while all 1..s are units mod n."""
    a = 1 % n
    for j in range(s):
        d = j + 1
        if gcd(d, n) != 1:
            raise ArithmeticError("recurrence denominator is not invertible")
        inv = pow(d, -1, n)
        a = (
            a
            * 6
            * (2 * j + 1)
            * (3 * j + 1)
            * (3 * j + 2)
            * pow(inv, 3, n)
        ) % n
    return a


def factor_n_only(n: int) -> tuple[int, dict]:
    """Return a nontrivial factor for the promised distinct odd semiprime domain."""
    if n <= 0 or gcd(n, 6) != 1:
        raise ValueError("domain requires a positive integer coprime to 6")

    dyadic = []
    s = 1
    while True:
        a = a_mod_n(s, n)
        g = gcd(a, n)
        dyadic.append((s, g))
        if 1 < g < n:
            return g, {"route": "dyadic", "dyadic": dyadic, "seed": s}
        if g == n:
            break
        s *= 2

    t = isqrt(n) // 3
    fallback = []
    for u in (t, t + 1):
        a = a_mod_n(u, n)
        g = gcd(a, n)
        fallback.append((u, g))
        if 1 < g < n:
            return g, {
                "route": "fallback",
                "dyadic": dyadic,
                "fallback": fallback,
                "seed": u,
            }
    raise AssertionError("two-seed fallback failed on promised domain")


def v_factorial(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out


def v_a(s: int, p: int) -> int:
    return v_factorial(2 * s, p) + v_factorial(3 * s, p) - 5 * v_factorial(s, p)


def validate_local_wall(primes: list[int]) -> int:
    checks = 0
    for r in primes:
        for s in range(r):
            lhs = v_a(s, r)
            rhs = (2 * s) // r + (3 * s) // r
            assert lhs == rhs, (r, s, lhs, rhs)
            assert (lhs > 0) == (3 * s >= r), (r, s, lhs)
            checks += 1
    return checks


def validate_recurrence() -> int:
    ns = [35, 77, 143, 221, 899, 10403]
    checks = 0
    for n in ns:
        least = next(p for p in range(5, isqrt(n) + 1) if n % p == 0)
        for s in range(least):
            direct = a_exact(s) % n
            assert a_mod_n(s, n) == direct, (n, s, "factorial")
            assert a_mod_recurrence(s, n) == direct, (n, s, "recurrence")
            checks += 1
    return checks


def run_regression(primes: list[int]) -> dict:
    total = 0
    dyadic_splits = 0
    synchronized = 0
    fallback_splits = 0
    max_seed = 0
    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            n = p * q
            f, trace = factor_n_only(n)
            assert f in (p, q), (p, q, f, trace)
            total += 1
            max_seed = max(max_seed, trace["seed"])
            if trace["route"] == "dyadic":
                dyadic_splits += 1
            else:
                fallback_splits += 1
                synchronized += 1
                sync_seed, sync_g = trace["dyadic"][-1]
                assert sync_g == n
                assert q <= 3 * sync_seed < 2 * p, (p, q, sync_seed)
                t = isqrt(n) // 3
                assert t + 1 < p < q
                assert 3 * t <= isqrt(n) < q
                if 3 * t >= p:
                    assert trace["fallback"][0][1] == p
                else:
                    assert p in (3 * t + 1, 3 * t + 2)
                    assert q > 3 * (t + 1)
                    assert trace["fallback"][-1][1] == p

    return {
        "semiprimes": total,
        "dyadic_splits": dyadic_splits,
        "synchronized_cases": synchronized,
        "fallback_splits": fallback_splits,
        "max_return_seed": max_seed,
        "failures": 0,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-limit", type=int, default=1000)
    args = ap.parse_args()
    primes = primes_upto(args.prime_limit)
    report = {
        "schema": "PCF4R_PHASE_A_INDEPENDENT_CHECK_V1",
        "prime_limit": args.prime_limit,
        "prime_count": len(primes),
        "local_wall_checks": validate_local_wall(primes),
        "recurrence_crosschecks": validate_recurrence(),
        "regression": run_regression(primes),
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
