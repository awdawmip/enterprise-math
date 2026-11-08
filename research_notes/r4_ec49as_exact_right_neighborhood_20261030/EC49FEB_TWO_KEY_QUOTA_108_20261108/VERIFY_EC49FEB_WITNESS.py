#!/usr/bin/env python3
"""Independent explicit literal witness verifier (standard library)."""
import json
from pathlib import Path
from collections import Counter
a=json.loads(Path(__file__).with_name("EC49FEB_EXACT_WITNESS.json").read_text())
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0)
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
Q={4:2,5:4,6:2,7:4,8:4,9:2}
count=Counter();seen={h:set() for h in Q};masks=Counter()
for h,word,key,sig in a['paths']:
    assert h in Q and len(word)==h and word not in seen[h]
    seen[h].add(word);count[h]+=1
    q=0;native=[]
    for c in word:
        q=T[q]['acdefg'.index(c)]
        native.extend(OPS[c])
    pos=Counter(x for x in native if x>0)
    displacement=[native.count(i)-native.count(-i) for i in range(1,7)]
    assert S[q]==sig
    assert displacement==[2,0,0,0,0,0]
    assert [pos[1],pos[2],pos[3]]==key
    assert len(native)==2*sum(key)-2
    masks[h]|=sig
assert count==Counter(Q)
assert all(all(masks[h]&c for c in (18,20,33,40)) for h in Q)
assert len(a['paths'])==18
assert {tuple(k) for _,_,k,_ in a['paths']}=={(3,2,1),(3,4,1),(6,4,1)}
assert sum(tuple(k)==(6,4,1) for h,_,k,_ in a['paths'] if h==5)==1
print("18/18 words, 6/6 rank masks, complete BRC keys, signed X6 +2E1: PASS")
