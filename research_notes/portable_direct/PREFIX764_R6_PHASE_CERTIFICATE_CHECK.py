"""PREFIX-764 exact finite support-kernel and rectangle phase verification.

Requires the unchanged PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json
in the same directory; all comparisons are exact Python Fraction operations.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json
import hashlib

src = Path(__file__).with_name('PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json')
raw = src.read_bytes()
assert len(raw) == 24743
assert hashlib.sha256(raw).hexdigest() == '1a480a9a05c4773f82091037fa8f6b695855ffbb885b21e804d56fdc181d4e76'
data = json.loads(raw)
assert data['scientific_input_commit'] == 'f42f2906d77f24085c123f3ccfe9667d41caa96d'

minimum, locations = Q(1), []
for i in range(25, 189):
    for j in range(25, 189):
        val = Q(comb(i+j, i), 2**(i+j+1))
        if val < minimum:
            minimum, locations = val, [(i, j)]
        elif val == minimum:
            locations.append((i, j))
assert minimum == Q(comb(213,25), 2**214)
assert locations == [(25,188), (188,25)]

old_lb = 1 / (Q(2**190) + 377)
new_lb = 1 / (Q(2) / minimum + 377)
assert new_lb > old_lb

def deltas(z):
    row = data['variance_comparisons'][z]
    var = Q(int(row['exact_delta_variance_numerator']), int(row['exact_delta_variance_denominator']))
    v2 = Q(int(row['exact_delta_Vq2_numerator']), int(row['exact_delta_Vq2_denominator']))
    return var, 2*var-v2/2

v0, m0 = deltas('0')
v1, m1 = deltas('1/4')
variance_rect, mean_rect = v1-v0, m1-m0
assert variance_rect < 0 and mean_rect < 0
q_rect = mean_rect / variance_rect
assert Q(190005, 1000000) < q_rect < Q(190006, 1000000)
q_witness = Q(190006, 1000000)
assert q_witness*q_witness*variance_rect-q_witness*mean_rect < 0

summary = {
    'schema': 'PREFIX764_R6_PHASE_CERTIFICATE_CHECK_V1',
    'source_pin': data['scientific_input_commit'],
    'source_json_sha256': hashlib.sha256(raw).hexdigest(),
    'support_interval': [25,188],
    'pairs_exactly_checked': 164*164,
    'minimum_K_numerator': str(minimum.numerator),
    'minimum_K_denominator': str(minimum.denominator),
    'minimum_locations': [[i,j] for i,j in locations],
    'new_q_lower_bound_decimal': format(float(new_lb), '.17g'),
    'lower_bound_improvement_ratio_decimal': format(float(new_lb/old_lb), '.17g'),
    'rectangle_q_switch_decimal': format(float(q_rect), '.17g'),
    'q_switch_strict_upper_bound': '190006/1000000',
    'result': 'ALL_CHECKS_PASS PREFIX764',
    'limits': ['algebraicity and polynomial sign oracle proved analytically',
               'no exact q_c optimization or new 1/768 exclusion area',
               'author-level unreviewed auxiliary model']
}
print(json.dumps(summary, indent=2))
