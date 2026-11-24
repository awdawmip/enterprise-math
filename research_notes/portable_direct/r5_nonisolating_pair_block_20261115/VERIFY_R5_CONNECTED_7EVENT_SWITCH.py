#!/usr/bin/env python3
"""Exhaust 560 exact center candidates for all four two-gap attachment words."""
from itertools import combinations
import json

def calc(gaps, mask, k=4):
    d=list(gaps)
    if mask&1: d[0]-=1
    if mask&2: d[3]-=1
    x=[0]
    for a in d: x.append(x[-1]+a)
    best=None; F=set()
    for s in combinations(range(len(x)), k):
        dist=[min(abs(x[i]-x[j]) for j in s) for i in range(len(x))]
        if max(dist)>2: continue
        z=sum(dist)
        if best is None or z<best: best=z; F={s}
        elif z==best: F.add(s)
    return best,F

def arcs(s):
    return {(0,-1,s[0]),(len(s),s[-1],-2)} | {
        (i+1,s[i],s[i+1]) for i in range(len(s)-1)
    }

def all_arcs(F):
    out=set()
    for s in F: out.update(arcs(s))
    return out

def run():
    rows=[]
    for u in (1,2):
        for v in (1,2):
            gaps=(3,2,2,3,u,v)
            res=[calc(gaps,mask) for mask in range(4)]
            costs=[c for c,_ in res]
            fam=[f for _,f in res]
            f0,fa,fb,fab=fam
            p=(fa&fb)-f0
            q=fab-fa-fb
            neutral=all_arcs(fab)-all_arcs(fa)-all_arcs(fb)
            rows.append({'gaps':list(gaps),'costs':costs,
                'family_sizes':list(map(len,fam)),
                'P_count':len(p),'Q_count':len(q),
                'Q':[list(s) for s in sorted(q)],
                'neutral_arc_count':len(neutral),
                'suffix_index_counts':[[sum(i in s for s in F)
                    for i in (5,6)] for F in fam]})
    target=next(r for r in rows if r['gaps'][-2:]==[2,1])
    assert target['costs']==[5,5,5,5]
    assert target['family_sizes']==[5,12,9,17]
    assert target['P_count']==0 and target['Q']==[[1,2,3,6]]
    assert target['neutral_arc_count']==0
    for counts, n in zip(target['suffix_index_counts'],target['family_sizes']):
        assert all(0<c<n for c in counts)
    assert [(r['gaps'][-2:],r['Q_count'],r['neutral_arc_count'])
            for r in rows]==[
        ([1,1],0,0),([1,2],0,0),([2,1],1,0),([2,2],2,2)]
    return {'status':'PASS_R5_CONNECTED_N7_SWITCH_ONLY_Q',
        'finite_domain':'u,v in {1,2}; 4 masks each; 35 index sets each; 560 total',
        'rows':rows, 'review':'NOT_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
