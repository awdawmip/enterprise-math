#!/usr/bin/env python3
"""Independent exact p^2 original W216 vs source-aligned CM0 second-carry check."""
from math import comb

def check(p):
    r=(p-1)//6
    M=p*p
    z=pow(2,-1,M)
    ell=[comb(r,k)*comb(2*r,k)%M for k in range(r+1)]
    square=[0]*p
    for j,v in enumerate(ell):
        for k,w in enumerate(ell):
            square[j+k]=(square[j+k]+v*w)%M
    a=[1]*p
    for k in range(p-1):
        a[k+1]=a[k]*(2*k+1)*(3*k+1)*(3*k+2)*pow(18*(k+1)**3,-1,M)%M
    assert all((a[k]-square[k])%p==0 for k in range(p))
    RA=[((a[k]-square[k])%M)//p for k in range(p)]
    zz=1
    W=src=0
    for k in range(p):
        W=(W+(6*k+1)*a[k]*zz)%M
        src=(src+(6*k+1)*RA[k]*zz)%p
        zz=zz*z%M
    zz=1
    ell0=j=0
    for k,v in enumerate(ell):
        ell0=(ell0+v*zz)%M
        j=(j+k*v*zz)%M
        zz=zz*z%M
    assert ell0%p==0
    g=(ell0//p)%p
    j%=p
    predicted=(12*g*j+src)%p
    assert W%p==0 and predicted==W//p%p
    return dict(p=p,g=g,j=j,q=src,CMterm=12*g*j%p,W_div_p=W//p,predicted=predicted)

if __name__=="__main__":
    for p in (13,19,37,43,373,1171):
        print(check(p))
