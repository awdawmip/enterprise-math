#!/usr/bin/env python3
"""Exact R749SSI certificate. Pure Python standard-library integer arithmetic.

The companion paper supplies the generating-function quasi-polynomial degree
bound needed to promote the Newton-tail calculation to an infinite proof.
"""
from math import comb
from fractions import Fraction
import json

QTAIL = 5070
STEPS = 14
N = QTAIL + 5 + 6*STEPS + 6 + 1
WEIGHTS = (1, 1, 2, 3, 6)
A = tuple(map(Fraction, ('3335/3','13780/9','12845/9','3740/3',
                         '11485/9','12980/9')))

shell=[0]*N
shell[0]=1
for w in WEIGHTS:
    for m in range(w,N):
        shell[m]+=shell[m-w]
mark_shell=[0]*N
for m in range(1,N):
    mark_shell[m]=mark_shell[m-1]+shell[m-1]
C=[0]*N
T=[0]*N
for q in range(1,N):
    C[q]=C[q-1]+shell[q-1]
    T[q]=T[q-1]+mark_shell[q-1]
assert [(C[q],T[q]) for q in (5,6,7,8,11,28)] == [
    (25,25),(41,50),(65,91),(98,156),(281,600),(10126,51356)]

def S(q):
    return 18*q**4+54*q**3-345*q**2+2070*q-16315

def diff_numerator(q,e,d):
    cp,cq=C[q+6]+d,C[q]+d
    return (108*((q+6)**3*(T[q+6]+e)*cq-q**3*(T[q]+e)*cp)
            -(S(q+6)-S(q))*cp*cq)

def newton_diffs(vals):
    ans=[]
    while vals:
        ans.append(vals[0])
        vals=[vals[i+1]-vals[i] for i in range(len(vals)-1)]
    return ans

# D(q) is a degree <=14 polynomial separately on each residue for q>=36.
# Complete signed Newton coefficients certify all q>=5070.
tail_cert_count=0
min_signed_nonzero=None
nonzero_degree_counts={}
for r in range(6):
    for d in range(-2,3):
        sign=1 if A[r]-720*d<0 else -1
        for e in range(-2,3):
            vals=[sign*diff_numerator(QTAIL+r+6*j,e,d)
                  for j in range(STEPS+1)]
            delta=newton_diffs(vals)
            assert delta[0]>0 and all(z>=0 for z in delta),(r,e,d)
            assert all(z==0 for z in delta[9:]),(r,e,d)
            assert delta[8]>0
            assert Fraction(delta[8],6**8*40320)==abs(A[r]-720*d)/28800
            nz=max(i for i,v in enumerate(delta) if v)
            nonzero_degree_counts[nz]=nonzero_degree_counts.get(nz,0)+1
            tail_cert_count+=1
            here=min(z for z in delta if z>0)
            min_signed_nonzero=here if min_signed_nonzero is None else min(min_signed_nonzero,here)

# All finite q<5070, independent of the Newton-tail certificate.
finite_checks=0
last_failing_q=None
last_failure=None
bad_count=0
for q in range(6,QTAIL):
    r=q%6
    for d in range(-2,3):
        sign=1 if A[r]-720*d<0 else -1
        for e in range(-2,3):
            z=sign*diff_numerator(q,e,d)
            finite_checks+=1
            if z<=0:
                bad_count+=1
                if last_failing_q is None or q>=last_failing_q:
                    last_failing_q=q
                    last_failure=[q,r,e,d,'zero' if z==0 else 'opposite_sign']
assert last_failure==[5066,2,2,2,'opposite_sign'],last_failure

# Separate exact collision search, 6<=q<=10000; finite scope only.
SEARCH_LAST=10000
Q=SEARCH_LAST+1
shell2=[0]*Q
shell2[0]=1
for w in WEIGHTS:
    for m in range(w,Q):
        shell2[m]+=shell2[m-w]
mark2=[0]*Q
for m in range(1,Q):
    mark2[m]=mark2[m-1]+shell2[m-1]
seen={}
collisions=[]
running_c=0
running_t=0
for q in range(1,Q):
    running_c+=shell2[q-1]
    running_t+=mark2[q-1]
    if q<6:
        continue
    for e in range(-2,3):
        for d in range(-2,3):
            den=108*(running_c+d)
            num=108*q**3*(running_t+e)-S(q)*(running_c+d)
            val=Fraction(num,den)
            if val in seen:
                collisions.append([seen[val],[q,e,d]])
            else:
                seen[val]=[q,e,d]
assert not collisions,collisions[:3]
assert len(seen)==(SEARCH_LAST-5)*25

result={
  'unit':'R749SSI',
  'status':'PASS',
  'frozen_science_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
  'universal_eventual_monotonicity_start':5067,
  'last_direction_failure':last_failure,
  'tail_base':QTAIL,
  'tail_polynomial_degree_bound':STEPS,
  'actual_nonzero_newton_degree_counts':nonzero_degree_counts,
  'positive_tail_certificates':tail_cert_count,
  'minimum_positive_newton_coefficient_numerator':str(min_signed_nonzero),
  'finite_signed_comparisons':finite_checks,
  'finite_sign_failure_count':bad_count,
  'Y_exact_collision_search_cutoffs':[6,SEARCH_LAST],
  'exact_readouts_compared':len(seen),
  'exact_collisions_found':len(collisions),
  'phase_limits':['455/36','-295/36','-25/36','185/36','-25/36','-295/36'],
  'phase_first_order_coefficients':[str(a) for a in A],
  'limitation':'Y unknown-cutoff global exact injectivity remains unproved'
}
with open('R749SSI_SIX_SHIFT_EVENTUAL_MONOTONICITY_RESULTS.json','w') as f:
    json.dump(result,f,ensure_ascii=False,indent=2,sort_keys=True)
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
