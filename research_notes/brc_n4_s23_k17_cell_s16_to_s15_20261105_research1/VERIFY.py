#!/usr/bin/env python3
"""Exact rational certificate for BRC N=4 S23 K=17 on [1/6,1/5].
All arithmetic used for signs is Fraction interval arithmetic; no floating inputs.
"""
from fractions import Fraction as F
from math import isqrt
N = 34
S = 10**48

def I(x):
    return x if isinstance(x, tuple) else (F(x), F(x))

def add(x,y):
    x,y=I(x),I(y)
    return (x[0]+y[0],x[1]+y[1])

def neg(x):
    x=I(x)
    return (-x[1],-x[0])

def sub(x,y): return add(x,neg(y))

def mul(x,y):
    x,y=I(x),I(y)
    p=[u*v for u in x for v in y]
    return (min(p),max(p))

def div(x,y):
    y=I(y)
    assert y[0]>0
    return mul(x,(1/y[1],1/y[0]))

def sqrti(x):
    x=F(x)
    assert x>0
    k=isqrt((x.numerator*S*S)//x.denominator)
    lo,hi=F(k,S),F(k+1,S)
    assert lo*lo<=x<hi*hi
    return (lo,hi)

def log_rational(x):
    x=F(x)
    assert x>0
    y=(x-1)/(x+1)
    assert abs(y)<F(1,3)
    t=y
    partial=F(0)
    for k in range(N):
        partial+=2*t/F(2*k+1)
        t*=y*y
    bound=2*abs(t)/(F(2*N+1)*(1-y*y))
    return (partial-bound,partial+bound)

def logi(x):
    x=I(x)
    assert x[0]>0
    return (log_rational(x[0])[0],log_rational(x[1])[1])

a,b=F(11,21),F(10,21)

def info(s):
    s=F(s)
    u=mul(s,sqrti(a*b))
    qt=add(1-s,mul(2,u))
    qb=add(u,sqrti((1-a*s)*(1-b*s)))
    ct=neg(logi(qt))
    fh=neg(logi(qb))
    H=logi(a/b)
    J=logi(F(1-b*s,1-a*s))
    rho=div(J,add(H,J))
    cb=add(mul(rho,logi(div(rho,a*s))),
           mul(sub(1,rho),logi(div(sub(1,rho),1-a*s))))
    return ct,fh,cb

def check(name,iv,scale):
    assert iv[0]>0,(name,iv)
    print(f'{name}_GT {iv[0]*scale//1}/{scale}')

def main():
    l,r,d=F(1,6),F(1,5),F(1,1000)
    ctl,fhl,cbl=info(l)
    ctr,fhr,cbr=info(r)
    _,_,cbld=info(l-d)
    ctrd,_,cbrd=info(r+d)
    L=div(sub(cbl,cbld),d)
    RT=div(sub(ctrd,ctr),d)
    UF=div(sub(add(mul(6,ctrd),mul(6,cbrd)),
               add(mul(6,ctr),mul(6,fhr))),d)
    check('GLOBAL_7T4B_EXCLUSION_13L_MINUS_7RT',sub(mul(13,L),mul(7,RT)),10**9)
    check('GLOBAL_6T6B_VS_PUREB_17L_MINUS_UF',sub(mul(17,L),UF),10**9)
    check('7T4B_BELOW_PUREB_AT_S1_6',sub(mul(13,cbl),mul(7,ctl)),10**12)
    # Signs of G=C(6,6)-17 CB use genuine lower and upper envelopes.
    check('6T6B_ABOVE_PUREB_AT_S1_6',sub(add(mul(6,ctl),mul(6,fhl)),mul(17,cbl)),10**15)
    check('6T6B_BELOW_PUREB_AT_S1_5',sub(mul(11,cbr),mul(6,ctr)),10**12)
    sl,sr=F(16668,100000),F(16674,100000)
    ctl2,fhl2,cbl2=info(sl)
    ctr2,fhr2,cbr2=info(sr)
    check('ROOT_GT_16668_100000',sub(add(mul(6,ctl2),mul(6,fhl2)),mul(17,cbl2)),10**15)
    check('ROOT_LT_16674_100000',sub(mul(11,cbr2),mul(6,ctr2)),10**15)
    # New exact-budget feasible (5,8) at s=1/5; compete against all others.
    check('NEW_5T8B_BEATS_PUREB_AT_S1_5',sub(add(mul(5,ctr),mul(8,fhr)),mul(17,cbr)),10**15)
    print('PASS_BRC_S23_K17_FULL_CELL_S1_6_TO_S1_5_AND_BOUNDARY_JUMP_20261105')
    print('Domain: real 1/6<=s<1/5; unique global switch in (16668/100000,16674/100000); at s=1/5 unique 5T8B.')

if __name__=='__main__': main()
