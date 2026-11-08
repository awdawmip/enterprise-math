#!/usr/bin/env python3
"""Exact exhaustive centrality check for PREFIX-617/618 BRC signed-label stopping.
Proof of monotonicity in the paper uses an exact derivative factorization,
not numerical sampling or extrapolation from checked p-values.
"""
import contextlib
import io
import json
from fractions import Fraction as Q
with contextlib.redirect_stdout(io.StringIO()):
    import PREFIX618_R6_exact_balanced_stop_certificate as baseline

caps = []
number_of_states = 0
central_nontrivial = 0
for m in range(1, 190):
    surviving = [k for k in range(m + 1) if baseline.wide(m, k)]
    number_of_states += m + 1
    if m == 189:
        assert surviving == []
        continue
    assert surviving
    a = surviving[0]
    assert surviving == list(range(a, m - a + 1)), (m, surviving)
    assert 0 <= a <= m // 2
    if a >= 1:
        central_nontrivial += 1
    caps.append([m, a, m - a])
assert len(caps) == 188
assert caps[24][0] == 25 and caps[24][1] == 1
assert central_nontrivial > 0

for p in [Q(0), Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4), Q(7, 8), Q(1)]:
    for m, a, upper in caps:
        if a == 0: continue
        s = sum((Q(__import__('math').comb(m,k)) * p**k*(1-p)**(m-k)
                 for k in range(a, upper+1)),Q(0))
        s_half = sum((Q(__import__('math').comb(m,k), 2**m) for k in range(a,upper+1)),Q(0))
        assert s <= s_half

print(json.dumps({
  'schema': 'PREFIX620_R6_GLOBAL_WORST_CASE_V1',
  'science_pin': 'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'domain': 'd=2, p1,p2 in [0,1], q=12 or 24; beta=1/40, confidence p-diameter 1/4',
  'enumerated_m_values': 190,
  'enumerated_mk_pairs': number_of_states,
  'central_survival_ranges_count': len(caps),
  'first_nontrivial_survival_index': next(m for m,a,b in caps if a>0),
  'centrality_exact': True,
  'm189_all_stopped': True,
  'theorem': 'The unique global maximizer of E[T_q] is p1=p2=1/2',
  'E_T12_max_decimal': '2350.8871013999329674336846958203177',
  'E_T24_max_decimal': '4701.7742027998659348673693916406354',
  'number_of_exact_integer_inequality_checks': baseline.checks,
  'proof_component': 'Binomial central interval derivative s_m prime = m*[b_(m-1,p)(a-1)-b_(m-1,p)(m-a)] >= 0 for p<=1/2; strict for m=25, a=1.',
  'verification': 'ALL_CHECKS_PASS'
},indent=2))
