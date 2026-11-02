#!/usr/bin/env python3
"""PREFIX-440 exact independent certificate, no upstream module import."""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations
from math import comb
import json

def rank(a):
    b=[[Fraction(x) for x in r] for r in a]; k=0
    for j in range(len(b[0])):
        p=next((i for i in range(k,len(b)) if b[i][j]),None)
        if p is None: continue
        b[k],b[p]=b[p],b[k]; d=b[k][j]; b[k]=[x/d for x in b[k]]
        for i in range(len(b)):
            if i!=k and b[i][j]:
                d=b[i][j]; b[i]=[x-d*y for x,y in zip(b[i],b[k])]
        k+=1
        if k==len(b): break
    return k

def moment(b,d): return sum(c*x**d for x,c in b.items())
def recover_r6(n,x,r): 
    assert len(x)==6 and len(r)==5
    z=n-sum(x)
    assert z>=0 and z%2==0
    return (z//2+sum(r))%2

for n in range(3):
    xs=[n-2*k for k in range(n+1)]
    assert rank([[x**d for x in xs] for d in range(3)])==n+1
xs=[3,1,-1,-3]; v=[[x**d for x in xs] for d in range(4)]
vec=[(-1)**k*comb(3,k) for k in range(4)]
assert vec==[1,-3,3,-1]
assert rank(v[:3])==3 and rank(v)==4
assert [sum(r[k]*vec[k] for k in range(4)) for r in v]==[0,0,0,48]

for n in range(3,101):
    assert len(list(combinations(range(n),1)))>=3
    assert len(list(combinations(range(n),2)))>=3
    assert comb(n,3)>=1
    E={n:1,n-4:3}; O={n-2:3,n-6:1}
    assert all(moment(E,d)==moment(O,d) for d in range(3))
    assert moment(E,3)-moment(O,3)==48
E=Counter();O=Counter()
for w in product((1,-1),repeat=3):
    (E if (sum(s==-1 for s in w)%2)==0 else O)[sum(w)]+=1
assert dict(E)=={3:1,-1:3} and dict(O)=={1:3,-3:1}
assert [moment(E,d) for d in range(3)]==[4,0,12]
assert [moment(O,d) for d in range(3)]==[4,0,12]
assert (moment(E,3),moment(O,3))==(24,-24)
f=lambda x: int(((3-x)//2)%2==0)
assert sum(c*f(x) for x,c in E.items())==4
assert sum(c*f(x) for x,c in O.items())==0
assert f(3)-3*f(1)+3*f(-1)-f(-3)==4
assert (5*3*3-3*3+7)-3*(5*1*1-3*1+7)+3*(5-3*(-1)+7)-(5*9-3*(-3)+7)==0
coalesced=Counter([(0,0,1,(0,)*6),(0,0,1,(0,)*6)])
split=Counter([(0,1,1,(0,)*6),(0,2,1,(0,)*6)])
assert len(coalesced)==1 and next(iter(coalesced.values()))==2
assert len(split)==2
words=0
alphabet=[(a,s) for a in range(6) for s in (-1,1)]
for n in range(6):
    for word in product(alphabet,repeat=n):
        x=[0]*6;r=[0]*6
        for a,s in word:
            x[a]+=s
            if s<0:r[a]^=1
        assert recover_r6(n,x,r[:5])==r[5]
        words+=1
assert words==271453
print(json.dumps(dict(status="PASS", arithmetic="exact integers and Fraction",
    rank_n0_n1_n2="1,2,3", rank_n3_M0_M2=3,rank_n3_M0_M3=4,
    kernel=vec,even_histogram=dict(E),odd_histogram=dict(O),
    moments_0_2=[4,0,12],cubic_gap=48,parity_observer_gap=4,
    uniform_n_checked="3..100",signed_six_axis_words_checked=words,
    upstream_classes_imported=False),sort_keys=True))
