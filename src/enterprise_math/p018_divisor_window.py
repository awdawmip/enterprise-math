"""WIP P018 discovery: quotient-window and root-channel separation.

For a square basin k^2 <= n < (k+1)^2 and divisor d>=2, quotient/root transport
has much stronger cross-divisor structure than the canonical one-divisor T110
pair bound alone reveals.

This module records:

* exact quotient-window separation;
* nonadjacent small-product separation of T110 candidate root pairs;
* a candidate-channel overlap dichotomy and a quartic candidate horizon;
* a stronger **actual quotient coalescence** theorem: if two different divisors
  give the same actual quotient root t on one square-basin state, then

      t^3 < 2 (k+1)^2.

  Hence actual root coalescence is confined below the cubic horizon

      H_3(k) = R_3(2(k+1)^2 - 1) = O(k^(2/3)).

Combined with canonical T111 quotient-path flatness, roots above H_3(k) uniquely
identify the nontrivial total divisor, independent of how that divisor was
factorized along the path.

This is discovery-stage evidence, not a canonical theorem module.
"""

from __future__ import annotations

from math import isqrt

from .core import integer_nth_root


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def fourth_root(value: int) -> int:
    """Return floor(value^(1/4)) using exact integer square roots."""
    _require_int("value", value)
    if value < 0:
        raise ValueError("value must be nonnegative")
    return isqrt(isqrt(value))


def actual_coalescence_horizon(k: int) -> int:
    """Return H_3(k)=R_3(2(k+1)^2-1), the actual collision ceiling."""
    _require_int("k", k)
    if k < 1:
        raise ValueError("k must be positive")
    return integer_nth_root(2 * (k + 1) ** 2 - 1, 3)


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


def actual_divisor_root(k: int, n: int, divisor: int) -> int:
    """Return R_2(floor(n/divisor)) for a state in the k-th square basin."""
    _require_int("k", k)
    _require_int("n", n)
    _require_int("divisor", divisor)
    if k < 1:
        raise ValueError("k must be positive")
    if not k * k <= n < (k + 1) * (k + 1):
        raise ValueError("n must lie in the complete k-th square basin")
    if divisor < 2:
        raise ValueError("divisor must be at least 2")
    return isqrt(n // divisor)


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

    For d>=3, first show j_e>=2d+1. Since k>=de+1 and e>=d+2,

        (de+1)^2 >= e(2d+1)^2.

    The left-minus-right polynomial is increasing in e on e>=d+2 and at the
    minimum e=d+2 equals

        d^4 - 6d^2 - 5d - 1 > 0    (d>=3).

    With u=j_e and e-d>=2,

        e*u^2 - d(u+2)^2
        >= 2(u^2-2du-2d) > 0,

    so d(u+2)^2<k^2 and j_d>=u+2.

    The d=2 family follows from k>=9, j_e<=floor(k/2), and

        (floor(k/2)+2)^2 <= floor(k^2/2).
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
    elif j_right < 2 * d + 1:
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
    """If two candidate channels overlap, labels are adjacent or de>=k."""
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
    """A product-threshold candidate overlap lies below R_4(k^3)+1."""
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
    """Above R_4(k^3)+1, candidate multiplicity is <=2 and doubles are adjacent."""
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
        if target_root in divisor_root_channel(k, divisor)["candidates"]:
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


def actual_divisor_root_collision(
    k: int, n: int, left: int, right: int
) -> dict[str, object]:
    """Classify an actual cross-divisor quotient-root collision.

    Let 2<=d<e and assume both quotients have the same root t. Exact root
    intervals give

        e t^2 <= n < d(t+1)^2.

    Therefore

        (e-d)t^2 < d(2t+1).

    Since e-d>=1, t>=2d+1 would contradict this inequality, so t<=2d<2e.
    Multiplying the strict inequality t<2e by t^2 and using e t^2<=n gives

        t^3 < 2e t^2 <= 2n < 2(k+1)^2.

    Hence every actual collision satisfies

        t <= R_3(2(k+1)^2 - 1).

    No primality, parity, d<=k, or factorization assumption is needed.
    """
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
        raise AssertionError("actual collision exceeded H_3(k)")

    return {
        **result,
        "common_root": t,
        "spacing_margin": left * (2 * t + 1) - (right - left) * t * t,
    }


def high_scale_actual_divisor_root_injectivity(
    k: int, n: int, divisors: tuple[int, ...]
) -> dict[str, object]:
    """Above H_3(k), actual quotient roots uniquely identify total divisors.

    Canonical T111 says any repeated floor-division path equals division by its
    product divisor. Therefore this finite direct-divisor statement is also a
    path statement: two factorization paths with distinct nontrivial total
    divisors cannot coalesce at an actual root above H_3(k).
    """
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
        if root in owner:
            collision = actual_divisor_root_collision(
                k, n, min(owner[root], divisor), max(owner[root], divisor)
            )
            if collision["coalesces"]:
                raise AssertionError("distinct divisors coalesced above H_3(k)")
        owner[root] = divisor

    return {
        "k": k,
        "n": n,
        "actual_coalescence_horizon": horizon,
        "roots_by_divisor": roots,
        "high_root_owner": owner,
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
