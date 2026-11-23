#!/usr/bin/env python3
"""Exact all-real-D certificate for the conditional six-pair Port-10 BRC observer."""
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

def port(a):
    return max(sum(max(x,0) for x in a),sum(max(-x,0) for x in a))
def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[i]-h[j]) for i,j in PAIRS)

FULL=[]
for x in range(-10,11):
 for y in range(-10,11):
  for z in range(-10,11):
   a=(x,y,z)
   if a>(-x,-y,-z) and port(a)<=10:
    FULL.append(a)
assert len(FULL)==1935
GG={a:gaps(a) for a in FULL}
assert all(any(all(u<=v for u,v in zip(GG[b],GG[a])) for b in BANK) for a in FULL)
assert set(NEAR)=={a for a in FULL if not any(all(2*u>=3*v for u,v in zip(GG[a],GG[b])) for b in BANK)}

# For weights (240,577,48,D), elementary rational pieces of the six retained pairs.
# Atom = (numerator, fixed denominator or None, D-offset or None).
CAP=(817,288,None,625,None,None)
OFF=(None,None,240,None,577,48)
def atom(a,j):
    return (Q(GG[a][j]),Q(CAP[j]) if CAP[j] is not None else None,
            Q(OFF[j]) if OFF[j] is not None else None)
ATOMS={a:tuple(atom(a,j) for j in range(6)) for a in set(BANK+NEAR)}
def value(f,d):
    n,c,o=f
    return n/c if c is not None else n/(d+o)
def score(a,d):
    return max(value(f,d) for f in ATOMS[a])
def state(d):
    scores={a:score(a,d) for a in BANK}
    opt=min(scores.values())
    winners=tuple(a for a in BANK if scores[a]==opt)
    near=tuple(a for a in NEAR if 2*score(a,d)<3*opt)
    return opt,winners,near

def root(f,g,left=1,right=1):
    n,c,o=f; m,e,p=g
    a=left*n; b=right*m
    if not a or not b or (c is not None and e is not None):return None
    if c is None and e is None:
        if a==b:return None
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
            if d is not None:critical.add(d)
for a in BANK+NEAR:
    for f,g in combinations(ATOMS[a],2):
        d=root(f,g)
        if d is not None:critical.add(d)
for a,b in combinations(BANK,2):pair_roots(ATOMS[a],ATOMS[b])
for a in NEAR:
    for b in BANK:pair_roots(ATOMS[a],ATOMS[b],2,3)
points=[Q(0)]+sorted(critical)
intervals=[state((points[i]+points[i+1])/2 if i+1<len(points) else points[i]+1) for i in range(len(points))]

def active_formula(d):
    opt,winners,_=state(d)
    active=set()
    for a in winners:
        for j,f in enumerate(ATOMS[a]):
            if value(f,d)==opt:
                n,c,o=f
                active.add(("constant",str(n/c)) if c is not None else ("ratio",int(n),int(o)))
    return tuple(sorted(active))

near_changes=[]; opt_formula_changes=[]
for i in range(1,len(points)):
    left=intervals[i-1];right=intervals[i];at=state(points[i]);d=points[i]
    if left[2]!=right[2]:
        near_changes.append([str(d),len(left[2]),len(at[2]),len(right[2]),
                             [list(a) for a in right[2] if a not in left[2]],
                             [list(a) for a in left[2] if a not in right[2]]])
    if active_formula((points[i-1]+d)/2)!=active_formula((d+points[i+1])/2 if i+1<len(points) else d+1):
        opt_formula_changes.append(str(d))
assert len(critical)==953,("critical",len(critical))
assert [c[0] for c in near_changes]==[
    '48/7','96/5','624/19','96','192','400','464','656',
    '720','912','976','6096/5','1536','11202']
assert opt_formula_changes==['48','144','336','1008','5771','6923','7452']
# Isolated changes in strict membership cannot occur (strict continuity), but
# check every root directly as well as both adjacent open intervals.
assert all(set(state(points[i])[2])==set(intervals[i-1][2]) & set(intervals[i][2])
           for i in range(1,len(points)))
# Independent full-1935 checks at targeted thresholds (the 18/20 domination
# proof already covers all positive weights, all D, not just these tests).
for d in [Q(1),Q(48,7),Q(10),Q(96,5),Q(624,19),Q(48),Q(96),
          Q(192),Q(400),Q(464),Q(656),Q(720),Q(912),Q(976),
          Q(978),Q(1008),Q(6096,5),Q(1536),Q(5771),Q(6923),
          Q(7452),Q(11202),Q(50000)]:
    den=(Q(817),Q(288),d+240,Q(625),d+577,d+48)
    fs={a:max(Q(g,k) for g,k in zip(GG[a],den)) for a in FULL}
    opt=min(fs.values())
    assert opt==state(d)[0]
    assert {a for a in FULL if 2*fs[a]<3*opt}==set(state(d)[2])

print(json.dumps({'status':'PASS','model':'conditional-six-pair-Port10',
 'weights':[240,577,48,'D>0'],'full_directions':len(FULL),
 'optimizer_bank':len(BANK),'near_envelope':len(NEAR),'critical_roots':len(critical),
 'open_intervals_checked':len(intervals),'root_points_checked':len(critical),
 'near_changes':near_changes,'optimizer_formula_changes':opt_formula_changes,
 'full_population_crosscheck_samples':23},ensure_ascii=False,indent=2))
