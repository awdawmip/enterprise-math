#!/usr/bin/env python3
"""EC49FFM exact all-h native BRC lower-bound lemma audit.
Frozen input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Original BRC op/DFA source: EC49FFJ BRC_ORIGINAL_MODEL_EC49FFJ.py,
Git blob 6350340fbe869f17b5a50bd1ba30640db44a3a99.
"""
from itertools import product
from collections import defaultdict
import json

ORDER='acdefg'
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0)
LOW={1,2,4,8}

def native(w):return tuple(v for o in w for v in OPS[o])
def observe(w,q=0):
    for o in w:q=T[q][ORDER.index(o)]
    return S[q]

def reachable(q):
    v={q}
    while True:
        w=v|{T[s][i] for s in v for i in range(6)}
        if w==v:return v
        v=w

def keys(h):
    for z in range(1,(h+1)//2+1):
        for x in range(2*z,h+2):
            for y in range(h+2-2*z):
                if x+y>=h+2 and h+1-x>=0 and h+1-y-2*z>=0:
                    yield x,y,z

def candidates(h,key):
    x,y,z=key
    a=z-1;cd=x+y-h-1;f=h+1-y-2*z;g=h+1-x
    for c in range(cd+1):
        ct=[a,c,cd-c,z,f,g]
        def dfs(w,q):
            if not any(ct):
                yield w,S[q];return
            for i in range(6):
                if ct[i]:
                    ct[i]-=1
                    yield from dfs(w+ORDER[i],T[q][i])
                    ct[i]+=1
        yield from dfs('',0)

def verify():
    assert len({OPS[o][:2] for o in ORDER})==6
    reach={o:{S[s] for s in reachable(T[0][i])}&LOW for i,o in enumerate(ORDER)}
    sig4={OPS[o][0] for o in ORDER if 4 in reach[o]}
    sig1={OPS[o][0] for o in ORDER if 1 in reach[o]}
    assert sig4=={1} and sig1=={2}
    assert all(T[q][ORDER.index(o)]==q for q in range(1,9) for o in 'afg')
    tails=['c','d','e']+[a+b for a,b in product('afg',repeat=2)]
    for q in range(9):
        groups=defaultdict(set)
        for w in tails:
            v=observe(w,q)
            if v in LOW:groups[native(w)[0]].add(v)
        assert all(len(v)<=1 for v in groups.values()),(q,groups)
    exhaustive=[]
    for h in range(2,10):
        count=0;key_count=0
        for key in keys(h):
            key_count+=1;seen={};L=2*(sum(key)-1)
            for w,sig in candidates(h,key):
                if sig not in LOW:continue
                n=native(w)
                assert len(n)==L
                old=seen.setdefault(n[:-3],sig)
                assert old==sig,(h,key,w,sig,old)
                count+=1
        exhaustive.append([h,key_count,count])
    assert [row[2] for row in exhaustive]==[4,30,176,950,4932,25060,125680,625050]
    constructed=0
    for h in list(range(4,22))+[25,31,32,33,63,64,65,100,128,200]:
        for x in {4,h,(h+4)//2}:
            if not 4<=x<=h:continue
            r=x-3;s=h+1-x
            words=['f'*r+'e'+'g'*s+'c','f'*r+'e'+'g'*s+'d',
                   'g'+'f'*r+'e'+'g'*(s-1)+'c','g'+'f'*r+'e'+'g'*(s-1)+'d']
            assert [observe(w) for w in words]==[4,2,8,1]
            assert all(len(w)==h and len(native(w))==2*h+4 for w in words)
            prefixes={native(w)[:i] for w in words for i in range(1,2*h+5)}
            assert len(prefixes)==4*h+16
            constructed+=1
    return {'status':'EXACT_PASS','scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'theorem':'C_min(h)=4h+16 for all integers h>=4, one full key, low signatures 1/2/4/8',
            'tail_patterns':len(tails),'dfa_states':9,'signature4_initial_native_steps':sorted(sig4),
            'signature1_initial_native_steps':sorted(sig1),'exhaustive_by_h':exhaustive,
            'constructors_checked':constructed}

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,sort_keys=True))
