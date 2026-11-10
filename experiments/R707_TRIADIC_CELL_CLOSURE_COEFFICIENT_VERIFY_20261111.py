#!/usr/bin/env python3
"""R707 exact Cell-attached canonical equal-quantum triad decomposition checker."""
from itertools import combinations,permutations,product
from functools import lru_cache
from math import factorial
D=6; triples=list(combinations(range(D),3));assert len(triples)==20
@lru_cache(None)
def coeff(n):
 if not any(n):return 1
 if sum(n)%3:return 0
 return sum(coeff(tuple(n[i]-int(i in t) for i in range(D)))
            for t in triples if all(n[i] for i in t))
def formula(n):
 if sum(n)%3:return 0
 m=sum(n)//3;a=coeff(tuple(n))
 prod=1
 for j in n:prod*=factorial(j)
 assert (a*prod)%factorial(m)==0
 return a*prod//factorial(m)
@lru_cache(None)
def direct(n):
 if not any(n):return 1
 a=next(i for i,x in enumerate(n) if x)
 result=0
 for i,j in combinations((i for i in range(6) if i!=a and n[i]),2):
  nxt=list(n);nxt[a]-=1;nxt[i]-=1;nxt[j]-=1
  result+=n[i]*n[j]*direct(tuple(nxt))
 return result
checked=0
for n in product(range(3),repeat=6):
 if sum(n)>9 or sum(n)%3:continue
 assert formula(n)==direct(n),(n,formula(n),direct(n))
 checked+=1
assert checked==242
assert formula((2,2,2,0,0,0))==4
assert formula((1,1,1,1,1,1))==10
for m in range(1,7):assert formula((m,m,m,0,0,0))==factorial(m)**2
for i,j in combinations(range(D),2):
 assert len([t for k in range(D) if k not in {i,j} for t in (-1,1)])==8
 assert sum(6 for k in range(D) if k not in {i,j} for t in (-1,1))==48
for n in ((2,2,2,0,0,0),(1,1,1,1,1,1),(2,1,2,0,1,0)):
 a=formula(n)
 for perm in permutations(range(6)):
  z=[0]*6
  for i,j in enumerate(perm):z[j]=n[i]
  assert formula(tuple(z))==a
print("R707_X6_CELL_TRIAD_COEFFICIENT_EXACT_PASS",checked,4,10)
