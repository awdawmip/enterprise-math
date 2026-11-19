#!/usr/bin/env python3
"""PREFIX-925: exact same-start collision family versus capacity and zero-zero."""
import json
from math import gcd
N=1<<32
L,U=262145,524287
C=33
Q=range(L,U+1,2)
def ceildiv(a,b):return (a+b-1)//b
def safe(a,b):
    return b>=C*ceildiv(N,a) and a>=C*ceildiv(N,b)
def W(b):
    r=2%b
    total=0
    for d in range(1,32):
        if r==1 or r==b-1:total+=32-d
        r=2*r%b
    return total
special=[(b,W(b)) for b in Q if W(b)]
assert len(special)==24
rows=[]
for b,w in special:
    # Four mutually exclusive classes: not-capacity-safe / capacity-safe
    # crossed with zero-zero collision / zero-zero safe.
    notsafe_notzz=notsafe_zz=safe_notzz=safe_zz=0
    for a in Q:
        is_safe=safe(a,b)
        zz=(a//gcd(a,b))*b<N
        if is_safe:
            if zz:safe_zz+=1
            else:safe_notzz+=1
        else:
            if zz:notsafe_zz+=1
            else:notsafe_notzz+=1
    rows.append({"b":b,"W32":w,"capacity_collision_only":notsafe_notzz,
                 "capacity_and_zerozero":notsafe_zz,
                 "three_family_new":safe_notzz,
                 "capacity_safe_zerozero":safe_zz})
assert all(sum((r["capacity_collision_only"],r["capacity_and_zerozero"],
                r["three_family_new"],r["capacity_safe_zerozero"]))==131072 for r in rows)
added=sum(r["three_family_new"] for r in rows)
b_intersect=sum(r["capacity_collision_only"]+r["capacity_and_zerozero"] for r in rows)
z_intersect=sum(r["capacity_and_zerozero"]+r["capacity_safe_zerozero"] for r in rows)
triple_intersect=sum(r["capacity_and_zerozero"] for r in rows)
assert (added,b_intersect,z_intersect,triple_intersect)==(1613509,1493890,93092,54763)
out={"schema":"PREFIX925_R6_SAME_START_THREE_FAMILY_UNION_V1",
     "special_b_count":len(rows),"same_start_support_ordered_pairs":24*131072,
     "same_start_outside_capacity_zerozero":added,
     "S_intersect_B":b_intersect,"S_intersect_Z":z_intersect,
     "S_intersect_B_intersect_Z":triple_intersect,
     "capacity_zerozero_union":7460895462,
     "three_family_union":7460895462+added,
     "remaining_after_three_family_union":9718973722-added,
     "rows":rows}
print(json.dumps(out,ensure_ascii=True,sort_keys=True))
