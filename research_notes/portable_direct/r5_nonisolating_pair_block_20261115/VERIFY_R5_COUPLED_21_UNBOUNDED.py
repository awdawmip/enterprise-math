#!/usr/bin/env python3
"""Exact finite checks supporting an all-m (2,1)-coupled R5 theorem.
Check every binomial indexed-center set for m=1..6; no floating point.
"""
from itertools import combinations, product
import json

BASE = (3,2,2,3)

def positions(gaps,mask):
    d=list(gaps)
    if mask&1: d[0]-=1
    if mask&2: d[3]-=1
    x=[0]
    for a in d: x.append(x[-1]+a)
    return x

def optimal(gaps,mask,k):
    x=positions(gaps,mask)
    best=None; F=set()
    for s in combinations(range(len(x)),k):
        ds=[min(abs(x[i]-x[j]) for j in s) for i in range(len(x))]
        if max(ds)>2: continue
        cost=sum(ds)
        if best is None or cost<best: best=cost; F={s}
        elif cost==best: F.add(s)
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
    prefix_barriers=[]
    for mask in range(4):
        x=positions(BASE+(2,1),mask)
        vals=[]
        for q in range(1,6):
            best=None
            for external_idx5 in (False,True):
                for B in combinations(range(5),q):
                    centers=B+((5,) if external_idx5 else ())
                    d=[min(abs(x[i]-x[j]) for j in centers)
                       for i in range(5)]
                    if max(d)>2: continue
                    z=sum(d)
                    if best is None or z<best: best=z
            vals.append(best)
        assert vals==[None,6,4,2,0],(mask,vals)
        prefix_barriers.append(vals)

    core=[optimal(BASE+(2,1),mask,4) for mask in range(4)]
    core_fams=[f for _,f in core]
    assert [cost for cost,_ in core]==[5]*4
    assert list(map(len,core_fams))==[5,12,9,17]
    assert (core_fams[1]&core_fams[2])-core_fams[0]==set()
    assert core_fams[3]-core_fams[1]-core_fams[2]=={(1,2,3,6)}
    assert all_arcs(core_fams[3])==all_arcs(core_fams[1])|all_arcs(core_fams[2])

    rows=[]
    for m in range(1,7):
        gaps=BASE+(2,1)*m
        n,k=5+2*m,3+m
        actual=[optimal(gaps,mask,k) for mask in range(4)]
        suffix={tuple(5+2*j+e for j,e in enumerate(bits,start=1))
                for bits in product((0,1),repeat=m-1)}
        expected=[{s+t for s in core_fams[mask] for t in suffix}
                  for mask in range(4)]
        fam=[f for _,f in actual]
        assert [cost for cost,_ in actual]==[m+4]*4
        assert fam==expected,('optimizer-product',m)
        f0,fa,fb,fab=fam
        p=(fa&fb)-f0
        q=fab-fa-fb
        assert not p
        assert q=={(1,2,3,6)+t for t in suffix}
        assert all_arcs(fab)==all_arcs(fa)|all_arcs(fb)
        assert list(map(len,fam))==[5*2**(m-1),12*2**(m-1),
                                   9*2**(m-1),17*2**(m-1)]
        rows.append({'m':m,'n':n,'K':k,'J':m+4,
            'optimizer_counts':list(map(len,fam)),
            'P_count':len(p),'Q_count':len(q),
            'neutral_arcs':len(all_arcs(fab)-all_arcs(fa)-all_arcs(fb))})
    return {'status':'PASS_R5_UNBOUNDED_COUPLED_21_BLOCKS',
        'frozen_science_input':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'finite_coverage':'all indexed-center choices for m=1..6, 4 masks',
        'prefix_cost_lower_bounds_q1_to_q5':prefix_barriers,
        'core_7event_optimizer_counts':list(map(len,core_fams)),
        'rows':rows,
        'proof':'COUPLED_21_UNBOUNDED_SWITCH_THEOREM.md',
        'independent_review':'NOT_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
