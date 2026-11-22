"""Exact generic identities for C78's two cleared direction numerators."""
from pathlib import Path
import json
import sympy as sp

r, s, u, v, qq, qp = sp.symbols("r s u v qq qp", nonzero=True)
aq, bq, ap, bp, m1, m2, k, eq, ep = sp.symbols(
    "aq bq ap bp m1 m2 k eq ep"
)
source = eq * (m1 * aq / (4 * r**3 * qq**2)
               + m2 * bq / (4 * s**3 * qq**2))
rows = []
for direction, target_root, target_numerator in [(1, u, ap), (2, v, bp)]:
    denominator = 4 * r**3 * s**3 * target_root**3 * qq**2 * qp**2
    numerator = (
        eq * target_root**3 * (m1 * s**3 * aq + m2 * r**3 * bq) * qp**2
        - k * ep * r**3 * s**3 * target_numerator * qq**2
    )
    direction_value = source - k * ep * target_numerator / (
        4 * target_root**3 * qp**2
    )
    difference = sp.cancel(numerator - denominator * direction_value)
    assert difference == 0
    rows.append({"direction": direction, "exact_difference": str(difference)})

q_upper = (1 + 448) * (1 + 1792)
assert q_upper == 805057
result = {
    "status": "PASS",
    "arithmetic": "exact symbolic rational functions and Python integers",
    "identities": rows,
    "Q_upper_on_positive_unit_square": q_upper,
    "direction_denominator_upper": 4 * q_upper**4,
    "scope": (
        "Verifies the two generic common-denominator identities. "
        "The direction nonzero theorem and generic correspondence algebra "
        "are proved in ALGEBRAIC_DIRECTION_AND_SMALL_VALUES.md. "
        "No expanded inverse-correspondence multiplication matrix is claimed."
    ),
}
path = Path(__file__).with_name("direction_denominator_checks.json")
path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(result, ensure_ascii=False, indent=2))
