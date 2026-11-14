"""Independent BRC native signed-X6 witness, complete-key, DFA and prefix checks."""
from collections import Counter
import json, subprocess, sys
A={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
O='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0)
B={4:'ce',8:'ec',2:'ed',1:'de'}
def check(w,h,s):
    q=0
    for a in w:q=T[q][O.index(a)]
    assert S[q]==s
    c=Counter(w);z=c['a']+1;x=h+1-c['g'];y=h+1-2*z-c['f']
    assert min(x,y,z)>0
    assert (c['a'],c['e'],c['c']+c['d'],c['f'],c['g'])==(z-1,z,x+y-h-1,h+1-y-2*z,h+1-x)
    p=tuple(v for a in w for v in A[a])
    assert len(p)==2*(x+y+z-1)
    assert tuple(p.count(i)-p.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
    return (x,y,z),p
def count(paths):return len({p[:i] for p in paths for i in range(1,len(p)+1)})
base=[check(w,2,s)[1] for s,w in B.items()]
assert count(base)==28
expected={3:36,4:44,5:52,6:59,7:65,8:71,9:77,10:82}
for h,cost in expected.items():
    with open(f'report_H{h}.json') as file:r=json.load(file)
    assert r['minimum_cost']==cost
    assert sorted(t['signature'] for t in r['witness'])==[1,2,4,8]
    paths=base+[check(t['word'],h,t['signature'])[1] for t in r['witness']]
    assert count(paths)==cost
def fam(h,x):
    r=x-3;s=h+1-x
    return {4:'f'*r+'e'+'g'*s+'c',2:'f'*r+'e'+'g'*s+'d',8:'g'+'f'*r+'e'+'g'*(s-1)+'c',1:'g'+'f'*r+'e'+'g'*(s-1)+'d'}
four=fam(10,4);keys_and_paths=[check(w,10,s) for s,w in four.items()]
assert {k for k,p in keys_and_paths}=={(4,8,1)}
assert count(base+[p for k,p in keys_and_paths])==82
print('WITNESS_CHECK_PASS; 8 horizons including unrestricted H9=77 and H10=82; 2-key H10=82')
