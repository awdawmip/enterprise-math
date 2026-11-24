#!/usr/bin/env python3
"""Exact finite witness/slack/schedule verifier, derived scalar R5 fifth chamber.
Run next to frozen EXACT_R5_ALL_101_BUDGETS.json (SHA256 checked).
All-f assertion is mathematically proved in RESEARCH.md.
"""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
FILE=ROOT/'EXACT_R5_ALL_101_BUDGETS.json'
SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
raw=FILE.read_bytes()
assert hashlib.sha256(raw).hexdigest()==SHA
D=json.loads(raw)['counts_and_cohorts']
N={k:tuple(map(int,D[str(k)]['counts'])) for k in range(214,315)}
assert len(N)==101 and all(len(a)==256 for a in N.values())
L=25845652773852463277015040000
U=58182461585441404127941754880
W=[((0,64),223),((1,2),1),((2,8),215),((16,32),296)]
SETS=[set(range(223,291)),set([214]+list(range(216,222))),
      set(range(215,222)),set(range(296,313))]
P=[(a,b) for a in range(256) for b in range(a+1,256)]
assert len(P)==32640

def split(k,a,b,tau):
    return abs(N[k][a]-N[k][b])>tau

for (pair,_),expected in zip(W,SETS):
    assert {k for k in N if split(k,*pair,L)}==expected
    assert {k for k in N if split(k,*pair,U-1)}==expected

s={k:k-sum(w for (a,b),w in W if split(k,a,b,L)) for k in N}
assert min(s.values())==0
assert {k for k in N if s[k]==0}=={215,216,223,296}
assert {k for k in N if s[k]==1}=={217,224,297}
# This classification plus the four witness equalities proves both uniqueness
# and the EXHAUSTIVE list of cost-gap-one candidate multisets.

triple=(216,223,296)
swaps=((216,217),(223,224),(296,297))
for old,new in swaps:
    modified=tuple(new if k==old else k for k in triple)
    assert sum(modified)==736
    assert all(any(split(k,a,b,U-1) for k in modified) for a,b in P)

# General-t correctness follows since unchanged budgets are repeated t times
# and the changed budget t-1 times plus one copy of the new budget.
# Finite high-t checks independently exercise that counting argument.
for t in (1,3,17,61):
    for old,new in swaps:
        counts={k:t for k in triple}
        counts[old]-=1
        counts[new]=1
        assert sum(k*v for k,v in counts.items())==735*t+1
        assert all(sum(v for k,v in counts.items()
                       if split(k,a,b,U-1))>=t for a,b in P)
print('PASS_R5_UNIQUE_OPTIMUM_THREE_SECOND_BEST_ALL_F')
print('frozen_sha256',SHA,'budgets',len(N),'pairs',len(P))
print('zero_slack',sorted(k for k in s if s[k]==0))
print('one_slack',sorted(k for k in s if s[k]==1))
print('optimal: each of 216,223,296 repeated 2*f+1; cost 735*(2*f+1)')
print('second: swap one of 216->217,223->224,296->297; cost 735*(2*f+1)+1')
