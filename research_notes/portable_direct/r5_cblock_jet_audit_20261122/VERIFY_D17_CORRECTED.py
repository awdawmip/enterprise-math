#!/usr/bin/env python3
"""Correct ten order-17 R5 dotR witnesses using the true total-multiplicity Z-block.
Reuses the old author's exact A_m basis values pinned at @6f0635fa79fc610410cdb88f39bf538d2ddac510:D17_D19.csv.
The old C jet used prod(1-q**(m*p)); correct is D_Z * sum_{j<m} h_j.
Exact arithmetic in Z[q]/(q**17-1) and primitive cyclotomic coefficient c0.
"""
from pathlib import Path
import csv
D=17
OLD=[(13,-75752,-195551),(14,-74307,-176732),(15,-80393,-184246),
     (16,-90661,-191726),(17,1156,3859),(30,-174743,-195551),
     (31,-161126,-176732),(32,-173842,-184246),
     (33,-186524,-191726),(34,3859,3859)]
def shift(a,p):
    p%=D
    return a[-p:]+a[:-p] if p else a[:]
def dproduct(scale=1):
    p=[1]+[0]*(D-1);dp=[0]*D
    for price in range(296,313):
        b=shift(p,scale*price)
        db=[x+scale*price*y for x,y in zip(shift(dp,scale*price),b)]
        p=[x-y for x,y in zip(p,b)]
        dp=[x-y for x,y in zip(dp,db)]
    return p,dp
def mul(a,b):
    c=[0]*D
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[(i+j)%D]+=x*y
    return c
def c0(a):return a[0]-a[D-1]
M=102
h=[[0]*D for _ in range(M)]
h[0][0]=1
for price in range(296,313):
    for j in range(1,M):
        h[j]=[x+y for x,y in zip(h[j],shift(h[j-1],price))]
Dz,dDz=dproduct()
assert len(set(Dz))==1
s=[0]*D
true={}
for m in range(1,M+1):
    s=[x+y for x,y in zip(s,h[m-1])]
    true[m]=c0(mul(dDz,s))
outputs=[]
for r,u,v in OLD:
    m=(r,r+34,r+68)
    wrong=[c0(dproduct(t)[1]) for t in m]
    truejets=[true[t] for t in m]
    adjusted=[t-w for t,w in zip(truejets,wrong)]
    assert adjusted[2]-2*adjusted[1]+adjusted[0]==0
    newU=u+adjusted[0]
    newV=v+adjusted[1]-adjusted[0]
    assert newU and newU*newV>=0
    outputs.append((r,u,v,newU,newV))
out=Path(__file__).with_name('D17_CORRECTED_WITNESSES.csv')
with out.open('w',newline='') as f:
    w=csv.writer(f)
    w.writerow(('r','old_U','old_V','corrected_U','corrected_V'))
    w.writerows(outputs)
for row in outputs:print(*row,sep=',')
print('PASS corrected_order17_firstjet=10/10 all same-sign; degree_le_one consistent')
