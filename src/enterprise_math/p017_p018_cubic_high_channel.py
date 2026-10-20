"""P017/P018 bridge: residual hard-core small endpoints lie above the cubic channel horizon.

This module consumes, but does not re-own, the P018 candidate-channel theorem
validated on PR #195: for one square source basin, nonadjacent divisor channels
can overlap only at target roots at or below

    H_c(k) = R_3(2*k^2 - 1) + 1.

Distinct odd divisor labels are never adjacent, so above H_c(k) an odd divisor
channel is globally unique among all odd divisor labels.

The P017 residual hard core has a stronger consequence.  Let 3<=d<e be odd,
let d*e<k, and require the full cores to be transverse to M=k(k+1), as they are
for an anchor-surviving mirror pair.  Put

    j_d = R_2(floor(k^2/d)).

Then

    j_d >= H_c(k) + 1.

Thus the complete two-point candidate channel {j_d,j_d+1} of the *smaller*
full core lies strictly above the cubic coalescence horizon.  By the P018
mother theorem, this channel cannot overlap any channel carrying a different
odd full-core label.  Every residual hard-core mirror edge therefore contains
a globally unique high-scale routing channel for its smaller core cell.

Proof structure
---------------
The proof is integer-only.

For k>=64, write

    c = R_3(2*k^2-1),
    a = R_4(k^3).

Then c>=20.  From c>=20,

    10(c+2) <= 11c

and the fixed integer inequality 8*11^8 < 20*10^8 gives

    8(c+2)^8 < c^9.

Since c^3 < 2k^2, one also has c^9 < 8k^6.  Hence

    (c+2)^8 < k^6,

so (c+2)^4 < k^3 and therefore a>=c+2.

Now d^2<d*e<k, so d<=h=isqrt(k-1).  Because a^4<=k^3,

    (h*a^2)^2 <= (k-1)k^3 < k^4,

hence h*a^2<k^2 and therefore d*a^2<k^2.  Thus

    floor(k^2/d) >= a^2,

which gives j_d>=a>=c+2=H_c(k)+1.

The only remaining range is 16<=k<=63; k>=16 follows from the smallest odd
product 3*5<k.  Exhaustive exact integer reconstruction of every odd
3<=d<e with d*e<k leaves one and only one abstract failure:

    (k,d,e) = (17,3,5),  j_d=H_c(17)=9.

But 3 divides 17*18, so this row violates the mandatory full-core
transversality gcd(d*e,k(k+1))=1 and cannot occur in an anchor-surviving P017
hard-core mirror pair.

No P017 L-number or P018 theorem number is reserved here.
"""

from __future__ import annotations

from math import gcd, isqrt

from .core import integer_nth_root
from .p017_cofactor_window import square_basin_smooth_tail
from .p017_mirror import anchor_surviving_radius, mirror_center, mirror_pair
from .p017_p018_hard_core_bridge import base_root_index

SMALL_K_MAX = 63
ABSTRACT_SMALL_K_EXCEPTIONS = ((17, 3, 5, 9, 9),)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def cubic_candidate_horizon(k: int) -> int:
    """Return the P018 candidate-channel horizon R_3(2*k^2-1)+1."""
    _require_int("k", k)
    if k < 2:
        raise ValueError("k must be at least 2")
    return integer_nth_root(2 * k * k - 1, 3) + 1


def fourth_root(value: int) -> int:
    """Return the exact floor fourth root using nested integer square roots."""
    _require_int("value", value)
    if value < 0:
        raise ValueError("value must be nonnegative")
    return isqrt(isqrt(value))


def small_k_abstract_exception_frontier() -> tuple[tuple[int, int, int, int, int], ...]:
    """Reconstruct the complete 16<=k<=63 abstract failure frontier.

    Rows record (k,d,e,j_d,H_c) for odd 3<=d<e, d*e<k and j_d<=H_c.
    Full-core transversality is deliberately *not* imposed here so that the one
    exceptional arithmetic row remains visible and can then be killed by the
    P017 anchor condition rather than hidden by the enumeration.
    """
    rows: list[tuple[int, int, int, int, int]] = []
    for k in range(16, SMALL_K_MAX + 1):
        horizon = cubic_candidate_horizon(k)
        for d in range(3, k, 2):
            for e in range(d + 2, k + 1, 2):
                if d * e >= k:
                    break
                root = base_root_index(k, d)
                if root <= horizon:
                    rows.append((k, d, e, root, horizon))
    return tuple(rows)


def cubic_to_quartic_margin(k: int) -> dict[str, int]:
    """Certify R_4(k^3) >= R_3(2k^2-1)+2 for k>=64.

    This is only a bridge estimate.  It does not reintroduce the weaker P018
    quartic coalescence theorem: the canonical/WIP collision horizon consumed by
    this module remains the stronger cubic one.
    """
    _require_int("k", k)
    if k < 64:
        raise ValueError("large-scale cubic/quartic margin requires k>=64")

    c = integer_nth_root(2 * k * k - 1, 3)
    a = fourth_root(k**3)
    if c < 20:
        raise AssertionError("k>=64 should force cubic root at least 20")
    if 10 * (c + 2) > 11 * c:
        raise AssertionError("c>=20 failed the 10(c+2)<=11c comparison")
    if not 8 * 11**8 < 20 * 10**8:
        raise AssertionError("fixed eighth-power comparison was miscomputed")
    if not 8 * (c + 2) ** 8 < c**9:
        raise AssertionError("cubic-to-quartic bridge margin failed")
    if not c**9 < 8 * k**6:
        raise AssertionError("c^3<2k^2 failed after cubing")
    if not (c + 2) ** 4 < k**3:
        raise AssertionError("c+2 did not fit below the quartic root threshold")
    if a < c + 2:
        raise AssertionError("integer fourth root failed to dominate c+2")

    return {
        "k": k,
        "cubic_base": c,
        "cubic_horizon": c + 1,
        "quartic_root": a,
        "root_margin": a - (c + 1),
    }


def transverse_small_endpoint_cubic_channel(k: int, d: int, e: int) -> dict[str, object]:
    """Certify that the smaller hard-core full-core channel is cubic-high.

    Assumptions are exactly the abstract arithmetic inherited from a residual
    anchor-surviving full-core pair: distinct odd cores, product below k, and
    transversality to M=k(k+1).
    """
    for name, value in (("k", k), ("d", d), ("e", e)):
        _require_int(name, value)
    if not (3 <= d < e and d % 2 == 1 and e % 2 == 1 and d * e < k):
        raise ValueError("require odd 3<=d<e with d*e<k")

    center = k * (k + 1)
    if gcd(d * e, center) != 1:
        raise ValueError("full cores must be transverse to k(k+1)")

    horizon = cubic_candidate_horizon(k)
    root = base_root_index(k, d)

    # Smallest possible odd product is 3*5, so every valid row has k>=16.
    if k < 16:
        raise AssertionError("odd residual core-product assumptions should force k>=16")

    if k >= 64:
        margin = cubic_to_quartic_margin(k)
        a = int(margin["quartic_root"])
        h = isqrt(k - 1)
        if d > h:
            raise AssertionError("d^2<d*e<k failed to put d below isqrt(k-1)")
        if h * h > k - 1 or a**4 > k**3:
            raise AssertionError("integer root definitions were violated")
        if not (h * a * a) ** 2 < k**4:
            raise AssertionError("h*a^2 failed the strict square comparison")
        if not d * a * a < k * k:
            raise AssertionError("small endpoint did not fit below the quartic square scale")
        if (k * k) // d < a * a:
            raise AssertionError("quotient floor lost the quartic lower square")
        if root < a:
            raise AssertionError("base root fell below the quartic routing floor")
        if root < horizon + 1:
            raise AssertionError("small endpoint failed cubic-high routing")
    else:
        frontier = small_k_abstract_exception_frontier()
        if frontier != ABSTRACT_SMALL_K_EXCEPTIONS:
            raise AssertionError("small-k cubic exception frontier changed")
        if root <= horizon:
            row = (k, d, e, root, horizon)
            if row not in frontier:
                raise AssertionError("unclassified small-k cubic-high failure")
            # The unique row is (17,3,5), but 3|17*18.  The transversality
            # check above therefore makes this branch unreachable.
            raise AssertionError("transverse hard-core row reached the unique nontransverse exception")

    return {
        "k": k,
        "small_core": d,
        "other_core": e,
        "core_product": d * e,
        "center": center,
        "cubic_horizon": horizon,
        "base_root": root,
        "candidate_channel": (root, root + 1),
        "height_above_horizon": root - horizon,
    }


def hard_core_cubic_routing(k: int, radius: int) -> dict[str, object]:
    """Apply cubic-high routing to one actual residual P017 mirror pair."""
    for name, value in (("k", k), ("radius", radius)):
        _require_int(name, value)
    if k < 2 or not 1 <= radius < k:
        raise ValueError("require k>=2 and 1<=radius<k")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    lower, upper = mirror_pair(k, radius)
    lower_data = square_basin_smooth_tail(k, lower)
    upper_data = square_basin_smooth_tail(k, upper)
    if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
        raise ValueError("both mirror states must be composite")

    lower_core = int(lower_data["smooth_core"])
    upper_core = int(upper_data["smooth_core"])
    lower_tail = int(lower_data["tail"])
    upper_tail = int(upper_data["tail"])
    product = lower_core * upper_core
    if product >= k:
        raise ValueError("residual hard-core routing requires core product < k")
    if lower_core <= 1 or upper_core <= 1:
        raise AssertionError("hard-core composite state lost a nontrivial full core")
    if lower_tail <= k or upper_tail <= k:
        raise AssertionError("product<k should force two nontrivial large tails")

    small_core = min(lower_core, upper_core)
    other_core = max(lower_core, upper_core)
    route = transverse_small_endpoint_cubic_channel(k, small_core, other_core)

    if lower_core == small_core:
        small_state = lower
        small_tail = lower_tail
        small_side = -1
    else:
        small_state = upper
        small_tail = upper_tail
        small_side = 1

    actual_root = isqrt(small_tail)
    if actual_root not in route["candidate_channel"]:
        raise AssertionError("actual small-core tail left its two-root candidate channel")

    return {
        **route,
        "radius": radius,
        "lower_core": lower_core,
        "upper_core": upper_core,
        "lower_tail": lower_tail,
        "upper_tail": upper_tail,
        "small_core_side": small_side,
        "small_core_state": small_state,
        "small_core_tail": small_tail,
        "small_core_actual_root": actual_root,
    }
