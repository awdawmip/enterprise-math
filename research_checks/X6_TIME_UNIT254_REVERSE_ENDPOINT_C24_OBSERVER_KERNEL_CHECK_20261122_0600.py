"""Exact conditional directed-Port terminal-observer kernel (Unit254).
Input: frozen Unit245 spoke counts, Unit253 transpose theorem; not native physical measurements.
Requires sympy (integer Smith normal form only)."""
import json
from math import gcd, prod
from sympy import Matrix, ZZ, eye
from sympy.matrices.normalforms import smith_normal_form

E = [0, 2, 4, 6, 8, 10]
N = 24
forward_cost = [
    [30, 38, 36, 38, 38, 46],
    [38, 30, 46, 38, 38, 36],
    [32, 36, 32, 48, 38, 32],
    [28, 30, 40, 36, 44, 34],
    [30, 28, 34, 44, 36, 40],
    [36, 32, 32, 38, 48, 32],
]
# Unit245 certificate: exact number of complete center traversals, by ingress/egress.
passages = [
    [1, 6, 3, 2, 3, 6],
    [6, 1, 6, 3, 2, 3],
    [3, 6, 1, 6, 3, 2],
    [2, 3, 6, 1, 6, 3],
    [3, 2, 3, 6, 1, 6],
    [6, 3, 2, 3, 6, 1],
]
assert all(passages[i][j] == 12 // gcd(12, (E[j]-E[i]) % 12)
           for i in range(6) for j in range(6))
assert all(passages[i][j] == passages[j][i] for i in range(6) for j in range(6))

def observer_rows(mode):
    rows = []
    for i in range(6):
        for j in range(6):
            count = passages[i][j] if mode == 'forward' else passages[j][i]
            row = [0]*12
            row[i], row[6+j] = count, count
            rows.append(row)
    return rows

def kernel_size(rows):
    M = Matrix(rows + (N*eye(12)).tolist())
    S = smith_normal_form(M, domain=ZZ)
    d = [abs(int(S[k,k])) for k in range(12)]
    return int(prod(d)), d

F, R = observer_rows('forward'), observer_rows('reverse')
fk, fd = kernel_size(F)
frk, both_d = kernel_size(F+R)
assert fk == frk == 432
assert fd == both_d == [1]*9 + [3,6,24]
assert len(F) == len(R) == 36 and F == R
# Gauge: add t to all ingress weights and subtract t from all egress weights.
gauge = N
assert fk//gauge == frk//gauge == 18
alpha = [0,16,0,0,16,0]
beta  = [0,8,0,0,8,0]
assert any(alpha) and len(set(alpha)) > 1
assert all(sum(x*y for x,y in zip(row,alpha+beta))%N==0 for row in F+R)
forward_reverse_costs = [(forward_cost[i][j],forward_cost[j][i]) for i in range(6) for j in range(6)]
min_dual_cost = min(sum(pair) for pair in forward_reverse_costs)
min_dual_max = min(max(pair) for pair in forward_reverse_costs)
min_distinct_dual = min(sum(forward_reverse_costs[6*i+j]) for i in range(6) for j in range(6) if i!=j)
min_distinct_max = min(max(forward_reverse_costs[6*i+j]) for i in range(6) for j in range(6) if i!=j)
assert (min_dual_cost,min_dual_max,min_distinct_dual,min_distinct_max)==(60,30,64,32)
asym = sum(a != b for a,b in forward_reverse_costs)
assert asym == 24
result = {
    'schema':'X6_UNIT254_DUAL_WINDING_TERMINAL_C24_OBSERVER_NO_GAIN_V1',
    'date':'2026-11-22', 'task_id':'RS-X6-NATIVE-TIME-DYNAMICS',
    'model':'CONDITIONAL_SIGNED_C12_PLUS_CENTRE_PORT_AND_ADDITIVE_C24',
    'frozen_p000':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'unit245_original_certificate_commit':'f56840285cafeb9f5767ea91e903e1f53808186f',
    'unit253_reverse_certificate_commit':'757728c0b4006eece132c28473502a9749b21a8d',
    'ports':E, 'centre_passages_matrix':passages,
    'terminal_observation_rows':{'forward':36,'reverse':36,'combined':72,'same_rows_pairwise':True},
    'smith_invariant_factors_forward':fd,
    'smith_invariant_factors_combined':both_d,
    'kernel_forward':fk,'kernel_combined':frk,'gauge_size':gauge,
    'distinct_laws_up_to_gauge_forward':fk//gauge,
    'distinct_laws_up_to_gauge_combined':frk//gauge,
    'explicit_nongauge_kernel_witness':{'ingress':alpha,'egress':beta},
    'asymmetric_cost_port_pairs':asym,
    'min_two_goal_total_events':min_dual_cost,
    'min_two_goal_worst_case_events':min_dual_max,
    'min_two_goal_total_events_distinct_spokes':min_distinct_dual,
    'min_two_goal_worst_case_events_distinct_spokes':min_distinct_max,
    'source_scope':'exact conditional model; no native physical Port/sensor execution',
    'mathematical_status':'AUTHOR_PROVED_EXACT_INTEGER_EXECUTED_NOT_REVIEWED_NOT_ADMITTED'
}
print(json.dumps(result,ensure_ascii=False,indent=2))
