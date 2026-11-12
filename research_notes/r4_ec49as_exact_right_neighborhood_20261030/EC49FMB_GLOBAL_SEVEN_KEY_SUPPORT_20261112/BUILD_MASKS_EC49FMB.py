#!/usr/bin/env python3
"""Regenerate full raw-key 24-bit masks from the frozen signed-X6 BRC catalogue."""
import sys, json, collections
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, raw_key
assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
SEED={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
labels=sorted((h,s) for h,signatures in REQ.items() for s in signatures)
assert len(labels)==24
bits={label:1<<i for i,label in enumerate(labels)}
support=collections.defaultdict(int)
n=0
for label, word in all_words():
    support[raw_key(word)] |= bits[label]
    n += 1
assert n==178850 and len(support)==94 and SEED<=support.keys()
forced_keys={(2,1,1),(3,0,1)}
assert {key for key in support if support[key]&bits[(2,16)]}=={(3,0,1)}
assert {key for key in support if support[key]&bits[(2,32)]}=={(2,1,1)}
outside=sorted(support.keys()-forced_keys)
assert len(outside)==92
missing=((1<<24)-1) & ~(support[(2,1,1)]|support[(3,0,1)])
remaining_seed=SEED-forced_keys
rows=[(support[k]&missing,int(k in remaining_seed)) for k in outside]
(P/'MASKS_EC49FMB.txt').write_text(str(len(rows))+' '+str(missing)+'\n'+
    ''.join(f'{mask} {seed}\n' for mask,seed in rows))
print('GLOBAL_MASK_INPUT_PASS',n,len(support),len(labels),len(outside),missing)
