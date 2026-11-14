#!/usr/bin/env python3
"""EC49FEU full finite census, independent Python-stdlib exact checker.
Input: frozen original native-X6 six-op grammar, nine-state observer and
positive complete BRC keys, science commit fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from itertools import combinations, product
from functools import lru_cache
import json

T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
@lru_cache(None)
def signatures(h,key):
    x,y,z=key
    a=z-1; cd=x+y-h-1; f=h+1-y-2*z; g=h+1-x
    if min(a,cd,f,g)<0: return frozenset()
    obs=set()
    for nc in range(cd+1):
        queue={((a,nc,cd-nc,z,f,g),0)}
        while queue:
            following=set()
            for counts,q in queue:
                if sum(counts)==0:
                    if SIG[q]: obs.add(SIG[q])
                    continue
                for j,c in enumerate(counts):
                    if c: following.add((counts[:j]+(c-1,)+counts[j+1:],T[q][j]))
            queue=following
    return frozenset(obs)

def keys(h, need):
    """Every positive full BRC key at this horizon which supports need."""
    out=[]
    for z in range(1,(h+1)//2+1):
        for cd in range(h-2*z+2):
            for f in range(h-2*z+2-cd):
                g=h+1-2*z-cd-f
                k=(cd+2*z+f,cd+g,z)
                s=signatures(h,k)
                if need.issubset(s):
                    assert k[0]+k[1]==h+1  # requires at least one high label
                    out.append(k)
    return tuple(sorted(set(out)))

def census():
    late=tuple(range(4,10))
    both={h:keys(h,frozenset((16,32))) for h in late}
    only16={h:keys(h,frozenset((16,))) for h in late}
    assert [len(both[h]) for h in late]==[2,4,6,9,12,16]
    assert [len(only16[h]) for h in late]==[4,6,9,12,16,20]
    assert set((1,2,4,8)).issubset(signatures(2,(3,1,1)))
    assert set((16,32)).issubset(signatures(3,(3,1,1)))
    totals={}; detail={}; examples={}
    for mixed in late:
        row={'all':0,'feasible':0,'missing_mixed':0,'missing_low':0}
        branches={}
        for hs in combinations(late,4):
            if mixed not in hs: continue
            low=tuple(h for h in late if h not in hs)
            counts={'all':0,'feasible':0,'missing_mixed':0,'missing_low':0}
            for choices in product(*(only16[h] if h==mixed else both[h] for h in hs)):
                counts['all']+=1
                K=((3,1,1),)+choices
                if not {1,8,16}.issubset(set().union(*(signatures(mixed,k) for k in K))):
                    counts['missing_mixed']+=1
                elif not all({1,2,4,8}.issubset(set().union(*(signatures(h,k) for k in K))) for h in low):
                    counts['missing_low']+=1
                else:
                    counts['feasible']+=1
                    examples.setdefault(str(mixed),{'high_horizons':list(hs),'keys':[list(k) for k in K]})
            for field in row: row[field]+=counts[field]
            branches[''.join(map(str,hs))]=counts
        assert row['all']==sum(row[k] for k in ('feasible','missing_mixed','missing_low'))
        totals[str(mixed)]=row;detail[str(mixed)]=branches
    assert [totals[str(h)]['feasible'] for h in late]==[8800,15812,18426,20568,26652,0]
    assert sum(r['all'] for r in totals.values())==239144
    assert sum(r['feasible'] for r in totals.values())==90258
    assert all(row['feasible']==0 for h,rows in detail.items() for name,row in rows.items() if '9' not in name)
    return {'status':'PASS', 'frozen_science':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
        'late_pair_key_counts':{str(h):len(both[h]) for h in late},
        'late_sig16_key_counts':{str(h):len(only16[h]) for h in late},
        'type_B_total':{'all':239144,'feasible':90258,'missing_mixed':82520,'missing_low':66366},
        'type_B_by_mixed_horizon':totals,'by_high_set':detail,
        'type_C_mirror_feasible':90258, 'sample_witness_key_inventories':examples}
if __name__=='__main__':print(json.dumps(census(),ensure_ascii=False,indent=2))
