#!/usr/bin/env python3
"""Independent exact signed-native H2-H9 witness audit for EC49FDW."""
import json, collections
from fractions import Fraction
from pathlib import Path
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
Q={2:4,3:2,4:2,5:4,6:2,7:4,8:4,9:2}
def steps(w):
    return tuple(z for c in w for z in OPS[c])
def key(w):
    s=steps(w);return tuple(s.count(i) for i in (1,2,3))
def pref(w):
    s=steps(w);return {s[:i] for i in range(1,len(s)+1)}
def observations(w):
    s=steps(w);ans=[]
    for name,prev in [('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0)]:
        state=name
        for t in s:
            if prev==1 and t==2:
                if state=='N': state='A'
                elif state=='B': state='BA'
            elif prev==2 and t==1:
                if state=='N': state='B'
                elif state=='A': state='AB'
            prev=t
        ans.append(('N','A','B','AB','BA').index(state))
    return tuple(ans)
def rank(ws):
    obs=[observations(w) for w in ws]
    cols=[[int(o[i]==state) for i in range(9)] for o in obs for state in range(5)]
    mat=[[Fraction(col[i]) for col in cols] for i in range(9)]
    pivot=0
    for j in range(len(mat[0])):
        where=next((r for r in range(pivot,9) if mat[r][j]),None)
        if where is None:continue
        mat[pivot],mat[where]=mat[where],mat[pivot]
        inv=mat[pivot][j]
        mat[pivot]=[v/inv for v in mat[pivot]]
        for r in range(pivot+1,9):
            if mat[r][j]:
                m=mat[r][j]
                mat[r]=[u-m*v for u,v in zip(mat[r],mat[pivot])]
        pivot+=1
        if pivot==9:break
    return pivot
data=json.loads(Path(__file__).with_name('WITNESSES_EC49FDW.json').read_text())
assert data['science_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert len(data['cases'])==8
horizons=0; native_words=0; costs=[]
for rec in data['cases']:
    W={int(h):ws for h,ws in rec['words'].items()}
    assert {h:len(ws) for h,ws in W.items()}==Q
    assert all(len(set(ws))==len(ws) for ws in W.values())
    allkeys=set(); allobs=set(); allpre=set()
    for h,ws in W.items():
        assert rank(ws)==9,(h,ws)
        horizons+=1
        for w in ws:
            s=steps(w)
            assert len(w)==h and len(s)==2*(sum(key(w))-1)
            c=collections.Counter(s)
            assert c[1]-c[-1]==2
            assert all(c[i]==c[-i] for i in (2,3,4,5,6))
            if h>=4:
                assert list(key(w))==rec['late_keys'][rec['schedule'][h-4]]
            allkeys.add(key(w));allobs.add(observations(w));allpre.update(pref(w))
            native_words+=1
    assert len(allkeys)==5 and len(allobs)==6
    assert len(allpre)==rec['cost']
    assert rec['baseline_cost']-rec['cost']==8
    costs.append(len(allpre))
assert costs==[118,118,118,118,120,120,120,120]
print(json.dumps({'verified_cases':8,'rank9_horizon_checks':horizons,'complete_words_checked':native_words,'costs':costs,'min_constructed_cost':min(costs),'status':'PASS'},indent=2))
