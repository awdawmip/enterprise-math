"""Higher-order primitive-response moments reveal discrete structure hidden at order two.

For A_(N-1) primitive roots e_i-e_j define even response moments

    M_(2s)(x)=sum_{i!=j}(x_i-x_j)^(2s).

On the zero-sum relation space, M2 is proportional to the unique anonymous
quadratic shadow.  At fourth order

    M4 = 2N*S4 + 6*S2^2,

where Sk=sum_i x_i^k.  For N>=4, S4 is an independent invariant, so the fourth
moment is not determined by the quadratic shadow alone.  Thus complete anonymous
A geometry has an isotropic second-order real shadow but retains higher-order
discrete anisotropy.

A2/N=3 is exceptional: on S1=0, S4=S2^2/2, so M4=9*S2^2.  Its first analogous
split appears at sixth order:

    M6 = (33*S2^3 - 36*S3^2)/2.

These are integer polynomial identities.  Any physical interpretation of the
higher moments requires a separate P016 bridge.
"""

from __future__ import annotations

Vector = tuple[int, ...]


def power_sum(state: Vector, power: int) -> int:
    if not state or any(isinstance(value, bool) or not isinstance(value, int) for value in state):
        raise ValueError("state must be a nonempty integer tuple")
    if isinstance(power, bool) or not isinstance(power, int) or power < 0:
        raise ValueError("power must be a non-negative integer")
    return sum(value ** power for value in state)


def a_oriented_even_moment(state: Vector, order: int) -> int:
    if sum(state) != 0:
        raise ValueError("A relation state must have zero total")
    if isinstance(order, bool) or not isinstance(order, int) or order <= 0 or order % 2:
        raise ValueError("order must be a positive even integer")
    return sum(
        (state[i] - state[j]) ** order
        for i in range(len(state))
        for j in range(len(state))
        if i != j
    )


def a_second_moment_identity(state: Vector) -> bool:
    if sum(state) != 0:
        raise ValueError("state must have zero total")
    return a_oriented_even_moment(state, 2) == 2 * len(state) * power_sum(state, 2)


def a_fourth_moment_closed_form(state: Vector) -> int:
    if sum(state) != 0:
        raise ValueError("state must have zero total")
    n = len(state)
    s2 = power_sum(state, 2)
    s4 = power_sum(state, 4)
    return 2 * n * s4 + 6 * s2 * s2


def a_fourth_moment_identity(state: Vector) -> bool:
    return a_oriented_even_moment(state, 4) == a_fourth_moment_closed_form(state)


def quartic_is_not_quadratic_only_witness() -> tuple[Vector, Vector, int, int]:
    """Exact rank-3 witness using cross multiplication, no normalization division."""
    left = (1, -1, 0, 0)
    right = (1, 1, -1, -1)
    left_m4 = a_oriented_even_moment(left, 4)
    right_m4 = a_oriented_even_moment(right, 4)
    left_s2 = power_sum(left, 2)
    right_s2 = power_sum(right, 2)
    left_cross = left_m4 * right_s2 ** 2
    right_cross = right_m4 * left_s2 ** 2
    return left, right, left_cross, right_cross


def a2_fourth_moment_quadratic_identity(state: Vector) -> bool:
    if len(state) != 3 or sum(state) != 0:
        raise ValueError("A2 state requires three zero-sum coordinates")
    s2 = power_sum(state, 2)
    return a_oriented_even_moment(state, 4) == 9 * s2 * s2


def a2_sixth_moment_closed_form_twice(state: Vector) -> int:
    """Return 2*M6 = 33*S2^3 - 36*S3^2 on A2."""
    if len(state) != 3 or sum(state) != 0:
        raise ValueError("A2 state requires three zero-sum coordinates")
    s2 = power_sum(state, 2)
    s3 = power_sum(state, 3)
    return 33 * s2 ** 3 - 36 * s3 ** 2


def a2_sixth_moment_identity(state: Vector) -> bool:
    return 2 * a_oriented_even_moment(state, 6) == a2_sixth_moment_closed_form_twice(state)


def a2_sixth_order_anisotropy_witness() -> tuple[Vector, Vector, int, int]:
    left = (1, -1, 0)
    right = (1, 1, -2)
    left_m6 = a_oriented_even_moment(left, 6)
    right_m6 = a_oriented_even_moment(right, 6)
    left_s2 = power_sum(left, 2)
    right_s2 = power_sum(right, 2)
    # Compare scale-free ratios M6/S2^3 by cross multiplication.
    return left, right, left_m6 * right_s2 ** 3, right_m6 * left_s2 ** 3
