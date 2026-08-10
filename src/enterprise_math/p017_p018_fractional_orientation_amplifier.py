"""Fractional orientation amplifier and its exact sieve-dimension boundary.

For a surviving P017 mirror radius let L,U be the disjoint lower/upper
transverse small-prime supports.  For a rational parameter 0<=lambda<=1 define

    F_lambda,+ = (1+lambda)^|L| 1_{U empty}.

Equivalently, by L043 disjointness,

    F_lambda,+(r)
      = product_p [1 + lambda 1_{p|M-r} - 1_{p|M+r}].

Every lambda therefore preserves the same zero set: F_lambda,+ is positive iff
the upper mirror state is prime.  The endpoint lambda=0 is the ordinary upper
prime indicator; lambda=1 is the hard orientation-Walsh amplifier.

There are two different density notions and they must not be confused.

1. Direct signed-root expansion.  On one complete p-period the local factor has
   mean

       1 - (1-lambda)/p.

   A selected j-prime orientation column has continuous-floor coefficient

       (lambda-1)^j.

   Thus lambda=1 is uniquely the all-orders zero-floor endpoint.

2. Positive-sequence + upper-side sieve decomposition.  Put

       a_lambda(r)=(1+lambda)^|L(r)|

   before sieving the upper roots.  Its formal unsifted mass contains the local
   factor 1+lambda/p.  Conditional on this positive amplifier, the upper-root
   divisibility density is

       g_lambda(p)=1/(p+lambda).

   Consequently

       g_lambda(p)=1/p+O(1/p^2),

   so the classical beta/linear-sieve dimension is **one for every fixed
   lambda**, not 1-lambda.  The identity

       X_lambda product_p(1-g_lambda(p))
         = base * product_p(1-(1-lambda)/p)

   reflects growth of the unsifted amplifier X_lambda, not a reduction of the
   target-side sieve dimension.

The lower-support divisor expansion is

    (1+lambda)^|L| = sum_{d|rad(L)} lambda^omega(d).

Hence lambda genuinely interpolates between no opposite-side divisor amplifier
and full Walsh divisor weight, and may trade analytic divisor complexity against
continuous bulk.  What it does *not* do is turn the target prime sieve into a
half-dimensional beta sieve.

This module records that distinction as a reusable negative boundary.  It does
not establish a remainder theorem or a prime gap result.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

from .legendre import primes_up_to
from .p017_mirror import anchor_surviving_radius, mirror_transverse_supports
from .p017_p018_effective_anchor import effective_odd_anchor_primes


def _require_lambda(value: Fraction) -> Fraction:
    lam = Fraction(value)
    if not (Fraction(0, 1) <= lam <= Fraction(1, 1)):
        raise ValueError("lambda must lie in [0,1]")
    return lam


def fractional_local_factor(prime: int, lam: Fraction) -> dict[str, Fraction]:
    """Return exact direct-factor and positive-sieve local statistics."""
    lam = _require_lambda(lam)
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 3:
        raise ValueError("prime must be an odd integer >=3")
    p = prime
    direct_mean = Fraction(p - 1, p) + lam / p
    positive_amplifier_mean = Fraction(1, 1) + lam / p
    upper_divisibility_density = Fraction(1, 1) / (p + lam)
    if direct_mean != positive_amplifier_mean * (1 - upper_divisibility_density):
        raise AssertionError("fractional local factorization failed")
    return {
        "lambda": lam,
        "direct_lower_hit_value": 1 + lam,
        "direct_upper_hit_value": Fraction(0, 1),
        "direct_neutral_value": Fraction(1, 1),
        "direct_complete_period_mean": direct_mean,
        "positive_amplifier_local_mean": positive_amplifier_mean,
        "upper_divisibility_density_g": upper_divisibility_density,
        "p_times_g": p * upper_divisibility_density,
        "classical_sieve_dimension_first_order": Fraction(1, 1),
    }


def fractional_orientation_floor_coefficient(selected_degree: int, lam: Fraction) -> Fraction:
    """Return (lambda-1)^j for one selected j-prime orientation cube."""
    lam = _require_lambda(lam)
    if (
        isinstance(selected_degree, bool)
        or not isinstance(selected_degree, int)
        or selected_degree < 1
    ):
        raise ValueError("selected_degree must be a positive integer")
    j = selected_degree
    direct = sum(
        Fraction(comb(j, lower_degree), 1)
        * (lam ** lower_degree)
        * ((-1) ** (j - lower_degree))
        for lower_degree in range(j + 1)
    )
    expected = (lam - 1) ** j
    if direct != expected:
        raise AssertionError("fractional orientation cube did not telescope")
    return expected


def _transverse_primes(k: int) -> tuple[int, ...]:
    M = k * (k + 1)
    return tuple(p for p in primes_up_to(k) if p % 2 == 1 and M % p != 0)


def formal_fractional_sieve_model(k: int, lam: Fraction) -> dict[str, object]:
    """Return exact rational local products separating mass growth from sieve dimension."""
    lam = _require_lambda(lam)
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    K = k - 1
    trans = _transverse_primes(k)
    anchors = effective_odd_anchor_primes(k)
    base = Fraction(K, 2)
    for prime in anchors:
        base *= Fraction(prime - 1, prime)

    amplifier = Fraction(1, 1)
    sieve_product = Fraction(1, 1)
    direct_product = Fraction(1, 1)
    for prime in trans:
        local = fractional_local_factor(prime, lam)
        amplifier *= local["positive_amplifier_local_mean"]
        sieve_product *= 1 - local["upper_divisibility_density_g"]
        direct_product *= local["direct_complete_period_mean"]
    X = base * amplifier
    sifted = X * sieve_product
    direct = base * direct_product
    if sifted != direct:
        raise AssertionError("fractional formal main did not factor consistently")

    alternate = base
    for prime in trans:
        alternate *= 1 - (1 - lam) / prime
    if direct != alternate:
        raise AssertionError("fractional net logarithmic-decay product failed")

    return {
        "k": k,
        "lambda": lam,
        "effective_odd_anchors": anchors,
        "transverse_primes": trans,
        "base_radius_mass": base,
        "formal_unsifted_amplified_mass_X": X,
        "target_side_sieve_product": sieve_product,
        "formal_sifted_main": sifted,
        "direct_signed_root_mean_product": direct,
        "net_decay_euler_product": alternate,
        "classical_target_sieve_dimension": 1,
        "net_log_decay_exponent_from_mass_times_sieve": 1 - lam,
        "dimension_warning": (
            "1-lambda is the net Euler-product decay exponent, not the classical sieve dimension"
        ),
    }


def fractional_point_weight(k: int, radius: int, lam: Fraction) -> dict[str, object]:
    """Return the exact one-sided fractional prime detector on one surviving radius."""
    lam = _require_lambda(lam)
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")
    lower_support, upper_support = mirror_transverse_supports(k, radius)
    c_lower = len(lower_support)
    upper_prime = len(upper_support) == 0
    weight = (1 + lam) ** c_lower if upper_prime else Fraction(0, 1)

    divisor_expansion = sum(
        Fraction(comb(c_lower, size), 1) * (lam ** size)
        for size in range(c_lower + 1)
    )
    if divisor_expansion != (1 + lam) ** c_lower:
        raise AssertionError("fractional opposite-divisor binomial expansion failed")
    if upper_prime and divisor_expansion != weight:
        raise AssertionError("fractional opposite-divisor expansion failed")
    if (weight > 0) != upper_prime:
        raise AssertionError("fractional weight lost exact upper-prime positivity")
    return {
        "k": k,
        "radius": radius,
        "lambda": lam,
        "lower_support": tuple(lower_support),
        "upper_support": tuple(upper_support),
        "upper_prime": upper_prime,
        "fractional_upper_prime_weight": weight,
        "opposite_divisor_expansion": divisor_expansion,
        "positive_iff_upper_prime": True,
    }
