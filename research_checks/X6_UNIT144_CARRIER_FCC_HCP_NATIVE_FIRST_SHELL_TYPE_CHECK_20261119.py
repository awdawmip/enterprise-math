#!/usr/bin/env python3
"""Exact typed first-shell metric/trace comparison; author research checker.
Historical source scripts/check_p000_first_shell_polyhedron_classification.py
at fd2bcff10ca6e147348b6c1236027fc0d2877df3 (same blob on current main).
Current X6 Cell definitions at 59538f585d037d09ef687b28715c4bc1a3f9fe03.
The 3-component q-shell models are carrier representations, not native Cell addresses.
"""
from collections import Counter
from itertools import combinations
import json
import math

R=((2,0,0),(1,3,0),(-1,3,0),(-2,0,0),(-1,-3,0),(1,-3,0))
U=((1,1,1),(-1,1,1),(0,-2,1))
CARRIER={
    "FCC_C":R+U+((0,2,-1),(-1,-1,-1),(1,-1,-1)),
    "HCP_H":R+U+((1,1,-1),(-1,1,-1),(0,-2,-1)),
}

def carrier_q(a,b):
    d=tuple(x-y for x,y in zip(a,b))
    return 3*d[0]**2+d[1]**2+8*d[2]**2

def native_g(a,b):
    return sum((x-y)**2 for x,y in zip(a,b))

def native_brc(a,b):
    z=[abs(x-y) for x,y in zip(a,b)]
    out=math.factorial(sum(z))
    for v in z:
        out//=math.factorial(v)
    return out

def require(ok,name):
    if not ok: raise RuntimeError("CHECK_FAILED:"+name)

def run():
    native=[tuple(s if j==i else 0 for j in range(6))
            for i in range(6) for s in (-1,1)]
    require(len(native)==len(set(native))==12,"native_size")
    require(all(native_g(z,(0,)*6)==1 for z in native),"native_radius")
    pairs=list(combinations(native,2))
    ng=Counter(native_g(a,b) for a,b in pairs)
    br=Counter(native_brc(a,b) for a,b in pairs)
    l1=Counter(sum(abs(x-y) for x,y in zip(a,b)) for a,b in pairs)
    require(ng==Counter({2:60,4:6}),"native_metric")
    require(br==Counter({2:60,1:6}),"native_brc")
    require(l1==Counter({2:66}),"native_l1")
    out={"schema":"ENTERPRISE_MATH_X6_UNIT144_CARRIER_NATIVE_FIRST_SHELL_EXACT_V1",
        "typed_source":"CARRIER_Q3_VS_NATIVE_SIGNED_X6_COMPONENT_G",
        "native":{"endpoints":12,"pair_count":66,
                  "component_norm_squared_hist":dict(sorted(ng.items())),
                  "shortest_path_N_BRC_hist":dict(sorted(br.items())),
                  "primitive_step_L1_hist":dict(sorted(l1.items())),
                  "one_step_adjacent_first_shell_pairs":0,
                  "opposite_pairs":6,"centrally_symmetric_about_anchor":True},
        "carrier":{}}
    for model,sites in CARRIER.items():
        require(len(sites)==len(set(sites))==12,"carrier_size_"+model)
        require(all(carrier_q(z,(0,0,0))==12 for z in sites),
                "carrier_radius_"+model)
        hist=Counter(carrier_q(a,b) for a,b in combinations(sites,2))
        require(sum(hist.values())==66,"carrier_pair_count_"+model)
        contacts=hist[12]
        require(contacts==24,"carrier_contacts_"+model)
        opposite=sum(all(x==-y for x,y in zip(a,b))
                     for a,b in combinations(sites,2))
        symmetric=all(tuple(-x for x in z) in sites for z in sites)
        require(symmetric==(model=="FCC_C"),"carrier_symmetry_"+model)
        require(hist!=Counter({24:60,48:6}),"carrier_native_obstruction_"+model)
        out["carrier"][model]={
            "endpoints":12,"pair_count":66,"q_radius_squared":12,
            "pair_q_squared_hist":dict(sorted(hist.items())),
            "q_distance_12_contact_pairs":contacts,
            "opposite_pairs":opposite,
            "centrally_symmetric_about_anchor":symmetric,
            "matches_12_times_X6_native_G_distance_hist":False}
    print(json.dumps(out,sort_keys=True,ensure_ascii=False,separators=(",",":")))

if __name__=="__main__":
    run()
