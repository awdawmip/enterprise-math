#!/usr/bin/env python3
"""Exact finite-difference certificate for the global R749SQL Walsh mean threshold.
Uses the unchanged R749SQK frozen weight multiset. Python stdlib only.
The quasipolynomial degree bound is proved in the companion note.
"""
import hashlib
import json

WEIGHTS = {1: 3, 2: 4, 3: 6, 4: 4, 5: 3, 6: 2, 7: 1}
PERIOD = 420
DEGREE_BOUND = 23
RMAX = (DEGREE_BOUND + 2) * PERIOD

a = [0] * RMAX
a[0] = 1
for weight, count in WEIGHTS.items():
    for _ in range(count):
        for t in range(weight, RMAX):
            a[t] += a[t - weight]

c = [0] * (RMAX + 1)
for r in range(1, RMAX + 1):
    c[r] = c[r - 1] + a[r - 1]

s = [0] * (RMAX + 1)
for r in range(3, RMAX + 1):
    s[r] = c[r - 3] + s[r - 3]

b = [0] * (RMAX + 1)
for r in range(1, RMAX + 1):
    b[r] = 72 * s[r] - r * c[r]

assert all(b[r] < 0 for r in range(1, 39))
assert all(b[r] > 0 for r in range(39, PERIOD + 1))
min_deltas = [None] * (DEGREE_BOUND + 2)
zeros = [0] * (DEGREE_BOUND + 2)
packed = []
for residue in range(1, PERIOD + 1):
    values = [b[residue + PERIOD * j] for j in range(DEGREE_BOUND + 2)]
    diffs = []
    for order in range(DEGREE_BOUND + 2):
        value = values[0]
        diffs.append(value)
        if min_deltas[order] is None or value < min_deltas[order]:
            min_deltas[order] = value
        zeros[order] += int(value == 0)
        values = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    assert (diffs[0] > 0 if residue >= 39 else diffs[0] < 0)
    assert all(x > 0 for x in diffs[1:DEGREE_BOUND + 1])
    assert diffs[DEGREE_BOUND + 1] == 0
    packed.append(diffs)

assert all(b[residue + PERIOD] > 0 for residue in range(1, 39))
serialized = json.dumps(packed, ensure_ascii=True, separators=(',', ':')).encode()
result = {
    "schema": "ENTERPRISE_MATH_R749SQL_WALSH_GLOBAL_THRESHOLD_V1",
    "status": "PASS",
    "frozen_scientific_pin": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "period": PERIOD,
    "degree_bound": DEGREE_BOUND,
    "weights": WEIGHTS,
    "r_max_computed": RMAX,
    "residue_classes": PERIOD,
    "strictly_positive_differences_orders_1_to_23": PERIOD * DEGREE_BOUND,
    "order_24_zero_count": zeros[24],
    "min_order_1_difference": str(min_deltas[1]),
    "min_order_23_difference": str(min_deltas[23]),
    "last_negative_r": 38,
    "B_38": str(b[38]),
    "B_39": str(b[39]),
    "all_difference_table_sha256": hashlib.sha256(serialized).hexdigest(),
    "proved_global_sign_via_quasipolynomial": "B(r)<0 for 1<=r<=38; B(r)>0 for all r>=39",
    "review_state": "AUTHOR_EXACT_NOT_REVIEWED"
}
print(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2))
