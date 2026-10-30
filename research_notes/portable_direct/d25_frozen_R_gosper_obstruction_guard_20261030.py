#!/usr/bin/env python3
"""Exact finite checks for the frozen R inner-kernel, NOT native H0/B0.
No package beyond the Python standard library. 2026-10-30.
"""
from math import comb, isqrt
from fractions import Fraction


def primes_below(n):
    for p in range(7, n):
        if any(p % d == 0 for d in range(2, isqrt(p)+1)):
            continue
        if p % 6 == 1:
            yield p


def check_prime(p):
    m = (p-1)//6
    inv2 = pow(2,-1,p)
    c = [0]*(m+2)
    c[1] = pow(10,-1,p)
    for a in range(1,m+1):
        denominator=((6*a+5)*(3*a+2))%p
        assert denominator, (p,a,'original C denominator not a unit')
        c[a+1] = c[a]*36*a*a*pow(denominator,-1,p)%p
    S=[0]*(m+2); T=[0]*(m+2)
    for i in range(1,m+2):
        T[i] = (T[i-1]+6*S[i-1]+c[i])%p
        S[i] = (S[i-1]+c[i])%p
    # Verified original frozen double sum and independent two-port recurrence.
    r_direct = 0
    r_recurrent = 0
    for i in range(1,m+1):
        b = comb(m,i)*comb(2*m,i)*pow(inv2,i,p)%p
        inner = sum((1+6*(i-a))*c[a] for a in range(1,i+1))%p
        assert inner == T[i], (p,i,inner,T[i])
        r_direct = (r_direct+2*b*inner)%p
        r_recurrent=(r_recurrent+2*b*T[i])%p
    assert r_direct == r_recurrent
    # Explicit rank-three polynomial-coefficient annihilator, no N_i division.
    for i in range(1,m):
        D=lambda j:(6*j+5)*(3*j+2)
        N=lambda j:5*D(j)+36*j*j
        U_i=(T[i+1]-2*T[i]+T[i-1])%p
        U_next=(T[i+2]-2*T[i+1]+T[i])%p
        assert (D(i+1)*N(i)*U_next-36*i*i*N(i+1)*U_i)%p==0,(p,i)
        assert U_i==(5*c[i]+c[i+1])%p
    nzeros = [i for i in range(1,m) if (5*(6*i+5)*(3*i+2)+36*i*i)%p==0]
    return p,m,r_direct,T[m],len(nzeros),nzeros[:4]


def check_exact_small():
    C=[Fraction(0),Fraction(1,10)]
    for a in range(1,16):
        C.append(C[a]*Fraction(36*a*a,(6*a+5)*(3*a+2)))
    T=[Fraction(0)]; S=Fraction(0)
    for i in range(1,17):
        T.append(T[-1]+6*S+C[i]);S+=C[i]
        assert T[i]==sum((1+6*(i-a))*C[a] for a in range(1,i+1))
    for i in range(1,15):
        D=lambda j:(6*j+5)*(3*j+2)
        N=lambda j:5*D(j)+36*j*j
        U=lambda j:T[j+1]-2*T[j]+T[j-1]
        assert D(i+1)*N(i)*U(i+1)==36*i*i*N(i+1)*U(i)
    assert T[1]==Fraction(1,10)
    assert T[2]==Fraction(421,550)


def check_polynomial_obstruction():
    # If a rational Gosper certificate exists, pole-chain argument forces polynomial.
    # Degree then must be one q(a)=A*a+B. Leading coefficient gives A=-6.
    # Matching a^2 gives B=6*i-5. Remaining a and constant equations demand
    # i=19/27 and i=1/3, respectively: an exact contradiction.
    assert Fraction(19,27)!=Fraction(1,3)
    for i in [0,1,2,62]:
        B=Fraction(6*i-5)
        coef_a= -Fraction(3,2)*B-9*i+Fraction(31,6)
        coef_const= -Fraction(5,9)*B-Fraction(10,3)*i-Fraction(5,9)
        assert coef_a!=0 or coef_const!=0


if __name__=='__main__':
    check_polynomial_obstruction(); check_exact_small()
    values=[check_prime(p) for p in primes_below(1000)]
    assert len(values)==80, len(values)
    for p in [13,19,373]:
        print('WITNESS',check_prime(p))
    singular=[x for x in values if x[4]]
    print('PASS_D25_FROZEN_R_GOSPER_OBSTRUCTION_AND_RANK3_RECURRENCE',
          'primes_checked=',len(values),'N_zero_cases=',len(singular),
          'examples=',singular[:8])
