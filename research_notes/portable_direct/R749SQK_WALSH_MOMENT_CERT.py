#!/usr/bin/env python3
"""R749SQK: exact two-route finite moment certificate for frozen Walsh source slack.

Pure Python standard library. Verifies finite ranges, not the asymptotic
theorem (proved in the companion note by generating-function poles).
"""
import json
from fractions import Fraction
from math import factorial

WEIGHTS = {1: 3, 2: 4, 3: 6, 4: 4, 5: 3, 6: 2, 7: 1}
H = 3
DIM = sum(WEIGHTS.values())
MAX_R = 2400
PIN = "a72226e2430ffa4786321ac86e7f0c599d5f0389"
assert (DIM, sum((s - 1) * n for s, n in WEIGHTS.items())) == (23, 56)

def exact_counts(weights, maximum):
    q = [0] * maximum
    q[0] = 1
    for weight, multiplicity in sorted(weights.items()):
        for _ in range(multiplicity):
            for i in range(weight, maximum):
                q[i] += q[i - weight]
    cumulative = [0] * (maximum + 1)
    for r in range(1, maximum + 1):
        cumulative[r] = cumulative[r - 1] + q[r - 1]
    return cumulative

full = exact_counts(WEIGHTS, MAX_R)
without_optional = dict(WEIGHTS)
without_optional[H] -= 1
base = exact_counts(without_optional, MAX_R)

comparisons = 0
sign_changes = []
last_sign = None
last_nonpositive = 0
for r in range(1, MAX_R + 1):
    tally_a = [0, 0, 0, 0, 0]
    tally_b = [0, 0, 0, 0, 0]
    for k in range((r - 1) // H + 1):
        t = r - H * k
        a = base[t]
        b = full[t] - (full[t - H] if t - H > 0 else 0)
        assert a == b, (r, k, a, b)
        power = 1
        for m in range(5):
            tally_a[m] += power * a
            tally_b[m] += power * b
            power *= k
        comparisons += 1
    assert tally_a == tally_b and tally_a[0] == full[r], r
    expected_first = sum(full[r - H * k] for k in range(1, (r - 1) // H + 1))
    assert tally_a[1] == expected_first, r
    mean_bias_integer = 24 * H * tally_a[1] - r * full[r]
    sign = (mean_bias_integer > 0) - (mean_bias_integer < 0)
    if sign != last_sign:
        sign_changes.append([r, sign])
        last_sign = sign
    if sign <= 0:
        last_nonpositive = r

d = DIM
A = Fraction(sum((s - 1) * n for s, n in WEIGHTS.items()), 2)
L2 = Fraction(sum((s - 1) * (5 - s) * n for s, n in WEIGHTS.items()), 24)
B = A * A / 2 + L2
b = d * (Fraction(d - 1, 2) + A)
c = Fraction(2266627, 6)
assert (A, L2, B, b) == (28, Fraction(13, 12), Fraction(4717, 12), 897)

coefficients = {}
for m in range(1, 5):
    rising = 1
    for j in range(1, m + 1):
        rising *= d + j
    base_moment = Fraction(factorial(m), rising)
    relative_correction = Fraction(m, 1) * b / d - Fraction(H * (d + m), 2)
    coefficients[str(m)] = {
        "beta_moment": str(base_moment),
        "relative_first_order": str(relative_correction),
        "absolute_first_order": str(base_moment * relative_correction),
    }
assert coefficients["1"] == {
    "beta_moment": "1/24", "relative_first_order": "3", "absolute_first_order": "1/8"
}
assert coefficients["2"] == {
    "beta_moment": "1/300", "relative_first_order": "81/2", "absolute_first_order": "27/200"
}

second_mean = (
    Fraction(2) * c / ((d - 1) * (d + 1))
    - b * b / (d * (d + 1))
    + Fraction(H * H * d, 12)
)
assert second_mean == Fraction(-1357, 144)
variance_constant = Fraction(d, (d + 1) ** 2 * (d + 2))
variance_first = Fraction(27, 200) - Fraction(1, 12) * Fraction(1, 8)
assert variance_constant == Fraction(23, 14400)
assert variance_first == Fraction(299, 2400)

samples = {}
for r in [39, 60, 100, 420, 840, 1200, 2400]:
    z = [(k, base[r-H*k]) for k in range((r-1)//H+1)]
    den = full[r]
    e1 = Fraction(H * sum(k * a for k, a in z), r * den)
    e2 = Fraction(H * H * sum(k*k*a for k,a in z), r*r*den)
    vr = e2 - e1*e1
    samples[str(r)] = {
        "r_times_mean_bias": str(r * (e1 - Fraction(1, 24))),
        "r2_times_mean_second_remainder": str(r*r*(e1-Fraction(1,24)-Fraction(1,8*r))),
        "r_times_second_moment_bias": str(r*(e2-Fraction(1,300))),
        "r_times_variance_bias": str(r*(vr-Fraction(23,14400))),
    }

result = {
    "schema": "ENTERPRISE_MATH_R749SQK_EXACT_MOMENT_CERT_V1",
    "result": "PASS",
    "frozen_science": PIN,
    "type": "frozen_16_atom_auxiliary_Walsh_source_fiber",
    "weights": WEIGHTS,
    "optional_source_weight": H,
    "source_dimensions": d,
    "checked_r_inclusive": [1, MAX_R],
    "checked_moment_orders": [0, 1, 2, 3, 4],
    "independent_multiplicity_comparisons": comparisons,
    "moment_source_paths": ["optional_deleted_source_GF_DP", "consecutive_full_cumulative_differences"],
    "sign_changes_mean_minus_beta": sign_changes,
    "last_nonpositive_mean_bias_in_checked_range": last_nonpositive,
    "A": str(A), "L2": str(L2), "B": str(B), "b": str(b), "c": str(c),
    "fixed_moment_first_order": coefficients,
    "mean_second_order_coefficient": str(second_mean),
    "variance_constant": str(variance_constant),
    "variance_first_order_coefficient": str(variance_first),
    "selected_exact_rational_samples": samples,
    "scope": "Exact finite two-route count tests; infinite asymptotics are proved algebraically in the companion note.",
}
print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
