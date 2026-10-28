#!/usr/bin/env python3
"""Exact, finite-rational checks for EC48Y author-side occupancy certificates."""
from fractions import Fraction as F
from itertools import product
from json import dump
from pathlib import Path

D = F

# A two-stage Markov quotient: Y_1 has mass 1 and LR 1.
# At Y_2, Q=(3/4,1/4), P=(1/4,3/4), so LR=(1/3,3).
q = (D(3,4), D(1,4))
p = (D(1,4), D(3,4))
L = tuple(p[i]/q[i] for i in range(2))
assert L == (D(1,3), D(3))

def markov_readout(a, c, d0, d1):
    """A=stop-accept, C=continue; d_i terminal accept probabilities."""
    assert 0 <= a <= 1 and 0 <= c <= 1-a
    assert all(0 <= d <= 1 for d in (d0,d1))
    alpha = a + c * (p[0]*d0 + p[1]*d1)
    beta = a + c * (q[0]*d0 + q[1]*d1)
    return alpha, beta, D(1)+c, D(1)+c

witness = markov_readout(D(1,8), D(1,2), D(1,3), D(2,3))
assert witness == (D(5,12), D(1,3), D(3,2), D(3,2))
# Q occupation certificate: x_1=1; z_1=(1/8,3/8,1/2)
# x_2=(3/8,1/8); z_2(accept)=(1/8,1/12).
q_x2 = tuple(D(1,2)*qi for qi in q)
q_z2_accept = (D(1,8), D(1,12))
assert q_x2 == (D(3,8), D(1,8))
assert all(0 <= za <= x for za,x in zip(q_z2_accept,q_x2))
assert D(1,8)+sum(q_z2_accept) == witness[1]
assert D(1,8)+sum(li*zi for li,zi in zip(L,q_z2_accept)) == witness[0]
# Dual inequality for every common source-neutral policy: alpha - 3 beta <= 0
n_markov_grid=0
for a_units in range(9):
    for c_units in range(9-a_units):
        for d0_units in range(5):
            for d1_units in range(5):
                vec=markov_readout(D(a_units,8),D(c_units,8),D(d0_units,4),D(d1_units,4))
                assert vec[0]-3*vec[1] <= 0
                n_markov_grid += 1
independent_target=(D(3,4),D(1,8),D(3,2),D(3,2))
assert independent_target[0]-3*independent_target[1] == D(3,8)
# Separate policies (invalid as a joint common policy) realize each source's own coordinate.
p_only = markov_readout(D(3,8),D(1,2),D(0),D(1))
q_only = markov_readout(D(1,8),D(1,2),D(0),D(0))
assert p_only[0]==independent_target[0] and q_only[1]==independent_target[1]
assert p_only[2:]==q_only[2:]==independent_target[2:]

# Four strictly positive joint leaves (H,Z): an informative branch only for H=0.
leaves = {
    'H0Z1': {'P':D(3,8), 'Q':D(1,8), 'L':D(3)},
    'H0Z0': {'P':D(1,8), 'Q':D(3,8), 'L':D(1,3)},
    'H1Z1': {'P':D(1,4), 'Q':D(1,4), 'L':D(1)},
    'H1Z0': {'P':D(1,4), 'Q':D(1,4), 'L':D(1)},
}
for source in ('P','Q'):
    assert sum(v[source] for v in leaves.values())==1
    assert all(v[source]>0 for v in leaves.values())
for v in leaves.values():
    assert v['P']/v['Q']==v['L']

# Fine policy: H0 continues, H1 stops/rejects, accept iff H0Z1.
fine=(D(3,8),D(1,8),D(3,2),D(3,2))
assert fine[0]-fine[1]==D(1,4)
# Initial Q occupancy x(H0)=x(H1)=1/2, fine continue z(H0)=1/2, z(H1)=0.
rank_one_violation=D(1,2)*D(1,2)-D(0)*D(1,2)
assert rank_one_violation==D(1,4)

# A compressed single-register observer forgets H at t=1, LR=1.
# For any common c, positive alpha-beta can come only from H0Z1,
# and is at most c*(P(H0Z1)-Q(H0Z1))=c/4.
def compressed_readout(a,c,d):
    assert 0<=a<=1 and 0<=c<=1-a
    assert len(d)==4 and all(0<=v<=1 for v in d)
    names=('H0Z1','H0Z0','H1Z1','H1Z0')
    alp=a+c*sum(leaves[h]['P']*d[i] for i,h in enumerate(names))
    bet=a+c*sum(leaves[h]['Q']*d[i] for i,h in enumerate(names))
    return alp,bet,D(1)+c,D(1)+c
n_compressed_grid=0
max_support_at_half=None
for a_units in range(9):
    for c_units in range(9-a_units):
        a,c=D(a_units,8),D(c_units,8)
        for terminal_bits in product((D(0),D(1)),repeat=4):
            vec=compressed_readout(a,c,terminal_bits)
            assert vec[0]-vec[1] <= c/D(4)
            if c==D(1,2):
                delta=vec[0]-vec[1]
                max_support_at_half = delta if max_support_at_half is None else max(max_support_at_half,delta)
            n_compressed_grid+=1
assert max_support_at_half==D(1,8)
assert fine[0]-fine[1]-((fine[3]-1)/4)==D(1,8)
# More than deterministic terminal choices: exact fractional grid checks.
n_random_grid=0
for a_units in range(5):
    for c_units in range(5-a_units):
        a,c=D(a_units,4),D(c_units,4)
        for terminal in product((D(0),D(1,2),D(1)), repeat=4):
            v=compressed_readout(a,c,terminal)
            assert v[0]-v[1] <= c/4
            n_random_grid +=1

# In the 4-leaf case all four terminal (Z, full LR) pairs are distinguishable
# except the two H1 cases which both have LR=1, but their source masses match.
# The full-region impossibility uses only LR=3 positive branch, so no assumption
# that hidden H is directly observable at the terminal.

fmt=lambda v: str(v.numerator)+('/'+str(v.denominator) if v.denominator!=1 else '')
report={
  'model':'EC48Y fixed-updater dual-source positive-rational stopping models',
  'markov_quotient':{
      'Q_Z':[fmt(v) for v in q], 'P_Z':[fmt(v) for v in p],
      'LR_Z':[fmt(v) for v in L],
      'LP_witness_O':[fmt(v) for v in witness],
      'LP_occupation_Q_x2':[fmt(v) for v in q_x2],
      'LP_occupation_Q_terminal_accept':[fmt(v) for v in q_z2_accept],
      'source_separate_false_target':[fmt(v) for v in independent_target],
      'exact_separating_inequality':'alpha-3*beta <= 0',
      'false_target_dual_violation':fmt(independent_target[0]-3*independent_target[1]),
      'source_separate_P_policy_O':[fmt(v) for v in p_only],
      'source_separate_Q_policy_O':[fmt(v) for v in q_only],
      'rational_grid_policies_checked':n_markov_grid,
  },
  'nonlumpable_hidden_H':{
      'joint_leaves':{k:{kk:fmt(vv) for kk,vv in v.items()} for k,v in leaves.items()},
      'full_policy_O':[fmt(v) for v in fine],
      'one_state_bound':'alpha-beta <= (E_QT-1)/4',
      'bound_gap_at_full_policy':fmt(fine[0]-fine[1]-(fine[3]-1)/4),
      'rank_one_minor_for_fine_policy':fmt(rank_one_violation),
      'max_compressed_delta_at_C_half':fmt(max_support_at_half),
      'exact_deterministic_terminal_grid_checked':n_compressed_grid,
      'exact_fractional_terminal_grid_checked':n_random_grid,
  },
  'result':'all exact Fraction assertions passed',
  'coverage':'finite rational grids and explicit witnesses; general fixed-updater theorem is analytic, quantifier elimination not executed',
}
out=Path(__file__).with_name('EXACT_REPORT.json')
with out.open('w',encoding='utf-8') as f: dump(report,f,ensure_ascii=False,indent=2,sort_keys=True)
print('EXACT_PASS',n_markov_grid,n_compressed_grid,n_random_grid,'gap',fmt(D(1,8)))
