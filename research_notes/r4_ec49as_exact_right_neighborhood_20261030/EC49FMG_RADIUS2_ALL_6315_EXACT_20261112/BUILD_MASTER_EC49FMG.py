#!/usr/bin/env python3
"""Generate the complete pinned BRC radius-two feasible input catalogue.
Usage: python BUILD_MASTER_EC49FMG.py OUTPUT_DIRECTORY
Then: g++ -std=c++17 -O2 SCAN_CACHED_EC49FMG.cpp -o scan
      ./scan 0 6315 < OUTPUT_DIRECTORY/master_and_cases.txt > exact_raw_6315.txt
"""
import collections, functools, itertools, json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, pref, raw_key
assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
base = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
catalogue = list(all_words())
labels = sorted({lab for lab, _ in catalogue})
lid = {lab:i for i,lab in enumerate(labels)}
by_key = collections.defaultdict(list)
support = collections.defaultdict(int)
for lab, w in catalogue:
    k = raw_key(w)
    by_key[k].append((lid[lab], pref(w)[-1].hex()))
    support[k] |= 1 << lid[lab]
assert len(catalogue) == 178850 and len(labels) == 24 and len(support) == 94
keys = sorted(support)
ki = {k:i for i,k in enumerate(keys)}
outside = sorted(set(support) - base)
full = (1 << 24) - 1
cases, sets = [], []
for drop in itertools.combinations(sorted(base), 2):
    for add in itertools.combinations(outside, 2):
        K = sorted((base-set(drop))|set(add))
        if functools.reduce(int.__or__, (support[k] for k in K), 0) == full:
            cases.append([ki[k] for k in K])
            sets.append(K)
assert len(cases) == 6315
output = pathlib.Path(sys.argv[1])
output.mkdir(exist_ok=True, parents=True)
with (output / 'master_and_cases.txt').open('w') as out:
    out.write('94 178850 6315\n')
    for k in keys:
        rows = by_key[k]
        out.write(str(len(rows)) + '\n')
        for lab, p in rows: out.write(f'{lab} {p}\n')
    for case in cases: out.write(' '.join(map(str, case)) + '\n')
(output/'master_descriptor.json').write_text(json.dumps({
    'pin':PIN,'cache_keys':keys,'number_cases':len(cases),
    'number_words':len(catalogue),'root_support_masks':{str(k):support[k] for k in keys},
    'cases':cases
},separators=(',',':')) + '\n')
print('EC49FMG_PINNED_ALL_CASES_PASS',len(catalogue),len(keys),len(cases))
