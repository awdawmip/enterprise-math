#!/usr/bin/env python3
"""Exact finite R5 six-state Bellman and 64 quartet certification.

Uses frozen JSON from the R5 source package; all comparisons are exact integers.
Run: python3 VERIFY_R5_HARD_SEXTET.py EXACT_R5_ALL_101_BUDGETS.json stages_18.json
"""
import json,hashlib,sys,itertools,collections
from functools import lru_cache
from pathlib import Path

p=Path(sys.argv[1]) if len(sys.argv)>1 else Path('EXACT_R5_ALL_101_BUDGETS.json')
q=Path(sys.argv[2]) if len(sys.argv)>2 else Path('stages_18.json')
raw=p.read_bytes()
PIN='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
assert hashlib.sha256(raw).hexdigest()==PIN
source=json.loads(raw)
cs={k:tuple(int(v) for v in source['counts_and_cohorts'][str(k)]['counts'])
    for k in range(214,315)}
assert len(cs)==101 and all(len(row)==256 for row in cs.values())
stage=json.loads(q.read_text())
L,U=int(stage['L']),int(stage['U'])
tau=U-1
H=(0,16,32,48,1,64)

def maximal(sets):
    return tuple(sorted(s for s in sets if not any(s!=t and s&t==s for t in sets)))

def center_windows(k):
    a=[cs[k][h] for h in H]
    return maximal({sum(1<<i for i,c in enumerate(a) if v<=c<=v+tau) for v in a})

def interval_events(k):
    a=[cs[k][h] for h in H]
    endpoints=sorted({2*c-tau for c in a})
    return maximal({sum(1<<i for i,c in enumerate(a) if 2*c-tau<=y<=2*c+tau)
                    for y in endpoints})

families={k:center_windows(k) for k in range(214,315)}
assert all(families[k]==interval_events(k) for k in families)
cls=collections.defaultdict(list)
for k,mask in families.items():cls[mask].append(k)
assert len(cls)==5
assert {(min(v),s) for s,v in cls.items()}=={
    (214,(16,47)),(222,(63,)),(223,(31,32)),
    (295,(6,8,49)),(296,(2,4,8,49))}
active=(214,223,295,296)

def calc(f):
    @lru_cache(None)
    def V(e):
        live=sum(1<<i for i,c in enumerate(e) if c<=f)
        if live.bit_count()<=1:return 0
        best=None
        for k in active:
            fam=families[k]
            if any((s&live)==live for s in fam):continue
            worst=0
            for s in fam:
                new=tuple(min(f+1,c+(0 if s>>i&1 else 1)) for i,c in enumerate(e))
                worst=max(worst,V(new))
            candidate=k+worst
            if best is None or candidate<best:best=candidate
        assert best is not None
        return best
    root=V((0,)*6)
    return root,V.cache_info().currsize

expected=[732,1678,2624,3570,4516,5462,6408,7354,8300,9246,10192,11138]
states=[]
for f,val in enumerate(expected):
    got,c=calc(f)
    assert got==val,(f,got,val)
    states.append(c)
assert states[8]==80455
cohorts=[tuple(64*b+a+16*j for j in range(4))
         for b in range(4) for a in range(16)]
assert len(cohorts)==64 and len({i for C in cohorts for i in C})==256
taus=list(map(int,stage['stage_taus']))
assert len(taus)==18 and taus==sorted(set(taus)) and taus[0]==L
for t in taus+[U-1]:
    for C in cohorts:
        pairs=list(itertools.combinations(C,2))
        assert all(abs(cs[296][i]-cs[296][j])>t for i,j in pairs)
        hard=any(all(abs(cs[k][i]-cs[k][j])<=t for k in range(214,296))
                 for i,j in pairs)
        assert hard,(t,C)
print('PASS_R5_HARD_SEXTET',len(cls),len(cohorts),len(taus),
      'f8',expected[8],'memoized',states[8])
