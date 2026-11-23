#!/usr/bin/env python3
"""R133: exact rational first set-change on all orthant rays of two Port-10 centers.
The ray parameter is 0<=t<1, with physical four-positive-weight BRC six-pair observer.
"""
from fractions import Fraction as Q
from itertools import product

BANK=[(1,0,0),(0,2,-1),(1,-3,1),(2,-3,1),(3,-1,0),
      (1,3,-1),(3,-4,1),(4,-1,0),(3,2,-1),(4,-4,1),
      (5,-1,0),(5,-4,1),(6,-1,0),(3,-7,2),(6,-4,1),
      (7,-1,0),(7,2,-1),(9,-5,1)]
PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def port(a):
    return max(sum(max(z,0) for z in a),sum(max(-z,0) for z in a))

def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[i]-h[j]) for i,j in PAIRS)

V=[a for a in product(range(-10,11),repeat=3)
   if any(a) and next(z for z in a if z)!=0
   and next(z for z in a if z)>0 and port(a)<=10]
assert len(V)==1935
G={a:gaps(a) for a in V}
assert len(set(BANK))==18
assert all(any(all(u<=v for u,v in zip(gaps(b),G[a]))
               for b in BANK) for a in V)
E=[a for a in V if not any(
       all(2*u>=3*v for u,v in zip(G[a],gaps(b))) for b in BANK)]
assert len(E)==20
print("FULL FINITE INPUT: 1935 directions; B18 dominance PASS; E20 exclusion PASS")

def capacities(w):
    return tuple(w[i]+w[j] for i,j in PAIRS)

def score(a,s):
    return max(Q(x,y) for x,y in zip(gaps(a),s))

def near(w):
    s=capacities(w)
    eta=min(score(b,s) for b in BANK)
    return frozenset(a for a in E if 2*score(a,s)<3*eta),eta

def first_event(w0,signs):
    w0=tuple(map(Q,w0))
    s0=capacities(w0)
    s1=capacities(tuple(v*t for v,t in zip(w0,signs)))
    roots=set()
    # Membership can change only when two atomic pair scores meet at 3/2.
    for a in E:
        ga=G[a]
        for b in BANK:
            gb=gaps(b)
            for j in range(6):
                if not ga[j]: continue
                for k in range(6):
                    if not gb[k]: continue
                    c=2*ga[j]*s0[k]-3*gb[k]*s0[j]
                    m=2*ga[j]*s1[k]-3*gb[k]*s1[j]
                    if m:
                        t=Q(-c,m)
                        if 0<t<1: roots.add(t)
    baseline,_=near(w0)
    ordered=sorted(roots)
    for i,t in enumerate(ordered):
        w=tuple(v*(1+t*s) for v,s in zip(w0,signs))
        current,_=near(w)
        if current!=baseline:
            return t, sorted(baseline-current), sorted(current-baseline), len(roots)
        next_t=ordered[i+1] if i+1<len(ordered) else Q(1)
        middle=(t+next_t)/2
        w=tuple(v*(1+middle*s) for v,s in zip(w0,signs))
        current,_=near(w)
        if current!=baseline:
            return t, sorted(baseline-current), sorted(current-baseline), len(roots)
    return None,[],[],len(roots)

EXPECTED={
 (136,8,176,185):[
  "none","119/489","43/1803","43/693","9/329","119/505",
  "43/1883","43/773","3/1091","81/2735","3/1091","none",
  "1/369","9/343","1/369","none"],
 (722,465,240,48):[
  "none","1/161","1/641","1/721","none","1/161",
  "1/641","1/721","none","39/167","39/391","13/173",
  "9/71","1/7","none","none"]
}
for center,expected in EXPECTED.items():
    signs_list=list(product((-1,1),repeat=4))
    output=[]
    assert len(near(center)[0])==8
    for signs in signs_list:
        t,lost,entered,nroots=first_event(center,signs)
        output.append(str(t) if t is not None else "none")
        assert not entered, (center,signs,entered)
        print(center,''.join('+' if s==1 else '-' for s in signs),
              str(t) if t is not None else "UNCHANGED_FOR_t<1",
              'first_lost',lost,'first_entered',entered,'roots',nroots)
    assert output==expected,(center,output,expected)
    print("TABLE CERTIFICATE PASS",center)
print("ALL PASS")
