#!/usr/bin/env python3
"""Exact original-coefficient checks for D25 bottom-band p-adic two-jet transport.
Author-side portable calculation; not an H0/B0 native benchmark or Result admission.
"""
import json
from fractions import Fraction
from math import comb, factorial


def primes_up_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for q in range(2, int(n ** 0.5) + 1):
        if sieve[q]:
            sieve[q*q::q] = b'\x00' * ((n - q*q)//q + 1)
    return [q for q in range(5, n + 1) if sieve[q]]


def finite_unit(p):
    assert p % 6 == 1
    m = (p - 1)//6
    h = 3*m
    modulus = p**3
    inverse = lambda d: pow(d % modulus, -1, modulus)
    c, L, S = 1, 0, 0
    A0, A1, A2, B = 0, 0, 0, 0
    for n in range(2*m + 1):
        weight = 6*n + 1
        direct_a = comb(2*n, n)**2 * comb(3*n, n) * inverse(216**n) % modulus
        lower_expanded = c * (1 - p*L + (p*p*inverse(2))*(L*L - S)) % modulus
        assert direct_a == lower_expanded, (p, n, direct_a, lower_expanded)
        A0 = (A0 + weight*c) % modulus
        A1 = (A1 + weight*c*L) % modulus
        A2 = (A2 + weight*c*(L*L-S)) % modulus
        B = (B + weight*direct_a) % modulus
        if n < 2*m:
            x = inverse(2*(3*m-n))
            y = inverse(3*(2*m-n))
            z = 2*inverse(3*(4*m-n)) % modulus
            L = (L+x+y+z) % modulus
            S = (S+x*x+y*y+z*z) % modulus
            c = c*(-3*m+n)*(-2*m+n)*(-4*m+n)*inverse(2*(n+1)**3) % modulus
    V = sum((8*k+1)*comb(2*k,k)**2*comb(4*k,2*k)*inverse(2304**k)
            for k in range(h+1)) % modulus
    represented = (A0-p*A1+p*p*inverse(2)*A2) % modulus
    assert B == represented, (p, 'bottom sum', B, represented)
    if p%24 in (13, 19):
        assert (A0-V)%p == 0
        D_original = ((B-V)%modulus)//p
        D_twojet = (((A0-V)%modulus)//p-A1+p*inverse(2)*A2)%(p*p)
        assert D_original == D_twojet, (p, D_original, D_twojet)
    else:
        D_original = D_twojet = None
    return dict(p=p,m=m,A0_mod_p3=A0,A1_mod_p3=A1,A2_mod_p3=A2,
                B_mod_p3=B,V_mod_p3=V,D_original_mod_p2=D_original,
                D_twojet_mod_p2=D_twojet)


def rational_check(p):
    m=(p-1)//6
    for n in range(2*m+1):
        a = Fraction(comb(2*n,n)**2*comb(3*n,n),216**n)
        c = Fraction(1,2**n*factorial(n)**3)
        for r in range(n):
            c *= (-3*m+r)*(-2*m+r)*(-4*m+r)
        factors=Fraction(1)
        for r in range(n):
            factors *= (1-Fraction(p,2*(3*m-r)))*(1-Fraction(p,3*(2*m-r)))*(1-Fraction(2*p,3*(4*m-r)))
        assert a == c*factors, (p,n)


def main():
    results=[finite_unit(p) for p in primes_up_to(997) if p%6==1]
    rational_check(13);rational_check(19)
    targets=[r for r in results if r['p']%24 in (13,19)]
    assert len(results)==80 and len(targets)==45, (len(results),len(targets))
    report={
      'schema':'ENTERPRISE_MATH_D25_PORTABLE_TWO_JET_CHECK_V1',
      'scientific_input_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
      'task':'RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT',
      'classification':'AUTHOR_EXACT_FINITE_VERIFIED_UNREVIEWED_NOT_ADMITTED',
      'native_H0_B0_benchmark':'NOT_EXECUTED',
      'prime_ceiling':997,'all_p_1_mod_6_count':len(results),
      'target_p_13_19_mod_24_count':len(targets),
      'check_assertions':'ALL_PASSED',
      'independent_fraction_product_primes':[13,19],
      'examples':[r for r in results if r['p'] in (13,19,37,43,67,139,211,373)],
      'target_remainders':[{k:r[k] for k in ('p','D_original_mod_p2','D_twojet_mod_p2')} for r in targets]
    }
    with open('20261106_onhour_d25_bottom_parametric_two_jet_results.json','w') as f:
        json.dump(report,f,indent=2,ensure_ascii=False)
    print(json.dumps({k:v for k,v in report.items() if k not in ('target_remainders','examples')},ensure_ascii=False))
    for v in report['examples']:
        print(v)


if __name__=='__main__':
    main()
