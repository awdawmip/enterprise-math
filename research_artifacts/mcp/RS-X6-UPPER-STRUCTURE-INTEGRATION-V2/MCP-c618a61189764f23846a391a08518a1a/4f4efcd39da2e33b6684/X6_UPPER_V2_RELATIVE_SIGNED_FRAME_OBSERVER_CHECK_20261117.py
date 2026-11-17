#!/usr/bin/env python3
from itertools import permutations,product
from math import factorial
N=6
D=(1,)*N; Z=(0,)*N
def can(z): m=min(z);return tuple(x-m for x in z)
def even(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2==0
def act(p,e,z):return tuple(e[i]*z[p[i]] for i in range(N))
P=[p for p in permutations(range(N)) if even(p)]
assert len(P)==factorial(6)//2
good=bad=0
for p in P:
 for e in product((-1,1),repeat=N):
  ok=can(act(p,e,D))==Z
  assert ok==(len(set(e))==1)
  good+=ok;bad+=not ok
  z=(0,2,-1,3,1,-2); z3=tuple(x+3 for x in z)
  assert can(z)==can(z3)
  assert (can(act(p,e,z))==can(act(p,e,z3)))==ok
assert (good,bad)==(720,22320)
J=(-1,-1,-1,1,1,1); I=tuple(range(N))
assert can(act(I,J,D))==(0,0,0,2,2,2)
for m in (1,2,3,5,17):
 assert can(act(I,J,(m,)*N))==(0,0,0,2*m,2*m,2*m)
print('frame-group',good+bad,'observer-safe',good,'unsafe',bad)
