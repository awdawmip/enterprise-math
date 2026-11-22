#!/usr/bin/env python3
"""X6 R107 exact checker; author-side arithmetic, not an independent review."""
from fractions import Fraction as Q
import json

A=[(1,0,0),(5,-4,1),(9,-5,1),(10,-5,1),
   (14,-9,2),(15,-9,2),(19,-10,2),(23,-14,3),
   (24,-14,3),(25,-14,3),(29,-18,4),(34,-19,4)]
LOW=A[:8]
MID=[(10,-5,1),(14,-9,2),(24,-14,3),(34,-19,4)]
HIGH=[(24,-14,3)]

def q(a):
    return max(sum(max(x,0) for x in a),sum(max(-x,0) for x in a))

def moments(a):
    x,y,z=a
    return (x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)

def orient(a):
    return a if next(t for t in a if t!=0)>0 else tuple(-t for t in a)

def inverse(u,v,h):
    if v%3 or (h-u)%6 or (h-u-6*v)%12:return None
    x,y,z=Q(h+19*u-8*v,2),Q(-h-14*u+7*v,3),Q(h+11*u-6*v,12)
    assert x.denominator==y.denominator==z.denominator==1
    return (int(x),int(y),int(z))

def F(a,C):
    u,v,h=moments(a)
    denominators=[10,C+9,50,C+1,42,C+41]
    return max(Q(abs(t),d) for t,d in zip((u,v,h,v-u,h-u,h-v),denominators))

reference=set()
all_reference=set()
oriented=0
for u in range(-1,2):
    for v in range(-10,11):
        for h in range(-7,8):
            a=inverse(u,v,h)
            if a is None or a==(0,0,0):continue
            oriented+=1
            all_reference.add(orient(a))
            if F(a,59)<Q(3,20):reference.add(orient(a))
assert oriented==32 and len(all_reference)==16 and reference==set(A)

low=set()
for u in range(-1,2):
    for h in range(-7,8):
        if 20*abs(h)>=150 or 20*abs(h-u)>=126:continue
        for v in range(-55,56):
            a=inverse(u,v,h)
            if a is None or a==(0,0,0) or q(a)>26:continue
            low.add(orient(a))
assert low==set(LOW),(low^set(LOW))

walls={}
for a in A:
    u,v,h=moments(a)
    upper=[]
    for coeff,absval in [(90,abs(u)),(450,abs(h)),(378,abs(h-u))]:
        if absval:upper.append(Q(coeff,absval)-1)
    if abs(v)>9:upper.append(Q(81-abs(v),abs(v)-9))
    if abs(h-v)>9:upper.append(Q(369-abs(h-v),abs(h-v)-9))
    assert abs(v-u)<9
    walls[a]=min(upper) if upper else None
assert sum(t==Q(62) for t in walls.values())==8
assert sum(t==Q(89) for t in walls.values())==3
assert sum(t is None for t in walls.values())==1
assert {a for a,t in walls.items() if t is None or t>62}==set(MID)
assert {a for a,t in walls.items() if t is None or t>89}==set(HIGH)

samples=[Q(59),Q(119,2),Q(61),Q(62),Q(63),Q(88),Q(89),Q(120)]
ports=[11,16,17,21,26,27,28,33,37,38,44,55]
for C in samples:
    for p in ports:
        eta=Q(1,10) if p<=26 else Q(6,C+1)
        expected=({a for a in LOW if q(a)<=p} if p<=26 else
                  {a for a in A if q(a)<=p and (walls[a] is None or C<walls[a])})
        observed={a for a in all_reference|low if q(a)<=p and 2*F(a,C)<3*eta}
        assert observed==expected,(C,p,observed,expected)
        if p>=27:assert F((24,-14,3),C)==eta

certificate={
 "schema":"X6_R107_HIGH_C_PORT_ATLAS_EXACT_V1",
 "observer":"positive four-weight six-pair BRC star-gap",
 "family":"w=(9,1,C,41), real C>=59",
 "ports":"integer p>=11",
 "reference_box_moment_triples":945,
 "reference_valid_oriented":oriented,
 "reference_unoriented":len(all_reference),
 "reference_strict_near":len(reference),
 "low_port_limit_candidates":len(low),
 "walls":[{"direction":list(a),"q":q(a),"upper_wall":str(walls[a]) if walls[a] is not None else "unbounded"} for a in A],
 "eta_low_port":"1/10, p<=26",
 "eta_high_port":"6/(C+1), p>=27",
 "high_port_regions":["59<=C<62: 12 candidates","62<=C<89: 4 candidates","C>=89: 1 candidate"],
 "sample_exact_cases":len(samples)*len(ports),
 "assertions":"PASS",
 "scope":"Finite complete integer boxes, exact candidate walls; unbounded-C coverage via companion proof"
}
print(json.dumps(certificate,ensure_ascii=False,indent=2))
