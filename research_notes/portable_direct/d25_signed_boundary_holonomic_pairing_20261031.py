#!/usr/bin/env python3
"""Portable author-side exact verifier, D25 signed R; NOT native H0/B0.

No floating point. Computes the original signed overdegree jet independently
of the new rational generating-function/short-transfer calculation.
"""
from math import comb, isqrt
from fractions import Fraction


def primes_upto(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for d in range(2, isqrt(limit) + 1):
        if sieve[d]:
            for k in range(d*d, limit+1, d):
                sieve[k] = False
    return [p for p in range(7, limit + 1) if sieve[p] and p % 6 == 1]


def c_coefficients(p):
    """Explicit characteristic-zero recurrence reduced in F_p, up to l."""
    l = (p - 1) // 6
    c = [0] * (l+1)
    c[1] = pow(10, -1, p)
    for a in range(1, l):
        c[a+1] = c[a] * 36 * a*a * pow((6*a+5)*(3*a+2), -1, p) % p
    return c


def g_coefficients(p):
    l = (p-1)//6
    return [comb(l,i)*comb(2*l,i)*pow(2,-i,p)%p for i in range(l+1)]


def direct_original_signed_double_sum(p, c, g):
    l = (p-1)//6
    return (2 * sum(g[i] * sum((1+6*(i-a))*c[a] for a in range(1, i+1))
                    for i in range(1,l+1))) % p


def finite_green_transfer(p,c,g):
    """Compute inner Green convolution with two moment registers: O(l)."""
    l = (p-1)//6
    count, first_moment, R = 0, 0, 0
    q=[0]*(l+1)
    for i in range(1,l+1):
        count = (count + c[i]) % p
        first_moment = (first_moment + i*c[i]) % p
        q[i] = ((1+6*i)*count-6*first_moment) % p
        R = (R + 2*g[i]*q[i]) % p
    for i in range(1,l+1):
        assert (q[i]-2*q[i-1]+(q[i-2] if i>=2 else 0)
                -c[i]-5*c[i-1]) % p == 0
    return R,q


def hypergeometric_terminal_check(p,c,g):
    l=(p-1)//6
    inv6=pow(6,-1,p); inv3=pow(3,-1,p)
    f=[10*c[n+1]%p for n in range(l)]
    assert f[0]==1
    for n in range(1,l):
        left=n*(n+5*inv6)*(n+2*inv3)*f[n]
        right=2*n**3*f[n-1]
        assert (left-right)%p==0
    terminal=(-2*l**3*f[-1])%p
    assert terminal == (-20*l**3*c[l])%p
    inv2=pow(2,-1,p)
    for n in range(1,l+2):
        current=g[n] if n<=l else 0
        prev=g[n-1]
        assert (n*n*current - inv2*(n-1-l)*(n-1-2*l)*prev)%p==0
    return terminal


def original_jet_overdegree(p):
    """Original high-degree parameter t^2 jet w_k, modulo p."""
    l=(p-1)//6
    x,y,z=1,0,0
    u=[1];w=[0]
    inv6=pow(6,-1,p); inv3=pow(3,-1,p);inv2=pow(2,-1,p)
    for k in range(1,p):
        a,b=k-1-l,k-1-2*l
        xa=x*a%p;ya=(y*a+x*inv6)%p;za=(z*a+y*inv6)%p
        ik=pow(k*k,-1,p)
        x=xa*b*ik
        y=(ya*b+xa*inv3)*ik%p
        z=(za*b+ya*inv3)*ik%p
        u.append(x);w.append(z)
    assert all(not u[i] for i in range(l+1,p))
    acc=0
    for i in range(1,l+1):
        for k in range(p-i,p):
            acc += 2*(1+6*(i+k))*u[i]*w[k]*pow(inv2,i+k,p)
    return acc%p


def check(p):
    c=c_coefficients(p)
    g=g_coefficients(p)
    R_naive=direct_original_signed_double_sum(p,c,g)
    R_short,q=finite_green_transfer(p,c,g)
    terminal=hypergeometric_terminal_check(p,c,g)
    R_jet=original_jet_overdegree(p)
    assert R_naive==R_short==R_jet,(p,R_naive,R_short,R_jet)
    for i in range(1,(p-1)//6+1):
        assert q[i]==sum((1+6*(i-a))*c[a] for a in range(1,i+1))%p
    return (p,R_naive,terminal)


def rational_symbolic_crosscheck(max_l=8):
    """Independent exact-Q coefficient extraction and inhomogeneous ODE."""
    for l in range(1,max_l+1):
        c=[Fraction(0)]*(l+1)
        c[1]=Fraction(1,10)
        for a in range(1,l):
            c[a+1]=c[a]*2*a*a/((a+Fraction(5,6))*(a+Fraction(2,3)))
        g=[Fraction(comb(l,i)*comb(2*l,i),2**i) for i in range(l+1)]
        kernel=[1+6*d for d in range(l+1)]
        q=[sum(c[a]*kernel[i-a] for a in range(1,i+1)) for i in range(l+1)]
        naive=2*sum(g[i]*q[i] for i in range(1,l+1))
        ct=sum(2*g[i]*c[a]*kernel[i-a]
               for i in range(l+1) for a in range(1,i+1))
        assert naive==ct
        f=[10*c[n+1] for n in range(l)]
        assert f[0]==1
        for n in range(1,l):
            assert n*(n+Fraction(5,6))*(n+Fraction(2,3))*f[n] == 2*n**3*f[n-1]
        assert -2*l**3*f[-1] == -20*l**3*c[l]
        for i in range(1,l+1):
            assert i*i*g[i] == Fraction((i-1-l)*(i-1-2*l),2)*g[i-1]
        assert Fraction((l-l)*(l-2*l),2)*g[-1]==0
    return max_l


def main():
    rational_tests=rational_symbolic_crosscheck()
    tested=[check(p) for p in primes_upto(1200)]
    target=[r for r in tested if r[0]%24 in (13,19)]
    anchors=[r for r in tested if r[0] in (13,19,37,67,373)]
    assert anchors==[(13,0,3),(19,12,11),(37,11,28),(67,21,48),(373,196,259)], anchors
    print('exact rational characteristic-zero l range:',1,'to',rational_tests)
    print('p=1 (mod 6), 7<=p<=1200:',len(tested))
    print('frozen classes p=13,19 (mod24):',len(target))
    print('anchors (p, signed_R modp, C-terminal modp):',anchors)
    print('PASS_D25_SIGNED_R_HOLONOMIC_PAIRING_AND_SOURCE_JET_EXACT')


if __name__ == '__main__':
    main()
