"""Quadratic mirror-product lift from one P017 square basin into another.

For M=k(k+1), a mirror pair M-r,M+r has product

    Lambda_k(r)=M^2-r^2.

For 1<=r<k this product lies strictly in the square basin between (M-1)^2
and M^2.  The target collapse gap therefore encodes r^2 exactly.  At factor
cutoff k, the smooth core/tail coordinates multiply across the two original
mirror states.  This packages one mirror pair into one higher-basin state and
sharpens the total-full-core square-distance divisibility by an automatic
mod-8 factor.
"""

from __future__ import annotations

from math import gcd

from .core import collapse, integer_nth_root
from .legendre import primes_up_to
from .p017_cofactor_window import square_basin_smooth_tail
from .p017_core_cell_lattice import exact_full_core_pair


def _require_k_radius(k: int, radius: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")


def mirror_product_lift(k: int, radius: int) -> dict[str, int]:
    """QL01-QL02: embed one mirror product into the square basin rooted at M-1."""
    _require_k_radius(k, radius)
    center = k * (k + 1)
    target_root = center - 1
    lower = center - radius
    upper = center + radius
    lifted = lower * upper
    if lifted != center * center - radius * radius:
        raise AssertionError("difference-of-squares lift identity failed")
    if not (target_root * target_root < lifted < center * center):
        raise AssertionError("mirror product left the target consecutive-square basin")
    if integer_nth_root(lifted, 2) != target_root:
        raise AssertionError("quadratic lift has the wrong target integer root")

    collapsed = collapse(lifted, 2)
    gap = lifted - collapsed
    expected_gap = 2 * center - 1 - radius * radius
    if gap != expected_gap:
        raise AssertionError("target collapse gap failed to encode radius square")
    if radius * radius != 2 * center - 1 - gap:
        raise AssertionError("radius square was not recoverable from target gap")

    target_center = target_root * (target_root + 1)
    target_offset = lifted - target_center
    if target_offset != center - radius * radius:
        raise AssertionError("target centered offset identity failed")

    return {
        "k": k,
        "radius": radius,
        "center": center,
        "lower": lower,
        "upper": upper,
        "lifted_state": lifted,
        "target_root": target_root,
        "target_collapse": collapsed,
        "target_gap": gap,
        "target_center": target_center,
        "target_offset": target_offset,
    }


def _smooth_core_tail_at_cutoff(value: int, cutoff: int) -> tuple[int, int]:
    core = 1
    tail = value
    for prime in primes_up_to(cutoff):
        while tail % prime == 0:
            core *= prime
            tail //= prime
    if core * tail != value:
        raise AssertionError("smooth-core/tail reconstruction failed")
    return core, tail


def mirror_product_factor_transport(k: int, radius: int) -> dict[str, int]:
    """QL03: factor-precision coordinates multiply under the quadratic lift."""
    data = mirror_product_lift(k, radius)
    lower_data = square_basin_smooth_tail(k, data["lower"])
    upper_data = square_basin_smooth_tail(k, data["upper"])
    predicted_core = int(lower_data["smooth_core"]) * int(upper_data["smooth_core"])
    predicted_tail = int(lower_data["tail"]) * int(upper_data["tail"])

    actual_core, actual_tail = _smooth_core_tail_at_cutoff(data["lifted_state"], k)
    if (predicted_core, predicted_tail) != (actual_core, actual_tail):
        raise AssertionError("mirror-product factor precision did not multiply exactly")

    return {
        **data,
        "lower_core": int(lower_data["smooth_core"]),
        "upper_core": int(upper_data["smooth_core"]),
        "lower_tail": int(lower_data["tail"]),
        "upper_tail": int(upper_data["tail"]),
        "lifted_core_at_k": actual_core,
        "lifted_tail_at_k": actual_tail,
    }


def lifted_full_core_square_spacing(k: int, left: int, right: int) -> dict[str, int]:
    """QL04: total full-core overlap has an automatic factor-eight spacing.

    For anchor-surviving odd radii r,s, let D_r=A_r B_r and D_s=A_s B_s be the
    products of their exact lower/upper full k-smooth cores.  Since D_r divides
    M^2-r^2 and D_s divides M^2-s^2,

        gcd(D_r,D_s) | r^2-s^2.

    Odd squares are 1 mod 8 and the gcd is odd, hence

        8*gcd(D_r,D_s) | |r^2-s^2|.
    """
    _require_k_radius(k, left)
    _require_k_radius(k, right)
    if left == right:
        raise ValueError("radii must be distinct")
    center = k * (k + 1)
    if gcd(left, center) != 1 or gcd(right, center) != 1:
        raise ValueError("both radii must survive the anchor sieve")

    a, b = exact_full_core_pair(k, left)
    c, d = exact_full_core_pair(k, right)
    left_core = a * b
    right_core = c * d
    shared = gcd(left_core, right_core)
    square_difference = abs(left * left - right * right)
    if shared % 2 == 0:
        raise AssertionError("anchor-surviving total full cores must be odd")
    if square_difference % (8 * shared) != 0:
        raise AssertionError("quadratic-lift full-core overlap lost factor-eight spacing")

    left_lift = mirror_product_lift(k, left)["lifted_state"]
    right_lift = mirror_product_lift(k, right)["lifted_state"]
    if abs(left_lift - right_lift) != square_difference:
        raise AssertionError("lift-state difference is not the radius-square difference")

    return {
        "left_radius": left,
        "right_radius": right,
        "left_total_core": left_core,
        "right_total_core": right_core,
        "shared_total_core": shared,
        "radius_square_difference": square_difference,
        "required_divisor": 8 * shared,
    }
