#!/usr/bin/env python3
"""R663: exact V17 slot transport over all V36 eligible length-four cyclic triad words."""
from itertools import combinations
from collections import Counter
import json
from pathlib import Path

TRIADS = tuple(combinations(range(6),3))
BASE = (0,1,2)
def adjacent(a,b):
    return len(set(a)&set(b))==2
def update_slot(old,new,slots):
    assert adjacent(old,new)
    leave=next(iter(set(old)-set(new)))
    enter=next(iter(set(new)-set(old)))
    f=dict(zip(old,slots))
    f[enter]=f[leave]
    return tuple(f[x] for x in new)
def holonomy(word):
    assert word[0]==BASE and len(word)==4
    slots=(0,1,2)
    for old,new in zip(word,word[1:]+(BASE,)):
        slots=update_slot(old,new,slots)
    return slots

counts=Counter()
examples={}
for a in TRIADS:
    if not adjacent(BASE,a):continue
    for b in TRIADS:
        if not adjacent(a,b):continue
        for c in TRIADS:
            if not adjacent(b,c) or not adjacent(c,BASE):continue
            w=(BASE,a,b,c)
            h=holonomy(w)
            counts[h]+=1
            examples.setdefault(h,w)
expected={(0,1,2):207,(0,2,1):48,(2,1,0):48,(2,0,1):9,(1,2,0):9,(1,0,2):48}
assert dict(counts)==expected and sum(counts.values())==369
assert len(examples)==6 and set(examples)==set(expected)
w_flat=(BASE,(0,1,3),BASE,(0,1,3))
w_rot=(BASE,(0,1,3),(0,2,3),(1,2,3))
w_odd=(BASE,(0,1,3),(0,1,4),(0,2,4))
assert holonomy(w_flat)==BASE
assert holonomy(w_rot)==(2,0,1)
assert holonomy(w_odd)==(0,2,1)
for w in (w_flat,w_rot,w_odd):
    assert all(adjacent(x,y) for x,y in zip(w,w[1:]+(BASE,)))
chart=((0,0,0,0,0,0),(1,0,0,0,0,0),(1,1,0,0,0,0),(0,1,0,0,0,0))
for i in range(4):
    d=tuple(chart[(i+1)%4][j]-chart[i][j] for j in range(6))
    assert sum(abs(z) for z in d)==1
marker="R663_V36_FOUR_RING_ALL_S3_SEED_DEPENDENT_HOLONOMY_PASS"
result={
  "marker":marker,"science_pin":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
  "exact_source":"X6_ACTIVE_LOOP_TO_DIRECTED_RING_REALIZATION_V36_20260906.md @ blob b104e09cdb7479d0d981492ddfb20b713cc817d9",
  "base_triad":BASE,"length4_closed_words":369,
  "holonomy_counts":{str(k):v for k,v in sorted(counts.items())},
  "examples":{str(k):list(w) for k,w in sorted(examples.items())},
  "two_distinct_seed_holonomies":{"flat":holonomy(w_flat),"rotation":holonomy(w_rot),"odd":holonomy(w_odd)},
  "x6_native_unit_steps":True,
  "scope":"V36 one-context directed four-cell ring; V29 transfer permission H uninstantiated; abstract relational time not heartbeat",
  "review":"AUTHOR_SIDE_UNREVIEWED"
}
Path(__file__).with_name("R663_EVIDENCE_RECOMPUTED.json").write_text(
    json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(marker,"closed_words",sum(counts.values()),"counts",dict(counts))
