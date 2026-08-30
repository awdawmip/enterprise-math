#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from enterprise_math.precision_signed_holonomy import (  # noqa: E402
    signed_defect_transport,
    signed_transport_is_coherent,
)

PRIMES = (2, 3, 5, 7, 11, 13)


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return p == d
        d += 1
    return True


def delta(p: int, n: int) -> int:
    assert is_prime(p)
    numerator = n - n**p
    assert numerator % p == 0
    return numerator // p


def defect(p: int, x: int, y: int) -> int:
    return delta(p, x + y) - delta(p, x) - delta(p, y)


def cross_effect(p: int, x: int, y: int) -> int:
    return -defect(p, x, y)


def t_polynomial(p: int, s: int, q: int) -> int:
    assert p % 2 == 1 and is_prime(p)
    total = 0
    for j in range(1, (p - 1) // 2 + 1):
        num = math.comb(p - j, j)
        den = p - j
        assert num % den == 0
        a = num // den
        total += (-1) ** (j + 1) * a * q**j * s ** (p - 2 * j - 1)
    return total


def t_derivative(p: int, s: int, q: int) -> int:
    assert p % 2 == 1 and is_prime(p)
    total = 0
    for j in range(1, (p - 1) // 2 + 1):
        num = math.comb(p - j, j)
        den = p - j
        assert num % den == 0
        a = num // den
        total += (
            (-1) ** (j + 1)
            * a
            * j
            * q ** (j - 1)
            * s ** (p - 2 * j - 1)
        )
    return total


def valid_pair_product(s: int, q: int) -> bool:
    disc = s * s - 4 * q
    if disc < 0:
        return False
    r = math.isqrt(disc)
    return r * r == disc and (s + r) % 2 == 0


def recover_product_odd(p: int, s: int, d: int) -> int:
    assert p % 2 == 1 and is_prime(p)
    if s == 0:
        raise ValueError("s=0 is the infinite-fiber singular hyperplane")
    if d % s != 0:
        raise ValueError("observation is outside the integer defect image")
    target = -d // s
    hi = (s * s) // 4

    lo = -1
    while t_polynomial(p, s, lo) > target:
        lo *= 2

    left, right = lo, hi
    while left <= right:
        mid = (left + right) // 2
        value = t_polynomial(p, s, mid)
        if value < target:
            left = mid + 1
        elif value > target:
            right = mid - 1
        else:
            if not valid_pair_product(s, mid):
                raise ValueError("unique algebraic q is outside the integer-pair image")
            return mid
    raise ValueError("observation is outside the semantic image")


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("v_p(0) is not used in this checker")
    n = abs(n)
    out = 0
    while n % p == 0:
        out += 1
        n //= p
    return out


def finite_log(p: int, z: int) -> int:
    z %= p
    return sum(pow(z, i, p) * pow(i, -1, p) for i in range(1, p)) % p


def cyclotomic_division(coeffs: list[int]) -> tuple[list[int], tuple[int, int]]:
    """Divide low-to-high coeffs by t^2+t+1; divisor is monic."""
    r = coeffs[:]
    n = len(r) - 1
    if n < 2:
        return [], (r[0] if r else 0, r[1] if len(r) > 1 else 0)
    quotient = [0] * (n - 1)
    for degree in range(n, 1, -1):
        c = r[degree]
        quotient[degree - 2] = c
        r[degree] -= c
        r[degree - 1] -= c
        r[degree - 2] -= c
    return quotient, (r[0], r[1])


def cyclotomic_multiplicity(p: int) -> int:
    # C_p(1,t)=((1+t)^p-1-t^p)/p.
    coeffs = [0] * (p + 1)
    for k in range(1, p):
        assert math.comb(p, k) % p == 0
        coeffs[k] = math.comb(p, k) // p
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    multiplicity = 0
    while len(coeffs) >= 3:
        q, rem = cyclotomic_division(coeffs)
        if rem != (0, 0):
            break
        multiplicity += 1
        coeffs = q
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
    return multiplicity


def main() -> int:
    counts: dict[str, int] = {}

    integrality = 0
    for p in PRIMES:
        for n in range(-25, 26):
            _ = delta(p, n)
            integrality += 1
        for i in range(1, p):
            assert math.comb(p, i) % p == 0
            assert vp(math.comb(p, i), p) == 1
            integrality += 1
    counts["integrality_and_unit_coefficients"] = integrality

    low_prime = 0
    for x in range(-12, 13):
        for y in range(-12, 13):
            s = x + y
            q = x * y
            assert defect(2, x, y) == -q
            assert defect(3, x, y) == -s * q
            assert defect(5, x, y) == -s * q * (s * s - q)
            assert defect(7, x, y) == -s * q * (s * s - q) ** 2
            low_prime += 4
    counts["p2_p3_p5_p7_exact_formulas"] = low_prime

    symmetric = 0
    for p in (3, 5, 7, 11, 13, 17):
        for x in range(-8, 9):
            for y in range(-8, 9):
                s = x + y
                q = x * y
                if s != 0:
                    assert cross_effect(p, x, y) == s * t_polynomial(p, s, q)
                else:
                    assert cross_effect(p, x, y) == 0
                symmetric += 1
    counts["odd_symmetric_polynomial_identity"] = symmetric

    monotonic = 0
    for p in (3, 5, 7, 11, 13, 17, 19):
        for s in range(-10, 11):
            if s == 0:
                continue
            hi = (s * s) // 4
            for q in range(-40, hi + 1):
                assert t_derivative(p, s, q) > 0
                monotonic += 1
    counts["strict_semantic_domain_monotonicity"] = monotonic

    reconstruction = 0
    for p in (3, 5, 7, 11, 13):
        for x in range(-18, 19):
            for y in range(-18, 19):
                s = x + y
                d = defect(p, x, y)
                if s == 0:
                    assert d == 0
                    continue
                assert recover_product_odd(p, s, d) == x * y
                reconstruction += 1
    counts["odd_product_reconstruction"] = reconstruction

    assert defect(3, 1, -1) == defect(3, 2, -2) == defect(3, 17, -17) == 0
    assert len({1 * -1, 2 * -2, 17 * -17}) == 3
    counts["singular_hyperplane_witnesses"] = 3

    cocycle = 0
    for p in PRIMES:
        for x in range(-6, 7):
            for y in range(-6, 7):
                for z in range(-4, 5):
                    lhs = defect(p, x, y) + defect(p, x + y, z)
                    rhs = defect(p, y, z) + defect(p, x, y + z)
                    assert lhs == rhs
                    cocycle += 1
    counts["coboundary_cocycle"] = cocycle

    expected_mult = {3: 0, 5: 1, 7: 2, 11: 1, 13: 2, 17: 1, 19: 2, 23: 1, 31: 2}
    for p, expected in expected_mult.items():
        assert cyclotomic_multiplicity(p) == expected
    counts["eisenstein_norm_exact_multiplicity"] = len(expected_mult)

    unequal = 0
    for p in (3, 5, 7, 11, 13):
        units = [u for u in (-4, -3, -2, -1, 1, 2, 3, 4) if u % p]
        for a in range(3):
            for b in range(3):
                if a == b:
                    continue
                for u in units:
                    for v in units:
                        x = p**a * u
                        y = p**b * v
                        d = defect(p, x, y)
                        assert d != 0
                        assert vp(d, p) == (p - 1) * min(a, b) + max(a, b)
                        unequal += 1
    counts["unequal_p_valuation_exact_law"] = unequal

    finite_log_checks = 0
    for p in (3, 5, 7, 11, 13, 17, 59):
        for u in range(1, min(p, 10)):
            for v in range(1, min(p, 10)):
                if u % p == 0 or v % p == 0:
                    continue
                z = (-u * pow(v, -1, p)) % p
                lhs = defect(p, u, v) * pow(pow(v, p, p), -1, p) % p
                assert lhs == finite_log(p, z)
                finite_log_checks += 1
    counts["equal_valuation_finite_log_residue"] = finite_log_checks

    roots59 = [z for z in range(59) if finite_log(59, z) == 0]
    assert roots59 == [0, 1, 4, 5, 12, 15, 16, 21, 39, 44, 45, 48, 55, 56]
    d59 = defect(59, 3, 1)
    assert vp(d59, 59) == 1
    assert (3 + 1) % 59 != 0
    assert (3 * 3 + 3 + 1) % 59 != 0
    d7 = defect(7, 2, 1)
    assert d7 == -294 and vp(d7, 7) == 2 and (2 * 2 + 2 + 1) == 7
    counts["finite_log_extra_root_and_norm_witnesses"] = 2

    transport = 0
    for p in (2, 3, 5, 7):
        for x in range(-6, 7):
            for y in range(-6, 7):
                base = delta(p, x) + delta(p, y)
                d = defect(p, x, y)
                for modulus in (2, 3, 5, 7):
                    visible = signed_defect_transport(modulus, base, d)
                    assert visible == delta(p, x + y) // modulus - base // modulus
                    assert signed_transport_is_coherent(3, modulus, base, d)
                    transport += 1
    counts["T9_signed_transport_reuse"] = transport

    total = sum(counts.values())
    print(json.dumps(
        {
            "status": "PASS",
            "task": "RS-ADDMUL-DELTA-FROBENIUS-DEFECT-TOWER",
            "checks": counts,
            "total_assertion_families_instantiated": total,
            "t9_reuse": "REUSE_EXECUTED",
            "method_harvest": "RESULT_ONLY",
        },
        sort_keys=True,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
