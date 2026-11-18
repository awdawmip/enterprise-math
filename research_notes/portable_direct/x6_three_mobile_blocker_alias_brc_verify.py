#!/usr/bin/env python3
"""Exact X6 three-mobile blocker-alias Boolean BRC witness.
Every labelled source triad has one permitted +e0 Port; branch-word labels and
all six signed coordinate components are retained. Conditional vacancy model.
"""
from itertools import product
import json
DIM=6
def pt(x=0,y=0,z=0):return (x,y,z,0,0,0)
def move(p):return (p[0]+1,)+p[1:]
def example_positions(bits):
    positions=[]
    for j,bit in enumerate(bits):
        positions.extend((pt(0,0,4*j),pt(0,1,4*j),pt(-1,bit,4*j)))
    assert len(set(positions))==len(positions)
    return tuple(positions)
def labelled_words(positions,h):
    branches={((),positions)}
    support={()}
    for _ in range(h):
        nxt=set()
        for word,state in branches:
            occupied=set(state)
            for s,pos in enumerate(state):
                target=move(pos)
                if target in occupied:continue
                new=list(state);new[s]=target
                w=word+((s,0),)
                support.add(w)
                nxt.add((w,tuple(new)))
        branches=nxt
    return frozenset(support)
def pair_sigma_1(u,v):
    d=tuple(b-a for a,b in zip(u,v))
    if any(d[i]!=0 for i in range(1,6)):return 'FAR'
    if abs(d[0])>1:return 'FAR'
    return d
def pair_signature(positions):
    return tuple(pair_sigma_1(positions[i],positions[j])
        for i in range(len(positions)) for j in range(i+1,len(positions)))
def run():
    family=[]
    for m in range(1,6):
        L1=set();L2=set();pairs=set()
        for bits in product(range(2),repeat=m):
            state=example_positions(bits)
            a=labelled_words(state,1)
            b=labelled_words(state,2)
            sig=pair_signature(state)
            expected={()}|{((s,0),) for j in range(m)
                          for s in (3*j,3*j+1)}
            assert a==expected,(m,bits,'one-step')
            for j,bit in enumerate(bits):
                witness=((3*j,0),(3*j+2,0))
                assert (witness in b)==(bit==0),(m,bits,j)
            L1.add(a);L2.add(b);pairs.add(sig)
        assert len(L1)==1 and len(L2)==len(pairs)==2**m
        family.append({'blocks':m,'sources':3*m,'configurations':2**m,
          'distinct_L1_languages':1,'distinct_L2_languages':2**m,
          'distinct_pairwise_sigma_1':2**m,
          'minimal_bits_h1':0,'minimal_bits_h2':m})
    pts=[pt(x,y) for x in range(-2,3) for y in range(-1,2)]
    sample=pt(0,0)
    by_signature={};by_language={};count=0
    for b in pts:
        for c in pts:
            if b==sample or c==sample or b==c:continue
            st=(sample,b,c)
            L=labelled_words(st,1)
            sig=pair_signature(st)
            if sig in by_signature:assert by_signature[sig]==L
            else:by_signature[sig]=L
            by_language.setdefault(L,set()).add(sig)
            count+=1
    aliases=sum(len(sigs)>1 for sigs in by_language.values())
    assert aliases>0
    return {'schema':'X6_THREE_MOBILE_BLOCKER_ALIAS_BRC_EXACT_V1',
      'status':'PASS','spatial_dimensions':DIM,
      'tested_labeled_sources_per_block':3,'positive_port_axis':0,
      'example_other_coordinate_axes':[1,2],
      'exhaustive_3_source_configurations':count,
      'exhaustive_distinct_L1_languages':len(by_language),
      'exhaustive_distinct_pairwise_signatures':len(by_signature),
      'exhaustive_language_classes_with_multiple_pair_signatures':aliases,
      'independent_block_family':family}
if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True,ensure_ascii=False))
