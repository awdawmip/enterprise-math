#!/usr/bin/env python3
"""D25 p^2 terminal-gamma/harmonic correction guard.

AUTHOR-SIDE / NOT_ADMITTED; does not compute original native H0/B0.
All modular arithmetic is integer-exact. Proof is in companion MD.
"""
from math import comb, factorial


def primes_1mod6(limit):
    return [p for p in range(7, limit + 1) if p % 6 == 1 and
            all(p % d for d in range(2, int(p**.5)+1))]


def gamma_direct_factorial(p):
    """Independently calculate gamma=20*l*l*w_{p-1} (source factorial formula)."""
    l = (p-1)//6
    q=p*p
    numerator = 20*l*l*(-1)**l*factorial(l)*factorial(2*l)*factorial(5*l-1)*factorial(4*l-1)
    denominator = 18*factorial(6*l)**2
    return (numerator%q)*pow(denominator%q,-1,q)%q


def harmonic_correction(p):
    """Novel finite p-local harmonic witness: H_l=-H_3l+sum_i (-1)^i u_i/(i*C(3l,i))."""
    l=(p-1)//6
    M=3*l
    H=sum(pow(j,-1,p) for j in range(1,M+1))%p
    T=sum((-1)**i * comb(l,i)*comb(2*l,i)*pow(i*comb(M,i),-1,p)
          for i in range(1,l+1))%p
    return (-H+T)%p


def verify_prime(p):
    l=(p-1)//6
    M=3*l
    q=p*p
    sign=(-1)**l
    S=sum(comb(l,i)*comb(2*l,i)*comb(p-1+i,M) for i in range(l+1))%q
    h=harmonic_correction(p)
    assert S==sign*(1+p*h)%q, ('S_harmonic',p,S,h)
    gamma_from_exact_S = sign*pow(18*S,-1,q)%q
    gamma_from_factorial = gamma_direct_factorial(p)
    assert gamma_from_factorial==gamma_from_exact_S, ('gamma factor',p)
    gamma_lift=pow(18,-1,q)*(1-p*h)%q
    assert gamma_from_factorial==gamma_lift, ('gamma mod p2',p)
    # Constant gamma=1/18 introduces a p-divisible log residue.
    residue=(gamma_from_exact_S-pow(18,-1,q))*sign*S%q
    predicted=-p*h*pow(18,-1,q)%q
    assert residue==predicted, ('log residue',p,residue,predicted)
    return (p,l,h,gamma_lift,residue,residue//p)


def main():
    primes=primes_1mod6(1200)
    results=[verify_prime(p) for p in primes]
    assert len(primes)>80
    print('PASS_D25_TERMINAL_GAMMA_P2_HARMONIC_AND_LOG_RESIDUE',len(primes))
    for a in results:
        if a[0] in (7,13,19,37,67,103,373):
            print('p,ell,h,gamma_p2,residue_p2,residue/p',a)


if __name__=='__main__':
    main()
