#!/usr/bin/env python3
"""Exact finite X6/BRC tests for Stage508; import pinned Stage507 BRC engine.
Run: PYTHONPATH=<directory containing REPRO_STAGE507B.py> python REPRO_STAGE508B_DELTA.py
Required immutable dependency: enterprise-math@7d53c1741c5bec29886b43d7d7d27c0e68ff6370
research_notes/n12_x6_native_brc_stage507b_rank_provenance_20261107_RESEARCH2/REPRO_STAGE507B.py
"""
from itertools import product
import json
import REPRO_STAGE507B as base


def exposure(tags,h,R,S):
    frontier={tuple((i,bool(p)) for i,p in enumerate(tags))}
    exposed=set();states=0
    for depth in range(h):
        nxt=set()
        for w in frontier:
            states+=1;n=len(w)
            def mark(j):
                if 0<=j<n and w[j][0]>=0: exposed.add(w[j][0])
            if n>=1:mark(n-1);nxt.add(w[:-1])
            if n>=3:mark(n-3);nxt.add(w[:n-3]+w[n-2:])
            if n>=2:
                if n>=3:mark(n-3)
                mark(n-2)
                nxt.add(w[:n-2]+((-depth-1,True),)+w[n-2:])
            for r in R:
                if r<n:mark(n-r-1);nxt.add(w)
            ids=[j for j in range(n-1,-1,-1) if w[j][1]]
            for k in S:
                if k<=len(ids):
                    j=ids[k-1];mark(j);nxt.add(w[:j]+w[j+1:])
        frontier=nxt
    return exposed,states


def pack(w,keep):
    z=[];i=0
    while i<len(w):
        if i in keep:
            z.append(('E',w[i][0],w[i][1]));i+=1
        else:
            j=i
            while j<len(w) and j not in keep:j+=1
            z.append(('G',base.fword([a for a,t in w[i:j]])))
            i=j
    return tuple(z)


counts={'roots':0,'prefix_nodes':0,'transitions':0,'mask_states':0,'strict_savings':0}

def check(w,h,R,S):
    keep,states=exposure([t for a,t in w],h,R,S)
    old=base.mask(len(w),h,R,S,w)
    assert keep<=old
    counts['roots']+=1;counts['mask_states']+=states
    counts['strict_savings']+=len(keep)<len(old)
    frontier=[(w,pack(w,keep))]
    for d in range(h+1):
        nxt=[]
        for raw,pieces in frontier:
            counts['prefix_nodes']+=1
            assert base.observe(raw)==base.fpieces(pieces)[:3]
            if d==h:continue
            for act in base.actions(R,S):
                counts['transitions']+=1
                a=base.raw_step(raw,act)
                b=base.piece_step(pieces,act)
                assert (a is None)==(b is None)
                if a is not None:
                    assert base.observe(a)==base.fpieces(b)[:3]
                    nxt.append((a,b))
        frontier=nxt
    return keep,old


def run():
    for h,limit,R,S in ((1,5,(2,5),(1,2)),(2,4,(2,4),(1,2))):
        for n in range(limit+1):
            for digits in product(range(6),repeat=n):
                w=tuple((base.DIRECTIONS[z//2],bool(z%2)) for z in digits)
                check(w,h,R,S)
    n,h,R,S=19,3,(2,11),(1,3)
    w=tuple(((3*i+i*i+7)%12,i in {0,3,6,12,15,18}) for i in range(n))
    kept,old=check(w,h,R,S)
    assert len(old)==15 and len(kept)==12
    all_dir_x=tuple(((9*i+i*i)%12, i in {0,20,24,26,27}) for i in range(28))
    all_dir_y=tuple((a,(i==1 or i in {20,24,26,27})) for i,(a,t) in enumerate(all_dir_x))
    x_mask,_=check(all_dir_x,2,(2,12),(1,2))
    y_mask,_=check(all_dir_y,2,(2,12),(1,2))
    assert all_dir_x!=all_dir_y and x_mask==y_mask
    assert pack(all_dir_x,x_mask)==pack(all_dir_y,y_mask)
    return {'stage':'508-B delta','status':'PASS','six_axes':6,'signed_directions':12,
            'full_directed_relations':144,'counts':counts,
            'witness':{'n':19,'h':3,'R':list(R),'S':list(S),
                       'stage507_keep':sorted(old),'stage508_keep':sorted(kept),
                       'explicit_saved':len(old)-len(kept)},
            'collision':{'n':28,'same_compressed':True,'extra_P_positions':[0,1]}}

if __name__=='__main__': print(json.dumps(run(),indent=2,sort_keys=True))
