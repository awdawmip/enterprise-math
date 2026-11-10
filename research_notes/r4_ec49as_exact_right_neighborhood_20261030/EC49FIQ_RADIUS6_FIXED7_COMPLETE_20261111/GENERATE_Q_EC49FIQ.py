#!/usr/bin/env python3
"""Enumerate exact retained-seven-key Q classes from frozen EC49FGW witness words.
Usage: python GENERATE_Q_EC49FIQ.py [B]
Output: exact hist; optionally QS_A_B.txt/QS_B_B.txt (6 label indices per row).
Frozen EC49FGW module and EC49FGJ witness JSON are sibling project files.
"""
from pathlib import Path
import sys,itertools,collections,json
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,PIN,raw_key,validate_profile
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
budget=int(sys.argv[1]) if len(sys.argv)>1 else None
expected={-1:6941,1:10824,3:9344,5:4400,7:6582,9:8700,10:2572,11:6284,12:2970,13:2498,14:1612,15:1425,16:396,17:1656,18:740,19:920,20:760,21:362,22:276,23:84,24:38,25:54,27:12,28:10,29:2}
out={}
for pr in W['profiles']:
    name=pr['profile_id'];rows,paths=validate_profile(pr)
    ps=collections.defaultdict(int);ks=collections.defaultdict(int)
    for i,(row,prefixes) in enumerate(zip(rows,paths)):
        ks[raw_key(row['word'])]|=1<<i
        for p in prefixes:ps[p]|=1<<i
    assert len(ps)==94 and len(ks)==7
    hist=collections.Counter(); qout=[]
    for q in itertools.combinations(range(24),6):
        m=sum(1<<i for i in q)
        if any((s&m)==s for s in ks.values()):continue
        b=sum((s&m)==s for s in ps.values())-1
        hist[b]+=1
        if budget==b:qout.append(q)
    assert dict(hist)==expected and sum(hist.values())==69462
    if budget is not None:
        (R/f'QS_{name}_{budget}.txt').write_text(''.join(' '.join(map(str,q))+'\n' for q in qout))
    out[name]=dict(sorted(hist.items()))
print(json.dumps({'frozen_pin':PIN,'retained_seven_key_budget_counts':out},sort_keys=True))
print('EC49FIQ_ENUMERATION_PASS')
