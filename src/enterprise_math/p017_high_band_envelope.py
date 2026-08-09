"""Exact finite envelopes for the P017 high-band pressure test.

This module contains only the integer layer.  The asymptotic passage from the
finite reciprocal-prime envelopes to the constant log(2) uses classical prime
estimates and is documented separately; it is not implemented numerically here.
"""

from __future__ import annotations

from .core import integer_nth_root
from .legendre import interior_hit_count, primes_up_to
from .p017_cofactor_window import cofactor_window_shell
from .p017_high_band import high_band_global_hit_union_bound


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def ceil_integer_sqrt(n: int) -> int:
    """Return the least integer m with m^2 >= n."""
    _require_positive("n", n)
    root = integer_nth_root(n, 2)
    return root if root * root == n else root + 1


def high_band_resource_interval(k: int) -> tuple[int, int]:
    """Return the universal cofactor-prime resource interval for L049.

    If a high-band triple resource r occurs with least prime p, then

        p^2 >= 2k,
        p <= r,
        p^2 r <= U = k(k+2).

    Therefore r >= sqrt(2k) and r <= U/(2k)=(k+2)/2.
    """
    _require_positive("k", k)
    lower = ceil_integer_sqrt(2 * k)
    upper = (k + 2) // 2
    return lower, upper


def high_band_composite_envelope(k: int) -> dict[str, object]:
    """Bound all high-band composite states by raw least-factor hit counts.

    Let N_H(k) count all composite basin states whose least prime p satisfies
    p^2>=2k.  Least-factor shells are disjoint, and each exact shell is a subset
    of all basin multiples of p.  Hence

        N_H(k) <= A_H(k) := sum H_p(k)

    over primes sqrt(2k)<=p<=k.

    This finite inequality includes both semiprime and three-prime high-band
    states.  Classical Mertens estimates later imply A_H(k)/(2k) has limsup at
    most log(2); that analytic step is deliberately not encoded here.
    """
    _require_positive("k", k)
    lower = ceil_integer_sqrt(2 * k)
    least_primes = [prime for prime in primes_up_to(k) if prime >= lower]
    raw_hit_counts = {
        prime: interior_hit_count(k, prime, 2)
        for prime in least_primes
    }
    raw_hit_sum = sum(raw_hit_counts.values())

    exact_shell_counts = {
        prime: len(cofactor_window_shell(k, prime))
        for prime in least_primes
    }
    exact_composite_count = sum(exact_shell_counts.values())
    if exact_composite_count > raw_hit_sum:
        raise AssertionError("high-band composite shells exceeded the raw H_p envelope")

    return {
        "k": k,
        "least_prime_lower": lower,
        "least_primes": least_primes,
        "raw_hit_counts": raw_hit_counts,
        "raw_hit_sum": raw_hit_sum,
        "exact_shell_counts": exact_shell_counts,
        "exact_composite_count": exact_composite_count,
    }


def high_band_hit_count_envelope(k: int) -> dict[str, object]:
    """Return an exact finite envelope above the L049 triple support capacity.

    Let C_H(k)=sum_r c_r(k) be the exact L049 hit-union support capacity.  Every
    resource prime r lies in the universal interval returned above, and every
    state in X_r(k) is a basin multiple of r.  Hence

        C_H(k) <= B_H(k) := sum_r H_r(k)

    over primes in that interval.

    The exact square-cofactor correction E_H(k) is at most R_3(U), because every
    high-band square-cofactor shell has least prime p satisfying p^3<=U and each
    least-prime shell contributes at most one such square.  Therefore

        T_H(k) <= floor((B_H(k)+R_3(U))/2).

    This is deliberately a coarse finite envelope.  It exists to separate the
    project-specific exact combinatorics from the classical analytic estimates
    later used to obtain the stronger triple-only asymptotic log(2)/2 fraction.
    """
    _require_positive("k", k)
    lower, upper = high_band_resource_interval(k)
    resources = [prime for prime in primes_up_to(upper) if prime >= lower]
    hit_counts = {
        prime: interior_hit_count(k, prime, 2)
        for prime in resources
    }
    hit_count_sum = sum(hit_counts.values())

    exact = high_band_global_hit_union_bound(k)
    support_capacity = int(exact["support_capacity"])
    if support_capacity > hit_count_sum:
        raise AssertionError("L049 hit-union capacity exceeded the H_r envelope")

    U = k * (k + 2)
    cube_root_bound = integer_nth_root(U, 3)
    square_branch_count = int(exact["square_branch_count"])
    if square_branch_count > cube_root_bound:
        raise AssertionError("square-cofactor correction exceeded the cube-root bound")

    global_triple_bound = int(exact["global_triple_bound"])
    finite_triple_envelope = (hit_count_sum + cube_root_bound) // 2
    if global_triple_bound > finite_triple_envelope:
        raise AssertionError("finite analytic envelope fell below the exact L049 bound")

    return {
        "k": k,
        "resource_lower": lower,
        "resource_upper": upper,
        "resource_primes": resources,
        "hit_counts": hit_counts,
        "hit_count_sum": hit_count_sum,
        "exact_support_capacity": support_capacity,
        "square_branch_count": square_branch_count,
        "cube_root_bound": cube_root_bound,
        "exact_global_triple_bound": global_triple_bound,
        "finite_triple_envelope": finite_triple_envelope,
    }
