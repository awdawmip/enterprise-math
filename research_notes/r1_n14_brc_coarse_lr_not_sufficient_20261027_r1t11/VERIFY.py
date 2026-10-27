#!/usr/bin/env python3
"""Exact rational verifier for a law-independent coarse-observer LR counterexample."""
from fractions import Fraction as F
from itertools import product
import json

symbols = range(3)
r = (F(2),F(1),F(1,2))
P_early = (F(1,3),)*3
P_hi = (F(1,4),F(1,4),F(1,2))
P_lo = (F(1,12),F(3,4),F(1,6))

def state(h):
    if len(h) <= 2:
        return (len(h),)
    return (len(h),h[-1])

def early(h):
    return F(1,3)**len(h)

def conditional(h):
    return P_hi if h==(0,0) else P_lo

def mass(h,law):
    if len(h) <= 2:
        return early(h)
    p=early(h[:2])*conditional(h[:2])[h[2]]
    return p*(r[h[2]] if law=='Q' else F(1))

def s(v): return str(v.numerator) + '/' + str(v.denominator)

for alphabet in (P_hi,P_lo):
    assert sum(alphabet)==1 and sum(p*q for p,q in zip(alphabet,r))==1
    assert all(v>0 for v in alphabet)
for t in range(4):
    for law in ('P','Q'):
        assert sum((mass(h,law) for h in product(symbols,repeat=t)),F(0))==1
    fibers = {}
    for h in product(symbols,repeat=t):
        fibers.setdefault(state(h),set()).add(mass(h,'Q')/mass(h,'P'))
    assert all(len(z)==1 for z in fibers.values()),(t,fibers)

# Original: no stop before t=2; at t=2 continue only history (0,0).
# At t=3 output D=1 only if last symbol=0.
t3=F(1,9)
P_target=mass((0,0,0),'P')
Q_target=mass((0,0,0),'Q')
assert (P_target,Q_target)==(F(1,36),F(1,18))

# The compressed x-only policy must continue at t=2 with u=1/9
# because all length-two prefixes share one state and t<2 stopping is absent.
u=t3
pbar=tuple(sum((conditional(h)[j] for h in product(symbols,repeat=2)),F(0))/9 for j in symbols)
qbar=tuple(pbar[j]*r[j] for j in symbols)
assert sum(pbar)==sum(qbar)==1
# Achieving Q/P=2 at (T=3,D=1) forces D=1 only on j=0.
P_cap=u*pbar[0]
Q_cap=u*qbar[0]
assert P_cap==F(11,972)
assert Q_cap==F(11,486)
P_gap=P_target-P_cap
Q_gap=Q_target-Q_cap
assert P_gap==F(4,243) and Q_gap==F(8,243)

# Exact branchwise coefficient: Q-2P is 0 for j=0 and negative for other symbols.
separation={str(j):s(qbar[j]-2*pbar[j]) for j in symbols}
assert separation['0']=='0/1'
assert all((qbar[j]-2*pbar[j])<0 for j in (1,2))

result={
 'schema':'EM_R1_COARSE_LR_NOT_SUFFICIENT_V1',
 'horizon':3,'alphabet':[0,1,2],
 'positive_histories_checked':40,
 'LR_fiber_constancy_verified_for_t':[0,1,2,3],
 'full_policy_T3':s(t3),
 'full_policy_P_T3_D1':s(P_target),
 'full_policy_Q_T3_D1':s(Q_target),
 'compressed_forced_continue_at_t2':s(u),
 'compressed_pre_action_P_last0':s(pbar[0]),
 'compressed_pre_action_Q_last0':s(qbar[0]),
 'compressed_max_P_T3_D1_given_ratio2':s(P_cap),
 'compressed_max_Q_T3_D1_given_ratio2':s(Q_cap),
 'forced_P_shortfall':s(P_gap),
 'forced_Q_shortfall':s(Q_gap),
 'conditional_gap_Q_minus_2P_by_symbol':separation,
 'status':'EXACT_FRACTION_PASS'
}
print(json.dumps(result,sort_keys=True,indent=2))
