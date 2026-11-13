"""PREFIX-763: exact finite checks for the mixed-curvature phase theorem.

This checks the finite K kernel and the exact PREFIX-760 witnesses; the
continuous phase theorem itself is proved in the companion Markdown note.
"""
import hashlib
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

SRC = Path(__file__).with_name("PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json")
EXPECTED_SHA256 = "1a480a9a05c4773f82091037fa8f6b695855ffbb885b21e804d56fdc181d4e76"
raw = SRC.read_bytes()
assert len(raw) == 24743 and hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
source = json.loads(raw)
assert source["scientific_input_commit"] == "f42f2906d77f24085c123f3ccfe9667d41caa96d"


def increments(z):
    data = source["variance_comparisons"][z]
    variance = F(int(data["exact_delta_variance_numerator"]),
                 int(data["exact_delta_variance_denominator"]))
    v2 = F(int(data["exact_delta_Vq2_numerator"]),
           int(data["exact_delta_Vq2_denominator"]))
    mean = 2 * variance - v2 / 2
    return variance, mean


v0, m0 = increments("0")
v1, m1 = increments("1/4")
v2, m2 = increments("1/2")
dv_minus, dm_minus = v1 - v0, m1 - m0
dv_plus, dm_plus = v2 - v1, m2 - m1
assert dv_minus < -526 and -112 < dm_minus < 0
assert dv_plus > 155 and dm_plus < 0
q_test = F(191, 1000)
assert q_test * q_test * dv_minus - q_test * dm_minus < 0
q_rectangle = dm_minus / dv_minus
assert F(19, 100) < q_rectangle < q_test
assert dv_plus > 0  # positive variance mixed difference gives theta<0 somewhere

n = 188
minimum = F(1)
min_locations = []
for i in range(n + 1):
    for j in range(n + 1):
        k = F(comb(i + j, i), 2 ** (i + j + 1))
        if k < minimum:
            minimum, min_locations = k, [(i, j)]
        elif k == minimum:
            min_locations.append((i, j))
assert minimum == F(1, 2 ** 189)
assert set(min_locations) == {(0, 188), (188, 0)}

result = {
    "schema": "PREFIX763_MIXED_CURVATURE_PHASE_CHECK_V1",
    "source_pin": source["scientific_input_commit"],
    "source_sha256": EXPECTED_SHA256,
    "K_index_domain": "0<=i,j<=188",
    "K_pairs_exactly_checked": 189 * 189,
    "K_min": "1/2^189",
    "K_min_locations": [[0, 188], [188, 0]],
    "negative_rectangle_delta_variance_approx": float(dv_minus),
    "negative_rectangle_delta_mean_approx": float(dm_minus),
    "rectangle_threshold_q_approx": float(q_rectangle),
    "q_test": "191/1000",
    "q_test_negative_rectangle_mixed_V_approx": float(q_test*q_test*dv_minus - q_test*dm_minus),
    "positive_rectangle_delta_variance_approx": float(dv_plus),
    "critical_q_lower_bound": "1/(2^190+377)",
    "critical_q_upper_bound": "<191/1000",
    "run_status": "ALL_CHECKS_PASS PREFIX763",
    "limitations": "Author-level analytic proof; finite kernel and source rational witness checks, no new exclusion area"
}
Path(__file__).with_name("PREFIX763_R6_MIXED_CURVATURE_PHASE_RESULTS.json").write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
print(result["run_status"])
print("q_rectangle", result["rectangle_threshold_q_approx"])
