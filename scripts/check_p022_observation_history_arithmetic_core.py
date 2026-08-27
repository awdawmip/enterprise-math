#!/usr/bin/env python3
"""Exact checker for the P022 q=3r-1 boundary Franel reduction.

No external packages are required.

The checker certifies:
1. the MacMahon-term reduction
       F_(6m) == 2^(6m) * 3F2(-3m,6m,6m+1;1,1;1) (mod q),
   for q=18m-1 prime;
2. every term in the terminating kernel is a q-adic unit;
3. the standard terminating Weber-Erdelyi transformation orbit specialized
   to this kernel has 12 canonical parameter types and no direct
   cancellation or Saalschutz-balanced member;
4. the full twin-boundary census q<50000 contains 90 candidates and no
   Franel zero; the complete-escape survivor classes 17,35 mod 72 contain
   47 candidates and no Franel zero;
5. q=149, r=50 is a control counterexample showing q==2 (mod 3) alone does
   not force nonvanishing.
"""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
import argparse
import json


def primes_through(limit: int) -> tuple[int, ...]:
    if limit < 2:
        return ()
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= limit:
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
        p += 1
    return tuple(i for i in range(2, limit + 1) if sieve[i])


def franel_mod(n: int, prime: int) -> int:
    """F_n=sum C(n,k)^3 modulo prime, using exact modular binomial recurrence."""
    if n == 0:
        return 1 % prime
    inv = [0] * (n + 1)
    inv[1] = 1
    for k in range(2, n + 1):
        inv[k] = (-(prime // k) * inv[prime % k]) % prime
    choose = 1
    total = 1
    for k in range(1, n + 1):
        choose = choose * (n - k + 1) * inv[k] % prime
        total = (total + choose * choose % prime * choose) % prime
    return total


def boundary_kernel_mod(m: int, prime: int) -> int:
    """S_m = 3F2(-3m,6m,6m+1;1,1;1) modulo prime."""
    n = 3 * m
    term = 1
    total = 1
    for k in range(n):
        numerator = (-n + k) * (6 * m + k) * (6 * m + 1 + k)
        denominator = (k + 1) ** 3
        term = term * (numerator % prime) % prime
        term = term * pow(denominator % prime, -1, prime) % prime
        total = (total + term) % prime
    return total


def unit_kernel_holds(m: int, prime: int) -> bool:
    """Every factor in every S_m term lies strictly between -prime and prime."""
    n = 3 * m
    if prime != 18 * m - 1 or m < 1:
        return False
    # (-3m)_k uses -3m,...,-1; (6m)_k ends at 9m-1;
    # (6m+1)_k ends at 9m; k! ends at 3m.
    return 3 * m < prime and 9 * m < prime


# Affine parameter A*m+B used for an exact symbolic orbit check.
Affine = tuple[Fraction, Fraction]


def add(x: Affine, y: Affine) -> Affine:
    return (x[0] + y[0], x[1] + y[1])


def sub(x: Affine, y: Affine) -> Affine:
    return (x[0] - y[0], x[1] - y[1])


ONE: Affine = (Fraction(0), Fraction(1))
NEG_N: Affine = (Fraction(-3), Fraction(0))
N: Affine = (Fraction(3), Fraction(0))


def canonical(params: tuple[Affine, Affine, Affine, Affine]) -> tuple[Affine, ...]:
    a, b, d, e = params
    return tuple(sorted((a, b))) + tuple(sorted((d, e)))


def weber_erdelyi_step(
    params: tuple[Affine, Affine, Affine, Affine],
    numerator_choice: int,
    denominator_choice: int,
) -> tuple[Affine, ...]:
    """Specialize the terminating transform

    3F2(A,B,-N;D,E;1)
      = (D-A)_N/(D)_N
        3F2(A,E-B,-N;1+A-D-N,E;1),

    allowing numerator and denominator permutations before each step.
    """
    a, b, d, e = params
    nums = (a, b)
    dens = (d, e)
    A = nums[numerator_choice]
    B = nums[1 - numerator_choice]
    D = dens[denominator_choice]
    E = dens[1 - denominator_choice]
    return canonical(
        (
            A,
            sub(E, B),
            sub(add(ONE, sub(A, D)), N),
            E,
        )
    )


def terminating_orbit() -> set[tuple[Affine, ...]]:
    start = canonical(
        (
            (Fraction(6), Fraction(0)),
            (Fraction(6), Fraction(1)),
            ONE,
            ONE,
        )
    )
    seen = {start}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for ni in (0, 1):
            for di in (0, 1):
                nxt = weber_erdelyi_step(current, ni, di)
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
    return seen


def has_direct_cancellation(params: tuple[Affine, ...]) -> bool:
    a, b, d, e = params
    return any(num == den for num in (NEG_N, a, b) for den in (d, e))


def is_saalschutz_balanced(params: tuple[Affine, ...]) -> bool:
    a, b, d, e = params
    return add(add(add(NEG_N, a), b), ONE) == add(d, e)


def census(limit: int) -> dict:
    primes = primes_through(limit)
    prime_set = set(primes)
    candidates = []
    for q in primes:
        if q <= 3 or (q + 1) % 18:
            continue
        m = (q + 1) // 18
        left = 12 * m - 1
        right = 12 * m + 1
        if left not in prime_set or right not in prime_set:
            continue
        f = franel_mod(6 * m, q)
        kernel = boundary_kernel_mod(m, q)
        assert f == pow(2, 6 * m, q) * kernel % q
        assert unit_kernel_holds(m, q)
        candidates.append(
            {
                "m": m,
                "q": q,
                "q_mod_72": q % 72,
                "left_twin_prime": left,
                "right_twin_prime": right,
                "franel_mod_q": f,
            }
        )
    counts = Counter(row["q_mod_72"] for row in candidates)
    survivors = [row for row in candidates if row["q_mod_72"] in (17, 35)]
    return {
        "search_limit_q": limit,
        "candidate_count": len(candidates),
        "residue_class_counts": {str(k): counts[k] for k in sorted(counts)},
        "zero_count": sum(row["franel_mod_q"] == 0 for row in candidates),
        "survivor_count": len(survivors),
        "survivor_zero_count": sum(row["franel_mod_q"] == 0 for row in survivors),
        "candidates": candidates,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=50_000)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    orbit = terminating_orbit()
    assert len(orbit) == 12
    assert not any(has_direct_cancellation(item) for item in orbit)
    assert not any(is_saalschutz_balanced(item) for item in orbit)

    # General q == 2 mod 3 is not enough.
    assert franel_mod(50, 149) == 0

    result = census(args.limit)
    if args.limit == 50_000:
        assert result["candidate_count"] == 90
        assert result["residue_class_counts"] == {"17": 22, "35": 25, "53": 28, "71": 15}
        assert result["zero_count"] == 0
        assert result["survivor_count"] == 47
        assert result["survivor_zero_count"] == 0

    result["weber_erdelyi_canonical_orbit_size"] = len(orbit)
    result["direct_cancellation_members"] = 0
    result["saalschutz_balanced_members"] = 0
    result["control_q149_r50_franel_mod_q"] = franel_mod(50, 149)

    if args.json:
        print(json.dumps(result, sort_keys=True, indent=2))
    else:
        print(
            "PASS "
            f"limit={result['search_limit_q']} "
            f"candidates={result['candidate_count']} "
            f"survivors={result['survivor_count']} "
            f"zeros={result['zero_count']} "
            f"survivor_zeros={result['survivor_zero_count']} "
            f"orbit={len(orbit)}"
        )


if __name__ == "__main__":
    main()
