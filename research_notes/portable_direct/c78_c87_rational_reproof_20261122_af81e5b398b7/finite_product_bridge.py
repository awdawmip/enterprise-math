"""Finite rational replacement for the C78 Gamma-ratio normalization.

For k in {1,3,5}, prove the one-step sign and cubic error by exact
nonnegative polynomial coefficients, then verify sample finite products.
The general finite-product proof is in FINITE_PRODUCT_BOUND.md.
"""
from fractions import Fraction as Q
from math import prod
import json
from pathlib import Path


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def scale(a, n):
    return trim([n*v for v in a])


def mul(a, b):
    c = [0] * (len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i+j] += u*v
    return trim(c)


def power(a, n):
    out = [1]
    for _ in range(n):
        out = mul(out, a)
    return out


def sign_certificate(k):
    """All polynomials use y=j-1, so y>=0 at every actual step."""
    p = 3*k
    signed = 1 if k == 1 else -1
    magnitude = abs(k*(16-9*k*k))
    # 8j+2k, 8j+8k, 8j+5k+4, 8j+5k-4, with j=y+1.
    numerator = mul(power([8+2*k, 8], 4), power([12+5*k, 8], p))
    denominator = mul(power([8+8*k, 8], 4), power([4+5*k, 8], p))
    positive_difference = scale(add(numerator, scale(denominator, -1)), signed)
    majorant = scale(mul(power([8+8*k, 8], 4),
                        power([4+5*k, 8], p-3)), 8*magnitude)
    positive_slack = add(majorant, scale(positive_difference, -1))
    assert all(v >= 0 for v in positive_difference)
    assert all(v >= 0 for v in positive_slack)
    assert positive_difference[0] > 0
    assert positive_slack[0] > 0
    return {
        "k": k, "variable": "y=j-1>=0",
        "sign": signed, "C": str(Q(magnitude, 64)),
        "sign_polynomial_coefficients_low_to_high": positive_difference,
        "bound_slack_coefficients_low_to_high": positive_slack,
        "all_coefficients_nonnegative": True,
    }


def eta(k):
    return Q(5*k+4, 8)


def error_budget(k, m, n):
    """0<=m<=n; all rational, including m=0 and n=m."""
    c = Q(abs(k*(16-9*k*k)), 64)
    d = Q(5*k, 8)
    return c/2 * (1/(m+d)**2 - 1/(n+d)**2)


def ratio_fourth_bounds(k, m, n):
    e = error_budget(k, m, n)
    model = ((m+eta(k))/(n+eta(k)))**(3*k)
    if k == 1:
        return model, model/(1-e)
    return model*(1-e), model


def prefix_table(k, n):
    row = [Q(1)]
    for j in range(1, n+1):
        row.append(row[-1]*Q(4*j+k, 4*(j+k)))
    return row


def run_checks():
    certificates = [sign_certificate(k) for k in (1, 3, 5)]
    checked = 0
    for k in (1, 3, 5):
        fs = prefix_table(k, 64)
        for m in range(65):
            for n in range(m, 65):
                value = (fs[n]/fs[m])**4
                lo, hi = ratio_fourth_bounds(k, m, n)
                assert lo <= value <= hi
                assert 0 <= error_budget(k, m, n) < 1
                checked += 1
    budgets = []
    for k in (1, 3, 5):
        for m, n in ((0, 1), (2, 64), (10, 11), (10, 20),
                     (100, 101), (100, 200), (1000, 1001),
                     (1000, 2000), (10**6, 10**6+1)):
            e = error_budget(k, m, n)
            budgets.append({"k": k, "m": m, "n": n, "E": str(e)})
    return {
        "arithmetic": "Python arbitrary-precision integers and fractions.Fraction",
        "universal_polynomial_certificates": certificates,
        "finite_product_checks": {
            "scope": "k=1,3,5; every integer 0<=m<=n<=64",
            "count": checked, "failures": 0,
        },
        "sample_error_budgets": budgets,
        "proof_status": "Author-side finite algebra; no formal or independent admission",
    }


if __name__ == "__main__":
    result = run_checks()
    path = Path(__file__).with_name("finite_product_checks.json")
    path.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({
        "certificate_count": len(result["universal_polynomial_certificates"]),
        "finite_checks": result["finite_product_checks"],
        "saved": str(path),
    }, indent=2))

