"""Exact relative repair spectrum for P017 factor -> cofactor-root precision.

L064 bounds every least-prime block by at most two realized cofactor-root values.
Therefore the whole relative P011/P023 repair spectrum is quadratic: the only
nontrivial higher coordinate counts factor shells that actually split across
both adjacent root basins.
"""

from __future__ import annotations

from collections import defaultdict
from math import isqrt

from .legendre import primes_up_to
from .p017_cofactor_window import centered_cofactor_window, is_p_rough
from .p017_directional_root_factor_precision import root_factor_tagged_states


def factor_root_split_shell_primes(k: int) -> tuple[int, ...]:
    """Least primes whose actual p-rough cofactor shell realizes two root values."""

    states = root_factor_tagged_states(k)
    roots_by_prime: dict[int, set[int]] = defaultdict(set)
    for prime, q in states:
        roots_by_prime[prime].add(isqrt(q))
    if any(len(roots) > 2 for roots in roots_by_prime.values()):
        raise AssertionError("L064 two-root bound failed")
    return tuple(sorted(prime for prime, roots in roots_by_prime.items() if len(roots) == 2))


def split_shell_threshold_criterion(k: int, prime: int) -> bool:
    """Exact p-rough occupancy criterion for one factor shell to split.

    Let j=floor_sqrt(floor(k^2/p)).  The two possible root branches are separated
    by q=(j+1)^2.  The actual shell splits exactly when p-rough quotients occur
    on both sides of this boundary inside the open cofactor window.
    """

    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if prime not in primes_up_to(k):
        raise ValueError("prime must be a prime <=k")

    window = centered_cofactor_window(k, prime)
    lo = int(window["q_min"])
    hi = int(window["q_max"])
    base_root = isqrt((k * k) // prime)
    boundary = (base_root + 1) * (base_root + 1)

    lower_hi = min(hi, boundary - 1)
    upper_lo = max(lo, boundary)
    lower_realized = lower_hi >= lo and any(
        is_p_rough(q, prime) for q in range(lo, lower_hi + 1)
    )
    upper_realized = upper_lo <= hi and any(
        is_p_rough(q, prime) for q in range(upper_lo, hi + 1)
    )
    return lower_realized and upper_realized


def factor_root_relative_spectrum(k: int) -> dict[str, object]:
    """Return the exact L067 quadratic repair spectrum and code-support defect."""

    states = root_factor_tagged_states(k)
    roots_by_prime: dict[int, set[int]] = defaultdict(set)
    for prime, q in states:
        roots_by_prime[prime].add(isqrt(q))
    if any(len(roots) > 2 for roots in roots_by_prime.values()):
        raise AssertionError("factor block split beyond binary")

    factor_shell_count = len(roots_by_prime)
    split_primes = tuple(sorted(prime for prime, roots in roots_by_prime.items() if len(roots) == 2))
    split_shell_count = len(split_primes)
    joint_class_count = sum(len(roots) for roots in roots_by_prime.values())

    if joint_class_count != factor_shell_count + split_shell_count:
        raise AssertionError("binary split class-count identity failed")

    for prime in roots_by_prime:
        if split_shell_threshold_criterion(k, prime) != (prime in split_primes):
            raise AssertionError("threshold p-rough occupancy disagrees with direct root split")

    repair_factor = 2 if split_shell_count else 1
    product_capacity = factor_shell_count * repair_factor
    unused_product_codes = product_capacity - joint_class_count
    expected_unused = factor_shell_count - split_shell_count if split_shell_count else 0
    if unused_product_codes != expected_unused:
        raise AssertionError("unused binary code count disagrees with unsplit shell count")

    spectrum = (joint_class_count, split_shell_count)
    return {
        "factor_shell_count": factor_shell_count,
        "split_shell_primes": split_primes,
        "split_shell_count": split_shell_count,
        "joint_class_count": joint_class_count,
        "repair_factor": repair_factor,
        "relative_repair_spectrum": spectrum,
        "repair_polynomial_coefficients": (0, joint_class_count, split_shell_count),
        "product_capacity": product_capacity,
        "unused_product_codes": unused_product_codes,
    }
