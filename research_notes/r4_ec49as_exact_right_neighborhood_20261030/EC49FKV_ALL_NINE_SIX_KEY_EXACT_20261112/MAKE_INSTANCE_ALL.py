#!/usr/bin/env python3
"""Generate exact signed-X6 word instances for the nine frozen residual key sets."""
import pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
PARENT=HERE.parent
for d in (HERE,PARENT/'EC49FJD_RELEASE_B11_COMPLETE_20261111',PARENT/'EC49FKS_EXACT_FRACTIONAL_BARRIER_20261112'):
 if d.exists():sys.path.insert(0,str(d))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,raw_key,pref,REQ
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
KEY_BASE={(2,1,1),(3,0,1),(3,1,1),(4,2,1)}
EXTRAS=[((5,4,1),(5,5,1)), ((5,4,1),(6,4,1)),((6,3,1),(6,4,1)),((6,3,1),(7,3,1)),((6,4,1),(6,6,1)),((6,4,1),(7,5,1)),((6,4,1),(7,6,1)),((6,4,1),(8,4,1)),((6,4,1),(8,5,1))]
LABELS=sorted((h,s) for h,labs in REQ.items() for s in labs)
assert len(LABELS)==24
IDX={label:i for i,label in enumerate(LABELS)}
if __name__=='__main__':
 case=int(sys.argv[1]);assert 0<=case<9
 keys=KEY_BASE|set(EXTRAS[case]);count=0
 for label,w in all_words():
  if raw_key(w) in keys:
   print(IDX[label],pref(w)[-1].hex());count+=1
 assert count>=1000
