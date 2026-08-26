"""Orientation-Walsh sieve for the P017 centered mirror pair.

This module preserves a piece of P017 information that is lost when the two
mirror orientations are flattened into one ordinary Jacobsthal/roughness
interval: L043 says that on an anchor-surviving radius the transverse supports
of M-r and M+r are disjoint.

Fix M=k(k+1), 1<=r<k, gcd(r,M)=1.  Let L(r),U(r) be the transverse odd-prime
supports of M-r and M+r and put c_-=|L|, c_+=|U|.  Define

    W_r(z)=(1+z)^c_- (1-z)^c_+.

The endpoint weights are exact prime detectors with an opposite-side divisor
amplifier:

    W_r(1)  = 2^c_-  1_{M+r prime},
    W_r(-1) = 2^c_+  1_{M-r prime}.

Indeed an open-square composite side always has a transverse prime <=k, while
L043 prevents a prime from hitting both orientations.  Hence the nonnegative
quantity W_r(1)+W_r(-1) is positive iff at least one side of that mirror radius
is prime.

Write sigma_p(r)=+1 if p|(M-r), -1 if p|(M+r).  Expanding W gives signed
squarefree incidences.  For a nonempty selected transverse prime set T, define

    A_T = sum_r prod_{p in T} sigma_p(r)

where r runs over anchor-surviving radii for which every p in T divides one of
the two mirror states.  Each p has two root choices r=+/-M (mod p).  For one
root pattern epsilon in {+1,-1}^T the root weight is prod epsilon_p.

After imposing odd parity and anchor survival by Mobius inclusion-exclusion,
each root pattern is one residue class modulo 2*a*prod(T).  Its count in
1<=r<=k-1 is

    floor((k-1)/(2*a*prod(T))) + boundary_bit.

The floor term is independent of epsilon, while

    sum_epsilon prod epsilon_p = 0

for nonempty T.  Therefore **every nonconstant orientation-Walsh column has
exactly zero floor/density bulk**.  A_T is a finite signed sum of boundary bits
only.  This differs from the ordinary positive roughness projector, whose local
Euler factors carry the parity barrier in their main density.

Equivalently the one-prime local factor of the upper-prime weight is

    1 + 1_{p|M-r} - 1_{p|M+r}.

Across a complete p-period its mean is exactly

    (2 + 0 + (p-2)*1)/p = 1.

Thus the Walsh sieve is ``parity-balanced'' at the local-density level.  This is
an exact representation theorem, not a proof of Legendre: controlling the
finite boundary discrepancy of the product over all p may still encode the
full short-interval prime problem.
"""

from __future__ import annotations

from itertools import product
from math import comb, prod

from .legendre import squarefree_divisors_with_mu
from .p017_mirror import anchor_surviving_radius, mirror_pair, mirror_transverse_supports
from .p017_p018_effective_anchor import effective_odd_anchor_primes


def _crt_pair(residue: int, modulus: int, target: int, target_modulus: int) -> tuple[int, int]:
    """Combine two coprime congruences."""
    if target_modulus == 1:
        return residue % modulus, modulus
    inverse = pow(modulus, -1, target_modulus)
    step = ((target - residue) * inverse) % target_modulus
    new_modulus = modulus * target_modulus
    return (residue + modulus * step) % new_modulus, new_modulus


def _positive_class_count(limit: int, residue: int, modulus: int) -> dict[str, int]:
    """Count one nonzero residue class modulo modulus in 1..limit."""
    if limit < 0 or modulus <= 0:
        raise ValueError("invalid positive-class count parameters")
    residue %= modulus
    first = residue if residue else modulus
    if first > limit:
        exact = 0
    else:
        exact = 1 + (limit - first) // modulus
    coarse, remainder = divmod(limit, modulus)
    carry = int(residue != 0 and residue <= remainder)
    if exact != coarse + carry:
        raise AssertionError("positive residue-class count did not split into floor plus carry")
    return {
        "residue": residue,
        "modulus": modulus,
        "coarse": coarse,
        "remainder": remainder,
        "boundary_bit": carry,
        "exact_count": exact,
    }


def orientation_walsh_point(k: int, radius: int) -> dict[str, object]:
    """Return W_r coefficients and exact endpoint prime weights."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1<=radius<k")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    lower, upper = mirror_pair(k, radius)
    lower_support, upper_support = mirror_transverse_supports(k, radius)
    c_lower = len(lower_support)
    c_upper = len(upper_support)

    coefficients: list[int] = []
    for degree in range(c_lower + c_upper + 1):
        coefficient = 0
        for lower_degree in range(max(0, degree - c_upper), min(c_lower, degree) + 1):
            upper_degree = degree - lower_degree
            coefficient += (
                comb(c_lower, lower_degree)
                * comb(c_upper, upper_degree)
                * ((-1) ** upper_degree)
            )
        coefficients.append(coefficient)

    at_plus_one = (2**c_lower) if c_upper == 0 else 0
    at_minus_one = (2**c_upper) if c_lower == 0 else 0
    reconstructed_plus = sum(coefficients)
    reconstructed_minus = sum(((-1) ** degree) * value for degree, value in enumerate(coefficients))
    if reconstructed_plus != at_plus_one or reconstructed_minus != at_minus_one:
        raise AssertionError("orientation-Walsh endpoint evaluation failed")

    lower_prime = c_lower == 0
    upper_prime = c_upper == 0
    if (at_plus_one > 0) != upper_prime or (at_minus_one > 0) != lower_prime:
        raise AssertionError("orientation-Walsh endpoint did not detect prime mirror side")

    return {
        "k": k,
        "radius": radius,
        "lower_state": lower,
        "upper_state": upper,
        "lower_support": tuple(lower_support),
        "upper_support": tuple(upper_support),
        "lower_support_size": c_lower,
        "upper_support_size": c_upper,
        "walsh_coefficients": tuple(coefficients),
        "upper_prime_weight_W_plus_one": at_plus_one,
        "lower_prime_weight_W_minus_one": at_minus_one,
        "at_least_one_prime_side": lower_prime or upper_prime,
    }


def orientation_walsh_profile(k: int) -> dict[str, object]:
    """Aggregate signed levels and exact weighted prime-side observable."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    rows: list[dict[str, object]] = []
    levels: list[int] = []
    upper_weight = 0
    lower_weight = 0
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        row = orientation_walsh_point(k, radius)
        rows.append(row)
        coefficients = tuple(int(value) for value in row["walsh_coefficients"])
        if len(levels) < len(coefficients):
            levels.extend([0] * (len(coefficients) - len(levels)))
        for degree, value in enumerate(coefficients):
            levels[degree] += value
        upper_weight += int(row["upper_prime_weight_W_plus_one"])
        lower_weight += int(row["lower_prime_weight_W_minus_one"])

    surviving = len(rows)
    if not levels or levels[0] != surviving:
        raise AssertionError("Walsh constant level is not the surviving-radius count")
    weighted_observable = upper_weight + lower_weight
    even_reconstruction = 2 * sum(levels[degree] for degree in range(0, len(levels), 2))
    if weighted_observable != even_reconstruction:
        raise AssertionError("even signed levels did not reconstruct endpoint observable")
    prime_exists = any(bool(row["at_least_one_prime_side"]) for row in rows)
    if (weighted_observable > 0) != prime_exists:
        raise AssertionError("positive Walsh observable is not equivalent to a prime mirror side")

    return {
        "k": k,
        "surviving_radius_count": surviving,
        "signed_levels": tuple(levels),
        "upper_prime_weight": upper_weight,
        "lower_prime_weight": lower_weight,
        "weighted_prime_side_observable": weighted_observable,
        "nonconstant_even_signed_sum": sum(
            levels[degree] for degree in range(2, len(levels), 2)
        ),
        "absolute_nonconstant_even_level_sum": sum(
            abs(levels[degree]) for degree in range(2, len(levels), 2)
        ),
        "prime_mirror_side_exists": prime_exists,
        "rows": tuple(rows),
    }


def orientation_signed_root_fiber(k: int, selected_primes: tuple[int, ...]) -> dict[str, object]:
    """Reconstruct one signed squarefree column as boundary bits only.

    selected_primes must be a nonempty set of transverse odd primes <=k.
    +1 root means p|(M-r); -1 root means p|(M+r).
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    normalized = tuple(sorted(int(p) for p in selected_primes))
    if not normalized or len(set(normalized)) != len(normalized):
        raise ValueError("selected_primes must be nonempty and distinct")
    M = k * (k + 1)
    K = k - 1
    for prime in normalized:
        if prime < 3 or prime > k or prime % 2 == 0 or M % prime == 0:
            raise ValueError("selected primes must be odd transverse primes <=k")

    anchors = effective_odd_anchor_primes(k)
    anchor_rows = squarefree_divisors_with_mu(list(anchors))
    selected_product = prod(normalized)
    total_exact = 0
    total_boundary = 0
    pattern_rows: list[dict[str, object]] = []

    for anchor_divisor, mu in anchor_rows:
        weighted_exact = 0
        weighted_boundary = 0
        common_coarse: int | None = None
        sign_weight_sum = 0
        for signs in product((1, -1), repeat=len(normalized)):
            residue, modulus = 1, 2  # anchor survival includes odd parity
            if anchor_divisor > 1:
                residue, modulus = _crt_pair(residue, modulus, 0, anchor_divisor)
            sign_weight = 1
            for prime, sign in zip(normalized, signs):
                target = (sign * M) % prime
                residue, modulus = _crt_pair(residue, modulus, target, prime)
                sign_weight *= sign
            count = _positive_class_count(K, residue, modulus)
            expected_modulus = 2 * anchor_divisor * selected_product
            if modulus != expected_modulus:
                raise AssertionError("root-pattern CRT modulus is not 2*a*d")
            coarse = int(count["coarse"])
            if common_coarse is None:
                common_coarse = coarse
            elif common_coarse != coarse:
                raise AssertionError("root-pattern floor bulk depends on orientation")
            weighted_exact += sign_weight * int(count["exact_count"])
            weighted_boundary += sign_weight * int(count["boundary_bit"])
            sign_weight_sum += sign_weight
            pattern_rows.append(
                {
                    "anchor_divisor": anchor_divisor,
                    "anchor_mu": mu,
                    "orientation_signs": tuple(signs),
                    "orientation_weight": sign_weight,
                    **count,
                }
            )
        if sign_weight_sum != 0:
            raise AssertionError("nonempty Walsh root cube did not annihilate its constant mode")
        if weighted_exact != weighted_boundary:
            raise AssertionError("orientation-signed root fiber retained nonzero floor bulk")
        total_exact += mu * weighted_exact
        total_boundary += mu * weighted_boundary

    direct = 0
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        lower_support, upper_support = mirror_transverse_supports(k, radius)
        lower_set = set(lower_support)
        upper_set = set(upper_support)
        weight = 1
        visible = True
        for prime in normalized:
            if prime in lower_set:
                weight *= 1
            elif prime in upper_set:
                weight *= -1
            else:
                visible = False
                break
        if visible:
            direct += weight

    if total_exact != direct or total_boundary != direct:
        raise AssertionError("orientation boundary root decomposition disagrees with direct mirror incidence")
    return {
        "k": k,
        "selected_primes": normalized,
        "selected_product": selected_product,
        "effective_odd_anchors": anchors,
        "direct_signed_fiber": direct,
        "mobius_root_exact_sum": total_exact,
        "mobius_boundary_only_sum": total_boundary,
        "floor_bulk_exactly_zero": True,
        "pattern_rows": tuple(pattern_rows),
    }
