#!/usr/bin/env python3
"""R005-A two-dimensional observation-arity / collapse-dimension phase diagram.

For p-power basins A=k^p, U=(k+1)^p-1, and an m-th-root forced observation core q<=U^(1/m), m>=2, the worst cofactor scale is x~k^(p(m-1)/m), while the available cofactor interval has length ~x/k. Therefore the short-prime exponent needed to force the whole m-root core is

lambda(p,m)=1-m/[p(m-1)].

Interpretation: m=2 full forcing; m=3 unique least basis; m>=4 residual Omega<=m-1 by T-A21. Compare with Baker-Harman-Pintz theta=0.525=21/40.
"""

from __future__ import annotations
from fractions import Fraction
import json

BHP = Fraction(21, 40)


def lam(p: int, m: int) -> Fraction:
    if p < 2 or m < 2:
        raise ValueError("p,m must be >=2")
    return Fraction(1, 1) - Fraction(m, p * (m - 1))


def role(m: int) -> str:
    if m == 2:
        return "full_forcing"
    if m == 3:
        return "unique_least_basis"
    return f"residual_Omega_at_most_{m-1}"


def main() -> None:
    rows = []
    for p in range(2, 11):
        for m in range(2, 11):
            x = lam(p, m)
            rows.append({
                "p": p,
                "m": m,
                "role": role(m),
                "lambda": f"{x.numerator}/{x.denominator}",
                "lambda_decimal": float(x),
                "bhp_suffices_asymptotically": x > BHP,
            })

    assert all(not (lam(2, m) > BHP) for m in range(2, 500))
    assert lam(2, 10_000) < Fraction(1, 2) < BHP
    assert not (lam(3, 2) > BHP)
    assert not (lam(3, 3) > BHP)
    assert all(lam(3, m) > BHP for m in range(4, 500))
    assert not (lam(4, 2) > BHP)
    assert all(lam(4, m) > BHP for m in range(3, 500))
    assert all(lam(p, m) > BHP for p in range(5, 100) for m in range(2, 100))

    assert lam(2, 3) == Fraction(1, 4)
    assert lam(3, 3) == Fraction(1, 2)
    assert lam(4, 3) == Fraction(5, 8)
    assert lam(4, 2) == Fraction(1, 2)
    assert lam(5, 2) == Fraction(3, 5)
    assert lam(3, 4) == Fraction(5, 9)

    result = {
        "status": "R005-A TWO-DIMENSIONAL OBSERVATION-ARITY PHASE DIAGRAM",
        "formula": "lambda(p,m)=1-m/[p(m-1)]",
        "BHP_theta": "21/40",
        "condition": "lambda(p,m)>21/40 iff p>40m/[19(m-1)]",
        "phase": {
            "p=2": {"BHP_controlled_finite_m": "none", "limit_as_m_to_infinity": "1/2 < 21/40"},
            "p=3": {"BHP_controlled_m": "m>=4", "critical_m3": "lambda(3,3)=1/2"},
            "p=4": {"BHP_controlled_m": "m>=3", "critical_m2": "lambda(4,2)=1/2"},
            "p>=5": {"BHP_controlled_m": "all m>=2"},
        },
        "selected_rows": [row for row in rows if (row["p"], row["m"]) in {(2,2),(2,3),(2,4),(2,8),(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(5,2),(5,3)}],
        "T_A21_interpretation": "for m>=3, if every candidate q<=floor(U^(1/m)) is forced, then every residual composite has Omega<=m-1",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
