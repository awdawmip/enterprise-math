"""Exact two-adic refinement checks for EC49FVB. Analytic proof in addendum."""
from fractions import Fraction as Q
from math import gcd

BETA = Q(3, 637)
GAMMA = Q(141024, 1653649)
U = Q(4822040484, 8132285009)
M = 8132285009

def ordp(n, p):
    assert n
    k = 0
    while n % p == 0:
        k += 1
        n //= p
    return k

def valuation(q, p):
    return ordp(q.numerator, p) - ordp(q.denominator, p)

def input_case(x):
    t0 = (1-x)*(1-BETA*x)
    te = (1-x)*(1+GAMMA*x)
    a = 1-t0
    b = 1-U*te
    r = t0/(U*te)
    s = (b/a)*r
    assert 0 < a < b < 1 and 1 < r < s
    return valuation(r,2),valuation(s,2)

assert tuple(valuation(q,2) for q in (BETA,GAMMA,U)) == (0,5,2)
# Exhaust all reduced fractions m/d, 0<m<d<=180, checking the two proven families.
checked_even = checked_odd = 0
for d in range(2,181):
    for m in range(1,d):
        if gcd(m,d)>1:
            continue
        r,s = input_case(Q(m,d))
        if d%2 == 0:
            assert r<0 and (s>=0 or r<s<0), (m,d,r,s)
            checked_even += 1
        elif m%2 == 1:
            res = m*pow(d,-1,8)%8
            if res==3:
                assert (r,s)==(0,0), (m,d,res,r,s)
            else:
                assert res in (1,5,7) and r==s!=0,(m,d,res,r,s)
            checked_odd+=1

assert checked_even>2500 and checked_odd>1500
assert 8*M == 65058280072
assert 8*M-40 == 65058280032
assert (40,8*M) == (40,65058280072)
print('ALL PASS: v2(beta,gamma,u),', checked_even,
      'even-denominator fractions,', checked_odd,
      'odd-numerator/denominator fractions, CRT 40/(8M)')
