#!/usr/bin/env python3
"""Exact author-side original hypergeometric counterexamples for composite q=6m+1.

The original source sum and cutoff are unchanged. The prime-only D25
supercongruence and its native benchmark are NOT disproved or verified here.
"""
from fractions import Fraction as Q
from math import factorial, gcd

def source_sum_by_recurrence(m):
    assert m >= 1
    R = Q(1)
    series = Q(0)
    for n in range(4*m+1):
        series += (6*n+12*m+1)*R
        if n < 4*m:
            R *= Q((4*m+2*n+1)*(3*n+1)*(3*n+2),
                   36*(n+1)*(2*m+n+1)*(4*m+n+1))
    A = Q(factorial(6*m), 3**(6*m)*factorial(2*m)**3)
    return A*series

def source_sum_by_factorials(m):
    A = Q(factorial(6*m), 3**(6*m)*factorial(2*m)**3)
    result = Q(0)
    for n in range(4*m+1):
        R = Q(factorial(4*m+2*n)*factorial(2*m)**2*factorial(3*n),
              216**n*factorial(2*m+n)**2*factorial(4*m+n)*factorial(n)**2)
        result += (6*n+12*m+1)*R
    return A*result

def residue(x, mod):
    if gcd(x.denominator, mod) != 1:
        raise ValueError("denominator is not invertible")
    return x.numerator*pow(x.denominator, -1, mod)%mod

def valuation(x, prime):
    numerator, denominator = x.numerator, x.denominator
    order = 0
    while numerator%prime == 0:
        order += 1
        numerator //= prime
    while denominator%prime == 0:
        order -= 1
        denominator //= prime
    return order

def certificate(m):
    q = 6*m+1
    modulus = q**3
    original = source_sum_by_recurrence(m)
    factorial = source_sum_by_factorials(m)
    assert original == factorial, ("independent expression mismatch", m)
    target = Q(q*4**(q-1), 3**(q-1))
    difference = original-target
    assert gcd(difference.denominator, q) == 1
    return (
        m,q,residue(original,modulus),
        residue(target,modulus),residue(difference,modulus)
    ), difference

def verify():
    # Every example stays in the actual prescribed 13/19 (mod 24) classes.
    in_class = [
        (14,85,(5,17),563125,95710,467415),
        (15,91,(7,13),140777,74620,66157),
        (19,115,(5,23),945875,505885,439990),
        (22,133,(7,19),466431,786828,2032240),
        (31,187,(11,17),5070505,1103487,3967018),
    ]
    for m,q,factors,s,t,d in in_class:
        row, delta = certificate(m)
        assert row == (m,q,s,t,d), (m,row)
        assert q%24 in (13,19) and d%q==0 and d%(q*q)!=0
        assert all(valuation(delta,ell)==1 for ell in factors)
        print("TARGET_CLASS_COMPOSITE", row, "prime factors",factors,
              "prime-adic orders",[valuation(delta,ell) for ell in factors])
    # Secondary non-target diagnostics, explicitly distinct from the target.
    extra = [(4,25,1275,4400,12500),
             (8,49,49784,4165,45619),
             (9,55,88825,54945,33880)]
    for m,q,s,t,d in extra:
        row,delta=certificate(m)
        assert row==(m,q,s,t,d)
        print("NON_TARGET_COMPOSITE",row)
    assert valuation(certificate(4)[1],5)==5
    assert valuation(certificate(8)[1],7)==4
    print("PASS: 8/8 exact finite composite examples, original recurrence",
          "== factorial sum; NOT prime-only D25 proof or native benchmark")

if __name__ == "__main__":
    verify()
