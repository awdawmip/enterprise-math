"""Canonical P017 L054 cofactor-window separation.

For k>=4 and distinct first-factor primes p<r<=k, the exact raw cofactor
windows W_p(k)=[floor(k^2/p)+1, floor(k(k+2)/p)] are strictly ordered and
disjoint. Consequently least-factor stripping n -> n/spf(n) is injective on
square-basin composite states. The sharp finite overlap exception is k=3.
"""

from __future__ import annotations

from .factor_precision import first_factor_shell
from .legendre import is_prime, primes_up_to
from .p017_cofactor_window import centered_cofactor_window


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_shell_prime(k: int, prime: int) -> None:
    _require_positive("k", k)
    _require_positive("prime", prime)
    if prime > k or not is_prime(prime):
        raise ValueError("prime must be a prime <= k")


def raw_cofactor_interval(k: int, prime: int) -> tuple[int, int]:
    """Return [floor(k^2/p)+1, floor(k(k+2)/p)] for one first-prime shell."""
    _require_shell_prime(k, prime)
    lower = (k * k) // prime + 1
    upper = (k * (k + 2)) // prime
    centered = centered_cofactor_window(k, prime)
    if (lower, upper) != (centered["q_min"], centered["q_max"]):
        raise AssertionError("direct and centered cofactor windows disagree")
    return lower, upper


def cofactor_window_pair_separation(k: int, left_prime: int, right_prime: int) -> dict[str, int]:
    """Return L054 separation data for primes p<r<=k and k>=4."""
    _require_positive("k", k)
    if k < 4:
        raise ValueError("L054 separation requires k >= 4")
    _require_shell_prime(k, left_prime)
    _require_shell_prime(k, right_prime)
    if not left_prime < right_prime:
        raise ValueError("require left_prime < right_prime")

    p = left_prime
    r = right_prime
    spacing_margin = k * (r - p) - 2 * p
    if spacing_margin < 0:
        raise AssertionError("prime-spacing arithmetic margin became negative")

    left_min, left_max = raw_cofactor_interval(k, p)
    right_min, right_max = raw_cofactor_interval(k, r)
    gap = left_min - right_max - 1
    if gap < 0:
        raise AssertionError("L054 cofactor windows overlap")

    return {
        "k": k,
        "left_prime": p,
        "right_prime": r,
        "left_q_min": left_min,
        "left_q_max": left_max,
        "right_q_min": right_min,
        "right_q_max": right_max,
        "spacing_margin": spacing_margin,
        "integer_gap": gap,
    }


def all_cofactor_windows_separated(k: int) -> dict[str, object]:
    """Verify strict ordering of all first-prime cofactor windows at one k>=4."""
    _require_positive("k", k)
    if k < 4:
        raise ValueError("L054 separation requires k >= 4")
    primes = primes_up_to(k)
    windows = {p: raw_cofactor_interval(k, p) for p in primes}
    gaps: list[int] = []
    for p, r in zip(primes, primes[1:]):
        gaps.append(cofactor_window_pair_separation(k, p, r)["integer_gap"])
    return {
        "k": k,
        "primes": tuple(primes),
        "windows": windows,
        "minimum_integer_gap": min(gaps) if gaps else 0,
    }


def least_factor_strip_injection(k: int) -> dict[str, object]:
    """Validate n -> n/spf(n) injectivity on square-basin composites for k>=4."""
    _require_positive("k", k)
    if k < 4:
        raise ValueError("L054 injection requires k >= 4")
    all_cofactor_windows_separated(k)
    owner: dict[int, tuple[int, int]] = {}
    for p in primes_up_to(k):
        for n in first_factor_shell(k, p):
            q = n // p
            if q in owner:
                raise AssertionError("least-factor stripping was not injective across shells")
            owner[q] = (p, n)
    return {
        "k": k,
        "cofactor_owner": owner,
        "composite_state_count": len(owner),
    }
