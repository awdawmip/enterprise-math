#!/usr/bin/env python3
"""Exact original W216 p^2-grade -> terminating hypergeometric companion.

Author-side mathematical certificate; no native H0/B0 operation or Source claim.
"""
import json
from math import comb, factorial


def primes_up_to(limit):
    flags = bytearray(b'\x01') * (limit + 1)
    flags[0:2] = b'\x00\x00'
    for d in range(2, int(limit**0.5) + 1):
        if flags[d]:
            flags[d*d:limit+1:d] = b'\x00' * (((limit-d*d)//d) + 1)
    return [p for p in range(7, limit + 1) if flags[p] and p % 6 == 1]


def original_w_grades(p):
    """Exact original binomial numerator, coefficients, p-adic grade, mod p^3."""
    assert p > 3 and p % 6 == 1
    q, inv216, pow216 = p**3, pow(216, -1, p**3), 1
    grades = [0, 0, 0, 0]
    for n in range(p):
        numerator = comb(2*n, n)**2 * comb(3*n, n)
        grade = 0
        while numerator % p == 0:
            numerator //= p
            grade += 1
        residue = (6*n+1)*numerator*pow(p, grade, q)*pow216 % q
        grades[min(grade, 3)] = (grades[min(grade, 3)]+residue) % q
        pow216 = pow216 * inv216 % q
    return grades


def original_v_grades(p):
    """Independent old V2304 binomial integer coefficients for layer contrast."""
    q, inv2304, power = p**3, pow(2304,-1,p**3), 1
    grades = [0, 0, 0, 0]
    for n in range(p):
        numerator = comb(4*n, 2*n) * comb(2*n, n)**2
        grade=0
        while numerator % p == 0:
            numerator //= p
            grade += 1
        residue=(8*n+1)*numerator*pow(p,grade,q)*power % q
        grades[min(grade,3)] = (grades[min(grade,3)]+residue)%q
        power=power*inv2304%q
    return grades


def companion(p):
    """Mod-p hypergeometric partner; all denominators are units, p=6m+1."""
    assert p > 3 and p % 6 == 1
    m = (p-1)//6
    kappa = factorial(3*m+2)*pow(factorial(3*m+1),-5,p) * pow(216,-(3*m+1),p) % p
    h, u = 0, 1
    inv2 = pow(2, -1, p)
    inv6 = pow(6, -1, p)
    for j in range(m):
        h = (h+(6*j+4)*u)%p
        if j+1 < m:
            r1=(6*j+5)*inv6%p
            r2=(6*j+7)*inv6%p
            den=((2*j+3)*inv2%p)**3 % p
            u = u*(j+1)*r1*r2*pow(2*den,-1,p)%p
    return {'p':p, 'm':m,'kappa_p':kappa,'companion_sum_mod_p':h,
            'W_grade2_over_p2_mod_p':kappa*h%p}


def main():
    explicit_primes=[7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373]
    examples=[]
    for p in explicit_primes:
        a=original_w_grades(p)
        c=companion(p)
        assert a[2] == p*p*c['W_grade2_over_p2_mod_p']
        assert a[3]==0
        assert sum(a)%(p**3) == sum(original_w_grades(p))%(p**3)
        examples.append({**c,'original_grade2_mod_p3':a[2], 'verified_equal':True})
    prime_scan=primes_up_to(10000)
    zeros=[p for p in prime_scan if companion(p)['W_grade2_over_p2_mod_p']==0]
    w=original_w_grades(373)
    v=original_v_grades(373)
    assert sum(w)%(373**3)==373
    assert sum(v)%(373**3)==373
    assert v[2]==0
    assert w[2] == 37008314
    assert companion(373)['W_grade2_over_p2_mod_p']==266
    payload={
        'scope':'AUTHOR_SIDE_EXACT_GRADE2_COMPANION_NOT_NATIVE_H0_B0_NOT_UNIVERSAL_W_V_PROOF',
        'theorem_domain':'prime p=6m+1>3; original full n=0..p-1',
        'verification':'18 exact original-binomial grade vs modular companion, 611-prime modular finite screening',
        'examples':examples,
        'finite_nonzero_screen':{'upper_bound':10000,'p_1_mod_6_count':len(prime_scan),'zero_count':len(zeros),'zero_primes':zeros},
        'p373':{'modulus':373**3,'W_grade_residues':w,'V_grade_residues':v,
                'W_minus_V_grade2_mod_p3':(w[2]-v[2])%(373**3),
                'companion':companion(373)}
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__=='__main__':
    main()
