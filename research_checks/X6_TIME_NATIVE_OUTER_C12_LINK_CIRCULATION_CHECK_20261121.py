"""Exact native OUTER-C12 link-circulation checks, frozen X6 source pin.
A conditional fiber lift is tested, not asserted as physical dynamics.
"""
import json
from itertools import product


def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-v for v in x)
def sub(x,y): return add(x,neg(y))
def unit(i): return tuple(1 if k==i else 0 for k in range(6))

A=[unit(0),unit(1),unit(2),neg(unit(0)),neg(unit(1)),neg(unit(2))]
points=[]
for r in range(6):
    points.extend((A[r],add(A[r],A[(r+1)%6])))
steps=[sub(points[(q+1)%12],points[q]) for q in range(12)]
checks=0
assert len(set(points))==12; checks+=1
assert all(sum(abs(v) for v in s)==1 for s in steps); checks+=1
assert all(points[(q+6)%12]==neg(points[q]) for q in range(12)); checks+=12
assert all(sum(v*v for v in points[q])==(1 if q%2==0 else 2) for q in range(12)); checks+=12
assert all(sum(s[i] for s in steps)==0 for i in range(6)); checks+=6
assert len({frozenset((points[q],points[(q+1)%12])) for q in range(12)})==12; checks+=1

from collections import Counter
counts=Counter(steps)
assert all(counts[s]==counts[neg(s)] for s in counts); checks+=len(counts)

mods=[6,12,24,48,96,192]
for N in mods:
    # Homogeneous, orientation-reversing, group-valued signed-axis link updates.
    for coeffs in product(range(3), repeat=3):
        weights=dict(zip([unit(i) for i in range(3)],coeffs))
        def w(s):
            for i in range(3):
                if s==unit(i): return weights[unit(i)]%N
                if s==neg(unit(i)): return -weights[unit(i)]%N
            raise AssertionError(s)
        assert sum(w(s) for s in steps)%N==0; checks+=1

    gamma=[3 if q in (5,11) else 0 for q in range(12)]
    assert gamma[5]==gamma[11]==3; checks+=1
    assert sum(gamma)%N==6%N; checks+=1
    for q in range(12):
        assert sum(gamma[(q+j)%12] for j in range(6))%N==3%N; checks+=1
        assert gamma[(q+6)%12]==gamma[q]; checks+=1
    # Reverse of each physical directed native edge is assigned minus the edge value.
    forward={(points[q],points[(q+1)%12]):gamma[q]%N for q in range(12)}
    reverse={(v,u):(-val)%N for (u,v),val in forward.items()}
    assert len(forward)==12 and len(reverse)==12; checks+=1
    for (u,v),val in forward.items():
        assert reverse[(v,u)]==(-val)%N; checks+=1
    # Homogeneous orientation-odd update cannot realize gamma when 6 != 0 mod N.
    if N>6:
        assert sum(gamma)%N!=0; checks+=1

# Coarse/fine readout distinguishes loop holonomy, not existence of a physical fiber.
observability={str(N):{"zero":0,"plus6":6%N,"minus6":(-6)%N,
                         "zero_vs_plus":(6%N)!=0,
                         "plus_vs_minus":(6%N)!=((-6)%N)} for N in mods}
assert observability['6']['zero_vs_plus'] is False; checks+=1
assert observability['12']['zero_vs_plus'] and not observability['12']['plus_vs_minus']; checks+=1
assert observability['24']['plus_vs_minus']; checks+=1

result={"schema":"X6_NATIVE_OUTER_C12_LINK_CIRCULATION_CHECK_V1",
"source_pin":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md",
"native_state_count":len(points),"native_directed_edge_count":len(steps),
"native_signed_steps":[list(s) for s in steps],"direction_histogram":{str(k):v for k,v in counts.items()},
"total_signed_displacement":[sum(s[i] for s in steps) for i in range(6)],
"homogeneous_axis_local_holonomy":0,"gamma_holonomy_integer":6,
"gamma_halfturn_increment_integer":3,"modular_readout":observability,
"checks":checks,"mismatches":0,
"scope":"exact finite representative of frozen OUTER native X6 twelve-cell cycle; fiber updates are explicitly conditional"}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
