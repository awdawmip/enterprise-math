"""Soft endpoint compiler for the P017 orientation-Walsh prime detector.

The hard orientation-Walsh endpoint t=1 is an exact prime detector, but its
local factors take the extreme values 2,0,1.  There is a unique mean-one soft
interpolation obtained by replacing these values by

    2-epsilon, epsilon, 1,

or equivalently t=1-epsilon in

    F_(x,y)(t)=(1+t)^x(1-t)^y+(1+t)^y(1-t)^x,

where x,y are the two disjoint mirror support sizes.  The complete one-prime
mean stays one for every epsilon, and the one-orientation second moment is

    1 + 2(1-epsilon)^2/p.

Let J_pair(k) be the largest number of distinct transverse odd primes whose
prefix product is still below M^2, M=k(k+1).  Since the two mirror supports are
disjoint and their radicals divide (M-r)(M+r)<M^2,

    x+y <= J_pair(k).

If both mirror sides are composite, x,y>=1.  For fixed c=x+y the soft pair
weight is maximized at the extreme split {1,c-1}; these maxima are nondecreasing
in c.  Hence every prime-free mirror pair obeys the exact uniform ceiling

    B_J(epsilon)
      =(2-epsilon)*epsilon^(J-1)
       +epsilon*(2-epsilon)^(J-1).

Choose the task-relative softness

    epsilon_J = 2^(1-J).

For J>=3 one has B_J(epsilon_J)<1.  Therefore

    sum_r F_r(1-epsilon_J) > R_surv

is a sufficient prime certificate, while the complete-period pair mean is 2.
So this compiler replaces hard endpoint positivity by a constant-factor
short-window mean-transfer target: retaining more than half of the complete
mean already forces a prime.

There is also a sharp negative lesson.  Any softness making the worst bad-pair
weight O(1) must be exponentially small in J, because the extreme (1,J-1)
pair already contributes

    epsilon*(2-epsilon)^(J-1).

Thus t remains exponentially close to the hard endpoint as support depth grows.
The soft one-prime second moment consequently remains asymptotically as hard as
1+2/p; this is a target compiler, not free Fourier smoothing.

Finally, in the endpoint coordinate u=1-t the same pair polynomial has vanishing
order min(x,y) when x,y>0, and order zero iff at least one mirror side is prime.
This packages mirror support depth as an exact endpoint jet.

This module is a finite algebraic bridge, not a Legendre proof and not a
short-window discrepancy theorem.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

from .legendre import primes_up_to
from .p017_mirror import anchor_surviving_radius, mirror_transverse_supports


def pair_transverse_support_ceiling(k: int) -> dict[str, object]:
    """Return J_pair from the transverse primorial barrier below M^2."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    M = k * (k + 1)
    cutoff = M * M
    product = 1
    chosen: list[int] = []
    for prime in primes_up_to(k):
        if prime == 2 or M % prime == 0:
            continue
        if product > (cutoff - 1) // prime:
            break
        product *= prime
        chosen.append(prime)
    return {
        "k": k,
        "center": M,
        "pair_product_cutoff": cutoff,
        "pair_support_ceiling": len(chosen),
        "transverse_prime_prefix": tuple(chosen),
        "prefix_product": product,
    }


def balanced_soft_local_moments(prime: int, epsilon: Fraction) -> dict[str, Fraction]:
    """Return exact mean/second moment of the unique neutral mean-one soft factor."""
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 3:
        raise ValueError("prime must be an odd integer >=3")
    if not (Fraction(0, 1) <= epsilon <= Fraction(1, 1)):
        raise ValueError("epsilon must lie in [0,1]")
    lower = Fraction(2, 1) - epsilon
    upper = epsilon
    neutral = Fraction(1, 1)
    mean = (lower + upper + (prime - 2) * neutral) / prime
    second = (lower * lower + upper * upper + (prime - 2) * neutral) / prime
    expected_second = Fraction(1, 1) + Fraction(2, prime) * (1 - epsilon) ** 2
    if mean != 1 or second != expected_second:
        raise AssertionError("soft Walsh local moment identity failed")
    return {
        "epsilon": epsilon,
        "lower_hit_value": lower,
        "upper_hit_value": upper,
        "neutral_value": neutral,
        "mean": mean,
        "second_moment": second,
    }


def soft_pair_weight(lower_support_size: int, upper_support_size: int, epsilon: Fraction) -> Fraction:
    """Evaluate the symmetric soft pair weight exactly."""
    for value in (lower_support_size, upper_support_size):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("support sizes must be nonnegative integers")
    if not (Fraction(0, 1) <= epsilon <= Fraction(1, 1)):
        raise ValueError("epsilon must lie in [0,1]")
    a = Fraction(2, 1) - epsilon
    b = epsilon
    x = lower_support_size
    y = upper_support_size
    return (a**x) * (b**y) + (a**y) * (b**x)


def prime_free_soft_pair_ceiling(total_support_ceiling: int, epsilon: Fraction) -> Fraction:
    """Return the exact worst pair weight over x,y>=1 and x+y<=J."""
    if (
        isinstance(total_support_ceiling, bool)
        or not isinstance(total_support_ceiling, int)
        or total_support_ceiling < 2
    ):
        raise ValueError("total_support_ceiling must be an integer >=2")
    J = total_support_ceiling
    a = Fraction(2, 1) - epsilon
    b = epsilon
    claimed = a * (b ** (J - 1)) + b * (a ** (J - 1))
    direct = max(
        soft_pair_weight(x, c - x, epsilon)
        for c in range(2, J + 1)
        for x in range(1, c)
    )
    if claimed != direct:
        raise AssertionError("extreme support split did not maximize the soft bad-pair weight")
    return claimed


def endpoint_jet_coefficients(lower_support_size: int, upper_support_size: int) -> tuple[int, ...]:
    """Expand F(1-u) in powers of u exactly."""
    x = lower_support_size
    y = upper_support_size
    for value in (x, y):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("support sizes must be nonnegative integers")
    coeff = [0] * (x + y + 1)
    # (2-u)^x u^y
    for j in range(x + 1):
        coeff[y + j] += ((-1) ** j) * comb(x, j) * (2 ** (x - j))
    # (2-u)^y u^x
    for j in range(y + 1):
        coeff[x + j] += ((-1) ** j) * comb(y, j) * (2 ** (y - j))
    while len(coeff) > 1 and coeff[-1] == 0:
        coeff.pop()
    return tuple(coeff)


def endpoint_jet_order(lower_support_size: int, upper_support_size: int) -> dict[str, object]:
    """Return the exact u=0 vanishing order of one mirror-pair soft polynomial."""
    coeff = endpoint_jet_coefficients(lower_support_size, upper_support_size)
    order = next((index for index, value in enumerate(coeff) if value), None)
    if order is None:
        raise AssertionError("soft pair polynomial vanished identically")
    expected = min(lower_support_size, upper_support_size)
    if order != expected:
        raise AssertionError("endpoint jet order did not equal minimum mirror support depth")
    leading = coeff[order]
    if leading <= 0:
        raise AssertionError("first endpoint-jet coefficient must be positive")
    return {
        "lower_support_size": lower_support_size,
        "upper_support_size": upper_support_size,
        "vanishing_order_at_t_one": order,
        "leading_u_coefficient": leading,
        "prime_side_detected_at_order_zero": order == 0,
        "u_coefficients": coeff,
    }


def soft_walsh_profile(k: int) -> dict[str, object]:
    """Evaluate the canonical epsilon=2^(1-J) soft compiler on the physical basin."""
    ceiling = pair_transverse_support_ceiling(k)
    J = int(ceiling["pair_support_ceiling"])
    if J < 2:
        epsilon = Fraction(1, 2)
        bad_ceiling = None
    else:
        epsilon = Fraction(1, 2 ** (J - 1))
        bad_ceiling = prime_free_soft_pair_ceiling(J, epsilon)
    rows: list[dict[str, object]] = []
    total = Fraction(0, 1)
    prime_exists = False
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        lower_support, upper_support = mirror_transverse_supports(k, radius)
        x = len(lower_support)
        y = len(upper_support)
        if x + y > J:
            raise AssertionError("actual mirror support exceeded the pair primorial ceiling")
        weight = soft_pair_weight(x, y, epsilon)
        jet = endpoint_jet_order(x, y)
        prime = bool(jet["prime_side_detected_at_order_zero"])
        prime_exists = prime_exists or prime
        total += weight
        rows.append(
            {
                "radius": radius,
                "lower_support_size": x,
                "upper_support_size": y,
                "soft_pair_weight": weight,
                "endpoint_jet_order": int(jet["vanishing_order_at_t_one"]),
                "at_least_one_prime_side": prime,
            }
        )
    R = len(rows)
    if R == 0:
        raise AssertionError("soft Walsh profile has no surviving radii")
    certificate = bad_ceiling is not None and total > R * bad_ceiling
    if certificate and not prime_exists:
        raise AssertionError("soft Walsh sufficient certificate fired without a prime side")
    return {
        **ceiling,
        "epsilon": epsilon,
        "t": Fraction(1, 1) - epsilon,
        "surviving_radius_count": R,
        "complete_period_pair_mean": Fraction(2, 1),
        "prime_free_pair_weight_ceiling": bad_ceiling,
        "soft_weight_sum": total,
        "soft_physical_average": total / R,
        "soft_prime_certificate": certificate,
        "prime_mirror_side_exists": prime_exists,
        "rows": tuple(rows),
    }
