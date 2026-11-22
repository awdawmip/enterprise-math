#!/usr/bin/env python3
"""R111: exact moment-box certificate for weights (1,1,6,16)."""
from fractions import Fraction
from json import dumps

W=(1,1,6,16)
DEN=(2,7,17,7,17,22)

def port(a):
    return max(sum(max(x,0) for x in a),sum(max(-x,0) for x in a))

def moments(a):
    x,y,z=a
    return (x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)

def score(a):
    u,v,h=moments(a)
    return max(Fraction(n,d) for n,d in zip((abs(u),abs(v),abs(h),abs(v-u),abs(h-u),abs(h-v)),DEN))

B=(9,-5,1)
assert port(B)==10 and moments(B)==(0,-3,-6)
assert score(B)==Fraction(3,7)
limit=Fraction(9,14)
near=set()
for u in range(-1,2):
    for v in range(-4,5):
        for h in range(-10,11):
            if v%3 or (h-u)%6 or (h-u-6*v)%12:
                continue
            x=(h+19*u-8*v)//2
            y=(-h-14*u+7*v)//3
            z=(h+11*u-6*v)//12
            a=(x,y,z)
            if a!=(0,0,0) and score(a)<limit:
                near.add(max(a,tuple(-t for t in a)))
expected={(1,0,0),(5,-4,1),(9,-5,1),(10,-5,1),(15,-9,2),(19,-10,2),(25,-14,3)}
assert near==expected, (near,expected)
rows=[]
for a in sorted(near,key=lambda a:(port(a),a)):
    rows.append({'direction':list(a), 'port':port(a), 'score':str(score(a))})
assert [r['port'] for r in rows]==[1,6,10,11,17,21,28]
# Finite check independently tests all feasible q<=28, not used to prove the infinite-lattice bound.
all_vectors=[]
for x in range(-28,29):
    for y in range(-28,29):
        for z in range(-28,29):
            a=(x,y,z)
            if a==(0,0,0) or a<tuple(-t for t in a) or port(a)>28:
                continue
            all_vectors.append((a,port(a),score(a)))
for p in (10,11,17,21,27,28):
    eligible=[(a,q,f) for a,q,f in all_vectors if q<=p]
    assert min(f for a,q,f in eligible)==Fraction(3,7)
    assert {a for a,q,f in eligible if f<limit}=={a for a in near if port(a)<=p}
res={'id':'X6-R111-DUAL-WITNESS','status':'PASS','weight':[1,1,6,16],
     'eta_for_all_integer_p_ge_10':'3/7','strict_cutoff':'9/14',
     'moment_box':{'u':[-1,1],'v':[-4,4],'h':[-10,10]},
     'near_directions_all_ports':rows,
     'finite_q28_direction_count':len(all_vectors),
     'p_crosschecks':[10,11,17,21,27,28],
     'new_cone_example':{'R110_U_st':'1/2','new_U_b':'3/7','required_max':'8/17'},
     'scope':'Analytic infinite-lattice proof and all-p atlas at fixed weight; finite crosscheck q<=28'}
print(dumps(res,indent=2))
