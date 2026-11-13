#!/usr/bin/env python3
"""Exact author-side Cauchy boundary certificate; NOT a native H0/B0 run."""
from fractions import Fraction
from math import comb, factorial
import json

def verify(p):
    m=p**3
    inv36=pow(36,-1,m); inv4=pow(4,-1,m); inv2=pow(2,-1,m)
    c=[1];u=[1]
    for k in range(p-1):
        d=pow(k+1,-1,m)
        c.append(c[-1]*(3*k+1)*(3*k+2)*(2*k+1)*inv36*pow(d,3,m)%m)
        u.append(u[-1]*(2*k+1)*inv4*d%m)
    U=[0]
    for z in u:U.append((U[-1]+z)%m)
    def summand(k):
        r=p-k
        return c[k]*((6*k+1)*U[r]-3*(2*r-1)*u[r-1])
    t=(2*p+2)//3
    S=sum(summand(k) for k in range(p))*inv2%m
    S_sparse=sum(summand(k) for k in range(t))*inv2%m
    assert S==S_sparse
    W=sum((6*k+1)*c[k] for k in range(p))%m
    if p<=373:
        triangle=sum((3*n-1)*sum(u[j]*c[n-j] for j in range(n+1)) for n in range(p))%m
        assert triangle==S
    for k in range(p):
        v=(3*k)//p+(2*k)//p
        assert c[k]%(p**min(v,3))==0
        if v<3: assert c[k]//p**v%p!=0
    E=(S-W)%m
    return dict(p=p,T=t,W_mod_p3=W,S_mod_p3=S,E_mod_p3=E,E_over_p2_mod_p=E//p**2 if E%p**2==0 else None)

def rational(N):
    u=[Fraction(comb(2*j,j),8**j) for j in range(N)]
    c=[Fraction(factorial(3*k)*factorial(2*k),216**k*factorial(k)**5) for k in range(N)]
    U=[Fraction(0)]
    for z in u:U.append(U[-1]+z)
    a=sum((3*(j+k)-1)*u[j]*c[k] for j in range(N) for k in range(N-j))
    b=sum(c[k]*((6*k+1)*U[N-k]-3*(2*(N-k)-1)*u[N-k-1])/2 for k in range(N))
    assert a==b

if __name__=="__main__":
    for N in range(1,14):rational(N)
    rows=[verify(p) for p in [13,19,37,43,211,373,997,1213]]
    assert rows[1]["E_over_p2_mod_p"]==9
    assert rows[5]["E_over_p2_mod_p"]==61
    print(json.dumps(dict(status="PASS",author_only=True,formal_check=False,native_H0B0=False,rational_checks=13,rows=rows),indent=2))
