#!/usr/bin/env python3
"""EC48X exact two-source positive-weighted branch model and policy simulation.
Finite auxiliary branch arithmetic only; NOT native X6/BRC-Shor execution.
"""
from fractions import Fraction as F
from itertools import product
import json, random

H=(0,1); W=(0,1); Z=(0,1)
rho={0:F(1,2),1:F(1,2)}
w1={0:F(3,4),1:F(1,4)}
ZP={0:F(1,4),1:F(3,4)}
ZQ={0:F(3,4),1:F(1,4)}
K={(h,w):w1[h] if w else 1-w1[h] for h in H for w in W}
leaves={}
for h,w,z in product(H,W,Z):
    leaves[(h,w,z)]={'P':rho[h]*K[(h,w)]*ZP[z],
                     'Q':rho[h]*K[(h,w)]*ZQ[z]}
assert all(u['P']>0 and u['Q']>0 for u in leaves.values())
assert sum(u['P'] for u in leaves.values())==1
assert sum(u['Q'] for u in leaves.values())==1
assert all(u['P']/u['Q']==(F(3) if key[2] else F(1,3)) for key,u in leaves.items())

raw_vectors=set(); exhaustive=0
for first in product(range(3),repeat=2):
    # 0 stop/reject, 1 stop/accept, 2 continue for the two H branches
    A=sum((rho[h] for h in H if first[h]==1),F(0))
    C=sum((rho[h] for h in H if first[h]==2),F(0))
    B=1-A-C
    for final in product((0,1),repeat=8):
        d=dict(zip(product(H,W,Z),final))
        N={z:sum((rho[h]*K[(h,w)]*d[(h,w,z)]
                  for h in H if first[h]==2 for w in W),F(0)) for z in Z}
        assert all(F(0)<=N[z]<=C for z in Z)
        alpha=A+sum(ZP[z]*N[z] for z in Z)
        beta=A+sum(ZQ[z]*N[z] for z in Z)
        def fine(s):
            early=sum((rho[h] for h in H if first[h]==1),F(0))
            late=sum((leaves[(h,w,z)][s]*d[(h,w,z)]
                     for h,w,z in product(H,W,Z) if first[h]==2),F(0))
            time=sum((rho[h]*(1 if first[h]!=2 else 2) for h in H),F(0))
            return early+late,time
        assert fine('P')==(alpha,1+C)
        assert fine('Q')==(beta,1+C)
        # Implement with one register; decision at t=1 no longer knows H.
        accept_z={z:N[z]/C if C else F(0) for z in Z}
        assert all(F(0)<=accept_z[z]<=1 for z in Z)
        compressed_P=A+C*sum(ZP[z]*accept_z[z] for z in Z)
        compressed_Q=A+C*sum(ZQ[z]*accept_z[z] for z in Z)
        assert (alpha,beta,1+C,1+C)==(compressed_P,compressed_Q,1+C,1+C)
        raw_vectors.add((alpha,beta,1+C,1+C))
        exhaustive+=1
assert exhaustive==2304

rng=random.Random(48028)
random_checks=512
for _ in range(random_checks):
    pi={}
    for h in H:
        v=[rng.randrange(1,10) for _ in range(3)]
        pi[h]=tuple(F(x,sum(v)) for x in v)
    acc={key:F(rng.randrange(9),8) for key in leaves}
    A=sum((rho[h]*pi[h][1] for h in H),F(0))
    C=sum((rho[h]*pi[h][2] for h in H),F(0))
    N={z:sum((rho[h]*pi[h][2]*K[(h,w)]*acc[(h,w,z)]
             for h in H for w in W),F(0)) for z in Z}
    assert all(F(0)<=N[z]<=C for z in Z)
    for s,nu in (('P',ZP),('Q',ZQ)):
        val=sum((rho[h]*pi[h][1] for h in H),F(0))
        val+=sum((leaves[(h,w,z)][s]*pi[h][2]*acc[(h,w,z)]
                   for h,w,z in product(H,W,Z)),F(0))
        assert val==A+sum(nu[z]*N[z] for z in Z)

assert K[(0,1)]==F(3,4) and K[(1,1)]==F(1,4)
assert K[(0,1)]!=K[(1,1)]
assert ZP[1]!=ZQ[1]
Rfine=rho[0]*K[(0,1)]
Rcoarse_bound=F(1,2)*sum((rho[h]*K[(h,1)] for h in H),F(0))
assert Rfine==F(3,8) and Rcoarse_bound==F(1,4)
assert Rfine-Rcoarse_bound==F(1,8)

fmt=lambda x: str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
summary={
 'unit':'EC48X',
 'scope':'auxiliary two-source finite positive rational weighted branch probability',
 'not_native_X6_or_signed_BRC':True,
 'eight_positive_leaves':[{'h':h,'w':w,'z':z,'P':fmt(leaves[(h,w,z)]['P']),
                            'Q':fmt(leaves[(h,w,z)]['Q']),
                            'LR':fmt(leaves[(h,w,z)]['P']/leaves[(h,w,z)]['Q'])}
                           for h,w,z in product(H,W,Z)],
 'full_deterministic_policies_exhausted':exhaustive,
 'distinct_full_deterministic_raw_vectors':len(raw_vectors),
 'rational_randomized_policies_exactly_checked':random_checks,
 'one_register_preserves_all_four_coordinates':True,
 'nonlumpable_W_kernel':['3/4','1/4'],
 'informative_Z_PQ':['3/4','1/4'],
 'fifth_observer_fine':'3/8',
 'fifth_observer_one_register_upper_bound':'1/4',
 'fifth_observer_gap':'1/8',
 'analytic_general_policy_proof':'see PROOF.md X2',
 'analytic_causal_sufficiency_proof':'see PROOF.md X1',
 'native_execution':False,
 'formal_admission':False
}
with open('EXACT_REPORT.json','w',encoding='utf-8') as f:
    json.dump(summary,f,indent=2,ensure_ascii=False)
    f.write('\n')
print(json.dumps({key:summary[key] for key in
  ('full_deterministic_policies_exhausted','distinct_full_deterministic_raw_vectors',
   'rational_randomized_policies_exactly_checked','fifth_observer_gap')},indent=2))
