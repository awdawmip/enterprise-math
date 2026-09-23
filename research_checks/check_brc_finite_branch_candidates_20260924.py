#!/usr/bin/env python3
"""
Exact falsification for the per-monomial finite branch-candidate theorem.

Portable research checker only. It does not confer Source authority,
mathematical acceptance, CLAIM, OPEN, Result, review, or Working Truth.

For a finite exponent vector m, define the target-prime credit candidate set:
  * endpoint candidate: (p-1) divides 2j for some occupied port j;
  * denominator candidate: p divides some occupied port j;
  * factorial candidate: p <= max_j m_j.

If a target prime is outside this set, all positive gain mechanisms vanish,
so Gamma_p(m) = -C_p(m) <= 0. Therefore only this finite set can make the
uniform carrier appear earlier than the generic branch.
"""

from __future__ import annotations

import random


P_RANDOM = 3000
J_MAX = 150
M_MAX = 160
VECTORS = 3000
SEED = 20260924


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


def target_primes_upto(bound: int) -> list[int]:
    return [
        p
        for p in range(13, bound + 1)
        if is_prime(p) and p % 24 in (13, 19)
    ]


def vp_int(n: int, p: int) -> int:
    if n == 0:
        raise ValueError
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def vp_factorial(n: int, p: int) -> int:
    e = 0
    q = p
    while q <= n:
        e += n // q
        q *= p
    return e


def vp_one_plus_four_power(j: int, p: int) -> int:
    e = 0
    modulus = p
    while (pow(4, j, modulus) + 1) % modulus == 0:
        e += 1
        modulus *= p
        if e > 12:
            raise RuntimeError("unexpectedly high valuation")
    return e


def endpoint_indicator(p: int, j: int) -> int:
    return int((2 * j) % (p - 1) == 0)


def gamma(p: int, m: dict[int, int]) -> int:
    E = sum(a * endpoint_indicator(p, j) for j, a in m.items())
    D = sum(a * vp_int(j, p) for j, a in m.items())
    C = sum(a * vp_one_plus_four_power(j, p) for j, a in m.items())
    F = sum(vp_factorial(a, p) for a in m.values())
    return E + D - C + F


def candidate_set(m: dict[int, int]) -> set[int]:
    occupied = [j for j, a in m.items() if a > 0]
    max_mult = max(m.values(), default=0)
    bound = max([max_mult] + [2 * j + 1 for j in occupied], default=0)
    targets = target_primes_upto(bound)

    out: set[int] = set()
    for p in targets:
        factorial = p <= max_mult
        endpoint = any((2 * j) % (p - 1) == 0 for j in occupied)
        denominator = any(j % p == 0 for j in occupied)
        if factorial or endpoint or denominator:
            out.add(p)
    return out


def candidate_bound(m: dict[int, int]) -> int:
    occupied = [j for j, a in m.items() if a > 0]
    max_mult = max(m.values(), default=0)
    return max([max_mult] + [2 * j + 1 for j in occupied], default=0)


def main() -> None:
    rng = random.Random(SEED)
    checked = 0
    outside_checked = 0
    strict_reductions = 0

    for _ in range(VECTORS):
        size = rng.randint(1, 6)
        js = rng.sample(range(1, J_MAX + 1), size)
        m = {j: rng.randint(1, M_MAX) for j in js}

        cand = candidate_set(m)
        bound = candidate_bound(m)
        all_relevant = target_primes_upto(bound)

        gain_all = max([0] + [gamma(p, m) for p in all_relevant])
        gain_cand = max([0] + [gamma(p, m) for p in cand])
        assert gain_all == gain_cand, (m, bound, cand, gain_all, gain_cand)

        for p in all_relevant:
            if p not in cand:
                g = gamma(p, m)
                assert g <= 0, (p, m, g)
                outside_checked += 1

        # Also probe larger target primes: they cannot carry endpoint,
        # denominator, or factorial credit because p > bound.
        for p in target_primes_upto(P_RANDOM):
            if p <= bound:
                continue
            g = gamma(p, m)
            assert g <= 0, (p, m, bound, g)
            outside_checked += 1

        if len(cand) < len(all_relevant):
            strict_reductions += 1

        checked += 1

    # Mechanism witnesses.
    witnesses = [
        {6: 1},        # endpoint candidate p=13
        {13: 1},       # denominator candidate p=13
        {1: 19},       # factorial candidate p=19
        {3: 1},        # cancellation can prune but cannot create candidate credit
        {6: 1, 3: 1},  # mixed balance
    ]
    for m in witnesses:
        cand = candidate_set(m)
        bound = candidate_bound(m)
        full = target_primes_upto(bound)
        assert max([0] + [gamma(p, m) for p in cand]) == max(
            [0] + [gamma(p, m) for p in full]
        )

    print("status=PASS")
    print(f"vectors_checked={checked}")
    print(f"outside_candidate_prime_checks={outside_checked}")
    print(f"vectors_with_strict_candidate_reduction={strict_reductions}")
    print("witness_candidate_sets=")
    for m in witnesses:
        print(m, sorted(candidate_set(m)))


if __name__ == "__main__":
    main()
