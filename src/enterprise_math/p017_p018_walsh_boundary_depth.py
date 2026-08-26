"""Exact boundary-depth ladder for complementary mixed-Walsh Mobius transport.

Let R>1 be squarefree and let

    S_R(B)=sum_{b|R,b<=B} mu(b),      1<=B<R.

Complementary-divisor transport gives

    S_R(B)=-mu(R) sum_{e|R,e<=H} mu(e),
    H=floor((R-1)/B).

Order all squarefree divisors of R increasingly:

    1=delta_0<delta_1<...<delta_m=R.

If the complement horizon satisfies

    delta_j <= H < delta_(j+1),

then the high-product boundary is determined exactly by the finite prefix

    S_R(B)=-mu(R) * sum_(i=0)^j mu(delta_i).

Equivalently, because every delta_i divides R, the same shell is

    R/delta_(j+1) <= B < R/delta_j.

In the Walsh hyperbola B=floor(C/a), so shell j is equivalently

    a*R/delta_(j+1) <= C < a*R/delta_j.

Thus boundary precision is not naturally support depth.  It is the number of
complement divisors exposed by crossing the product horizon.  The first two
shells are universal.  If p1<p2 are the two smallest prime factors of R:

* first shell R/p1<=B<R:
    S_R(B)=-mu(R),
    sum_{1<b<=B,b|R}mu(b)=-mu(R)-1 in {0,-2};

* second shell R/p2<=B<R/p1:
    S_R(B)=0,
    sum_{1<b<=B,b|R}mu(b)=-1.

Hence the first two mixed-boundary depth shells are never positive.  Genuine
sign fluctuation starts only after at least three complement divisors (including
1) are visible.  This is an exact finite BRC/precision ladder, not a bound on
the number of physical radii in each shell and not a Legendre proof.
"""

from __future__ import annotations

from .p017_p018_walsh_complement_transport import (
    squarefree_divisors_with_mu,
    truncated_divisor_mobius,
)


def ordered_divisor_mobius_prefix(value: int) -> tuple[dict[str, int], ...]:
    """Return increasing divisors with cumulative Mobius prefix sums."""
    rows = squarefree_divisors_with_mu(value)
    cumulative = 0
    result: list[dict[str, int]] = []
    for index, (divisor, mu) in enumerate(rows):
        cumulative += mu
        result.append(
            {
                "index": index,
                "divisor": divisor,
                "mu": mu,
                "cumulative_mu": cumulative,
            }
        )
    return tuple(result)


def boundary_depth_shell(value: int, budget: int) -> dict[str, object]:
    """Return the exact exposed complement-divisor prefix at one budget B<R."""
    if value <= 1:
        raise ValueError("value must be squarefree and >1")
    if isinstance(budget, bool) or not isinstance(budget, int) or not (1 <= budget < value):
        raise ValueError("require integer budget 1<=B<R")
    rows = ordered_divisor_mobius_prefix(value)
    mu_R = int(rows[-1]["mu"])
    horizon = (value - 1) // budget
    exposed = tuple(row for row in rows if int(row["divisor"]) <= horizon)
    if not exposed:
        raise AssertionError("complement horizon must expose divisor 1")
    depth = len(exposed) - 1
    prefix_mu = int(exposed[-1]["cumulative_mu"])
    reconstructed = -mu_R * prefix_mu
    direct = truncated_divisor_mobius(value, budget)
    if direct != reconstructed:
        raise AssertionError("boundary-depth prefix failed complementary Mobius reconstruction")

    current_delta = int(exposed[-1]["divisor"])
    upper_budget_exclusive = value // current_delta
    lower_budget = 0
    if len(exposed) < len(rows):
        next_delta = int(rows[len(exposed)]["divisor"])
        lower_budget = value // next_delta
    if not (lower_budget <= budget < upper_budget_exclusive):
        raise AssertionError("budget did not lie in reconstructed boundary-depth shell")

    return {
        "radical_R": value,
        "budget_B": budget,
        "complement_horizon_H": horizon,
        "boundary_depth": depth,
        "exposed_complement_divisors": tuple(int(row["divisor"]) for row in exposed),
        "exposed_mobius_prefix_sum": prefix_mu,
        "mu_R": mu_R,
        "direct_truncated_mobius_sum": direct,
        "complementary_reconstruction": reconstructed,
        "shell_budget_lower_inclusive": lower_budget,
        "shell_budget_upper_exclusive": upper_budget_exclusive,
        "mixed_inner_excluding_unit": direct - 1,
        "exact_boundary_depth_state": True,
    }


def _prime_factors_squarefree(value: int) -> tuple[int, ...]:
    remaining = value
    factors: list[int] = []
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            factors.append(p)
            remaining //= p
            if remaining % p == 0:
                raise ValueError("value must be squarefree")
        p += 1
    if remaining > 1:
        factors.append(remaining)
    return tuple(factors)


def first_two_boundary_shells(value: int) -> dict[str, object]:
    """Expose universal formulas for the first two shells when omega(R)>=2."""
    rows = ordered_divisor_mobius_prefix(value)
    factors = _prime_factors_squarefree(value)
    if len(factors) < 2:
        raise ValueError("first_two_boundary_shells requires at least two prime factors")
    p1, p2 = factors[0], factors[1]
    mu_R = int(rows[-1]["mu"])
    first_inner = -mu_R - 1
    second_inner = -1
    if first_inner not in (0, -2):
        raise AssertionError("first boundary shell left universal {0,-2} range")
    return {
        "radical_R": value,
        "smallest_prime_p1": p1,
        "second_prime_p2": p2,
        "first_shell_budget": (value // p1, value),
        "first_shell_truncated_sum": -mu_R,
        "first_shell_mixed_inner": first_inner,
        "second_shell_budget": (value // p2, value // p1),
        "second_shell_truncated_sum": 0,
        "second_shell_mixed_inner": second_inner,
        "first_two_shells_never_positive": True,
    }
