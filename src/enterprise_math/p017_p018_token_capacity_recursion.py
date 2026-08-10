"""Exact quotient recursion for Bonferroni token reuse capacity.

For an odd Bonferroni order m, a canonical defect token contains m+1 distinct
transverse odd primes.  Let

    P_m(k) = P_perp(k,m+1)

be the minimum possible squarefree token product and, when that prefix exists,
let

    C_m(k) = floor((k-1)/P_m(k)) + 1

be the P017 CG12 universal signed reuse-capacity bound.  Define the *extra reuse
budget*

    E_m(k) = C_m(k)-1 = floor((k-1)/P_m(k)).

When proof order increases from m to m+2, the minimum token prefix gains exactly
the next two transverse primes u,v:

    P_{m+2}=P_m*u*v.

Euclidean quotient flattening then gives the exact recursion

    E_{m+2}
      = floor((k-1)/(P_m*u*v))
      = floor(E_m/(u*v)).

Thus proof-order refinement acts on the repair/reuse resource by an exact
integer quotient chain.  The first order at which E_m=0 is exactly the global
single-use token horizon (when the token family still exists); if too few
transverse primes remain, the defect-token family itself is empty.

This is a P017/P018 specialization of ordinary quotient path flattening, not a
new division theorem.  Its project value is to show that proof-order resource
refinement is governed by the same discrete scale algebra as other Enterprise
Math precision projections.
"""

from __future__ import annotations

from .p017_p018_token_reuse_precision import defect_token_reuse_capacity
from .p017_p018_transverse_primorial import transverse_odd_prime_prefix


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def token_capacity_step(k: int, order: int) -> dict[str, object]:
    """Certify E_{m+2}=floor(E_m/(u*v)) for one adjacent odd proof-order step."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)

    next_order = order + 2
    current = defect_token_reuse_capacity(k, order)
    following = defect_token_reuse_capacity(k, next_order)
    primes = transverse_odd_prime_prefix(k, next_order + 1)

    current_possible = bool(current["defect_tokens_possible"])
    next_possible = bool(following["defect_tokens_possible"])
    current_capacity = int(current["universal_signed_reuse_capacity"])
    next_capacity = int(following["universal_signed_reuse_capacity"])
    current_excess = max(0, current_capacity - 1)
    next_excess = max(0, next_capacity - 1)

    if not current_possible:
        if next_possible or current_capacity != 0 or next_capacity != 0:
            raise AssertionError("empty current token family revived at a higher proof order")
        return {
            "k": k,
            "order": order,
            "next_order": next_order,
            "current_capacity": 0,
            "next_capacity": 0,
            "current_excess": 0,
            "next_excess": 0,
            "new_prime_pair": (),
            "pair_scale_factor": None,
            "quotient_recursion_exact": True,
            "token_family_empty": True,
        }

    current_count = order + 1
    next_count = next_order + 1
    if len(primes) < current_count:
        raise AssertionError("current token family exists without its transverse prime prefix")

    if len(primes) < next_count:
        if next_possible or next_capacity != 0 or next_excess != 0:
            raise AssertionError("incomplete next prime prefix did not kill higher-order tokens")
        return {
            "k": k,
            "order": order,
            "next_order": next_order,
            "current_capacity": current_capacity,
            "next_capacity": 0,
            "current_excess": current_excess,
            "next_excess": 0,
            "new_prime_pair": tuple(primes[current_count:]),
            "pair_scale_factor": None,
            "quotient_recursion_exact": True,
            "token_family_empty_at_next_order": True,
        }

    pair = (int(primes[current_count]), int(primes[current_count + 1]))
    scale = pair[0] * pair[1]
    expected = current_excess // scale
    if expected != next_excess:
        raise AssertionError("token reuse excess failed nested quotient flattening")
    if next_excess > current_excess:
        raise AssertionError("higher proof order increased token reuse excess")

    return {
        "k": k,
        "order": order,
        "next_order": next_order,
        "current_capacity": current_capacity,
        "next_capacity": next_capacity,
        "current_excess": current_excess,
        "next_excess": next_excess,
        "new_prime_pair": pair,
        "pair_scale_factor": scale,
        "quotient_recursion_exact": True,
        "token_family_empty": False,
    }


def token_capacity_descent(k: int, max_order: int) -> dict[str, object]:
    """Return the odd-order capacity chain until max_order or the first zero excess."""
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 1 or max_order % 2 == 0:
        raise ValueError("max_order must be a positive odd integer")

    rows: list[dict[str, object]] = []
    order = 1
    current = defect_token_reuse_capacity(k, order)
    rows.append(
        {
            "order": order,
            "capacity": int(current["universal_signed_reuse_capacity"]),
            "excess": max(0, int(current["universal_signed_reuse_capacity"]) - 1),
            "tokens_possible": bool(current["defect_tokens_possible"]),
        }
    )
    while order + 2 <= max_order and rows[-1]["excess"] != 0:
        step = token_capacity_step(k, order)
        order += 2
        rows.append(
            {
                "order": order,
                "capacity": int(step["next_capacity"]),
                "excess": int(step["next_excess"]),
                "tokens_possible": bool(defect_token_reuse_capacity(k, order)["defect_tokens_possible"]),
                "incoming_prime_pair": tuple(step["new_prime_pair"]),
                "incoming_scale_factor": step["pair_scale_factor"],
            }
        )

    terminal = next((int(row["order"]) for row in rows if int(row["excess"]) == 0), None)
    return {
        "k": k,
        "max_order": max_order,
        "rows": tuple(rows),
        "first_zero_excess_order_within_horizon": terminal,
    }
