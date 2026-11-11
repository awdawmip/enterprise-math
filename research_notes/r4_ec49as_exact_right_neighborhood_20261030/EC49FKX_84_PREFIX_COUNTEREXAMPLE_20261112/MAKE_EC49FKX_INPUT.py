#!/usr/bin/env python3
"""Emit all exact frozen BRC signed-native word candidates for the 84-prefix key set.
Run this script from a checked-out research PR (imports the frozen EC49FGW generator).
"""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'
sys.path.insert(0, str(ROOT))
from EC49FGW_RADIUS5_SCREEN import all_words, raw_key, pref, REQ, PIN
K = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
labels = sorted((h,s) for h, ss in REQ.items() for s in ss)
idx = {v:i for i,v in enumerate(labels)}
assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
for label, w in all_words():
    if raw_key(w) in K:
        print(idx[label], pref(w)[-1].hex())
