#!/usr/bin/env python3
from fractions import Fraction as Q
from math import comb

def pair(a,b):
    a,b=Q(a),Q(b)
    den=a*a+b*b
    return (Q(1),-2*a/den,Q(1)/den)

def mul(f,g):
    h=[Q(0)]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        for j,y in enumerate(g): h[i+j]+=x*y
    return tuple(h)

def model(im):
    return mul(mul(pair(1,1),pair(2,im)),(Q(1),-Q(1,3)))

f1,f2=model(1),model(2)
assert len(f1)==len(f2)==6 and f1!=f2
assert f1[0]==f2[0]==1
assert all((-1)**i*f1[i]>0 and (-1)**i*f2[i]>0 for i in range(6))
k,d=3,5
v1=Q(2*(1+1),d*k**4)
v2=Q(2*(1+4),d*k**4)
assert v1==Q(4,405) and v2==Q(2,81) and v2-v1==Q(2,135)
print('R605_POLY_A_COEFFS',*[str(x) for x in f1])
print('R605_POLY_B_COEFFS',*[str(x) for x in f2])
print('R605_ENERGIES',v1,v2,'difference',v2-v1)
print('R605_AUXILIARY_OBSERVER_PAIR_COUNTEREXAMPLE_PASS')

def cat(n): return comb(2*n,n)//(n+1)
def H_catalan(k,s):
    return comb(2*k+1+s,2*s)*sum(comb(s-1,2*q)*4**q*cat(k-q)
        for q in range(min(k,(s-1)//2)+1))
def H_signed(k,s):
    r=2*k+1
    def coeff(deg):
        return sum(comb(r-s,q)*comb(2*s,deg-2*q)
            for q in range(r-s+1) if 0<=deg-2*q<=2*s)
    return comb(r+s,2*s)*(coeff(r)-coeff(r-1))

n=0
for kk in range(2,9):
    dd=2*kk-1
    H2=H_signed(kk,2)
    assert H2==H_catalan(kk,2)==comb(2*kk+3,4)*cat(kk)
    for j in range(dd+1):
        h=H_signed(kk,j+2)
        assert h==H_catalan(kk,j+2)
        a=Q(h,H2*kk**(2*j))
        assert a>0 and H2*kk**(2*j)*a==h
        n+=1
print('R605_NATIVE_SIGNED_TO_CATALAN_CHECK',n,'identities k=2..8')
print('R605_ALL_EXACT_TESTS_PASS')
