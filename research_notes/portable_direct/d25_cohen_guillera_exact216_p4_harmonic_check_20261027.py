#!/usr/bin/env python3
"""Author-side verification: Cohen–Guillera row 30, L(-3,3-p) and p4 harmonic digit.
This does NOT prove the conjectural supercongruence or execute native H0/B0.
No dependencies outside the Python standard library.
"""
from math import comb, factorial
from fractions import Fraction
from functools import reduce

PRIMES = (7, 11, 13, 17, 19, 23, 37, 43, 73, 373)

def poch(a, n):
    return reduce(lambda v, j: v * (a + j), range(n), Fraction(1))

def verify_exact_terms():
    for n in range(15):
        original = Fraction(comb(2*n, n)**2 * comb(3*n, n), 216**n)
        row30 = poch(Fraction(1,2), n)*poch(Fraction(1,3), n)*poch(Fraction(2,3), n)/(factorial(n)**3 * 2**n)
        assert original == row30, (n, original, row30)

def W_recurrence(p):
    q = p**4
    a, total = 1, 0
    for n in range(p):
        total = (total + (6*n+1)*a) % q
        if n+1 < p:
            a = (a*(2*n+1)*(3*n+1)*(3*n+2)
                 * pow(36*(n+1)**3, -1, q)) % q
    return total

def W_binomial(p):
    q = p**4
    inv216 = pow(216, -1, q)
    return sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)
               * pow(inv216,n,q) for n in range(p)) % q

def B_n_at_one_third(n, p):
    # Bernoulli recursion: (n+1)B_n = - sum_{k<n} binom(n+1,k) B_k.
    # Only n<=p-2 is used; no denominator divisible by p occurs.
    b = [1]
    for j in range(1,n+1):
        b.append(-sum(comb(j+1,k)*b[k] for k in range(j))*pow(j+1,-1,p)%p)
    one_third=pow(3,-1,p)
    return sum(comb(n,k)*b[k]*pow(one_third,n-k,p) for k in range(n+1))%p

def L_negative3_mod_p(p):
    n=p-2
    return (-2*pow(3,n-1,p)*B_n_at_one_third(n,p)*pow(n,-1,p))%p

def H2(n,p):
    return sum(pow(j,-2,p) for j in range(1,n+1))%p

def run():
    verify_exact_terms()
    for p in PRIMES:
        w=W_recurrence(p)
        assert w==W_binomial(p),p
        sign=1 if p%3==1 else -1
        assert (w-sign*p)%(p**3)==0,p
        d=((w-sign*p)%(p**4))//p**3
        l=L_negative3_mod_p(p)
        t=(2*p+1)//3 if p%3==1 else (p+1)//3
        assert (3*t-1)%p==0
        assert l==(-2*pow(9,-1,p)*H2(t-1,p))%p,p
        cutoff=(p-1)//3 if p%3==1 else (p-2)//3
        predicted=(((-5 if p%3==1 else 5)*pow(6,-1,p))*H2(cutoff,p))%p
        assert d == (-15*pow(4,-1,p)*l)%p == predicted,p
        print(f"p={p} sign={sign:+d} fourth_digit={d} L={l} H2={H2(cutoff,p)}")
    print("PASS_ROW30_EXACT_OBJECT_AND_L_MODP_IDENTITY; P4_CONJECTURE_FINITE_REGRESSION_ONLY")

if __name__=="__main__":
    run()
