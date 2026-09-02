#!/usr/bin/env python3
"""Focused executable probe for R005-A witness-cover formalization.

This probe is deliberately finite and exact.  It does not implement new
primality algorithms; it validates the structural claims used by the Lean
candidate:
- cover criterion / pseudoprime fiber
- forced witness <-> mandatory witness on a safe full witness universe
- unique least cover iff forced basis covers
- root-factor unique least basis
- Miller--Rabin minimum-cover antichain with empty forced basis
- pass-strength versus binary-partition refinement boundary
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, isqrt
import json


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


def covers_composites(states, prime, pass_test, witnesses) -> bool:
    witnesses = tuple(witnesses)
    return all(
        prime(x) or any(not pass_test(w, x) for w in witnesses)
        for x in states
    )


def pseudoprimes(states, prime, pass_test, witnesses):
    witnesses = tuple(witnesses)
    return [
        x for x in states
        if not prime(x) and all(pass_test(w, x) for w in witnesses)
    ]


def forced_witnesses(states, prime, pass_test, universe):
    universe = tuple(universe)
    forced = {}
    for w in universe:
        collisions = []
        for x in states:
            if prime(x) or pass_test(w, x):
                continue
            if all(v == w or pass_test(v, x) for v in universe):
                collisions.append(x)
        if collisions:
            forced[w] = collisions
    return forced


def safe_subsets(states, prime, pass_test, universe):
    universe = tuple(universe)
    out = []
    for k in range(len(universe) + 1):
        for subset in combinations(universe, k):
            if covers_composites(states, prime, pass_test, subset):
                out.append(subset)
    return out


def minimum_safe_subsets(states, prime, pass_test, universe):
    universe = tuple(universe)
    for k in range(len(universe) + 1):
        safe = [
            subset
            for subset in combinations(universe, k)
            if covers_composites(states, prime, pass_test, subset)
        ]
        if safe:
            return safe
    return []


def binary_refines(states, f, g) -> bool:
    """Partition induced by f refines the partition induced by g."""
    for x in states:
        for y in states:
            if f(x) == f(y) and g(x) != g(y):
                return False
    return True


def fermat2(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or gcd(2, n) != 1:
        return False
    return pow(2, n - 1, n) == 1


def mr(n: int, a: int) -> bool:
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False
    a %= n
    if a in (0, 1):
        return True
    if gcd(a, n) != 1:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1:
            return True
    return False


def root_factor_pass(p: int, n: int) -> bool:
    return not (p * p <= n and n % p == 0)


def main():
    # Root-factor instance: exhaustive finite cover lattice at N=30.
    N = 30
    states = tuple(range(2, N + 1))
    witness_universe = tuple(n for n in range(2, N + 1) if is_prime(n))
    root_basis = tuple(p for p in witness_universe if p <= isqrt(N))

    root_forced = forced_witnesses(
        states, is_prime, root_factor_pass, witness_universe
    )
    root_safe = safe_subsets(
        states, is_prime, root_factor_pass, witness_universe
    )

    assert covers_composites(states, is_prime, root_factor_pass, witness_universe)
    assert set(root_forced) == set(root_basis)
    assert all(set(root_basis).issubset(A) for A in map(set, root_safe))
    assert tuple(root_basis) in root_safe
    assert pseudoprimes(states, is_prime, root_factor_pass, root_basis) == []

    # MR instance: exact bounded minimum cover + forced-basis boundary.
    mr_N = 100_000
    mr_states = tuple(
        n for n in range(3, mr_N + 1, 2)
        if not is_prime(n)
    )
    mr_bases = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)

    def mr_prime_false(_n):
        return False

    def mr_pass(a, n):
        return mr(n, a)

    mr_min = minimum_safe_subsets(
        mr_states, mr_prime_false, mr_pass, mr_bases
    )
    mr_forced = forced_witnesses(
        mr_states, mr_prime_false, mr_pass, mr_bases
    )

    assert len(mr_min) > 1
    assert mr_forced == {}
    assert not covers_composites(
        mr_states, mr_prime_false, mr_pass, tuple(mr_forced)
    )

    # T-A3 concrete boundary.
    boundary_states = (9, 17, 341)
    f = lambda n: mr(n, 2)       # stronger pass filter
    g = fermat2                  # weaker pass filter

    assert all(not f(n) or g(n) for n in boundary_states)
    assert g(341) and not f(341)
    assert f(17)
    assert not g(9)
    assert not binary_refines(boundary_states, f, g)
    assert not binary_refines(boundary_states, g, f)

    result = {
        "status": "R005-A witness-cover structural probe / exact finite",
        "root_factor": {
            "N": N,
            "witness_universe": witness_universe,
            "forced_basis": tuple(root_forced),
            "forced_collisions": {
                str(w): xs for w, xs in root_forced.items()
            },
            "unique_least_basis": root_basis,
            "safe_family_count": len(root_safe),
        },
        "miller_rabin": {
            "N": mr_N,
            "candidate_bases": mr_bases,
            "forced_basis": tuple(mr_forced),
            "minimum_safe_subsets": mr_min,
            "least_cover_exists": False,
        },
        "partition_boundary": {
            "states": boundary_states,
            "mr2_pass_implies_fermat2_pass": True,
            "mr2_refines_fermat2_partition": False,
            "fermat2_refines_mr2_partition": False,
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
