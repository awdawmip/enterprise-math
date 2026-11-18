#!/usr/bin/env python3
"""Independent 12,356-row signed-prefix clique census using computed q_i(d)."""
import collections,contextlib,io,itertools,json,runpy
from pathlib import Path
P=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):m=runpy.run_path(str(P/'VERIFY_EC49FAH_COMPACT.py'))
G=m['G'];C=m['CAP'];rows=m['rows'];hist=collections.Counter();first=[]
for ix,(raw,groups) in enumerate(rows):
    depth_max=max(G[k][1] for k in groups);score=0
    for d in range(1,depth_max+1):
        q=[G[g][0].get(d,0) for g in groups];best=0
        for cnt in range(1,6):
            for J in itertools.combinations(range(5),cnt):
                if all(C[groups[i],groups[j]]<d for i,j in itertools.combinations(J,2)):
                    best=max(best,sum(q[i] for i in J))
        score+=best
    hist[score]+=1
    if score==76 and len(first)<15:first.append(ix)
assert sum(hist.values())==12356 and min(hist)==76 and hist[76]==66
r={'id':'EC49FAH_INDEPENDENT_PAIRWISE_CENSUS','status':'PASS','schedule_rows':12356,'pairwise_min':min(hist),'exactly_76':hist[76],'strictly_lt76':0,'first_15_tight_schedule_rows':first,'histogram':dict(sorted(hist.items()))}
(P/'EC49FAH_INDEPENDENT_PAIRWISE_CENSUS_COMPACT.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k!='histogram'}))
