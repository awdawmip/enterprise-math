#!/usr/bin/env python3
"""R232: exact seven-source Sperner-level spectral collision certificate."""
from fractions import Fraction as F
from itertools import combinations
import json
alpha=tuple(F(p,q) for p,q in [(1,5),(1,4),(3,10),(7,20),(2,5),(3,4),(4,5)])
pi=(F(687,2287),F(455,6861),F(130,2287),F(105,2287),F(455,13722),F(455,2287),F(1365,4574))
assert len(set(alpha))==7 and all(F(0)<v<F(1) for v in alpha)
assert sum(pi)==1 and all(v>0 for v in pi)
b=tuple((1-a)*p for a,p in zip(alpha,pi))
Z,O=F(0),F(1)
def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def add(a,b):
 c=[Z]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return trim(c)
def mul(a,b):
 c=[Z]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]+=u*v
 return trim(c)
def monic(a):
 a=trim(a)
 return [v/a[-1] for v in a] if a!=[Z] else [Z]
def rem(a,b):
 a=trim(a);b=trim(b);assert b!=[Z]
 while a!=[Z] and len(a)>=len(b):
  coef=a[-1]/b[-1];off=len(a)-len(b)
  for j,v in enumerate(b):a[off+j]-=coef*v
  a=trim(a)
 return a
def gcd(a,b):
 while b!=[Z]:a,b=b,rem(a,b)
 return monic(a)
def product(indices):
 p=[O]
 for i in indices:p=mul(p,[-alpha[i],O])
 return p
def killed(mask):
 D=[0]+[i for i in range(1,7) if mask>>(i-1)&1]
 p=product(D)
 for i in D:p=add(p,[-b[i]*v for v in product([j for j in D if j!=i])])
 return monic(p)
polys={m:killed(m) for m in range(63)}
assert sum(len(v)-1 for v in polys.values())+1==250
masks={1,2,4,8,19,21,22,25,26,28,35,37,38,41,42,44,55,59,61,62}
assert len(masks)==20
expected={m for m in range(63) if
          sum(bool(m & (1<<i)) for i in range(4))
          -sum(bool(m & (1<<i)) for i in (4,5))==1}
assert expected==masks
assert all(sum(bool(m & (1<<i)) for i in range(4))+
               sum(not bool(m & (1<<i)) for i in (4,5))==3 for m in masks)
lam=F(1,2);c=F(455,2287)
assert b[0]/(lam-alpha[0])==1-c
assert all(b[i]/(lam-alpha[i])==c for i in (1,2,3,4))
assert all(b[i]/(lam-alpha[i])==-c for i in (5,6))
assert {m for m,p in polys.items() if sum(v*lam**i for i,v in enumerate(p))==0}==masks
for p in polys.values():
 assert gcd(p,[F(i)*v for i,v in enumerate(p)][1:])==[O]
 assert sum(p)!=0
collisions=[]
for m,n in combinations(range(63),2):
 d=gcd(polys[m],polys[n])
 if len(d)>1:
  assert d==[-lam,O],(m,n,d)
  collisions.append((m,n))
assert len(collisions)==190
assert all(m in masks and n in masks for m,n in collisions)
rank=1+sum(len(p)-1 for p in polys.values())-(len(masks)-1)
assert rank==231
result={"schema":"R232_EXACT_CERTIFICATE_V1","status":"PASS","k":6,
 "source_count":7,"proper_blocks":63,"generic_degree_upper":250,
 "observed_minimal_recurrence_order":231,"shared_rational_mode":"1/2",
 "blocks_with_shared_mode":sorted(masks),
 "nontrivial_pairwise_gcd_count":len(collisions),
 "all_nontrivial_gcds":"x-1/2","pairwise_gcd_checks":1953,
 "squarefree_block_checks":63,"arithmetic":"exact fractions.Fraction",
 "native_BRC_integration":"NOT_EXECUTED","independent_review":"NOT_REVIEWED"}
print(json.dumps(result,ensure_ascii=False,indent=2))
