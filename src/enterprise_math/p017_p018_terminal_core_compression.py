"""Terminal full-core compression for the even-J P017×P018 proof-precision shell.

Let

    J = J_perp(k) = max{j : P_perp(k,j) < k}

be the transverse primorial depth.  The near-primorial terminal order is

    m = J - 1

when J>0 is even.  For one anchor-surviving signed basin state n=M-x, let P(n)
be its complete transverse small-prime support and c=|P(n)|.  The exact odd
Bonferroni point excess at order m is

    E_m(n) = binom(c-1, J-1).

Write the complete transverse small-prime core

    C(n) = product_{p in P(n)} p^{v_p(n)}.

Maximality of J gives P_perp(k,J+1) >= k whenever a (J+1)-st transverse prime
exists.  Consequently:

* if E_m(n)>0 and C(n)<=k-1, then c=J;
* hence every such low-core residual row has E_m(n)=1;
* every row with c>=J+1 has C(n)>=rad(C(n))>=P_perp(k,J+1)>=k and all of its
  Bonferroni excess can be charged to the single complete-core label C(n).

Thus the terminal point identity compresses from many subset tokens to

    b_m(c)
      = 1_{c>0}
        + E_m(n) 1_{C(n)>k-1}
        + 1_{c=J, C(n)<=k-1}.

After subtracting the high-core term, the remaining excess is exactly one bit
per low terminal full-core row:

    b^core_m(n)
      = 1_{c>0} + 1_{c=J, C(n)<=k-1}.

This is stronger than merely selecting one defect token: a high-support row with
large complete core can carry many Bonferroni defect units, and the whole row is
compressed to one divisor label.  Because C(n)>k-1 is an odd transverse divisor
of n, P017 CG12 gives global single-use of that label across both mirror
orientations.  For the remaining low rows, c=J and the ordinary point defect is
already one, so every signed point has at most one relevant complete-core label.
This removes the repeated-x obstruction that would make a direct token-expanded
Vandermonde product vanish.

The theorem is a finite integer identity plus the transverse-primorial cutoff.
It does not prove Legendre's conjecture.  Its next use is to apply P017 CG05
directly to the residual pairs (x,C(n)), retaining the near-primorial prime
weights in the gcd/Vandermonde collision cost.
"""

from __future__ import annotations

from .p017_p018_bonferroni_defect import odd_bonferroni_point_defect
from .p017_p018_bonferroni_precision import signed_support_profile
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


def _complete_support_block(state: int, support: tuple[int, ...]) -> int:
    """Return prod p^v_p(state) over the declared complete small-prime support."""
    if isinstance(state, bool) or not isinstance(state, int) or state <= 0:
        raise ValueError("state must be a positive integer")
    normalized = tuple(sorted(int(p) for p in support))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct primes")

    block = 1
    for prime in normalized:
        if prime < 2 or state % prime != 0:
            raise ValueError("every support prime must divide state")
        remaining = state
        power = 1
        while remaining % prime == 0:
            remaining //= prime
            power *= prime
        block *= power
    if state % block != 0:
        raise AssertionError("complete support block failed to divide state")
    return block


def terminal_core_point_majorant(
    k: int,
    state: int,
    support: tuple[int, ...],
) -> dict[str, object]:
    """Compress the terminal even-J Bonferroni excess of one signed state."""
    j, order = _require_even_terminal_order(k)
    normalized = tuple(sorted(int(p) for p in support))
    core = _complete_support_block(state, normalized)
    c = len(normalized)

    point = odd_bonferroni_point_defect(c, order)
    ordinary = int(point["bonferroni_value"])
    indicator = int(point["nonempty_indicator"])
    defect = int(point["defect"])

    high_core_correction = defect if core > k - 1 else 0
    residual = defect - high_core_correction

    if defect > 0 and core <= k - 1:
        if c != j:
            raise AssertionError(
                "low complete core carried terminal defect above support depth J"
            )
        if defect != 1 or residual != 1:
            raise AssertionError("terminal low-core row did not reduce to one defect bit")

    compressed = ordinary - high_core_correction
    expected_residual = 1 if c == j and core <= k - 1 else 0
    if residual != expected_residual:
        raise AssertionError("terminal full-core residual identity failed")
    if compressed != indicator + residual:
        raise AssertionError("terminal full-core majorant identity failed")
    if c >= j + 1 and core < k:
        raise AssertionError("J+1 transverse support directions fit below k")

    return {
        "k": k,
        "state": state,
        "support": normalized,
        "support_size": c,
        "transverse_primorial_depth": j,
        "order": order,
        "complete_transverse_core": core,
        "ordinary_bonferroni_value": ordinary,
        "nonempty_indicator": indicator,
        "ordinary_defect": defect,
        "high_core_defect_correction": high_core_correction,
        "residual_core_excess": residual,
        "core_compressed_value": compressed,
        "low_terminal_full_core_row": bool(residual),
        "high_complete_core_row": defect > 0 and core > k - 1,
    }


def terminal_core_signed_profile(k: int) -> dict[str, object]:
    """Evaluate the exact terminal full-core compression on the whole signed basin."""
    j, order = _require_even_terminal_order(k)
    profile = signed_support_profile(k)

    rows: list[dict[str, object]] = []
    ordinary_sum = 0
    indicator_sum = 0
    ordinary_defect = 0
    high_correction = 0
    residual_excess = 0
    compressed_sum = 0
    residual_rows: list[dict[str, object]] = []

    for row in profile["rows"]:
        data = terminal_core_point_majorant(
            k,
            int(row["state"]),
            tuple(int(p) for p in row["support"]),
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
        compressed_sum += int(data["core_compressed_value"])
        if bool(data["low_terminal_full_core_row"]):
            core = int(data["complete_transverse_core"])
            if int(row["state"]) % core != 0:
                raise AssertionError("terminal residual core failed to divide state")
            residual_rows.append(
                {
                    "signed_point": signed_point,
                    "radius": int(row["radius"]),
                    "side": str(row["side"]),
                    "state": int(row["state"]),
                    "support": tuple(int(p) for p in row["support"]),
                    "complete_transverse_core": core,
                    "cofactor": int(row["state"]) // core,
                }
            )

    if ordinary_sum != indicator_sum + ordinary_defect:
        raise AssertionError("ordinary Bonferroni defect identity failed globally")
    if ordinary_defect != high_correction + residual_excess:
        raise AssertionError("terminal core correction did not partition the defect")
    if compressed_sum != indicator_sum + residual_excess:
        raise AssertionError("terminal core-compressed global identity failed")
    if residual_excess != len(residual_rows):
        raise AssertionError("terminal residual excess is not one bit per residual row")

    total = int(profile["signed_state_count"])
    if compressed_sum > ordinary_sum:
        raise AssertionError("full-core compression enlarged the Bonferroni majorant")

    return {
        "k": k,
        "transverse_primorial_depth": j,
        "order": order,
        "signed_state_count": total,
        "prime_state_count": int(profile["prime_state_count"]),
        "composite_state_count": int(profile["composite_state_count"]),
        "ordinary_bonferroni_sum": ordinary_sum,
        "exact_nonempty_union": indicator_sum,
        "ordinary_defect": ordinary_defect,
        "high_core_defect_correction": high_correction,
        "residual_core_excess": residual_excess,
        "core_compressed_sum": compressed_sum,
        "core_compressed_certificate": compressed_sum < total,
        "pointwise_residual_is_at_most_one": True,
        "residual_rows": tuple(residual_rows),
        "rows": tuple(rows),
    }
