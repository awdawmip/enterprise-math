"""Coarser joint-product root precision for the P017 mirror-product bridge.

CG08 shows that the square-root observation of a residual joint-tail product has
zero cross-core-product ambiguity.  This module asks how far that observation
can be coarsened before repair becomes necessary.

The key moving-state inequality works for every root degree m>=2.  Its cubic
specialization is unusually sharp: if two distinct odd core products S<T<k can
produce the same cubic root from (M^2-r^2)/S and (M^2-s^2)/T, then necessarily
T=S+2.  Thus the cubic observation has at most two candidate core-product
labels, resolved by one binary repair bit.  A real residual-hard-core example at
k=88 attains this ambiguity with S=85 and S=87.
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


def residual_cubic_core_product_observation(k: int, radius: int) -> dict[str, int]:
    """Return the cubic joint-tail observation for one residual hard-core pair."""
    data = residual_hard_core_joint_channel(k, radius)
    cubic_root = integer_nth_root(int(data["joint_tail_product"]), 3)
    return {
        **data,
        "cubic_joint_root": cubic_root,
    }
