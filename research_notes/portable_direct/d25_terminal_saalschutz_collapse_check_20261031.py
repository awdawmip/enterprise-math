"""Exact Saalschutz collapse / third-digit terminal gamma certificate for D25.
No floating point and no claim of native Source/Task authorization.
"""
from math import comb
from fractions import Fraction


def primes_up_to(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for n in range(2, int(limit ** .5) + 1):
        if sieve[n]:
            sieve[n*n::n] = b'\x00' * ((limit-n*n)//n+1)
    return [n for n in range(2, limit+1) if sieve[n]]


def S_direct(l, N):
    return sum(comb(l,i)*comb(2*l,i)*comb(N+i,3*l) for i in range(l+1))


def H(n, power=1):
    return sum((Fraction(1, j**power) for j in range(1,n+1)), Fraction(0))


def harmonic_identity(l):
    M=3*l
    old=-H(M)+sum((Fraction((-1)**i * comb(l,i)*comb(2*l,i),i*comb(M,i))
                    for i in range(1,l+1)), Fraction(0))
    return old == -H(l)-H(2*l)


def trial():
    for l in range(1,15):
        M=3*l
        for N in [M,M+1,M+2,5*l,6*l,6*l+1,8*l+3]:
            assert S_direct(l,N)==comb(N,l)*comb(N,2*l), (l,N)
        assert harmonic_identity(l)
    ps=[p for p in primes_up_to(1200) if p%6==1]
    witnesses={}
    for p in ps:
        l=(p-1)//6
        M=3*l
        S=S_direct(l,p-1)
        assert S==comb(p-1,l)*comb(p-1,2*l)
        pp=p*p; ppp=pp*p
        Ap2=(sum(pow(j,-1,pp) for j in range(1,l+1))+
             sum(pow(j,-1,pp) for j in range(1,2*l+1)))%pp
        Bp=(sum(pow(j,-2,p) for j in range(1,l+1))+
            sum(pow(j,-2,p) for j in range(1,2*l+1)))%p
        inv2=pow(2,-1,p)
        gamma=((-1)**l*pow(18*S,-1,ppp))%ppp
        pred_gamma=(1+p*Ap2+p*p*(Ap2*Ap2+Bp)*inv2)*pow(18,-1,ppp)%ppp
        assert gamma==pred_gamma,(p,gamma,pred_gamma)
        normalizedS=((-1)**l*S)%ppp
        predS=(1-p*Ap2+p*p*(Ap2*Ap2-Bp)*inv2)%ppp
        assert normalizedS==predS
        if p in {7,13,19,37,67,283,373}:
            witnesses[p]=(l,Ap2%p,Bp,gamma, normalizedS)
    print('PASS_D25_SAALSCHUTZ_TERMINAL_GAMMA_ALL_JETS',
          'exact_ell=1..14', 'primes=94', 'p<=1200')
    for p,v in witnesses.items():
        print('WITNESS',p,'ell,A,B,gamma_mod_p3,normS_mod_p3=',v)

if __name__=='__main__':
    trial()
