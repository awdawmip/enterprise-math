#!/usr/bin/env python3
"""D25 AF4 original-coefficient grade interface: integer modular recurrence."""
import json
from math import factorial
def vf(k,p):
    s=0
    while k:
        k//=p;s+=k
    return s
def calculate(p):
    m=p**4; a=c=1; w=[0]*4; v=[0]*4
    for n in range(p):
        ga=vf(2*n,p)+vf(3*n,p)-5*vf(n,p)
        gc=vf(4*n,p)-4*vf(n,p)
        assert 0<=ga<4 and 0<=gc<4
        w[ga]=(w[ga]+(6*n+1)*a)%m
        v[gc]=(v[gc]+(8*n+1)*c)%m
        if n+1<p:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,m)%m
            c=c*(4*n+1)*(4*n+3)*(2*n+1)*pow(288*(n+1)**3,-1,m)%m
    chi=1 if pow((-3)%p,(p-1)//2,p)==1 else -1
    low=(w[0]+w[1]-2*(v[0]+v[1])+p*chi)%m
    mid=(w[2]-2*v[2])%m
    high=(w[3]-2*v[3])%m
    assert low%p**2==mid%p**2==0 and high%p**3==0
    ell=low//p**2; b=mid//p**2; t=high//p**3
    ell0,ell1=ell%p,ell//p
    b0,b1=b%p,b//p
    carry=(ell0+b0)//p
    assert (ell0+b0)%p==0
    assert (ell1+b1+carry+t)%p==0
    assert (sum(w)-2*sum(v)+p*chi)%m==0
    return dict(p=p,modulus_p4=m,chi=chi,W_grades=w,V_grades=v,
         low_mod_p4=low,grade2_mod_p4=mid,grade3_mod_p4=high,
         ell=ell,b=b,t=t,digits=dict(ell0=ell0,ell1=ell1,b0=b0,b1=b1,carry=carry),
         balance=(ell+b+p*t)%(p**2))
if __name__=='__main__':
    samples=[calculate(p) for p in [13,19,37,43,73,373]]
    print(json.dumps(samples,indent=2))
