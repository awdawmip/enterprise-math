#!/usr/bin/env python3
"""Exact author-side ten-round auxiliary four-label BRC classifier.
No native X6 dynamics, independent Driver review, or external libraries.
"""
from fractions import Fraction as F
from collections import Counter
from math import comb

GOOD=(3,6,10,12)
def step(state,protect,t):
    nxt=[[0]*(t+1) for _ in range(16)]
    for mask,pol in enumerate(state):
        if not any(pol): continue
        for v in range(4):
            if v==protect: continue
            dst=nxt[mask|(1<<v)]
            s=(1 if v==1 else -1 if v==2 else 0) if protect==0 else 0
            for j,a in enumerate(pol):
                dst[j]+=a
                if s:dst[j+1]+=s*a
    return tuple(map(tuple,nxt))
def mass(state,t):
    return tuple(sum(state[m][i] for m in GOOD) for i in range(t+1))
def value(p,x):
    return sum((a*x**i for i,a in enumerate(p)),F(0))
def bez(p,a=F(0),b=F(1),degree=10):
    power=[sum((F(p[h])*comb(h,j)*a**(h-j)*(b-a)**j
                for h in range(j,len(p))),F(0)) for j in range(degree+1)]
    return [sum((power[j]*F(comb(k,j),comb(degree,j))
                 for j in range(k+1)),F(0)) for k in range(degree+1)]
def word_diffs(word):
    state=tuple([(1,)]+[(0,)]*15);prev=(0,);out=[];nums=[]
    for t,c in enumerate(word,1):
        state=step(state,int(c),t);cur=mass(state,t)
        out.append(tuple(cur[i]-(3*prev[i] if i<len(prev) else 0)
                         for i in range(t+1)))
        nums.append(cur);prev=cur
    return nums,out

states={tuple([(1,)]+[(0,)]*15):(1,'')}
for t in range(1,10):
    nxt={}
    for st,(cnt,rep) in states.items():
        for v in range(4):
            ns=step(st,v,t)
            if ns in nxt:
                n,ex=nxt[ns];nxt[ns]=(n+cnt,ex)
            else:nxt[ns]=(cnt,rep+str(v))
    states=nxt
assert len(states)==220 and sum(c for c,w in states.values())==4**9
polys=Counter();reps={};states10=Counter()
for st,(count,word) in states.items():
    previous=mass(st,9)
    for v in range(4):
        ns=step(st,v,10);cur=mass(ns,10);states10[ns]+=count
        q=tuple(cur[i]-(3*previous[i] if i<len(previous) else 0)
                for i in range(11))
        polys[q]+=count;reps.setdefault(q,word+str(v))
assert len(states10)==286 and sum(states10.values())==4**10
assert len(polys)==628 and sum(polys.values())==4**10
exception=[];negative=0;min_margin=None
for q,count in polys.items():
    margin=min(bez([-x for x in q]))
    if margin>0:
        negative+=count
        min_margin=margin if min_margin is None else min(margin,min_margin)
    else:exception.append((reps[q],count,q))
E=(-1524,0,-4356,0,3360,0,2856,0,180,0,-2)
V=(-1018,-753,-2256,84,2100,714,1008,84,39,0,0)
assert negative==4**10-10 and min_margin==58
assert set((cnt,q) for w,cnt,q in exception)=={(1,E),(9,V)}
assert min(bez([-v for v in E],F(0),F(97,100)))>0
assert min(bez([-v for v in V],F(0),F(4999,5000)))>0
assert value(V,F(0))<0 and value(V,F(1))==2
signs=[1 if x>0 else -1 for x in reversed(V) if x]
assert sum(a!=b for a,b in zip(signs,signs[1:]))==1
for k in range(0,10):
    w='0'*10 if k==0 else '0'*(k-1)+'2'+'0'*(10-k)
    nums,ds=word_diffs(w)
    left=F(97,100) if k==0 else F(4999,5000)
    for t in range(2,10):
        sign=-1 if k>=4 and t==k else +1
        assert min(bez([sign*x for x in ds[t-1]],left,F(1)))>0,(w,t)
    if k>=4:
        peak=k-1
        gap=[0]*11
        for i,x in enumerate(nums[peak-1]):gap[i]+=3**(10-peak)*x
        for i,x in enumerate(nums[9]):gap[i]-=x
        assert min(bez(gap,F(4999,5000),F(1)))>0,w
lo,hi=F(4999,5000),F(1)
for _ in range(150):
    m=(lo+hi)/2
    if value(V,m)<0:lo=m
    else:hi=m
assert value(V,lo)<0<value(V,hi)
print('PASS: 4^10 words, 628 D10 polys, 626 strict negative groups')
print('PASS: ten exceptions, exact signs, earlier peak gaps')
print('root bracket:',lo,hi)
print('PASS: no second strict rebound through ten rounds given nine-round predecessor')
