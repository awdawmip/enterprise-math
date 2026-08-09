"""WIP P018 discovery: quotient-window and root-channel separation.

For a square basin k^2 < n < (k+1)^2 and divisor d>=2, the possible integer
quotients n//d lie in

    W_d(k) = [floor(k^2/d)+1, floor(k(k+2)/d)].

This module records elementary separation criteria for exact quotient windows
and stronger root-channel consequences.  Nonadjacent divisors d<e with de<k
have disjoint T110 candidate root pairs.  Therefore any overlap is either the
adjacent-divisor exception e=d+1 or occurs only after the divisor product has
reached k; the latter forces the descended root below a universal quartic
horizon R_4(k^3)+1.  It is discovery-stage evidence, not a canonical theorem
module.
"""

from __future__ import annotations

from math import isqrt


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def fourth_root(value: int) -> int:
    """Return floor(value^(1/4)) using nested exact integer square roots."""
    _require_int("value", value)
    if value < 0:
        raise ValueError("value must be nonnegative")
    return isqrt(isqrt(value))


def divisor_quotient_window(k: int, divisor: int) -> tuple[int, int]:
    """Return the exact quotient window for 2<=divisor<=k."""
    _require_int("k", k)
    _require_int("divisor", divisor)
    if k < 2:
        raise ValueError("k must be at least 2")
    if divisor < 2 or divisor > k:
        raise ValueError("require 2 <= divisor <= k")
    return (k * k) // divisor + 1, (k * (k + 2)) // divisor


def divisor_root_channel(k: int, divisor: int) -> dict[str, object]:
    """Return the T110 base root and its two-point candidate channel."""
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


def divisor_window_separation(k: int, left: int, right: int) -> dict[str, object]:
    """Check the sufficient criterion 2*left <= k*(right-left).

    If 2d <= k(e-d), then d(k+2)<=ek and therefore

        floor(k(k+2)/e) <= floor(k^2/d),

    so W_e(k) lies strictly below W_d(k).
    """
    _require_int("k", k)
    _require_int("left", left)
    _require_int("right", right)
    if not (2 <= left < right <= k):
        raise ValueError("require 2 <= left < right <= k")
    margin = k * (right - left) - 2 * left
    if margin < 0:
        raise ValueError("the sufficient separation criterion is not satisfied")
    left_window = divisor_quotient_window(k, left)
    right_window = divisor_quotient_window(k, right)
    if right_window[1] >= left_window[0]:
        raise AssertionError("criterion held but quotient windows were not separated")
    return {
        "k": k,
        "left": left,
        "right": right,
        "criterion_margin": margin,
        "left_window": left_window,
        "right_window": right_window,
        "integer_gap": left_window[0] - right_window[1] - 1,
    }


def same_parity_divisor_windows(k: int) -> dict[str, object]:
    """Executable corollary: same-parity divisor windows are disjoint."""
    _require_int("k", k)
    if k < 3:
        raise ValueError("k must be at least 3")
    divisors = list(range(2, k + 1))
    checked: list[tuple[int, int]] = []
    for i, left in enumerate(divisors):
        for right in divisors[i + 1 :]:
            if (right - left) % 2:
                continue
            divisor_window_separation(k, left, right)
            checked.append((left, right))
    return {"k": k, "checked_pairs": tuple(checked), "pair_count": len(checked)}


def nonadjacent_small_product_root_pair_separation(
    k: int, left: int, right: int
) -> dict[str, object]:
    """WIP candidate: e>=d+2 and de<k force disjoint T110 root pairs.

    Put

        j_d = R_2(floor(k^2/d)),
        j_e = R_2(floor(k^2/e)).

    For integers 2<=d<e with e>=d+2 and d*e<k, one has

        j_d >= j_e + 2.

    Hence {j_d,j_d+1} and {j_e,j_e+1} are disjoint.

    For d>=3, first show j_e>=2d+1.  Since k>=de+1 and e>=d+2,

        (de+1)^2 >= e(2d+1)^2.

    The left-minus-right polynomial is increasing in e on e>=d+2 and at the
    minimum e=d+2 equals

        d^4 - 6d^2 - 5d - 1 > 0    (d>=3).

    With u=j_e and e-d>=2,

        e*u^2 - d(u+2)^2
        >= 2(u^2-2du-2d) > 0,

    so d(u+2)^2<k^2 and j_d>=u+2.

    The only missing base family is d=2.  Then e>=4 and de<k imply k>=9.
    Since j_e<=floor(k/2), the elementary parity split k=2m or 2m+1 gives

        (floor(k/2)+2)^2 <= floor(k^2/2)    for k>=9,

    hence j_2>=j_e+2 as well.
    """
    _require_int("k", k)
    _require_int("left", left)
    _require_int("right", right)
    d = left
    e = right
    if not (2 <= d < e <= k):
        raise ValueError("require 2 <= left < right <= k")
    if e < d + 2:
        raise ValueError("require nonadjacent divisors: right >= left + 2")
    if d * e >= k:
        raise ValueError("require left*right < k")

    j_left = isqrt((k * k) // d)
    j_right = isqrt((k * k) // e)

    if d == 2:
        half = k // 2
        if k < 9:
            raise AssertionError("d=2 small-product assumptions should force k>=9")
        if j_right > half:
            raise AssertionError("d=2 upper-divisor root exceeded floor(k/2)")
        if (half + 2) ** 2 > (k * k) // 2:
            raise AssertionError("d=2 base square inequality failed")
    else:
        if j_right < 2 * d + 1:
            raise AssertionError("small-product lower-root estimate failed")

    if j_left < j_right + 2:
        raise AssertionError("small-product root candidate pairs overlap")

    return {
        "k": k,
        "left": d,
        "right": e,
        "left_root": j_left,
        "right_root": j_right,
        "root_gap": j_left - j_right,
        "left_candidates": (j_left, j_left + 1),
        "right_candidates": (j_right, j_right + 1),
    }


def divisor_channel_overlap_dichotomy(k: int, left: int, right: int) -> dict[str, object]:
    """Classify overlap of two divisor root channels.

    For 2<=d<e<=k, if C_d(k) and C_e(k) overlap, then either

        e=d+1

    or

        d*e>=k.

    This is the contrapositive interface of the nonadjacent small-product
    separation theorem.
    """
    _require_int("k", k)
    _require_int("left", left)
    _require_int("right", right)
    if not (2 <= left < right <= k):
        raise ValueError("require 2 <= left < right <= k")

    left_data = divisor_root_channel(k, left)
    right_data = divisor_root_channel(k, right)
    common = tuple(sorted(set(left_data["candidates"]) & set(right_data["candidates"])))
    overlap = bool(common)
    adjacent = right == left + 1
    product_threshold = left * right >= k

    if overlap and not adjacent and not product_threshold:
        # The branch assumptions now satisfy the proved separation theorem.
        nonadjacent_small_product_root_pair_separation(k, left, right)
        raise AssertionError("overlapping nonadjacent small-product channels survived")

    return {
        "k": k,
        "left": left,
        "right": right,
        "left_channel": left_data["candidates"],
        "right_channel": right_data["candidates"],
        "common_roots": common,
        "overlap": overlap,
        "adjacent_exception": adjacent,
        "product_threshold": product_threshold,
    }


def product_threshold_overlap_quartic_contraction(
    k: int, left: int, right: int
) -> dict[str, object]:
    """A non-small-product overlap forces the larger channel below R_4(k^3)+1.

    Assume C_d(k) and C_e(k) overlap for 2<=d<e<=k and k<=de.  Since d<e,
    k<=de<=e^2.  If j_e=R_2(floor(k^2/e)), then

        e*j_e^2 <= k^2.

    Squaring and using k<=e^2 gives

        k*j_e^4 <= e^2*j_e^4 <= k^4,

    hence j_e^4<=k^3 and j_e<=R_4(k^3).  Every common candidate root is at
    most j_e+1, so it is at most R_4(k^3)+1.
    """
    data = divisor_channel_overlap_dichotomy(k, left, right)
    if not data["overlap"]:
        raise ValueError("the two divisor channels do not overlap")
    if not data["product_threshold"]:
        raise ValueError("quartic contraction requires left*right >= k")

    j_right = isqrt((k * k) // right)
    if right * j_right * j_right > k * k:
        raise AssertionError("base root left its quotient square bound")
    if k > right * right:
        raise AssertionError("product threshold did not force k<=right^2")
    if j_right**4 > k**3:
        raise AssertionError("overlap channel missed quartic contraction")

    root4 = fourth_root(k**3)
    if j_right > root4:
        raise AssertionError("base root exceeded R_4(k^3)")
    for target in data["common_roots"]:
        if target > root4 + 1:
            raise AssertionError("common target exceeded quartic coalescence horizon")

    return {
        **data,
        "larger_base_root": j_right,
        "quartic_base_ceiling": root4,
        "coalescence_horizon": root4 + 1,
    }


def high_scale_divisor_channel_multiplicity(k: int, target_root: int) -> dict[str, object]:
    """Above R_4(k^3)+1, at most two divisor channels hit one target root.

    Moreover, if two channels hit, their divisor labels are consecutive.  If
    three distinct labels hit the same high target, the smallest and largest are
    nonadjacent; their overlap would force the quartic contraction and contradict
    the high-target assumption.
    """
    _require_int("k", k)
    _require_int("target_root", target_root)
    if k < 2:
        raise ValueError("k must be at least 2")
    if target_root < 0:
        raise ValueError("target_root must be nonnegative")

    horizon = fourth_root(k**3) + 1
    if target_root <= horizon:
        raise ValueError("target_root must lie above the quartic coalescence horizon")

    hits: list[int] = []
    for divisor in range(2, k + 1):
        channel = divisor_root_channel(k, divisor)["candidates"]
        if target_root in channel:
            hits.append(divisor)

    if len(hits) > 2:
        raise AssertionError("high-scale target has more than two divisor channels")
    if len(hits) == 2 and hits[1] != hits[0] + 1:
        raise AssertionError("high-scale double channel is not an adjacent pair")

    return {
        "k": k,
        "target_root": target_root,
        "coalescence_horizon": horizon,
        "divisor_hits": tuple(hits),
        "multiplicity": len(hits),
        "adjacent_double": len(hits) == 2,
    }


def odd_small_product_root_pair_separation(
    k: int, left: int, right: int
) -> dict[str, object]:
    """Backward-compatible P017 corollary for distinct odd full cores."""
    _require_int("left", left)
    _require_int("right", right)
    if left < 3 or left % 2 == 0 or right % 2 == 0:
        raise ValueError("both divisors must be odd and left must be at least 3")
    return nonadjacent_small_product_root_pair_separation(k, left, right)
