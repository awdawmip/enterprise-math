#!/usr/bin/env python3
"""Recalculate four complete 24-path native X6 systems from the EC49FAV
112-edge witness by replacing only the H3 pair. Never claim optimality here.
"""
import json
from EC49FDS_seedpairs import key,steps,pref
from EC49FDS_independent_fraction_audit import rank
SEED2=['fe','ge']
REST={4:['fegc','fegd','gefc','gefd'],
      5:['feggf','gefgf'],
      6:['fegccc','fegddd','gefccc','gefddd'],
      7:['fegccfg','fegddgf','gefccfg','gefddgf'],
      8:['feggfgfc','feggfgfd','gefgfgfc','gefgfgfd'],
      9:['feggfgfgf','gefgfgfgf']}
alt=[['feg','gef'],['feg','gfe'],['fge','gef'],['fge','gfe']]
res=[]
for h3 in alt:
    ws={2:SEED2,3:h3,**REST}
    unique=set(w for a in ws.values() for w in a)
    assert sum(map(len,ws.values()))==24 and len(unique)==24
    for h,wordlist in ws.items():
        assert all(len(w)==h for w in wordlist)
        assert rank(wordlist)==9
        assert all(tuple(steps(w).count(v)-steps(w).count(-v) for v in (1,2,3))==(2,0,0) for w in wordlist)
    keys=sorted({key(w) for w in unique})
    assert len(keys)==5
    p=set();history=[]
    for h in sorted(ws):
        p.update(*(pref(w) for w in ws[h]))
        history.append(len(p))
    res.append({'H3':h3,'native_prefix_edges':len(p),'cumulative_edges_h2_to_h9':history,'full_BRC_keys':[list(k) for k in keys],'all_horizon_fraction_rank9':True,'total_words':24})
print(json.dumps({'scope':'Four explicit full legal 24-path systems; fixed EC49FAV late H4-H9 words, fixed H2 fe/ge, varying admissible 3-key H3 variants; neither exhaustive nor optimal','pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','results':res},indent=2))
