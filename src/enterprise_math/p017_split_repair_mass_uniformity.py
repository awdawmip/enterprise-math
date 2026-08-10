"""Uniform dyadic audit for P017 split-shell repair mass.

For a square basin indexed by k and a least-prime shell p, strip p and retain
the square-root index of the cofactor. The shell can meet at most two adjacent
cofactor-root bins. This module audits exactly when both bins contain a
p-rough cofactor.

The accompanying theorem document proves a uniform dyadic lower bound for the
number of actually split shells by combining this exact boundary arithmetic
with classical Jacobsthal and continued-fraction discrepancy bounds. The
asymptotic theorem is proved in prose; bounded computation here is regression
only.
"""

from __future__ import annotations

from math import isqrt

from .legendre import is_prime, primes_up_to
from .p017_cofactor_window import is_p_rough


def _require_shell_prime(k: int, prime: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be a positive prime")
    if prime > k or not is_prime(prime):
        raise ValueError("prime must be a prime <= k")


def beatty_core_index(multiplier: int, prime: int) -> int:
    """Return floor(multiplier*sqrt(prime)) by exact integer arithmetic."""
    if isinstance(multiplier, bool) or not isinstance(multiplier, int) or multiplier < 1:
        raise ValueError("multiplier must be positive")
    if isinstance(prime, bool) or not isinstance(prime, int) or not is_prime(prime):
        raise ValueError("prime must be prime")
    return isqrt(prime * multiplier * multiplier)


def split_branch_data(k: int, prime: int) -> dict[str, object]:
    """Exact raw and p-rough branch data for one least-prime shell.

    Put
        m = R_2(floor(k^2/p)) + 1,
        tau = p*m^2-k^2.
    The open cofactor window is cut at the square boundary m^2.

    The numbers of raw quotient slots below and above that boundary are
        L = ceil(tau/p)-1,
        U = floor((2k-tau)/p)+1.

    A raw two-root split occurs iff p < tau <= 2k. An actual shell split
    additionally requires at least one p-rough quotient on each side.
    """
    _require_shell_prime(k, prime)

    lower_square = k * k
    quotient_floor = lower_square // prime
    multiplier = isqrt(quotient_floor) + 1
    boundary = multiplier * multiplier
    tau = prime * boundary - lower_square

    q_lo = quotient_floor + 1
    q_hi = (k * (k + 2)) // prime

    lower_lo = q_lo
    lower_hi = min(q_hi, boundary - 1)
    upper_lo = max(q_lo, boundary)
    upper_hi = q_hi

    lower_slots = max(0, lower_hi - lower_lo + 1)
    upper_slots = max(0, upper_hi - upper_lo + 1)

    formula_lower = (tau + prime - 1) // prime - 1
    formula_upper = (2 * k - tau) // prime + 1
    if lower_slots != max(0, formula_lower):
        raise AssertionError("lower branch-slot formula failed")
    if upper_slots != max(0, formula_upper):
        raise AssertionError("upper branch-slot formula failed")

    raw_split = prime < tau <= 2 * k
    if raw_split != (lower_slots > 0 and upper_slots > 0):
        raise AssertionError("raw split criterion disagreed with branch slots")

    upper_nonempty = upper_slots > 0
    beatty = beatty_core_index(multiplier, prime)
    if upper_nonempty != (beatty == k):
        raise AssertionError("upper branch is not the Beatty-core criterion")

    lower_rough = (
        sum(is_p_rough(q, prime) for q in range(lower_lo, lower_hi + 1))
        if lower_slots
        else 0
    )
    upper_rough = (
        sum(is_p_rough(q, prime) for q in range(upper_lo, upper_hi + 1))
        if upper_slots
        else 0
    )
    actual_split = lower_rough > 0 and upper_rough > 0

    return {
        "k": k,
        "prime": prime,
        "multiplier": multiplier,
        "tau": tau,
        "q_lo": q_lo,
        "q_hi": q_hi,
        "lower_interval": (lower_lo, lower_hi),
        "upper_interval": (upper_lo, upper_hi),
        "lower_slots": lower_slots,
        "upper_slots": upper_slots,
        "raw_split": raw_split,
        "lower_rough_count": lower_rough,
        "upper_rough_count": upper_rough,
        "actual_split": actual_split,
    }


def fixed_prime_dyadic_counts(K: int, prime: int) -> dict[str, object]:
    """Count Beatty-core, raw-split, and actual-split indices in (K,2K]."""
    if isinstance(K, bool) or not isinstance(K, int) or K < 2:
        raise ValueError("K must be an integer >=2")
    if isinstance(prime, bool) or not isinstance(prime, int) or not is_prime(prime):
        raise ValueError("prime must be prime")
    if prime > K:
        raise ValueError("this audit requires prime <= K")

    multiplier = 1
    while beatty_core_index(multiplier, prime) <= K:
        multiplier += 1

    candidates: list[int] = []
    raw: list[int] = []
    actual: list[int] = []
    while True:
        k = beatty_core_index(multiplier, prime)
        if k > 2 * K:
            break
        if k >= prime:
            candidates.append(k)
            data = split_branch_data(k, prime)
            if data["raw_split"]:
                raw.append(k)
            if data["actual_split"]:
                actual.append(k)
        multiplier += 1

    if len(set(candidates)) != len(candidates):
        raise AssertionError("Beatty-core indices unexpectedly repeated")
    if not set(actual).issubset(raw):
        raise AssertionError("actual split escaped raw split envelope")

    return {
        "K": K,
        "prime": prime,
        "beatty_candidates": tuple(candidates),
        "raw_splits": tuple(raw),
        "actual_splits": tuple(actual),
        "beatty_count": len(candidates),
        "raw_split_count": len(raw),
        "actual_split_count": len(actual),
        "realizability_failures": len(raw) - len(actual),
    }


def dyadic_actual_split_mass(K: int, prime_cutoff: int) -> dict[str, object]:
    """Sum actual fixed-prime split counts over primes <= prime_cutoff."""
    if prime_cutoff > K:
        raise ValueError("prime_cutoff must not exceed K")
    rows = {
        prime: fixed_prime_dyadic_counts(K, prime)
        for prime in primes_up_to(prime_cutoff)
    }
    total = sum(int(row["actual_split_count"]) for row in rows.values())
    return {
        "K": K,
        "prime_cutoff": prime_cutoff,
        "by_prime": rows,
        "total_actual_split_mass": total,
    }
