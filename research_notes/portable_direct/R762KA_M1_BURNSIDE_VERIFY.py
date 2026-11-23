#!/usr/bin/env python3
"""R762KA: exact Burnside orbit counts for one inactive composite Port.
Python >=3.10, pure integers and standard library. No Euler feasibility claim.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb
import json

A=tuple(range(6))
S=tuple(combinations(A,3))
idx={s:i for i,s in enumerate(S)}
F={i for i,s in enumerate(S) if {0,1}.issubset(s)}
H=tuple(p for p in permutations(A) if {p[0],p[1]}=={0,1})
assert len(S)==20 and len(F)==4 and len(H)==48

def cycles(p):
    perm=[idx[tuple(sorted(p[i] for i in s))] for s in S]
    todo=set(range(20)); out=[]
    while todo:
        start=min(todo); cur=start; c=[]
        while cur in todo:
            todo.remove(cur); c.append(cur); cur=perm[cur]
        assert cur==start
        assert all(i in F for i in c) or all(i not in F for i in c)
        out.append(tuple(c))
    return out

def fixed_profiles(cycles_):
    # DP indexed by singleton size, triple size, forced singleton, forced triple.
    dp={(0,0,0,0):1}
    for c in cycles_:
        l=len(c); f=l if c[0] in F else 0
        nxt=Counter()
        for (d,t,df,tf),n in dp.items():
            nxt[d,t,df,tf]+=n
            if d+l<=5: nxt[d+l,t,df+f,tf]+=n
            if t+l<=7: nxt[d,t+l,df,tf+f]+=n
        dp=nxt
    return Counter({(df,tf):n for (d,t,df,tf),n in dp.items() if d==5 and t==7})

fixed=Counter(); types=Counter(); fixed_type={}
Dfixed=Counter()
for h in H:
    cs=cycles(h)
    typ=tuple(sorted(Counter(map(len,cs)).items()))
    types[typ]+=1
    part=fixed_profiles(cs)
    fixed.update(part)
    fixed_type[typ]=sum(part.values())
    dp={(0,0):1}
    for c in cs:
        l=len(c); f=l if c[0] in F else 0
        nxt=Counter(dp)
        for (d,df),n in dp.items():
            if d+l<=5: nxt[d+l,df+f]+=n
        dp=nxt
    for df in range(5):
        Dfixed[df]+=dp.get((5,df),0)

assert all(v%48==0 for v in fixed.values())
assert all(v%48==0 for v in Dfixed.values())
orbits={k:v//48 for k,v in sorted(fixed.items())}
D_orbits={k:v//48 for k,v in sorted(Dfixed.items())}
assert sum(orbits.values())==2094150
assert D_orbits=={0:124,1:189,2:93,3:18,4:2}
labeled={(d,t):comb(4,d)*comb(16,5-d)*comb(4-d,t)*comb(11+d,7-t)
         for d in range(5) for t in range(5-d)}
assert sum(labeled.values())==comb(20,5)*comb(15,7)==99768240

# Independent direct enumeration of D orbits: no Burnside coefficient arithmetic.
maps=[tuple(idx[tuple(sorted(h[i] for i in s))] for s in S) for h in H]
unseen=set(combinations(range(20),5))
D_direct=Counter(); sizes=Counter()
while unseen:
    D=min(unseen)
    orb={tuple(sorted(m[i] for i in D)) for m in maps}
    assert orb<=unseen
    unseen-=orb
    D_direct[len(set(D)&F)]+=1
    sizes[len(orb)]+=1
assert dict(D_direct)==D_orbits
assert sizes==Counter({4:2,8:2,12:34,24:148,48:240})
assert sum(k*v for k,v in sizes.items())==15504

record={
 "schema":"R762KA_M1_BURNSIDE_EVIDENCE_V1",
 "model":"UNSIGNED_COMPOSITE_PORT_EULER_ONE_INACTIVE_PORT",
 "date":"2026-11-23","inactive_port":[0,1],"group_order":48,
 "colors":20,"forced_colors":4,"D_size":5,"T_size":7,
 "labeled_targets":99768240,"D_orbits":426,"joint_orbits":2094150,
 "D_profile_orbits":{str(k):v for k,v in D_orbits.items()},
 "D_orbit_size_distribution":{str(k):v for k,v in sorted(sizes.items())},
 "cycle_types":[{"signature":[list(item) for item in typ],
                 "elements":n,"fixed_joint_per_element":fixed_type[typ]}
                for typ,n in sorted(types.items())],
 "joint_profiles":[{"d":d,"t":t,"labeled":labeled[d,t],"orbits":orbits[d,t]}
                   for d,t in sorted(orbits)],
 "exact_coverage":"All 48 H permutations and all 15,504 D via independent direct orbit method",
 "review":"AUTHOR_EXACT_INTEGER_CHECKED_NOT_REVIEWED",
 "limitations":["Orbit count, not Euler existence","No signed P000/BRC native lift"]
}
if __name__=="__main__":
    with open("R762KA_M1_BURNSIDE_EVIDENCE.json","w",encoding="utf-8") as f:
        json.dump(record,f,ensure_ascii=False,indent=2)
    print(json.dumps({"D_orbits":sum(D_orbits.values()),"joint_orbits":sum(orbits.values()),
                       "profiles":len(orbits),"cycle_classes":len(types),
                       "labeled_targets":sum(labeled.values()),"checks":"PASS"},sort_keys=True))
