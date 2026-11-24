#!/usr/bin/env python3
"""Exact four-pair dual + 32640-pair construction certificate, all integer f>=0."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=(ROOT/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
sha='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
assert hashlib.sha256(raw).hexdigest()==sha
D=json.loads(raw)['counts_and_cohorts']
N={k:list(map(int,D[str(k)]['counts'])) for k in range(214,315)}
assert len(N)==101 and all(len(x)==256 for x in N.values())
L=25845652773852463277015040000
U=58182461585441404127941754880
W=[(0,64,223),(1,2,1),(2,8,215),(16,32,296)]
expected=[list(range(223,291)),[214]+list(range(216,222)),list(range(215,222)),list(range(296,313))]
for (h,j,_),target in zip(W,expected):
 assert [k for k,v in N.items() if abs(v[h]-v[j])>L]==target
 assert [k for k,v in N.items() if abs(v[h]-v[j])>U-1]==target
for k,v in N.items():
 assert sum(w for h,j,w in W if abs(v[h]-v[j])>L)<=k
assert sum(w for _,_,w in W)==735
T=(216,223,296)
for h in range(256):
 for j in range(h+1,256):
  assert any(abs(N[k][h]-N[k][j])>=U for k in T),(h,j)
# Full 101-budget pair coverage classification.
separations=[]
for h in range(256):
 for j in range(h+1,256):
  separations.append(tuple(k for k in N if abs(N[k][h]-N[k][j])>=U))
coverage={k:0 for k in N}
for i,d in enumerate(separations):
 for k in d:coverage[k]|=1<<i
FULL=(1<<len(separations))-1
keys=list(N)
for i in range(len(keys)):
 for j in range(i+1,len(keys)):
  assert coverage[keys[i]]|coverage[keys[j]]!=FULL
low=[]
for i,a in enumerate(keys):
 for j,b in enumerate(keys[i+1:],start=i+1):
  ab=coverage[a]|coverage[b]
  for c in keys[j+1:]:
   if a+b+c>735:break
   if ab|coverage[c]==FULL:low.append((a,b,c))
assert low==[(216,223,296)]
print('PASS_FULL256_FIXED_SCHEDULE_ALL_F_CERTIFICATE')
print('pairs=32640 budgets=101 witnesses=',W)
print('optimal_fixed_cost=735*(2f+1), all integer f>=0, L<=tau<U')
print('f8_exact=12495, achieving budgets=216,223,296 each 17 times')
