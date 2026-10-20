"""One-step support-depth contraction for high-product Bonferroni defect tokens.

The Bonferroni token bridge already proves that, for an anchor-surviving state
in the open k-th square basin, a defect token whose squarefree radical exceeds
k-1 is globally single-use and its complete selected prime-power block has
quotient q<=k.  This module records what that descent does to the *remaining*
support.

For odd order m, every defect token selects exactly m+1 distinct transverse
support primes.  Removing their complete prime-power blocks therefore deletes
exactly m+1 support directions.  If the parent support has cardinality c, the
quotient has exactly

    t = c-m-1

distinct prime directions.

Put child = R_2(q).  Since q<=k,

    child <= R_2(k) < k.

Moreover q<(child+1)^2, so at most one quotient prime can exceed child, and such
a prime occurs only to the first power.  Thus all but at most one of the
remaining support directions lie already in the lower child scale.

There is also a scale-wide sufficient condition for one-step *same-order*
termination.  Let P_perp(k,j) be the product of the first j odd primes
transverse to M=k(k+1).

* If P_perp(k,m+1)>k-1 (or fewer than m+1 transverse primes exist), every
  order-m defect token is in the single-use product regime.
* If P_perp(k,2m+2)>k(k+2) (or fewer than 2m+2 transverse primes exist), no
  square-basin state can contain 2m+2 distinct transverse support primes.

Under both conditions every order-m defect row has c<=2m+1.  After deleting
m+1 selected directions the quotient support has size at most m, so the same
order-m Bonferroni defect is exactly zero on the quotient after one descent.

This is a bridge theorem about proof-detail transport, not a Legendre proof and
not a claim that the quotient itself is a new P017 mirror state.  The child
square-root scale is used only as an exact integer complexity coordinate.
"""

from __future__ import annotations

from math import isqrt

from .cutoff_pairing import transverse_prime_support
from .legendre import anchor_product
from .p017_p018_bonferroni_tokens import point_full_block_defect_tokens
from .p017_p018_transverse_primorial import transverse_odd_primorial


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def _global_transverse_product_barrier(k: int, count: int, upper: int) -> dict[str, object]:
    data = transverse_odd_primorial(k, count)
    complete = bool(data["complete"])
    product = int(data["product"])
    return {
        "required_prime_count": count,
        "transverse_primes": tuple(data["transverse_primes"]),
        "complete": complete,
        "product": product,
        "upper_bound": upper,
        "impossible_below_upper": (not complete) or product > upper,
    }


def one_step_token_terminal_criterion(k: int, order: int) -> dict[str, object]:
    """Return a sufficient scale-wide criterion for one-step same-order termination."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)

    token = _global_transverse_product_barrier(k, order + 1, k - 1)
    support = _global_transverse_product_barrier(k, 2 * order + 2, k * (k + 2))
    guaranteed = bool(token["impossible_below_upper"] and support["impossible_below_upper"])
    return {
        "k": k,
        "order": order,
        "single_use_token_barrier": token,
        "two_block_support_barrier": support,
        "all_defect_tokens_single_use": bool(token["impossible_below_upper"]),
        "all_parent_support_sizes_at_most_2m_plus_1": bool(support["impossible_below_upper"]),
        "one_step_same_order_terminal": guaranteed,
        "parent_state_upper": k * (k + 2),
        "parent_root_ceiling": isqrt(k),
    }


def point_token_support_descent(k: int, state: int, order: int) -> dict[str, object]:
    """Expose exact support and square-root contraction for every token of one row."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(state, bool) or not isinstance(state, int) or not (k * k < state < (k + 1) ** 2):
        raise ValueError("state must lie in the open k-th square basin")
    _require_order(order)

    support = tuple(transverse_prime_support(state, k, anchor_product(k)))
    token_data = point_full_block_defect_tokens(k, state, support, order)
    parent_support_size = len(support)
    rows: list[dict[str, object]] = []

    for token in token_data["token_rows"]:
        single_use = bool(token["single_use_product_regime"])
        omitted = tuple(int(p) for p in token["omitted_support_primes"])
        quotient = int(token["quotient"])
        expected_omitted = parent_support_size - order - 1
        if len(omitted) != expected_omitted:
            raise AssertionError("full-block token did not delete exactly m+1 support directions")

        row: dict[str, object] = {
            **token,
            "parent_support_size": parent_support_size,
            "support_drop": order + 1,
            "child_support_size": len(omitted),
            "same_order_defect_terminal_by_support": len(omitted) <= order,
        }
        if not single_use:
            rows.append(row)
            continue

        canonical_q_support = tuple(int(p) for p in (token["quotient_support"] or ()))
        if canonical_q_support != omitted:
            raise AssertionError("single-use quotient support is not the exact omitted support")
        if quotient < 1 or quotient > k:
            raise AssertionError("single-use token quotient escaped 1<=q<=k")

        child_root = isqrt(quotient)
        if not child_root * child_root <= quotient < (child_root + 1) ** 2:
            raise AssertionError("child square-root cell identity failed")
        if child_root > isqrt(k) or child_root >= k:
            raise AssertionError("token quotient failed strict parent-scale contraction")

        high = tuple(p for p in omitted if p > child_root)
        low = tuple(p for p in omitted if p <= child_root)
        if len(high) > 1:
            raise AssertionError("two quotient support primes escaped above the child square root")
        if high and quotient % (high[0] * high[0]) == 0:
            raise AssertionError("a child-large quotient prime appeared with exponent >=2")
        if len(low) < max(0, len(omitted) - 1):
            raise AssertionError("too many quotient support directions escaped the child root scale")

        row.update(
            {
                "child_root_scale": child_root,
                "child_root_scale_ceiling": isqrt(k),
                "child_low_support": low,
                "child_large_tail_support": high,
                "child_low_support_size": len(low),
                "at_most_one_child_large_tail_direction": True,
                "strict_scale_descent": True,
            }
        )
        rows.append(row)

    return {
        "k": k,
        "state": state,
        "order": order,
        "support": support,
        "support_size": parent_support_size,
        "defect": int(token_data["defect"]),
        "token_rows": tuple(rows),
        "all_tokens_single_use": all(bool(row["single_use_product_regime"]) for row in rows),
        "all_single_use_tokens_same_order_terminal": all(
            (not bool(row["single_use_product_regime"]))
            or bool(row["same_order_defect_terminal_by_support"])
            for row in rows
        ),
    }


def certify_one_step_same_order_terminal(k: int, state: int, order: int) -> dict[str, object]:
    """Require the scale-wide criterion and certify one actual defect row."""
    criterion = one_step_token_terminal_criterion(k, order)
    if not bool(criterion["one_step_same_order_terminal"]):
        raise ValueError("scale does not satisfy the sufficient one-step terminal criterion")

    data = point_token_support_descent(k, state, order)
    if int(data["defect"]) <= 0:
        raise ValueError("state must carry positive order-m Bonferroni defect")
    if not bool(data["all_tokens_single_use"]):
        raise AssertionError("global single-use barrier failed on an actual defect token")
    if int(data["support_size"]) > 2 * order + 1:
        raise AssertionError("global support barrier failed on an actual square-basin state")
    if not bool(data["all_single_use_tokens_same_order_terminal"]):
        raise AssertionError("single-use token quotient retained same-order defect support")

    return {
        **data,
        "criterion": criterion,
        "certified_one_step_same_order_terminal": True,
    }
