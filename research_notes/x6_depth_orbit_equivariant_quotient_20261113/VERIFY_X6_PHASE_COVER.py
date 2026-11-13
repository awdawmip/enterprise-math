#!/usr/bin/env python3
"""Exact 6m-cycle skew-product lift of a selected compensated C6 quotient orbit."""
import json
from itertools import product,combinations
from collections import Counter,deque
from math import lcm
N=6; ID=tuple(range(1,7))
def gen(i,j,k,l=None):
 a=list(ID);a[i]=j+1;a[j]=k+1;a[k]=-(i+1)
 if l is not None:a[l]=-(l+1)
 return tuple(a)
def compose(f,g):
 return tuple((1 if x>0 else -1)*f[abs(x)-1] for x in g)
def closure(gens):
 done={ID};queue=deque([ID])
 while queue:
  a=queue.popleft()
  for b in gens:
   c=compose(a,b)
   if c not in done:done.add(c);queue.append(c)
 return done
def element_order(g):
 seen=set();factors=[]
 for i in range(N):
  if i in seen:continue
  k=i;n=0;sgn=1
  while k not in seen:
   seen.add(k);v=g[k];sgn*=1 if v>0 else -1;k=abs(v)-1;n+=1
  factors.append(n*(2 if sgn<0 else 1))
 return lcm(*factors)
triads=list(combinations(range(N),3))
G=closure([gen(*t,l) for t in triads for l in range(N) if l not in t])
assert len(G)==11520
counts=Counter(element_order(g) for g in G)
assert set(counts)=={1,2,3,4,5,6,8,10}
assert counts[12]==counts[24]==0
D6mod4=[tuple((t+2*a)%4 for a in v) for t in range(4)
        for v in product((0,1),repeat=N) if sum(v)%2==0]
D6mod4=set(D6mod4)
def add(a,b):return tuple((x+y)%4 for x,y in zip(a,b))
def canon(x):return min(add(x,v) for v in D6mod4)
def act(g,x):
 o=[0]*N
 for j,v in enumerate(g):o[abs(v)-1]=(1 if v>0 else -1)*x[j]
 return tuple(y%4 for y in o)
g=gen(0,1,2,3)
def step(x):return canon(act(g,x))
x0=canon((0,0,1,0,0,0))
cycle=[x0]
for _ in range(5):cycle.append(step(cycle[-1]))
assert len(set(cycle))==6 and step(cycle[-1])==x0
last=cycle[-1]
def lift(x,k,m):return (step(x),(k+int(x==last))%m)
verified={}
for m in (1,2,3,4,5,7):
 st=(x0,0);seen=set()
 for n in range(6*m):
  assert st not in seen
  seen.add(st);st=lift(*st,m)
 assert st==(x0,0) and len(seen)==6*m
 assert {x for x,k in seen}==set(cycle)
 assert {k for x,k in seen}==set(range(m))
 verified[str(m)]={'period':6*m,'states':len(seen),'fiber_cardinality':m}
print(json.dumps({'status':'PASS_X6_SKew_COVER','G_even_order':len(G),
 'G_even_element_orders':dict(sorted(counts.items())),
 'no_single_signed_group_element_of_order_12_or_24':True,
 'selected_original_C6_orbit':cycle,
 'wrap_state':last,'exact_finite_covers':verified},indent=2))
