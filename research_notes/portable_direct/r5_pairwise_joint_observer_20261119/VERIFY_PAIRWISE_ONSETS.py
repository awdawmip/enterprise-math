#!/usr/bin/env python3
"""Exact named nine-slot pairwise-onset census from frozen R5 center JSON."""
from pathlib import Path
import bisect, hashlib, json, itertools, collections
P=Path(__file__).resolve().parent
raw=(P/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
expected='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
assert hashlib.sha256(raw).hexdigest()==expected
D=json.loads(raw)['counts_and_cohorts'];T=json.loads((P/'stages_18.json').read_text())
assert T['frozen_sha256']==expected
S=list(map(int,T['stage_taus']))
assert len(S)==18 and S==sorted(S) and len(set(S))==18
H=(18,24,82,34,17,144,208)
X=[i for i in range(256) if i not in H];assert len(X)==249
rows=[list(map(int,D[str(k)]['counts'])) for k in range(214,315)]
assert len(rows)==101 and all(len(r)==256 for r in rows)
onset=lambda v:bisect.bisect_left(S,v)
unary=[{x:bytes(onset(abs(row[x]-row[h])) for h in H) for x in X} for row in rows]
first_unary={};binary_keys=set();full_keys=set();endpoint_keys=set()
splits=collections.defaultdict(set);first_joint_witness=None
for x,y in itertools.combinations(X,2):
    u=bytearray();b=bytearray();f=bytearray();e=bytearray()
    for ki,row in enumerate(rows):
        ux=unary[ki][x];uy=unary[ki][y];z=onset(abs(row[x]-row[y]))
        u.extend(ux);u.extend(uy);b.append(z)
        f.extend(ux);f.extend(uy);f.append(z)
        for d in (*ux,*uy,z):e.extend((d==0,d<=17))
    ut,bt,ft,et=map(bytes,(u,b,f,e))
    if ut not in first_unary:first_unary[ut]=((x,y),ft)
    elif ft!=first_unary[ut][1] and first_joint_witness is None:
        first_joint_witness=(first_unary[ut][0],(x,y))
    binary_keys.add(bt);endpoint_keys.add(et);full_keys.add(ft)
    splits[ut].add(ft)
U=len(first_unary);B=len(binary_keys);F=len(full_keys);E=len(endpoint_keys)
assert (U,B,F,E)==(1663,145,2711,2563),(U,B,F,E)
assert sum(len(v)>1 for v in splits.values())==448
assert first_joint_witness==((0,1),(0,49))
print('PASS_PAIRWISE_ONSETS_PYTHON',U,B,F,E,'JOINT_SPLITS',448,'WITNESS',first_joint_witness)
