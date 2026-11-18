#!/usr/bin/env python3
"""Frozen BRC radius-three: all 3,709,825 complete seven-key replacements.
Writes exact C++ cached-trie input and support-coverable sorted case index.
Python standard library; no numerical approximations.
Usage: python BUILD_EC49FMI.py OUTPUT_DIR [GENERATOR_DIRECTORY]
"""
import collections
import functools
import hashlib
import itertools
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
GEN=Path(sys.argv[2]) if len(sys.argv)>2 else HERE.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'
sys.path.insert(0,str(GEN))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,pref,raw_key
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
OUT=Path(sys.argv[1]);OUT.mkdir(parents=True,exist_ok=True)
cat=list(all_words());assert len(cat)==178850
labels=sorted({lab for lab,_ in cat});assert len(labels)==24
li={lab:i for i,lab in enumerate(labels)}
by_key=collections.defaultdict(list)
support=collections.defaultdict(int)
for lab,word in cat:
    k=raw_key(word)
    by_key[k].append((li[lab],pref(word)[-1].hex()))
    support[k]|=1<<li[lab]
keys=sorted(support);assert len(keys)==94
ki={k:i for i,k in enumerate(keys)}
base={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
assert base <= set(keys)
outside=sorted(set(keys)-base)
all_mask=(1<<24)-1
cases=[];n=0
for drop in itertools.combinations(sorted(base),3):
    kept=base-set(drop)
    retained=functools.reduce(int.__or__,(support[k] for k in kept),0)
    for add in itertools.combinations(outside,3):
        n+=1
        if retained|support[add[0]]|support[add[1]]|support[add[2]] != all_mask:
            continue
        cases.append([ki[k] for k in sorted(kept|set(add))])
assert n==3709825 and len(cases)==38169,(n,len(cases))
master=OUT/'master_and_radius3_cases.txt'
with master.open('w') as f:
    f.write(f'94 178850 {len(cases)}\n')
    for key in keys:
        rows=by_key[key]
        f.write(f'{len(rows)}\n')
        for lab,code in rows:f.write(f'{lab} {code}\n')
    for case in cases:f.write(' '.join(map(str,case))+'\n')
sha=hashlib.sha256(master.read_bytes()).hexdigest()
assert sha=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e',sha
(OUT/'radius3_cases.json').write_text(json.dumps({'pin':PIN,'keys':keys,'cases':cases},separators=(',',':'))+'\n')
print('RADIUS3_EXACT_SUPPORT_PASS',n,len(cases),sha)
