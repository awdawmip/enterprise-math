#!/usr/bin/env python3
"""Exact/brute-force checker for the odd-curvature filament deformation theorem."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb, gcd, isqrt, lcm


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def eps(n: int) -> int:
    return n & 1


def F(B: int, H: int, r: int) -> int:
    assert B % 2 == 1 and B > 0
    return H + (B * r * r + eps(r)) // 2


def window_formula(B: int, H: int, R: int, j: int) -> int:
    c = F(B, H, R)
    chi = 1 if R % 2 == 0 else -1
    return c + B * R * j + (B * j * j + chi * eps(j)) // 2


def code_words(B: int, M: int, k: int) -> set[tuple[int, ...]]:
    out = set()
    # 4M covers a multiple of both relevant periods for the finite checks below.
    for H in range(M):
        for R in range(4 * M):
            out.add(tuple(F(B, H, R + j) % M for j in range(k)))
    return out


def eta(B: int, chi: int, j: int) -> int:
    return (B * j * j + chi * eps(j)) // 2


def determinant_twice(B: int, chi: int, i: int, j: int, l: int) -> int:
    # Twice det[[1,x,eta_x]] = det[[1,x,2 eta_x]], avoiding fractions.
    rows = [(1, x, B * x * x + chi * eps(x)) for x in (i, j, l)]
    (a1, b1, c1), (a2, b2, c2), (a3, b3, c3) = rows
    return (
        a1 * (b2 * c3 - c2 * b3)
        - b1 * (a2 * c3 - c2 * a3)
        + c1 * (a2 * b3 - b2 * a3)
    )


def line_defect(B: int, k: int, q: int, chi: int, exponent: int = 1) -> tuple[int, Counter[int]]:
    modulus = q ** exponent
    spectrum: Counter[int] = Counter()
    offsets = [eta(B, chi, j) % modulus for j in range(k)]
    for a in range(modulus):
        for b in range(modulus):
            zeros = sum((a + b * j + offsets[j]) % modulus == 0 for j in range(k))
            spectrum[zeros] += 1
    delta = sum(count * comb(m - 1, 2) for m, count in spectrum.items() if m >= 3)
    return delta, spectrum


def legendre(a: int, q: int) -> int:
    a %= q
    if a == 0:
        return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else -1


def transparency_formula(B: int, q: int) -> int:
    if B % q == 0:
        return q - 2
    return (q - 3 + legendre(B, q) + legendre(-B, q)) // 4


def transparency_bruteforce(B: int, q: int) -> int:
    inv2 = pow(2, -1, q)
    good = 0
    for H in range(q):
        even_hit = any((H + 2 * B * m * m) % q == 0 for m in range(q))
        odd_hit = any(
            (H + (B * x * x + 1) * inv2) % q == 0
            for x in range(q)
        )
        if not even_hit and not odd_hit:
            good += 1
    return good


def max_periodic_nonzero_run(B: int, H: int, q: int = 5) -> int | None:
    seq = [F(B, H, r) % q for r in range(2 * q)]
    if all(x != 0 for x in seq):
        return None
    cur = best = 0
    for x in seq * 2:
        if x != 0:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return min(best, len(seq) - 1)


def main() -> None:
    # Window identity, alternating curvature, and universal fourth-order recurrence.
    for B in (1, 3, 5, 7, 9, 11):
        for H in (-3, 0, 4):
            for R in range(8):
                vals = [F(B, H, R + j) for j in range(10)]
                assert vals == [window_formula(B, H, R, j) for j in range(10)]
                chi = 1 if R % 2 == 0 else -1
                for j in range(8):
                    assert vals[j] - 2 * vals[j + 1] + vals[j + 2] == B - chi * ((-1) ** j)
                for j in range(6):
                    assert vals[j + 4] - 2 * vals[j + 3] + 2 * vals[j + 1] - vals[j] == 0

    # Exact finite-quotient cardinality across a nontrivial grid.
    for B in (1, 3, 5, 7, 9):
        for M in range(2, 16):
            for k in (3, 4, 6):
                got = len(code_words(B, M, k))
                expected = 2 if M == 2 else M * lcm(2, M // gcd(B, M))
                assert got == expected, (B, M, k, got, expected)

    # Determinant factorization predicts every higher concurrence in the distinct-slope range.
    for B in (3, 5, 7, 9, 11):
        for k in range(5, 10):
            determinants = {
                abs(determinant_twice(B, chi, *triple))
                for triple in combinations(range(k), 3)
                for chi in (1, -1)
            }
            for q in range(k, 50):
                if not is_prime(q):
                    continue
                predicted = any(d % q == 0 for d in determinants)
                observed = False
                for chi in (1, -1):
                    delta, _ = line_defect(B, k, q, chi)
                    observed |= delta > 0
                assert predicted == observed, (B, k, q, predicted, observed)

    # Transparency formula, including the q|B branch.
    for B in (1, 3, 5, 7, 9, 11, 13, 15):
        for q in (5, 7, 11, 13, 17, 19, 23):
            assert transparency_formula(B, q) == transparency_bruteforce(B, q), (B, q)

    # q=5 phase diagram and exact sharp run-9 breaker phase.
    for Bmod in range(5):
        B = Bmod if Bmod % 2 == 1 else Bmod + 5
        # Keep a positive odd representative of each residue class mod5.
        if B <= 0:
            B += 10
        t = transparency_bruteforce(B, 5)
        if Bmod == 0:
            assert t == 3
        elif Bmod in (1, 4):
            assert t == 1
        else:
            assert Bmod in (2, 3) and t == 0
            runs = [max_periodic_nonzero_run(B, H, 5) for H in range(5)]
            assert max(r for r in runs if r is not None) == 9
            assert max_periodic_nonzero_run(B, 0, 5) == 9
            assert max_periodic_nonzero_run(B, 2, 5) == 9

    # The native B=3 channel is in the nonresidue/breaker phase.
    assert legendre(3, 5) == -1
    assert transparency_formula(3, 5) == 0

    # p-adic depth need not be one in the deformation family.
    # B=49, k=5, q=5, chi=-1 has a mixed obstruction of valuation two.
    d1, _ = line_defect(49, 5, 5, -1, 1)
    d2, _ = line_defect(49, 5, 5, -1, 2)
    d3, _ = line_defect(49, 5, 5, -1, 3)
    assert d1 > 0 and d2 > 0 and d3 == 0

    print("ODD_CURVATURE_WINDOW_IDENTITY=PASS")
    print("CURVATURE_AND_RECURRENCE=PASS")
    print("FINITE_QUOTIENT_CARDINALITY=PASS")
    print("DISCRIMINANT_EXCEPTION_PREDICTION=PASS")
    print("TRANSPARENCY_FORMULA=PASS")
    print("MOD5_PHASE_DIAGRAM=PASS")
    print("NONRESIDUE_PHASE_SHARP_RUN_CAP=9")
    print("NATIVE_B3_LEGENDRE_3_OVER_5=-1")
    print("DEFORMATION_PADIC_DEPTH_GT1_WITNESS=B49_Q5=PASS")


if __name__ == "__main__":
    main()
