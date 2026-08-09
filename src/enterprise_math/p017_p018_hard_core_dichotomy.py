"""Sharper P017/P018 bridge dichotomy for close base-root channels.

This module sharpens the first hard-core bridge theorem. Under the same odd
small-product mirror hypotheses with two prime tails, either the P018 base-root
indices differ by at least four, or there is one unique sharp finite exception:

    k=64, d=7, e=9, r=47, orientation=+1,
    (q_d,q_e)=(601,457), (j_d,j_e)=(24,21).

A useful analytic refinement is that any hypothetical base gap at most three
forces ``e=d+2``. If ``e-d>=4``, the bridge inequality gives ``u=j_e<=2d+1``.
Combining ``de<k`` with ``k^2<e(u+1)^2`` yields
``d^2 e < (2d+2)^2``. For odd d>=5 this contradicts e>=d+4. The only remaining
possibility d=3,e=7 would require k>=22 while k^2<7*8^2=448, also impossible.

The remaining consecutive-odd finite frontier is reconstructed exactly from
the analytically complete 58 triples in ``p017_p018_hard_core_bridge``.
"""

from __future__ import annotations

from math import isqrt

from .legendre import is_prime
from .p017_p018_hard_core_bridge import (
    base_root_index,
    finite_base_gap_reduction,
    finite_base_risk_triples,
)

UNIQUE_SMALL_BASE_GAP_PRIME_ROW = (
    64,
    7,
    9,
    47,
    1,
    601,
    457,
    24,
    21,
)


def adjacent_core_reduction(k: int, d: int, e: int) -> dict[str, int]:
    """Under base-root gap <=3, certify that the odd cores are consecutive."""
    data = finite_base_gap_reduction(k, d, e)
    u = data["j_e"]
    if e - d >= 4:
        # (e-d)u^2 < 8du+16d and e-d>=4 imply u<=2d+1.
        if u >= 2 * d + 2:
            if 4 * u * u <= 8 * d * u + 16 * d:
                raise AssertionError("strong quadratic cutoff arithmetic failed")
            raise AssertionError("base-gap hypothesis contradicts e-d>=4")
        if not (d * d * e < (2 * d + 2) ** 2):
            raise AssertionError("strong finite-reduction inequality failed")
        if d >= 5:
            raise AssertionError("odd d>=5 cannot support e-d>=4")
        if (d, e) != (3, 7):
            raise AssertionError("only (3,7) survives the first strong cutoff")
        if k < 22 or not (k * k < 7 * 8 * 8):
            raise AssertionError("(3,7) contradicts de<k and the root upper bound")
        raise AssertionError("non-adjacent odd cores survived unexpectedly")

    if e != d + 2:
        raise AssertionError("odd distinct cores should differ by at least two")
    return {
        **data,
        "core_gap": e - d,
    }


def enumerate_small_base_gap_mirror_rows() -> tuple[tuple[int, ...], ...]:
    """Enumerate every exact mirror row in the complete base-gap<=3 frontier."""
    rows: list[tuple[int, ...]] = []
    for k, d, e, j_d, j_e in finite_base_risk_triples():
        adjacent_core_reduction(k, d, e)
        center = k * (k + 1)
        for orientation in (-1, 1):
            for radius in range(1, k):
                d_num = center + orientation * radius
                e_num = center - orientation * radius
                if d_num % d or e_num % e:
                    continue
                q_d = d_num // d
                q_e = e_num // e
                if q_d <= k or q_e <= k:
                    continue
                rows.append(
                    (
                        k,
                        d,
                        e,
                        radius,
                        orientation,
                        q_d,
                        q_e,
                        j_d,
                        j_e,
                    )
                )
    return tuple(rows)


def enumerate_small_base_gap_prime_rows() -> tuple[tuple[int, ...], ...]:
    """Return the prime-tail rows inside the complete close-base frontier."""
    return tuple(
        row
        for row in enumerate_small_base_gap_mirror_rows()
        if is_prime(row[5]) and is_prime(row[6])
    )


def prime_tail_base_gap_dichotomy(
    k: int,
    d: int,
    e: int,
    radius: int,
    orientation: int,
) -> dict[str, int | bool]:
    """Certify base-root gap >=4 except for the unique k=64 sharp row."""
    if orientation not in (-1, 1):
        raise ValueError("orientation must be -1 or +1")
    if not (3 <= d < e and d % 2 == 1 and e % 2 == 1 and d * e < k):
        raise ValueError("require odd 3<=d<e with d*e<k")
    if not 1 <= radius < k:
        raise ValueError("require 1<=radius<k")

    center = k * (k + 1)
    d_num = center + orientation * radius
    e_num = center - orientation * radius
    if d_num % d or e_num % e:
        raise ValueError("mirror states must divide exactly by their declared cores")
    q_d = d_num // d
    q_e = e_num // e
    if q_d <= k or q_e <= k or not is_prime(q_d) or not is_prime(q_e):
        raise ValueError("both exact residual tails must be prime and exceed k")

    j_d = base_root_index(k, d)
    j_e = base_root_index(k, e)
    base_gap = j_d - j_e
    exceptional = False
    if base_gap <= 3:
        adjacent_core_reduction(k, d, e)
        row = (k, d, e, radius, orientation, q_d, q_e, j_d, j_e)
        if row != UNIQUE_SMALL_BASE_GAP_PRIME_ROW:
            raise AssertionError("prime row escaped the unique close-base certificate")
        exceptional = True
        if base_gap != 3:
            raise AssertionError("unique close-base prime row must have gap three")
    elif base_gap < 4:
        raise AssertionError("base gap classification is inconsistent")

    return {
        "k": k,
        "d": d,
        "e": e,
        "radius": radius,
        "orientation": orientation,
        "q_d": q_d,
        "q_e": q_e,
        "j_d": j_d,
        "j_e": j_e,
        "base_root_gap": base_gap,
        "exceptional": exceptional,
        "root_d": isqrt(q_d),
        "root_e": isqrt(q_e),
    }
