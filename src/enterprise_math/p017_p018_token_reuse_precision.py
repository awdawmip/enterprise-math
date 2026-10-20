"""Relate residual exact proof order to global defect-token reuse precision.

Let

    P_perp(k,j)

be the product of the first j odd primes transverse to M=k(k+1), and let

    J_perp(k)=max{j : P_perp(k,j)<k}.

The residual S<k hard core already has a canonical transverse-primorial proof
precision: every residual side has support size at most J_perp-1, so the least
positive odd order m>=J_perp-1 is pointwise exact there.

Bonferroni defect tokens have a different but adjacent threshold.  An order-m
defect token is a squarefree product of m+1 transverse primes.  The P017 CG12
signed divisor-capacity theorem gives

    multiplicity(D) <= floor((k-1)/D)+1.

Thus every order-m defect token is globally single-use once its minimum possible
product satisfies

    P_perp(k,m+1) > k-1,

equivalently P_perp(k,m+1)>=k.  By maximality of J_perp, the least positive odd
order with this property is the least odd m>=J_perp.

Consequently the two proof-detail horizons differ by at most one odd-order
quantum:

    m_token - m_residual in {0,2}.

More precisely they are equal when J_perp is odd, and differ by two when
J_perp is even.

The same local data gives a quantitative reuse ladder at any lower order.  If
P=P_perp(k,m+1) is complete, every token D>=P has universal signed reuse
capacity at most

    floor((k-1)/P)+1.

This module records that bridge consequence without duplicating the P017 CG12
implementation.  CG12 remains PROVED_WIP until separately promoted.
"""

from __future__ import annotations

from .p017_p018_transverse_primorial import (
    residual_exact_bonferroni_order,
    transverse_odd_primorial,
    transverse_primorial_depth,
)


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def defect_token_reuse_capacity(k: int, order: int) -> dict[str, object]:
    """Return the CG12 reuse ceiling implied by the minimum order-m token product."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)

    minimum = transverse_odd_primorial(k, order + 1)
    complete = bool(minimum["complete"])
    product = int(minimum["product"])
    if not complete:
        capacity = 0
        tokens_possible = False
        single_use = True
    else:
        capacity = (k - 1) // product + 1
        tokens_possible = True
        single_use = capacity <= 1

    return {
        "k": k,
        "order": order,
        "required_token_prime_count": order + 1,
        "minimum_transverse_token_primes": tuple(minimum["transverse_primes"]),
        "minimum_transverse_token_product": product,
        "defect_tokens_possible": tokens_possible,
        "universal_signed_reuse_capacity": capacity,
        "all_order_m_tokens_single_use": single_use,
        "capacity_dependency": "P017_PROVED_WIP_CG12",
    }


def least_global_single_use_odd_order(k: int) -> dict[str, object]:
    """Return the least odd m for which every order-m token is globally single-use."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    depth = transverse_primorial_depth(k)
    j = int(depth["transverse_primorial_depth"])
    target = max(1, j)
    if target % 2 == 0:
        target += 1

    capacity = defect_token_reuse_capacity(k, target)
    if not bool(capacity["all_order_m_tokens_single_use"]):
        raise AssertionError("least odd order >=J_perp failed the global single-use threshold")
    if target >= 3:
        previous = target - 2
        previous_capacity = defect_token_reuse_capacity(k, previous)
        if bool(previous_capacity["defect_tokens_possible"]) and bool(
            previous_capacity["all_order_m_tokens_single_use"]
        ):
            raise AssertionError("claimed single-use proof order is not minimal")

    return {
        **depth,
        "least_global_single_use_odd_order": target,
        "single_use_capacity": capacity,
    }


def residual_vs_token_precision_horizons(k: int) -> dict[str, object]:
    """Compare residual exactness and global token single-use proof orders."""
    residual = residual_exact_bonferroni_order(k)
    token = least_global_single_use_odd_order(k)
    j = int(residual["transverse_primorial_depth"])
    if j != int(token["transverse_primorial_depth"]):
        raise AssertionError("precision horizons used different transverse primorial depths")

    m_residual = int(residual["least_guaranteed_exact_odd_order"])
    m_token = int(token["least_global_single_use_odd_order"])
    gap = m_token - m_residual
    expected_gap = 0 if j % 2 == 1 else 2
    if gap != expected_gap or gap not in (0, 2):
        raise AssertionError("residual/token proof-precision gap is not one odd-order quantum")

    return {
        "k": k,
        "transverse_primorial_depth": j,
        "residual_exact_odd_order": m_residual,
        "global_token_single_use_odd_order": m_token,
        "odd_order_quantum_gap": gap,
        "horizons_coincide": gap == 0,
        "one_additional_odd_order_quantum": gap == 2,
        "residual": residual,
        "token": token,
    }
