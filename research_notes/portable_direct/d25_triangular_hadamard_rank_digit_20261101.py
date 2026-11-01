#!/usr/bin/env python3
"""Exact integer/modular witnesses for the D25 triangular Clausen/Hadamard observer.
Pure standard-library arithmetic; this is NOT a native H0/B0 computation.
"""
from fractions import Fraction
from math import isqrt


def primes_to(limit):
    for n in range(7, limit + 1):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n


def three_series(p):
    mod = p**3
    u = v = b = 1
    us, vs, bs = [], [], []
    for n in range(p):
        us.append(u)
        vs.append(v)
        bs.append(b)
        if n + 1 < p:
            k = n + 1
            u = u * (6*n + 1)*(3*n + 1)*pow(18*k*k, -1, mod) % mod
            v = v * (2*n + 1)*(3*n + 1)*(3*n + 2)*pow(18*k**3, -1, mod) % mod
            b = b * (8*n + 1)*(8*n + 3)*pow(64*k*k, -1, mod) % mod
    return us, vs, bs


def check_prime(p):
    mod = p**3
    us, vs, bs = three_series(p)
    inv2 = pow(2, -1, mod)
    powers = [1]
    for _ in range(2*p-2):
        powers.append(powers[-1]*inv2%mod)
    a = [u * powers[n] % mod for n,u in enumerate(us)]
    s = sum(a) % mod
    d = sum(n*x for n,x in enumerate(a)) % mod
    w = sum((6*n+1)*vs[n]*powers[n] for n in range(p)) % mod
    low = 0
    high = 0
    for i in range(p):
        for j in range(p):
            term = (6*(i+j)+1)*a[i]*a[j]
            if i+j < p: low += term
            else: high += term
    low %= mod
    high %= mod
    assert low == w, (p, "exact triangular Clausen mismatch")
    assert (s*s+12*s*d-high-w)%mod == 0, (p,"full square-tail mismatch")
    assert high % (p*p) == 0, (p,"Clausen high tail valuation")

    # Exact source h_1=27/32, point lambda=1/9.
    # q(z)=z-3/32 satisfies (T_H q)(1/9)=0.
    q0 = -Fraction(3,32)
    assert q0 + Fraction(27,32)/9 == 0
    lin = Fraction(109,16)
    quad = Fraction(2665,1024)
    eps = next(e for e in [1,2,3] if
               (e*lin.numerator*pow(lin.denominator,-1,p)
                +e*e*quad.numerator*pow(quad.denominator,-1,p))%p)
    delta = (eps*lin.numerator*pow(lin.denominator,-1,p)
             +eps*eps*quad.numerator*pow(quad.denominator,-1,p))%p

    outcome = {"p":p,"residue24":p%24,"W_mod_p3":w,"tail_digit":high//(p*p),
               "Y_mod_p":s%p,"delta_eps":eps,"delta_Q_mod_p":delta}
    if p%24 in (13,19):
        # This zero is verified here in the stated finite domain only.
        assert s%p == 0, (p,"candidate Hasse zero has counterexample")
        alpha=(s//p)%(p*p)
        a0, a1 = alpha%p, alpha//p
        d0,d1=d%p,(d//p)%p
        c=high//(p*p)
        first=(12*a0*d0)%p
        carry=(12*a0*d0-1)//p if first==1 else None
        second=None if carry is None else (carry + 12*(a1*d0+a0*d1)+a0*a0-c)%p
        reconstructed=(p*(12*alpha*d+p*(alpha*alpha-c)))%mod
        assert reconstructed == w,(p,"digit identity")
        outcome.update({"A0":a0,"A1":a1,"D0":d0,"D1":d1,
                        "carry":carry,"digit1":first,"digit2_residual":second,
                        "W_equals_p_mod_p3":w==p})
    return outcome


def det_mod_p(matrix, p):
    n = len(matrix)
    a = [[v%p for v in row] for row in matrix]
    det = 1
    for i in range(n):
        k = next((k for k in range(i,n) if a[k][i]),None)
        if k is None: return 0
        if k != i:
            a[i],a[k] = a[k],a[i]
            det = -det
        pivot = a[i][i]
        det = det*pivot%p
        inv = pow(pivot,-1,p)
        for k in range(i+1,n):
            factor = a[k][i]*inv%p
            if factor:
                for j in range(i+1,n):
                    a[k][j] = (a[k][j]-factor*a[i][j])%p
                a[k][i] = 0
    return det%p


def check_det(p):
    inv2 = pow(2,-1,p)
    m = [[((6*(i+j)+1)*pow(inv2,i+j,p) if i+j<p else 0)%p
          for j in range(p)] for i in range(p)]
    measured = det_mod_p(m,p)
    expected = ((-1 if ((p*(p-1)//2)%2) else 1)
                *pow(6*p-5,p,p)*pow(inv2,p*(p-1),p))%p
    assert measured == expected !=0, (p,measured,expected)
    return measured


if __name__ == '__main__':
    selected = []
    all_tested = []
    target = []
    for p in primes_to(400):
        if p%6 != 1: continue
        rec = check_prime(p)
        all_tested.append(p)
        if p%24 in (13,19): target.append(rec)
        if p in (7,13,19,31,37,43,61,73,109,139,157,193,373):
            selected.append(rec)
    det_checks = {p:check_det(p) for p in (7,13,19,31,37,43,61)}
    print('EXACT MODULAR TESTS: {} primes p<=400, p=1 mod 6; {} target classes 13/19'.format(len(all_tested),len(target)))
    print('CLAUSEN triangular W, full signed high-tail, p^2 divisibility: PASS')
    print('RANK determinant checks (mod p):',det_checks)
    print('Explicit B(1/9)-fiber nonconstancy: PASS for all tested primes')
    print('TARGET finite sample W=p mod p^3: {}/{} (not a general proof)'.format(
        sum(x['W_equals_p_mod_p3'] for x in target),len(target)))
    print('Selected exact modular records:')
    for row in selected: print(row)
