"""Coarser joint-product root precision for the P017 mirror-product bridge.

CG08 shows that the square-root observation of a residual joint-tail product has
zero cross-core-product ambiguity.  This module asks how far that observation
can be coarsened before repair becomes necessary.

The key moving-state inequality works for every root degree m>=2.  Its cubic
specialization is unusually sharp: if two distinct odd core products S<T<k can
produce the same cubic root from (M^2-r^2)/S and (M^2-s^2)/T, then necessarily
T=S+2.  Thus the cubic observation has at most two candidate core-product
labels, resolved by one binary repair bit.  CG13 makes those candidates an
explicit interval of width <4, and CG14 shows any nontrivial odd divisor of the
true product selects it uniquely.  A real residual-hard-core example at k=88
attains the two-label ambiguity with S=85 and S=87.
"""

from __future__ import annotations

from .core import integer_nth_root
from .p017_mirror_product_bridge import (
    joint_product_root,
    p017_mirror_product_embedding,
    residual_hard_core_joint_channel,
)


def moving_state_power_root_collision_kernel(
    k: int,
    smaller_product: int,
    larger_product: int,
    smaller_radius: int,
    larger_radius: int,
    degree: int,
) -> dict[str, int]:
    """CG12 kernel for equal m-th roots on two moving mirror-product states.

    Put Lambda_r=M^2-r^2.  Assume odd 1<=S<T<k and

        S | Lambda_r,  T | Lambda_s,
        R_m(Lambda_r/S) = R_m(Lambda_s/T) = t.

    Then

        (T-S)t^m
          < k^2 + S((t+1)^m-t^m).

    Unlike canonical P018 distinct-divisor coalescence, the two observed states
    here may differ.  The extra k^2 term is exactly the moving-state budget
    because |Lambda_r-Lambda_s|=|r^2-s^2|<k^2.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >= 4")
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 2:
        raise ValueError("degree must be an integer >= 2")
    for name, value in (("smaller_product", smaller_product), ("larger_product", larger_product)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0 or value % 2 == 0:
            raise ValueError(f"{name} must be a positive odd integer")
    if not (smaller_product < larger_product < k):
        raise ValueError("products must satisfy smaller_product < larger_product < k")

    small = joint_product_root(k, smaller_radius, smaller_product)
    large = joint_product_root(k, larger_radius, larger_product)
    small_q = int(small["joint_quotient"])
    large_q = int(large["joint_quotient"])
    small_root = integer_nth_root(small_q, degree)
    large_root = integer_nth_root(large_q, degree)
    if small_root != large_root:
        raise ValueError("the two observations do not collide at the requested root degree")
    t = small_root

    delta_power = (t + 1) ** degree - t**degree
    lhs = (larger_product - smaller_product) * (t**degree)
    rhs = k * k + smaller_product * delta_power
    if lhs >= rhs:
        raise AssertionError("moving-state root-collision kernel inequality failed")

    small_lambda = int(p017_mirror_product_embedding(k, smaller_radius)["product"])
    large_lambda = int(p017_mirror_product_embedding(k, larger_radius)["product"])
    moving_budget = abs(small_lambda - large_lambda)
    if moving_budget >= k * k:
        raise AssertionError("mirror-product moving-state budget must be below k^2")

    return {
        "k": k,
        "degree": degree,
        "smaller_product": smaller_product,
        "larger_product": larger_product,
        "smaller_radius": smaller_radius,
        "larger_radius": larger_radius,
        "common_root": t,
        "product_gap": larger_product - smaller_product,
        "delta_power": delta_power,
        "lhs": lhs,
        "rhs": rhs,
        "moving_budget": moving_budget,
    }


def cubic_product_collision_ambiguity(
    k: int,
    smaller_product: int,
    larger_product: int,
    smaller_radius: int,
    larger_radius: int,
) -> dict[str, int]:
    """CG12 cubic corollary: a collision can only be S versus S+2.

    For the larger-product quotient Q_T,

        Q_T > (M-1)^2/(k-1) > k^3,

    so its cubic root t is at least k.  The general kernel becomes

        (T-S)t^3 < k^2 + S(3t^2+3t+1)
                    < 3t^3.

    Hence T-S<3.  Distinct S,T are odd, so T-S=2.  Therefore one cubic-root
    state carries at most two candidate odd core products and one repair bit is
    sufficient.  The bound is sharp in the actual residual hard core.
    """
    data = moving_state_power_root_collision_kernel(
        k,
        smaller_product,
        larger_product,
        smaller_radius,
        larger_radius,
        3,
    )
    t = int(data["common_root"])
    if t < k:
        raise AssertionError("cubic joint-product collision root fell below k")

    cubic_rhs = k * k + smaller_product * (3 * t * t + 3 * t + 1)
    if cubic_rhs >= 3 * (t**3):
        raise AssertionError("cubic ambiguity envelope failed to fall below three root blocks")
    if larger_product - smaller_product != 2:
        raise AssertionError("distinct odd cubic-collision products must differ by exactly two")
    return {
        **data,
        "repair_cardinality": 2,
        "repair_bits": 1,
    }


def cubic_core_product_candidate_window(k: int, cubic_root: int) -> dict[str, object]:
    """CG13: decode a cubic joint-root to at most two odd product candidates.

    For any valid residual observation t=R_3((M^2-r^2)/S),

        [M^2-(k-1)^2] / (t+1)^3 < S <= [M^2-1] / t^3.

    Valid residual channels satisfy t>=k.  At that scale the rational interval
    above has width strictly below four.  Therefore it contains at most two odd
    integers below k, and two candidates (if present) differ by exactly two.

    This is an explicit decoder window: no scan over radii or full-core cells is
    needed to obtain the worst-case one-bit candidate set.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >= 4")
    if isinstance(cubic_root, bool) or not isinstance(cubic_root, int) or cubic_root < k:
        raise ValueError("cubic_root must be an integer >= k")

    center = k * (k + 1)
    lower_numerator = center * center - (k - 1) * (k - 1)
    lower_denominator = (cubic_root + 1) ** 3
    upper_numerator = center * center - 1
    upper_denominator = cubic_root**3

    # Strict lower endpoint, closed upper endpoint.
    minimum = lower_numerator // lower_denominator + 1
    maximum = upper_numerator // upper_denominator
    minimum = max(1, minimum)
    maximum = min(k - 1, maximum)

    # Cross-multiply the rational interval width; this avoids any real-number
    # approximation in the implementation.
    width_numerator = (
        upper_numerator * lower_denominator
        - lower_numerator * upper_denominator
    )
    width_denominator = upper_denominator * lower_denominator
    if width_numerator >= 4 * width_denominator:
        raise AssertionError("cubic core-product decoder interval is not narrower than four")

    odd_candidates = tuple(value for value in range(minimum, maximum + 1) if value % 2 == 1)
    if len(odd_candidates) > 2:
        raise AssertionError("cubic decoder window contains more than two odd products")
    if len(odd_candidates) == 2 and odd_candidates[1] - odd_candidates[0] != 2:
        raise AssertionError("two cubic decoder candidates must be consecutive odd integers")

    return {
        "k": k,
        "cubic_root": cubic_root,
        "minimum_product": minimum,
        "maximum_product": maximum,
        "odd_candidates": odd_candidates,
        "candidate_count": len(odd_candidates),
        "repair_bits": 1 if len(odd_candidates) == 2 else 0,
        "width_numerator": width_numerator,
        "width_denominator": width_denominator,
    }


def select_cubic_product_with_divisor(k: int, cubic_root: int, divisor: int) -> dict[str, object]:
    """CG14: any nontrivial odd divisor of the true S removes cubic ambiguity.

    If the CG13 window contains two candidates, they are consecutive odd
    integers and therefore coprime.  No odd divisor d>1 can divide both.  Hence
    a nontrivial endpoint core divisor selects at most one candidate product.

    In the P017 residual hard core, the smaller full core is such a divisor.
    Bridge PR #170 separately gives root-channel mechanisms for recovering that
    small core; composing the two observations removes the explicit S label.
    """
    if isinstance(divisor, bool) or not isinstance(divisor, int) or divisor <= 1 or divisor % 2 == 0:
        raise ValueError("divisor must be an odd integer > 1")
    window = cubic_core_product_candidate_window(k, cubic_root)
    matches = tuple(value for value in window["odd_candidates"] if value % divisor == 0)
    if len(matches) > 1:
        raise AssertionError("one odd divisor selected multiple consecutive cubic candidates")
    return {
        **window,
        "divisor": divisor,
        "matching_products": matches,
        "decoded_product": matches[0] if matches else 0,
        "decoded": len(matches) == 1,
    }


def residual_cubic_core_product_observation(k: int, radius: int) -> dict[str, int]:
    """Return the cubic joint-tail observation for one residual hard-core pair."""
    data = residual_hard_core_joint_channel(k, radius)
    cubic_root = integer_nth_root(int(data["joint_tail_product"]), 3)
    return {
        **data,
        "cubic_joint_root": cubic_root,
    }


def residual_cubic_product_decoder(k: int, radius: int) -> dict[str, object]:
    """CG14 residual specialization using the smaller exact full core as selector."""
    observation = residual_cubic_core_product_observation(k, radius)
    product = int(observation["core_product"])
    divisor = min(int(observation["lower_core"]), int(observation["upper_core"]))
    selected = select_cubic_product_with_divisor(k, int(observation["cubic_joint_root"]), divisor)
    if product not in selected["odd_candidates"]:
        raise AssertionError("true residual core product escaped the cubic decoder window")
    if int(selected["decoded_product"]) != product:
        raise AssertionError("smaller endpoint core failed to select the true cubic product")
    return {
        **observation,
        "small_core_selector": divisor,
        "candidate_products": selected["odd_candidates"],
        "candidate_count": selected["candidate_count"],
        "decoded_product": selected["decoded_product"],
        "remaining_product_repair_bits": 0,
    }
