#!/usr/bin/env python3
"""R749STG: exact all-future monotone conditioning certificate.

The six-residue quasipolynomials follow algebraically from the generating
functions, not from interpolation or sampled observation values.
Dependencies: Python 3 and SymPy. This script produces the companion JSON.
"""
import json
from math import factorial
from pathlib import Path
import sympy as s

N = s.Symbol("N")
J = s.Symbol("J")
WEIGHTS = (1, 1, 2, 3, 6)

def convolution(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i + j] += x * y
    return z

def block_numerator(ws):
    v = [1]
    for w in ws:
        assert 6 % w == 0
        v = convolution(v, [int(k % w == 0) for k in range(7 - w)])
    return v

def binom_poly(x, k):
    return s.prod(x - i for i in range(k)) / factorial(k)

# sum_{n>=1} C_n*z^(n-1) = QC(z)/(1-z^6)^6;
# sum_{n>=1} T_n*z^(n-1) = QT(z)/(1-z^6)^7.
# T marks the first weight-1 source via z/(1-z)^2.
QC = block_numerator((*WEIGHTS, 1))
QT = convolution([0, 1], block_numerator((1, 1, 1, 1, 2, 3, 6)))
assert len(QC) == 23 and len(QT) == 29
assert sum(QC) == 1296 and sum(QT) == 7776

def quasipolys(residue):
    c = sum((a * binom_poly((N - 1 - i) / 6 + 5, 5)
             for i, a in enumerate(QC) if (residue - 1 - i) % 6 == 0),
            s.Integer(0))
    t = sum((a * binom_poly((N - 1 - i) / 6 + 6, 6)
             for i, a in enumerate(QT) if (residue - 1 - i) % 6 == 0),
            s.Integer(0))
    return s.Poly(c, N), s.Poly(t, N)

# Separate integer recurrence checks at boundary indices.
M = 110
part = [0] * (M + 1)
part[0] = 1
for w in WEIGHTS:
    for k in range(w, M + 1):
        part[k] += part[k - w]
C = [0] * (M + 1)
T = [0] * (M + 1)
for k in range(1, M + 1):
    C[k] = C[k - 1] + part[k - 1]
    T[k] = T[k - 1] + C[k - 1]

result = {
    "unit": "R749STG",
    "status": "AUTHOR_EXACT_NOT_REVIEWED",
    "frozen_science": "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "dependency": "R749STF@eaca9aaec9f2b38d0e66f6283454e307e8704860",
    "predecessor_analytic_collision": "R749STB@d2a4436f4ed42aba25a54f9b7015e4c4a776c944 (reused, not rechecked)",
    "new_bound": "q in {73,77}, all j>=0, 0<=eta<=1e-8, correct bit: error <=131*eta",
    "old_bound": "66000*eta",
    "proof_scope": "two-class auxiliary observer, clipped two-read inverse, all infinite six-step future",
    "quasipolynomial_derivation": "[z^(n-1)] QC(z)/(1-z^6)^6 and QT(z)/(1-z^6)^7; n>=29",
    "q_certificates": {}
}

for q in (73, 77):
    cp, tp = quasipolys(q % 6)
    assert cp.degree() == 5 and tp.degree() == 6
    for k in (q, q + 6, q + 12, q + 18):
        assert int(cp.eval(k)) == C[k]
        assert int(tp.eval(k)) == T[k]
    c0, c1 = int(cp.eval(q)), int(cp.eval(q + 6))
    t0, t1 = int(tp.eval(q)), int(tp.eval(q + 6))
    kd = s.Integer(2 * (c0 + c1 + 4))
    ke = s.Integer(c0 + 2) + (
        s.Rational(t0 + 2, c0 - 2) + s.Rational(1, 4)
    ) * kd
    c = cp.as_expr() - 2
    t = tp.as_expr() + 2
    h = N**3 * (ke * c + kd * t)
    # Strict positivity of Delta makes h(n)/c(n)^2 decrease at n=q+6J.
    delta = s.Poly(s.expand(
        (h * c.subs(N, N + 6)**2 - h.subs(N, N + 6) * c**2)
        .subs(N, q + 6 * J)), J)
    cs = list(reversed(delta.all_coeffs()))
    assert len(cs) == 19 and all(a > 0 for a in cs)
    start = s.factor((h / c**2).subs(N, q) / q**3)
    assert start < 131
    result["q_certificates"][str(q)] = {
        "C_q": c0, "C_q6": c1, "T_q": t0, "T_q6": t1,
        "Kd": str(kd), "Ke": str(ke),
        "C_poly_descending": [str(v) for v in cp.all_coeffs()],
        "T_poly_descending": [str(v) for v in tp.all_coeffs()],
        "delta_degree": delta.degree(),
        "delta_coefficient_signs": "+" * len(cs),
        "delta_coefficients_ascending": [str(v) for v in cs],
        "all_future_factor_at_j0": str(start),
        "factor_less_than_131": True
    }

out = Path(__file__).with_name("R749STG_ALL_FUTURE_MONOTONICITY_RESULTS.json")
out.write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
print("PASS R749STG: 38/38 strictly positive coefficients, 131*eta all-horizon bound")
for q, v in result["q_certificates"].items():
    print(q, "A(q)=", v["all_future_factor_at_j0"],
          "degree=", v["delta_degree"])
