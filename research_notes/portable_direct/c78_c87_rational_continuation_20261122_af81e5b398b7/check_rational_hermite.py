"""Finite exact coefficient checks for the four-node rational C2 interpolant."""
from math import comb
from pathlib import Path
import json
import sympy as sp

t, z = sp.symbols("t z")
phi = [
    t * (t - 1)**3 * (2*t + 1) / 2,
    -(t - 1) * (6*t**4 - 9*t**3 + 2*t + 2) / 2,
    t * (6*t**4 - 15*t**3 + 9*t**2 + t + 1) / 2,
    -t**3 * (t - 1) * (2*t - 3) / 2,
]
endpoints = [
    (0, 0, [0, 1, 0, 0]),
    (1, 0, [0, 0, 1, 0]),
    (0, 1, [sp.Rational(-1, 2), 0, sp.Rational(1, 2), 0]),
    (1, 1, [0, sp.Rational(-1, 2), 0, sp.Rational(1, 2)]),
    (0, 2, [1, -2, 1, 0]),
    (1, 2, [0, 1, -2, 1]),
]
for node, order, expected in endpoints:
    assert [sp.diff(p, t, order).subs(t, node) for p in phi] == expected
for degree in range(3):
    assert sp.expand(sum(j**degree*p for j, p in zip(range(-1, 3), phi))
                     - t**degree) == 0

rows = []
expected_bounds = [sp.Rational(13, 10), sp.Integer(4), sp.Integer(7)]
for order in range(3):
    shift_poly = sum(sp.diff(phi[k], t, order)*z**k for k in range(4))
    quotient, remainder = sp.div(shift_poly, (z - 1)**order, z)
    assert remainder == 0
    weights = [sp.expand(quotient.coeff(z, k)) for k in range(4 - order)]
    assert sp.simplify(sum(weights) - 1) == 0
    degree = 5 - order
    bernstein = [
        [sum(sp.Poly(p, t).nth(l)*sp.Rational(comb(j, l), comb(degree, l))
             for l in range(j + 1)) for j in range(degree + 1)]
        for p in weights
    ]
    for p, coeffs in zip(weights, bernstein):
        rebuilt = sum(coeffs[j]*comb(degree, j)*t**j*(1-t)**(degree-j)
                      for j in range(degree + 1))
        assert sp.expand(rebuilt - p) == 0
    column_bounds = [sum(abs(row[j]) for row in bernstein)
                     for j in range(degree + 1)]
    assert max(column_bounds) == expected_bounds[order]
    rows.append({
        "order": order,
        "weights": list(map(str, weights)),
        "bernstein_coefficients": [list(map(str, row)) for row in bernstein],
        "column_absolute_sums": list(map(str, column_bounds)),
        "l1_bound_on_unit_interval": str(max(column_bounds)),
    })
two_dimensional_bounds = {
    f"{a},{b}": str(expected_bounds[a]*expected_bounds[b])
    for a, b in [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
}
assert max(map(sp.Rational, two_dimensional_bounds.values())) == 16
result = {
    "status": "PASS",
    "arithmetic": "exact symbolic rational polynomial coefficients",
    "shape_functions": list(map(str, phi)),
    "endpoint_constraints_checked": len(endpoints),
    "polynomial_reproduction_degrees": [0, 1, 2],
    "difference_weight_certificates": rows,
    "two_dimensional_total_order_at_most_two_bounds": two_dimensional_bounds,
    "uniform_C2_stability_constant": 16,
    "scope": (
        "Finite identities and coefficient bounds. "
        "The C2 convergence theorem and near-stock averaging proof are in "
        "RATIONAL_HERMITE_C2_BRIDGE.md; no finite-inventory jet assumption "
        "is verified by these coefficient identities."
    ),
}
Path(__file__).with_name("rational_hermite_checks.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps({
    "status": result["status"],
    "endpoint_constraints_checked": result["endpoint_constraints_checked"],
    "one_dimensional_bounds": list(map(str, expected_bounds)),
    "two_dimensional_C2_bound": 16,
}, indent=2))
