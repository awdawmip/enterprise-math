"""Logarithmic-degree precision ceiling for P017×P018 moment pressure.

The logarithmic moment minorants from p017_p018_moment_pressure.py can be made
uniformly close to the exact high-complete-core correction without retaining one
label per complete core.

Fix odd Bonferroni order m and write

    K = k-1,
    X = k(k+2)-1,
    a = log K,
    b = log X,
    c0 = log(k^2+1).

For full valuation and degree d>=2,

    P_d(y)=(y/b)^(d-1)(y-a)/(b-a).

Low complete cores satisfy 0<=y<=a.  High complete cores satisfy the much
stronger spectral-gap statement c0<=y<=b because P017 proves C(n)=n whenever
C(n)>K.

The negative low weight has exact maximum

    L_d = [a/(b-a)] [a/b]^(d-1) (d-1)^(d-1)/d^d

and therefore, since X>K^2,

    L_d < 2^(-(d-1))/d.

Writing delta=b-c0, Bernoulli's inequality gives

    1-G_d
      <= delta[(d-1)/b + 1/(b-a)]
      < (d+1)/(k log k),

where G_d=min_{c0<=y<=b} P_d(y).

Let J_L be the largest j for which the first j transverse odd primes have
product <=K, and J_H the corresponding depth below X.  Every low row has
support size <=J_L; every high row has support size <=J_H.  Since there are at
most k signed odd points in the centered interval,

    R <= k binom(J_L-1,m),
    H <= k binom(J_H-1,m).

Choose the integer logarithmic degree

    d_*(k)=min{d>=1: 2^d>=k} = bit_length(k-1).

Then the full-valuation degree-d_* pressure lower bound h obeys

    0 <= H-h
      < binom(J_H-1,m) (d_*+1)/log k
        + binom(J_L-1,m) 2/d_*.

Thus an O(k)-scale exact correction is compressed to a support-depth/polylog
error envelope by O(log k) moment degree.  A universal full-valuation cap is
also only logarithmic: if r>=floor(log_3 X), every odd prime exponent in a basin
state is already fully visible.

This is not a Legendre proof.  It isolates the remaining task: combine the
polylog moment-pressure information loss with the P018 quotient-channel /
finite-boundary collision machinery, rather than asking one scalar product to
carry the whole sieve.
"""

from __future__ import annotations

from math import comb, log

from .legendre import primes_up_to


def _choose(n: int, r: int) -> int:
    return comb(n, r) if 0 <= r <= n else 0


def transverse_primorial_depth_below(k: int, cutoff: int) -> dict[str, object]:
    """Return max j with product of first j transverse odd primes <= cutoff."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 1:
        raise ValueError("cutoff must be a positive integer")

    center = k * (k + 1)
    product_value = 1
    chosen: list[int] = []
    for prime in primes_up_to(k):
        if prime == 2 or center % prime == 0:
            continue
        if product_value > cutoff // prime:
            break
        product_value *= prime
        chosen.append(prime)
    return {
        "k": k,
        "cutoff": cutoff,
        "depth": len(chosen),
        "transverse_primes": tuple(chosen),
        "primorial_product": product_value,
    }


def universal_full_valuation_cap(k: int) -> int:
    """Return floor(log_3 X), an exponent cap sufficient for every odd prime."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    xmax = k * (k + 2) - 1
    power = 1
    exponent = 0
    while power <= xmax // 3:
        power *= 3
        exponent += 1
    return exponent


def logarithmic_degree(k: int) -> int:
    """Return the least d with 2^d>=k, using integer bit length."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    return (k - 1).bit_length()


def logarithmic_degree_precision_ceiling(k: int, order: int) -> dict[str, object]:
    """Return the explicit full-valuation H-h_d information-loss ceiling."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")

    K = k - 1
    X = k * (k + 2) - 1
    d = logarithmic_degree(k)
    low = transverse_primorial_depth_below(k, K)
    high = transverse_primorial_depth_below(k, X)
    j_low = int(low["depth"])
    j_high = int(high["depth"])
    e_low = _choose(j_low - 1, order)
    e_high = _choose(j_high - 1, order)

    a = log(K)
    b = log(X)
    c0 = log(k * k + 1)
    low_exact = (
        (a / (b - a))
        * ((a / b) ** (d - 1))
        * (((d - 1) ** (d - 1)) / (d**d))
    )
    high_floor = ((c0 / b) ** (d - 1)) * ((c0 - a) / (b - a))
    high_loss_exact = 1.0 - high_floor

    low_simple = (2.0 ** (-(d - 1))) / d
    high_simple = (d + 1) / (k * log(k))
    simple_ceiling = e_high * (d + 1) / log(k) + e_low * 2.0 / d
    exact_support_depth_ceiling = k * (e_high * high_loss_exact + e_low * low_exact)

    if low_exact > low_simple + 1e-15:
        raise AssertionError("exact low loss exceeded the simple dyadic bound")
    if high_loss_exact > high_simple + 1e-15:
        raise AssertionError("exact high loss exceeded the simple spectral-gap bound")
    if exact_support_depth_ceiling > simple_ceiling + 1e-12:
        raise AssertionError("exact support-depth ceiling exceeded the simple ceiling")

    return {
        "k": k,
        "order": order,
        "logarithmic_degree": d,
        "universal_full_valuation_cap": universal_full_valuation_cap(k),
        "low_transverse_depth": j_low,
        "high_transverse_depth": j_high,
        "low_max_defect_per_row": e_low,
        "high_max_defect_per_row": e_high,
        "exact_low_negative_magnitude_ceiling": low_exact,
        "simple_low_negative_magnitude_ceiling": low_simple,
        "exact_high_loss_ceiling_per_unit": high_loss_exact,
        "simple_high_loss_ceiling_per_unit": high_simple,
        "exact_support_depth_information_loss_ceiling": exact_support_depth_ceiling,
        "simple_information_loss_ceiling": simple_ceiling,
        "statement": "H_minus_h_log_degree_is_below_returned_ceiling",
    }
