#!/usr/bin/env python3
"""216 middle-shell two-digit reflection, exact modular checker. AUTHOR-side."""
from math import comb
import json

def primes_upto(n):
    return [p for p in range(7,n+1)
            if all(p%d for d in range(2,int(p**0.5)+1))]

def check(p):
    assert p%6==1 and p>=7
    mod=p**3; m=p*p; h=(p-1)//2; J=(p-7)//6
    low_end=(p-1)//3; s=(p+1)//2; L=(2*p-1)//3
    def a(k):
        return comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)%mod
    def b(k):
        return comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,mod)%mod
    def inv(x):
        assert x%p!=0
        return pow(x,-1,m)
    q2=((pow(2,p-1,m)-1)//p)%p
    q6=((pow(6,p-1,m)-1)//p)%p
    eps=pow(6,h,p)
    assert eps in (1,p-1)
    eps=1 if eps==1 else -1
    gamma=(3+2*q2-3*q6*pow(2,-1,p))%p
    top=a(h)//p
    assert top% m==(-2*eps*(1+p*gamma))%m
    q=1; q0=1; D=0; mid_units=0; signed_mid=0; coeff=[]
    for j in range(J+1):
        k=h-j; aj=a(k)
        assert aj%p==0 and aj%(p*p)!=0
        actual=aj//p
        assert actual%m==top*q%m
        assert q==q0*(1+p*D)%m
        signed_mid=(signed_mid+(6*k+1)*actual)%m
        mid_units=(mid_units+(3*p-2-6*j)*top*q)%m
        coeff.append(q)
        if j<J:
            den=(p-2*j-2)*(3*p-6*j-7)*(3*p-6*j-5)
            q=q*18*(p-2*j-1)**3*inv(den)%m
            q0=q0*9*(2*j+1)**3*inv((j+1)*(6*j+5)*(6*j+7))%m
            D=(D-3*pow(2*j+1,-1,p)+pow(2*j+2,-1,p)+
                 3*pow(6*j+5,-1,p)+3*pow(6*j+7,-1,p))%p
    assert mid_units==signed_mid
    # 72*P(theta) with P(theta)=theta*(theta-p/2)*
    # (theta-1/6-p/2)*(theta+1/6-p/2).
    for j in range(1,J+1):
        P=j*(2*j-p)*(6*j-1-3*p)*(6*j+1-3*p)
        assert (P*coeff[j]-144*j*(j-1-h)**3*coeff[j-1])%m==0
    boundary=(-2*(J+1)*(J-h)**3*coeff[-1])%m
    low=sum((6*k+1)*a(k) for k in range(low_end+1))%mod
    mid=sum((6*k+1)*a(k) for k in range(low_end+1,h+1))%mod
    high=sum((6*k+1)*a(k) for k in range(s,L+1))%mod
    Vh=sum((8*k+1)*b(k) for k in range(h+1))%mod
    W=sum((6*k+1)*a(k) for k in range(p))%mod
    assert all(a(k)==0 for k in range(L+1,p))
    assert mid==p*mid_units%mod and high%(p*p)==0
    assert W==(low+mid+high)%mod and (low-Vh)%p==0
    bottom=((low-Vh)%mod)//p
    upper=high//(p*p)
    residual=(bottom+mid_units+p*upper)%m
    assert residual==((W-Vh)%mod)//p
    if p%24 in (13,19):
        assert residual==0
    return dict(p=p,J=J,top_unit=top%m,gamma=gamma,
                middle_div_p=mid_units,bottom_div_p=bottom,
                upper_div_p2=upper,operator_endpoint=boundary,
                lift_residual=residual)

if __name__=="__main__":
    rows=[check(p) for p in primes_upto(997) if p%6==1]
    assert len(rows)==80
    print(json.dumps(dict(schema="D25_216_TWO_DIGIT_BOUNDARY_CHECK_V1",
        checked=len(rows),all_assertions="PASS",
        representatives=[r for r in rows if r["p"] in
        (7,13,19,67,139,373,997)]),indent=2))
