#!/usr/bin/env python3
"""Verifier for EM-FREE-F6D046 cross-signature first-jet orbit analysis.

Checks exact singular-value arithmetic, both Ramanujan series, an explicit
first-jet arrow, and rank-2/rank-3 quadratic pullback obstructions.
Only Python's standard library is used.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from math import gcd
import json
from typing import Iterable

getcontext().prec = 120
D = Decimal
TOL = D("1e-95")


def dfrac(x: Fraction) -> Decimal:
    return D(x.numerator) / D(x.denominator)


def gauss_legendre_pi(iterations: int = 9) -> Decimal:
    a = D(1)
    b = D(1) / D(2).sqrt()
    t = D(1) / D(4)
    p = D(1)
    for _ in range(iterations):
        an = (a + b) / D(2)
        b = (a * b).sqrt()
        t = t - p * (a - an) * (a - an)
        a = an
        p *= D(2)
    return (a + b) * (a + b) / (D(4) * t)


def hyper3f2_theta(a: Fraction, z: Fraction, max_terms: int = 10000) -> tuple[Decimal, Decimal, int]:
    """Return F_a(z), Theta F_a(z), and the number of terms used."""
    ad = dfrac(a)
    zd = dfrac(z)
    term = D(1)
    total = D(1)
    theta_total = D(0)
    threshold = D("1e-112")
    for n in range(1, max_terms + 1):
        k = D(n - 1)
        nd = D(n)
        term *= (
            (k + D(1) / D(2))
            * (k + ad)
            * (k + D(1) - ad)
            / (nd * nd * nd)
            * zd
        )
        total += term
        theta_total += nd * term
        if abs(term) < threshold:
            return total, theta_total, n + 1
    raise RuntimeError("hypergeometric series failed to converge")


def mod_one(x: Fraction) -> Fraction:
    q = x.numerator // x.denominator
    r = x - q
    return r + 1 if r < 0 else r


def root_of_unity_order(delta: Fraction) -> int:
    r = mod_one(delta)
    return 1 if r == 0 else r.denominator


def powered_order(order: int, ramification: int) -> int:
    return order // gcd(order, ramification)


def odd_part(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n


def pairwise_projective_orders(exponents: Iterable[Fraction], ramification: int = 1) -> list[int]:
    xs = list(exponents)
    orders: list[int] = []
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            orders.append(root_of_unity_order(ramification * (xs[j] - xs[i])))
    return sorted(orders)


# Standard formulas.
a2 = Fraction(1, 4)
z2 = Fraction(1, 99**4)
A2_J = Fraction(2206, 9801)
B2_J = Fraction(52780, 9801)

a3 = Fraction(1, 3)
z3 = Fraction(-1, 500**2)
A3_J = Fraction(827, 3000)
B3_J = Fraction(14151, 3000)

checks: dict[str, bool] = {}
checks["level2_pell_identity"] = 9801**2 - 29 * 1820**2 == 1
checks["level2_singular_value_exact"] = (
    Fraction(1, 1) - Fraction(29 * 1820**2, 9801**2) == z2
)
checks["level3_norm_identity"] = 4 * 53**2 * 89 == 1_000_004
checks["level3_singular_value_exact"] = (
    Fraction(1, 1) - Fraction(4 * 53**2 * 89, 1000**2) == z3
)

F2, Th2, terms2 = hyper3f2_theta(a2, z2)
F3, Th3, terms3 = hyper3f2_theta(a3, z3)
pi = gauss_legendre_pi()
sqrt2 = D(2).sqrt()
sqrt3 = D(3).sqrt()
invpi = D(1) / pi

# Wronskian normalization J_a=sin(pi*a)/pi.
J2 = dfrac(A2_J) * F2 + dfrac(B2_J) * Th2
J3 = dfrac(A3_J) * F3 + dfrac(B3_J) * Th3
J2_target = sqrt2 / (D(2) * pi)
J3_target = sqrt3 / (D(2) * pi)
checks["level2_wronskian_normalization"] = abs(J2 - J2_target) < TOL
checks["level3_wronskian_normalization"] = abs(J3 - J3_target) < TOL

# Common 1/pi normalization.
A2_pi = sqrt2 * dfrac(A2_J)
B2_pi = sqrt2 * dfrac(B2_J)
A3_pi = dfrac(Fraction(827, 1500)) / sqrt3
B3_pi = dfrac(Fraction(14151, 1500)) / sqrt3
value2_pi = A2_pi * F2 + B2_pi * Th2
value3_pi = A3_pi * F3 + B3_pi * Th3
checks["level2_inverse_pi_normalization"] = abs(value2_pi - invpi) < TOL
checks["level3_inverse_pi_normalization"] = abs(value3_pi - invpi) < TOL

# Explicit local analytic first-jet arrow from level 2 to level 3.
g0 = F2 / F3
kappa0 = B3_pi / (B2_pi * g0)
phi_prime0 = dfrac(z2) / (dfrac(z3) * kappa0)
theta_g0 = Th2 / (kappa0 * F3) - g0 * Th3 / F3
lower_left = kappa0 * theta_g0
lower_right = kappa0 * g0
mapped_A3 = A2_pi * g0 + B2_pi * lower_left
mapped_B3 = B2_pi * lower_right
checks["first_jet_arrow_is_invertible"] = abs(g0 * lower_right) > D("1e-20")
checks["first_jet_arrow_maps_A"] = abs(mapped_A3 - A3_pi) < TOL
checks["first_jet_arrow_maps_B"] = abs(mapped_B3 - B3_pi) < TOL
checks["first_jet_arrow_coordinate_derivative_nonzero"] = abs(phi_prime0) > D("1e-20")

# Rank-2 period local-system invariant.
delta2 = Fraction(1, 1) - 2 * a2
delta3 = Fraction(1, 1) - 2 * a3
order2 = root_of_unity_order(delta2)
order3 = root_of_unity_order(delta3)
checks["rank2_level2_projective_order"] = order2 == 2
checks["rank2_level3_projective_order"] = order3 == 3
checks["quadratic_direct_order_sets_disjoint"] = (
    {powered_order(order2, e) for e in (1, 2)}
    .isdisjoint({powered_order(order3, e) for e in (1, 2)})
)
checks["quadratic_chain_odd_part_separates"] = odd_part(order2) != odd_part(order3)

# Rank-3 Clausen/hypergeometric regression.
exp0 = [Fraction(0), Fraction(0), Fraction(0)]
exp1 = [Fraction(0), Fraction(1, 2), Fraction(1)]
expinf2 = [a2, Fraction(1, 2), 1 - a2]
expinf3 = [a3, Fraction(1, 2), 1 - a3]
rank3_inf2 = pairwise_projective_orders(expinf2)
rank3_inf3 = pairwise_projective_orders(expinf3)
checks["rank3_level2_infinity_orders"] = rank3_inf2 == [2, 4, 4]
checks["rank3_level3_infinity_orders"] = rank3_inf3 == [3, 6, 6]
source2_quadratic_local_types = {
    tuple(pairwise_projective_orders(exps, e))
    for exps in (exp0, exp1, expinf2)
    for e in (1, 2)
}
source3_quadratic_local_types = {
    tuple(pairwise_projective_orders(exps, e))
    for exps in (exp0, exp1, expinf3)
    for e in (1, 2)
}
checks["rank3_no_quadratic_pullback_2_to_3"] = tuple(rank3_inf3) not in source2_quadratic_local_types
checks["rank3_no_quadratic_pullback_3_to_2"] = tuple(rank3_inf2) not in source3_quadratic_local_types

result = {
    "schema": "EM_FREE_F6D046_CROSS_SIGNATURE_JET_ORBIT_VERIFICATION_V1",
    "researcher_id": "EM-FREE-F6D046",
    "parent_candidate_id": "EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN",
    "research_unit": "CROSS_SIGNATURE_FIRST_JET_ORBIT_COLLAPSE",
    "all_passed": all(checks.values()),
    "checks": checks,
    "exact": {
        "level2": {
            "a": str(a2), "z": str(z2),
            "wronskian_covector": [str(A2_J), str(B2_J)],
            "rank2_exponent_difference_infinity": str(delta2),
            "projective_monodromy_order": order2,
            "quadratic_odd_part": odd_part(order2),
            "rank3_pairwise_projective_orders_infinity": rank3_inf2,
        },
        "level3": {
            "a": str(a3), "z": str(z3),
            "wronskian_covector": [str(A3_J), str(B3_J)],
            "rank2_exponent_difference_infinity": str(delta3),
            "projective_monodromy_order": order3,
            "quadratic_odd_part": odd_part(order3),
            "rank3_pairwise_projective_orders_infinity": rank3_inf3,
        },
        "source2_quadratic_local_types": sorted([list(x) for x in source2_quadratic_local_types]),
        "source3_quadratic_local_types": sorted([list(x) for x in source3_quadratic_local_types]),
    },
    "numeric": {
        "pi": str(pi), "inverse_pi": str(invpi),
        "level2": {
            "terms_used": terms2, "F": str(F2), "ThetaF": str(Th2),
            "J_value": str(J2), "J_target": str(J2_target),
            "inverse_pi_value": str(value2_pi),
            "inverse_pi_covector": [str(A2_pi), str(B2_pi)],
        },
        "level3": {
            "terms_used": terms3, "F": str(F3), "ThetaF": str(Th3),
            "J_value": str(J3), "J_target": str(J3_target),
            "inverse_pi_value": str(value3_pi),
            "inverse_pi_covector": [str(A3_pi), str(B3_pi)],
        },
        "explicit_first_jet_arrow_level2_to_level3": {
            "g0": str(g0), "kappa0": str(kappa0), "theta_g0": str(theta_g0),
            "T": [[str(g0), "0"], [str(lower_left), str(lower_right)]],
            "phi_prime0": str(phi_prime0),
            "mapped_covector": [str(mapped_A3), str(mapped_B3)],
            "target_covector": [str(A3_pi), str(B3_pi)],
            "A_residual": str(mapped_A3 - A3_pi),
            "B_residual": str(mapped_B3 - B3_pi),
        },
    },
    "verdict": {
        "unrestricted_first_jet_groupoid": "SINGLE_DERIVATIVE_BEARING_ORBIT_AT_FIXED_NONZERO_SCALAR",
        "quadratic_equation_enriched_groupoid": "LEVEL2_AND_LEVEL3_SEPARATED_BY_ODD_PROJECTIVE_MONODROMY_ORDER",
        "axiom_status": "DERIVED_NO_GO_NOT_AXIOM",
    },
}

print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if result["all_passed"] else 1)
