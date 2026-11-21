"""R77 exact rational verification of arbitrary-four-weight D=4 BRC chamber.

Checks the theorem against the existing 28-vector R72 sufficient atlas.
Scientific computation is exact arithmetic; the finite atlas remains an
upstream author certificate rather than a new independent completeness proof.
"""
from fractions import Fraction as Q
from itertools import product
import json

ATLAS = [
(1,1,0,0),(2,0,2,-1),(3,1,-3,1),(3,2,-3,1),(3,3,-1,0),
(4,1,3,-1),(4,3,-4,1),(4,4,-1,0),(5,3,2,-1),(5,4,-4,1),
(5,5,-1,0),(6,5,-4,1),(6,6,-1,0),(7,3,-7,2),(7,6,-4,1),
(7,7,-1,0),(9,7,2,-1),(10,9,-5,1),(11,10,-5,1),
(16,15,-6,1),(22,21,-7,1),(27,24,-14,3),
(39,36,-16,3),(43,39,-20,4),(47,42,-24,5),
(49,45,-21,4),(71,66,-28,5),(125,114,-56,11)
]
S=(114,-56,11)
L=(10,-5,1)
H=(45,-21,4)
M=(39,-20,4)

def qcost(v):
    return max(sum(max(x,0) for x in v),sum(max(-x,0) for x in v))

def moments(v):
    return tuple([0]+[sum(v[i]*(d**t-d) for i,d in enumerate(range(2,5))) for t in (2,3,4)])

def radius(v,w):
    z=moments(v)
    return max(Q(abs(z[i]-z[j]),2*(w[i]+w[j])) for i in range(4) for j in range(i+1,4))

def fine_m(A,C,D):
    mL=max(1/(A+D),1/(C+D))
    mH=max(3/(A+C),3/(C+D))
    mM=max(3/(A+C),3/(A+D))
    return min(mL,mH,mM)

assert [qcost(v) for v in (L,H,M,S)]==[11,49,43,125]
assert [moments(v) for v in (L,H,M,S)]==[(0,2,0,2),(0,12,6,0),(0,6,-6,-6),(0,24,0,0)]
assert tuple(x[0] for x in ATLAS)==tuple(sorted(x[0] for x in ATLAS))
assert all(qcost(row[1:])==row[0] for row in ATLAS)

checked_triples=0
for a2,a3,a4 in product(range(-12,13), repeat=3):
    v=(a2,a3,a4)
    z=moments(v)
    if z[2]==z[3]==0:
        assert v==(0,0,0)
        continue
    assert z[2]%6==0 and z[3]%2==0
    checked_triples+=1

trials=0
counts={"S_strict":0,"S_tied":0,"S_suboptimal":0}
examples=[]
for A,C,D in product(map(Q,(1,2,3,7,20,100)), repeat=3):
    m=fine_m(A,C,D)
    delta=min(A,C,D)
    threshold=Q(12,1)/m-delta
    assert threshold>0
    for B in (threshold/2,threshold,threshold+1,Q(1),Q(3),Q(1000)):
        w=(A,B,C,D)
        E=Q(12,1)/(B+delta)
        from_atlas_125=min(radius(row[1:],w) for row in ATLAS)
        from_atlas_124=min(radius(row[1:],w) for row in ATLAS if row[0]<=124)
        fS=radius(S,w)
        assert fS==E
        assert min(radius(x,w) for x in (L,H,M))<=E if E>=m else True
        assert all(radius(x,w)>=m for x in (L,H,M))
        assert (from_atlas_125<from_atlas_124)==(E<m)
        if E<m:
            assert from_atlas_125==E and from_atlas_124==m
            assert sum(radius(row[1:],w)==E for row in ATLAS)==1
            label="S_strict"
        elif E==m:
            assert from_atlas_125==from_atlas_124==m
            assert min(radius(x,w) for x in (L,H,M))==m
            label="S_tied"
        else:
            assert from_atlas_125==from_atlas_124<E
            assert min(radius(x,w) for x in (L,H,M))<E
            label="S_suboptimal"
        trials+=1
        counts[label]+=1
        if (A,C,D)==(Q(100),Q(1),Q(1)) and B in (threshold,threshold+1):
            examples.append({"weights":[str(x) for x in w],"m":str(m),"E":str(E),"eta124":str(from_atlas_124),"eta125":str(from_atlas_125),"threshold_B":str(threshold),"status":label})

results={
    "schema":"X6_R77_ALL_FOUR_WEIGHT_WINNER_CHAMBER_CHECK_V1",
    "date":"2026-11-21",
    "source":"R72 28-vector atlas @ awdawmip/enterprise-math (2026-11-21)",
    "frozen_P000_commit":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "fine_witnesses":{"L":{"a":list(L),"q":qcost(L),"z":moments(L)},"H":{"a":list(H),"q":qcost(H),"z":moments(H)},"M":{"a":list(M),"q":qcost(M),"z":moments(M)},"S":{"a":list(S),"q":qcost(S),"z":moments(S)}},
    "tested_nonkernel_integer_triples":checked_triples,
    "exact_rational_weight_profiles":trials,
    "classification_counts":counts,
    "examples":examples,
    "assertions":"PASS",
    "scope":"Exact rational author-check against R72 published atlas; mathematical completeness of general-weights theorem is established by the accompanying symbolic proof, not sampling; atlas-complete no-drop corollary is conditional on R72 completeness."
}
print(json.dumps(results,indent=2,ensure_ascii=False))
