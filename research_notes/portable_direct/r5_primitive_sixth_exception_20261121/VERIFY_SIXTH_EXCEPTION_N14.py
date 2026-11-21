#!/usr/bin/env python3
"""Exact sixth-root Laurent order-15 correction for exceptional R5 thresholds."""
from fractions import Fraction
from collections import defaultdict
import json

S=[set(range(214,219)), {214,216,217,218,219,220,221},
   set(range(215,222)), set(range(223,291)),set(range(296,313))]
PRICES=set(range(214,315))
Q=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
Z=(0,0)
ONE=(1,0)

def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[0],-x[1]
def mul(x,y):
    a,b=x;c,d=y
    return a*c-b*d,a*d+b*c+b*d
def smul(x,v): return v*x[0],v*x[1]
def inv(x):
    a,b=x;n=a*a+a*b+b*b
    return Fraction(a+b,n),Fraction(-b,n)
def div(x,y): return mul(x,inv(y))
def sub(x,y): return add(x,neg(y))

def vloc(mask,m):
    active=[j for j in range(3) if (mask>>j)&1]
    U=sorted(set().union(*(S[j] for j in active)))
    state={tuple(0 for _ in active):(ONE,Z)}
    for p in U:
        indexes=[i for i,j in enumerate(active) if p in S[j]]
        nex=defaultdict(lambda:(Z,Z))
        for bounds,(h,hm) in state.items():
            limit=min(m-1-bounds[i] for i in indexes)
            factor=ONE
            for n in range(limit+1):
                key=list(bounds)
                for i in indexes:key[i]+=n
                key=tuple(key)
                sh=mul(h,factor)
                shm=mul(add(hm,smul(h,p*n)),factor)
                prev,prevm=nex[key]
                nex[key]=add(prev,sh),add(prevm,shm)
                factor=mul(factor,Q[p%6])
        state=nex
    return tuple(tuple(sum((v[i][j] for v in state.values()),Fraction(0))
                       for j in range(2)) for i in range(2))

def ratio(mask):
    U=set().union(*(S[j] for j in range(3) if (mask>>j)&1))
    v=ONE
    for p in sorted(U-S[0]):v=mul(v,sub(ONE,Q[p%6]))
    for p in sorted(S[0]-U):v=div(v,sub(ONE,Q[p%6]))
    return v

def B_free(mask):
    U=set().union(*(S[j] for j in range(3) if (mask>>j)&1))
    b=(Fraction(0),Fraction(0))
    for p in PRICES-U:
        if p%6==0:
            b=add(b,(Fraction(p-1,2),0))
        else:
            b=sub(b,smul(div(Q[p%6],sub(ONE,Q[p%6])),p))
    return b

def calc(m):
    s0=Z;s1=Z
    for mask in range(1,8):
        h,hm=vloc(mask,m)
        rr=ratio(mask)
        b=B_free(mask)
        sign=1 if mask.bit_count()%2 else -1
        s0=add(s0,smul(mul(rr,h),sign))
        s1=add(s1,smul(mul(rr,sub(mul(h,b),hm)),sign))
    return s0,s1

results={}
for m in [1,2,3,4,5,6,7,8,11,17,23]:
    lead,subleading=calc(m)
    results[str(m)]={'lead_s0':list(map(str,lead)),
                     'pole_order_15_s1':list(map(str,subleading)),
                     'N14_coefficient':list(map(str,add(subleading,smul(lead,8))))}
    print(m,results[str(m)])
for m,expect in {5:(1336,1726),11:(7490,1688),
                 17:(16722,3366),23:(30772,3280)}.items():
    assert results[str(m)]['lead_s0']==['0','0']
    assert results[str(m)]['pole_order_15_s1']==list(map(str,expect))
print('PASS')
print(json.dumps(results,indent=2))
