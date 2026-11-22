#!/usr/bin/env python3
"""X6 R109: exact integer witness for the four-weight BRC cone theorem.

This checker is for the auxiliary positive six-pair BRC observer. It does not
execute native X6 dynamics or assert a formal review result.
"""
from fractions import Fraction
import json

W = (9, 1, 58, 41)
PAIR_DEN = (W[0]+W[1], W[0]+W[2], W[0]+W[3], W[1]+W[2], W[1]+W[3], W[2]+W[3])
CAP = (1, 10, 7, 8, 6, 14)

def moments(a):
    x, y, z = a
    return (x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z)

def port(a):
    return max(sum(max(n,0) for n in a), sum(max(-n,0) for n in a))

def score(a):
    u, v, h = moments(a)
    return max(Fraction(n, den) for n, den in zip(
        (abs(u), abs(v), abs(h), abs(v-u), abs(h-u), abs(h-v)), PAIR_DEN))

def sign_canonical(a):
    return a if next(t for t in a if t != 0)>0 else tuple(-n for n in a)

def residue_orbit(a):
    x,y,z=a
    return min((x%3,y%3,z%3),((-x)%3,(-y)%3,(-z)%3))

solutions=[]
for u in range(-CAP[0],CAP[0]+1):
    for v in range(-CAP[1],CAP[1]+1):
        for h in range(-CAP[2],CAP[2]+1):
            if abs(v-u)>CAP[3] or abs(h-u)>CAP[4] or abs(h-v)>CAP[5]:
                continue
            if v%3 or (h-u)%6 or (h-u-6*v)%12:
                continue
            a=((h+19*u-8*v)//2,(-h-14*u+7*v)//3,(h+11*u-6*v)//12)
            if a==(0,0,0):
                continue
            assert moments(a)==(u,v,h)
            assert score(a)<Fraction(3,20)
            assert port(a)<=38
            solutions.append(a)

assert len(solutions)==24
unoriented=sorted({sign_canonical(a) for a in solutions},key=lambda a:(port(a),a))
assert len(unoriented)==12
assert len({residue_orbit(a) for a in unoriented})==12
assert (0,1,2) not in {residue_orbit(a) for a in unoriented}

# Independent original-coordinate scan to the exact sharpness budget.
full=[]
for x in range(-38,39):
    for y in range(-38,39):
        for z in range(-38,39):
            a=(x,y,z)
            if a==(0,0,0) or port(a)>38:
                continue
            if next(t for t in a if t!=0)<0:
                continue
            if score(a)<Fraction(3,20):
                full.append(a)
assert sorted(full)==sorted(unoriented)

eta=min(score((x,y,z))
        for x in range(-11,12) for y in range(-11,12) for z in range(-11,12)
        if (x,y,z)!=(0,0,0) and port((x,y,z))<=11)
assert eta==Fraction(1,10)

cert={
  "id":"X6-R109-EXACT-CONE-TWELVE",
  "status":"PASS",
  "model":"auxiliary positive four-weight six-pair BRC score, not native physical model",
  "weights":list(W),
  "port_min":27,
  "sharpness_port":38,
  "eta":"1/10",
  "strict_threshold":"3/20",
  "moment_caps":list(CAP),
  "oriented_moment_solutions":len(solutions),
  "unoriented_directions":len(unoriented),
  "distinct_nonzero_mod3_sign_orbits":len({residue_orbit(a) for a in unoriented}),
  "missing_mod3_sign_orbit":[0,1,2],
  "directions":[{"a":list(a),"q":port(a),"score":str(score(a)),"moments":list(moments(a))} for a in unoriented],
  "proof_scope":"Weight-cone exclusion is symbolic for all real positive weights and p>=27; sharpness certificate checks exact weight (9,1,58,41).",
  "finite_validation":"Complete original integer differences q<=38 and exact congruence-bounded moment box."
}
print(json.dumps(cert,ensure_ascii=False,indent=2))
