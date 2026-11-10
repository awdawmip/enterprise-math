#!/usr/bin/env python3
"""PREFIX-673-R6 exact implication checker; Python stdlib only.
Uses the author-certified PREFIX-660 root/curvature and PREFIX-670
normal penalty. This does not replay the 189 frozen survivor layers.
"""
from fractions import Fraction as Q
import json

Z0 = Q(19, 128)
BAND = (Q(607, 4096), Q(609, 4096))
DELTA = Q(1, 2**24)
N = 10**13
SLOTS = {
    12: dict(root_offsets=(-584, -583), neg_curvature_cap=13_000_000,
             normal_linear=76_650),
    24: dict(root_offsets=(3682, 3683), neg_curvature_cap=52_000_000,
             normal_linear=306_490),
}

RESULTS = {}
for q, data in SLOTS.items():
    a, b = (Z0 + Q(k, 2**24) for k in data['root_offsets'])
    m = (a + b) / 2
    cap = Q(data['neg_curvature_cap'])
    L = Q(data['normal_linear'])
    # Reused hypotheses: z_*(q) in (a,b); -cap < g_q'' < 0
    # on BAND, and M(q)-V_q(p,z)>=Lp for 0<=p<=1/64.
    assert BAND[0] < a < m < b < BAND[1]
    assert b-a == DELTA
    edge_gap_cap = cap * DELTA * DELTA / 8
    normal_penalty = L / N
    margin = normal_penalty - edge_gap_cap
    assert Q(1, N) < Q(1, 64)
    assert margin > Q(1, 10**9)
    RESULTS[str(q)] = {
        'edge_optimizer_bracket': [str(a), str(b)],
        'fixed_rational_witness_z': str(m),
        'edge_witness_gap_strictly_below': str(edge_gap_cap),
        'normal_loss_at_p_1_over_10t': str(normal_penalty),
        'strict_margin_lower_bound': str(margin),
        'certified_uniform_margin': '1/1000000000',
        'p_range': [str(Q(1,N)),str(Q(1,64))],
        'z_range': [str(x) for x in BAND],
    }
assert Q(1, N) / Q(1, 64) == Q(64, N)
RESULTS_META = {
    'result_id': 'PREFIX-673-R6',
    'frozen_scientific_input': 'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'model': '189-survivor-layer BRC first-stop statistical observer',
    'excluded_fraction_of_prior_rectangle': str(1-Q(64,N)),
    'slot_specific': RESULTS,
    'dependency_scope': 'Author certificates PREFIX-660 (root brackets and whole-band curvature) and PREFIX-670 (normal coercivity); not independently replayed',
    'status': 'AUTHOR_DERIVED_EXACT_RATIONAL_IMPLICATION_CHECKED_UNREVIEWED_NOT_ADMITTED'
}
if __name__ == '__main__':
    print('ALL_CHECKS_PASS: dyadic fixed witnesses, two slot inequalities, rational margins')
    print(json.dumps(RESULTS_META, indent=2, ensure_ascii=False))
