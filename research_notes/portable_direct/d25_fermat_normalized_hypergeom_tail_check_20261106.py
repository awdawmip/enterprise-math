#!/usr/bin/env python3
"""Exact integer check of D25 2304 two-digit signed tail and p-deformed boundary."""
from math import factorial, gcd
import json

def primes_to(n):
    return [p for p in range(5, n+1) if all(p%d for d in range(2,int(p**0.5)+1))]

def inv(x, m):
    assert gcd(x,m)==1
    return pow(x % m,-1,m)

def compute(p):
    h=(p-1)//2; L=(2*p-1)//3; K0=2*L//3
    K=K0-int(2*L-3*K0==1); J=h-K-1; m=p*p
    q3=((pow(3,p-1,m)-1)//p)%p
    q2=((pow(2,p-1,m)-1)//p)%p
    q48=((pow(48,p-1,m)-1)//p)%p
    H=sum(inv(i,p) for i in range(1,h+1))%p
    W=((factorial(p-1)+1)//p)%p
    half=((factorial(h)**4-1)//p)%p
    beta_old=(2*W-2+half+q48)%p; beta=(q3-2)%p
    assert beta_old==beta
    assert H==(-2*q2)%p
    assert half==2*(H-W)%p
    assert q48==(q3+4*q2)%p
    top=(factorial(2*p-2)//p)*inv(pow(48,p-1,m)*pow(factorial(h),4,m),m)%m
    top_clean=(-(1+2*p)*inv(pow(3,p-1,m),m))%m
    assert top==top_clean
    q=qp=1; D=0; S0=S1=Sp=direct=0; vals=[]
    for j in range(max(J+1,0)):
        vals.append(qp); w=8*j+3
        S0=(S0+w*q)%m
        S1=(S1+q*(w*(D-beta)-4))%p
        Sp=(Sp+(4*p-w)*qp)%m
        k=h-j
        bk=(factorial(4*k)//p)*inv(pow(2304,k,m)*pow(factorial(k),4,m),m)%m
        assert bk==top*qp%m,(p,j)
        direct=(direct+(8*k+1)*bk)%m
        if j<J:
            q=q*18*(2*j+1)**3*inv((j+1)*(4*j+3)*(4*j+5),m)%m
            D=(D-4*inv(2*j+1,p)+2*sum(inv(4*j+r,p) for r in range(2,6)))%p
            d=1
            for r in range(2,6): d*=2*p-4*j-r
            qp=qp*144*(p-2*j-1)**4*inv(d,m)%m
            assert qp==q*(1+p*D)%m,(p,j)
    def P(n):
        return n*(4*n-2*p-1)*(2*n-p)*(4*n-2*p+1)
    for n in range(1,max(J+1,0)):
        assert (P(n)*vals[n]*inv(32,m)-9*n*(n-1-h)**3*vals[n-1])%m==0,(p,n)
    endpoint=(-9*(J+1)*(J-h)**3*vals[-1])%m if J>=0 else 0
    assert direct==(S0+p*S1)%m==top_clean*Sp%m,(p,direct,S0,S1)
    return dict(p=p,J=J,q3_mod_p=q3,beta=beta,S0_mod_p2=S0,
                S1_mod_p=S1,V_tail_over_p_mod_p2=direct,
                operator_endpoint_mod_p2=endpoint)

if __name__=="__main__":
    out=[compute(p) for p in primes_to(997)]
    print("PASS",len(out),"primes 5..997, zero failed assertions")
    for r in out:
        if r["p"] in (13,19,67,139,373,997):
            print(r)
