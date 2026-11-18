#!/usr/bin/env python3
"""Rebuild five-action 16-state maximal-support families using exact pinned counts."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
H=(18,24,82,34,17,0,1,2,3,144,208,255,50,66,4,5)
K=(214,215,216,223,296)
U=58182461585441404127941754880
raw=(ROOT/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()==SHA
D=json.loads(raw)['counts_and_cohorts']
def supports(v,tau):
 m={}
 for i,x in enumerate(v):m[x]=m.get(x,0)|(1<<i)
 cand={sum(bit for val,bit in m.items() if start<=val<=start+tau) for start in m}
 return sorted(s for s in cand if not any(s!=t and s&t==s for t in cand))
lines=[f'{len(H)} {len(K)}']
for k in K:
 v=[int(D[str(k)]['counts'][h]) for h in H]
 z=supports(v,U-1)
 lines.append(f'{k} {len(z)} '+' '.join(map(str,z)))
txt='\n'.join(lines)+'\n'
assert txt==(ROOT/'ACTIONS_H16_PLUS_5.txt').read_text()
print('PASS_R5_H16_FIVE_QUERY_MAX_SUPPORTS',hashlib.sha256(txt.encode()).hexdigest())
