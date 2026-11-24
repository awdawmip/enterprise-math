"""Finite row geometry, explicit witnesses and symbolic counting checks."""
from math import gcd, prod, isqrt
from itertools import combinations, product, permutations
from fractions import Fraction
import json

A={1,2,10,11,12,16,17,22,25,26,30,31,32}
P={7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417}
R2_fixed={2,3}|P|{5,13,11,61,331,19,37,73,109,433,38737}
def prime(q):
    return q>1 and all(q%d for d in range(2,isqrt(q)+1))
def order(q,b):
    p=pow(2,b,q); x=p;k=1
    while x!=1:x=x*p%q;k+=1
    return k
def factors(x):
    p=2;r={}
    while p*p<=x:
        while x%p==0:r[p]=r.get(p,0)+1;x//=p
        p+=1
    if x>1:r[x]=1
    return r

# Covers of grid minus the marked point by full lines avoiding the point.
geo={}
for r in range(3):
    D={(a-r)*pow(3,-1,35)%35 for a in A}
    covers={}
    for t in sorted(D):
        lines=[(m,b,{u for u in D if u%m==b}) for m in (5,7) for b in range(m) if b!=t%m]
        valid=[]
        for k in range(5):
            for c in combinations(lines,k):
                if set().union(*(l[2] for l in c))==D-{t}:
                    assert k==4
                    valid.append([[m,b] for m,b,s in c])
        if valid:covers[t]=valid
    assert set(covers)=={(a-r)*pow(3,-1,35)%35 for a in (10,25,30)}
    assert all(len(v)==1 for v in covers.values())
    geo[r]=covers
assert set(geo[2])=={21,26,31}

F36=factors(2**36-1)
assert set(F36)-R2_fixed==set() and (set(F36)-P-{3,5,13,37,109})=={19,73}
F60=factors(2**60-1)
assert [q for q in F60 if q not in R2_fixed and order(q,12)==5]==[]

P5=(181,631,23311,54001,18837001,29247661)
P7=(29,43,1429,5419,92737,649657,40388473189,77158673929,118750098349)
assert all(order(q,36)==5 and order(q,12)==15 for q in P5)
assert all(order(q,36)==7 for q in P7)

# All eight abstract row-slot assignments and all three highest possible slots.
plans=[]
for periods in product((7,35),repeat=3):
  if 35 not in periods:continue
  for k in (i for i,m in enumerate(periods) if m==35):
    shape=[(5,0),(5,3)]+[(m,t%m) for m,t in zip(periods,(21,26,31))]
    B={u for u in range(70) if (2+3*u)%35 in A}
    private=[]
    for i,(m,b) in enumerate(shape):
      pp=[u for u in B if u%2==0 and [j for j,(l,c) in enumerate(shape) if u%l==c]==[i]]
      assert pp
      private.append(len(pp))
    assert all(any(u%m==b for m,b in shape) for u in B)
    plans.append({'tail_periods':periods,'highest_slot':(21,26,31)[k],'even_private_counts':private})
assert len(plans)==12

# Verify weighted inclusion-exclusion formula on explicit small trial sizes.
S=(7,11,13,17,19); H={13,17}
def weight(ps,k,s):
    return prod(2 if a is not None else q-2*k for q,a in zip(ps,s))
brute=sum(weight(S,3,s) for s in product([0,1,2,None],repeat=len(S))
          if all(i in s for i in range(3)) and any(a is not None for q,a in zip(S,s) if q in H))
from math import comb
ie=sum((-1)**j*comb(3,j)*
      (prod(q-2*j for q in S)-prod(q-6 if q in H else q-2*j for q in S))
      for j in range(4))
assert ie==brute
print(json.dumps({'row_geometry_by_phase':geo,'abstract_marked_assignments':plans,
                  'two_power_36_factorization':F36,'two_power_60_factorization':F60,
                  'weighted_occupancy_control':str(Fraction(ie,prod(S)))},indent=2))
