"""Fourth-root support-depth recovery for the P017/P018 square interval.

Let

    I_k = {k^2+1,...,k^2+2k},
    U_k = k^2+2k,
    z = floor(U_k^(1/4)).

After removing every prime <= z, every survivor has Omega <= 3.  For one
z-rough survivor n define the *medium support depth*

    c(n) = #{p prime : z < p <= k and p | n}.

Every composite n in I_k has a prime factor <= k, while roughness excludes all
such factors <= z.  Hence

    n is prime iff c(n)=0,
    0 <= c(n) <= 3.

The prime indicator therefore has the exact finite residual-support polynomial

    1_P(n) = 1 - c + C(c,2) - C(c,3).

If R is the number of z-rough survivors and

    S_j = sum_n C(c(n),j),

then

    prime_gap(k) = R - S_1 + S_2 - S_3.

A useful degree-two lower polynomial is obtained by interpolating the composite
support depths c=1 and c=3:

    w_2(c) = (c-1)(c-3)/3
           = 1 - c + (2/3) C(c,2).

For c=0,1,2,3 its values are 1,0,-1/3,0.  Therefore, with N_2 the number of
rough survivors of support depth exactly two,

    3*prime_gap(k) = 3R - 3S_1 + 2S_2 + N_2,

and

    3R - 3S_1 + 2S_2 > 0

is already a rigorous Legendre certificate.  The dominant squarefree triple
class c=3 is annihilated exactly by this quadratic weight.  The only negative
slack is the repeated-factor triple class c=2.

Token reuse has a sharp root-cutoff form.  At the general P_m cutoff

    z_m = floor(U_k^(1/(m+1))),

a squarefree j-medium-prime token D has

    D >= (z_m+1)^j.

If 2j >= m+1 then D>k.  Since the square interval consists of odd survivors
once 2 is pre-sieved, parity plus divisibility places a token incidence in one
class modulo 2D; therefore any such token is globally single-use across a
window of length 2k.  At P3, j>=2 already satisfies this condition.  Thus all
pair/triple corrections S_2,S_3 are single-use; only the first-order prime
columns S_1 can repeat.

The c=2 repeated layer also has a correct finite capacity bound.  Such a state
has a unique repeated prime p>z with p^2 | n.  Since (z+1)^2>k, the odd p^2
column is single-use, while the remaining rough prime factor is at least z+1;
therefore

    p <= floor(sqrt(U_k/(z+1))).

This corrects an earlier over-strong experimental bound which put the repeated
prime below the cubic P2 cutoff.

The functions below are executable research references and bounded regression
oracles.  They do not replace the proofs above and do not claim Legendre's
conjecture.
"""

from __future__ import annotations

from itertools import combinations
from math import comb, gcd, isqrt, prod

from .legendre import direct_square_interval_prime_count, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import (
    almost_prime_cutoff,
    rough_survivor_offsets,
    square_interval_upper,
)


def root_p3_cutoff(k: int) -> int:
    """Return the exact fourth-root cutoff z_3(k)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    return int(almost_prime_cutoff(k, 3)["cutoff"])


def medium_prime_support(k: int, value: int) -> tuple[int, ...]:
    """Return distinct prime divisors p of value with z_3(k)<p<=k."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be a positive integer")
    z = root_p3_cutoff(k)
    return tuple(p for p in primes_up_to(k) if p > z and value % p == 0)


def exact_prime_indicator_from_support_depth(depth: int) -> int:
    """Return 1-c+C(c,2)-C(c,3) for 0<=c<=3."""
    if isinstance(depth, bool) or not isinstance(depth, int) or not 0 <= depth <= 3:
        raise ValueError("depth must be an integer in 0..3")
    return 1 - depth + comb(depth, 2) - comb(depth, 3)


def quadratic_lower_weight_numerator(depth: int) -> int:
    """Return 3*w_2(c)=3-3c+2*C(c,2), avoiding fractions."""
    if isinstance(depth, bool) or not isinstance(depth, int) or not 0 <= depth <= 3:
        raise ValueError("depth must be an integer in 0..3")
    return 3 - 3 * depth + 2 * comb(depth, 2)


def root_cutoff_token_capacity(k: int, omega_bound: int, token_order: int) -> dict[str, object]:
    """Certify when j-medium-prime tokens are forced above the radius k.

    If 2*j >= m+1 at the P_m cutoff, the strict next-root inequality gives
    (z_m+1)^(2j) >= (z_m+1)^(m+1) > U_k > k^2, hence every such token exceeds k.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(omega_bound, bool) or not isinstance(omega_bound, int) or omega_bound < 1:
        raise ValueError("omega_bound must be positive")
    if isinstance(token_order, bool) or not isinstance(token_order, int) or not 1 <= token_order <= omega_bound:
        raise ValueError("token_order must lie in 1..omega_bound")

    data = almost_prime_cutoff(k, omega_bound)
    z = int(data["cutoff"])
    lower = (z + 1) ** token_order
    threshold_order = (omega_bound + 2) // 2
    structurally_single_use = 2 * token_order >= omega_bound + 1
    if structurally_single_use and lower <= k:
        raise AssertionError("root-cutoff single-use inequality failed")

    return {
        "k": k,
        "omega_bound": omega_bound,
        "cutoff": z,
        "token_order": token_order,
        "minimum_token_product": lower,
        "first_structurally_single_use_order": threshold_order,
        "structurally_single_use": structurally_single_use,
        "token_exceeds_k": lower > k,
        "odd_token_modulus_exceeds_window": 2 * lower > 2 * k,
    }


def repeated_support_prime_ceiling(k: int) -> int:
    """Return floor(sqrt(U_k/(z_3+1))) for the repeated-factor prime."""
    z = root_p3_cutoff(k)
    upper = square_interval_upper(k)
    return isqrt(upper // (z + 1))


def odd_token_candidate(k: int, token: int) -> dict[str, int | bool]:
    """Return the unique possible odd multiple of token in I_k when token>k."""
    if isinstance(token, bool) or not isinstance(token, int) or token <= k or token % 2 == 0:
        raise ValueError("token must be an odd integer > k")
    lower = k * k
    upper = square_interval_upper(k)
    quotient = lower // token + 1
    if quotient % 2 == 0:
        quotient += 1
    value = token * quotient
    return {
        "k": k,
        "token": token,
        "odd_quotient": quotient,
        "candidate_value": value,
        "candidate_offset": value - lower,
        "lies_in_square_interval": lower < value <= upper,
        "single_use": 2 * token > 2 * k,
    }


def root_p3_support_profile(k: int) -> dict[str, object]:
    """Enumerate the exact fourth-root support polynomial for bounded research."""
    z = root_p3_cutoff(k)
    offsets = rough_survivor_offsets(k, z)
    medium_primes = tuple(p for p in primes_up_to(k) if p > z)

    depth_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    moments = [len(offsets), 0, 0, 0]
    pair_usage: dict[tuple[int, int], int] = {}
    triple_usage: dict[tuple[int, int, int], int] = {}

    for offset in offsets:
        value = k * k + offset
        support = tuple(p for p in medium_primes if value % p == 0)
        depth = len(support)
        if depth > 3:
            raise AssertionError("fourth-root rough survivor exceeded support depth three")
        depth_counts[depth] += 1
        for j in (1, 2, 3):
            moments[j] += comb(depth, j)
        for token_support in combinations(support, 2):
            pair_usage[token_support] = pair_usage.get(token_support, 0) + 1
        for token_support in combinations(support, 3):
            triple_usage[token_support] = triple_usage.get(token_support, 0) + 1

    rough_count, s1, s2, s3 = moments
    prime_count = direct_square_interval_prime_count(k)
    exact_recovery = rough_count - s1 + s2 - s3
    quadratic_numerator = 3 * rough_count - 3 * s1 + 2 * s2
    depth_two = depth_counts[2]

    if exact_recovery != prime_count:
        raise AssertionError("support-depth polynomial failed to recover the prime count")
    if 3 * prime_count != quadratic_numerator + depth_two:
        raise AssertionError("quadratic support certificate identity failed")
    if pair_usage and max(pair_usage.values()) > 1:
        raise AssertionError("a pair token was reused inside the fourth-root survivor set")
    if triple_usage and max(triple_usage.values()) > 1:
        raise AssertionError("a triple token was reused inside the fourth-root survivor set")

    repeated_bound_primes = tuple(
        p for p in medium_primes if p <= repeated_support_prime_ceiling(k)
    )
    if depth_two > len(repeated_bound_primes):
        raise AssertionError("repeated-support states exceeded the square-column capacity bound")

    return {
        "k": k,
        "upper": square_interval_upper(k),
        "fourth_root_cutoff": z,
        "rough_offsets": offsets,
        "rough_count": rough_count,
        "support_moment_1": s1,
        "support_moment_2": s2,
        "support_moment_3": s3,
        "support_depth_counts": tuple(depth_counts[j] for j in range(4)),
        "prime_count": prime_count,
        "exact_support_polynomial_prime_count": exact_recovery,
        "quadratic_certificate_numerator": quadratic_numerator,
        "depth_two_repeated_count": depth_two,
        "quadratic_identity_rhs": quadratic_numerator + depth_two,
        "pair_token_max_usage": max(pair_usage.values(), default=0),
        "triple_token_max_usage": max(triple_usage.values(), default=0),
        "repeated_prime_ceiling": repeated_support_prime_ceiling(k),
        "repeated_square_column_capacity_bound": len(repeated_bound_primes),
        "quadratic_positive_forces_prime": quadratic_numerator > 0,
    }
