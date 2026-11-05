"""Native signed X6 integer-tuple prefix crosscheck of 15 EC49FCB groups."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'EC49FBY_COMPLETE_TRIPLE_RIGIDITY'))
from VERIFY_EC49FBY import W,STEPS,observe,candidates

def prefixes(w):
    seq=tuple(j for op in w for j in STEPS[op])
    return frozenset(seq[:i] for i in range(1,len(seq)+1))

def run():
    data=json.loads(Path(__file__).with_name('SPOTCHECK_EC49FCB.json').read_text())
    selected={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
    pools={f'{h}:{sig}':words for h in range(4,10) for sig,words in candidates(h).items()}
    P={w:prefixes(w) for w in set(selected.values())|{w for ws in pools.values() for w in ws}}
    assert len(set().union(*(P[w] for w in selected.values())))==158
    for row in data['rows']:
        slots=row['slots']
        fixed=frozenset().union(*(P[w] for k,w in selected.items() if k not in slots))
        k=158-len(fixed)
        arrays=[]
        for key in slots:
            a={P[w]-fixed for w in pools[key] if len(P[w]-fixed)<k}
            arrays.append(a)
        arrays.sort(key=len)
        a,b,c,d=arrays;checks=0;minimum=158
        for x in a:
            for y in b:
                xy=x|y
                if len(xy)>=k:continue
                for z in c:
                    xyz=xy|z
                    if len(xyz)>=k:continue
                    for w in d:
                        checks+=1;minimum=min(minimum,len(fixed|xyz|w))
        assert minimum==row['minimum'] and checks==row['fourth_evaluations'],row
    print('PASS tuple-prefix independent checks',len(data['rows']))
if __name__=='__main__':run()
