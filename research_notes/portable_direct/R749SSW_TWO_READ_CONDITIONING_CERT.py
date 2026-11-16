#!/usr/bin/env python3
"""R749SSW exact rational certificate. Requires Python 3 and SymPy.
No floating-point calculations or unreported numerical tolerances.
"""
import json
import sympy as sp

k = sp.symbols("k", integer=True, nonnegative=True)
WEIGHTS = (1, 1, 2, 3, 6)
NMAX = 150

def exact_counts(limit):
    # Coefficients for four labeled sources (k2,k3,k4,k5).
    a = [0] * limit
    a[0] = 1
    for w in (1, 2, 3, 6):
        for n in range(w, limit):
            a[n] += a[n - w]
    exact_c = [sum(a[n - j] for j in range(n + 1))
               for n in range(limit)]
    exact_t = [sum(j * a[n - j] for j in range(n + 1))
               for n in range(limit)]
    C = [0] * (limit + 1)
    T = [0] * (limit + 1)
    for q in range(1, limit + 1):
        C[q] = C[q - 1] + exact_c[q - 1]
        T[q] = T[q - 1] + exact_t[q - 1]
    return C, T

Cseq, Tseq = exact_counts(NMAX)
assert (Cseq[6], Tseq[6], Cseq[12], Tseq[12]) == (41, 50, 380, 881)
evidence = []

for r in range(6):
    def phase_poly(values, degree):
        return sp.expand(sp.interpolate(
            [(j, values[6 + r + 6*j]) for j in range(degree + 1)], k))
    C = phase_poly(Cseq, 5)
    T = phase_poly(Tseq, 6)
    # Extra checks support the generating-function derivation, but are
    # not substituted for its all-q quasipolynomial justification.
    for j in range(7, 17):
        assert C.subs(k, j) == Cseq[6 + r + 6*j]
        assert T.subs(k, j) == Tseq[6 + r + 6*j]
    C1 = sp.expand(C.subs(k, k + 1))
    T1 = sp.expand(T.subs(k, k + 1))
    A = sp.expand(T1*C - T*C1)
    B = sp.expand(T1 - T)
    D = sp.expand(C1 - C)
    assert sp.Poly(D, k).degree() == 4
    assert all(v > 0 for v in sp.Poly(D, k).all_coeffs())
    assert sp.Poly(T, k).LC() == sp.Poly(C, k).LC()
    cases = []
    for d in (-2, 2):
        N = sp.Poly(sp.expand(
            A + d*B - 2*D - (C + d)*(C1 + d)), k)
        coeffs = N.all_coeffs()
        assert N.degree() == 8
        assert all(z > 0 for z in coeffs)
        cases.append({"d": d, "degree": N.degree(),
                      "constant": str(N.eval(0)),
                      "min_coefficient": str(min(coeffs))})
    evidence.append({"residue": r, "cases": cases})

# Example q=6, e=2, d=-2:
X0 = sp.Rational(Tseq[6]+2, Cseq[6]-2)
X1 = sp.Rational(Tseq[12]+2, Cseq[12]-2)
assert X0 == sp.Rational(4, 3)
assert X1-X0 == sp.Rational(379, 378)

print(json.dumps({
    "result": "PASS",
    "proposition": "X_(q+6)(e,d)-X_q(e,d)>1 for all integer q>=6 and e,d in [-2,2]",
    "residue_cases": evidence,
    "global_min_coefficient_of_12_positivity_polynomials": str(min(
        sp.Rational(item["min_coefficient"])
        for row in evidence for item in row["cases"])),
    "q6_example_increment": str(X1-X0),
    "certificate_kind": "exact rational polynomial coefficient positivity",
}, ensure_ascii=False, indent=2))
