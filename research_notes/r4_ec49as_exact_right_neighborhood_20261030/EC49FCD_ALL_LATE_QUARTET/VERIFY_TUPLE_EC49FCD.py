"""Independent signed-integer tuple prefix crosscheck, five EC49FCD slot sets."""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'EC49FBY_COMPLETE_TRIPLE_RIGIDITY'))
from VERIFY_EC49FBY import W,STEPS,observe,candidates
HERE=Path(__file__).resolve().parent
SELECTED=[
 ('7:1','7:2','7:4','7:8'),
 ('7:1','7:2','7:4','9:16'),
 ('7:1','7:2','8:1','8:4'),
 ('7:1','7:2','8:1','9:16'),
 ('8:4','8:8','9:16','9:32')]

def prefixes(word):
    seq=tuple(step for op in word for step in STEPS[op])
    return frozenset(seq[:k] for k in range(1,len(seq)+1))

def run():
    chosen={f'{h}:{observe(word)}':word for h,words in W.items() for word in words}
    pools={f'{h}:{sig}':words for h in range(4,10) for sig,words in candidates(h).items()}
    relevant={word for slots in SELECTED for slot in slots for word in pools[slot]}
    relevant.update(chosen.values())
    pref={word:prefixes(word) for word in relevant}
    assert len(frozenset().union(*(pref[word] for word in chosen.values())))==158
    rows=[]
    for slots in SELECTED:
        fixed=frozenset().union(*(pref[word] for key,word in chosen.items() if key not in slots))
        limit=158-len(fixed)
        arrays=[{pref[word]-fixed for word in pools[slot]
                 if len(pref[word]-fixed)<limit} for slot in slots]
        arrays.sort(key=len)
        a,b,c,d=arrays
        best=158;checks=0
        for x in a:
            for y in b:
                xy=x|y
                if len(xy)>=limit:continue
                for z in c:
                    xyz=xy|z
                    if len(xyz)>=limit:continue
                    for w in d:
                        checks+=1
                        best=min(best,len(fixed|xyz|w))
        assert best==158
        rows.append({'slots':list(slots),'base':len(fixed),
                     'fourth_checks':checks,'minimum':best})
    (HERE/'EC49FCD_TUPLE_CHECK.json').write_text(json.dumps(rows,indent=2)+'\n')
    print('PASS signed primitive tuple representation',len(rows))
if __name__=='__main__':run()
