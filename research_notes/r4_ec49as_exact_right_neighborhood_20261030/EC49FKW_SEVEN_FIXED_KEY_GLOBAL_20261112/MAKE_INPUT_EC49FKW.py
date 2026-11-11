#!/usr/bin/env python3
"""Print fixed-key legal candidates as (label-number, full signed native X6 step bytes)."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'
sys.path.insert(0,str(ROOT))
from EC49FGW_RADIUS5_SCREEN import all_words,raw_key,pref,W,REQ,PIN
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert len(sys.argv)==2
profile=next(p for p in W['profiles'] if p['profile_id']==sys.argv[1])
keys=set(map(tuple,profile['allowed_keys']))
labels=sorted((h,s) for h,v in REQ.items() for s in v)
labelno={lab:i for i,lab in enumerate(labels)}
for lab,w in all_words():
 if raw_key(w) in keys:print(labelno[lab],pref(w)[-1].hex())
