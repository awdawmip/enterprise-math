#!/usr/bin/env python3
"""Exact rational CM-24 period-bridge and bounded prime-class check.

Author-side portable algebra/computation; does not execute native H0/B0.
"""
from fractions import Fraction
from math import isqrt


def q2(a=0, b=0):
    return (Fraction(a), Fraction(b))


def add(u, v):
    return (u[0]+v[0], u[1]+v[1])


def neg(u):
    return (-u[0], -u[1])


def mul(u, v):
    return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])


def inv(u):
    norm=u[0]*u[0]-2*u[1]*u[1]
    return (u[0]/norm, -u[1]/norm)


def div(u, v):
    return mul(u, inv(v))


def power(u, n):
    out=q2(1)
    while n:
        if n&1:
            out=mul(out,u)
        u=mul(u,u)
        n//=2
    return out


def cm_j_from_quadratic_transform(x):
    # x=4*t/(1+t)^2; j(t)=64*(4-3*x)^3/(x^2*(1-x)).
    return div(mul(q2(64),power(add(q2(4),neg(mul(q2(3),x))),3)),
               mul(power(x,2),add(q2(1),neg(x))))


def check_exact_cm_identity():
    xlo=q2(Fraction(1,2),Fraction(-1,3))
    xhi=q2(Fraction(1,2),Fraction(1,3))
    assert mul(q2(4),mul(xlo,add(q2(1),neg(xlo))))==q2(Fraction(1,9))
    assert mul(q2(4),mul(xhi,add(q2(1),neg(xhi))))==q2(Fraction(1,9))
    jp=cm_j_from_quadratic_transform(xlo)
    jm=cm_j_from_quadratic_transform(xhi)
    assert jp==q2(2417472,1707264)
    assert jm==q2(2417472,-1707264)
    assert add(jp,jm)==q2(4834944)
    assert mul(jp,jm)==q2(14670139392)
    return jp,jm


def relevant_primes(limit):
    sieve=bytearray(b'\1')*(limit+1)
    sieve[:2]=b'\0\0'
    for d in range(2,isqrt(limit)+1):
        if sieve[d]:
            sieve[d*d:limit+1:d]=b'\0'*((limit-d*d)//d+1)
    return [p for p in range(5,limit+1) if sieve[p] and p%8==5]


def jacobi_value_and_derivative(p):
    # J_p(z) = sum_{j=0}^q binom(q,j)binom(3q+1,j)(z/9)^j.
    q=(p-5)//8
    inverses=[0]*(q+1)
    if q:
        inverses[1]=1
    for k in range(2,q+1):
        inverses[k]=(p-p//k)*inverses[p%k]%p
    r9=pow(9,-1,p)
    ck=1
    J=1
    dJ=0
    for k in range(q):
        invk=inverses[k+1]
        ck=ck*(q-k)*(3*q+1-k)*r9*invk*invk%p
        J=(J+ck)%p
        dJ=(dJ+(k+1)*ck)%p
    return q,J,dJ


def legendre(a,p):
    k=pow(a%p,(p-1)//2,p)
    return 0 if k==0 else 1 if k==1 else -1


def check_prime_classes(limit=20000):
    primes=relevant_primes(limit)
    hits={5:0,13:0}
    samples={}
    for p in primes:
        q,J,dJ=jacobi_value_and_derivative(p)
        ls=legendre(-6,p)
        if p%24==13:
            assert ls==-1 and J==0 and dJ!=0, (p,q,J,dJ)
        else:
            assert p%24==5 and ls==1 and dJ==0 and J!=0, (p,q,J,dJ)
        assert legendre(2,p)==-1
        hits[p%24]+=1
        if p in (5,13,29,37,53,61,373):
            samples[p]={'q':q,'J':J,'dJ':dJ,'CM_split_character':ls}
    return len(primes),hits,samples


if __name__=='__main__':
    jp,jm=check_exact_cm_identity()
    n,hits,samples=check_prime_classes()
    print('EXACT_CM_PASS j_plus=%s+%s*sqrt2; j_minus=%s-%s*sqrt2' % (jp[0],jp[1],jm[0],-jm[1]))
    print('EXACT_H_MINUS24=X^2-4834944*X+14670139392')
    print('FINITE_CLASS_PASS primes=%d classes=%s limit=20000' % (n,hits))
    for p,row in samples.items():print('CASE',p,row)
