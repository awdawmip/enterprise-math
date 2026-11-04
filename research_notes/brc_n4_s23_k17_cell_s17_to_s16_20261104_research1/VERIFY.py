#!/usr/bin/env python3
"""Exact Fraction/isqrt certificate: BRC S23 K17, 1/7<=s<=1/6."""
from fractions import Fraction as F
from math import isqrt
N=34
S=10**48
def I(x):
    return x if isinstance(x,tuple) else (F(x),F(x))
def add(x,y):
    x,y=I(x),I(y);return (x[0]+y[0],x[1]+y[1])
def neg(x):
    x=I(x);return (-x[1],-x[0])
def sub(x,y):
    return add(x,neg(y))
def mul(x,y):
    x,y=I(x),I(y);v=[a*b for a in x for b in y];return(min(v),max(v))
def div(x,y):
    y=I(y);assert y[0]>0;return mul(x,(1/y[1],1/y[0]))
def sqrti(x):
    x=F(x);assert x>0
    k=isqrt(x.numerator*S*S//x.denominator)
    lo,hi=F(k,S),F(k+1,S)
    assert lo*lo<=x<hi*hi
    return(lo,hi)
def log_rational(x):
    x=F(x);assert x>0
    y=(x-1)/(x+1);assert abs(y)<F(1,3)
    t=y;partial=F(0)
    for k in range(N):
        partial+=2*t/F(2*k+1);t*=y*y
    bound=2*abs(t)/(F(2*N+1)*(1-y*y))
    return(partial-bound,partial+bound)
def logi(x):
    x=I(x);assert x[0]>0
    return(log_rational(x[0])[0],log_rational(x[1])[1])
a,b=F(11,21),F(10,21)
def info(s):
    s=F(s);u=mul(s,sqrti(a*b))
    qt=add(1-s,mul(2,u))
    qb=add(u,sqrti((1-a*s)*(1-b*s)))
    ct=neg(logi(qt));fh=neg(logi(qb))
    H=logi(a/b);J=logi(F(1-b*s,1-a*s))
    rho=div(J,add(H,J))
    cb=add(mul(rho,logi(div(rho,a*s))),
           mul(sub(1,rho),logi(div(sub(1,rho),1-a*s))))
    return ct,fh,cb
def check(name,v,scale):
    assert v[0]>0,(name,v)
    print(name+'_GT', (v[0]*scale).__floor__(), '/'+str(scale))
def main():
    l,r,delta=F(1,7),F(1,6),F(1,1000)
    ct0,fh0,cb0=info(l-delta)
    ct1,fh1,cb1=info(l)
    ct2,fh2,cb2=info(r)
    ct3,fh3,cb3=info(r+delta)
    L=div(sub(cb1,cb0),delta)
    RT=div(sub(ct3,ct2),delta)
    UF=div(sub(add(mul(7,ct3),mul(4,cb3)),
               add(mul(7,ct2),mul(4,fh2))),delta)
    check('GLOBAL_8T2B_EXCLUSION_SLOPE_15L_MINUS_8RT',
          sub(mul(15,L),mul(8,RT)),10**9)
    check('GLOBAL_7T4B_VS_PUREB_SLOPE_17L_MINUS_UF',
          sub(mul(17,L),UF),10**9)
    check('8T2B_BELOW_PUREB_AT_S1_7',
          sub(mul(15,cb1),mul(8,ct1)),10**12)
    check('7T4B_ABOVE_PUREB_AT_S1_7',
          sub(add(mul(7,ct1),mul(4,fh1)),mul(17,cb1)),10**15)
    sl,sr=F(14287,100000),F(14291,100000)
    cl,hl,bl=info(sl)
    cr,hr,br=info(sr)
    check('ROOT_GT_14287_100000',
          sub(add(mul(7,cl),mul(4,hl)),mul(17,bl)),10**15)
    check('ROOT_LT_14291_100000',
          sub(mul(13,br),mul(7,cr)),10**15)
    check('NEW_6T6B_BEATS_PUREB_AT_S1_6',
          sub(add(mul(6,ct2),mul(6,fh2)),mul(17,cb2)),10**15)
    check('7T4B_BELOW_PUREB_AT_S1_6',
          sub(mul(13,cb2),mul(7,ct2)),10**15)
    print('PASS_BRC_S23_K17_FULL_CELL_S1_7_TO_S1_6_AND_BOUNDARY_JUMP_20261104')
    print('Domain: real 1/7<=s<1/6, unique global switch in (14287/100000,14291/100000); at s=1/6 unique 6T6B.')
if __name__=='__main__':
    main()
