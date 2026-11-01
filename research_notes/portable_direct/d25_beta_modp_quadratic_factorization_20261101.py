#!/usr/bin/env python3
"""D25: exact finite-mod-p quadratic factorization and p-adic first-carry ports.

All-prime theorem is in companion manuscript; this checks polynomial coefficient
identities and independent original Gauss/Legendre recurrences, not native H0/B0.
"""
from math import comb


def primes_to(bound):
    sieve = [True] * (bound + 1)
    sieve[:2] = [False, False]
    for d in range(2, int(bound ** 0.5) + 1):
        if sieve[d]:
            for i in range(d*d, bound+1, d):
                sieve[i] = False
    return [p for p in range(5, bound+1) if sieve[p]]


def quad_mul(x, y, mod):
    a,b=x; c,d=y
    return ((a*c+2*b*d) % mod, (a*d+b*c) % mod)


def quad_pow(x, n, mod):
    out=(1,0)
    while n:
        if n&1:
            out=quad_mul(out,x,mod)
        x=quad_mul(x,x,mod); n//=2
    return out


def quad_eval(coeff,t,mod):
    out=(0,0)
    for a in coeff[::-1]:
        out=quad_mul(out,t,mod)
        out=((out[0]+a)%mod,out[1])
    return out


def modular_series(p,kind,mod):
    a,b,zden=(1,3,576) if kind=='beta' else (1,3,16)
    scale=8 if kind=='beta' else 4
    out=[1]
    for k in range(p-1):
        out.append(out[-1]*(scale*k+a)*(scale*k+b)*pow(zden*(k+1)**2,-1,mod)%mod)
    return out


def polynomial_factor_test(p):
    assert p%8==5
    a,b,n=(5*p-1)//8,(7*p-3)//8,(p-1)//4
    beta=[comb(a,k)*comb(b,k)%p for k in range(a+1)]
    U=[(-1)**k*comb(n,k)*comb(n+k,k)%p for k in range(n+1)]
    G=[0]*(p+n+1)
    for k,v in enumerate(beta):
        z=4**k*v%p
        for j in range(k,2*k+1):
            G[j]=(G[j]+z*(-1)**(j-k)*comb(k,j-k))%p
    want=[0]*(p+n+1)
    for k,v in enumerate(U):
        want[k]=v
        want[p+k]=-2*v%p
    assert G==want,(p,'modp polynomial identity failed')
    return p


def lifted_ports(p):
    assert p%8==5
    mod=p*p
    t=(pow(2,-1,mod), -pow(3,-1,mod)%mod)
    U=quad_eval(modular_series(p,'leg',mod),t,mod)
    t_pow=quad_pow(t,p,mod)
    multiplier=((1-2*t_pow[0])%mod,-2*t_pow[1]%mod)
    prod=quad_mul(multiplier,U,mod)
    G=sum(modular_series(p,'beta',mod))%mod
    diff=((G-prod[0])%mod,(-prod[1])%mod)
    assert diff[0]%p==0 and diff[1]%p==0,(p,diff)
    defect=(diff[0]//p,diff[1]//p)
    if p%24==13:
        assert U[0]%p==0 and U[1]%p==0,p
        U_first=(U[0]//p,U[1]//p)
        original_first=G//p
        first_factor=quad_mul(((1-2*pow(2,-1,p))%p, -2*pow(3,-1,p)%p),U_first,p)
        assert (first_factor[0]+defect[0])%p==original_first
        assert (first_factor[1]+defect[1])%p==0
        return (p,U_first,first_factor,defect,original_first)
    return (p,None,None,defect,G)


def main():
    ps=[p for p in primes_to(1000) if p%8==5]
    for p in ps:
        polynomial_factor_test(p)
    print('FULL_POLYNOMIAL_MOD_P_FACTORIZATION_PASS',len(ps),'primes <=1000 p=5 mod8')
    for p in [5,13,29,37,53,61,109,373]:
        print('p, Legendre first digit, multiplier first digit, defect, original beta:',lifted_ports(p))
    print('PASS; p^2 first-carry ports are finite observations, not an all-prime cancellation')


if __name__=='__main__':
    main()
