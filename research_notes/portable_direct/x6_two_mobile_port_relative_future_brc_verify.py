#!/usr/bin/env python3
"""Reproducible exact Boolean-BRC branch-support check: two mobile X6 triads.
Six signed relative coordinates; source-labelled positive unit Port moves.
This is conditional occupancy dynamics, not TRIADIC_CLOSURE_E admission.
"""
from itertools import product,combinations
from math import comb
import json
DIM=6
ZERO=(0,)*DIM
def bump(d,i,sign):
    out=list(d); out[i]+=sign
    return tuple(out)
def legal_words(d,IA,IB,h):
    assert len(d)==DIM and d!=ZERO
    branches={((),d)}
    output={()}
    for _ in range(h):
        nxt=set()
        for word,z in branches:
            for i in IA:
                dz=bump(z,i,-1)
                if dz!=ZERO:
                    w=word+(('A',i),)
                    nxt.add((w,dz));output.add(w)
            for i in IB:
                dz=bump(z,i,1)
                if dz!=ZERO:
                    w=word+(('B',i),)
                    nxt.add((w,dz));output.add(w)
        branches=nxt
    return frozenset(output)
def accessible(d,IA,IB):
    if d==ZERO: return False
    for i,v in enumerate(d):
        if i not in IA and i not in IB and v:return False
        if i not in IA and v>0:return False
        if i not in IB and v<0:return False
    return True
def classifier(d,IA,IB,h):
    return d if accessible(d,IA,IB) and sum(map(abs,d))<=h else 'INVISIBLE'
def collision_word(d,IA,IB):
    assert accessible(d,IA,IB)
    return tuple([('A',i) for i,v in enumerate(d) for _ in range(max(0,v))]+
                 [('B',i) for i,v in enumerate(d) for _ in range(max(0,-v))])
def first_illegal(word,d):
    z=d
    for k,(src,i) in enumerate(word,1):
        z=bump(z,i,-1 if src=='A' else 1)
        if z==ZERO:return k
    return None
def count_classes(IA,IB,h):
    s=len(set(IA)&set(IB))
    m=len(set(IA)|set(IB))
    def coeff(n):
        return sum(comb(s,j)*comb(n-j+m-1,m-1)
                   for j in range(min(s,n)+1))
    return 1+sum(coeff(n) for n in range(1,h+1))
def run():
    masks=[tuple(x) for n in range(1,4) for x in combinations(range(3),n)]
    states=[(x,y,z,0,0,0) for x,y,z in product(range(-3,4),repeat=3)
            if (x,y,z)!=(0,0,0)]
    states.append((0,0,0,1,0,0))
    out={'schema':'X6_TWO_MOBILE_PORT_BRC_EXACT_V1','status':'PASS',
         'source_state_dimension':6,'tested_port_axes':[0,1,2],
         'tested_mask_pairs':0,'tested_state_horizon_instances':0,
         'tested_language_class_equalities':0,
         'tested_transition_derivatives':0,'max_h':3}
    for IA in masks:
        for IB in masks:
            out['tested_mask_pairs']+=1
            for h in range(4):
                a={};b={}
                for d in states:
                    key=classifier(d,IA,IB,h)
                    words=legal_words(d,IA,IB,h)
                    if key in a:assert a[key]==words,('not-sufficient',IA,IB,h,d)
                    else:a[key]=words
                    if words in b:assert b[words]==key,('not-necessary',IA,IB,h,d)
                    else:b[words]=key
                    out['tested_state_horizon_instances']+=1
                    if key!='INVISIBLE':
                        witness=collision_word(d,IA,IB)
                        assert len(witness)<=h
                        assert first_illegal(witness,d)==len(witness)
                        assert witness not in words
                    if h:
                        for src,mask,sign in (('A',IA,-1),('B',IB,1)):
                            for i in mask:
                                next_d=bump(d,i,sign)
                                if next_d==ZERO:continue
                                suffix=legal_words(next_d,IA,IB,h-1)
                                derivative=frozenset(w[1:] for w in words
                                    if w and w[0]==(src,i))
                                assert derivative==suffix
                                if key=='INVISIBLE':
                                    assert classifier(next_d,IA,IB,h-1)=='INVISIBLE'
                                out['tested_transition_derivatives']+=1
                assert len(a)==len(b)==count_classes(IA,IB,h),(
                     IA,IB,h,len(a),count_classes(IA,IB,h))
                out['tested_language_class_equalities']+=len(a)
    out['visible_class_counts_full_three_axes']={
       str(h):count_classes((0,1,2),(0,1,2),h) for h in range(7)}
    cases=[
      ((2,-1,0,0,0,0),(0,1),(0,1),3),
      ((0,1,0,0,0,0),(0,),(1,),5),
      ((2,-3,0,0,0,0),(0,),(1,),5),
      ((0,0,0,1,0,0),(0,1,2),(0,1,2),9)]
    out['sample_witnesses']=[]
    for d,IA,IB,h in cases:
        key=classifier(d,IA,IB,h)
        out['sample_witnesses'].append({
          'd':list(d),'A_ports':list(IA),'B_ports':list(IB),'horizon':h,
          'class':'INVISIBLE' if key=='INVISIBLE' else 'VISIBLE',
          'first_collision_step':sum(map(abs,d)) if accessible(d,IA,IB) else None,
          'language_prefix_count_through_min_h5':
             len(legal_words(d,IA,IB,min(h,5)))})
    return out
if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False,sort_keys=True))
