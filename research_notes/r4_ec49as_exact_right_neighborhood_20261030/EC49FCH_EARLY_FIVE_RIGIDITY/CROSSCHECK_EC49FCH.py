"""Independent tuple-set checker for selected five-slot replacement problems.
Uses literal signed primitive tuple prefixes; no shared prefix bit-index or bitwise union.
"""
from itertools import combinations
from pathlib import Path
HERE=Path(__file__).resolve().parent
import sys
sibling=HERE.parent/'EC49FCF_EARLY1_LATE3_150'
if sibling.exists():sys.path.insert(0,str(sibling))
from frozen_model import W,STEPS,REQ,observe,candidates
from VERIFY_EC49FCH import BASELINE
import json

def prefixes(word):
    path=[]
    for op in word:path.extend(STEPS[op])
    return frozenset(tuple(path[:j]) for j in range(1,len(path)+1))

chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
base={key:prefixes(word) for key,word in chosen.items()}
assert len(frozenset().union(*base.values()))==BASELINE
pools={f'{h}:{sig}':words for h in range(4,10) for sig,words in candidates(h).items()}
reports=[]
for fam,selected in [
    ('early_five',[0,1,42,125,251]),
    ('early4_h7',[0,1,80,240,320,480,639,839]),
]:
    source = json.load(open(HERE/f'EC49FCH_{fam}_0_{252 if fam=="early_five" else 160}.json')) if fam=='early_five' else None
    for ix in selected:
        if fam=='early_five': row=source['rows'][ix]
        else:
            start=(ix//160)*160 if ix<640 else 640
            stop=start+160 if start<640 else 840
            src=json.load(open(HERE/f'EC49FCH_early4_h7_{start}_{stop}.json'))
            row=src['rows'][ix-start]
        slots=row['slots']; f=frozenset().union(*(v for k,v in base.items() if k not in slots))
        limit=BASELINE-len(f)
        ps=[]
        for key in slots:
            remaining=frozenset(prefixes(w)-f for w in pools[key])
            ps.append([v for v in remaining if len(v)<limit])
        ps.sort(key=len)
        states={frozenset()}
        for options in ps:
            states={s|v for s in states for v in options if len(s|v)<limit}
            if not states:break
        found=BASELINE if not states else min(BASELINE,min(len(f|v) for v in states))
        assert found==row['minimum']==BASELINE,(fam,ix,found,row)
        reports.append({'family':fam,'row_index':ix,'slots':slots,'result':found,'fixed_edges':len(f)})
print('PASS independent signed-native tuple five-slot verification groups',len(reports))
with open(HERE/'INDEPENDENT_CROSSCHECK_EC49FCH.json','w') as h:json.dump({'independent_representatives':reports},h,indent=2)
