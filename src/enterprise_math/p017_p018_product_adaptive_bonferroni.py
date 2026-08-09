"""Product-adaptive Bonferroni majorant for P017 signed states.

Odd Bonferroni truncation has the exact point identity

    B_m(c) = 1_{c>0} + E_m(c),
    E_m(c) = binom(c-1,m),

and the bridge canonically decomposes E_m into defect tokens by fixing the least
support prime and selecting m further support primes.

Each token has a complete selected prime-power block D_full.  Split the token
set into

    H_m = #{tokens : D_full > k-1},
    R_m = #{tokens : D_full <= k-1}.

Then E_m=H_m+R_m and therefore

    B~_m := B_m - H_m
           = 1_{c>0} + R_m.

So B~_m is still a pointwise upper majorant of the composite-support indicator,
but its excess is **exactly the reusable low-product token count**.  Every
high-product token is removed safely rather than left as Bonferroni error.

This is the natural two-cutoff object:

* cardinality cutoff m controls which support subsets create the ordinary
  Bonferroni defect;
* product cutoff k-1 removes the part of that defect already known, via P017
  CG12/full-block capacity, to be globally single-use and L053-singleton.

If the minimum squarefree (m+1)-prime transverse token product exceeds k-1,
then every actual full-block token is high-product and R_m=0.  In that regime
the product-adaptive order-m majorant is **exact on every signed state**, even
though ordinary B_m may still have positive high-support defect.

This is a finite combinatorial identity plus the proved full-block product
classification; it is not a Legendre proof.  Its value is to replace the entire
high-product Bonferroni tail by an exact correction and leave only the genuinely
reusable D_full<=k-1 boundary for further capacity analysis.
"""

from __future__ import annotations

from math import comb

from .p017_p018_bonferroni_defect import odd_bonferroni_point_defect
from .p017_p018_bonferroni_precision import signed_support_profile
from .p017_p018_bonferroni_tokens import defect_token_single_use_threshold
from .p017_p018_full_block_capacity import full_block_token_capacity


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def product_adaptive_point_majorant(
    k: int,
    state: int,
    support: tuple[int, ...],
    order: int,
) -> dict[str, object]:
    """Return B_m, the high-token correction, and the exact reusable excess."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)
    normalized = tuple(sorted(support))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct primes")

    point = odd_bonferroni_point_defect(len(normalized), order)
    ordinary = int(point["bonferroni_value"])
    indicator = int(point["nonempty_indicator"])
    defect = int(point["defect"])

    if defect == 0:
        high_rows: tuple[dict[str, object], ...] = ()
        reusable_rows: tuple[dict[str, object], ...] = ()
    else:
        least = normalized[0]
        from itertools import combinations
        high: list[dict[str, object]] = []
        reusable: list[dict[str, object]] = []
        for subset in combinations(normalized[1:], order):
            selected = (least, *subset)
            token = full_block_token_capacity(k, state, selected)
            if bool(token["full_block_single_use"]):
                high.append(token)
            else:
                reusable.append(token)
        high_rows = tuple(high)
        reusable_rows = tuple(reusable)

    if len(high_rows) + len(reusable_rows) != defect:
        raise AssertionError("full-block token partition lost Bonferroni defect mass")
    adjusted = ordinary - len(high_rows)
    if adjusted != indicator + len(reusable_rows):
        raise AssertionError("product-adaptive majorant identity failed")
    if adjusted < indicator:
        raise AssertionError("product-adaptive correction ceased to majorize support nonemptiness")

    return {
        "k": k,
        "state": state,
        "support": normalized,
        "support_size": len(normalized),
        "order": order,
        "ordinary_bonferroni_value": ordinary,
        "nonempty_indicator": indicator,
        "ordinary_defect": defect,
        "high_product_token_count": len(high_rows),
        "reusable_token_count": len(reusable_rows),
        "product_adaptive_value": adjusted,
        "product_adaptive_excess": adjusted - indicator,
        "high_product_tokens": high_rows,
        "reusable_tokens": reusable_rows,
        "pointwise_exact": adjusted == indicator,
    }


def product_adaptive_uniform_exactness(k: int, order: int) -> dict[str, object]:
    """Return the sufficient all-state exactness criterion P_perp(k,m+1)>k-1."""
    _require_order(order)
    threshold = defect_token_single_use_threshold(k, order)
    exact = bool(threshold["all_defect_tokens_globally_single_use_by_p017_capacity"])
    return {
        **threshold,
        "product_adaptive_majorant_uniformly_exact": exact,
    }


def product_adaptive_signed_profile(k: int, order: int) -> dict[str, object]:
    """Evaluate the adjusted majorant across all anchor-surviving signed states."""
    _require_order(order)
    profile = signed_support_profile(k)
    rows: list[dict[str, object]] = []
    ordinary_sum = 0
    adjusted_sum = 0
    indicator_sum = 0
    high_tokens = 0
    reusable_tokens = 0
    for row in profile["rows"]:
        data = product_adaptive_point_majorant(
            k,
            int(row["state"]),
            tuple(int(p) for p in row["support"]),
            order,
        )
        rows.append(data)
        ordinary_sum += int(data["ordinary_bonferroni_value"])
        adjusted_sum += int(data["product_adaptive_value"])
        indicator_sum += int(data["nonempty_indicator"])
        high_tokens += int(data["high_product_token_count"])
        reusable_tokens += int(data["reusable_token_count"])

    if ordinary_sum != indicator_sum + high_tokens + reusable_tokens:
        raise AssertionError("ordinary Bonferroni sum lost token defect decomposition")
    if adjusted_sum != indicator_sum + reusable_tokens:
        raise AssertionError("adjusted signed majorant lost reusable-token excess identity")

    uniform = product_adaptive_uniform_exactness(k, order)
    if bool(uniform["product_adaptive_majorant_uniformly_exact"]) and reusable_tokens != 0:
        raise AssertionError("uniform single-use threshold left reusable defect tokens")

    return {
        "k": k,
        "order": order,
        "signed_state_count": int(profile["signed_state_count"]),
        "prime_state_count": int(profile["prime_state_count"]),
        "composite_state_count": int(profile["composite_state_count"]),
        "ordinary_bonferroni_sum": ordinary_sum,
        "product_adaptive_sum": adjusted_sum,
        "exact_nonempty_union": indicator_sum,
        "high_product_token_correction": high_tokens,
        "reusable_token_excess": reusable_tokens,
        "product_adaptive_certificate": adjusted_sum < int(profile["signed_state_count"]),
        "pointwise_exact_on_all_rows": adjusted_sum == indicator_sum,
        "uniform_exactness": uniform,
        "rows": tuple(rows),
    }
