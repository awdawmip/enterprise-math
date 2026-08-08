"""Exact rough-window recursion for the P017 square-basin pressure test.

Buchstab/least-prime-factor recursion and rough-number counting are established
sieve theory.  This module only specializes that machinery to the exact moving
cofactor windows already forced by the consecutive-square geometry.

The project-specific pressure test is whether those windows contract strongly
enough to produce new finite survivor bounds.  In particular, the band p^2 >=
2k has an exact one-candidate-per-second-factor property and Omega(n) <= 3.
"""

from __future__ import annotations

from math import isqrt

from .factor_precision import smallest_prime_factor
from .legendre import is_prime, primes_up_to
from .p017_cofactor_window import (
    centered_cofactor_window,
    cofactor_window_shell,
    is_p_rough,
    omega_with_multiplicity,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_interval(lower: int, upper: int) -> None:
    _require_positive("lower", lower)
    _require_positive("upper", upper)
    if lower > upper:
        raise ValueError("lower must not exceed upper")


def ceil_div(numerator: int, denominator: int) -> int:
    """Positive-integer ceiling division."""
    _require_positive("numerator", numerator)
    _require_positive("denominator", denominator)
    return (numerator + denominator - 1) // denominator


def rough_interval_values(lower: int, upper: int, threshold: int) -> list[int]:
    """Return integers in [lower,upper] with no prime divisor < threshold."""
    _require_interval(lower, upper)
    _require_positive("threshold", threshold)
    return [value for value in range(lower, upper + 1) if is_p_rough(value, threshold)]


def raw_child_window(lower: int, upper: int, prime: int) -> dict[str, int]:
    """Return exact child interval after extracting one prime factor.

    The un-clipped multiple count is the number of multiples of ``prime`` in the
    parent interval.  It is an exact quotient response and therefore decomposes
    into full blocks plus one residual boundary carry.  The actual least-factor
    child additionally requires the cofactor to be at least ``prime``.
    """
    _require_interval(lower, upper)
    _require_positive("prime", prime)

    length = upper - lower + 1
    quotient_multiple_count = upper // prime - (lower - 1) // prime
    base = lower - 1
    bulk = length // prime
    carry = ((base % prime) + (length % prime)) // prime
    if quotient_multiple_count != bulk + carry:
        raise AssertionError("child-window quotient-response identity failed")
    if carry not in (0, 1):
        raise AssertionError("child-window residual carry must be binary")

    child_min_unclipped = ceil_div(lower, prime)
    child_min = max(prime, child_min_unclipped)
    child_max = upper // prime
    child_count = max(0, child_max - child_min + 1)

    ceiling_bound = ceil_div(length, prime)
    if quotient_multiple_count > ceiling_bound:
        raise AssertionError("multiple count exceeded ceiling interval bound")
    if child_count > quotient_multiple_count:
        raise AssertionError("least-factor clipping increased child count")

    return {
        "lower": lower,
        "upper": upper,
        "prime": prime,
        "parent_length": length,
        "child_min": child_min,
        "child_max": child_max,
        "child_count": child_count,
        "multiple_count": quotient_multiple_count,
        "transport_bulk": bulk,
        "transport_carry": carry,
        "ceiling_bound": ceiling_bound,
    }


def rough_interval_least_factor_partition(
    lower: int, upper: int, threshold: int
) -> dict[str, object]:
    """Partition a rough interval into primes and composite least-factor branches.

    This is the finite-interval least-prime-factor/Buchstab decomposition.  Each
    composite rough integer q has a unique least prime factor ell>=threshold and
    q=ell*s with s>=ell and s ell-rough.
    """
    values = rough_interval_values(lower, upper, threshold)
    prime_values: list[int] = []
    branches: dict[int, list[int]] = {}
    reconstructed: list[int] = []

    for value in values:
        if is_prime(value):
            prime_values.append(value)
            reconstructed.append(value)
            continue
        ell = smallest_prime_factor(value)
        if ell < threshold:
            raise AssertionError("rough value acquired too-small least prime factor")
        child = value // ell
        if child < ell:
            raise AssertionError("least prime factor exceeded complementary factor")
        if not is_p_rough(child, ell):
            raise AssertionError("least-factor child is not ell-rough")
        branches.setdefault(ell, []).append(child)
        reconstructed.append(ell * child)

    if sorted(reconstructed) != values:
        raise AssertionError("least-factor recursion failed to reconstruct rough interval")

    # Verify every branch lies in its exact divided child interval.
    for ell, children in branches.items():
        child_data = raw_child_window(lower, upper, ell)
        for child in children:
            if not (child_data["child_min"] <= child <= child_data["child_max"]):
                raise AssertionError("Buchstab child left the exact divided window")

    return {
        "values": values,
        "primes": prime_values,
        "branches": branches,
        "count": len(values),
    }


def p017_shell_rough_partition(k: int, prime: int) -> dict[str, object]:
    """Apply exact least-factor recursion to the P017 cofactor window W_p(k)."""
    data = centered_cofactor_window(k, prime)
    partition = rough_interval_least_factor_partition(
        data["q_min"], data["q_max"], prime
    )
    shell = cofactor_window_shell(k, prime)
    if [prime * q for q in partition["values"]] != shell:
        raise AssertionError("rough recursion does not match canonical P017 shell")
    return {**data, **partition}


def high_least_factor_band(k: int, prime: int) -> dict[str, object]:
    """Classify the P017 band p^2 >= 2k.

    In this band the parent cofactor window has raw length at most p.  Hence each
    possible second least-prime-factor branch contains at most one raw child.
    Also p^4 > (k+1)^2-1, so every shell state has Omega <= 3.
    """
    _require_positive("k", k)
    _require_positive("prime", prime)
    if prime not in primes_up_to(k):
        raise ValueError("prime must be a prime <= k")
    if prime * prime < 2 * k:
        raise ValueError("high least-factor band requires p^2 >= 2k")

    data = centered_cofactor_window(k, prime)
    parent_length = data["raw_count"]
    radius = data["radius"]
    increment = 2 * radius - 2

    # N_raw = 2 + quotient-response increment.  The universal interval bound
    # Delta Q <= ceil(h/p), combined with p^2>=2k, forces N_raw<=p.
    ceiling_increment = 0 if increment == 0 else ceil_div(increment, prime)
    if parent_length > 2 + ceiling_increment:
        raise AssertionError("P017 window exceeded quotient-response ceiling bound")
    if 2 * k <= prime * prime:
        # increment = 2k-2p <= p(p-2)
        if increment > prime * (prime - 2):
            raise AssertionError("high-band arithmetic reduction failed")
        if parent_length > prime:
            raise AssertionError("high-band parent window is longer than p")

    q_min = data["q_min"]
    q_max = data["q_max"]
    possible_second_primes = list(primes_up_to(isqrt(q_max)))
    branch_raw_counts: dict[int, int] = {}
    for ell in possible_second_primes:
        if ell < prime:
            continue
        child = raw_child_window(q_min, q_max, ell)
        branch_raw_counts[ell] = child["child_count"]
        if child["child_count"] > 1:
            raise AssertionError("high-band second-factor branch has multiple raw candidates")

    shell = cofactor_window_shell(k, prime)
    semiprime_states: list[int] = []
    triple_prime_states: list[int] = []
    triple_by_second_prime: dict[int, int] = {}
    upper = (k + 1) * (k + 1) - 1
    if prime**4 <= upper:
        raise AssertionError("high-band fourth-power root-depth bound failed")

    for n in shell:
        omega = omega_with_multiplicity(n)
        if omega > 3:
            raise AssertionError("high-band shell exceeded Omega<=3")
        q = n // prime
        if is_prime(q):
            semiprime_states.append(n)
            continue
        ell = smallest_prime_factor(q)
        tail = q // ell
        if ell < prime or tail < ell or not is_prime(tail):
            raise AssertionError("high-band composite cofactor is not ell*prime")
        if ell in triple_by_second_prime:
            raise AssertionError("second-prime branch contains multiple shell states")
        triple_by_second_prime[ell] = n
        triple_prime_states.append(n)

    if sorted(semiprime_states + triple_prime_states) != shell:
        raise AssertionError("high-band semiprime/triple-prime classification incomplete")

    return {
        **data,
        "parent_length": parent_length,
        "branch_raw_counts": branch_raw_counts,
        "semiprime_states": semiprime_states,
        "triple_prime_states": triple_prime_states,
        "triple_by_second_prime": triple_by_second_prime,
        "shell": shell,
    }


def semiprime_only_band(k: int, prime: int) -> dict[str, object]:
    """Recover the stronger root-depth band p^3 > (k+1)^2-1."""
    _require_positive("k", k)
    _require_positive("prime", prime)
    if prime not in primes_up_to(k):
        raise ValueError("prime must be a prime <= k")
    upper = (k + 1) * (k + 1) - 1
    if prime**3 <= upper:
        raise ValueError("semiprime-only band requires p^3 > square-basin upper endpoint")
    shell = cofactor_window_shell(k, prime)
    for n in shell:
        if omega_with_multiplicity(n) != 2:
            raise AssertionError("semiprime-only band contains non-semiprime state")
    return {"upper": upper, "shell": shell}
