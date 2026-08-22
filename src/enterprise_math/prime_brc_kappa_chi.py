"""Prime-BRC kappa/chi directional-carry completion.

For a square basin split at M=k(k+1), P017's centered carry ``kappa`` records
how many boundary carry cells are present, while Prime-BRC's midpoint defect
``chi`` records their signed orientation.  On a true divisor of an
anchor-surviving mirror endpoint the pair is lossless:

    b_minus = (kappa+chi)/2,
    b_plus  = (kappa-chi)/2.

Thus chi-only collapse merges the no-carry state (0,0) with the double-carry
state (1,1); kappa repairs exactly that no-resurrection alias.
"""

from __future__ import annotations

from math import gcd

from .legendre import square_carry
from .prime_brc_phase import square_basin_frame, square_midpoint_defect
from .prime_brc_silent_core import silent_core_classification


def carry_state(k: int, divisor: int) -> dict[str, int]:
    """Return the complete two-half boundary-carry state (kappa,chi)."""
    if k < 2 or divisor < 2:
        raise ValueError("require k>=2 and divisor>=2")
    kappa = square_carry(k, divisor)
    chi = square_midpoint_defect(k, divisor)
    if kappa not in (0, 1, 2) or chi not in (-1, 0, 1):
        raise AssertionError("square carry state escaped its finite alphabet")
    if (kappa + chi) % 2 or (kappa - chi) % 2:
        raise AssertionError("kappa/chi parity mismatch")
    b_minus = (kappa + chi) // 2
    b_plus = (kappa - chi) // 2
    if b_minus not in (0, 1) or b_plus not in (0, 1):
        raise AssertionError("directional carry recovery escaped bit values")
    if kappa != b_minus + b_plus or chi != b_minus - b_plus:
        raise AssertionError("sum/detail transform failed")
    return {
        "k": k,
        "divisor": divisor,
        "kappa": kappa,
        "chi": chi,
        "lower_carry_bit": b_minus,
        "upper_carry_bit": b_plus,
    }


def strict_directional_hit_counts(k: int, divisor: int) -> dict[str, int]:
    """Return strict lower/upper basin hit counts and their kappa/chi split.

    This interface requires ``divisor`` to be coprime to M.  Then it cannot
    divide either square endpoint, so the strict hit counts are exactly

      H_- = floor(M/d)-floor(L/d),
      H_+ = floor(U/d)-floor(M/d).

    The bulk count in each half is floor(k/d), with the two carry bits as the
    0/1 corrections.
    """
    frame = square_basin_frame(k)
    if gcd(divisor, frame["center"]) != 1:
        raise ValueError("directional strict-count interface requires d coprime to M")
    lower_hits = frame["center"] // divisor - frame["lower"] // divisor
    upper_hits = frame["upper"] // divisor - frame["center"] // divisor
    state = carry_state(k, divisor)
    bulk = k // divisor
    if lower_hits != bulk + state["lower_carry_bit"]:
        raise AssertionError("lower hit count disagrees with kappa/chi carry split")
    if upper_hits != bulk + state["upper_carry_bit"]:
        raise AssertionError("upper hit count disagrees with kappa/chi carry split")
    if lower_hits - upper_hits != state["chi"]:
        raise AssertionError("chi lost directional hit imbalance")
    return {
        **state,
        "bulk_per_half": bulk,
        "lower_hits": lower_hits,
        "upper_hits": upper_hits,
    }


def silent_binary_carry_repair(k: int, radius: int, side: int) -> dict[str, object]:
    """Show that a polarity-silent semiprime is visible to the old d<->2d carry.

    If n=p*q is silent with q>k, then chi_q=0 and q has exactly one hit in
    each half, so kappa_q=2.  The paired q-multipliers are p and p+-1; exactly
    one is even.  Therefore exactly one hit is a 2q-hit and kappa_2q=1.

        kappa_q-kappa_2q = 1.

    This proves that the chi-only ambiguity is repaired by retaining P017's
    carry amount; no third observable is needed merely to recover this core.
    """
    data = silent_core_classification(k, radius, side)
    q = int(data["cofactor_prime"])
    frame = square_basin_frame(k)
    if q <= k or gcd(q, frame["center"]) != 1:
        raise AssertionError("silent cofactor failed large transverse range")
    q_state = carry_state(k, q)
    two_q_state = carry_state(k, 2 * q)
    if q_state["chi"] != 0 or q_state["kappa"] != 2:
        raise AssertionError("silent q did not realize the double-carry state")
    if two_q_state["kappa"] != 1:
        raise AssertionError("silent q shadow did not leave exactly one 2q hit")
    if q_state["kappa"] - two_q_state["kappa"] != 1:
        raise AssertionError("binary carry repair delta is not one")
    return {
        **data,
        "q_carry": q_state,
        "two_q_carry": two_q_state,
        "binary_carry_delta": 1,
        "repair_status": "CHI_ONLY_ALIAS_REPAIRED_BY_KAPPA_AMOUNT",
    }
