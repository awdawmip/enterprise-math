#!/usr/bin/env python3
"""Independent exact check: grade-1 W216 shorter 3F2 first p-jet, p=6m+1."""
from math import factorial, comb

PRIMES=(7,13,19,31,37,43,61,67,73,109,157,181,373)

def inv(a,mod): return pow(a%mod,-1,mod)
def frac(a,b,mod): return a*inv(b,mod)%mod

def check(p):
    assert p>3 and p%6==1
    m=(p-1)//6
    n=(p+2)//3
    md=p*p
    md3=p**3
    assert n==2*m+1
    # Wilson quotient is an integer. Calculate modulo p (not replace by a random Wilson lift).
    w=(factorial(p-1)+1)//p%p
    u0 = frac(-2*factorial(2*n),factorial(n)**5*216**n,md)
    u0 = u0*(1+p*(frac(3,2,md)-w))%md
    direct0= frac(comb(2*n,n)**2*comb(3*n,n),216**n,md3)
    assert direct0%p==0
    assert u0==direct0//p%md, (p,'seed',u0,direct0//p%md)
    g=1;S=0;weighted=0
    for j in range(m):
        k=n+j
        uj= u0*g*(1+p*S)%md
        direct=frac(comb(2*k,k)**2*comb(3*k,k),216**k,md3)
        assert direct%p==0, (p,k)
        assert uj==direct//p%md, (p,j,'firstjet',uj,direct//p)
        weighted=(weighted+(2*p+5+6*j)*uj)%md
        if j+1<m:
            ratio=frac(3*(6*j+7)*(j+1)*(3*j+4),4*(3*j+5)**3,md)
            E=(frac(2,6*j+7,md)+frac(1,3*(j+1),md)+frac(1,3*j+4,md)-frac(3,3*j+5,md))%md
            g=g*ratio%md
            S=(S+E)%md
    full=sum((6*k+1)*frac(comb(2*k,k)**2*comb(3*k,k),216**k,md3) for k in range(2*m+1,3*m+1))%md3
    assert full%p==0
    assert weighted==full//p%md
    return {'p':p,'m':m,'U0':u0,'grade1_div_p_mod_p2':weighted,'mod_p':weighted%p,'Wilson_w':w}

if __name__=='__main__':
    for p in PRIMES:print(check(p))
    print('PASS: 13 selected primes, coefficientwise /p modulo p^2 and exact weighted sum')
