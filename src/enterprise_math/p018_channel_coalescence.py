"""P018 cubic quotient-channel coalescence interfaces.

This module isolates the reusable cross-divisor cubic structure from the older
exact-divisor/cofactor-window discovery route.  No exact cofactor-window formula
is needed here.

Two source-basin conventions are intentionally separated:

* candidate channels use the lower square boundary ``k^2`` through
  ``j_d = R_2(floor(k^2/d))`` and the canonical two-point channel
  ``C_d={j_d,j_d+1}``;
* actual-state coalescence accepts the complete half-open square basin
  ``k^2 <= n < (k+1)^2`` and studies the actual value
  ``R_2(floor(n/d))``.

Candidate-channel horizon
-------------------------
For nonadjacent labels ``d<e`` whose candidate channels overlap, writing
``u=j_e`` gives

    e*u^2 <= k^2 < d*(u+2)^2,

hence ``u^3 < 2k^2``.  Every common candidate therefore lies at or below

    H_c(k) = R_3(2k^2-1)+1.

Above ``H_c(k)`` candidate multiplicity is at most two, and a double hit must
come from adjacent labels.  Consequently odd divisor labels are injective above
``H_c(k)``.

Actual coalescence horizon
--------------------------
If two distinct divisors give the same actual quotient root ``t`` on one state
``n`` in the complete square basin, exact root intervals imply

    t^3 < 2(k+1)^2.

Thus actual collisions lie at or below

    H_a(k) = R_3(2(k+1)^2-1).

For ``k>=4``, ``H_a(k)<k``.  Together with quotient-path flattening, this gives
a well-founded collision skeleton and makes roots above ``H_a`` injective in
the nontrivial total divisor.

All arithmetic is integer-only.  Historical quartic candidate bounds and exact
cofactor-window separation remain provenance in their own discovery route; they
are not dependencies of this cubic interface.
"""

from __future__ import annotations

from math import isqrt

from .core import integer_nth_root


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def candidate_coalescence_horizon(k: int) -> int:
    """Return H_c(k)=R_3(2k^2-1)+1."""
    _require_int("k", k)
    if k < 1:
        raise ValueError("k must be positive")
    return integer_nth_root(2 * k * k - 1, 3) + 1


def actual_coalescence_horizon(k: int) -> int:
    """Return H_a(k)=R_3(2(k+1)^2-1)."""
    _require_int("k", k)
    if k < 1:
        raise ValueError("k must be positive")
    return integer_nth_root(2 * (k + 1) ** 2 - 1, 3)


def divisor_root_channel(k: int, divisor: int) -> dict[str, object]:
    """Return the canonical base root and two-point candidate channel."""
    _require_int("k", k)
    _require_int("divisor", divisor)
    if k < 1:
        raise ValueError("k must be positive")
    if divisor < 2:
        raise ValueError("divisor must be at least 2")
    base = isqrt((k * k) // divisor)
    return {
        "k": k,
        "divisor": divisor,
        "base_root": base,
        "candidates": (base, base + 1),
    }


def actual_divisor_root(k: int, n: int, divisor: int) -> int:
    """Return R_2(floor(n/divisor)) on k^2<=n<(k+1)^2."""
    for name, value in (("k", k), ("n", n), ("divisor", divisor)):
        _require_int(name, value)
    if k < 1:
        raise ValueError("k must be positive")
    if not k * k <= n < (k + 1) * (k + 1):
        raise ValueError("n must lie in the complete k-th square basin")
    if divisor < 2:
        raise ValueError("divisor must be at least 2")
    return isqrt(n // divisor)


def nonadjacent_candidate_overlap_cubic_contraction(
    k: int, left: int, right: int
) -> dict[str, object]:
    """Classify a nonadjacent overlapping candidate pair cubically."""
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
    if k * k >= left * (u + 2) * (u + 2):
        raise AssertionError("overlap failed to transport the upper square bound")
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
    """Above H_c(k), at most two channels hit and doubles are adjacent."""
    _require_int("k", k)
    _require_int("target_root", target_root)
    if k < 2:
        raise ValueError("k must be at least 2")
    if target_root < 0:
        raise ValueError("target_root must be nonnegative")

    horizon = candidate_coalescence_horizon(k)
    if target_root <= horizon:
        raise ValueError("target_root must lie above the cubic candidate horizon")

    hits = [
        divisor
        for divisor in range(2, k + 1)
        if target_root in divisor_root_channel(k, divisor)["candidates"]
    ]
    for i, left in enumerate(hits):
        for right in hits[i + 1 :]:
            if right >= left + 2:
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


def actual_divisor_root_collision(
    k: int, n: int, left: int, right: int
) -> dict[str, object]:
    """Classify an actual cross-divisor quotient-root collision."""
    _require_int("left", left)
    _require_int("right", right)
    if not 2 <= left < right:
        raise ValueError("require 2 <= left < right")

    left_root = actual_divisor_root(k, n, left)
    right_root = actual_divisor_root(k, n, right)
    coalesces = left_root == right_root
    horizon = actual_coalescence_horizon(k)
    result: dict[str, object] = {
        "k": k,
        "n": n,
        "left": left,
        "right": right,
        "left_root": left_root,
        "right_root": right_root,
        "coalesces": coalesces,
        "actual_coalescence_horizon": horizon,
    }
    if not coalesces:
        return result

    t = left_root
    if right * t * t > n:
        raise AssertionError("common root lower interval failed")
    if n >= left * (t + 1) * (t + 1):
        raise AssertionError("common root upper interval failed")
    if (right - left) * t * t >= left * (2 * t + 1):
        raise AssertionError("collision spacing inequality failed")
    if t > 2 * left:
        raise AssertionError("actual collision root exceeded 2d")
    if t**3 >= 2 * (k + 1) ** 2:
        raise AssertionError("actual collision escaped the cubic basin bound")
    if t > horizon:
        raise AssertionError("actual collision exceeded H_a(k)")

    return {
        **result,
        "common_root": t,
        "spacing_margin": left * (2 * t + 1) - (right - left) * t * t,
    }


def high_scale_actual_divisor_root_injectivity(
    k: int, n: int, divisors: tuple[int, ...]
) -> dict[str, object]:
    """Above H_a(k), actual roots uniquely identify distinct total divisors."""
    if len(set(divisors)) != len(divisors):
        raise ValueError("divisors must be distinct")
    if any(isinstance(d, bool) or not isinstance(d, int) or d < 2 for d in divisors):
        raise ValueError("all divisors must be integers >=2")

    horizon = actual_coalescence_horizon(k)
    owner: dict[int, int] = {}
    roots: dict[int, int] = {}
    for divisor in divisors:
        root = actual_divisor_root(k, n, divisor)
        roots[divisor] = root
        if root <= horizon:
            continue
        previous = owner.get(root)
        if previous is not None:
            collision = actual_divisor_root_collision(
                k, n, min(previous, divisor), max(previous, divisor)
            )
            if collision["coalesces"]:
                raise AssertionError("distinct divisors coalesced above H_a(k)")
        owner[root] = divisor

    return {
        "k": k,
        "n": n,
        "actual_coalescence_horizon": horizon,
        "roots_by_divisor": roots,
        "high_root_owner": owner,
    }


def candidate_horizon_strict_descent(k: int) -> dict[str, int]:
    """Verify H_c(k)<k for k>=5."""
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
    """Iterate H_a until the finite base range."""
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
