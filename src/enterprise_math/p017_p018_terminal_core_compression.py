"""Terminal full-core compression for the even-J P017×P018 proof-precision shell.

This module is the positive-even-J specialization of the generic core-adaptive
Bonferroni majorant in ``p017_p018_core_adaptive_bonferroni``.

Let

    J = J_perp(k) = max{j : P_perp(k,j) < k}

be positive and even, and take the terminal odd order m=J-1.  For one
anchor-surviving signed state n=M-x, let c(x) be its complete transverse
small-prime support size and C_x its complete transverse small-prime core.

The generic core-adaptive point identity removes the whole Bonferroni defect
whenever C_x>k-1.  Maximality of J supplies the extra terminal conclusion:
if the remaining low-core defect is positive, then C_x<=k-1 rules out
c(x)>=J+1 because rad(C_x)>=P_perp(k,J+1)>=k.  Hence c(x)=J and

    binom(c(x)-1,J-1)=1.

Therefore

    b^core_{J-1}(x)
      = 1_{c(x)>0} + 1_{c(x)=J, C_x<=k-1}.

Every surviving signed row carries at most one complete-core label.  Combined
with P017 CG12 for the high-core single-use part, this removes the duplicate-x
obstruction of token-expanded Vandermonde arguments and exposes the residual
pairs (x,C_x) directly to P017 CG05.

No Legendre proof is claimed.
"""

from __future__ import annotations

from .p017_p018_core_adaptive_bonferroni import (
    core_adaptive_point_majorant,
    core_adaptive_signed_profile,
)
from .p017_p018_near_primorial_precision import near_primorial_adaptive_order


def _require_even_terminal_order(k: int) -> tuple[int, int]:
    data = near_primorial_adaptive_order(k)
    j = int(data["transverse_primorial_depth"])
    if j <= 0 or data["J_parity"] != "EVEN":
        raise ValueError("terminal full-core compression requires positive even J_perp(k)")
    order = int(data["adaptive_odd_order"])
    if order != j - 1 or order % 2 == 0:
        raise AssertionError("even-J near-primorial order is not J-1")
    return j, order


def terminal_core_point_majorant(
    k: int,
    state: int,
    support: tuple[int, ...],
) -> dict[str, object]:
    """Specialize the generic core-adaptive point majorant at m=J-1."""
    j, order = _require_even_terminal_order(k)
    generic = core_adaptive_point_majorant(k, state, support, order)

    c = int(generic["support_size"])
    core = int(generic["complete_transverse_core"])
    defect = int(generic["ordinary_defect"])
    residual = int(generic["residual_core_excess"])

    if residual > 0:
        if core > k - 1:
            raise AssertionError("terminal residual escaped the low-core region")
        if c != j:
            raise AssertionError(
                "low complete core carried terminal defect above support depth J"
            )
        if defect != 1 or residual != 1:
            raise AssertionError("terminal low-core row did not reduce to one defect bit")

    expected_residual = 1 if c == j and core <= k - 1 else 0
    if residual != expected_residual:
        raise AssertionError("terminal full-core residual identity failed")
    if c >= j + 1 and core < k:
        raise AssertionError("J+1 transverse support directions fit below k")

    return {
        **generic,
        "transverse_primorial_depth": j,
        "core_compressed_value": int(generic["core_adaptive_value"]),
        "low_terminal_full_core_row": bool(residual),
    }


def terminal_core_signed_profile(k: int) -> dict[str, object]:
    """Evaluate the one-label residual theorem on the whole signed basin."""
    j, order = _require_even_terminal_order(k)
    generic = core_adaptive_signed_profile(k, order)

    residual_rows: list[dict[str, object]] = []
    for row in generic["residual_rows"]:
        if int(row["support_size"]) != j:
            raise AssertionError("terminal residual row did not have support size J")
        if int(row["ordinary_defect"]) != 1:
            raise AssertionError("terminal residual row did not have unit defect")
        residual_rows.append(dict(row))

    residual = int(generic["residual_core_excess"])
    if residual != len(residual_rows):
        raise AssertionError("terminal residual excess is not one bit per residual row")

    return {
        "k": k,
        "transverse_primorial_depth": j,
        "order": order,
        "signed_state_count": int(generic["signed_state_count"]),
        "prime_state_count": int(generic["prime_state_count"]),
        "composite_state_count": int(generic["composite_state_count"]),
        "ordinary_bonferroni_sum": int(generic["ordinary_bonferroni_sum"]),
        "exact_nonempty_union": int(generic["exact_nonempty_union"]),
        "ordinary_defect": int(generic["ordinary_defect"]),
        "high_core_defect_correction": int(generic["high_core_defect_correction"]),
        "residual_core_excess": residual,
        "core_compressed_sum": int(generic["core_adaptive_sum"]),
        "core_compressed_certificate": bool(generic["core_adaptive_certificate"]),
        "pointwise_residual_is_at_most_one": True,
        "residual_rows": tuple(residual_rows),
        "rows": tuple(generic["rows"]),
    }
