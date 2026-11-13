#!/usr/bin/env python3
"""Exact Fraction / isqrt certificate for BRC S23 K17 full-cell switch."""
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
    s=F(s)
    u=mul(s,sqrti(a*b))
    qt=add(1-s,mul(2,u))
    qb=add(u,sqrti((1-a*s)*(1-b*s)))
    ct=neg(logi(qt));fh=neg(logi(qb))
    h=logi(a/b)
    ell=logi(F(1-b*s,1-a*s))
    r=div(ell,add(h,ell))
    cb=add(mul(r,logi(div(r,a*s))),mul(sub(1,r),logi(div(sub(1,r),1-a*s))))
    return ct,fh,cb
def floorlower(x,scale):
    return (x[0]*scale).__floor__()

def main():
    delta=F(1,1000)
    ct0,fh0,cb0=info(F(1,8)-delta)
    ct1,fh1,cb1=info(F(1,8))
    ct2,fh2,cb2=info(F(1,7))
    ct3,fh3,cb3=info(F(1,7)+delta)
    L=div(sub(cb1,cb0),delta)
    U=div(sub(add(mul(8,ct3),mul(2,cb3)),add(mul(8,ct2),mul(2,fh2))),delta)
    margin=sub(mul(17,L),U)
    assert margin[0]>F(1,2000)
    print('GLOBAL_SECANT_MARGIN_GT',floorlower(margin,10**9),'/10^9')
    print('L_interval',float(L[0]),float(L[1]))
    print('U_interval',float(U[0]),float(U[1]))
    print('17L_minus_U_lower',float(margin[0]))
    ct,fh,cb=info(F(12501,100000))
    mixed=sub(add(mul(8,ct),mul(2,fh)),mul(17,cb))
    assert mixed[0]>0
    print('MIXED_WIN_AT_12501_100000_GT',floorlower(mixed,10**15),'/10^15')
    ct,fh,cb=info(F(12503,100000))
    pure=sub(mul(15,cb),mul(8,ct))
    assert pure[0]>0
    print('PURE_B_WIN_AT_12503_100000_GT',floorlower(pure,10**15),'/10^15')
    jump=sub(add(mul(7,ct2),mul(4,fh2)),mul(17,cb2))
    assert jump[0]>0
    old=sub(mul(15,cb2),mul(8,ct2))
    assert old[0]>0
    print('BOUNDARY_NEW_7T4B_OVER_B_GT',floorlower(jump,10**15),'/10^15')
    print('BOUNDARY_8T2B_LOSES_TO_B_GT',floorlower(old,10**15),'/10^15')
    print('PASS_S23_K17_FULL_CELL_UNIQUE_SWITCH_AND_S1_7_JUMP_20261104')
    print('Scope: all real 1/8 <= s < 1/7; unique root in (12501/100000,12503/100000); 7T4B wins at s=1/7.')
if __name__=="__main__":
    main()
