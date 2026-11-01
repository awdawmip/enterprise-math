"""Exact independent split-Green residue and terminal-Gamma checks.

Distinguishes the Laurent form's two nonrational pieces from their rational sum;
not a native H0/B0 experiment or an all-prime D25 cancellation proof.
"""
from fractions import Fraction
from math import comb, factorial


def primes(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b'\0\0'
    for q in range(2, int(limit**.5) + 1):
        if sieve[q]:
            sieve[q*q::q] = b'\0' * (((limit - q*q) // q) + 1)
    return [p for p in range(7, limit+1) if sieve[p] and p % 6 == 1]


def exact_ell(ell):
    p = 6*ell + 1
    M = 3*ell
    u = [comb(ell, i)*comb(2*ell, i) for i in range(ell+1)]
    # The linear coefficient of (-ell+t/6)_k(-2ell+t/3)_k/(k!)^2
    # at k=2ell is obtained by differentiating its sole first-factor zero.
    v_last = Fraction((-1)**ell * factorial(ell)*factorial(ell-1), 6*factorial(2*ell))
    low_top = Fraction(ell, 3)*u[-1]*v_last
    assert low_top == Fraction((-1)**ell, 18)
    low_residue = (-1)**M * low_top
    assert low_residue == Fraction(1, 18)
    S = sum(u[i] * comb(p-1+i, M) for i in range(ell+1))
    assert S != 0
    gamma_from_residue = low_top / S
    # Independently derive gamma from last second-jet coefficient w_(p-1).
    w_last = Fraction((-1)**ell * factorial(ell)*factorial(2*ell)
                      *factorial(5*ell-1)*factorial(4*ell-1),
                      18*factorial(6*ell)**2)
    gamma_from_jet = 20*ell**2*w_last
    assert gamma_from_jet == gamma_from_residue
    terminal_residue = (-1)**M * (-gamma_from_jet*S)
    assert terminal_residue == -Fraction(1,18)
    return S, gamma_from_jet


def modular_gamma(p):
    ell = (p-1)//6
    fac=[1]*p
    for i in range(1,p):fac[i]=fac[i-1]*i%p
    # The factorial formula for w_(p-1), obtained from its exact double zero.
    numer = ((-1)**ell * fac[ell]*fac[2*ell]*fac[5*ell-1]*fac[4*ell-1])%p
    denom = 18 * fac[p-1]**2 %p
    w = numer * pow(denom,-1,p)%p
    gamma = (20*ell*ell*w)%p
    assert gamma == pow(18,-1,p), (p,ell,gamma)
    # Independent Lucas specialization: C(p-1+i,3ell) = 0 for 1<=i<=ell;
    # C(p-1,3ell)=(-1)^(3ell), all modulo p.
    if p<=1000:
        S = sum(comb(ell,i)*comb(2*ell,i)*comb(p-1+i,3*ell)
                for i in range(ell+1)) %p
        assert S == (-1)**ell %p
        assert gamma*S%p == (-1)**ell * pow(18,-1,p)%p
    return gamma


def main():
    for ell in range(1,9):
        exact_ell(ell)
    ps=primes(5000)
    assert len(ps)==330
    for p in ps:modular_gamma(p)
    for p in (7,13,19,37,67,373):
        print(f'ANCHOR p={p} gamma={modular_gamma(p)} inv18={pow(18,-1,p)}')
    print('PASS_D25_SPLIT_GREEN_LOG_RESIDUE_EXACT rational_ell=1..8 primes=330 gamma=inv18 residues=+1/18,-1/18')

if __name__=='__main__':main()
