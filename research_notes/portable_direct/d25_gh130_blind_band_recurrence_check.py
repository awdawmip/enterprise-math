#!/usr/bin/env python3
"""Independent coefficient recurrence for GH129, no factorials/multinomial sums.
Computes polynomial coefficients by the differential equation g P' = L g' P,
using reciprocal polynomial for degrees >= p in g^L.
"""
from d25_gh129_blind_band_check import add,mul,scale,power,inv,conj,div,neg,coefficient_prediction,fact_tables

def coeff_low_recurrence(p,B,L,maxdeg,reverse=False):
    assert 0<=L<p and maxdeg<p
    z=[(0,0)]*(maxdeg+1)
    if reverse:
        z[0]=(1,0)
        for k in range(maxdeg):
            v=add(scale(z[k],L-k,p), mul(B,scale(z[k-1] if k>0 else (0,0),2*L-k+1,p),p),p)
            z[k+1]=scale(v,pow(k+1,-1,p),p)
    else:
        assert B!=(0,0)
        z[0]=power(B,L,p)
        ib=inv(B,p)
        for k in range(maxdeg):
            v=add(scale(z[k],L-k,p),scale(z[k-1] if k>0 else (0,0),2*L-k+1,p),p)
            z[k+1]=mul(scale(v,pow(k+1,-1,p),p),ib,p)
    return z

def predict(p,B,s):
    N=(p-1)//2
    Cvec=coeff_low_recurrence(p,B,N-1,N)
    C=Cvec[N];D=Cvec[N-1]
    L=p-s
    A=coeff_low_recurrence(p,B,L,N)[N]
    rev=2*L-(3*N+1)
    E=coeff_low_recurrence(p,B,L,rev,reverse=True)[rev] if rev>=0 else (0,0)
    return neg(add(mul(A,conj(C,p),p),mul(E,conj(D,p),p),p),p), (A,E,C,D)

if __name__=='__main__':
    count=0
    for p,B in [(11,(3,1)),(11,(4,0)),(19,(4,2)),(43,(5,1)),(59,(7,3)),(3347,(2092,279))]:
        fac,ifac=fact_tables(p)
        N=(p-1)//2
        ss=[1,2,N] if p==3347 else list(range(1,N+1))
        for s in ss:
            expected,_=coefficient_prediction(p,B,s,fac,ifac)
            actual,parts=predict(p,B,s)
            assert expected==actual,(p,s,expected,actual,parts)
            count+=1
        print('recurrence',p,'B',B,'S_N+1',predict(p,B,1)[0])
    print('PASS_GH129_INDEPENDENT_COEFFICIENT_RECURRENCE',count)
