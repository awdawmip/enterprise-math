"""Discovery-stage P018 cubic coalescence interfaces.

This module isolates the stronger cross-divisor consequences discovered after the
initial quotient-window work.  It deliberately keeps the weaker quartic
candidate bound in the earlier discovery module as provenance while exposing
the cubic bounds that should control any later canonical replay.

Two horizons are distinguished.

Candidate-channel horizon
-------------------------
For ``j_d = R_2(floor(k^2/d))`` and ``C_d={j_d,j_d+1}``, if ``d<e`` are
nonadjacent (``e>=d+2``) and ``C_d`` and ``C_e`` overlap, put ``u=j_e``.  Then
``j_d<=u+1``.  Integer-root bounds give

    e*u^2 <= k^2 < d*(u+2)^2.

Hence

    (e-d)u^2 < 4d(u+1).

Since ``e-d>=2``, this forces ``u<=2d+1<2e`` and therefore

    u^3 < 2e*u^2 <= 2k^2.

Every common candidate is at most ``u+1``, so it lies below

    H_c(k) = R_3(2k^2-1)+1.

Thus above ``H_c(k)`` every target receives at most two divisor channels, and a
double channel must come from adjacent divisor labels.  Restricting to odd
labels removes even that exception: odd divisor channels are injective above the
cubic candidate horizon.

Actual coalescence horizon
--------------------------
The companion discovery in ``p018_divisor_window`` is stronger for one actual
state ``n``: distinct divisors with equal actual quotient root ``t`` satisfy
``t^3 < 2(k+1)^2``.  Its exact horizon is
``H_a(k)=R_3(2(k+1)^2-1)``.  Both horizon maps are strictly reductive beyond
finite base cases, yielding a well-founded collision skeleton.

These are research-stage interfaces, not canonical theorem numbers.
"""

from __future__ import annotations

from .core import integer_nth_root
from .p018_divisor_window import (
    actual_coalescence_horizon,
    divisor_root_channel,
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def candidate_coalescence_horizon(k: int) -> int:
    """Return H_c(k)=R_3(2k^2-1)+1."""
    _require_int("k", k)
    if k < 1:
        raise ValueError("k must be positive")
    return integer_nth_root(2 * k * k - 1, 3) + 1


def nonadjacent_candidate_overlap_cubic_contraction(
    k: int, left: int, right: int
) -> dict[str, object]:
    """Classify a nonadjacent overlapping T110 candidate pair cubically.

    Assumptions: ``2<=left<right<=k``, ``right>=left+2``, and the two candidate
    root pairs overlap.  Conclusion: if ``u`` is the larger-divisor base root,
    then ``u^3<2k^2`` and every common target is at most ``H_c(k)``.
    """
    for name, value in (("k", k), ("left", left), ("right", right)):
        _require_int(name, value)
    if not (2 <= left < right <= k):
        raise ValueError("require 2 <= left < right <= k")
    if right < left + 2:
        raise ValueError("require nonadjacent divisors: right >= left + 2")

    left_data = divisor_root_channel(k, left)
    right_data = divisor_root_channel(k, right)
    j_left = int(left_data["base_root"])
    j_right = int(right_data["base_root"])
    common = tuple(
        sorted(set(left_data["candidates"]).intersection(right_data["candidates"]))
    )
    if not common:
        raise ValueError("the nonadjacent candidate channels do not overlap")
    if j_right > j_left:
        raise AssertionError("larger divisor unexpectedly increased the base root")
    if j_left > j_right + 1:
        raise AssertionError("overlap did not force adjacent base-root indices")

    u = j_right
    if right * u * u > k * k:
        raise AssertionError("larger-divisor base root left its lower square bound")
    if k * k >= left * (j_left + 1) * (j_left + 1):
        raise AssertionError("smaller-divisor base root left its upper square bound")
    if k * k >= left * (u + 2) * (u + 2):
        raise AssertionError("overlap failed to transport the upper square bound")

    # Subtract d*u^2 from e*u^2 < d*(u+2)^2.
    if (right - left) * u * u >= 4 * left * (u + 1):
        raise AssertionError("nonadjacent candidate spacing inequality failed")
    if u > 2 * left + 1:
        raise AssertionError("larger-divisor base root exceeded 2d+1")
    if u >= 2 * right:
        raise AssertionError("larger-divisor base root failed u<2e")
    if u**3 >= 2 * k * k:
        raise AssertionError("nonadjacent candidate overlap escaped the cubic bound")

    horizon = candidate_coalescence_horizon(k)
    for target in common:
        if target > horizon:
            raise AssertionError("common candidate escaped H_c(k)")

    return {
        "k": k,
        "left": left,
        "right": right,
        "left_base_root": j_left,
        "right_base_root": j_right,
        "common_roots": common,
        "candidate_coalescence_horizon": horizon,
        "right_base_cubic": u**3,
        "cubic_ceiling_argument": 2 * k * k - 1,
    }


def high_scale_candidate_channel_multiplicity(
    k: int, target_root: int
) -> dict[str, object]:
    """Above H_c(k), at most two channels hit, and doubles are adjacent.

    Any three distinct labels contain a nonadjacent pair, contradicting the
    cubic contraction.  The same argument shows that among odd divisor labels
    the multiplicity is at most one above H_c(k).
    """
    _require_int("k", k)
    _require_int("target_root", target_root)
    if k < 2:
        raise ValueError("k must be at least 2")
    if target_root < 0:
        raise ValueError("target_root must be nonnegative")

    horizon = candidate_coalescence_horizon(k)
    if target_root <= horizon:
        raise ValueError("target_root must lie above the cubic candidate horizon")

    hits: list[int] = []
    for divisor in range(2, k + 1):
        if target_root in divisor_root_channel(k, divisor)["candidates"]:
            hits.append(divisor)

    for i, left in enumerate(hits):
        for right in hits[i + 1 :]:
            if right >= left + 2:
                # This call must prove the pair lies below the horizon, so a
                # high-scale hit would be a contradiction.
                data = nonadjacent_candidate_overlap_cubic_contraction(
                    k, left, right
                )
                if target_root in data["common_roots"]:
                    raise AssertionError(
                        "nonadjacent divisor channels coalesced above H_c(k)"
                    )

    if len(hits) > 2:
        raise AssertionError("high-scale target has more than two divisor channels")
    if len(hits) == 2 and hits[1] != hits[0] + 1:
        raise AssertionError("high-scale double channel is not adjacent")
    odd_hits = tuple(divisor for divisor in hits if divisor % 2 == 1)
    if len(odd_hits) > 1:
        raise AssertionError("odd divisor channels are not high-scale injective")

    return {
        "k": k,
        "target_root": target_root,
        "candidate_coalescence_horizon": horizon,
        "divisor_hits": tuple(hits),
        "odd_divisor_hits": odd_hits,
        "multiplicity": len(hits),
        "odd_multiplicity": len(odd_hits),
    }


def candidate_horizon_strict_descent(k: int) -> dict[str, int]:
    """Verify H_c(k)<k for the nontrivial range k>=5."""
    _require_int("k", k)
    if k < 5:
        raise ValueError("candidate cubic descent starts at k>=5")
    horizon = candidate_coalescence_horizon(k)
    if horizon >= k:
        raise AssertionError("candidate cubic horizon failed strict descent")
    return {"k": k, "horizon": horizon, "drop": k - horizon}


def actual_horizon_strict_descent(k: int) -> dict[str, int]:
    """Verify H_a(k)<k for k>=4, matching the Lean theorem."""
    _require_int("k", k)
    if k < 4:
        raise ValueError("actual cubic descent starts at k>=4")
    horizon = actual_coalescence_horizon(k)
    if horizon >= k:
        raise AssertionError("actual cubic horizon failed strict descent")
    return {"k": k, "horizon": horizon, "drop": k - horizon}


def actual_collision_horizon_chain(k: int) -> tuple[int, ...]:
    """Iterate the exact actual-collision horizon until the finite base range.

    Every step is strict while the current scale is at least four.  This is an
    executable representation of the well-founded collision skeleton; it does
    not assert that a collision occurs at every step.
    """
    _require_int("k", k)
    if k < 1:
        raise ValueError("k must be positive")
    chain = [k]
    current = k
    while current >= 4:
        next_scale = actual_coalescence_horizon(current)
        if next_scale >= current:
            raise AssertionError("collision horizon chain stopped descending")
        chain.append(next_scale)
        current = next_scale
    return tuple(chain)
