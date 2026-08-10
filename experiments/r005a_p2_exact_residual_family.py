#!/usr/bin/env python3
"""R005-A exact verifier for 49 square-basin no-least certificates.

This file does not claim the listed basins are exhaustive up to a cutoff.
It independently verifies 50 concrete residual composites in 49 basins.

For each certificate it checks:
- the declared prime factorization exactly;
- the residual composite lies in k^2 < n < (k+1)^2;
- every candidate support prime is genuinely non-forced, by exhaustively
  checking the T-A12 exclusive-collision forms q^e and q^e*r with r>k;
- every prime witness q<=floor(U^(1/4)) is forced;
- Omega(n)=3.

Thus these examples show the residual arity filtration is sharp at m=4:
the fourth-root core can be fully forced while an Omega=3 residual remains.
"""

from __future__ import annotations

from math import isqrt
import json

CERTIFICATES = [(25, 637, ((7, 2), (13, 1))), (47, 2299, ((11, 2), (19, 1))), (62, 3887, ((13, 2), (23, 1))), (123, 15317, ((17, 2), (53, 1))), (130, 16967, ((19, 2), (47, 1))), (151, 22831, ((17, 2), (79, 1))), (157, 24863, ((23, 2), (47, 1))), (162, 26353, ((19, 2), (73, 1))), (196, 38617, ((23, 2), (73, 1))), (217, 47291, ((19, 2), (131, 1))), (308, 95033, ((29, 2), (113, 1))), (364, 132799, ((41, 2), (79, 1))), (365, 133579, ((31, 2), (139, 1))), (479, 230297, ((41, 2), (137, 1))), (556, 309809, ((59, 2), (89, 1))), (888, 790079, ((73, 1), (79, 1), (137, 1))), (924, 855017, ((79, 2), (137, 1))), (935, 874903, ((83, 2), (127, 1))), (1008, 1017283, ((79, 2), (163, 1))), (1056, 1117139, ((79, 2), (179, 1))), (1078, 1163243, ((37, 1), (149, 1), (211, 1))), (1162, 1351447, ((43, 1), (53, 1), (593, 1))), (1290, 1665737, ((53, 2), (593, 1))), (1345, 1809719, ((71, 2), (359, 1))), (1454, 2114923, ((83, 2), (307, 1))), (1511, 2284901, ((67, 2), (509, 1))), (1541, 2375507, ((107, 1), (149, 2))), (1577, 2488643, ((73, 2), (467, 1))), (1612, 2598923, ((107, 2), (227, 1))), (1627, 2649463, ((109, 2), (223, 1))), (1679, 2819527, ((127, 1), (149, 2))), (1781, 3172511, ((101, 2), (311, 1))), (1781, 3175339, ((101, 1), (149, 1), (211, 1))), (1790, 3205019, ((113, 2), (251, 1))), (1865, 3481133, ((109, 2), (293, 1))), (1897, 3600953, ((101, 2), (353, 1))), (2073, 4299913, ((97, 2), (457, 1))), (2164, 4684411, ((149, 2), (211, 1))), (2850, 8126977, ((137, 2), (433, 1))), (4412, 19469647, ((193, 1), (281, 1), (359, 1))), (5833, 34032191, ((281, 2), (431, 1))), (5834, 34038679, ((181, 2), (1039, 1))), (6339, 40191149, ((281, 2), (509, 1))), (7289, 53140753, ((281, 2), (673, 1))), (8584, 73697461, ((199, 2), (1861, 1))), (9369, 87788213, ((397, 2), (557, 1))), (11226, 126024953, ((461, 2), (593, 1))), (11433, 130714841, ((353, 2), (1049, 1))), (13006, 169179893, ((509, 2), (653, 1))), (35901, 1288933697, ((641, 2), (3137, 1)))]


def sieve(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start:limit+1:p] = b"\x00" * (((limit-start)//p)+1)
    return [n for n in range(2, limit + 1) if flags[n]]


BASE_PRIMES = sieve(50_000)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in BASE_PRIMES:
        if p * p > n:
            return True
        if n % p == 0:
            return n == p
    raise ValueError("prime table too short for exact trial division")


def prime_exists(lo: int, hi: int) -> bool:
    if lo > hi:
        return False
    if lo <= 2 <= hi:
        return True
    n = max(lo, 3)
    if n % 2 == 0:
        n += 1
    while n <= hi:
        if is_prime(n):
            return True
        n += 2
    return False


def integer_root(n: int, m: int) -> int:
    lo, hi = 0, 1
    while hi**m <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**m <= n:
            lo = mid
        else:
            hi = mid
    return lo


def witness_forced(k: int, q: int) -> bool:
    """Exact T-A12 forcedness for a square-basin divisor witness q<=k."""
    A = k * k
    U = A + 2 * k
    qe = q
    e = 1
    while qe <= U:
        if e >= 2 and A < qe <= U:
            return True

        lo = max(k + 1, A // qe + 1)
        hi = U // qe
        if prime_exists(lo, hi):
            return True

        if qe > U // q:
            break
        qe *= q
        e += 1
    return False


def factor_product(factors: tuple[tuple[int, int], ...]) -> int:
    out = 1
    for p, e in factors:
        out *= p**e
    return out


def main() -> None:
    rows = []
    basin_count = len({k for k, _, _ in CERTIFICATES})
    assert basin_count == 49

    for k, n, factors in CERTIFICATES:
        A = k * k
        U = A + 2 * k
        assert A < n <= U
        assert factor_product(factors) == n
        assert all(is_prime(p) for p, _ in factors)

        omega = sum(e for _, e in factors)
        assert omega == 3

        support = tuple(sorted(p for p, _ in factors if p <= k))
        assert len(set(support)) >= 2

        assert all(not witness_forced(k, q) for q in support)

        fourth_root = integer_root(U, 4)
        fourth_core = tuple(p for p in BASE_PRIMES if p <= fourth_root)
        assert all(witness_forced(k, q) for q in fourth_core)

        cube_root = integer_root(U, 3)
        assert any(q <= cube_root for q in support)

        rows.append({
            "k": k,
            "n": n,
            "factors": factors,
            "support": support,
            "omega": omega,
            "fourth_root_core": fourth_root,
            "cube_root_core": cube_root,
        })

    result = {
        "status": "R005-A EXACT SQUARE-BASIN RESIDUAL CERTIFICATE FAMILY / NOT EXHAUSTIVENESS CLAIM",
        "verified_basin_count": basin_count,
        "verified_residual_count": len(rows),
        "all_residual_omega": 3,
        "all_fourth_root_cores_forced": True,
        "all_examples_have_nonforced_support_in_cube_root_core": True,
        "largest_k": max(row["k"] for row in rows),
        "interpretation": (
            "These examples make the m=4 residual arity bound sharp: "
            "forcing the fourth-root core can leave Omega=3 residuals, "
            "while forcing the cube-root core would eliminate residuals."
        ),
        "rows": rows,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
