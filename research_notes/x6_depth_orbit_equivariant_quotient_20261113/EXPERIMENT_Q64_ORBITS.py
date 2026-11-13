#!/usr/bin/env python3
"""Exhaustively classify all 64 finite states of Q_even under 60 C6 lifts."""
from itertools import combinations,product
from collections import Counter
import json
N=6
I=tuple(range(1,N+1))
triads=list(combinations(range(N),3))
def gen(i,j,k,l):
    a=list(I);a[i]=j+1;a[j]=k+1;a[k]=-(i+1);a[l]=-(l+1);return tuple(a)
def act(g,v):
    o=[0]*N
    for i,x in enumerate(g):o[abs(x)-1]=(1 if x>0 else -1)*v[i]
    return tuple(y%4 for y in o)
L=list(set(tuple((t+2*a)%4 for a in v) for t in range(4) for v in product((0,1),repeat=N) if sum(v)%2==0))
assert len(L)==64
def add(x,y):return tuple((a+b)%4 for a,b in zip(x,y))
ambient=list(product(range(4),repeat=N))
reps={x:min(add(x,y) for y in L) for x in ambient}
assert len(set(reps.values()))==64
states=sorted(set(reps.values()))
ops=[gen(*t,l) for t in triads for l in range(N) if l not in t]
def jump(s,g):return reps[act(g,s)]
unseen=set(states);orbits=[]
while unseen:
    seed=min(unseen);Q=[seed];seen={seed};k=0
    while k<len(Q):
        x=Q[k];k+=1
        for g in ops:
            y=jump(x,g)
            if y not in seen:seen.add(y);Q.append(y)
    unseen-=seen;orbits.append({'size':len(seen),'seed':seed,'members':sorted(seen)})
orbits.sort(key=lambda o:o['size'],reverse=True)
assert sorted(o['size'] for o in orbits)==[1,1,12,20,30]
p=ops[0];unvisited=set(states);cycles=Counter()
while unvisited:
    x=next(iter(unvisited));y=x;n=0
    while True:
        assert y in unvisited
        unvisited.remove(y);n+=1;y=jump(y,p)
        if y==x:break
    cycles[n]+=1
assert dict(cycles)=={1:8,2:4,3:8,6:4}
print(json.dumps({'status':'PASS_Q64_ORBITS','orbit_sizes':[o['size'] for o in orbits],
 'orbit_seeds':[o['seed'] for o in orbits],
 'one_compensated_C6_cycle_counts':dict(sorted(cycles.items())),
 'complete_mod4_population':len(ambient),
 'quotient_states':len(states),'compensated_generators':len(ops)},indent=2))
