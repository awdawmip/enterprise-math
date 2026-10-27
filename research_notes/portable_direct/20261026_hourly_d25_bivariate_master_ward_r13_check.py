#!/usr/bin/env python3
"""Independent exact rational / p-adic checks for the two-parameter finite-rank Clausen Green identity."""
from fractions import Fraction as F


def mod_inv(x, q):
    return pow(x % q, -1, q)


def run(p, t, s, q=None):
    m=(p-1)//6
    N=2*m-1
    if q is None:
        half=F(1,2)
        def coefficients(z):
            f=[F(1)]
            for r in range(1,p):
                ratio=(r-1-m-z)*(r-1-2*m-2*z)/(r*(r-F(p,2)-3*z))
                f.append(f[-1]*ratio)
            return f
        def norm(z):return z
    else:
        half=mod_inv(2,q)
        def coefficients(z):
            f=[1]
            for r in range(1,p):
                factor=(r-1-m-z)*(r-1-2*m-2*z)
                denom=r*(r-p*half-3*z)
                f.append(f[-1]*factor*mod_inv(denom,q)%q)
            return f
        def norm(z):return z%q
    ft=coefficients(t);fs=coefficients(s)
    a0={n:0 for n in range(-N,N+2)}
    a1=a0.copy()
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            n=ell-j
            v=ft[j]*fs[p-ell]
            a0[n]+=v
            a1[n]+=j*v
    count=0
    for n in range(-N,N+1):
        C=(p-n)*(p*half-n)
        A=6*m-2*n
        B=-18*m*m+9*m*n-n*n
        lhs=(p-2*n-3*(t+s))*a1[n]+(-C+3*s*(p-n))*a0[n]
        rhs=(A-3*(t+s))*a1[n+1]+(B+4*m*t+(14*m-3*n)*s+2*(t*t-s*s))*a0[n+1]
        if n>=0:
            edge=2*(m+t)**2*fs[p-n-1]-(6*m*m-8*m*s+2*s*s)*ft[2*m-n]*fs[4*m]
        else:
            edge=(20*m*m-14*m*s+2*s*s)*ft[-n]*fs[p-1]+(2*m*t-2*t*t)*ft[2*m]*fs[p-(2*m+n+1)]
        assert norm(lhs-rhs-edge)==0,('master',p,n,q,t,s,lhs,rhs,edge)
        count+=1
    return count


def primes():
    return [p for p in range(7,212) if p%6==1 and
            all(p%d for d in range(2,int(p**.5)+1))]+[733]


def main():
    exact=0
    for m in range(1,5):
        p=6*m+1
        exact+=run(p,F(1,7),F(-2,11))
    modular=0
    for p in primes():
        q=p**3
        modular+=run(p,p,2*p,q)
        modular+=run(p,3*p,-p,q)
    print('PASS rational:',exact,'all-rank bivariate identities, including composite p=25')
    print('PASS modular:',modular,'all-rank identities over 23 primes and 2 probe pairs mod p^3')


if __name__=='__main__':main()
