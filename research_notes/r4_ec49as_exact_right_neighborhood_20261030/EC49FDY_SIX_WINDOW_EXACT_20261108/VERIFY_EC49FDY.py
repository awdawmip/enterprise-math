#!/usr/bin/env python3
"""Independent EC49FDY eight-system verifier: Fraction rank-nine, original six signed-native codes, BRC keys, complete primitive prefixes."""
import json,collections
from fractions import Fraction
from pathlib import Path
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
Q={2:4,3:2,4:2,5:4,6:2,7:4,8:4,9:2}
def steps(w):return tuple(k for op in w for k in OPS[op])
def history(w):
    ret=[]
    for s,prev in [('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0)]:
        for t in steps(w):
            if prev==1 and t==2:
                if s=='N':s='A'
                elif s=='B':s='BA'
            elif prev==2 and t==1:
                if s=='N':s='B'
                elif s=='A':s='AB'
            prev=t
        ret.append(('N','A','B','AB','BA').index(s))
    return ret
def rank9(ws):
    columns=[[int(o[i]==state) for i in range(9)] for o in map(history,ws) for state in range(5)]
    m=[[Fraction(col[i]) for col in columns] for i in range(9)]
    pivot=0
    for j in range(len(m[0])):
        k=next((i for i in range(pivot,9) if m[i][j]),None)
        if k is None:continue
        m[pivot],m[k]=m[k],m[pivot]
        d=m[pivot][j];m[pivot]=[x/d for x in m[pivot]]
        for i in range(pivot+1,9):
            if m[i][j]:
                q=m[i][j];m[i]=[x-q*y for x,y in zip(m[i],m[pivot])]
        pivot+=1
        if pivot==9:break
    return pivot
file=Path(__file__).with_name('EC49FDY_FULL_WITNESSES.json')
data=json.loads(file.read_text())
assert data['science_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert len(data['cases'])==8
count=0
for case_id,cost,words in data['cases']:
    assert count==case_id
    w={int(h):list(ws) for h,ws in words.items()}
    assert {h:len(ws) for h,ws in w.items()}==Q
    union=set();allkeys=set()
    for h,ws in w.items():
        assert len(set(ws))==len(ws) and all(len(x)==h for x in ws)
        assert rank9(ws)==9,(case_id,h)
        for word in ws:
            seq=steps(word);ctr=collections.Counter(seq)
            assert ctr[1]-ctr[-1]==2 and all(ctr[i]==ctr[-i] for i in (2,3,4,5,6))
            key=(ctr[1],ctr[2],ctr[3])
            allkeys.add(key)
            assert len(seq)==2*(sum(key)-1)
            union.update(seq[:i] for i in range(1,len(seq)+1))
    assert len(allkeys)==5 and len(union)==cost
    count+=1
print(json.dumps({'status':'PASS','cases':count,'rank9_windows':8*count,'complete_native_paths':24*count,'costs':[c[1] for c in data['cases']],'source':'original nine histories, exact rational rank elimination and literal full native prefixes'},indent=2))
