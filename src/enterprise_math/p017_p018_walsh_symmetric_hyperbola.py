"""Exact symmetric Dirichlet-hyperbola compiler for P017/P018 Walsh precision.

Let C=floor((k-1)/2) be the exact reusable-floor cutoff.  For one surviving
mirror radius write n_-=M-r and n_+=M+r and let L,U be their disjoint transverse
small-prime supports.  The incidence-optimal one-sided weight is

    h_*(S)=#{T subseteq S : rad(T)<=C}.

Hence the normalized symmetric detector

    G_C(r)=1/2[h_*(L) 1_{U=empty}+h_*(U) 1_{L=empty}]

has the exact divisor-hyperbola expansion

    G_C(r)=1/2[
      sum_{e|rad(L), e<=C} sum_{d|rad(U)} mu(d)
      +
      sum_{d|rad(U), d<=C} sum_{e|rad(L)} mu(e)
    ].

Thus the coefficient of an oriented squarefree divisor pair (e,d) is

    c_C(e,d)=1/2[1_{e<=C} mu(d)+1_{d<=C} mu(e)].

Every retained pair has min(e,d)<=C; the both-high quadrant is compiled away.
For an anchor-Mobius divisor a, one orientation pattern occupies one class
modulo 2*a*e*d.  Its repeated floor bulk can be nonzero only when

    a*e*d <= C.

Therefore the genuinely reusable mixed core lies below the *product* hyperbola,
not in the full square [1,C]^2.

When q=e*d<=C is squarefree and (e,d)=1, both sides are in the forced low
incidence down-set.  Then

    c_C(e,q/e)=0                  if omega(q) is odd,
                mu(e)             if omega(q) is even.

So every odd-support reusable pattern vanishes pointwise.  For even nontrivial
q, summing over all orientation splits gives

    sum_{e|q} mu(e)=0,

which is the exact zero-continuous-bulk law at fixed total conductor.  Only the
finite orientation-split boundary difference remains.

This is an exact compiler/precision theorem.  It does not estimate the boundary
remainder and does not prove prime existence.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd, prod

from .p017_mirror import anchor_surviving_radius, mirror_transverse_supports
from .p017_p018_walsh_incidence_optimal import incidence_optimal_weight
from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff


def _squarefree_divisors_from_support(support: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Return (divisor,mu) for every subset of a declared distinct-prime support."""
    normalized = tuple(sorted(int(p) for p in support))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct primes")
    rows: list[tuple[int, int]] = []
    for size in range(len(normalized) + 1):
        mu = -1 if size % 2 else 1
        for subset in combinations(normalized, size):
            rows.append((prod(subset, start=1), mu))
    return tuple(sorted(rows))


def symmetric_hyperbola_coefficient(k: int, lower_divisor: int, upper_divisor: int) -> Fraction:
    """Return c_C(e,d) for one squarefree orientation-divisor pair."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    for name, value in (("lower_divisor", lower_divisor), ("upper_divisor", upper_divisor)):
        if isinstance(value, bool) or not isinstance(value, int) or value < 1 or value % 2 == 0:
            raise ValueError(f"{name} must be a positive odd integer")
    if gcd(lower_divisor, upper_divisor) != 1:
        raise ValueError("orientation divisors must be coprime")

    def squarefree_mu(value: int) -> int:
        remaining = value
        omega = 0
        p = 3
        while p * p <= remaining:
            if remaining % p == 0:
                remaining //= p
                omega += 1
                if remaining % p == 0:
                    raise ValueError("orientation divisors must be squarefree")
            p += 2
        if remaining > 1:
            omega += 1
        return -1 if omega % 2 else 1

    C = reusable_floor_product_cutoff(k)
    mu_e = squarefree_mu(lower_divisor)
    mu_d = squarefree_mu(upper_divisor)
    return Fraction(
        int(lower_divisor <= C) * mu_d + int(upper_divisor <= C) * mu_e,
        2,
    )


def hyperbola_floor_classification(
    k: int,
    lower_divisor: int,
    upper_divisor: int,
    anchor_divisor: int = 1,
) -> dict[str, object]:
    """Classify retained-vs-floor-reusable geometry for one (e,d,a) pattern."""
    if isinstance(anchor_divisor, bool) or not isinstance(anchor_divisor, int) or anchor_divisor < 1:
        raise ValueError("anchor_divisor must be a positive integer")
    coefficient = symmetric_hyperbola_coefficient(k, lower_divisor, upper_divisor)
    C = reusable_floor_product_cutoff(k)
    product_value = lower_divisor * upper_divisor
    floor_reusable = anchor_divisor * product_value <= C
    if floor_reusable and coefficient == 0 and product_value == 1:
        raise AssertionError("constant pattern cannot vanish")
    return {
        "k": k,
        "lower_divisor": lower_divisor,
        "upper_divisor": upper_divisor,
        "anchor_divisor": anchor_divisor,
        "reusable_floor_product_cutoff": C,
        "pair_product": product_value,
        "symmetric_hyperbola_coefficient": coefficient,
        "retained_by_compiler": coefficient != 0,
        "both_high_quadrant_compiled_away": lower_divisor > C and upper_divisor > C,
        "floor_reusable_product_hyperbola": floor_reusable,
        "boundary_only_by_product": not floor_reusable,
    }


def fixed_total_conductor_parity(k: int, primes: tuple[int, ...]) -> dict[str, object]:
    """Verify the odd-layer annihilation / even-layer Mobius split law for q<=C."""
    normalized = tuple(sorted(int(p) for p in primes))
    if not normalized or len(set(normalized)) != len(normalized):
        raise ValueError("primes must be a nonempty distinct tuple")
    q = prod(normalized)
    C = reusable_floor_product_cutoff(k)
    if q > C:
        raise ValueError("total conductor must lie in the reusable product hyperbola")
    rows: list[dict[str, object]] = []
    split_sum = Fraction(0, 1)
    for size in range(len(normalized) + 1):
        for subset in combinations(normalized, size):
            e = prod(subset, start=1)
            d = q // e
            coeff = symmetric_hyperbola_coefficient(k, e, d)
            mu_e = -1 if size % 2 else 1
            expected = Fraction(0, 1) if len(normalized) % 2 else Fraction(mu_e, 1)
            if coeff != expected:
                raise AssertionError("fixed-conductor parity collapse failed")
            split_sum += coeff
            rows.append({"lower_divisor": e, "upper_divisor": d, "coefficient": coeff})
    if len(normalized) % 2:
        if any(row["coefficient"] != 0 for row in rows):
            raise AssertionError("odd total support retained a reusable symmetric pattern")
    elif q > 1 and split_sum != 0:
        raise AssertionError("even nontrivial conductor retained nonzero complete split bulk")
    return {
        "k": k,
        "total_conductor": q,
        "support_degree": len(normalized),
        "odd_degree_pointwise_zero": len(normalized) % 2 == 1,
        "complete_orientation_split_coefficient_sum": split_sum,
        "zero_complete_split_bulk": split_sum == 0,
        "rows": tuple(rows),
    }


def symmetric_hyperbola_point(k: int, radius: int) -> dict[str, object]:
    """Verify the divisor-hyperbola expansion against one physical mirror radius."""
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")
    lower_support_raw, upper_support_raw = mirror_transverse_supports(k, radius)
    lower_support = tuple(int(p) for p in lower_support_raw)
    upper_support = tuple(int(p) for p in upper_support_raw)
    if set(lower_support).intersection(upper_support):
        raise AssertionError("L043 disjointness failed")
    C = reusable_floor_product_cutoff(k)
    lower_rows = _squarefree_divisors_from_support(lower_support)
    upper_rows = _squarefree_divisors_from_support(upper_support)

    expanded = Fraction(0, 1)
    pattern_rows: list[dict[str, object]] = []
    for e, mu_e in lower_rows:
        for d, mu_d in upper_rows:
            coefficient = Fraction(int(e <= C) * mu_d + int(d <= C) * mu_e, 2)
            expanded += coefficient
            pattern_rows.append(
                {
                    "lower_divisor": e,
                    "upper_divisor": d,
                    "lower_mu": mu_e,
                    "upper_mu": mu_d,
                    "coefficient": coefficient,
                    "pair_product": e * d,
                    "floor_reusable_at_anchor_one": e * d <= C,
                }
            )

    lower_prime = not lower_support
    upper_prime = not upper_support
    direct = Fraction(
        (incidence_optimal_weight(k, lower_support) if upper_prime else 0)
        + (incidence_optimal_weight(k, upper_support) if lower_prime else 0),
        2,
    )
    if expanded != direct:
        raise AssertionError("symmetric hyperbola expansion disagreed with direct detector")
    if any(
        row["coefficient"] != 0 and row["lower_divisor"] > C and row["upper_divisor"] > C
        for row in pattern_rows
    ):
        raise AssertionError("both-high divisor quadrant was not compiled away")
    return {
        "k": k,
        "radius": radius,
        "lower_support": lower_support,
        "upper_support": upper_support,
        "reusable_floor_product_cutoff": C,
        "direct_symmetric_detector": direct,
        "expanded_symmetric_detector": expanded,
        "hyperbola_identity": True,
        "pattern_rows": tuple(pattern_rows),
    }
