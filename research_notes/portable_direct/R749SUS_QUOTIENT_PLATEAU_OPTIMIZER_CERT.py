#!/usr/bin/env python3
"""R749SUS: O(M^1/4) exact quotient-plateau optimizer (arithmetic operations).
Auxiliary named two-Port WBRC-T30–T32; conditional on cited Q=+1 classification.
"""
from math import isqrt
import json


def score_xy(x, y):
    n=x*y
    return (n-1)*(n-x-1)*(n-y-1)


def near_product(m):
    t=isqrt(m+1)
    k=m+1-t*t
    j=1 if k<=t else 2
    z=0
    while z*(z+j)<j*t-k:
        z+=1
    x0,y0=t-z,t+z+j
    assert x0>=2 and x0*y0<=m+1
    return x0,y0,t


def cutoff(m):
    b=m+1
    x0,y0,t=near_product(m)
    t0=score_xy(x0,y0)
    K=m*(m*m+b)-t0
    def phi(x):
        return m*m*(x*x+b)-K*x
    lo,hi=2,x0
    assert phi(hi)<=0
    while lo<hi:
        mid=(lo+hi)//2
        if phi(mid)<=0:
            hi=mid
        else:
            lo=mid+1
    assert lo==2 or phi(lo-1)>0
    return lo,t,t0


def solve(m):
    assert m>=9999
    b=m+1
    xmin,t,witness=cutoff(m)
    k=b-t*t
    H=t-xmin
    j0=k//t
    jmax=(k+H*H)//(t-H)
    opt=[]; best=-1; checked=0; skipped=0
    for j in range(j0,jmax+1):
        if j==j0:
            h=0
        else:
            D=j*j+4*(j*t-k)
            assert D>=0
            h=max(0,(isqrt(D)-j)//2)
            if h*h+j*h+k-j*t<0:
                h+=1
        if h>H:
            continue
        x=t-h
        jj=(k+h*h)//x
        if jj!=j:
            skipped+=1
            continue
        y=t+h+j
        assert y==b//x
        assert b-x*y==h*h+j*h+k-j*t
        if x*y-x-y<1:
            continue
        value=score_xy(x,y)
        checked+=1
        if value>best:
            best=value;opt=[(x,y)]
        elif value==best:
            opt.append((x,y))
    assert best>=witness
    num=sum(2 if x==y else 4 for x,y in opt)
    return best, num, opt, dict(plateaus_checked=checked,j_range=jmax-j0+1,skipped=skipped,original_x_window=H+1,xmin=xmin,t=t)


def oracle(m):
    b=m+1
    opt=[]; best=-1
    for x in range(2,isqrt(b)+1):
        y=b//x
        if x*y-x-y<1:
            continue
        val=score_xy(x,y)
        if val>best:best=val;opt=[(x,y)]
        elif val==best:opt.append((x,y))
    return best,sum(2 if x==y else 4 for x,y in opt),opt


def verify():
    max_counts=[0,0];count=0;examples={}
    for m in range(9999,25001):
        fast=solve(m)
        slow=oracle(m)
        assert fast[:3]==slow,(m,fast[:3],slow)
        max_counts=[max(max_counts[0],fast[3]['plateaus_checked']),max(max_counts[1],fast[3]['original_x_window'])]
        count+=1
    samples=[9999,10000,25000,100000,1000000,100000000,10**12]
    for m in samples:
        fast=solve(m)
        slow=oracle(m)
        assert fast[:3]==slow,(m,fast[:3],slow)
        examples[str(m)]={"value":str(fast[0]),"named_count":fast[1],"pairs":fast[2],**fast[3]}
    for m in [10**14,10**16,10**18]:
        fast=solve(m)
        examples[str(m)]={"value":str(fast[0]),"named_count":fast[1],"pairs":fast[2],**fast[3],"crosscheck":"plateau-local exact checks; full oracle not executed"}
    return {"status":"PASS","id":"R749SUS_QUOTIENT_PLATEAU_V1","all_m_crosscheck":{"from":9999,"to":25000,"count":count,"maximum_plateaus":max_counts[0],"maximum_old_x_window":max_counts[1]},"extra_full_x_crosscheck_count":len(samples),"examples":examples,"scope":"exact integer arithmetic; Q=+1 classification from R749SUO not independently re-proved"}

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,sort_keys=True,indent=2))
