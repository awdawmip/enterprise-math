#!/usr/bin/env python3
"""Exact all-real-D Port-10 six-pair BRC certificate; w=(136,8,176,D).
All comparisons are Python Fraction arithmetic. No floats or external dependencies.
"""
from fractions import Fraction as Q
from itertools import combinations
import json

BANK=[(1,0,0),(0,2,-1),(1,-3,1),(2,-3,1),(3,-1,0),(1,3,-1),
(3,-4,1),(4,-1,0),(3,2,-1),(4,-4,1),(5,-1,0),(5,-4,1),
(6,-1,0),(3,-7,2),(6,-4,1),(7,-1,0),(7,2,-1),(9,-5,1)]
NEAR=[(1,-3,1),(1,0,0),(1,3,-1),(2,-4,1),(3,-7,2),
(3,-4,1),(3,-1,0),(3,3,-1),(4,-4,1),(4,-1,0),
(5,-4,1),(5,-1,0),(6,-4,1),(6,-1,0),(7,-8,2),
(7,-4,1),(7,-1,0),(7,2,-1),(9,-5,1),(9,-2,0)]
PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
A,B,C=136,8,176

def port(a):
    return max(sum(max(x,0) for x in a),sum(max(-x,0) for x in a))
def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[i]-h[j]) for i,j in PAIRS)

FULL=[(x,y,z) for x in range(-10,11) for y in range(-10,11)
      for z in range(-10,11)
      if (x,y,z)>(-x,-y,-z) and port((x,y,z))<=10]
assert len(FULL)==1935
GG={a:gaps(a) for a in FULL}
assert all(any(all(u<=v for u,v in zip(GG[b],GG[a]))
               for b in BANK) for a in FULL)
assert set(NEAR)=={
    a for a in FULL if not any(
        all(2*u>=3*v for u,v in zip(GG[a],GG[b])) for b in BANK)}

CAP=(A+B,A+C,None,B+C,None,None)
OFF=(None,None,A,None,B,C)
ATOMS={a:tuple((Q(GG[a][j]),
                Q(CAP[j]) if CAP[j] is not None else None,
                Q(OFF[j]) if OFF[j] is not None else None)
               for j in range(6)) for a in set(BANK+NEAR)}

def val(f,d):
    n,c,o=f
    return n/c if c is not None else n/(d+o)
def score(a,d):
    return max(val(f,d) for f in ATOMS[a])
def state(d):
    s={a:score(a,d) for a in BANK}
    opt=min(s.values())
    return (opt,tuple(a for a in BANK if s[a]==opt),
            tuple(a for a in NEAR if 2*score(a,d)<3*opt))

def root(f,g,left=1,right=1):
    n,c,o=f
    m,e,p=g
    a=left*n
    b=right*m
    if not a or not b or (c is not None and e is not None):
        return None
    if c is None and e is None:
        if a==b:
            return None
        d=(b*o-a*p)/(a-b)
    elif c is None:
        d=a*e/b-o
    else:
        d=b*c/a-p
    return d if d>0 else None

critical=set()
def pair_roots(L,R,scale_l=1,scale_r=1):
    for f in L:
        for g in R:
            d=root(f,g,scale_l,scale_r)
            if d is not None:
                critical.add(d)
for a in BANK+NEAR:
    for f,g in combinations(ATOMS[a],2):
        d=root(f,g)
        if d is not None:
            critical.add(d)
for a,b in combinations(BANK,2):
    pair_roots(ATOMS[a],ATOMS[b])
for a in NEAR:
    for b in BANK:
        pair_roots(ATOMS[a],ATOMS[b],2,3)
points=[Q(0)]+sorted(critical)
intervals=[
    state((points[i]+points[i+1])/2 if i+1<len(points)
          else points[i]+1)
    for i in range(len(points))]

def active_formula(d):
    opt,winners,_=state(d)
    active=set()
    for a in winners:
        for f in ATOMS[a]:
            if val(f,d)==opt:
                n,c,o=f
                active.add(("constant",str(n/c)) if c is not None
                           else ("ratio",int(n),int(o)))
    return tuple(sorted(active))

changes=[]
opt_changes=[]
for i in range(1,len(points)):
    d=points[i]
    L=intervals[i-1]
    R=intervals[i]
    at=state(d)
    if L[2]!=R[2] or at[2]!=L[2]:
        changes.append({
            "d":str(d),"left":len(L[2]),"at":len(at[2]),
            "right":len(R[2]),
            "add":[list(a) for a in R[2] if a not in L[2]],
            "remove":[list(a) for a in L[2] if a not in R[2]]
        })
    assert set(at[2])==set(L[2])&set(R[2])
    left_d=(points[i-1]+d)/2
    right_d=(d+points[i+1])/2 if i+1<len(points) else d+1
    if active_formula(left_d)!=active_formula(right_d):
        opt_changes.append(str(d))

assert len(critical)==753
assert [r["d"] for r in changes]==[
    "184","304","406","424","544","728","1288","1648","2584"]
assert opt_changes==["8","280","544","1096"]
assert [r["left"] for r in changes]==[2,8,6,5,4,3,5,4,2]
assert [r["at"] for r in changes]==[2,6,5,4,3,3,4,2,1]
assert [r["right"] for r in changes]==[8,6,5,4,3,5,4,2,1]

# Independent full-lattice crosscheck at every membership/formula boundary
# plus four other positions.
samples=sorted(set([Q(1),Q(48),Q(185),Q(500),Q(10000)]+
                   [Q(r["d"]) for r in changes]+
                   [Q(s) for s in opt_changes]))
for d in samples:
    den=(Q(A+B),Q(A+C),d+A,Q(B+C),d+B,d+C)
    fs={a:max(Q(g,k) for g,k in zip(GG[a],den)) for a in FULL}
    opt=min(fs.values())
    assert opt==state(d)[0]
    assert {a for a in FULL if 2*fs[a]<3*opt}==set(state(d)[2])

print(json.dumps({
 "schema":"X6_R129_CLASSIII_PORT10_FULL_POSITIVE_D_RAY",
 "status":"PASS","weights":[136,8,176,"D>0"],
 "full_directions":len(FULL),"optimizer_bank":len(BANK),
 "near_envelope":len(NEAR),"positive_critical_roots":len(critical),
 "open_intervals_checked":len(intervals),
 "critical_points_checked":len(critical),
 "near_events":changes,"optimizer_formula_changes":opt_changes,
 "full_lattice_samples":len(samples),
 "D_185_optimum":str(state(Q(185))[0]),
 "D_185_near":[list(a) for a in state(Q(185))[2]]
},ensure_ascii=False,indent=2))
