#!/usr/bin/env python3
"""Conditional four-positive-weight/six-pair BRC Port-10 exact D-ray sweep.
Usage: python x6_port10_six_pair_D_ray_exact_sweep.py A B C
Outputs exact rational roots, full membership transitions, optimizer switches.
No floating point or third-party modules.
"""
from fractions import Fraction as Q
from itertools import combinations
import sys,json

BANK=[(1,0,0),(0,2,-1),(1,-3,1),(2,-3,1),(3,-1,0),(1,3,-1),
(3,-4,1),(4,-1,0),(3,2,-1),(4,-4,1),(5,-1,0),(5,-4,1),
(6,-1,0),(3,-7,2),(6,-4,1),(7,-1,0),(7,2,-1),(9,-5,1)]
NEAR=[(1,-3,1),(1,0,0),(1,3,-1),(2,-4,1),(3,-7,2),
(3,-4,1),(3,-1,0),(3,3,-1),(4,-4,1),(4,-1,0),
(5,-4,1),(5,-1,0),(6,-4,1),(6,-1,0),(7,-8,2),
(7,-4,1),(7,-1,0),(7,2,-1),(9,-5,1),(9,-2,0)]
PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
def port(a):
    return max(sum(max(x,0) for x in a),sum(max(-x,0) for x in a))
def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[i]-h[j]) for i,j in PAIRS)

FULL=[(x,y,z) for x in range(-10,11)
      for y in range(-10,11) for z in range(-10,11)
      if (x,y,z)>(-x,-y,-z) and port((x,y,z))<=10]
assert len(FULL)==1935
GG={a:gaps(a) for a in FULL}
assert all(any(all(u<=v for u,v in zip(GG[b],GG[a]))
               for b in BANK) for a in FULL)
assert set(NEAR)=={a for a in FULL if not any(
    all(2*u>=3*v for u,v in zip(GG[a],GG[b])) for b in BANK)}

def analyze(A,B,C):
    assert min(A,B,C)>0
    cap=(A+B,A+C,None,B+C,None,None)
    off=(None,None,A,None,B,C)
    atoms={a:tuple((Q(GG[a][j]),
           Q(cap[j]) if cap[j] is not None else None,
           Q(off[j]) if off[j] is not None else None)
           for j in range(6)) for a in set(BANK+NEAR)}
    def value(f,d):
        n,c,o=f
        return n/c if c is not None else n/(d+o)
    def score(a,d):
        return max(value(f,d) for f in atoms[a])
    def state(d):
        scores={a:score(a,d) for a in BANK}
        opt=min(scores.values())
        return opt,tuple(a for a in BANK if scores[a]==opt),tuple(
            a for a in NEAR if 2*score(a,d)<3*opt)
    def root(f,g,left=1,right=1):
        n,c,o=f;m,e,p=g;a=left*n;b=right*m
        if not a or not b or (c is not None and e is not None):
            return None
        if c is None and e is None:
            if a==b:return None
            d=(b*o-a*p)/(a-b)
        elif c is None:d=a*e/b-o
        else:d=b*c/a-p
        return d if d>0 else None
    roots=set()
    def pair_roots(L,R,l=1,r=1):
        for f in L:
            for g in R:
                d=root(f,g,l,r)
                if d is not None:roots.add(d)
    for a in BANK+NEAR:
        for f,g in combinations(atoms[a],2):
            d=root(f,g)
            if d is not None:roots.add(d)
    for a,b in combinations(BANK,2):
        pair_roots(atoms[a],atoms[b])
    for a in NEAR:
        for b in BANK:
            pair_roots(atoms[a],atoms[b],2,3)
    points=[Q(0)]+sorted(roots)
    intervals=[state((points[i]+points[i+1])/2 if i+1<len(points)
                else points[i]+1) for i in range(len(points))]
    def formula(d):
        opt,winners,_=state(d)
        active=set()
        for a in winners:
            for f in atoms[a]:
                if value(f,d)==opt:
                    n,c,o=f
                    active.add(("constant",str(n/c)) if c is not None
                               else ("ratio",int(n),int(o)))
        return tuple(sorted(active))
    changes=[]
    optimizer=[]
    for i in range(1,len(points)):
        d=points[i]
        L,R=intervals[i-1],intervals[i]
        at=state(d)
        if L[2]!=R[2] or at[2]!=L[2]:
            changes.append({
                "d":str(d),"left":len(L[2]),"at":len(at[2]),
                "right":len(R[2]),
                "add":[list(a) for a in R[2] if a not in L[2]],
                "remove":[list(a) for a in L[2] if a not in R[2]]})
        assert set(at[2])==set(L[2])&set(R[2])
        ld=(points[i-1]+d)/2
        rd=(d+points[i+1])/2 if i+1<len(points) else d+1
        if formula(ld)!=formula(rd):
            optimizer.append({"d":str(d),"left":formula(ld),"right":formula(rd)})
    # Independently crosscheck unreduced full lattice at all classified
    # breakpoints and selected distinct interior/exterior witnesses.
    samples=sorted(set([Q(1),Q(48),Q(185),Q(500),Q(10000)]+
            [Q(z["d"]) for z in changes+optimizer]))
    for d in samples:
        den=(Q(A+B),Q(A+C),d+A,Q(B+C),d+B,d+C)
        fs={a:max(Q(g,k) for g,k in zip(GG[a],den)) for a in FULL}
        opt=min(fs.values())
        assert opt==state(d)[0]
        assert {a for a in FULL if 2*fs[a]<3*opt}==set(state(d)[2])
    return {"status":"PASS","weights":[A,B,C,"D>0"],
        "full_directions":len(FULL),"optimizer_bank":len(BANK),
        "near_envelope":len(NEAR),"critical_roots":len(roots),
        "open_intervals":len(intervals),"near_changes":changes,
        "optimizer_changes":optimizer,"full_population_crosschecks":len(samples),
        "examples":[{"d":str(d),"opt":str(state(d)[0]),
                     "count":len(state(d)[2]),
                     "near":[list(a) for a in state(d)[2]]}
                   for d in [Q(1),Q(48),Q(185),Q(200),Q(500),Q(10000)]]}
if __name__=="__main__":
    r=analyze(*map(int,sys.argv[1:4]))
    print(json.dumps(r,ensure_ascii=False,indent=2))
