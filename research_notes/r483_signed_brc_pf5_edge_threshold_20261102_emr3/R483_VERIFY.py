#!/usr/bin/env python3
"""R483 exact verification of the signed BRC right-edge PF5 determinant.

Standard library only; symbolic polynomial arithmetic over Q and raw coefficient
convolution over Z. No floats, external libraries, or model-semantic simulation.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial
import json
from pathlib import Path
import hashlib


def C(n, j):
    return comb(n, j) if n >= 0 and 0 <= j <= n else 0


def catalan(k):
    return comb(2 * k, k) // (k + 1)


def raw_H(k, t):
    r = 2 * k + 1
    if t < 2 or t > r:
        return 0
    return C(r + t, 2 * t) * sum(
        C(r - t, q) * (C(2 * t, r - 2 * q) - C(2 * t, r - 2 * q - 1))
        for q in range(r - t + 1)
    )


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    result = [Fraction(0) for _ in range(max(len(a), len(b)))]
    for i, v in enumerate(a):
        result[i] += v
    for i, v in enumerate(b):
        result[i] += v
    return trim(result)


def neg(a):
    return [-v for v in a]


def mul(a, b):
    ans = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                ans[i + j] += x * y
    return trim(ans)


def scale(a, c):
    return trim([x * c for x in a])


def prod_polys(pols):
    ret = [Fraction(1)]
    for p in pols:
        ret = mul(ret, p)
    return ret


def p_poly(t):
    if t < 2:
        return [Fraction(0)]
    terms = []
    for q in range((t - 1) // 2 + 1):
        factors = []
        for h in range(q):
            factors.extend(([-h, 1], [1 - h, 1]))
        canceled = set(range(1 - 2 * q, 1))
        for ell in range(2 - t, t + 2):
            if ell not in canceled:
                factors.append([ell, 2])
        terms.append(scale(prod_polys(factors), Fraction(C(t-1, 2*q) * 4**q, factorial(2*t))))
    result = [Fraction(0)]
    for item in terms:
        result = add(result, item)
    assert len(result) == 2*t + 1
    return result


def evaluate(poly, value):
    result = Fraction(0)
    for coeff in reversed(poly):
        result = result * value + coeff
    return result


def determinant_poly_5():
    vals = {t:p_poly(t) for t in range(2,8)}
    vals.update({0:[Fraction(0)],1:[Fraction(0)]})
    result = [Fraction(0)]
    count=0
    for perm in permutations(range(5)):
        inversions = sum(perm[i] > perm[j] for i in range(5) for j in range(i+1,5))
        factor = prod_polys([vals.get(3+i-perm[i], [Fraction(0)]) for i in range(5)])
        result = add(result, neg(factor) if inversions % 2 else factor)
        count += 1
    assert count==120
    return result


def integer_poly(*coefficients_ascending):
    return [Fraction(int(t)) for t in coefficients_ascending]


def to_json_number(x):
    assert x.denominator == 1
    return int(x.numerator)


def det_numeric(a):
    n=len(a)
    total=0
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        item=1
        for i in range(n):
            item *= a[i][perm[i]]
        total += -item if inversions%2 else item
    return total


def main():
    P5 = integer_poly(
        -1432864592, -5092612394, -8057900273, -7458198896,
        -4362096657, -1617117168, -342536356, -23083312,
        6684416, 1375232
    )
    denominator = 662010148800000
    factor = prod_polys([
        *([[0,1]]*5), *([[1,1]]*5), [2,1],
        *([[1,2]]*5), *([[3,2]]*5), P5,
    ])
    rhs = scale(factor, Fraction(-1,denominator))
    lhs = determinant_poly_5()
    assert len(lhs)==31 and len(rhs)==31 and lhs == rhs
    # Exact 31-coefficient symbolic identity above is a universal Q[k] check.

    # Integer positive-root certificate: P5(8+u) has 10 positive coefficients.
    shifted=[Fraction(0)]
    for n, coeff in enumerate(P5):
        term = [coeff * C(n,j) * 8**(n-j) for j in range(n+1)]
        shifted = add(shifted,term)
    assert len(shifted)==10 and all(x>0 for x in shifted)
    assert int(evaluate(P5,7)) == -5921622860508
    assert int(evaluate(P5,8)) == 83290020660000

    # Independent raw signed convolution and polynomial formula for t=2,...,7.
    coeff_count=0
    for kval in range(1,81):
        for t in range(2,8):
            raw = raw_H(kval,t)
            symbolic = evaluate(p_poly(t),kval)*catalan(kval)
            assert symbolic.denominator==1 and raw==symbolic
            coeff_count += 1

    # Independent raw 5x5 determinants, including all 1..7 positive cases,
    # the first negative case k=8, and non-adjacent large k=49 and 101.
    raw_ks=tuple(range(1,20))+(48,49,50,64,101)
    raw_count=0
    for kval in raw_ks:
        a=[[raw_H(kval,3+i-j) for j in range(5)] for i in range(5)]
        det=det_numeric(a)
        formula=evaluate(lhs,kval)*catalan(kval)**5
        assert formula.denominator==1 and det==formula
        assert (det>0 if kval<=7 else det<0)
        raw_count+=1

    # s=2: lower triangular for arbitrary m; here independent samples m=1..9.
    s2_count=0
    for kval in range(1,17):
        for m in range(1,10):
            a=[[raw_H(kval,2+i-j) for j in range(m)] for i in range(m)]
            # Triangular identity does not require enumerating m! permutations.
            assert all(a[i][j]==0 for i in range(m) for j in range(i+1,m))
            assert all(a[i][i]==raw_H(kval,2) for i in range(m))
            assert raw_H(kval,2)==catalan(kval)*C(2*kval+3,4)>0
            s2_count+=1

    # m5 fixed right-edge asymptotic constant, via leading coefficient.
    # r = 2k+1, hence normalized by r^30 = (2k+1)^30.
    leading_limit=lhs[-1]/2**30
    assert leading_limit == Fraction(-1343,677898392371200000)
    assert len(lhs)-1==30

    evidence={
        "schema":"ENTERPRISE_MATH_R483_EXACT_EVIDENCE_V1",
        "result":"R483_EXACT_PASS",
        "scientific_pin":"18783e01e3646c72b7aab3b16d3f565e83e6446f",
        "object":"signed BRC auxiliary scalar H, not native X6 transfer",
        "main_claim":"D5(r,r-3)>0 for 1<=k<=7, and <0 for all k>=8, r=2k+1",
        "secondary_claim":"D_m(r,r-2)=H(r,2)^m>0 for all integers k,m>=1",
        "symbolic_identity":{"degree":30,"checked_coefficients":31,"permutation_terms":120,"coefficient_comparison":"exact over Q[k]"},
        "P5_coefficients_ascending":[to_json_number(x) for x in P5],
        "P5_shift_8_coefficients_ascending":[to_json_number(x) for x in shifted],
        "P5_at_1_through_7":[to_json_number(evaluate(P5,x)) for x in range(1,8)],
        "P5_at_7":to_json_number(evaluate(P5,7)),
        "P5_at_8":to_json_number(evaluate(P5,8)),
        "raw_H_vs_polynomial_checks":coeff_count,
        "raw_determinant_cross_checks":raw_count,
        "raw_determinant_k_values":list(raw_ks),
        "triangular_samples":s2_count,
        "rank5_limit_constant":{"numerator":leading_limit.numerator,"denominator":leading_limit.denominator},
        "arithmetic":"Python arbitrary precision integers and fractions, exact polynomial coefficient arithmetic, no floating point",
        "scope":"universal symbolic identity in Q[k], positivity certificate for k>=8, individual exact checks k=1..7, finite raw cross-validation",
        "admission":"AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED"
    }
    print(json.dumps(evidence,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
