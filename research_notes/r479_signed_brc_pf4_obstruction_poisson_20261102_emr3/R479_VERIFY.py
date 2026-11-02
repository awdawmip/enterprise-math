#!/usr/bin/env python3
"""R479: exact independent polynomial and integer witness for signed BRC PF4 obstruction.

Pure Python standard library; no floating-point arithmetic. Input identities:
H(2k+1,s) = binom(2k+1+s,2s) sum_q binom(s-1,2q) 4^q C_(k-q).
All calculations are exact in Q[k] or Z.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai*bj
    return trim(out)


def product(*factors):
    ans = (F(1),)
    for f in factors:
        ans = mul(ans, f)
    return ans


def scale(p, c):
    return trim([v*c for v in p])


def evalpoly(p, n):
    ans = 0
    for a in reversed(p):
        ans = ans*n + a
    return ans


def sign_perm(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2 else 1


def det4(mat, add_op=add, mul_op=mul, neg_op=lambda x: scale(x,-1), zero=(F(0),)):
    result = zero
    for order in permutations(range(4)):
        term = (F(1),)
        for i, j in enumerate(order):
            term = mul_op(term, mat[i][j])
        if sign_perm(order) < 0:
            term = neg_op(term)
        result = add_op(result, term)
    return result


X = (F(0), F(1))
def lin(a, b=1):
    return (F(a), F(b))  # a + bk

k = X
P = {
    2: scale(product(k,lin(1),lin(1,2),lin(3,2)),F(1,6)),
    3: scale(product(k,lin(1),lin(2),lin(1,2),lin(3,2),lin(1,4)),F(1,90)),
    4: scale(product(k,lin(-1),lin(1),lin(2),lin(1,2),lin(3,2),lin(5,2),lin(5,8)),F(1,2520)),
    5: scale(product(k,lin(-1),lin(1),lin(2),lin(3),lin(1,2),lin(3,2),lin(5,2),
                     (F(-33),F(-16),F(32))),F(1,113400)),
    6: scale(product(k,lin(-2),lin(-1),lin(1),lin(2),lin(3),lin(1,2),lin(3,2),lin(5,2),lin(7,2),
                     (F(-57),F(-8),F(64))),F(1,7484400)),
}
for s in range(2,7):
    assert len(P[s]) == 2*s+1, (s, len(P[s]))
zero=(F(0),)
M = [[P.get(3+i-j,zero) for j in range(4)] for i in range(4)]
actual = det4(M)
poly7 = (F(-11787442),F(-35761465),F(-46354824),F(-33616293),
         F(-14300148),F(-3408516),F(-309248),F(7936))
expected = scale(product(*([k]*4 + [lin(1)]*4 + [lin(2)] +
                           [lin(1,2)]*4 + [lin(3,2)]*4 + [poly7])),F(-1,565820640000))
assert len(actual) == 25 and len(expected) == 25
assert actual == expected, "rational polynomial identity failed"


def catalan(n):
    return comb(2*n,n)//(n+1)


def exact_a(k,s):
    r=2*k+1
    if s < 2 or s > r:
        return 0
    return comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*catalan(k-q)
                              for q in range(min(k,(s-1)//2)+1))


def integer_det4(k,s=3):
    vals = [[exact_a(k,s+i-j) for j in range(4)] for i in range(4)]
    tot=0
    for perm in permutations(range(4)):
        t=sign_perm(perm)
        for i,j in enumerate(perm):
            t*=vals[i][j]
        tot+=t
    return tot

# Cross-verify every symbolic p_s against its original Catalan convolution.
for k0 in range(2,81):
    ck=catalan(k0)
    for s in range(2,7):
        assert P[s] and evalpoly(P[s],k0)*ck == exact_a(k0,s), (k0,s)
    raw=integer_det4(k0)
    assert evalpoly(actual,k0)*ck**4 == raw, k0

# The polynomial has one sign change (descending coefficients), so exactly one
# positive real zero (Descartes); its rational signs at 48 and 49 locate it.
assert list(reversed(poly7))[0] > 0
assert all(x<0 for x in list(reversed(poly7))[1:])
q48 = int(evalpoly(poly7,48)); q49=int(evalpoly(poly7,49))
assert q48 < 0 < q49
shift_coeff = [int(sum(comb(j,i)*poly7[j]*49**(j-i) for j in range(i,len(poly7))))
               for i in range(len(poly7))]
assert all(c>0 for c in shift_coeff)

samples=[]
for kval in (2,8,20,47,48,49,50,143,500):
    raw=integer_det4(kval)
    assert raw == evalpoly(expected,kval)*catalan(kval)**4
    samples.append({"k":kval,"r":2*kval+1,"D4_sign":(raw>0)-(raw<0),
                    "D4_abs_decimal_digits":len(str(abs(raw)))})

# Check the rational fixed-j finite asymptotic direction only as a numerical
# cross-check. The all-j theorem is established analytically in R479_PROOF.
poisson_samples=[]
for r in (51,101,201,401):
    kval=(r-1)//2
    ck=catalan(r)
    row=[]
    for j in (0,1,2,3):
        coeff=exact_a(kval,r-j)
        rat=F(coeff*factorial(j),ck*r**j)
        row.append({"j":j,"normalized_times_factorial_numerator":str(rat.numerator),
                    "normalized_times_factorial_denominator":str(rat.denominator)})
    poisson_samples.append({"r":r,"ratios":row})

report={
  "schema":"EM_R479_EXACT_EVIDENCE_V1",
  "source":"R462 frozen scientific pin 18783e01e3646c72b7aab3b16d3f565e83e6446f via R478 stated Catalan representation",
  "arithmetic":"exact_integer_and_rational_only",
  "symbolic_check":"D4_over_Ck4_polynomials_identical_all_25_coefficients",
  "degree":24,"polynomial_coefficients_checked":25,
  "catalan_convolution_samples":79*5,
  "raw_determinant_samples":79,
  "P7_at_48":str(q48), "P7_at_49":str(q49),
  "P7_shift_k_eq_49_plus_u_coefficients_ascending":list(map(str,shift_coeff)),
  "strictly_positive_shift_coefficients":True,
  "sign_theorem":"For every integer k>=49, D4_(2k+1,2k-2) < 0; corresponding s=3",
  "selected_samples":samples,
  "poisson_normalization_samples":poisson_samples,
  "unverified":"Independent Driver review; general PF4 status below r=99; global PF_m for variable j; native X6 transfer",
  "result":"R479_EXACT_PASS"
}
print(json.dumps(report,ensure_ascii=False,indent=2))
