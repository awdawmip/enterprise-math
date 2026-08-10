"""Bi-precision product pressure for the P017×P018 Bonferroni bridge.

For one anchor-surviving signed state n=M-x with transverse support P(n), let

    c = |P(n)|,
    E_m(n) = binom(c-1,m)

at a positive odd Bonferroni order m.  The complete transverse core is

    C(n) = product_{p in P(n)} p^v_p(n).

This bridge separates two independent proof-precision axes.

Valuation precision
-------------------
For r>=1 truncate only p-adic depth:

    C_[r](n) = product_{p in P(n)} p^min(v_p(n),r),
    Pi_{m,r} = product_n C_[r](n)^E_m(n).

If H_m^core is the exact number of defect units on rows with C(n)>k-1,
K=k-1 and X=k(k+2)-1, then

    Pi_{m,r} <= K^(T_m-H_m^core) X^H_m^core,

where T_m=sum_n E_m(n).

Support-tail precision
----------------------
For any positive odd tail length ell, define

    U_{m,ell}
      = S_{m+1}-S_{m+2}+...+S_{m+ell}.

Pascal cancellation gives the exact point identity

    sum_{j=m+1}^{m+ell} (-1)^(j-m-1) binom(c,j)
      = binom(c-1,m) + binom(c-1,m+ell),

so every U_{m,ell} is a safe upper bound for T_m.  These upper bounds are not
pointwise monotone as ell grows because the positive remainder can first grow.
The stable adaptive object is therefore the minimum over whatever odd tail
lengths have actually been computed.  Adding another safe candidate can only
lower that minimum.

For one chosen U>=T_m, let h_{m,r}(U) be the least h>=0 satisfying

    Pi_{m,r} <= K^(U-h) X^h.

Then h_{m,r}(U)<=H_m^core, so

    B_m - h_{m,r}(U)

remains a valid composite-support upper majorant.  If it is below the signed
state count, a basin prime is forced.

Fixed-support-order column reconstruction
-----------------------------------------
The p-adic product itself keeps distinct-prime support order fixed at m+1.  For
every transverse prime p,

    alpha_{p,r}
      = sum_{T subset P_perp\{p}, |T|=m}
          sum_{e=1}^r F_surv(p^e product(T)),

and

    Pi_{m,r}=product_p p^alpha_{p,r}.

The valuation refinement quantum is

    Pi_{m,r+1}/Pi_{m,r}
      = product_p p^(sum_T F_surv(p^(r+1) product(T))).

Only primes with p^(r+1)<=X can occur, so every valuation refinement is
localized to one integer-root shell.  Support-tail refinement is separately
localized by the transverse primorial/support-depth geometry.

Negative boundaries / orthogonal witnesses
-------------------------------------------
Independent integer pressure probes deliberately falsified over-compression.

* Valuation boundary: at k=900001 the radical product r=1 still fails even when
  the exact T_3 is used; r=2 repairs that probe.  Therefore valuation precision
  is genuinely independent and cannot always be collapsed to radicals.
* Support boundary: at k=4999996, r=2 with the exact T_3 has positive pressure
  slack (35528 in the independent probe), while the fixed six-moment upper
  U=S4-S5+S6 has negative slack (-1617).  The failure is support truncation,
  not valuation cap 2.  Extending the safe support tail through S8 removes
  almost all of that support remainder without raising valuation precision.

These are finite research probes, not a Legendre proof and not claims about the
first failing scales.  In particular no fixed valuation cap is claimed to be
uniformly sufficient.  The durable result is the two-axis precision calculus,
its exact integer envelope, and its fixed-order divisor-fiber reconstruction.
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


def _require_tail_terms(support_tail_terms: int) -> None:
    if (
        isinstance(support_tail_terms, bool)
        or not isinstance(support_tail_terms, int)
        or support_tail_terms < 1
        or support_tail_terms % 2 == 0
    ):
        raise ValueError("support_tail_terms must be a positive odd integer")


def _choose(n: int, r: int) -> int:
    return comb(n, r) if 0 <= r <= n else 0


def alternating_tail_point_defect_upper(
    support_size: int,
    order: int,
    support_tail_terms: int,
) -> dict[str, int]:
    """Return E_m(c)+the exact positive remainder of one odd tail truncation."""
    _require_order(order)
    _require_tail_terms(support_tail_terms)
    if isinstance(support_size, bool) or not isinstance(support_size, int) or support_size < 0:
        raise ValueError("support_size must be a nonnegative integer")

    c = support_size
    end_order = order + support_tail_terms
    upper = sum(
        _choose(c, degree) if (degree - order - 1) % 2 == 0 else -_choose(c, degree)
        for degree in range(order + 1, end_order + 1)
    )
    defect = _choose(c - 1, order) if c > 0 else 0
    remainder = _choose(c - 1, end_order) if c > 0 else 0
    if upper != defect + remainder:
        raise AssertionError("alternating support-tail defect upper identity failed")
    return {
        "support_size": c,
        "order": order,
        "support_tail_terms": support_tail_terms,
        "support_tail_end_order": end_order,
        "exact_defect": defect,
        "support_tail_upper": upper,
        "upper_remainder": remainder,
    }


def three_term_point_defect_upper(support_size: int, order: int) -> dict[str, int]:
    """Compatibility wrapper for the S_(m+1)-S_(m+2)+S_(m+3) upper."""
    data = alternating_tail_point_defect_upper(support_size, order, 3)
    return {
        "support_size": int(data["support_size"]),
        "order": int(data["order"]),
        "exact_defect": int(data["exact_defect"]),
        "three_term_upper": int(data["support_tail_upper"]),
        "upper_remainder": int(data["upper_remainder"]),
    }


def support_tail_defect_upper_from_moments(
    moments: tuple[int, ...],
    order: int,
    support_tail_terms: int,
) -> int:
    """Return one safe U_{m,ell} from moments S_1,...,S_(m+ell)."""
    _require_order(order)
    _require_tail_terms(support_tail_terms)
    end_order = order + support_tail_terms
    if len(moments) < end_order:
        raise ValueError("moments do not reach the requested support-tail horizon")
    return sum(
        moments[degree - 1]
        if (degree - order - 1) % 2 == 0
        else -moments[degree - 1]
        for degree in range(order + 1, end_order + 1)
    )


def adaptive_support_tail_upper(
    moments: tuple[int, ...],
    order: int,
    candidate_tail_terms: tuple[int, ...],
) -> dict[str, object]:
    """Choose the smallest safe defect upper among declared odd tail horizons."""
    _require_order(order)
    if not candidate_tail_terms:
        raise ValueError("candidate_tail_terms must be nonempty")

    rows: list[dict[str, int]] = []
    best_value: int | None = None
    best_terms: int | None = None
    for terms in candidate_tail_terms:
        _require_tail_terms(terms)
        value = support_tail_defect_upper_from_moments(moments, order, terms)
        rows.append({"support_tail_terms": terms, "defect_upper": value})
        if best_value is None or value < best_value:
            best_value = value
            best_terms = terms

    if best_value is None or best_terms is None:
        raise AssertionError("adaptive support-tail selection lost all candidates")
    return {
        "order": order,
        "candidate_rows": tuple(rows),
        "selected_support_tail_terms": best_terms,
        "selected_defect_upper": best_value,
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
    support_tail_terms: int = 3,
) -> dict[str, object]:
    """Evaluate one point in the support-tail × valuation precision plane."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    _require_order(order)
    _require_cap(valuation_cap)
    _require_tail_terms(support_tail_terms)

    profile = signed_support_profile(k)
    max_moment = order + support_tail_terms
    moments = tuple(
        sum(
            _choose(int(row["support_size"]), degree)
            for row in profile["rows"]
        )
        for degree in range(1, max_moment + 1)
    )
    ordinary = odd_bonferroni_upper_from_moments(moments, order)
    defect_upper = support_tail_defect_upper_from_moments(
        moments,
        order,
        support_tail_terms,
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
        raise AssertionError("support-tail upper fell below exact defect")
    pointwise_upper = sum(
        int(
            alternating_tail_point_defect_upper(
                int(row["support_size"]),
                order,
                support_tail_terms,
            )["support_tail_upper"]
        )
        for row in profile["rows"]
    )
    if pointwise_upper != defect_upper:
        raise AssertionError("moment and pointwise support-tail uppers disagree")

    if k == 2:
        forced_high_exact = 0
        forced_high = 0
    else:
        low = k - 1
        high = k * (k + 2) - 1
        forced_high_exact = _least_envelope_index(
            pressure_product,
            low,
            high,
            exact_defect,
        )
        forced_high = _least_envelope_index(
            pressure_product,
            low,
            high,
            defect_upper,
        )
    if forced_high_exact > actual_high_core or forced_high > actual_high_core:
        raise AssertionError("product pressure exceeded the actual high-core correction")
    if forced_high > forced_high_exact:
        raise AssertionError("using a defect upper unexpectedly strengthened product pressure")

    total = int(profile["signed_state_count"])
    pressure_majorant = ordinary - forced_high
    exact_defect_pressure_majorant = ordinary - forced_high_exact
    return {
        "k": k,
        "order": order,
        "valuation_cap": valuation_cap,
        "support_tail_terms": support_tail_terms,
        "support_tail_end_order": order + support_tail_terms,
        "signed_state_count": total,
        "prime_state_count": int(profile["prime_state_count"]),
        "composite_state_count": int(profile["composite_state_count"]),
        "support_moments": moments,
        "ordinary_bonferroni_sum": ordinary,
        "exact_bonferroni_defect": exact_defect,
        "support_tail_defect_upper": defect_upper,
        "support_tail_overcount": defect_upper - exact_defect,
        "pressure_product": pressure_product,
        "pressure_factor_exponents": tuple(sorted(factor_exponents.items())),
        "forced_high_core_lower_bound_exact_defect": forced_high_exact,
        "forced_high_core_lower_bound": forced_high,
        "support_truncation_pressure_loss": forced_high_exact - forced_high,
        "actual_high_core_correction": actual_high_core,
        "exact_defect_pressure_majorant": exact_defect_pressure_majorant,
        "exact_defect_pressure_certificate": exact_defect_pressure_majorant < total,
        "exact_defect_pressure_slack": total - exact_defect_pressure_majorant,
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
