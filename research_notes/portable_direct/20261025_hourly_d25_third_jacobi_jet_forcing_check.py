#!/usr/bin/env python3
"""Exact author checker for third terminating Jacobi parameter jet, no extra dependencies."""
from fractions import Fraction
from math import factorial

def primes_upto(limit):
    for n in range(7,limit+1):
        if n%6==1 and all(n%d for d in range(2,int(n**0.5)+1)):
            yield n

def H(n,mod,power=1):
    return sum(pow(pow(j,power,mod),-1,mod) for j in range(1,n+1))%mod

def fact(n,mod):
    a=1
    for j in range(2,n+1):a=a*j%mod
    return a

def modular_check(p):
    m,q=(p-1)//6,p*p
    c=[1,0,0,0]
    for n in range(p-1):
        a=(n-m)*(n-2*m)
        b=-(3*n-4*m)
        inv=pow((n+1)**2,-1,q)
        c=[(a*c[k]+(b*c[k-1] if k>=1 else 0)+(2*c[k-2] if k>=2 else 0))*inv%q for k in range(4)]
    w,t=c[2],c[3]
    f=[fact(j,q) for j in (m,2*m,5*m-1,4*m-1,p-1)]
    w_fact=(2*(-1)**m*f[0]*f[1]*f[2]*f[3]*pow(f[4]**2,-1,q))%q
    lam=(H(m,q)-H(5*m-1,q)+2*H(2*m,q)-2*H(4*m-1,q))%q
    assert w==w_fact and t==w*lam%q,(p,"Taylor/factorial")
    k3=(-6*(20*m*m*t-14*m*w))%q
    s=(H(m+1,p,2)+2*H(2*m+1,p,2))%p
    assert k3%p==0
    predicted=p*(12*s-1782*pow(25,-1,p))%q
    assert k3==predicted,(p,"lift")
    point=k3*pow(2**p,-1,q)%q
    assert point==p*(6*s-891*pow(25,-1,p))%q,(p,"point")
    return p,k3,k3//p,point

def rational_check(p):
    m,N=(p-1)//6,p-1
    c=[Fraction(1),Fraction(0),Fraction(0),Fraction(0)]
    rows=[c[:]]
    for n in range(N):
        a,b=(n-m)*(n-2*m),-(3*n-4*m)
        c=[(a*c[k]+(b*c[k-1] if k>=1 else 0)+(2*c[k-2] if k>=2 else 0))/(n+1)**2 for k in range(4)]
        rows.append(c[:])
    w,t=rows[N][2],rows[N][3]
    w_fact=Fraction(2*(-1)**m*factorial(m)*factorial(2*m)*factorial(5*m-1)*factorial(4*m-1),factorial(N)**2)
    h=lambda n:sum((Fraction(1,j) for j in range(1,n+1)),Fraction(0))
    lam=h(m)-h(5*m-1)+2*h(2*m)-2*h(4*m-1)
    assert w==w_fact and t==w*lam
    k3=-6*(20*m*m*t-14*m*w)
    def coeff(order,n):
        return factorial(order)*rows[n][order] if 0<=n<=N else Fraction(0)
    for n in range(N+2):
        left=n*n*coeff(3,n)
        if n>=1:
            left-=(n-1-m)*(n-1-2*m)*coeff(3,n-1)
            left+=3*(3*(n-1)-4*m)*coeff(2,n-1)-12*coeff(1,n-1)
        assert left==(k3 if n==p else 0),(p,n)
    return p

if __name__=="__main__":
    checks=[rational_check(p) for p in (7,13,19,31,37,43)]
    cases=[modular_check(p) for p in [*primes_upto(373),1327,19963]]
    print("RATIONAL_DEGREE_P_PASS",checks)
    print("MODULAR_P2_PASS",len(cases))
    print("WITNESSES",[c for c in cases if c[0] in (7,13,19,373,1327,19963)])
