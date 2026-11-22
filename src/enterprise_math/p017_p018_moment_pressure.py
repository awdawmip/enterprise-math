"""Adaptive logarithmic-moment pressure for the P017×P018 core bridge.

Fix an odd Bonferroni order m.  For one anchor-surviving signed state n=M-x,
let

    E_m(n)=binom(c(n)-1,m)

be its exact point defect and let C_[r](n) be the transverse small-prime core
with each p-adic valuation capped at r>=1.  Write

    y_[r](n)=log C_[r](n),
    a=log(k-1),
    b=log(k(k+2)-1).

Low complete-core rows have C(n)<=k-1, hence y_[r](n)<=a.  High complete-core
rows have C(n)>k-1 and y_[r](n)<=b.  Therefore for every integer d>=1,

    P_d(y)=(y/b)^(d-1) (y-a)/(b-a)

satisfies P_d(y)<=0 on the low region and P_d(y)<=1 on the high region.
Consequently

    H_m^core >= h_(m,r,d)

with

    h_(m,r,d)
      = [M_(d,r)-a M_(d-1,r)] / [b^(d-1)(b-a)],

where

    M_(j,r)=sum_n E_m(n) y_[r](n)^j,
    M_(0,r)=sum_n E_m(n).

This strictly contains the scalar product-pressure bridge: d=1 is exactly the
logarithm of the defect-weighted product.  Higher d suppress the negative cost
of very small low cores while retaining almost unit weight on high cores,
because P017 full-core dichotomy puts every high core at the basin state itself:

    C(n)=n in [k^2+1, k(k+2)-1].

No degree is declared universally best.  Each d is an independently safe lower
bound, so the stable adaptive object is the maximum over the finite degrees
actually computed.

The hierarchy remains a finite divisor-fiber observable.  Expand

    y_[r](n)=sum_(p transverse) sum_(1<=e<=r) log(p) 1_(p^e|n).

For an ordered d-tuple of prime-power level atoms a_i=(p_i,e_i), distinguish
p_1.  The identity E_m(n)=#{m-subsets of support(n)\{p_1}} gives

    M_(d,r)
      = sum_(a_1,...,a_d) prod_i log(p_i)
          sum_(T subset P_perp\{p_1}, |T|=m)
            F_surv(lcm(p_1^e1,...,p_d^ed, prod(T))).

Thus degree d needs at most m+d distinct transverse support directions; repeated
moment primes do not increase that bound.  Valuation precision r and moment
degree d are separate proof coordinates, and every required column is an exact
P017 anchor-surviving divisor fiber already represented by the boundary-carry
layer.

A useful deterministic gap envelope follows from the spectral separation.  Put

    c0=log(k^2+1).

For d>=2, the largest magnitude of -P_d on 0<=y<=a is

    L_d = a^d (d-1)^(d-1) / [d^d b^(d-1)(b-a)],

while the minimum P_d on the high interval c0<=y<=b is

    G_d = (c0/b)^(d-1) (c0-a)/(b-a).

If R is the low-core defect mass and H the high-core defect mass, then

    0 <= H-h_(m,r,d) <= H(1-G_d)+R L_d

when r is deep enough that y_[r]=log C on the rows under consideration.  This
explains why moderate degree can recover most information lost by a single
global geometric mean: L_d decays rapidly while c0/b is extremely close to 1.

Finite independent pressure probes (not theorem ranges):

* k=12,500,002, exact support and full valuation: d=1 has slack about -25,310,
  d=2 about +39,772, while exact core-adaptive slack is about +79,068;
* k=15,000,016: d=2 about -16,120, d=3 about +14,632;
* k=19,999,996: d=3 about -10,268, d=4 about +5,579.

These probes establish an adaptive degree axis and a negative boundary for the
single-scalar product compression.  They do not prove Legendre's conjecture and
do not claim the displayed probes are first failures.
"""

from __future__ import annotations

from itertools import combinations, product
from math import comb, lcm, log, prod

from .legendre import primes_up_to
from .p017_p018_bonferroni_precision import (
    odd_bonferroni_upper_from_moments,
    signed_support_profile,
)
from .p017_p018_signed_boundary_carry import anchor_surviving_divisor_boundary_carry


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def _require_cap(valuation_cap: int) -> None:
    if isinstance(valuation_cap, bool) or not isinstance(valuation_cap, int) or valuation_cap < 1:
        raise ValueError("valuation_cap must be a positive integer")


def _require_degree(degree: int) -> None:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")


def _choose(n: int, r: int) -> int:
    return comb(n, r) if 0 <= r <= n else 0


def capped_log_core(state: int, support: tuple[int, ...], valuation_cap: int) -> float:
    """Return log(prod p^min(v_p(state),valuation_cap))."""
    _require_cap(valuation_cap)
    value = 0.0
    for prime in support:
        remaining = state
        depth = 0
        while depth < valuation_cap and remaining % prime == 0:
            remaining //= prime
            value += log(prime)
            depth += 1
    return value


def pressure_polynomial_value(y: float, a: float, b: float, degree: int) -> float:
    """Evaluate the degree-d safe threshold minorant P_d."""
    _require_degree(degree)
    if not (0.0 <= y <= b + 1e-12) or not (0.0 < a < b):
        raise ValueError("require 0<=y<=b and 0<a<b")
    return (y / b) ** (degree - 1) * (y - a) / (b - a)


def moment_pressure_profile(
    k: int,
    order: int,
    valuation_cap: int,
    max_degree: int,
) -> dict[str, object]:
    """Evaluate row moments and all safe degree bounds through max_degree."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    _require_order(order)
    _require_cap(valuation_cap)
    _require_degree(max_degree)

    profile = signed_support_profile(k)
    support_moments = tuple(
        sum(_choose(int(row["support_size"]), j) for row in profile["rows"])
        for j in range(1, order + 1)
    )
    ordinary = odd_bonferroni_upper_from_moments(support_moments, order)

    defect_weights: list[int] = []
    y_rows: list[float] = []
    for row in profile["rows"]:
        c = int(row["support_size"])
        defect = _choose(c - 1, order) if c > 0 else 0
        if defect == 0:
            continue
        support = tuple(int(p) for p in row["support"])
        defect_weights.append(defect)
        y_rows.append(capped_log_core(int(row["state"]), support, valuation_cap))

    moments = [float(sum(defect_weights))]
    for degree in range(1, max_degree + 1):
        moments.append(
            sum(weight * (y**degree) for weight, y in zip(defect_weights, y_rows))
        )

    a = log(k - 1)
    b = log(k * (k + 2) - 1)
    rows: list[dict[str, float | int | bool]] = []
    best = 0.0
    best_degree = 1
    total = int(profile["signed_state_count"])
    for degree in range(1, max_degree + 1):
        bound = (moments[degree] - a * moments[degree - 1]) / (
            (b ** (degree - 1)) * (b - a)
        )
        safe = max(0.0, bound)
        if safe > best:
            best = safe
            best_degree = degree
        majorant = ordinary - safe
        rows.append(
            {
                "degree": degree,
                "raw_high_core_lower_bound": bound,
                "safe_high_core_lower_bound": safe,
                "pressure_majorant": majorant,
                "pressure_slack": total - majorant,
                "pressure_certificate": majorant < total,
            }
        )

    return {
        "k": k,
        "order": order,
        "valuation_cap": valuation_cap,
        "max_degree": max_degree,
        "signed_state_count": total,
        "ordinary_bonferroni_sum": ordinary,
        "defect_moments": tuple(moments),
        "degree_rows": tuple(rows),
        "selected_degree": best_degree,
        "selected_high_core_lower_bound": best,
        "adaptive_pressure_majorant": ordinary - best,
        "adaptive_pressure_certificate": ordinary - best < total,
        "adaptive_pressure_slack": total - (ordinary - best),
    }


def full_core_gap_envelope(k: int, degree: int) -> dict[str, float | int]:
    """Return the deterministic low/high loss factors for full valuation."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    _require_degree(degree)
    a = log(k - 1)
    b = log(k * (k + 2) - 1)
    c0 = log(k * k + 1)
    if degree == 1:
        low_loss = a / (b - a)
    else:
        low_loss = (
            (a**degree)
            * ((degree - 1) ** (degree - 1))
            / ((degree**degree) * (b ** (degree - 1)) * (b - a))
        )
    high_floor = (c0 / b) ** (degree - 1) * (c0 - a) / (b - a)
    return {
        "k": k,
        "degree": degree,
        "low_negative_magnitude_ceiling": low_loss,
        "high_positive_floor": high_floor,
        "high_loss_ceiling_per_unit": 1.0 - high_floor,
    }


def _transverse_level_atoms(k: int, valuation_cap: int) -> tuple[tuple[int, int, int, float], ...]:
    center = k * (k + 1)
    xmax = k * (k + 2) - 1
    atoms: list[tuple[int, int, int, float]] = []
    for prime in primes_up_to(k):
        if prime == 2 or center % prime == 0:
            continue
        power_value = 1
        for exponent in range(1, valuation_cap + 1):
            power_value *= prime
            if power_value > xmax:
                break
            atoms.append((prime, exponent, power_value, log(prime)))
    return tuple(atoms)


def column_log_moment(
    k: int,
    order: int,
    valuation_cap: int,
    degree: int,
) -> float:
    """Bounded exact-column reconstruction of M_(degree,r), using float log weights.

    This is intentionally a small-scale executable reference; the finite double
    count is the theorem.  The union of required distinct support primes is at
    most order+degree.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    _require_order(order)
    _require_cap(valuation_cap)
    _require_degree(degree)

    center = k * (k + 1)
    transverse = tuple(
        p for p in primes_up_to(k) if p != 2 and center % p != 0
    )
    atoms = _transverse_level_atoms(k, valuation_cap)
    fiber_cache: dict[int, int] = {}

    def fiber(divisor: int) -> int:
        if divisor not in fiber_cache:
            fiber_cache[divisor] = int(
                anchor_surviving_divisor_boundary_carry(k, divisor)[
                    "anchor_surviving_fiber_size"
                ]
            )
        return fiber_cache[divisor]

    total = 0.0
    for atom_tuple in product(atoms, repeat=degree):
        first_prime = atom_tuple[0][0]
        base_lcm = 1
        weight = 1.0
        for _, _, power_value, log_weight in atom_tuple:
            base_lcm = lcm(base_lcm, power_value)
            weight *= log_weight
        others = tuple(p for p in transverse if p != first_prime)
        for selected in combinations(others, order):
            divisor = base_lcm
            for prime in selected:
                divisor = lcm(divisor, prime)
            total += weight * fiber(divisor)
    return total


def verify_row_column_moment_identity(
    k: int,
    order: int,
    valuation_cap: int,
    degree: int,
    tolerance: float = 1e-8,
) -> dict[str, object]:
    """Cross-check one bounded row moment against its divisor-fiber expansion."""
    row = moment_pressure_profile(k, order, valuation_cap, degree)
    row_moment = float(row["defect_moments"][degree])
    column_moment = column_log_moment(k, order, valuation_cap, degree)
    scale = max(1.0, abs(row_moment), abs(column_moment))
    if abs(row_moment - column_moment) > tolerance * scale:
        raise AssertionError("log-moment row/column reconstruction failed")
    return {
        "k": k,
        "order": order,
        "valuation_cap": valuation_cap,
        "degree": degree,
        "row_moment": row_moment,
        "column_moment": column_moment,
        "row_column_identity": True,
    }
