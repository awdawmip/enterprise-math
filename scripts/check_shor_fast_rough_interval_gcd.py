#!/usr/bin/env python3
"""Exact finite regressions for RS-SHOR-FAST-ROUGH-INTERVAL-GCD.

This checker is intentionally small and dependency-free.  It verifies the exact
structural reductions used by the research return; it is not a claimed fast
implementation of FAST_ROUGH_INTERVAL_GCD.
"""

from fractions import Fraction
from math import factorial, gcd, isqrt


def primes_upto(n: int) -> list[int]:
    mark = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        mark[0] = 0
    if n >= 1:
        mark[1] = 0
    for p in range(2, isqrt(n) + 1):
        if mark[p]:
            mark[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [p for p in range(2, n + 1) if mark[p]]


def mobius_upto(n: int) -> list[int]:
    mu = [0] * (n + 1)
    lp = [0] * (n + 1)
    ps: list[int] = []
    mu[1] = 1
    for a in range(2, n + 1):
        if lp[a] == 0:
            lp[a] = a
            ps.append(a)
            mu[a] = -1
        for p in ps:
            if p > lp[a] or a * p > n:
                break
            lp[a * p] = p
            mu[a * p] = 0 if p == lp[a] else -mu[a]
    return mu


def generated_legal_cases(B: int) -> list[tuple[int, tuple[int, ...]]]:
    """Generate all prime/square/distinct-semiprime cases from p>B^2, d<=B^6.

    For a semiprime p*q with p>B^2 and p*q<=B^6, q<B^4, so sieving only
    through B^4 suffices to enumerate every composite legal case.
    """
    ps = [p for p in primes_upto(B**4) if p > B * B]
    out: list[tuple[int, tuple[int, ...]]] = []
    for p in ps:
        if p <= B**6:
            out.append((p, (p,)))
        if p * p <= B**6:
            out.append((p * p, (p, p)))
    for i, p in enumerate(ps):
        for q in ps[i + 1 :]:
            d = p * q
            if d > B**6:
                break
            out.append((d, (p, q)))
    return out


def prefix_distinct_factor_product(factors: tuple[int, ...], z: int) -> int:
    ans = 1
    for p in set(factors):
        if p <= z:
            ans *= p
    return ans


def direct_interval_target(factors: tuple[int, ...], x: int, y: int) -> int:
    ans = 1
    for p in set(factors):
        if x < p <= y:
            ans *= p
    return ans


def truncated_mobius_factorial(B: int, z: int) -> Fraction:
    mu = mobius_upto(B)
    value = Fraction(1, 1)
    for k in range(1, B + 1):
        f = factorial(z // k)
        if mu[k] == 1:
            value *= f
        elif mu[k] == -1:
            value /= f
    return value


def main() -> None:
    total_cases = 0

    # Structural exhaustive generation for small B.
    for B in range(2, 9):
        lo, hi = B * B, B**3
        cases = generated_legal_cases(B)
        total_cases += len(cases)
        endpoints = sorted(
            {
                lo,
                lo + 1,
                (2 * lo + hi) // 3,
                (lo + 2 * hi) // 3,
                hi - 1,
                hi,
            }
        )

        for d, factors in cases:
            # Exact roughness-rank theorem: Omega(d)<=2.
            assert len(factors) <= 2

            # For squarefree d, gcd(d,z!) is exactly the distinct prefix factor product.
            squarefree = len(factors) == 1 or (
                len(factors) == 2 and factors[0] != factors[1]
            )
            if squarefree:
                for z in endpoints:
                    assert gcd(d, factorial(z)) == prefix_distinct_factor_product(
                        factors, z
                    )

            # The square-aware canonical prefix quotient equals the open-left,
            # closed-right interval target for every generated legal case.
            for x in endpoints:
                for y in endpoints:
                    if x >= y:
                        continue
                    lhs = prefix_distinct_factor_product(
                        factors, y
                    ) // prefix_distinct_factor_product(factors, x)
                    rhs = direct_interval_target(factors, x, y)
                    assert lhs == rhs

    # Rational-sign/floor/denominator regressions for the original T_B projector.
    rational_checks = 0
    for B in range(2, 6):
        lo, hi = B * B, B**3
        cases = generated_legal_cases(B)
        stride = max(1, len(cases) // 30)
        sampled = cases[::stride]
        endpoints = sorted({lo, lo + 1, (lo + hi) // 2, hi - 1, hi})
        for d, factors in sampled:
            for x in endpoints:
                for y in endpoints:
                    if x >= y:
                        continue
                    ratio = truncated_mobius_factorial(B, y) / truncated_mobius_factorial(
                        B, x
                    )
                    # Denominator must be a unit on a B^2-rough modulus.
                    assert gcd(d, ratio.denominator) == 1
                    residue = (ratio.numerator % d) * pow(
                        ratio.denominator, -1, d
                    ) % d
                    assert gcd(d, residue) == direct_interval_target(factors, x, y)
                    rational_checks += 1

    # Guard: naive gcd(d,z!) overcounts multiplicity for square inputs, so the
    # perfect-square preprocessing in the theorem is genuinely necessary.
    assert gcd(11 * 11, factorial(22)) == 11 * 11
    assert prefix_distinct_factor_product((11, 11), 22) == 11

    print(
        "PASS",
        f"generated_legal_cases={total_cases}",
        f"rational_projector_checks={rational_checks}",
        "square_multiplicity_guard=B3_p11_z22",
    )


if __name__ == "__main__":
    main()
