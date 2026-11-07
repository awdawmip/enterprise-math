#!/usr/bin/env python3
"""Exact Laurent-polynomial regression of common D25 kernel operator & finite Green identity."""
from fractions import Fraction
from math import comb

def d(f):
    return {k:k*v for k,v in f.items() if k*v}

def mul(f,g):
    z={}
    for i,vi in f.items():
        for j,vj in g.items():z[i+j]=z.get(i+j,Fraction(0))+vi*vj
    return {k:v for k,v in z.items() if v}

def add(*fs):
    z={}
    for f in fs:
        for k,v in f.items():z[k]=z.get(k,Fraction(0))+v
    return {k:v for k,v in z.items() if v}

def scale(f,a):return {k:a*v for k,v in f.items() if a*v}

def L(f):
    z={}
    for k,v in f.items():
        z[k]=z.get(k,Fraction(0))+(6*k-1)*(3*k-1)*v
        z[k+1]=z.get(k+1,Fraction(0))-36*k*k*v
    return {k:v for k,v in z.items() if v}

def W(m):return {-i:Fraction(comb(m,i)*comb(2*m,i),2**i) for i in range(m+1)}

def F(N):
    c=Fraction(1,10)
    z={}
    for i in range(1,N+1):
        z[i]=c
        c*=Fraction(36*i*i,(6*i+5)*(3*i+2))
    return z

def check(m):
    p=6*m+1
    w=W(m)
    defect=add(L(w),scale(add(scale(d(w),9),scale(w,-2)),p),scale(w,p*p))
    assert not defect,(m,defect)
    f=F(m+9)
    lf=L(f)
    assert all(v==0 for k,v in lf.items() if 1<k<=m+9), (m,lf)
    assert lf.get(1)==1,(m,lf)
    j=add(mul(w,d(f)),scale(mul(f,d(w)),-1))
    lhs=add(scale(d(j),18),scale({k+1:v for k,v in d(j).items()},-36),scale(j,-9))
    rhs=add(mul(w,{1:Fraction(1)}),scale(mul(f,add(scale(d(w),9),scale(w,-2))),p),scale(mul(f,w),p*p))
    mismatch=add(lhs,scale(rhs,-1))
    assert all(v==0 for k,v in mismatch.items() if k<=9),(m,mismatch)
    return {'m':m,'p':p,'L_W_exact':True,'L_F_up_to_degree':m+9,'green_identity_degree_leq':9}

if __name__=='__main__':
    for m in (1,2,3,7,11,62):print(check(m))
    print('PASS six exact Laurent models, including p=13,19,43,67,373')
