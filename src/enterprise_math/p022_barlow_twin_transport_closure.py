"""Finite closure of the strict twin-deferred Franel window.

For a twin center r and a primitive Franel prime q with
3r-1 < q < 4r-3, the earlier transport theorem reduces every survivor of the
3r-1 gate to the scaled twin center m=3r/2.  The two fixed later segments
3r+1 and 3r+2 then close the window: if 6r+1 is composite the first gives
valuation -v_q(F_r); if 6r+1 is prime the second gives +v_q(F_r).
Hence every such q is detected no later than 3r+2.  Since 4r-3 is divisible by
3 for a nontrivial twin center, the next open prime range starts at q>=4r-1.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import _is_prime, composite_A_relation_exponents
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center
from .p022_barlow_twin_defect_difference import twin_blackout_target
from .p022_barlow_twin_transport_window import (
    _require_strict_transport,
    strict_transport_survival_requires_scaled_twin,
)


def scaled_twin_n1_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    twin_blackout_target(rank)
    if rank % 2:
        raise ValueError("r must be even")
    middle = 3 * rank // 2
    if not is_twin_prime_deferral_center(middle):
        raise ValueError("3r/2 must be a twin center")
    segment = 3 * rank + 1
    if _is_prime(6 * rank + 1):
        raise ValueError("D_(3r+1) is absent")
    high = tuple((i, e) for i, e in composite_A_relation_exponents(segment) if i >= rank)
    expected = ((middle, 1), (middle + 1, -1), (3 * rank, 1))
    if high != expected:
        raise AssertionError("unexpected 3r+1 high support")
    return high


def scaled_twin_n2_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    twin_blackout_target(rank)
    if rank % 2:
        raise ValueError("r must be even")
    middle = 3 * rank // 2
    if not is_twin_prime_deferral_center(middle):
        raise ValueError("3r/2 must be a twin center")
    segment = 3 * rank + 2
    if 2 * segment - 1 != 3 * (2 * rank + 1):
        raise AssertionError("6r+3 factorization changed")
    high = tuple((i, e) for i, e in composite_A_relation_exponents(segment) if i >= rank)
    expected = ((rank, -1), (rank + 1, 1), (3 * rank + 1, 1))
    if high != expected:
        raise AssertionError("unexpected 3r+2 high support")
    return high


def strict_transport_upper_gate(rank: int, prime: int) -> tuple[int, int]:
    _require_strict_transport(rank, prime)
    strict_transport_survival_requires_scaled_twin(rank, prime)
    if not _is_prime(6 * rank + 1):
        scaled_twin_n1_high_support(rank)
        return 3 * rank + 1, -1
    scaled_twin_n2_high_support(rank)
    return 3 * rank + 2, 1


def strict_transport_ceiling(rank: int, prime: int) -> int:
    _require_strict_transport(rank, prime)
    return 3 * rank + 2


def first_open_prime_threshold(rank: int) -> int:
    twin_blackout_target(rank)
    excluded = 4 * rank - 3
    if excluded % 3 or _is_prime(excluded):
        raise AssertionError("4r-3 must be composite")
    return 4 * rank - 1
