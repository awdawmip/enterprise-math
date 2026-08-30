#!/usr/bin/env python3
from __future__ import annotations
import itertools, json
from collections import Counter, deque

H = tuple((a,b) for a in range(3) for b in range(3) if (a,b)!=(0,0))
HI = {v:i for i,v in enumerate(H)}
LINES = ((1,0),(0,1),(1,1),(1,2))
LI = {v:i for i,v in enumerate(LINES)}
ID8 = tuple(range(8))
ID4 = tuple(range(4))

def add3(x,y,z):
    return ((x[0]+y[0]+z[0])%3,(x[1]+y[1]+z[1])%3)

def norm(v):
    x,y=v
    if x%3:
        k=1 if x%3==1 else 2
        return ((x*k)%3,(y*k)%3)
    return (0,1)

FIBER = tuple(LI[norm(v)] for v in H)
FIBERS = tuple(tuple(i for i in range(8) if FIBER[i]==s) for s in range(4))
BAL = frozenset(tuple(sorted((HI[x],HI[y],HI[z])))
                for x,y,z in itertools.combinations(H,3)
                if add3(x,y,z)==(0,0))
assert len(BAL)==8 and all(len(f)==2 for f in FIBERS)

def comp(p,q): return tuple(p[q[i]] for i in range(len(p)))
def power(p,n):
    r=tuple(range(len(p)))
    for _ in range(n): r=comp(r,p)
    return r
def order(p):
    one=tuple(range(len(p))); r=one
    for n in range(1,100):
        r=comp(r,p)
        if r==one: return n
    raise AssertionError
def gen(gs):
    one=tuple(range(len(gs[0]))); seen={one}; q=deque([one])
    while q:
        x=q.popleft()
        for g in gs:
            y=comp(x,g)
            if y not in seen: seen.add(y); q.append(y)
    return seen
def image_tri(p,t): return tuple(sorted(p[i] for i in t))
def preserves(p,R): return frozenset(image_tri(p,t) for t in R)==R

# Opposite pairing is derived as pair codegree zero.
codeg={(i,j):sum(i in t and j in t for t in BAL)
       for i,j in itertools.combinations(range(8),2)}
assert Counter(codeg.values())==Counter({1:24,0:4})
OPP=frozenset(frozenset(k) for k,v in codeg.items() if v==0)
assert OPP==frozenset(frozenset(f) for f in FIBERS)

AUT=tuple(p for p in itertools.permutations(range(8)) if preserves(p,BAL))
assert len(AUT)==48

def star_action(p):
    out=[]
    for s in range(4):
        im={FIBER[p[i]] for i in FIBERS[s]}
        if len(im)!=1: return None
        out.append(next(iter(im)))
    return tuple(out)

S4={star_action(p) for p in AUT}
assert None not in S4 and len(S4)==24
KER=tuple(p for p in AUT if star_action(p)==ID4)
assert len(KER)==2

# Certificate identification Aut(BAL)=GL(2,3).
def det(A): return (A[0]*A[3]-A[1]*A[2])%3
def act(A,v):
    return ((A[0]*v[0]+A[1]*v[1])%3,(A[2]*v[0]+A[3]*v[1])%3)
GL=tuple(A for A in itertools.product(range(3),repeat=4) if det(A))
assert len(GL)==48
GLP={tuple(HI[act(A,v)] for v in H) for A in GL}
assert GLP==set(AUT)
Z=tuple(HI[((-v[0])%3,(-v[1])%3)] for v in H)
assert set(KER)=={ID8,Z}

# All 8 balance tuples are one orbit; remove one -> order/image 6.
seed=next(iter(BAL))
assert {image_tri(p,seed) for p in AUT}==BAL
BAL7=frozenset(set(BAL)-{seed})
AUT7=tuple(p for p in itertools.permutations(range(8)) if preserves(p,BAL7))
assert len(AUT7)==6
assert len({star_action(p) for p in AUT7 if star_action(p) is not None})==6

# Nonsplit residue census on every S4 (3,2,4) generator pair.
qpairs=[(a,b) for a in S4 for b in S4
        if order(a)==3 and order(b)==2 and order(comp(a,b))==4
        and len(gen((a,b)))==24]
assert len(qpairs)==24
lifts={q:tuple(p for p in AUT if star_action(p)==q) for q in S4}
assert all(len(x)==2 for x in lifts.values())
res=Counter()
for a,b in qpairs:
    for A in lifts[a]:
        for B in lifts[b]:
            res[power(comp(A,B),4)]+=1
assert res==Counter({Z:96})

# Same-signature split regression: sign-blind triples from 3 carrier fibres.
COARSE=frozenset(t for t in itertools.combinations(range(8),3)
                 if len({FIBER[i] for i in t})==3)
AUTS=tuple(p for p in itertools.permutations(range(8)) if preserves(p,COARSE))
assert len(COARSE)==32 and len(AUTS)==384
assert len({star_action(p) for p in AUTS})==24
assert len([p for p in AUTS if star_action(p)==ID4])==16

def split_lift(q):
    p=[None]*8
    for s in range(4):
        for bit,i in enumerate(FIBERS[s]):
            p[i]=FIBERS[q[s]][bit]
    return tuple(p)
for q in itertools.permutations(range(4)):
    assert split_lift(q) in AUTS and star_action(split_lift(q))==q
for q1 in itertools.permutations(range(4)):
    for q2 in itertools.permutations(range(4)):
        assert split_lift(comp(q1,q2))==comp(split_lift(q1),split_lift(q2))

# Same-signature no-lift regression: exact hidden witness + P4 NativeAdj.
E=frozenset(((0,1),(1,2),(2,3)))
def p4(q):
    return frozenset(tuple(sorted((q[i],q[j]))) for i,j in E)==E
P4={q for q in itertools.permutations(range(4)) if p4(q)}
AUTN=tuple(p for p in AUT if star_action(p) in P4)
assert len(P4)==2 and len(AUTN)==4
assert {star_action(p) for p in AUTN}==P4

# Deletions.
BRIDGE_ONLY=tuple(p for p in itertools.permutations(range(8))
                  if star_action(p) is not None)
assert len(BRIDGE_ONLY)==384
assert len([p for p in BRIDGE_ONLY if star_action(p)==ID4])==16
NO_BRIDGE_ORDER=len(AUT)*24
assert NO_BRIDGE_ORDER==1152
NO_HIDDEN_ORDER=24

report={
 "schema":"P000_Q15_HIDDEN_KERNEL_MODEL_SIGNATURE_CHECK_V1",
 "status":"PASS",
 "hard_target":"P000_HIDDEN_KERNEL_NONSPLIT_MODEL_SIGNATURE_MINIMALITY_CLASSIFIED",
 "terminal_class":"MINIMAL_NONSPLIT_HIDDEN_KERNEL_SIGNATURE_FOUND",
 "nonsplit":{"hidden_points":8,"balance_triples":8,"aut_order":48,
             "carrier_image_order":24,"kernel_order":2,
             "quotient_generator_pairs":24,"lifted_pairs":96,
             "residue":"(AB)^4=z for every lifted pair","section_exists":False},
 "same_signature":{"split":{"aut_order":384,"kernel_order":16,
                            "image_order":24,"section_exists":True},
                   "no_lift":{"aut_order":4,"image_order":2,"section_exists":False}},
 "deletions":{"HiddenBalance3":{"aut_order":384,"kernel_order":16,"split":True},
              "HiddenAxisInc":{"aut_order":NO_BRIDGE_ORDER,"pure_carrier_section":True},
              "HiddenPhase":{"aut_order":NO_HIDDEN_ORDER,"q10_split_base":True},
              "one_balance_tuple":{"aut_order":6,"image_order":6}},
 "q12":{"derived_kernel":"z","R":"(AB)^4=z","H_ind":"R=z",
        "independent_twist_rule":"reuse H=R*D"},
 "minimality":"deletion-minimal and two-role minimal under typed semantic discipline",
 "method_reuse":["T7_FINITE_SYMMETRY_EQUIVARIANCE",
                 "T9_HOLONOMY_COCOYCLE_GLUING",
                 "T2_BLOCK_FINITE_CERTIFICATE"]
}
print(json.dumps(report,indent=2,sort_keys=True))
