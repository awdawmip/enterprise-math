#!/usr/bin/env python3
"""Exact/regression checks for the P022 first-reentry fixed Franel kernel.

The universal statement proved in the return is an exact reduction to a Hahn
polynomial value.  The finite census below is regression/falsification only.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def inv(a: int, p: int) -> int:
    return pow(a % p, -1, p)


def poch(a: int, k: int) -> int:
    out = 1
    for j in range(k):
        out *= a + j
    return out


def hahn_diag_exact(n: int) -> Fraction:
    """Q_n(n;-3n,n-1,3n) in the DLMF Hahn normalization."""
    out = Fraction(0, 1)
    for j in range(n + 1):
        out += Fraction(
            poch(-n, j) ** 3,
            poch(1 - 3 * n, j) * poch(-3 * n, j) * math.factorial(j),
        )
    return out


def binomial_diag_exact(n: int) -> Fraction:
    return sum(
        (
            Fraction((-1) ** j * math.comb(n, j) ** 3,
                     math.comb(3 * n - 1, j) * math.comb(3 * n, j))
            for j in range(n + 1)
        ),
        Fraction(0, 1),
    )


def hahn_diag_mod(n: int, p: int) -> int:
    """Same Hahn diagonal, evaluated termwise in F_p."""
    term = total = 1
    for j in range(n):
        numerator = pow((j - n) % p, 3, p)
        denominator = ((j + 1 - 3 * n) * (j - 3 * n) * (j + 1)) % p
        term = term * numerator % p * inv(denominator, p) % p
        total = (total + term) % p
    return total


def fixed_rational_kernel_mod(n: int, p: int) -> int:
    """R_m(p), with n=3m, in the original fixed rational parameters."""
    a = -inv(6, p) % p
    b = inv(2, p)
    c = -inv(2, p) % p
    term = total = 1
    for j in range(n):
        denominator = ((b + j) * (c + j) * (j + 1)) % p
        term = term * pow((a + j) % p, 3, p) % p * inv(denominator, p) % p
        total = (total + term) % p
    return total


def franel_mod(r: int, p: int) -> int:
    """F_r mod p from the Franel three-term recurrence."""
    if r == 0:
        return 1
    prev, cur = 1, 2 % p
    if r == 1:
        return cur
    for k in range(1, r):
        rhs = ((7 * k * k + 7 * k + 2) * cur + 8 * k * k * prev) % p
        nxt = rhs * inv((k + 1) ** 2, p) % p
        prev, cur = cur, nxt
    return cur


def franel_to_hahn_unit(n: int, p: int) -> int:
    """Unit U with F_(2n) == U*Q_n(n;-3n,n-1,3n) (mod p)."""
    a = b = nf = 1
    for j in range(n):
        a = a * (2 * n + j) % p
        b = b * (2 * n + 1 + j) % p
        nf = nf * (j + 1) % p
    return (
        pow(2, 2 * n, p)
        * ((-1) ** n % p)
        * a % p
        * b % p
        * inv(nf * nf, p)
    ) % p


def sieve(limit: int) -> list[bool]:
    prime = [True] * (limit + 1)
    if limit >= 0:
        prime[0] = False
    if limit >= 1:
        prime[1] = False
    for d in range(2, math.isqrt(limit) + 1):
        if prime[d]:
            for k in range(d * d, limit + 1, d):
                prime[k] = False
    return prime


def exact_identity_checks() -> None:
    for n in range(1, 13):
        assert hahn_diag_exact(n) == binomial_diag_exact(n)


def regression(limit: int) -> dict[str, object]:
    prime = sieve(limit + 2)
    total = 0
    admissible = 0
    all_zeros: list[dict[str, int]] = []
    admissible_zeros: list[dict[str, int]] = []
    residue_counts = {5: 0, 11: 0, 17: 0}

    for n in range(1, (limit + 1) // 6 + 1):
        p = 6 * n - 1
        if p >= limit or not prime[p]:
            continue
        total += 1
        residue_counts[p % 18] = residue_counts.get(p % 18, 0) + 1

        h = hahn_diag_mod(n, p)
        assert h == fixed_rational_kernel_mod(n, p)
        f = franel_mod(2 * n, p)
        unit = franel_to_hahn_unit(n, p)
        assert unit != 0
        assert f == unit * h % p

        if h == 0:
            all_zeros.append({"n": n, "p": p})

        is_admissible = (
            n % 3 == 0
            and prime[4 * n - 1]
            and prime[4 * n + 1]
        )
        if is_admissible:
            admissible += 1
            if h == 0:
                admissible_zeros.append({"n": n, "p": p})

    return {
        "limit_exclusive": limit,
        "prime_boundaries_p_eq_6n_minus_1": total,
        "residue_counts_mod_18": residue_counts,
        "all_zero_witnesses": all_zeros,
        "admissible_twin_boundaries": admissible,
        "admissible_zero_witnesses": admissible_zeros,
        "proof_scope": "REGRESSION_ONLY_NOT_AN_ALL_PARAMETER_NONVANISHING_PROOF",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=50_000)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    exact_identity_checks()
    result = regression(args.limit)

    if args.limit == 50_000:
        assert result["prime_boundaries_p_eq_6n_minus_1"] == 2575
        assert result["admissible_twin_boundaries"] == 90
        assert result["all_zero_witnesses"] == [{"n": 1, "p": 5}, {"n": 25, "p": 149}]
        assert result["admissible_zero_witnesses"] == []

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
