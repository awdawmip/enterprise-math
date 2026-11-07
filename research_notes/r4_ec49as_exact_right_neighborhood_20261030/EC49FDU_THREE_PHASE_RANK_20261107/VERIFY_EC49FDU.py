#!/usr/bin/env python3
"""Verify published per-triple schedules against the exact observer masks."""
import json,runpy
from itertools import combinations
from pathlib import Path
src=runpy.run_path(str(Path(__file__).with_name('EC49FDU_THREE_PHASE_RANK.py')))
rows=json.loads(Path(__file__).with_name('EC49FDU_THREE_PHASE_RANK_CERTIFICATE.json').read_text())
assert len(rows)==6734 and len({tuple(map(tuple,r['keys'])) for r in rows})==6734
ok=0;exception=0
for item in rows:
    t=[tuple(k) for k in item['keys']]
    for h,keychoice in zip(range(4,10),item['schedule']):
        choices=keychoice if isinstance(keychoice,list) else [keychoice]
        m=0
        for j in choices:m|=src['horizon'][h].get(t[j],0)
        assert src['rank9'](m),(t,h,choices,m)
    assert all(not all(src['rank9'](src['horizon'][h].get(a,0)|src['horizon'][h].get(b,0)) for h in range(4,10)) for a,b in combinations(t,2))
    if any(isinstance(v,list) for v in item['schedule']):
        assert item['schedule']==[[0,1],[2],[2],[2],[2],[2]];exception+=1
    else:
        idx=item['schedule']; assert len(set(idx))==3
        changes=sum(idx[i]!=idx[i-1] for i in range(1,6))
        assert changes==2;ok+=1
assert (ok,exception)==(6730,4)
print('VERIFY_EC49FDU: PASS 6734 independent schedule checks; 6730 contiguous 3-key schedules; 4 H4-pair exceptions')
