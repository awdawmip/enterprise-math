#!/usr/bin/env python3
"""Exact rational R1 two-law N=2 nonconvexity certificate (stdlib only)."""
from fractions import Fraction as F
import json

p = (F(3,4), F(1,4))
q = (F(1,4), F(3,4))

# A continues on first symbol zero and chooses D=1 at time 2;
# B continues on first symbol one and chooses D=0 at time 2.
def terminal_law(law, c, d):
    v = sum((law[i]*c[i] for i in range(2)), F(0))
    return {'t1_d0': 1-v, 't2_d0': v*(1-d), 't2_d1':v*d}

A = {'P':terminal_law(p,(F(1),F(0)),F(1)),
     'Q':terminal_law(q,(F(1),F(0)),F(1))}
B = {'P':terminal_law(p,(F(0),F(1)),F(0)),
     'Q':terminal_law(q,(F(0),F(1)),F(0))}
M = {law:{k:(A[law][k]+B[law][k])/2 for k in A[law]}
     for law in ('P','Q')}

assert M['P']['t1_d0']==M['Q']['t1_d0']==F(1,2)
assert (M['P']['t2_d1'],M['Q']['t2_d1'])==(F(3,8),F(1,8))
assert (M['P']['t2_d0'],M['Q']['t2_d0'])==(F(1,8),F(3,8))

det=(M['P']['t2_d1']*M['Q']['t2_d0']-
     M['Q']['t2_d1']*M['P']['t2_d0'])
assert det == F(1,8)  # Every compressed strategy requires determinant 0.

# Total time-two mass equal under P and Q forces c0=c1=1/2;
# demanded D=1 masses then disagree across the two laws.
c0=(3*F(1,2)-F(1,2))/2
c1=(3*F(1,2)-F(1,2))/2
assert c0==c1==F(1,2)
assert M['P']['t2_d1']/F(1,2)==F(3,4)
assert M['Q']['t2_d1']/F(1,2)==F(1,4)

# All seven ordered prefixes have strictly positive mass for either law.
for law in (p,q):
    histories=[((),F(1))]
    for t in (1,2):
        for seq in __import__('itertools').product(range(2),repeat=t):
            prob=F(1)
            for i in seq: prob*=law[i]
            assert prob>0
            histories.append((seq,prob))
    assert len(histories)==7
    for t in (1,2):
        assert sum((v for h,v in histories if len(h)==t),F(0))==1

def ser(obj):
    if isinstance(obj,F):return f'{obj.numerator}/{obj.denominator}'
    if isinstance(obj,dict):return {k:ser(v) for k,v in obj.items()}
    return obj
out={'schema':'EM_R1_TWO_LAW_MARKOV_N2_NONCONVEX_V1',
     'status':'EXACT_FRACTION_PASS',
     'predecessor':'research_notes/r1_n14_brc_coarse_lr_not_sufficient_20261027_r1t11/NEXT_TASK.md',
     'path_model':'binary_IID_strictly_positive',
     'horizon':2,
     'state':'x0=star; x1=first_symbol; x2=star',
     'observer':'(T,constant,D)',
     'P0':ser(p[0]),'Q0':ser(q[0]),
     'A':ser(A),'B':ser(B),'midpoint':ser(M),
     'rank_one_determinant':ser(det),
     'universal_compressed_rank_one_determinant':'0/1',
     'smallest_horizon_under_single_root_and_time_in_state':'N=2 (N<=1 convex by root-mixture argument)',
     'note':'Fractions verify the witness; generality and N<=1 claim are proved in PROOF.md, not tested exhaustively.'}
print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
