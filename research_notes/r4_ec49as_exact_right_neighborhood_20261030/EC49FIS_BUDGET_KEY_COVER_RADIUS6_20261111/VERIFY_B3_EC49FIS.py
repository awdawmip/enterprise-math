#!/usr/bin/env python3
"""Complete legal six-word enumeration for twelve B=3 key-reallocation cases."""
import collections as C
import itertools as I
import json
from pathlib import Path
from EC49FGW_RADIUS5_SCREEN import W,raw_key,pref,validate_profile,all_words
FIS=json.loads(Path('EXACT_REPORT_EC49FIS.json').read_text())
words=C.defaultdict(list)
for label,w in all_words(): words[label].append((raw_key(w),frozenset(pref(w)),w))
reports=[]
for profile,data in zip(W['profiles'],FIS['profiles']):
    assert profile['profile_id']==data['profile']
    rows,ps=validate_profile(profile)
    cases=[]
    for Q,B,*rest in data['unresolved_210']:
        if B!=3: continue
        fixed_prefixes=set().union(*(ps[i] for i in range(24) if i not in Q))
        fixed_keys={raw_key(rows[i]['word']) for i in range(24) if i not in Q}
        options=[]
        for i in Q:
            lab=(rows[i]['window'],rows[i]['signature'])
            options.append([(k,p-fixed_prefixes,w) for k,p,w in words[lab]
                            if len(p-fixed_prefixes)<=3])
        count=0;best=1000;passing=0
        for selected in I.product(*options):
            count+=1
            if len(fixed_keys|{k for k,d,w in selected})>7: continue
            cost=len(set().union(*(d for k,d,w in selected)))
            if cost<best:best=cost
            if cost<=3:passing+=1
        assert passing==0 and best==4, (profile['profile_id'],Q,passing,best)
        cases.append(dict(Q=Q,B=B,options=[len(x) for x in options],examined=count,
                          exact_min_added_prefixes=4))
    assert len(cases)==6
    reports.append(dict(profile=profile['profile_id'],cases=cases))
Path('B3_FULL_EXACT_REPORT.json').write_text(json.dumps(dict(
    schema='EC49FIS_B3_FULL_SIXPATH_V1',profiles=reports),indent=2)+'\n')
print('EC49FIS_B3_FULL_ENUM_PASS',sum(len(r['cases']) for r in reports))
