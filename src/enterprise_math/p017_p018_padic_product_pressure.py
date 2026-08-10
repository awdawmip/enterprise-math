"""Adaptive p-adic product pressure for the P017×P018 Bonferroni bridge.

For one anchor-surviving signed state n=M-x with transverse support P(n), let

    c = |P(n)|,
    E_m(n) = binom(c-1,m)

at a positive odd Bonferroni order m.  The complete transverse core is

    C(n) = product_{p in P(n)} p^v_p(n).

Instead of classifying every complete core against k-1, truncate only the
valuation precision:

    C_[r](n) = product_{p in P(n)} p^min(v_p(n),r),    r>=1.

Define the defect-weighted product

    Pi_{m,r} = product_n C_[r](n)^E_m(n).

If H_m^core is the exact number of Bonferroni defect units carried by rows with
C(n)>k-1, K=k-1 and X=k(k+2)-1, then every low-core defect unit contributes at
most K to Pi_{m,r} and every high-core defect unit contributes at most X.  Hence

    Pi_{m,r} <= K^(T_m-H_m^core) X^H_m^core,

where T_m=sum_n E_m(n).  The three-term support tail

    U_m = S_{m+1}-S_{m+2}+S_{m+3}

is an exact upper bound because pointwise

    C(c,m+1)-C(c,m+2)+C(c,m+3)
      = C(c-1,m) + C(c-1,m+3).

Therefore T_m<=U_m and also

    Pi_{m,r} <= K^(U_m-H_m^core) X^H_m^core.

Let h_{m,r} be the least h>=0 for which

    Pi_{m,r} <= K^(U_m-h) X^h.

Then h_{m,r}<=H_m^core.  Consequently

    B_m - h_{m,r}

is still a valid upper majorant of the composite-support union.  If it is less
than the signed-state count, a basin prime is forced.

The product itself has a fixed-support-order column reconstruction.  For every
transverse prime p,

    alpha_{p,r}
      = sum_{T subset P_perp\{p}, |T|=m}
          sum_{e=1}^r F_surv(p^e product(T)),

and

    Pi_{m,r}=product_p p^alpha_{p,r}.

Thus the support precision stays fixed at m+1 while valuation precision r is an
independent adaptive axis.  The refinement quantum from r to r+1 is

    Pi_{m,r+1}/Pi_{m,r}
      = product_p p^(sum_T F_surv(p^(r+1) product(T))).

Only primes with p^(r+1)<=X can participate, so every valuation refinement is
localized to an integer-root shell.  This is a direct P017 product-pressure ->
P018 root-hierarchy interface.

Important negative boundary from independent integer pressure probes:

* radical-only r=1 is not uniformly sufficient; explicit adversarial probes
  include k=720007,739996,749992,759991,769996 and 900001;
* r=2 repairs those probes but is not uniformly sufficient either: at
  k=4999996 an adversarial no-small-anchor probe had negative r=2 pressure;
* r=3 repaired that same probe.

These are finite research probes, not a Legendre proof and not claims about the
first failing scale.  Their purpose is to falsify over-compression and establish
that valuation precision is genuinely adaptive rather than cosmetic.
"""

from __future__ import annotations

from itertools import combinations
from math import comb, prod

from .legendre import primes_up_to
from .p017_p018_bonferroni_precision import (
    odd_bonferroni_upper_from_moments,
    signed_support_profile,
)
from .p017_p018_core_adaptive_bonferroni import complete_transverse_core
from .p017_p018_signed_boundary_carry import anchor_surviving_divisor_boundary_carry


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def _require_cap(valuation_cap: int) -> None:
    if isinstance(valuation_cap, bool) or not isinstance(valuation_cap, int) or valuation_cap < 1:
        raise ValueError("valuation_cap must be a positive integer")


def _choose(n: int, r: int) -> int:
    return comb(n, r) if 0 <= r <= n else 0


def three_term_point_defect_upper(support_size: int, order: int) -> dict[str, int]:
    """Return E_m(c)+binom(c-1,m+3) by the three next support moments."""
    _require_order(order)
    if isinstance(support_size, bool) or not isinstance(support_size, int) or support_size < 0:
        raise ValueError("support_size must be a nonnegative integer")
    c = support_size
    upper = _choose(c, order + 1) - _choose(c, order + 2) + _choose(c, order + 3)
    defect = _choose(c - 1, order) if c > 0 else 0
    remainder = _choose(c - 1, order + 3) if c > 0 else 0
    if upper != defect + remainder:
        raise AssertionError("three-term defect upper identity failed")
    return {
        "support_size": c,
        "order": order,
        "exact_defect": defect,
        "three_term_upper": upper,
        "upper_remainder": remainder,
    }


def truncated_transverse_core(
    state: int,
    support: tuple[int, ...],
    valuation_cap: int,
) -> int:
    """Return prod p^min(v_p(state),valuation_cap) on the declared support."""
    _require_cap(valuation_cap)
    if isinstance(state, bool) or not isinstance(state, int) or state <= 0:
        raise ValueError("state must be a positive integer")
    normalized = tuple(sorted(int(p) for p in support))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct primes")

    value = 1
    for prime in normalized:
        if prime < 2 or state % prime != 0:
            raise ValueError("every support prime must divide state")
        remaining = state
        depth = 0
        while depth < valuation_cap and remaining % prime == 0:
            remaining //= prime
            value *= prime
            depth += 1
    return value


def _least_envelope_index(
    product_value: int,
    low_base: int,
    high_base: int,
    unit_upper: int,
) -> int:
    """Least h with P<=low_base^(U-h) high_base^h, using integer arithmetic only."""
    if product_value < 1:
        raise ValueError("product_value must be positive")
    if low_base < 1 or high_base < low_base or unit_upper < 0:
        raise ValueError("invalid envelope parameters")
    if unit_upper == 0:
        if product_value != 1:
            raise AssertionError("positive pressure product with zero defect upper")
        return 0

    lo = 0
    hi = unit_upper
    while lo < hi:
        mid = (lo + hi) // 2
        rhs = pow(low_base, unit_upper - mid) * pow(high_base, mid)
        if product_value <= rhs:
            hi = mid
        else:
            lo = mid + 1
    return lo


def padic_product_pressure_profile(
    k: int,
    order: int,
    valuation_cap: int,
) -> dict[str, object]:
    """Evaluate the exact row product and its safe high-core pressure lower bound."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)
    _require_cap(valuation_cap)

    profile = signed_support_profile(k)
    max_moment = order + 3
    moments = tuple(
        sum(
            _choose(int(row["support_size"]), degree)
            for row in profile["rows"]
        )
        for degree in range(1, max_moment + 1)
    )
    ordinary = odd_bonferroni_upper_from_moments(moments, order)
    defect_upper = (
        moments[order]
        - moments[order + 1]
        + moments[order + 2]
    )

    pressure_product = 1
    exact_defect = 0
    actual_high_core = 0
    factor_exponents: dict[int, int] = {}
    for row in profile["rows"]:
        support = tuple(int(p) for p in row["support"])
        c = len(support)
        defect = _choose(c - 1, order) if c > 0 else 0
        exact_defect += defect
        if defect == 0:
            continue

        state = int(row["state"])
        capped = truncated_transverse_core(state, support, valuation_cap)
        pressure_product *= pow(capped, defect)

        for prime in support:
            remaining = state
            depth = 0
            while depth < valuation_cap and remaining % prime == 0:
                remaining //= prime
                depth += 1
            factor_exponents[prime] = factor_exponents.get(prime, 0) + defect * depth

        if complete_transverse_core(state, support) > k - 1:
            actual_high_core += defect

    if defect_upper < exact_defect:
        raise AssertionError("three-term defect upper fell below exact defect")
    pointwise_upper = sum(
        three_term_point_defect_upper(int(row["support_size"]), order)["three_term_upper"]
        for row in profile["rows"]
    )
    if pointwise_upper != defect_upper:
        raise AssertionError("moment and pointwise three-term defect uppers disagree")

    if k == 2:
        forced_high = 0
    else:
        forced_high = _least_envelope_index(
            pressure_product,
            k - 1,
            k * (k + 2) - 1,
            defect_upper,
        )
    if forced_high > actual_high_core:
        raise AssertionError("product pressure exceeded the actual high-core correction")

    total = int(profile["signed_state_count"])
    pressure_majorant = ordinary - forced_high
    return {
        "k": k,
        "order": order,
        "valuation_cap": valuation_cap,
        "signed_state_count": total,
        "prime_state_count": int(profile["prime_state_count"]),
        "composite_state_count": int(profile["composite_state_count"]),
        "support_moments": moments,
        "ordinary_bonferroni_sum": ordinary,
        "exact_bonferroni_defect": exact_defect,
        "three_term_defect_upper": defect_upper,
        "pressure_product": pressure_product,
        "pressure_factor_exponents": tuple(sorted(factor_exponents.items())),
        "forced_high_core_lower_bound": forced_high,
        "actual_high_core_correction": actual_high_core,
        "pressure_majorant": pressure_majorant,
        "pressure_certificate": pressure_majorant < total,
        "pressure_slack": total - pressure_majorant,
    }


def column_pressure_factor_exponents(
    k: int,
    order: int,
    valuation_cap: int,
) -> tuple[tuple[int, int], ...]:
    """Reconstruct Pi_{m,r} prime exponents from fixed-order divisor fibers.

    This is a bounded executable reference.  The theorem is the finite double
    count; large-scale use should aggregate the same fibers rather than naively
    enumerate every selected prime tuple.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)
    _require_cap(valuation_cap)

    center = k * (k + 1)
    transverse = tuple(
        p for p in primes_up_to(k)
        if p % 2 == 1 and center % p != 0
    )
    exponents: dict[int, int] = {p: 0 for p in transverse}

    for selected in combinations(transverse, order + 1):
        selected_product = prod(selected)
        for prime in selected:
            other_product = selected_product // prime
            power = 1
            for _depth in range(1, valuation_cap + 1):
                power *= prime
                divisor = power * other_product
                fiber = anchor_surviving_divisor_boundary_carry(k, divisor)
                exponents[prime] += int(fiber["anchor_surviving_fiber_size"])

    return tuple(sorted((prime, exponent) for prime, exponent in exponents.items() if exponent))


def verify_row_column_pressure_identity(
    k: int,
    order: int,
    valuation_cap: int,
) -> dict[str, object]:
    """Cross-check the row product against the fixed-order divisor-fiber columns."""
    row = padic_product_pressure_profile(k, order, valuation_cap)
    column = column_pressure_factor_exponents(k, order, valuation_cap)
    if tuple(row["pressure_factor_exponents"]) != column:
        raise AssertionError("p-adic product pressure row/column identity failed")
    return {
        "k": k,
        "order": order,
        "valuation_cap": valuation_cap,
        "factor_exponents": column,
        "row_column_identity": True,
    }
