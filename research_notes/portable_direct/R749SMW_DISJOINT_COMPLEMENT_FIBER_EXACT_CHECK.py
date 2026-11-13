#!/usr/bin/env python3
"""R749SMW exact rational certificate for disjoint-edge B-Walsh fiber."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json

C = (1, 2, 4, 8, 15)
B = tuple(a for a in range(1,16) if a not in C)
TARGET = {3:F(1,2), 12:F(1,2)}

def chi(a,x):
    return 1 if ((a & x).bit_count() % 2 == 0) else -1

def gauss(A,b):
    n=len(b)
    T=[[F(y) for y in row]+[F(bi)] for row,bi in zip(A,b)]
    for j in range(n):
        p=next((i for i in range(j,n) if T[i][j]),None)
        if p is None:
            return None
        T[j],T[p]=T[p],T[j]
        q=T[j][j]; T[j]=[v/q for v in T[j]]
        for i in range(n):
            if i != j and T[i][j]:
                q=T[i][j]; T[i]=[v-q*w for v,w in zip(T[i],T[j])]
    return tuple(row[-1] for row in T)

def tv(p,q):
    return sum(abs(a-b) for a,b in zip(p,q))/2

def mom(p,a):
    return sum(p[x]*chi(a,x) for x in range(16))

def full_source(z):
    return tuple((F(1)+TARGET[3]*chi(3,x)+TARGET[12]*chi(12,x)
           +sum(z[i]*chi(a,x) for i,a in enumerate(C)))/16 for x in range(16))

vertices=set(); nonsing=0; feas=0
for inds in combinations(range(16),5):
    A=[[chi(a,x) for a in C] for x in inds]
    b=[-1-TARGET[3]*chi(3,x)-TARGET[12]*chi(12,x) for x in inds]
    z=gauss(A,b)
    if z is None:
        continue
    nonsing+=1
    p=full_source(z)
    if min(p)<0:
        continue
    feas+=1
    assert sum(p)==1
    assert all(mom(p,a)==TARGET.get(a,0) for a in B)
    vertices.add(p)

q_opt=tuple(F(3,20) if chi(3,x)==chi(12,x)==1 else
           (F(1,20) if chi(3,x)!=chi(12,x) else F(0)) for x in range(16))
q_cal=tuple((F(1)+F(1,2)*chi(3,x)+F(1,2)*chi(12,x)
             +F(2,11)*chi(15,x))/16 for x in range(16))
assert min(q_opt)>=0 and sum(q_opt)==1
assert min(q_cal)>=0 and sum(q_cal)==1
assert all(mom(q_cal,a)==TARGET.get(a,0) for a in B)
assert (mom(q_opt,3),mom(q_opt,12))==(F(3,5),F(3,5))

w1=[F(0)]*16
for x in (3,7,11,12,13,14): w1[x]=F(1,8)
w1[15]=F(1,4)
w1=tuple(w1)
w2=tuple(F(3,16) if chi(3,x)==chi(12,x)==1 else
         F(1,16) if chi(3,x)==chi(12,x)==-1 else F(0) for x in range(16))
assert all(mom(w,a)==TARGET.get(a,0) for w in (w1,w2) for a in B)
assert w1 in vertices and w2 in vertices
S1={7,11,13,14,15}
S2={0,3,5,6,9,10,12,15}
assert sum(w1[x] for x in S1)==F(3,4)
assert sum(w2[x] for x in S2)==1
assert sum(q_opt[x] for x in S1)==F(7,20)
assert sum(q_opt[x] for x in S2)==F(3,5)
assert (F(4,5)*(F(3,4)-sum(q_opt[x] for x in S1))+
        F(1,5)*(1-sum(q_opt[x] for x in S2)))==F(2,5)

hist_opt=Counter(str(tv(q_opt,p)) for p in vertices)
hist_cal=Counter(str(tv(q_cal,p)) for p in vertices)
assert len(vertices)==17 and nonsing==3008 and feas==456
assert max(tv(q_opt,p) for p in vertices)==F(2,5)
assert max(tv(q_cal,p) for p in vertices)==F(9,22)
assert F(8,11)*F(3,8)+F(3,11)*F(1,2)==F(9,22)
assert F(8,11)*F(3,16)-F(3,11)*F(1,2)==0

output={
 'schema':'R749SMW_DISJOINT_COMPLEMENT_FIBER_EXACT_V1',
 'status':'PASS',
 'mathematical_domain':'F2^4; B ten Walsh masks; moments m_3=m_12=1/2, all other retained B moments zero',
 'source_mask_C':C,'retained_mask_B':B,
 'basis_sets_checked':4368,'nonsingular_bases':nonsing,
 'feasible_bases':feas,'distinct_fiber_vertices':len(vertices),
 'unrestricted_exact_minimax_TV':'2/5',
 'calibrated_exact_minimax_TV':'9/22',
 'strict_calibration_penalty':'1/110',
 'unrestricted_vertex_distance_histogram':dict(sorted(hist_opt.items())),
 'calibrated_vertex_distance_histogram':dict(sorted(hist_cal.items())),
 'uncalibrated_decoder_sign_class_masses':{'++':'3/5','+-':'1/5','-+':'1/5','--':'0'},
 'uncalibrated_decoder_retained_moments':{'3':'3/5','12':'3/5'},
 'calibrated_decoder_walsh_15':'2/11',
 'lower_witness_events':{'S1':sorted(S1),'w1_event_mass':'3/4','S2':sorted(S2),'w2_event_mass':'1'},
 'exact_arithmetic':'Python fractions.Fraction only; all feasible five-active vertices enumerated, no floating point',
 'proof_boundary':'Constrained single rational fiber and GL(4,2)/translation orbit; global nonlinear minimax and native V29/V39 bridge remain open.'
}
print(json.dumps(output,ensure_ascii=False,indent=2))
