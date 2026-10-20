"""Core-adaptive Bonferroni majorant for P017×P018 signed mirror states.

For an anchor-surviving signed basin state n=M-x, let P(n) be its complete
transverse small-prime support and let

    C(n) = product_{p in P(n)} p^{v_p(n)}

be the complete transverse small-prime core.  At any positive odd Bonferroni
order m the exact point excess is

    E_m(n) = binom(|P(n)|-1,m).

Instead of splitting E_m into many selected (m+1)-prime tokens, split once by
the product size of the *entire* complete core:

    H^core_m(n) = E_m(n) 1_{C(n)>k-1},
    R^core_m(n) = E_m(n) 1_{C(n)<=k-1}.

Then the pointwise identity is

    b_m(n) - H^core_m(n)
      = 1_{P(n) nonempty} + R^core_m(n).

This is an exact majorant for every odd m.  If C(n)>k-1, the whole defect row is
charged to one complete-core divisor label rather than to many subset tokens.
The label C(n) is an odd transverse divisor of n; P017 CG12 therefore gives
global signed reuse capacity one for that high core.  Its Bonferroni weight is
recoverable from the label itself as

    binom(omega(rad(C(n)))-1,m).

Consequently the high correction has a one-column weighted form

    H^core_m
      = sum_{A>k-1} I_full(A) binom(omega(rad A)-1,m),

where I_full(A) is the exact incidence of A as the complete transverse
small-prime core of a signed state.  This is a row-to-column compression that
retains support depth, prime-power content and finite-boundary information.

The remaining error is supported only on rows whose *entire* small-prime core
fits below k.  At the positive even-J terminal order m=J-1 this specializes
further: every remaining row has exactly J support primes and residual weight
one; see p017_p018_terminal_core_compression.py.

This theorem does not prove Legendre's conjecture.  The unresolved task is to
control/count the low-complete-core residual uniformly without reintroducing
the independent-local-density route already ruled out by the bridge.
"""

from __future__ import annotations

from .p017_p018_bonferroni_defect import odd_bonferroni_point_defect
from .p017_p018_bonferroni_precision import signed_support_profile


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def complete_transverse_core(state: int, support: tuple[int, ...]) -> int:
    """Return prod p^v_p(state) over the declared complete transverse support."""
    if isinstance(state, bool) or not isinstance(state, int) or state <= 0:
        raise ValueError("state must be a positive integer")
    normalized = tuple(sorted(int(p) for p in support))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct primes")

    core = 1
    for prime in normalized:
        if prime < 2 or state % prime != 0:
            raise ValueError("every support prime must divide state")
        remaining = state
        power = 1
        while remaining % prime == 0:
            remaining //= prime
            power *= prime
        core *= power
    if state % core != 0:
        raise AssertionError("complete transverse core failed to divide state")
    return core


def core_adaptive_point_majorant(
    k: int,
    state: int,
    support: tuple[int, ...],
    order: int,
) -> dict[str, object]:
    """Remove the whole point defect when the complete core exceeds k-1."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)

    normalized = tuple(sorted(int(p) for p in support))
    core = complete_transverse_core(state, normalized)
    c = len(normalized)
    point = odd_bonferroni_point_defect(c, order)
    ordinary = int(point["bonferroni_value"])
    indicator = int(point["nonempty_indicator"])
    defect = int(point["defect"])

    high_correction = defect if core > k - 1 else 0
    residual = defect - high_correction
    adjusted = ordinary - high_correction

    if residual != (defect if core <= k - 1 else 0):
        raise AssertionError("complete-core product split lost point defect mass")
    if adjusted != indicator + residual:
        raise AssertionError("core-adaptive point identity failed")
    if adjusted < indicator:
        raise AssertionError("core-adaptive correction ceased to majorize support nonemptiness")

    return {
        "k": k,
        "state": state,
        "support": normalized,
        "support_size": c,
        "order": order,
        "complete_transverse_core": core,
        "ordinary_bonferroni_value": ordinary,
        "nonempty_indicator": indicator,
        "ordinary_defect": defect,
        "high_core_defect_correction": high_correction,
        "residual_core_excess": residual,
        "core_adaptive_value": adjusted,
        "high_complete_core_row": defect > 0 and core > k - 1,
        "low_complete_core_defect_row": residual > 0,
    }


def core_adaptive_signed_profile(k: int, order: int) -> dict[str, object]:
    """Evaluate the exact core-adaptive majorant across the signed mirror basin."""
    _require_order(order)
    profile = signed_support_profile(k)

    rows: list[dict[str, object]] = []
    ordinary_sum = 0
    indicator_sum = 0
    ordinary_defect = 0
    high_correction = 0
    residual_excess = 0
    adjusted_sum = 0
    residual_rows: list[dict[str, object]] = []

    for row in profile["rows"]:
        data = core_adaptive_point_majorant(
            k,
            int(row["state"]),
            tuple(int(p) for p in row["support"]),
            order,
        )
        signed_point = (
            int(row["radius"])
            if str(row["side"]) == "lower"
            else -int(row["radius"])
        )
        enriched = {
            **data,
            "radius": int(row["radius"]),
            "side": str(row["side"]),
            "signed_point": signed_point,
        }
        rows.append(enriched)

        ordinary_sum += int(data["ordinary_bonferroni_value"])
        indicator_sum += int(data["nonempty_indicator"])
        ordinary_defect += int(data["ordinary_defect"])
        high_correction += int(data["high_core_defect_correction"])
        residual_excess += int(data["residual_core_excess"])
        adjusted_sum += int(data["core_adaptive_value"])

        if bool(data["low_complete_core_defect_row"]):
            core = int(data["complete_transverse_core"])
            residual_rows.append(
                {
                    "signed_point": signed_point,
                    "radius": int(row["radius"]),
                    "side": str(row["side"]),
                    "state": int(row["state"]),
                    "support": tuple(int(p) for p in row["support"]),
                    "support_size": int(data["support_size"]),
                    "ordinary_defect": int(data["ordinary_defect"]),
                    "complete_transverse_core": core,
                    "cofactor": int(row["state"]) // core,
                }
            )

    if ordinary_sum != indicator_sum + ordinary_defect:
        raise AssertionError("ordinary Bonferroni defect identity failed globally")
    if ordinary_defect != high_correction + residual_excess:
        raise AssertionError("core-adaptive correction did not partition global defect")
    if adjusted_sum != indicator_sum + residual_excess:
        raise AssertionError("core-adaptive global identity failed")
    if adjusted_sum > ordinary_sum:
        raise AssertionError("core-adaptive majorant exceeded ordinary Bonferroni value")

    total = int(profile["signed_state_count"])
    return {
        "k": k,
        "order": order,
        "signed_state_count": total,
        "prime_state_count": int(profile["prime_state_count"]),
        "composite_state_count": int(profile["composite_state_count"]),
        "ordinary_bonferroni_sum": ordinary_sum,
        "exact_nonempty_union": indicator_sum,
        "ordinary_defect": ordinary_defect,
        "high_core_defect_correction": high_correction,
        "residual_core_excess": residual_excess,
        "core_adaptive_sum": adjusted_sum,
        "core_adaptive_certificate": adjusted_sum < total,
        "residual_rows": tuple(residual_rows),
        "rows": tuple(rows),
    }
