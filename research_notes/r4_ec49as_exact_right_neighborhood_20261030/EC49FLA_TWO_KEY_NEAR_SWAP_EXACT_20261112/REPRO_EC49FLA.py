#!/usr/bin/env python3
"""Regenerate exact EC49FLA pair enumeration and complete 133-case solver input."""
from pathlib import Path
import sys, json, collections, itertools

HERE=Path(__file__).resolve().parent
PREDECESSOR=HERE.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'
sys.path.insert(0,str(PREDECESSOR))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, raw_key, pref

assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
CAT=list(all_words())
labels=sorted(set(l for l,w in CAT))
assert len(CAT)==178850 and len(labels)==24
label_id={label:i for i,label in enumerate(labels)}
bykey=collections.defaultdict(list)
coverage=collections.defaultdict(int)
rootset=collections.defaultdict(set)
for label,word in CAT:
    key=raw_key(word)
    native=pref(word)[-1]
    bykey[key].append((label_id[label],native.hex()))
    coverage[key] |= 1<<label_id[label]
    rootset[key].add(pref(word)[0][0])

universe=sorted(coverage)
assert len(universe)==94
base={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
unused=sorted(set(universe)-base)
FULL=(1<<24)-1

def norm(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))

def matched_distance(old,new):
    a,b=old;u,v=new
    return min(norm(a,u)+norm(b,v),norm(a,v)+norm(b,u))

near_total=collections.Counter()
near_feasible=collections.Counter()
all_covered=0
root_hist=collections.Counter()
cases=[]
for old in itertools.combinations(sorted(base),2):
    retained=base-set(old)
    retained_mask=0
    for key in retained:retained_mask |= coverage[key]
    for new in itertools.combinations(unused,2):
        dist=matched_distance(old,new)
        if dist<=3:near_total[dist]+=1
        full_cover=(retained_mask|coverage[new[0]]|coverage[new[1]])==FULL
        if not full_cover:continue
        all_covered+=1
        keys=retained|set(new)
        nr=len(set().union(*(rootset[k] for k in keys)))
        root_hist[nr]+=1
        if dist<=3:
            near_feasible[dist]+=1
            cases.append(dict(distance=dist,roots=nr,dropped=old,added=new,
                              keyset=sorted(keys)))

cases.sort(key=lambda x:(x['distance'],x['roots'],x['dropped'],x['added']))
assert sum(near_total.values())==556 and dict(near_total)=={2:98,3:458}
assert sum(near_feasible.values())==133 and dict(near_feasible)=={2:22,3:111}
assert all_covered==6315 and dict(root_hist)=={3:2198,4:4117}
assert len(cases)==133

(HERE/'EC49FLA_CASE_INDEX.json').write_text(json.dumps(cases,indent=2)+'\n')
with (HERE/'EC49FLA_CASES.txt').open('w') as f:
    f.write(f'{len(cases)}\n')
    for case in cases:
        rows=[r for key in case['keyset'] for r in bykey[tuple(key)]]
        f.write(f'{len(rows)}\n')
        for label,native in rows:f.write(f'{label} {native}\n')
print('EC49FLA_COVERAGE_AND_CASES_PASS',len(CAT),len(universe),
      'total_double_swaps',21*3741,'covered',all_covered,
      'distance_le3',sum(near_total.values()),
      'covered_near',len(cases),'roots',dict(root_hist))
