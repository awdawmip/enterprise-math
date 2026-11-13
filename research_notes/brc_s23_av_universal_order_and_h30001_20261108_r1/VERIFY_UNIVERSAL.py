#!/usr/bin/env python3
"""Exact S23/AV triangular threshold rank/select at arbitrary finite H."""
from fractions import Fraction as F
from math import gcd
from random import Random

def ln_bounds(y, terms):
    assert 0 < y < 1
    value=F(0)
    power=y
    for j in range(terms):
        value+=2*power/(2*j+1)
        power*=y*y
    tail=2*power/((2*terms+1)*(1-y*y))
    return value,value+tail

def r_bounds(terms):
    a,b=ln_bounds(F(1,3),terms)
    c,d=ln_bounds(F(1,15),terms)
    e,f=ln_bounds(F(1,9),terms)
    lo=(3*a-d)/(f+d)
    hi=(3*b-c)/(e+c)
    assert lo<hi
    return lo,hi

def rational_key(H):
    assert isinstance(H,int) and H>=1
    terms=12
    while True:
        low,high=r_bounds(terms)
        mid=(low+high)/2
        x=mid
        pm2,pm1=0,1
        qm2,qm1=1,0
        while x.denominator:
            a=x.numerator//x.denominator
            p=a*pm1+pm2
            d=a*qm1+qm2
            if d>H:
                if gcd(p,d)==1 and H*max(abs(low*d-p),abs(high*d-p))<1:
                    return p,d,terms,low,high
                break
            pm2,pm1=pm1,p
            qm2,qm1=qm1,d
            x=x-a
            if x==0:break
            x=1/x
        terms*=2

def ceildiv(a,b):
    return -((-a)//b)

def floor_sum(n,m,a,b):
    assert n>=0 and m>0 and a>=0
    bq,b=divmod(b,m)
    total=n*bq
    while True:
        if a>=m:
            total+=(n-1)*n*(a//m)//2
            a%=m
        if b>=m:
            total+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:return total
        n=y//m
        b=y%m
        a,m=m,a

def rank_lt(H,p,d,m):
    assert 0<=H<d and p>0 and d>0
    A=max(0,min(H+1,ceildiv(m,p)))
    B=max(0,min(H+1,ceildiv(d*H+m,p+d)))
    assert A<=B
    n=B-A
    return A*(H+1)-A*(A-1)//2+n*H-n*(A+B-1)//2-floor_sum(n,d,p,p*A-m)

def select(H,p,d,s):
    M=(H+1)*(H+2)//2
    assert 0<=s<M
    l=-d*H
    u=p*H+2
    while l+1<u:
        m=(l+u)//2
        if rank_lt(H,p,d,m)>s:u=m
        else:l=m
    key=u-1
    v=(key*pow(p,-1,d))%d
    j=(p*v-key)//d
    assert 0<=v and 0<=j and v+j<=H
    return key,v,j

def main():
    rng=Random(20261108)
    for H in [1,2,3,10,25,80]:
        p,d,terms,low,high=rational_key(H)
        assert d>H and H*max(abs(low*d-p),abs(high*d-p))<1
        arr=sorted((p*v-d*j,v,j) for v in range(H+1) for j in range(H-v+1))
        for i,(key,v,j) in enumerate(arr):
            assert rank_lt(H,p,d,key)==i
            assert select(H,p,d,i)==(key,v,j)
        for _ in range(40):
            m=rng.randint(-d*H-100,p*H+100)
            assert rank_lt(H,p,d,m)==sum(k<m for k,_,_ in arr)
        print('SMALL_EXACT_PASS',H,len(arr),p,d)
    for H in [380294,4564092,1000000000,1000000000000]:
        p,d,terms,low,high=rational_key(H)
        M=(H+1)*(H+2)//2
        svals=[0,1,M//7,M//2,M-2,M-1]
        for s in svals:
            key,v,j=select(H,p,d,s)
            assert rank_lt(H,p,d,key)==s
            assert rank_lt(H,p,d,key+1)==s+1
        print('BIG_EXACT_PASS',H,'thresholds',M,'key',p,d,'terms',terms,'probes',len(svals))
    print('PASS_UNIVERSAL_DYNAMIC_EXACT_ORDER_ORACLE')

if __name__=='__main__':main()
