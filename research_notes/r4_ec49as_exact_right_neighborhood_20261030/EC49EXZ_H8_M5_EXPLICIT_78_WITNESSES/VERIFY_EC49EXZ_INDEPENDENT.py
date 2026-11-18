#!/usr/bin/env python3
"""Independent, exact witness verification: no external package or native solver needed."""
import json
from fractions import Fraction
from pathlib import Path

OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),
     'd':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
HISTORY=(('N',0),('N',1),('N',2),('A',0),('A',2),
         ('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
T4={1836687,1867942,1872656,1873981}
T2={1836425,1866380}

def path(word):
    return tuple(x for op in word for x in OPS[op])

def signature(p):
    result=0
    for i,(ev,previous) in enumerate(HISTORY):
        for s in p:
            if previous==1 and s==2:
                if ev=='N':ev='A'
                elif ev=='B':ev='BA'
            elif previous==2 and s==1:
                if ev=='N':ev='B'
                elif ev=='A':ev='AB'
            previous=s
        result+=BUCKETS.index(ev)*5**i
    return result

def rational_rank(matrix):
    a=[[Fraction(v) for v in row] for row in matrix]
    r=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[pivot],a[r]=a[r],a[pivot]
        x=a[r][col];a[r]=[v/x for v in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][col]:
                x=a[i][col]
                a[i]=[v-x*y for v,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def prefixes(paths):
    return {p[:i] for p in paths for i in range(1,len(p)+1)}

def run(case):
    keys=case['keys_by_h']
    assert len(keys)==7 and len({tuple(k) for k in keys})==5
    cumulative=set()
    all_signatures=set()
    cumulative_cost=[]
    for offset,(key,words) in enumerate(zip(keys,case['words_by_h'])):
        h=offset+2
        r=key[0]+key[1]-h-1
        desired=T4 if r>=1 else T2
        actual=set()
        assert len(words)==len(desired)
        for word in words:
            assert len(word)==h and set(word)<=set(OPS)-{'b'}
            p=path(word)
            assert tuple(p.count(i) for i in (1,2,3,4,5,6))==tuple(key)+(0,0,0)
            assert tuple(p.count(i)-p.count(-i) for i in (1,2,3,4,5,6))==(2,0,0,0,0,0)
            s=signature(p)
            assert s in desired and s not in actual
            actual.add(s)
            cumulative.update(prefixes([p]))
        assert actual==desired,(case['id'],h,actual,desired)
        all_signatures.update(actual)
        m=[[int((s//5**j)%5==b) for s in sorted(actual) for b in range(5)]
           for j in range(9)]
        assert rational_rank(m)==9,(case['id'],h,'not rank-nine')
        cumulative_cost.append(len(cumulative))
    core=prefixes([path(w) for w in ('ce','de','ec','ed')])
    assert len(core)==28 and core<=cumulative
    assert all_signatures==T2|T4 and len(all_signatures)==6
    assert cumulative_cost==case['expected_prefix_count']
    assert cumulative_cost[-1]==78
    return {'case':case['id'],'status':'PASS','E':78,'M':5,'S':6,
            'rank_nine_all_7_horizons':True,'prefix_cost_by_horizon':cumulative_cost}

data=json.loads(Path(__file__).with_name('EC49EXZ_EXPLICIT_WITNESSES.json').read_text())
report=[run(c) for c in data['cases']]
assert len(report)==2
print(json.dumps({'status':'PASS','reports':report},indent=2))
