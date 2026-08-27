#!/usr/bin/env python3
"""Regression checker for ABC Enterprise boundary-escape obstruction.

The finite tests verify exact algebraic identities/families used by the written
proof. They do not replace the general proofs or certify external theorems.
"""
from __future__ import annotations
from math import ceil, gcd, log
from pathlib import Path

ARTIFACT = Path("research_artifacts/ABC_ENTERPRISE_BOUNDARY_ESCAPE/ABC_BOUNDARY_REGIME_ENVELOPE_20260827.md")
RETURN = Path("research_returns/ABC_ENTERPRISE_BOUNDARY_ESCAPE_RETURN_20260827.md")


def rad(n: int) -> int:
    r = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            r *= p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        r *= n
    return r


def test_consecutive_family() -> None:
    for n in range(1, 2001):
        a, b, c = 1, n, n + 1
        assert a + b == c
        assert gcd(a, b) == 1
        assert min(a, b) / c == 1 / (n + 1)
        assert rad(a * b * c) == rad(n * (n + 1))


def test_fixed_band_not_power_small() -> None:
    eta = 0.25
    for delta in (0.49, 0.20, 0.10, 0.03):
        M = max(3, ceil(1 / delta))
        t = max(10, int((M + 1) ** ((1 - eta) / eta)) + 10)
        a = t
        b = (M - 1) * t + 1
        c = M * t + 1
        assert a + b == c
        assert gcd(a, b) == 1
        assert a == min(a, b)
        assert a / c < 1 / M <= delta
        assert a > c ** (1 - eta)


def test_eta_star_identity() -> None:
    samples = [(1, 10), (3, 97), (123, 1009), (999, 10000)]
    for m, c in samples:
        assert 0 < m <= c / 2
        eta = log(c / m) / log(c)
        reconstructed = c ** (1 - eta)
        assert abs(reconstructed - m) <= 1e-10 * max(1.0, m)


def test_frozen_text() -> None:
    a = ARTIFACT.read_text(encoding="utf-8")
    r = RETURN.read_text(encoding="utf-8")
    required = [
        "EXACT_OBSTRUCTION",
        "m/c",
        "c^{-\\eta_0}",
        "rad}(n(n+1))",
        "arXiv:2312.03566v1",
        "durable normalization gap",
    ]
    for token in required:
        assert token in a, token
    assert "`EXACT_OBSTRUCTION`" in r
    assert "BETA_NORMALIZATION_NOT_DURABLY_FROZEN" in r


def main() -> None:
    test_consecutive_family()
    test_fixed_band_not_power_small()
    test_eta_star_identity()
    test_frozen_text()
    print("ABC_BOUNDARY_ESCAPE_CHECK_PASS consecutive_n<=2000 fixed_band_witnesses=4 eta_star=PASS")


if __name__ == "__main__":
    main()
