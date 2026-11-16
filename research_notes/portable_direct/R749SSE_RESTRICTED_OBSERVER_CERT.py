#!/usr/bin/env python3
"""R749SSE exact finite collision and future-observer carrier certificate.
Frozen input: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Only standard-library exact integer/rational arithmetic.
"""
from fractions import Fraction
from itertools import product
from math import comb
import json

WEIGHTS=(1,1,2,3,6)
OFFSETS=(0,1,5)
PARTITIONS={'012':(0,0,0),'01|2':(0,0,1),'02|1':(0,1,0),
            '12|0':(1,0,0),'0|1|2':(0,1,2)}

def counts(limit):
    c=[0]*limit;t=[0]*limit;c[0]=1
    for j,w in enumerate(WEIGHTS):
        for v in range(w,limit):
            old=c[v-w];c[v]+=old
            t[v]+=t[v-w]+(old if j==0 else 0)
    C=[0]*(limit+1);T=[0]*(limit+1)
    for v in range(limit):
        C[v+1]=C[v]+c[v];T[v+1]=T[v]+t[v]
    return C,T

def residues(q):
    C=T=0
    for ts in product(*[range(6//w) for w in WEIGHTS]):
        weight=sum(w*x for w,x in zip(WEIGHTS,ts))
        L=(q-1-weight)//6
        if L<0:continue
        c=comb(L+5,5)
        C+=c;T+=(L+ts[0])*c
    return C,T

def collision(q,M,K,C,T):
    seen={}
    for d in range(-K,K+1):
        if C[q]+d<=0:continue
        for e in range(-M,M+1):
            x=Fraction(T[q]+e,C[q]+d)
            if x in seen:
                return {'first':seen[x],'second':[e,d],'ratio':str(x)}
            seen[x]=[e,d]
    return None

def restriction(p,S):
    return tuple(tuple(p[i]==p[j] for j in S) for i in S)

def run():
    C,T=counts(101)
    for q in range(1,101):
        assert (C[q],T[q])==residues(q),q
    witnesses={}
    for q in range(1,48):
        h=collision(q,2,2,C,T)
        if q<6:
            assert h is not None,q
            witnesses[str(q)]=h
        else:
            assert h is None,q
    assert (C[48],T[48])==(104712,883842)
    # Proof beyond finite enumeration: for all q>=48, residue block
    # L=floor((q-1-B)/6)>=5, B<=17; its mean marked count is L+t0>=5.
    # Therefore T_q>=5C_q>4(C_q+2) as C_q>=C_48>8.
    assert 5*C[48]>4*(C[48]+2)
    for q in range(48,101):
        assert T[q]>4*(C[q]+2),q
    classes={}
    for S in [(),(0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2)]:
        n=len({restriction(p,S) for p in PARTITIONS.values()})
        assert n=={0:1,1:1,2:2,3:5}[len(S)]
        classes[','.join(map(str,S)) or 'empty']={
            'one_positive_budget_error_type':n,
            'joint_positive_budget_types':n*n,
        }
    assert (C[11],T[11])==(281,600)
    assert Fraction(11**3,C[11])==Fraction(1331,281)
    return {
      'unit':'R749SSE','status':'PASS',
      'review':'AUTHOR_EXACT_NOT_REVIEWED',
      'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'weights':list(WEIGHTS),'marked_source':0,'offsets':list(OFFSETS),
      'numerator_budget_M':2,'denominator_budget_K':2,
      'sharp_coordinate_injectivity_threshold':6,
      'finite_collision_free_cutoffs':[6,47],
      'exact_residue_formula_checked':[1,100],
      'analytical_infinite_tail_starts':48,
      'C48':C[48],'T48':T[48],
      'early_collision_witnesses':witnesses,
      'joint_observer_class_counts':classes,
      'future_separator':{
          'base_cutoff':6,'numerator_partitions':['012','01|2'],
          'first_two_errors':[0,0],'third_error_difference':1,
          'denominator_errors':[0,0,0],
          'third_cutoff':11,'delta_third_Y':'1331/281',
      },
      'scope':'fixed-cutoff auxiliary source observer; not native BRC/X6 admission'
    }

if __name__=='__main__':
    result=run()
    with open('R749SSE_RESTRICTED_OBSERVER_RESULTS.json','w',encoding='utf8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
    print('PASS',result['sharp_coordinate_injectivity_threshold'],result['C48'])
