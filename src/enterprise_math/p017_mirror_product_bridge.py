"""Mirror-product scale bridge for the P017 square-basin hard core.

The mother arithmetic identity is more general than P017: for an integer center
M and radius r with 1 <= r^2 <= 2M-1, the product M^2-r^2 lies in the square
basin rooted at M-1.  P017 specializes M=k(k+1), so every centered mirror pair
(M-r,M+r) has the same product-root state M-1 while its P002 collapse-gap
retains the exact radius-square coordinate.

The same product transform acts on a residual full-core cell

    M-r = a*q_-,   M+r = b*q_+,

with S=a*b, by sending the two large tails to the joint quotient

    q_-*q_+ = (M^2-r^2)/S.

For fixed S all resulting square-root states occupy at most two adjacent
integers.  For distinct odd 1<=S<T<k and k>=6, the S-channel lies at least two
root states above the T-channel.  Thus the joint-tail root identifies the core
product S without retaining its label.  This is a finite integer routing result,
not a Legendre proof.
"""

from __future__ import annotations

from math import gcd

from .core import integer_nth_root
from .p017_cofactor_window import square_basin_smooth_tail
from .p017_core_cell_geometry import signed_shared_core_geometry
from .p017_core_cell_lattice import exact_full_core_pair


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def quadratic_mirror_embedding(center: int, radius: int) -> dict[str, int]:
    """CG06 mother arithmetic: M^2-r^2 collapses to (M-1)^2.

    The exact hypotheses are

        M>=1, 1<=r, r^2<=2M-1.

    Then

        (M-1)^2 <= M^2-r^2 < M^2,

    and the lower inequality is strict unless r^2=2M-1.  Under the P017
    specialization M=k(k+1), r<k, it is always strict.
    """
    if isinstance(center, bool) or not isinstance(center, int) or center < 1:
        raise ValueError("center must be a positive integer")
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 1:
        raise ValueError("radius must be a positive integer")
    square = radius * radius
    if square > 2 * center - 1:
        raise ValueError("radius^2 must satisfy radius^2 <= 2*center-1")

    value = center * center - square
    root = integer_nth_root(value, 2)
    expected_root = center - 1
    if root != expected_root:
        raise AssertionError("quadratic mirror product left the predicted square basin")
    collapsed = expected_root * expected_root
    gap = value - collapsed
    expected_gap = 2 * center - 1 - square
    if gap != expected_gap:
        raise AssertionError("quadratic mirror collapse-gap identity failed")

    return {
        "center": center,
        "radius": radius,
        "value": value,
        "root": root,
        "collapsed": collapsed,
        "gap": gap,
        "radius_square": square,
    }


def p017_mirror_product_embedding(k: int, radius: int) -> dict[str, int]:
    """CG06 P017 specialization of the quadratic mirror embedding.

    For M=k(k+1) and 1<=r<k,

        Lambda_r=(M-r)(M+r)=M^2-r^2,
        R_2(Lambda_r)=M-1,
        G_2(Lambda_r)=2M-1-r^2.

    Both original mirror factors have square-root state k, so the root carry of
    their product is the constant k-1.
    """
    _require_k(k)
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")

    center = k * (k + 1)
    lower = center - radius
    upper = center + radius
    product = lower * upper
    data = quadratic_mirror_embedding(center, radius)
    if product != int(data["value"]):
        raise AssertionError("mirror factor product disagrees with M^2-r^2")
    if not ((center - 1) * (center - 1) < product < center * center):
        raise AssertionError("P017 mirror product must lie in the open next-scale square basin")
    if integer_nth_root(lower, 2) != k or integer_nth_root(upper, 2) != k:
        raise AssertionError("original mirror states left their k-root basin")

    carry = int(data["root"]) - k * k
    if carry != k - 1:
        raise AssertionError("mirror-product root carry is not k-1")

    higher_root = center - 1
    higher_center = higher_root * (higher_root + 1)
    higher_offset = product - higher_center
    if higher_offset != center - radius * radius:
        raise AssertionError("higher-basin centered offset failed to encode radius square")

    return {
        **data,
        "k": k,
        "lower": lower,
        "upper": upper,
        "product": product,
        "product_root_carry": carry,
        "higher_root": higher_root,
        "higher_center": higher_center,
        "higher_offset": higher_offset,
    }


def joint_product_root(k: int, radius: int, core_product: int) -> dict[str, int]:
    """Return the square-root state of (M^2-r^2)/S when S divides the product."""
    _require_k(k)
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")
    if isinstance(core_product, bool) or not isinstance(core_product, int) or core_product <= 0:
        raise ValueError("core_product must be a positive integer")

    product = p017_mirror_product_embedding(k, radius)["product"]
    if product % core_product != 0:
        raise ValueError("core_product must divide the mirror product")
    quotient = product // core_product
    root = integer_nth_root(quotient, 2)
    return {
        "k": k,
        "radius": radius,
        "core_product": core_product,
        "mirror_product": product,
        "joint_quotient": quotient,
        "joint_root": root,
    }


def fixed_product_channel(k: int, core_product: int) -> dict[str, object]:
    """CG07: one fixed product S occupies at most two adjacent root states.

    This theorem does not assume primality or the residual hard-core
    classification.  It uses only the common narrow interval

        (M-1)^2 < M^2-r^2 < M^2.
    """
    _require_k(k)
    if isinstance(core_product, bool) or not isinstance(core_product, int) or core_product <= 0:
        raise ValueError("core_product must be a positive integer")

    radii = tuple(
        r for r in range(1, k)
        if (k * (k + 1)) ** 2 % core_product == (r * r) % core_product
    )
    roots = tuple(sorted({joint_product_root(k, r, core_product)["joint_root"] for r in radii}))
    if roots and roots[-1] - roots[0] > 1:
        raise AssertionError("fixed core-product channel spans more than two adjacent roots")
    return {
        "k": k,
        "core_product": core_product,
        "radii": radii,
        "roots": roots,
        "root_count": len(roots),
    }


def separated_product_channels(
    k: int,
    smaller_product: int,
    larger_product: int,
    smaller_radius: int,
    larger_radius: int,
) -> dict[str, int]:
    """CG08: distinct odd S<T<k have root channels separated by at least two.

    For k>=6, odd 1<=S<T<k, and valid divisibility incidences,

        R_2((M^2-r^2)/S) >= R_2((M^2-s^2)/T) + 2.

    The proof is ordinary integer arithmetic.  If t denotes the T-root, the
    lower next-scale basin bound forces t>=3k.  Assuming the S-root were at most
    t+1 would then make T*Q_T-S*Q_S exceed k^2, while this difference is only a
    signed difference of two radius squares and therefore has absolute value
    below k^2.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 6:
        raise ValueError("CG08 requires k >= 6")
    for name, value in (("smaller_product", smaller_product), ("larger_product", larger_product)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0 or value % 2 == 0:
            raise ValueError(f"{name} must be a positive odd integer")
    if not (smaller_product < larger_product < k):
        raise ValueError("products must satisfy smaller_product < larger_product < k")

    small = joint_product_root(k, smaller_radius, smaller_product)
    large = joint_product_root(k, larger_radius, larger_product)
    small_root = int(small["joint_root"])
    large_root = int(large["joint_root"])
    if small_root < large_root + 2:
        raise AssertionError("distinct odd core-product root channels are not separated by two")
    return {
        "smaller_product": smaller_product,
        "larger_product": larger_product,
        "smaller_root": small_root,
        "larger_root": large_root,
        "root_gap": small_root - large_root,
    }


def residual_hard_core_joint_channel(k: int, radius: int) -> dict[str, int]:
    """CG09: joint-tail root is a zero-repair label for residual core product S.

    The function accepts only the residual hard-core regime: both mirror states
    are composite, each has one large prime tail >k after removing its full
    k-smooth core, and S=a*b<k.  Then

        q_- q_+ = (M^2-r^2)/S.

    CG08 makes the root channels of distinct odd S disjoint for k>=6.
    """
    _require_k(k)
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")
    center = k * (k + 1)
    if gcd(radius, center) != 1:
        raise ValueError("radius must survive the anchor sieve")

    a, b = exact_full_core_pair(k, radius)
    lower = center - radius
    upper = center + radius
    lower_data = square_basin_smooth_tail(k, lower)
    upper_data = square_basin_smooth_tail(k, upper)
    q_minus = int(lower_data["tail"])
    q_plus = int(upper_data["tail"])
    if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
        raise ValueError("both mirror states must be composite")
    if q_minus <= k or q_plus <= k:
        raise ValueError("residual hard core requires two large prime tails")
    product = a * b
    if product >= k:
        raise ValueError("residual hard core requires full-core product S<k")

    channel = joint_product_root(k, radius, product)
    if int(channel["joint_quotient"]) != q_minus * q_plus:
        raise AssertionError("joint quotient failed to equal the product of large tails")
    return {
        "k": k,
        "radius": radius,
        "lower_core": a,
        "upper_core": b,
        "core_product": product,
        "lower_tail": q_minus,
        "upper_tail": q_plus,
        "joint_tail_product": q_minus * q_plus,
        "joint_root": int(channel["joint_root"]),
    }


def shared_core_gap_transport(k: int, left: int, right: int) -> dict[str, int]:
    """CG10: CG02 square-distance divisibility transports to P002 gap space."""
    if left == right:
        raise ValueError("radii must be distinct")
    geometry = signed_shared_core_geometry(k, left, right)
    left_gap = p017_mirror_product_embedding(k, left)["gap"]
    right_gap = p017_mirror_product_embedding(k, right)["gap"]
    gap_difference = abs(left_gap - right_gap)
    if gap_difference != int(geometry["radius_square_difference"]):
        raise AssertionError("mirror-product gap difference lost the radius-square geometry")
    required = 4 * int(geometry["total_overlap"])
    if gap_difference % required != 0:
        raise AssertionError("shared full-core overlap did not divide the higher-scale gap difference")
    return {
        "left_radius": left,
        "right_radius": right,
        "left_gap": left_gap,
        "right_gap": right_gap,
        "gap_difference": gap_difference,
        "shared_core_divisor": required,
    }
