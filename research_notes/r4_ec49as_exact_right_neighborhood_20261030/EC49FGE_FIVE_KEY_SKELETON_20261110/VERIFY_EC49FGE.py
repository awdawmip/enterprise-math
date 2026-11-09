#!/usr/bin/env python3
"""Exact five-raw-cache-key classification and 112 native-edge witness.
Frozen model: EC49FCZ/frozen_model.py Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859.
"""
from collections import defaultdict, Counter
from fractions import Fraction
import json

OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
S={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
   'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
NEED={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
      6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
BUCKET={1:(2,3,2,3,3,2,4,3,4),2:(2,2,2,3,3,2,2,3,4),
        4:(1,1,4,1,3,4,4,3,4),8:(1,1,1,1,1,4,4,3,4),
        16:(0,0,2,1,3,2,2,3,4),32:(0,1,0,1,1,2,4,3,4)}
W={
 2:{16:'fe',32:'ge'},
 3:{16:'feg',32:'gef'},
 4:{1:'gefd',2:'fegd',4:'fegc',8:'gefc'},
 5:{16:'feggf',32:'geffg'},
 6:{1:'gefddd',2:'fegddd',4:'fegccc',8:'gefccc'},
 7:{1:'gefddgf',2:'fegddgf',4:'fegccfg',8:'gefccfg'},
 8:{1:'geffgfgd',2:'feggfgfd',4:'feggfgfc',8:'geffgfgc'},
 9:{16:'feggfgffg',32:'geffgfggf'}
}

def exact_rank(rows):
    A=[list(map(Fraction,row)) for row in rows]
    rank=0
    for col in range(len(A[0])):
        pivot=next((i for i in range(rank,len(A)) if A[i][col]),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank]
        divisor=A[rank][col]
        for j in range(col,len(A[rank])):A[rank][j]/=divisor
        for i in range(rank+1,len(A)):
            if A[i][col]:
                factor=A[i][col]
                for j in range(col,len(A[i])):A[i][j]-=factor*A[rank][j]
        rank+=1
        if rank==len(A):break
    return rank

def support():
    # DFA state q and operation counts (e,a,c+d,f,g): exact quotient
    cur={(0,0,0,0,0,0)}
    covered=defaultdict(set);state_counts={}
    for h in range(1,10):
        nxt=set()
        for q,e,a,b,f,g in cur:
            for j,op in enumerate(OPS):
                nxt.add((T[q][j],e+(op=='e'),a+(op=='a'),
                         b+(op in ('c','d')),f+(op=='f'),g+(op=='g')))
        cur=nxt;state_counts[h]=len(cur)
        if h in NEED:
            for q,e,a,b,f,g in cur:
                if e==a+1 and SIG[q] in NEED[h]:
                    covered[(2*e+b+f,b+g,e)].add((h,SIG[q]))
    def all_signature_keys(h):
        return {k for k,labels in covered.items()
                if all((h,s) in labels for s in NEED[h])}
    assert {k for k,rs in covered.items() if (2,16) in rs}=={(3,0,1)}
    assert {k for k,rs in covered.items() if (2,32) in rs}=={(2,1,1)}
    assert {k for k,rs in covered.items()
            if (3,16) in rs and (3,32) in rs}=={(3,1,1)}
    early=all_signature_keys(4)&all_signature_keys(5)
    late=all_signature_keys(6)&all_signature_keys(7)&all_signature_keys(8)&all_signature_keys(9)
    assert early=={(3,3,1),(4,2,1),(5,1,1),(5,1,2)}
    assert late=={(5,5,1),(6,4,1),(7,3,1),(7,3,2)}
    forced={(3,0,1),(2,1,1),(3,1,1)}
    assert all(early.isdisjoint(all_signature_keys(h)) for h in (6,7,8,9))
    assert forced.isdisjoint(early|late) and early.isdisjoint(late)
    for ke in early:
        for h in (4,5):assert all((h,s) in covered[ke] for s in NEED[h])
    for kl in late:
        for h in (6,7,8,9):assert all((h,s) in covered[kl] for s in NEED[h])
    return state_counts,covered,forced,early,late

def witness():
    P=set();keys=set();counts={}
    for h in sorted(W):
        assert set(W[h])==set(NEED[h])
        for sig,w in W[h].items():
            assert len(w)==h and Counter(w)['e']==Counter(w)['a']+1
            q=0
            for op in w:
                q=T[q][OPS.index(op)];assert q!=8
            assert SIG[q]==sig,(h,sig,w)
            path=tuple(i for op in w for i in S[op])
            assert tuple(path.count(i)-path.count(-i) for i in (1,2,3))==(2,0,0)
            keys.add(tuple(path.count(i) for i in (1,2,3)))
            P.update(path[:j] for j in range(1,len(path)+1))
        rows=[[int(BUCKET[s][i]==j)
               for s in sorted(NEED[h]) for j in range(5)] for i in range(9)]
        assert exact_rank(rows)==9
        counts[h]=len(P)
    assert keys=={(3,0,1),(2,1,1),(3,1,1),(4,2,1),(6,4,1)}
    assert len(P)==112,len(P)
    return {'edges':len(P),'raw_keys':[list(k) for k in sorted(keys)],
            'strictly_positive_keys':sum(min(k)>0 for k in keys),
            'cumulative_prefix_edges':counts,'words':W}

if __name__=='__main__':
    states,covered,forced,early,late=support()
    result={'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
      'state_counts':states,'eligible_key_count':len(covered),
      'min_raw_key_count':5,'five_key_classes':len(early)*len(late),
      'forced':[list(k) for k in sorted(forced)],
      'H4_H5_choices':[list(k) for k in sorted(early)],
      'H6_H9_choices':[list(k) for k in sorted(late)],
      'witness':witness()}
    with open('EXACT_REPORT_EC49FGE.json','w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    print('EXACT_16_CLASS_PASS',states,'witness',result['witness']['edges'],
          'edges keys',len(result['witness']['raw_keys']))
