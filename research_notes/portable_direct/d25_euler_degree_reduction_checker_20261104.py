#!/usr/bin/env python3
"""Finite-field exact Euler identity, independent of native experiments."""
from math import comb
def primes(limit):
    v=bytearray(b'\x01')*(limit+1);v[0:2]=b'\x00\x00'
    for i in range(2,int(limit**0.5)+1):
        if v[i]:v[i*i:limit+1:i]=b'\x00'*(((limit-i*i)//i)+1)
    return (p for p in range(5,limit+1) if v[p])
def coeff(a,b,p):
    r=[1];v=1
    for k in range(min(a,b)):
        v=v*(a-k)*(b-k)*pow(k+1,-2,p)%p;r.append(v)
    return r
def ev(c,x,p):
    y=dy=0
    for u in c[::-1]:
        dy=(dy*x+y)%p;y=(y*x+u)%p
    return y,dy
def check():
    classes={5:0,7:0,13:0,23:0};full=0
    for p in primes(10000):
        if p%8 not in (5,7):continue
        a,b,c,d=[(-j*pow(8,-1,p))%p for j in (1,3,5,7)]
        h=(p+1)//2;H=coeff(a,b,p);J=coeff(c,d,p)
        assert len(H)==h+len(J)
        z=pow(9,-1,p);hv,hd=ev(H,z,p);jv,jd=ev(J,z,p)
        assert hv==pow(1-z,h,p)*jv%p
        assert (hv+16*z*hd)%p == pow(1-z,h-1,p)*((1-9*z)*jv+16*z*(1-z)*jd)%p
        if p<=251:
            full+=1;f=[(-1 if k%2 else 1)*comb(h,k)%p for k in range(h+1)]
            v=[0]*len(H)
            for i,x in enumerate(f):
                for j,y in enumerate(J):v[i+j]=(v[i+j]+x*y)%p
            assert v==H
            for x in range(p):
                v,dv=ev(H,x,p);w,dw=ev(J,x,p)
                assert v==pow(1-x,h,p)*w%p
                assert (v+16*x*dv)%p==pow(1-x,h-1,p)*((1-9*x)*w+16*x*(1-x)*dw)%p
        t=p%24;classes[t]+=1
        assert ((jv==0 and jd!=0) if t in (13,23) else (jd==0 and jv!=0)),(p,jv,jd)
    print('PASS primes=',sum(classes.values()),'full polynomial + all field points=',full,'classes=',classes)
if __name__=='__main__':check()
