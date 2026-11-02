#!/usr/bin/env python3
"""2026-11-02 D25: exact p-local Cauchy/truncation carry, independent integer checks.
Author-side exact modular verification; not the native H0/B0 experiment.
"""
from fractions import Fraction


def primes_upto(n):
    sieve = bytearray(b'\x01')*(n+1)
    sieve[:2] = b'\x00\x00'
    for q in range(2,int(n**0.5)+1):
        if sieve[q]:
            sieve[q*q::q] = b'\x00'*((n-q*q)//q+1)
    return [p for p in range(2,n+1) if sieve[p]]


def coeffs(p):
    """Original source A_m=binom(2m,m)^2 binom(3m,m)/216^m,
    B_j=binom(2j,j)/8^j, computed in Z/(p^2)."""
    d = p*p
    A, B = [1]*p, [1]*p
    for k in range(1,p):
        inv_k = pow(k,-1,d)
        A[k] = A[k-1]*(2*k-1)*(3*k-2)*(3*k-1)*pow(36,-1,d)*pow(inv_k,3,d)%d
        B[k] = B[k-1]*(2*k-1)*pow(4,-1,d)*inv_k%d
    return A,B


def check_formal_identity(n_max=11):
    """Direct rational n<=n_max coefficient crosscheck vs Le Lan 2026 (3.2)."""
    # signed generalized binomial (-u choose n) = (-1)^n (u)_n / n!
    def poch_over_fact(u, n):
        val=Fraction(1)
        for k in range(n):
            val *= (u+k)/(k+1)
        return val
    aa=[]; bb=[]; cc=[]
    for n in range(n_max+1):
        bb.append(poch_over_fact(Fraction(1,2),n))
        cc.append(poch_over_fact(Fraction(1,2),n)*poch_over_fact(Fraction(1,3),n)*poch_over_fact(Fraction(2,3),n)/Fraction(1))
        # cc = / n!^3 already via each independent poch_over_fact
        raw=Fraction(0)
        for k in range(n+1):
            raw += poch_over_fact(Fraction(1,3),k)*poch_over_fact(Fraction(1,6),k)*poch_over_fact(Fraction(2,3),n-k)*poch_over_fact(Fraction(5,6),n-k)
        converted=sum(bb[n-m]*cc[m] for m in range(n+1))
        assert raw==converted,(n,raw,converted)
        aa.append(raw)
    return len(aa)


def check_prime(p):
    assert p>3 and p%24 in (13,19)
    d=p*p
    A,B=coeffs(p)
    r=(p-1)//6
    F=sum(A)%d
    F1=sum(m*A[m] for m in range(p))%d
    S=(F+6*F1)%d
    Bs=sum(B)%d
    B1=sum(j*B[j] for j in range(p))%d
    # Piecewise moment prefix makes the original Cauchy triangle O(p) to read.
    pref0=[0]*(p+1);pref1=[0]*(p+1)
    for j in range(p):
        pref0[j+1]=(pref0[j]+B[j])%d
        pref1[j+1]=(pref1[j]+j*B[j])%d
    C=0;Hdirect=0
    C0=C1=H0=H1=0
    for m in range(p):
        C+=A[m]*((3*m-1)*pref0[p-m]+3*pref1[p-m])
        Hdirect+=A[m]*((3*m-1)*(pref0[p]-pref0[p-m])+3*(pref1[p]-pref1[p-m]))
        C0+=A[m]*pref0[p-m]
        C1+=A[m]*(m*pref0[p-m]+pref1[p-m])
        H0+=A[m]*(pref0[p]-pref0[p-m])
        H1+=A[m]*(m*(pref0[p]-pref0[p-m])+pref1[p]-pref1[p-m])
    C%=d;Hdirect%=d
    C0%=d;C1%=d;H0%=d;H1%=d
    assert C==(3*C1-C0)%d and Hdirect==(3*H1-H0)%d
    assert (C0+H0)%d==F*Bs%d
    assert (C1+H1)%d==(F1*Bs+F*B1)%d
    # Exact convolution factorization and truncation boundary.
    assert (C+Hdirect)%d == ((-Bs+3*B1)*F+3*Bs*F1)%d
    # Mod-p CM double zero is a separately checked premise for each test prime.
    assert F%p==0 and F1%p==0, (p,F%p,F1%p)
    assert Bs%p==p-1 and B1%p==(p-1)*pow(2,-1,p)%p
    assert (C+Hdirect+pow(2,-1,d)*S)%d==0, (p,C,Hdirect,S)
    # Source-local valuation: low 216 index and high central-binomial tail.
    Hlow=0
    for m in range(1,2*r+1):
        Hlow+=A[m]*((3*m-1)*(pref0[p]-pref0[p-m])+3*(pref1[p]-pref1[p-m]))
    Hlow%=d
    assert Hlow==Hdirect,(p,Hlow,Hdirect)
    assert Hdirect%p==0
    # Reflection of one carry across the p/2 boundary.
    ker = ker0 = ker1 = 0
    invsum=0; indexed=0
    for m in range(1,2*r+1):
        u = -pow((4*m*B[m])%p,-1,p)%p
        assert B[p-m]%p == 0
        assert (B[p-m]//p)%p == u, (p,m,(B[p-m]//p)%p,u)
        invsum=(invsum+u)%p
        indexed=(indexed+m*u)%p
        ker0=(ker0+A[m]*invsum)%p
        ker1=(ker1+A[m]*(m*invsum-indexed))%p
        ker=(ker+A[m]*((3*m-1)*invsum-3*indexed))%p
    assert ker==Hdirect//p,(p,ker,Hdirect//p)
    assert H0%p==H1%p==0
    assert ker0==H0//p and ker1==H1//p
    assert (3*ker1-ker0)%p==ker
    # Distinct numerical predictions: mother mod p^2, Le Lan/Sun p^2, carry.
    assert S==p,(p,'S',S)
    assert C==p,(p,'C',C)
    assert ker==(-3*pow(2,-1,p))%p,(p,'kernel',ker)
    assert ker0==0 and ker1==(-pow(2,-1,p))%p, (p,'moment-kernel',ker0,ker1)
    assert C0==0 and (3*C1-p)%d==0, (p,'C-moments',C0,C1)
    assert F==0, (p,'F modulus p^2',F)
    return (p, p%24, F//p, F1//p, S, C, Hdirect//p, ker,ker0,ker1,C0,C1)


def main():
    n=check_formal_identity(12)
    print('exact rational coefficient identity: n=0..12, 13 coefficients PASS')
    cases=[p for p in primes_upto(3000) if p%24 in (13,19)]
    targets={13,19,37,43,61,373,1171,2963}
    table=[]
    for p in cases:
        row=check_prime(p)
        if p in targets:table.append(row)
    print('target primes <=3000:',len(cases),'class13',sum(p%24==13 for p in cases),'class19',sum(p%24==19 for p in cases))
    print('all target primes: original Cauchy triangle, valuation truncation, reflected 0th/1st moment kernels, CM premise, S,C mod p^2, H1/p=-1/2, H0=0 mod p^2 PASS')
    print('sample p class F/p F1/p S_mod_p2 C_mod_p2 H/p kernel K0 K1 C0 C1')
    for row in table: print(*row)
    print('END PASS; arithmetic exact modulo p^2; no native experiment or formal checker claimed')

if __name__=='__main__':main()
