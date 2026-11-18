"""Independent primitive signed-integer tuple-prefix audit of all EC49FCA groups."""
from pathlib import Path
from itertools import combinations
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'EC49FBY_COMPLETE_TRIPLE_RIGIDITY'))
from VERIFY_EC49FBY import W,STEPS,REQ,observe,candidates

def pref(w):
    trace=[]
    for op in w:trace.extend(STEPS[op])
    return frozenset(tuple(trace[:j]) for j in range(1,len(trace)+1))
def run():
    chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
    early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
    late=[f'{h}:{s}' for h in (7,8,9) for s in REQ[h]]
    pools={f'{h}:{s}':ws for h in range(4,10) for s,ws in candidates(h).items()}
    ps={w:pref(w) for w in set(chosen.values())|{w for pool in pools.values() for w in pool}}
    assert len(set().union(*(ps[w] for w in chosen.values())))==158
    groups=[];evaluations=0
    for E in combinations(early,3):
        for L in late:
            slots=E+(L,)
            R=set().union(*(ps[w] for k,w in chosen.items() if k not in slots))
            K=158-len(R)
            arrays=[]
            for key in slots:
                arrays.append((key,tuple({ps[w]-R for w in pools[key] if len(ps[w]-R)<K})))
            arrays.sort(key=lambda pair:len(pair[1]))
            a,b,c,d=(arr for _,arr in arrays)
            checked=0;minimum=158
            for x in a:
                for y in b:
                    xy=x|y
                    if len(xy)>=K:continue
                    for z in c:
                        xyz=xy|z
                        if len(xyz)>=K:continue
                        for w in d:
                            checked+=1
                            minimum=min(minimum,len(R)+len(xyz|w))
            groups.append({'slots':slots,'fourth_evaluations':checked,'minimum':minimum})
            evaluations+=checked
    assert len(groups)==1200 and evaluations==1306868 and all(x['minimum']==158 for x in groups)
    print('PASS DIRECT EC49FCA',len(groups),'groups',evaluations,'fourth unions')
    return groups
if __name__=='__main__':run()
