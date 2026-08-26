"""Hybrid large-prime-factor / roughness ladder for square intervals.

Let n be an integer near scale X with one prime factor P>X^beta.  Suppose n is
X^alpha-rough: every prime divisor of n is >X^alpha.  Writing n=P*m gives

    m < X^(1-beta) * (harmless square-window endpoint factor).

If the cofactor contained r prime factors counted with multiplicity, then

    m > X^(r*alpha).

Thus whenever

    r*alpha > 1-beta,

the cofactor has at most r-1 prime factors and n has at most r prime factors in
total.  At a rigid finite square endpoint U=k^2+2k, the exact condition is

    (y+1)^r > U / P,

where y is the integral roughness cutoff and P is the known large prime factor.

For the current exact-square-root largest-prime-factor exponent beta=0.744
(Runbo Li, manuscript `On the largest prime factor of integers in short
intervals IV`, current August-2026 author-page version), the asymptotic roughness
thresholds are

    P3: alpha > (1-0.744)/3 = 0.085333...,
    P2: alpha > (1-0.744)/2 = 0.128,
    P1: alpha > 1-0.744       = 0.256.

Two near-threshold alignments are therefore visible:

* Campbell's explicit all-square P3 proof pre-sieves at X^(1/8)=X^0.125,
  only 0.003 below the hybrid P2 threshold 0.128;
* the project fourth-root support layer uses X^(1/4)=X^0.25, only 0.006 below
  the hybrid prime threshold 0.256.

These are *joint-witness* thresholds.  Separate theorems asserting one rough
state and another state with a large prime factor cannot be combined.  The
missing statement is simultaneous roughness + large-factor occurrence in one
square-shell state.
"""

from __future__ import annotations


def cofactor_factor_capacity(upper: int, large_prime: int, rough_cutoff: int) -> dict[str, int]:
    """Return the exact maximum possible cofactor Omega from product size alone.

    The state is assumed to satisfy n<=upper, large_prime|n, and every cofactor
    prime factor is >rough_cutoff.  The returned capacity t is the largest t
    for which (rough_cutoff+1)^t <= floor(upper/large_prime).
    Total Omega is at most t+1.
    """
    if any(isinstance(v, bool) or not isinstance(v, int) for v in (upper, large_prime, rough_cutoff)):
        raise ValueError("arguments must be integers")
    if upper < 2 or large_prime < 2 or rough_cutoff < 0 or large_prime > upper:
        raise ValueError("invalid positive scale data")
    cofactor_max = upper // large_prime
    base = rough_cutoff + 1
    t = 0
    power = 1
    while power * base <= cofactor_max:
        power *= base
        t += 1
    return {
        "upper": upper,
        "large_prime": large_prime,
        "rough_cutoff": rough_cutoff,
        "cofactor_max": cofactor_max,
        "cofactor_omega_capacity": t,
        "total_omega_capacity": t + 1,
    }


def square_large_factor_roughness_certificate(
    k: int,
    large_prime: int,
    rough_cutoff: int,
    target_omega: int,
) -> dict[str, int | bool]:
    """Certify a finite P_target consequence for one joint witness."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(target_omega, bool) or not isinstance(target_omega, int) or target_omega < 1:
        raise ValueError("target_omega must be positive")
    upper = k * k + 2 * k
    data = cofactor_factor_capacity(upper, large_prime, rough_cutoff)
    certified = int(data["total_omega_capacity"]) <= target_omega
    return {
        **data,
        "k": k,
        "target_omega": target_omega,
        "target_almost_prime_certified": certified,
        "finite_product_condition": (rough_cutoff + 1) ** target_omega > data["cofactor_max"],
    }
