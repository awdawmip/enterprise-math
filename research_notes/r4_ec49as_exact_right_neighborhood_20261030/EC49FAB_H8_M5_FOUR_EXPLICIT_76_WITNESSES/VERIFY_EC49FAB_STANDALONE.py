#!/usr/bin/env python3
"""EC49FAB: self-contained exact witness verifier; Python 3 stdlib only.
All 6-axis steps and 9-history transfer signatures are rebuilt from operation words.
Modular rank 9 over F_101 certifies rational rank 9 for 0/1 matrices.
"""
import json
from collections import defaultdict

OPS = {'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
HISTORY = (('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS = ('N','A','B','AB','BA')
T4 = frozenset((1836687,1867942,1872656,1873981))
T2 = frozenset((1836425,1866380))
BASE = ('de','ed','ce','ec')

# Schedule rows: exy_lb, exs_lb, four collision horizons, five (u,v,w) keys.
# Explicit operation words are ordered by horizon h=2,...,8.
DATA = {
 1512: ('62 62 2 3 4 5 3 1 1 4 2 1 4 3 1 4 4 1 4 5 1',
        ('de ed ce ec','feg gef','defg edfg fegc gefc','fegfg geffg',
         'fegfgg geffgg','fegfggg geffggg','fegfgggg geffgggg')),
 1513: ('62 62 2 3 4 5 3 1 1 4 2 1 5 2 1 6 2 1 7 2 1',
        ('de ed ce ec','feg gef','defg edfg fegc gefc','fegfg geffg',
         'fegfgf geffgf','fegfgff geffgff','fegfgfff geffgfff')),
 2200: ('62 62 2 3 5 6 3 1 1 4 3 1 3 2 1 4 4 1 4 5 1',
        ('de ed ce ec','feg gef','fegg gefg','feggd gefgd feggc gefgc',
         'fegggf gefggf','fegggfg gefggfg','fegggfgg gefggfgg')),
 2203: ('62 62 2 3 5 6 3 1 1 5 2 1 4 1 1 6 2 1 7 2 1',
        ('de ed ce ec','feg gef','fegf geff','fegfd geffd fegfc geffc',
         'fegfgf geffgf','fegfgff geffgff','fegfgfff geffgfff')),
}

def primitive(word):
    assert set(word).issubset(set(OPS)-{'b'})
    return tuple(v for op in word for v in OPS[op])

def transfer_sig(path):
    n=0
    for i,(event,p) in enumerate(HISTORY):
        for s in path:
            if p==1 and s==2:
                if event=='N':event='A'
                elif event=='B':event='BA'
            elif p==2 and s==1:
                if event=='N':event='B'
                elif event=='A':event='AB'
            p=s
        n+=BUCKETS.index(event)*5**i
    return n

def rank_mod_101(rows):
    a=[list(x) for x in rows]
    r=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][col]%101),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][col],-1,101)
        a[r]=[(v*inv)%101 for v in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][col]%101:
                x=a[i][col]
                a[i]=[(v-x*w)%101 for v,w in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def check(rank,raw,by_h):
    x=list(map(int,raw.split()))
    assert len(x)==21
    a,b,c,d=x[2:6]
    keys=[tuple(x[6+3*i:9+3*i]) for i in range(5)]
    groups=[(a,b),(c,d)]+[(h,) for h in range(2,9) if h not in (a,b,c,d)]
    assert len(set(keys))==5
    hk={h:keys[i] for i,group in enumerate(groups) for h in group}
    assert set(hk)==set(range(2,9))
    all_sigs=set()
    union=set()
    costs={}
    for h,section in zip(range(2,9),by_h):
        declared=hk[h]
        target=T4 if declared[0]+declared[1]-h-1>=1 else T2
        seen=set()
        for word in section.split():
            assert len(word)==h
            st=primitive(word)
            assert all(1<=abs(step)<=3 for step in st)
            assert tuple(st.count(i) for i in range(1,7))==declared+(0,0,0)
            assert tuple(st.count(i)-st.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
            assert len(st)==2*(sum(declared)-1)
            s=transfer_sig(st)
            assert s in target and s not in seen
            seen.add(s);all_sigs.add(s)
            union.update(st[:i] for i in range(1,len(st)+1))
        assert seen==target,(rank,h,target,seen)
        signatures=sorted(seen)
        matrix=[[int((s//5**i)%5==b) for s in signatures for b in range(5)] for i in range(9)]
        assert rank_mod_101(matrix)==9,(rank,h)
        costs[h]=len(union)
    assert len(all_sigs)==6
    assert sum(len(section.split()) for section in by_h)==18
    base=set()
    for w in BASE:
        p=primitive(w)
        base.update(p[:i] for i in range(1,len(p)+1))
    assert len(base)==28 and base.issubset(union)
    assert costs[8]==76 and costs[2]==28
    return {'schedule_rank':rank,'status':'PASS','six_axis_complete_keys':5,
            'observer_signatures':6,'rational_observer_rank_each_h':9,
            'chosen_operation_words':18,'prefix_union_edges':76,
            'cumulative_edge_count':costs}

if __name__=='__main__':
    print(json.dumps({'proposition':'E_star<=76',
        'model':'frozen signed native X6 BRC H2..H8 five keys six signatures',
        'verification':'integer primitive-step expansion, signed balance, nine-history transfer, mod-101 rank, exact prefix sets',
        'cases':[check(k,*v) for k,v in DATA.items()]},sort_keys=True,indent=2))