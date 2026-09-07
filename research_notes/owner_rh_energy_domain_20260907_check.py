"""Exact finite evidence for the RH energy-domain correction; no RH test."""

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json


def mobius(n):
    residual, sign, prime = n, 1, 2
    while prime * prime <= residual:
        if residual % prime == 0:
            residual //= prime
            sign = -sign
            if residual % prime == 0:
                return 0
        prime += 1
    return -sign if residual > 1 else sign


def finite_kernel(m, n, sigma):
    """Only integer sigma<=1 is needed for this exact rational fixture."""
    assert isinstance(sigma, int) and sigma <= 1
    rate = F(1, m * m) + F(1, n * n)
    return F(factorial(1 - sigma), m * m * n * n) * rate ** (sigma - 2)


def main():
    historical = Path(__file__).with_name("RH_X6_BRC_TRANSPORT_FRONTIER_20260906.md")
    historical_sha = hashlib.sha256(historical.read_bytes()).hexdigest()
    assert historical_sha == "693a7b2888d3eb72faca74c7d166a8af78caa9107bbf532aea918e9085873412"

    # Sum_{n>=2} n^-2 <= 1/4 + integral_2^infinity t^-2 dt.
    constant_lower = 1 - (F(1, 4) + F(1, 2))
    # Sum_{n>=1} n^-4 <= 1 + integral_1^infinity t^-4 dt.
    lipschitz_upper = 1 + F(1, 3)
    radius = F(1, 16)
    p2_lower = constant_lower - lipschitz_upper * radius
    assert (constant_lower, lipschitz_upper, p2_lower) == (F(1, 4), F(4, 3), F(1, 6))

    # Independent finite Mobius series interval, with a rigorous <=1/N tail.
    limit = 32
    partial = sum((F(mobius(n), n * n) for n in range(1, limit + 1)), F(0))
    assert partial - F(1, limit) > constant_lower

    divergences = []
    for j in (1, 2, 4, 8, 16):
        epsilon = radius / 4**j
        # At sigma=5/2: integral_epsilon^radius x^-3/2 dx
        # =2*(epsilon^-1/2-radius^-1/2); the chosen roots are integers.
        lower = p2_lower**2 * 2 * (4 * 2**j - 4)
        assert lower == F(2, 9) * (2**j - 1)
        divergences.append({"j": j, "epsilon": str(epsilon), "energy_lower_bound": str(lower)})

    rewrites = 0
    critical_rewrites = 0
    for m in range(1, 9):
        for n in range(1, 9):
            sech_log_ratio = F(2 * m * n, m * m + n * n)
            for sigma in (-1, 0, 1):
                historical_formula = (F(2) ** (sigma - 2) * factorial(1 - sigma)
                                      * F(m * n) ** (-sigma)
                                      * sech_log_ratio ** (2 - sigma))
                assert finite_kernel(m, n, sigma) == historical_formula
                rewrites += 1
            # Squared coefficient after dividing by pi, at sigma=1/2.
            direct = F(m * m * n * n, 4 * (m * m + n * n)**3)
            historical_formula_squared = F(1, 32 * m * n) * sech_log_ratio**3
            assert direct == historical_formula_squared
            critical_rewrites += 1

    finite_grams = []
    for size in (1, 2, 4, 8, 16):
        value = sum((F(mobius(m) * mobius(n)) * finite_kernel(m, n, 1)
                     for m in range(1, size + 1) for n in range(1, size + 1)), F(0))
        assert value > 0
        finite_grams.append({"N": size, "sigma": "1", "finite_gram": str(value)})

    return {
        "status": "PASS",
        "historical_note_sha256": historical_sha,
        "arithmetic": "fractions.Fraction; no floating approximation",
        "p2_zero_lower": str(constant_lower),
        "p2_lipschitz_upper": str(lipschitz_upper),
        "p2_uniform_lower_on_0_to_1_over_16": str(p2_lower),
        "p2_zero_independent_series_interval": [str(partial - F(1, limit)), str(partial + F(1, limit))],
        "sigma_5_over_2_divergence_witnesses": divergences,
        "integer_kernel_rewrites": rewrites,
        "critical_coefficient_squared_rewrites": critical_rewrites,
        "finite_signed_grams": finite_grams,
        "scope": "finite evidence only; universal domain and convergence proofs are in the audit note; no RH conclusion",
        "global_knowledge": "main@4fa7d7d",
    }


if __name__ == "__main__":
    print(json.dumps(main(), separators=(",", ":")))
