"""Unbounded LEGO interaction hierarchy of the saturation rule min(n,m).

The seemingly simple integer rule phi(n,m)=min(n,m) has exact multitype
interaction coefficients

    a_(k,l) = (-1)^(k+l) C(k+l-2,k-1),  k,l>=1,

and zero when either order is zero (apart from phi(0,0)=0).  Thus no finite
interaction order q represents min(n,m) on arbitrarily large inventories.

Proof sketch, entirely finite/integer:

    min(n,m) = sum_{t>=1} 1[n>=t] 1[m>=t].

The k-th binomial interaction coefficient of 1[n>=t] is
(-1)^(k-t) C(k-1,t-1) for 1<=t<=k.  Multiplying the two one-dimensional factors
and summing t gives a constant sign (-1)^(k+l) times Vandermonde's sum
sum_t C(k-1,t-1)C(l-1,t-1)=C(k+l-2,k-1).
"""

from __future__ import annotations

from math import comb


def min_interaction_coefficient(left_order: int, right_order: int) -> int:
    for value, name in ((left_order, "left_order"), (right_order, "right_order")):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    if left_order == 0 or right_order == 0:
        return 0
    magnitude = comb(left_order + right_order - 2, left_order - 1)
    return magnitude if (left_order + right_order) % 2 == 0 else -magnitude


def min_has_nonzero_interaction_at_total_order(total_order: int) -> bool:
    """For every total order >=2 choose (1,total_order-1), whose coefficient is nonzero."""
    if isinstance(total_order, bool) or not isinstance(total_order, int) or total_order < 0:
        raise ValueError("total_order must be a non-negative integer")
    if total_order < 2:
        return False
    return min_interaction_coefficient(1, total_order - 1) != 0


def min_requires_unbounded_interaction_order(maximum_checked_order: int) -> bool:
    """Finite executable witness that every order 2..N has a nonzero term."""
    if isinstance(maximum_checked_order, bool) or not isinstance(maximum_checked_order, int) or maximum_checked_order < 2:
        raise ValueError("maximum_checked_order must be at least two")
    return all(
        min_has_nonzero_interaction_at_total_order(order)
        for order in range(2, maximum_checked_order + 1)
    )
