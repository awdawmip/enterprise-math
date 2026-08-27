#!/usr/bin/env python3
"""Exact/regression checker for P022 composite Franel equal-depth escape.

Proof-level content checked here:
  * half-integer basis recurrence and exact Casoratian;
  * denominator-cleared K_d normalization of the midpoint companion G_d;
  * first derivative H_d=B_d'(0) of the midpoint-offset transport;
  * midpoint q^2 expansion F_m = A_q - 3 q T_q (mod q^2);
  * harmonic pairing U_q = 2 T_q (mod q).

Finite scans are explicitly diagnostic only.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
import argparse


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


def odd_double_factorial(odd: int) -> int:
    result = 1
    for value in range(1, odd + 1, 2):
        result *= value
    return result


def integer_midpoint_companion(offset: int) -> int:
    if offset == 0:
        return 0
    if offset == 1:
        return 1
    km1, kd = 0, 1
    for d in range(1, offset):
        kp1 = (28 * d * d + 1) * kd + 8 * (2 * d - 1) ** 4 * km1
        km1, kd = kd, kp1
    return kd


def integer_midpoint_companion_mod(offset: int, prime: int) -> int:
    if offset == 0:
        return 0
    if offset == 1:
        return 1 % prime
    km1, kd = 0, 1
    for d in range(1, offset):
        kp1 = (
            (28 * d * d + 1) * kd
            + 8 * pow(2 * d - 1, 4, prime) * km1
        ) % prime
        km1, kd = kd, kp1
    return kd


def midpoint_basis(max_offset: int) -> tuple[list[Fraction], list[Fraction]]:
    e = [Fraction(0) for _ in range(max_offset + 1)]
    g = [Fraction(0) for _ in range(max_offset + 1)]
    e[0] = Fraction(1)
    if max_offset >= 1:
        g[1] = Fraction(1)
    for d in range(1, max_offset):
        denominator = 8 * (2 * d + 1) ** 2
        e[d + 1] = Fraction(
            (2 * d - 1) ** 2 * e[d - 1] - (28 * d * d + 1) * e[d],
            denominator,
        )
        g[d + 1] = Fraction(
            (2 * d - 1) ** 2 * g[d - 1] - (28 * d * d + 1) * g[d],
            denominator,
        )
    return e, g


def midpoint_companion_derivative(
    g: list[Fraction], max_offset: int
) -> list[Fraction]:
    h = [Fraction(0) for _ in range(max_offset + 1)]
    for d in range(1, max_offset):
        denominator = 8 * (2 * d + 1) ** 2
        numerator = (
            (2 * d - 1) ** 2 * h[d - 1]
            - (28 * d * d + 1) * h[d]
            - 2 * (2 * d - 1) * g[d - 1]
            + 28 * d * g[d]
            + 16 * (2 * d + 1) * g[d + 1]
        )
        h[d + 1] = Fraction(numerator, denominator)
    return h


@dataclass(frozen=True)
class Dual:
    value: Fraction
    deriv: Fraction

    def __add__(self, other: "Dual | int") -> "Dual":
        other = as_dual(other)
        return Dual(self.value + other.value, self.deriv + other.deriv)

    __radd__ = __add__

    def __neg__(self) -> "Dual":
        return Dual(-self.value, -self.deriv)

    def __sub__(self, other: "Dual | int") -> "Dual":
        return self + (-as_dual(other))

    def __rsub__(self, other: "Dual | int") -> "Dual":
        return as_dual(other) - self

    def __mul__(self, other: "Dual | int") -> "Dual":
        other = as_dual(other)
        return Dual(
            self.value * other.value,
            self.deriv * other.value + self.value * other.deriv,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: "Dual | int") -> "Dual":
        other = as_dual(other)
        if other.value == 0:
            raise ZeroDivisionError
        return Dual(
            self.value / other.value,
            (self.deriv * other.value - self.value * other.deriv)
            / (other.value * other.value),
        )

    def __pow__(self, exponent: int) -> "Dual":
        if exponent == 0:
            return Dual(Fraction(1), Fraction(0))
        if exponent == 2:
            return self * self
        raise ValueError("only exponents 0 and 2 are needed")


def as_dual(value: Dual | int) -> Dual:
    if isinstance(value, Dual):
        return value
    return Dual(Fraction(value), Fraction(0))


def companion_dual(max_offset: int) -> list[Dual]:
    """Evaluate B_d(t) at t=0 with t carrying derivative one."""
    t = Dual(Fraction(0), Fraction(1))
    b = [Dual(Fraction(0), Fraction(0)) for _ in range(max_offset + 1)]
    if max_offset >= 1:
        b[1] = Dual(Fraction(1), Fraction(0))
    for d in range(1, max_offset):
        a = t - (2 * d + 1)
        c = t - (2 * d - 1)
        q = 7 * a * c + 8
        b[d + 1] = (c**2 * b[d - 1] - q * b[d]) / (8 * a**2)
    return b


def franel_mod(n: int, prime: int) -> int:
    choose = 1
    total = 1
    for j in range(n):
        choose = choose * (n - j) % prime
        choose = choose * pow(j + 1, -1, prime) % prime
        total = (total + choose * choose % prime * choose) % prime
    return total


def harmonic_mod(n: int, prime: int) -> int:
    return sum(pow(r, -1, prime) for r in range(1, n + 1)) % prime


def midpoint_q2_packet(prime: int) -> tuple[int, int, int, int, int]:
    """Return (A mod q^2, T mod q, U mod q, F_m mod q^2, m)."""
    m = (prime - 1) // 2
    q2 = prime * prime
    a_sum = 0
    t_sum = 0
    u_sum = 0
    inv2 = pow(2, -1, prime)
    for j in range(m + 1):
        central = comb(2 * j, j) % q2
        a_j_q2 = (
            pow(-1, j, q2)
            * pow(central, 3, q2)
            * pow(pow(64, j, q2), -1, q2)
        ) % q2
        a_sum = (a_sum + a_j_q2) % q2
        a_j = a_j_q2 % prime
        h_j = harmonic_mod(j, prime)
        h_2j = harmonic_mod(2 * j, prime)
        odd_harmonic = (h_2j - inv2 * h_j) % prime
        t_sum = (t_sum + a_j * odd_harmonic) % prime
        u_sum = (u_sum + a_j * h_j) % prime

    franel = sum(comb(m, j) ** 3 for j in range(m + 1)) % q2
    return a_sum, t_sum, u_sum, franel, m


def exact_algebra_checks(max_offset: int = 12) -> None:
    e, g = midpoint_basis(max_offset)
    h = midpoint_companion_derivative(g, max_offset)
    dual = companion_dual(max_offset)

    for d in range(max_offset + 1):
        assert dual[d].value == g[d], ("G dual mismatch", d)
        assert dual[d].deriv == h[d], ("H dual mismatch", d)

    for d in range(max_offset):
        x_d = (-8) ** d * e[d]
        y_d = (-8) ** d * g[d]
        x_next = (-8) ** (d + 1) * e[d + 1]
        y_next = (-8) ** (d + 1) * g[d + 1]
        casoratian = x_d * y_next - x_next * y_d
        expected = Fraction((-8) ** (d + 1), (2 * d + 1) ** 2)
        assert casoratian == expected, ("Casoratian mismatch", d)

    for d in range(1, max_offset + 1):
        normalizer = odd_double_factorial(2 * d - 1) ** 2 * (-8) ** (d - 1)
        normalized = normalizer * g[d]
        assert normalized.denominator == 1, ("K integrality", d)
        assert normalized.numerator == integer_midpoint_companion(d), (
            "K normalization mismatch",
            d,
        )


def midpoint_expansion_checks(bound: int = 300) -> int:
    checked = 0
    for q in range(5, bound, 2):
        if q % 24 not in (5, 23) or not is_prime(q):
            continue
        a_sum, t_sum, u_sum, franel, _m = midpoint_q2_packet(q)
        q2 = q * q
        assert (franel - (a_sum - 3 * q * t_sum)) % q2 == 0, (
            "midpoint q^2 expansion failed",
            q,
        )
        assert (u_sum - 2 * t_sum) % q == 0, ("harmonic pairing failed", q)
        # Forced-midpoint sectors q=5,23 (mod 24) lie in q=5,7 (mod 8).
        assert franel % q == 0, ("forced midpoint zero failed", q)
        assert a_sum % q == 0, ("base A_q divisibility failed", q)
        c_q = (a_sum // q) % q
        quotient = (franel // q) % q
        assert quotient == (c_q - 3 * t_sum) % q
        assert quotient == (c_q - 3 * pow(2, -1, q) * u_sum) % q
        checked += 1
    return checked


def diagnostic_scan(bound: int) -> tuple[int, list[int]]:
    """Diagnostic only: compare q|F_(2k-1) with q|K_k and list zeros."""
    checked = 0
    zeros: list[int] = []
    for q in range(5, bound, 2):
        if q % 24 not in (5, 23) or not is_prime(q):
            continue
        k = (q + 1) // 6
        franel_zero = franel_mod(2 * k - 1, q) == 0
        companion_zero = integer_midpoint_companion_mod(k, q) == 0
        assert franel_zero == companion_zero, ("companion bridge mismatch", q)
        if companion_zero:
            zeros.append(q)
        checked += 1
    return checked, zeros


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scan-bound",
        type=int,
        default=20_000,
        help="finite diagnostic bound; not a proof cutoff",
    )
    args = parser.parse_args()

    exact_algebra_checks()
    midpoint_checked = midpoint_expansion_checks()
    scanned, zeros = diagnostic_scan(args.scan_bound)

    print("EXACT_ALGEBRA=PASS")
    print(f"MIDPOINT_Q2_PACKETS=PASS ({midpoint_checked} target-sector primes < 300)")
    print(
        "FINITE_DIAGNOSTIC=PASS "
        f"({scanned} target-sector primes < {args.scan_bound}; "
        f"q|K_k witnesses={len(zeros)})"
    )
    if zeros:
        print("FINITE_WITNESSES=" + ",".join(map(str, zeros)))
    else:
        print("FINITE_WITNESSES=NONE")
    print("FINITE_DIAGNOSTIC_IS_NOT_AN_ALL_PRIME_PROOF=TRUE")


if __name__ == "__main__":
    main()
