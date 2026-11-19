"""Independent finite checks. The Euler-product numerical illustrations deliberately truncate primes."""
from fractions import Fraction as F
from math import cos, exp, expm1, fsum, gcd, log, pi, sin
from pathlib import Path
import cmath
import json
import mpmath as mp


def primes(n):
    sieve = bytearray(b'\1') * (n+1)
    for k in range(2, int(n**0.5)+1):
        if sieve[k]:
            sieve[k*k::k] = bytes((n-k*k)//k+1)
    return [k for k in range(2,n+1) if sieve[k]]


def exact_checks():
    bound=240
    h=[F(1)]*(bound+1)
    g=[F(1)]*(bound+1)
    for p in primes(bound):
        Hp=F(p*p,p*p-1)  # a=1 at this algebraic check only
        for j in range(p,bound+1,p):
            h[j]*=0 if j%(p*p)==0 else Hp
            g[j]*=0 if j%(p**3)==0 else -Hp if j%(p*p)==0 else Hp-1
    for n in range(1,bound+1):
        assert h[n]==sum(g[d] for d in range(1,n+1) if n%d==0)
    ntests=0
    for q in range(2,145):
        for t in (1,2,3,4,7,15,32,100):
            # A rational relaxation of 1+log(t) is 1+ceil(log2(t)).
            total=sum(min(t,F(q,2*min(j,q-j))) for j in range(1,q))
            assert total <= q*(1+(t-1).bit_length())
            ntests+=1
    return {'dirichlet_coefficient_identities':bound,'rational_truncated_period_tests':ntests}


def spectral(a,q,ps):
    h=[1.0]*(q+1)
    for p in ps:
        if p>q:break
        hp=(1-p**-2)/(1-p**(-1-a))**2
        for k in range(p,q+1,p):
            h[k]*=hp
        for k in range(p*p,q+1,p*p):
            h[k]=0.
    c=1/float(mp.zeta(1+a))
    return c*c*fsum(h[k]/k**(2*a) for k in range(2,q+1))/12


def illustration():
    ps=primes(1_000_000)
    logprod=0.; derivA=0.; logderG=0.
    for p in ps:
        k=p**-1.5;l=log(p)
        local=1+1/p-2*k
        logprod+=log((1-1/p)*local)
        derivA+=2*l*k*(1-k)/local
        hp=(1-p**-2)/(1-k)**2
        logderG+=l*(1/(p-1)-hp/(p+hp))
    astar=exp(logprod)/12
    c=1/float(mp.zeta(1.5))
    bstar=astar*(float(mp.euler)+logderG)-c*c/12
    rows=[]
    for q in (1000,10000,100000):
        L=log(q)
        for eta in (-1.,0.,1.):
            a=.5+eta/(2*L); f=-expm1(-eta)/eta if eta else 1.
            expected=astar*L*f+bstar-0.5*astar*derivA*expm1(-eta)
            actual=spectral(a,q,ps)
            rows.append({'Q':q,'eta':eta,'actual':actual,'two_term_approximation':expected})
    return {'Euler_product_prime_cutoff':ps[-1],'Astar_approximation':astar,
            'Bstar_approximation':bstar,'rows':rows}


def block_statistics(X=4096):
    a=.5;c=1/float(mp.zeta(1+a));N=2*X
    ps=primes(N);R=[1.]*(N+1)
    for p in ps:
        for n in range(p,N+1,p):R[n]*=1-p**-a
    B=[-1-c/2]
    for n in range(1,N+1): B.append(B[-1]+R[n]-c)
    Q=round(X**(1/3));spec=spectral(a,Q,ps)
    errors=[];inner_sq=0.
    for q in range(2,Q+1):
        fac=[p for p in ps if p<=q and q%p==0]
        if any(q%(p*p)==0 for p in fac):continue
        b=c*(-1)**len(fac)
        for p in fac:b/=p**(1+a)-1
        for r in range(1,q):
            if gcd(r,q)>1:continue
            u=cmath.exp(-2j*pi*r/q)
            # direct DFT on all actual unshifted B_n of the requested block
            bhat=sum(B[n]*u**(n%q) for n in range(X+1,N+1))/X
            inner_sq+=abs(bhat)**2
            errors.append(abs((1-u)*bhat-b))
    return {'X':X,'Q':Q,'c_a':c,'actual_raw_mean_square':fsum(v*v for v in B[X+1:])/X,
            'actual_finite_projection_coefficient_norm_squared':inner_sq,
            'arithmetic_spectral_energy':spec,'maximum_frequency_error':max(errors)}

if __name__=='__main__':
    print(json.dumps({'exact':exact_checks(),'floating_euler_illustration':illustration(),
                      'floating_anchored_source_fixture':block_statistics()},indent=2))
