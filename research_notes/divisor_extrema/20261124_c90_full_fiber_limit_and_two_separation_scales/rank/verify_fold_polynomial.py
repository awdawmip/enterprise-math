"""Independent exact polynomial checks for C90's global left-fold zero.

The rational denominators are cleared explicitly before expansion, avoiding a
large general-purpose rational simplification.  This is not a rerun of the
Fraction root-isolation certificate.
"""

import json
from pathlib import Path

import sympy as sp


A, d = sp.symbols("A d")
e = A - 1
M = 7 * A**4 * d + 16
V = 7 * A**5 * d + 16
D = e**2 * M**2 * V**2

# N=Nn/D and T=Tn/D, with the original spectral N and T.
Nn = A * M**2 * V**2 + 1792 * A**4 * d * e**2 * V**2 + 2800 * A**5 * d * e**2 * M**2
Tn = 448 * A**4 * d * e**2 * V**2 + 560 * A**5 * d * e**2 * M**2

q = [
    393216 - 983040 * A**2,
    114688 * A**4 * (5 * A**3 - 30 * A**2 + 21 * A - 5),
    -225792 * A**8 * (5 * e**4 + 3 * A**2),
    21952 * A**13 * (-5 * A**3 + 21 * A**2 - 30 * A + 5),
    7203 * A**18 * (2 * A**2 - 5),
]
Q = sum(d**i * qi for i, qi in enumerate(q))

claimed_derivatives = [
    -1966080 * A,
    573440 * A**3 * (7 * A**3 - 36 * A**2 + 21 * A - 4),
    -225792 * A**7 * (20 * e**3 * (3 * A - 2) + 30 * A**2),
    21952 * A**12 * (-80 * A**3 + 315 * A**2 - 420 * A + 65),
    7203 * A**17 * (40 * A**2 - 90),
]

residuals = {
    # d N_d = A T_A after multiplication by D^2.
    "dNd_equals_ATa": d * (sp.diff(Nn, d) * D - Nn * sp.diff(D, d))
    - A * (sp.diff(Tn, A) * D - Tn * sp.diff(D, A)),
    # A(N T_A - T N_A) equals the claimed factor times Q.
    # Multiplication by D^2=e^4 M^4 V^4 leaves this polynomial.
    "K_exact_factor": A * (Nn * sp.diff(Tn, A) - Tn * sp.diff(Nn, A))
    + 224 * d * A**5 * Q * e * M * V,
}
residuals.update({f"q{i}_derivative": sp.diff(qi, A) - rhs
                  for i, (qi, rhs) in enumerate(zip(q, claimed_derivatives))})

checks = {}
for name, residual in residuals.items():
    polynomial = sp.Poly(sp.expand(residual), A, d)
    checks[name] = polynomial.is_zero
    assert polynomial.is_zero, (name, polynomial.as_expr())

output = {
    "arithmetic": "SymPy exact integer polynomial expansion; no floating point",
    "checks": checks,
    "all_passed": all(checks.values()),
    "scope": "Polynomial identities only; derivative inequalities and fold continuation are proved in the review.",
}
path = Path(__file__).with_name("fold_polynomial_verification.json")
path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(output, ensure_ascii=False, indent=2))
