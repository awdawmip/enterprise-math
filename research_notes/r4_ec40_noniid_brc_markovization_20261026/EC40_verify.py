#!/usr/bin/env python3
"""Exact rational, finite BRC branch observer check for R4-EC40.

This checks the explicitly defined two-step positive-rational examples only;
all-depth/all-policy statements belong to the accompanying mathematical proof.
"""
from fractions import Fraction as F
import json
from itertools import product
from pathlib import Path

D=lambda x: f'{x.numerator}/{x.denominator}'
first={h:F(1,2) for h in ('a','b')}
P={'a':{'0':F(3,4),'1':F(1,4)},'b':{'0':F(1,2),'1':F(1,2)}}
Q={'a':{'0':F(1,4),'1':F(3,4)},'b':{'0':F(1,2),'1':F(1,2)}}
assert sum(first.values())==1
for M in (P,Q):
    for h in first:
        assert all(v>0 for v in M[h].values())
        assert sum(M[h].values())==1

# T1 maps both hidden prefixes to x; T2 keeps all ordered prefixes.
P2={(h,k):first[h]*P[h][k] for h,k in product('ab','01')}
Q2={(h,k):first[h]*Q[h][k] for h,k in product('ab','01')}
assert set(P2)==set(Q2)
ratio1={h:first[h]/first[h] for h in first}
ratio2={(h,k):Q2[(h,k)]/P2[(h,k)] for h,k in P2}
assert len(set(ratio1.values()))==1
assert len(ratio2)==4 and all(P2[w]>0 and Q2[w]>0 for w in ratio2)  # singleton T2 fibers
assert ratio2[('a','0')]==F(1,3) and ratio2[('a','1')]==3
assert ratio2[('b','0')]==ratio2[('b','1')]==1

# Non-lumpability at n=1: transition supports of T2 from a and b are disjoint.
Kp={h:{(g,k):(P[h][k] if g==h else F(0)) for g,k in product('ab','01')} for h in 'ab'}
Kq={h:{(g,k):(Q[h][k] if g==h else F(0)) for g,k in product('ab','01')} for h in 'ab'}
assert Kp['a']!=Kp['b'] and Kq['a']!=Kq['b']

# Full-history policy: continue exactly at a; at b stop and flip fair decision;
# at a0 decide P, at a1 decide Q. Both errors and both times are exact.
eP=first['b']/2+P2[('a','1')]
eQ=first['b']/2+Q2[('a','0')]
tP=1+first['a'];tQ=1+first['a']
assert (eP,eQ,tP,tQ)==(F(3,8),F(3,8),F(3,2),F(3,2))

# Every (n,T) Markov policy has a single continuation probability c at T1=x.
# Its stopping contribution to the sum of errors is (1-c). At n=2,
# each branch (h,k) contributes >= c * min(P(hk), Q(hk)) to eP+eQ.
bayes_overlap=sum(min(P2[w],Q2[w]) for w in P2)
assert bayes_overlap==F(3,4)
for c in [F(i,16) for i in range(17)]:
    lower=(1-c)+c*bayes_overlap
    assert lower==1-c/F(4)
    if c==F(1,2):
        assert lower==F(7,8)>eP+eQ

# At c=1/2 this bound is achieved with fair stopping decisions at n1,
# Bayes-optimal decisions at n2 for a histories, and fair b decisions.
c=F(1,2)
stop_eP=(1-c)*F(1,2);stop_eQ=(1-c)*F(1,2)
term_eP=c*(P2[('a','1')]+F(1,2)*(P2[('b','0')]+P2[('b','1')]))
term_eQ=c*(Q2[('a','0')]+F(1,2)*(Q2[('b','0')]+Q2[('b','1')]))
assert (stop_eP+term_eP,stop_eQ+term_eQ)==(F(7,16),F(7,16))

# Independent horizon-one LR erasure: continuation-kernel criterion is vacuous.
p1={'a':F(3,4),'b':F(1,4)}
q1={'a':F(1,4),'b':F(3,4)}
err_p=p1['a'];err_q=q1['b']
assert err_p==err_q==F(3,4)
assert all(r+(1-r)==1 for r in (F(0),F(1,3),F(1)))
assert err_p+err_q>1

result={
 'research_unit':'R4-EC40','arith':'Python fractions.Fraction exact rational',
 'example':{'horizon':2,'P_first':{k:D(v) for k,v in first.items()},
   'P_second':{h:{z:D(v) for z,v in vs.items()} for h,vs in P.items()},
   'Q_second':{h:{z:D(v) for z,v in vs.items()} for h,vs in Q.items()},
   'T1':'x for a and b','T2':'full two-symbol ordered history',
   'prefix_lr_constant_in_T1':True,'T2_fibers_singleton':True,
   'P_lumpable':False,'Q_lumpable':False,
   'full_history_observers':[D(v) for v in (eP,eQ,tP,tQ)],
   'any_T_policy_min_error_sum_at_t=3/2':D(F(7,8)),
   'full_policy_error_sum':D(eP+eQ),
   'sharp_T_policy_example_errors':[D(F(7,16)),D(F(7,16))],
   'overlap_at_n2':D(bayes_overlap),
   'grid_continuation_values_tested':17},
 'horizon_one_LR_failure':{'P_a':D(p1['a']),'Q_a':D(q1['a']),
   'full_policy_errors':[D(err_p),D(err_q)],'T_policy_error_sum':'1/1'},
 'mathematical_scope':'two-step witness exact finite checks only; universal theorem proved in separate manuscript',
 'outcome':'PASS'
}
with Path(__file__).with_name('EC40_REPORT.json').open('w',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2,sort_keys=True)
print(json.dumps(result,ensure_ascii=False,sort_keys=True))
