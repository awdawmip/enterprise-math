#!/usr/bin/env python3
"""R98: exact scaled-integer check of a conditional BRC count observer.
This is neither native X6 evolution nor a phase/signed-amplitude calculation.
"""
from math import lcm
P_MAX = 40
PAIRS = [(1,1),(1,11),(1,12),(1,23),(1,25),(5,23),(6,12),(11,11),
         (11,12),(13,25),(25,25),(100,100),(100,12),(12,100),
         (1000,1000),(5,1)]
PORTS = (11,15,26,27,28,38,40)

def q(x,y,z):
    return max(max(x,0)+max(y,0)+max(z,0),
               max(-x,0)+max(-y,0)+max(-z,0))

def directions(pmax):
    for x in range(-pmax,pmax+1):
      for y in range(-pmax,pmax+1):
       for z in range(-pmax,pmax+1):
        if not (x or y or z):
            continue
        p=q(x,y,z)
        if p>pmax:continue
        first=x if x else (y if y else z)
        if first<0:continue
        yield p,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z

vectors=list(directions(P_MAX))
assert len(vectors)==110740
cases=0
for S,T in PAIRS:
    D=lcm(2,S+1,T+1,S+T)
    f0=D//2
    fd=12*D//(T+1)
    fb=max(3*D//(S+1),6*D//(T+1))
    fc=6*D//(S+1)
    low=min(f0,fd,fb)
    high=min(low,fc)
    minima=[None]*(P_MAX+1)
    for p,u,v,h in vectors:
        F=max(abs(u)*D//2,abs(v)*D//(S+1),abs(h)*D//(T+1),
              abs(v-u)*D//(S+1),abs(h-u)*D//(T+1),
              abs(h-v)*D//(S+T))
        old=minima[p]
        if old is None or F<old:minima[p]=F
    current=None
    for p in range(P_MAX+1):
        if minima[p] is not None:
            current=minima[p] if current is None else min(current,minima[p])
        minima[p]=current
    for p in PORTS:
        expected=low if p<=26 else high
        assert minima[p]==expected,(S,T,p,minima[p],expected)
        cases+=1
assert cases==112
print({"status":"PASS","directions":len(vectors),
       "integer_weight_pairs":len(PAIRS),"port_budgets":len(PORTS),
       "cases":cases,"arithmetic":"exact integer with common LCM scaling"})
