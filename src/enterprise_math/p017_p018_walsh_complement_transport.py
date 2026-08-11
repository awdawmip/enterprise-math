"""Complementary-divisor transport for the one-sided mixed Walsh boundary.

Let R>1 be a squarefree target-side low radical and let B>=1 be the current
divisor budget.  Put

    S_R(B)=sum_{b|R, b<=B} mu(b).

If B>=R then S_R(B)=0.  If B<R, full Mobius cancellation together with the
complement involution b=R/e gives the exact identity

    S_R(B)
      = -mu(R) sum_{e|R, e<R/B} mu(e).

In the P017/P018 mixed Walsh hyperbola the budget is

    B=floor(C/a),

where C=floor((k-1)/2) and a is an opposite-side squarefree divisor.  Hence an
incomplete high-product condition a*R>C is transported to the low quotient
window

    e < R / floor(C/a).

Ignoring only the floor for intuition, the scale is the overshoot ratio aR/C.
Thus a boundary which barely crosses the reusable product horizon exposes only
a tiny complementary-divisor future language; deeper crossings reveal more
complement divisors.

The exact function below uses the integer budget B and checks the strict
complement condition R/e>B, so no approximation by aR/C is used in theorem
logic.  This is a finite Möbius/BRC transport identity, not a cancellation
estimate and not a Legendre proof.
"""

from __future__ import annotations

from itertools import combinations
from math import prod


def _factor_squarefree(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    remaining = value
    factors: list[int] = []
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            factors.append(p)
            if remaining % p == 0:
                raise ValueError("value must be squarefree")
        p += 1
    if remaining > 1:
        factors.append(remaining)
    if prod(factors, start=1) != value:
        raise AssertionError("squarefree factorization failed")
    return tuple(factors)


def squarefree_divisors_with_mu(value: int) -> tuple[tuple[int, int], ...]:
    factors = _factor_squarefree(value)
    rows: list[tuple[int, int]] = []
    for size in range(len(factors) + 1):
        mu = -1 if size % 2 else 1
        for subset in combinations(factors, size):
            rows.append((prod(subset, start=1), mu))
    return tuple(sorted(rows))


def truncated_divisor_mobius(value: int, budget: int) -> int:
    if isinstance(budget, bool) or not isinstance(budget, int) or budget < 0:
        raise ValueError("budget must be a nonnegative integer")
    return sum(mu for divisor, mu in squarefree_divisors_with_mu(value) if divisor <= budget)


def complementary_mobius_transport(value: int, budget: int) -> dict[str, object]:
    """Verify S_R(B) by direct and complementary divisor sums."""
    if value <= 1:
        raise ValueError("value must be squarefree and >1")
    rows = squarefree_divisors_with_mu(value)
    mu_R = next(mu for divisor, mu in rows if divisor == value)
    direct = sum(mu for divisor, mu in rows if divisor <= budget)

    if budget >= value:
        complement = 0
        complement_rows: tuple[tuple[int, int], ...] = ()
        regime = "COMPLETE_MOBIUS_CANCELLATION"
    else:
        selected = tuple((e, mu) for e, mu in rows if value // e > budget)
        complement = -mu_R * sum(mu for _e, mu in selected)
        complement_rows = selected
        regime = "COMPLEMENTARY_DIVISOR_TRANSPORT"
    if direct != complement:
        raise AssertionError("complementary Mobius transport identity failed")

    return {
        "radical_R": value,
        "budget_B": budget,
        "mu_R": mu_R,
        "direct_truncated_mobius_sum": direct,
        "complementary_reconstruction": complement,
        "regime": regime,
        "complement_divisor_rows": complement_rows,
        "identity": True,
    }


def walsh_overshoot_transport(k: int, opposite_divisor: int, target_radical: int) -> dict[str, object]:
    """Apply complement transport at B=floor(C/a) for one mixed Walsh term."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if opposite_divisor < 1:
        raise ValueError("opposite_divisor must be positive")
    C = (k - 1) // 2
    budget = C // opposite_divisor
    data = complementary_mobius_transport(target_radical, budget)
    product_value = opposite_divisor * target_radical
    incomplete = target_radical > budget
    if incomplete != (product_value > C):
        raise AssertionError("mixed product horizon and truncated-budget condition disagree")

    complement_values = tuple(int(e) for e, _mu in data["complement_divisor_rows"])
    exact_max_exposed = max(complement_values, default=0)
    # Every selected complement satisfies e*B < R.  The real overshoot ratio is
    # recorded only as a diagnostic Fraction-free pair aR/C.
    return {
        **data,
        "k": k,
        "reusable_floor_cutoff_C": C,
        "opposite_divisor_a": opposite_divisor,
        "mixed_full_product_aR": product_value,
        "crosses_product_horizon": product_value > C,
        "exact_complement_max_exposed": exact_max_exposed,
        "overshoot_numerator_aR": product_value,
        "overshoot_denominator_C": C,
        "high_to_low_transport": True,
    }
