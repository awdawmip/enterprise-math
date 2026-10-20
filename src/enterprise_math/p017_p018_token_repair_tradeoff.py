"""Exact proof-order / repair-alphabet tradeoff at the first reusable order-five critical scale.

The anchor-critical scale

    k = 524287 = 2^19-1

has no effective odd anchor.  For order-five Bonferroni defect, each squarefree
row token contains six distinct odd primes.  The minimum possible token is

    D0 = 3*5*7*11*13*17 = 255255.

The second-smallest product of six distinct odd primes is obtained by replacing
17 with 19:

    D1 = 3*5*7*11*13*19 = 285285.

Since

    D0 <= (k-1)/2 < D1,

CG12 says every order-five token except D0 has signed reuse capacity at most
two.  D0 is the only token for which the universal floor bound could be three.
Its actual parity/divisibility residue class in the signed window has exactly two
points:

    x = -345469, 165041.

The corresponding states factor as

    M-(-345469) = 3*5^5*7*11*13*17*1723,
    M-165041    = 3*5*7^3*11*13*17*21977.

Thus D0 is an actual order-five defect token at both points.  Removing the full
selected prime-power blocks leaves quotients 1723 and 21977, whose integer
square roots are 41 and 148.  Hence the natural repaired observable

    (D_rad, R_2(q_full))

separates the only potentially three-slot token fiber, while every other token
already has at most two signed incidences.

In particular the actual order-five token quotient at this scale has maximum
fiber multiplicity exactly two.  One binary incidence-repair symbol is therefore
necessary and sufficient if exact token-incidence identity is required.  By
contrast order seven is already globally single-use by the transverse-primorial
threshold, so it needs no such repair.

This is a scale-specific exact tradeoff theorem, not a general P023 mother
result and not a Legendre proof.  It demonstrates that proof order and repair
alphabet are distinct resources that can substitute for one another.
"""

from __future__ import annotations

from math import isqrt

from .legendre import is_prime
from .p017_p018_token_reuse_precision import defect_token_reuse_capacity


CRITICAL_K = 524_287
MIN_ORDER5_TOKEN = 255_255
SECOND_ORDER5_TOKEN = 285_285
MIN_TOKEN_PRIMES = (3, 5, 7, 11, 13, 17)


def _odd_signed_residue_points(k: int, center: int, divisor: int) -> tuple[int, ...]:
    if divisor <= 0 or divisor % 2 == 0:
        raise ValueError("divisor must be positive odd")
    residue = center % divisor
    if residue % 2 == 0:
        residue += divisor
    modulus = 2 * divisor
    lower = -(k - 1)
    upper = k - 1

    # Shift the canonical odd representative to the first point >=lower.
    point = residue
    while point - modulus >= lower:
        point -= modulus
    while point < lower:
        point += modulus

    points: list[int] = []
    while point <= upper:
        points.append(point)
        point += modulus
    return tuple(points)


def _product(values: tuple[int, ...]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def critical_524287_order5_binary_tradeoff() -> dict[str, object]:
    """Certify exact binary repair versus one extra odd-order precision quantum."""
    k = CRITICAL_K
    center = k * (k + 1)
    half_window = (k - 1) // 2

    if _product(MIN_TOKEN_PRIMES) != MIN_ORDER5_TOKEN:
        raise AssertionError("minimum six-prime token product changed")
    second_primes = (3, 5, 7, 11, 13, 19)
    if _product(second_primes) != SECOND_ORDER5_TOKEN:
        raise AssertionError("second six-prime token product changed")
    if not MIN_ORDER5_TOKEN <= half_window < SECOND_ORDER5_TOKEN:
        raise AssertionError("unique possible three-slot token inequality failed")

    # Every other six-prime token is at least SECOND_ORDER5_TOKEN, hence has
    # floor((k-1)/D)+1 <=2.  Only the minimum token needs exact residue analysis.
    points = _odd_signed_residue_points(k, center, MIN_ORDER5_TOKEN)
    expected_points = (-345_469, 165_041)
    if points != expected_points:
        raise AssertionError("minimum token did not have the exact two-point signed fiber")

    state_left = center - points[0]
    state_right = center - points[1]
    left_full_block = 3 * 5**5 * 7 * 11 * 13 * 17
    right_full_block = 3 * 5 * 7**3 * 11 * 13 * 17
    left_q = state_left // left_full_block
    right_q = state_right // right_full_block

    if state_left != left_full_block * 1723:
        raise AssertionError("left repeated-token factorization changed")
    if state_right != right_full_block * 21977:
        raise AssertionError("right repeated-token factorization changed")
    if not is_prime(left_q) or not is_prime(right_q):
        raise AssertionError("repeated-token repair quotients are not prime")

    left_root = isqrt(left_q)
    right_root = isqrt(right_q)
    if (left_q, right_q) != (1723, 21977) or (left_root, right_root) != (41, 148):
        raise AssertionError("repeated-token quotient/root repair data changed")
    if left_root == right_root:
        raise AssertionError("child quotient-root failed to separate the repeated token fiber")

    order5 = defect_token_reuse_capacity(k, 5)
    order7 = defect_token_reuse_capacity(k, 7)
    if int(order5["universal_signed_reuse_capacity"]) != 3:
        raise AssertionError("order-five universal CG12 capacity changed")
    if int(order7["universal_signed_reuse_capacity"]) != 1:
        raise AssertionError("order-seven token family is not globally single-use")

    actual_order5_max_fiber = 2
    return {
        "k": k,
        "order5": order5,
        "order7": order7,
        "half_signed_window": half_window,
        "minimum_order5_token": MIN_ORDER5_TOKEN,
        "second_order5_token": SECOND_ORDER5_TOKEN,
        "only_possible_three_slot_token": MIN_ORDER5_TOKEN,
        "minimum_token_signed_points": points,
        "minimum_token_states": (state_left, state_right),
        "full_block_quotients": (left_q, right_q),
        "child_quotient_roots": (left_root, right_root),
        "child_root_repairs_minimum_fiber": True,
        "actual_order5_max_token_fiber": actual_order5_max_fiber,
        "binary_repair_symbols_needed_for_exact_incidence": 2,
        "binary_repair_bits": 1,
        "order7_repair_symbols_needed": 1,
        "order7_repair_bits": 0,
        "proof_order_quantum_exchange": (5, 1, 7, 0),
    }
