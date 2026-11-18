#!/usr/bin/env python3
"""Exact valuation histograms, moments and full-block generating functions."""
from collections import Counter
from fractions import Fraction as F
from math import factorial, floor
import hashlib
import json

LENGTHS = [2,1,1,2]


def transition(p):
    eps = 1 if p%6 == 1 else -1
    return [[(p-eps)*LENGTHS[j]//6 + eps*(j == (i if eps == 1 else 3-i))
             for j in range(4)] for i in range(4)]


def state(x):
    return floor(2*x) + floor(3*x)


def audit_transitions(p):
    M = transition(p)
    for x in [F(i,60) for i in range(60)]:
        dest = Counter(state((x+d)/p) for d in range(p))
        assert [dest[j] for j in range(4)] == M[state(x)]
    return M


def next_level(M,old):
    out = [[0]*(len(old[0])+3) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mult = M[i][j]
            for v,n in enumerate(old[i]):
                out[j][v+j] += mult*n
    return out


def digit_sum(n,p):
    s = 0
    while n:
        n,r = divmod(n,p)
        s += r
    return s


def digit_valuation(n,p):
    return (5*digit_sum(n,p)-digit_sum(2*n,p)-digit_sum(3*n,p))//(p-1)


def moments(hist):
    mass = sum(hist)
    raw = [F(sum(v**j*n for v,n in enumerate(hist)),mass) for j in range(1,5)]
    m,r2,r3,r4 = raw
    var = r2-m*m
    third = r3-3*m*r2+2*m**3
    fourth = r4-4*m*r3+6*m*m*r2-3*m**4-3*var*var
    return m,var,third,fourth


def finite_mean_variance(p,k):
    eps = 1 if p%6 == 1 else -1
    r = F(1,p)
    m = F(3,2)*(k-(1-r**k)/(p-1))
    v = 0
    for i in range(1,k+1):
        vi = F(19,12)+F(2,3)*(eps*r)**i-F(9,4)*r**(2*i)
        v += vi*(1+2*(1-r**(k-i))/(p-1))
    return m,v


def multiply_t(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):
            out[i+j] += v*w
    return out


def rational_gf(p,u):
    vals = [u**i for i in range(4)]
    if p%6 == 5:
        return [1,-u**3],[1,-(p+1)//6*sum(v*w for v,w in zip(vals,LENGTHS)),p*u**3]
    factors = [[1,-v] for v in vals]
    num = [1]
    for f in factors[1:]:
        num = multiply_t(num,f)
    den = multiply_t(num,factors[0])
    for i in range(4):
        rest = [1]
        for j,f in enumerate(factors):
            if i != j:
                rest = multiply_t(rest,f)
        for j,c in enumerate(rest):
            den[j+1] -= (p-1)//6*LENGTHS[i]*vals[i]*c
    return num,den


def poly_value(poly,x):
    return sum(c*x**j for j,c in enumerate(poly))


def verify(p,brute_k):
    M = audit_transitions(p)
    eps = 1 if p%6 == 1 else -1
    s2 = F(19*(p+1),12*(p-1))
    k4 = -F((p+1)*(99*p*p+(396-128*eps)*p+99),24*(p-1)**3)
    old = [[1],[0],[0],[0]]
    values = {u:[] for u in (2,3,5)}
    observed = {}
    examples = []
    for n in range(101):
        a = factorial(2*n)*factorial(3*n)//factorial(n)**5
        v = 0
        while a%p == 0:
            a //= p
            v += 1
        assert digit_valuation(n,p) == v
    for k in range(43):
        h = [sum(column) for column in zip(*old)]
        assert sum(h) == p**k
        assert h[0] == (p//3+1)**k
        if k:
            assert h[-1] == (p//3)*(p//3+1)**(k-1)
        m,v,c3,c4 = moments(h)
        assert (m,v) == finite_mean_variance(p,k)
        if k in (40,41,42):
            observed[k] = (v,c3,c4)
        if k <= brute_k:
            raw = Counter(digit_valuation(n,p) for n in range(p**k))
            assert h == [raw[m] for m in range(3*k+1)]
            if k == brute_k:
                examples.append(dict(k=k,integers=p**k,counts=h,
                                     exact_mean=str(m),exact_variance=str(v)))
        if k < 10:
            for u,previous in values.items():
                previous.append(poly_value(h,u))
                num,den = rational_gf(p,u)
                coeff = sum(den[j]*previous[k-j] for j in range(min(k+1,len(den))))
                assert coeff == (num[k] if k < len(num) else 0)
        if k != 42:
            old = next_level(M,old)
    error = observed[42][2]-observed[41][2]-k4
    assert abs(error) < F(1,p**20)
    assert abs(observed[42][0]-observed[41][0]-s2) < F(1,p**20)
    assert abs(observed[42][1]-observed[41][1]) < F(1,p**20)
    digest = hashlib.sha256(','.join(map(str,h)).encode()).hexdigest()
    return dict(p=p,digit_transition_counts=M,brute=examples[0],generic_recurrence_order=(4 if eps==1 else 2),
                asymptotic_variance_slope=str(s2),fourth_cumulant_slope=str(k4),
                exact_cumulant_slope_residual_bound_at_42=f'< 1/{p}^20',
                histogram_k42_csv_sha256=digest)


if __name__ == '__main__':
    tests = [verify(p,k) for p,k in [(5,7),(7,6),(11,5),(13,4),(17,4),(19,4),(23,3),(31,3)]]
    print(json.dumps(dict(tests=tests,total_distinct_integers_by_prime=sum(row['brute']['integers'] for row in tests)),
                     sort_keys=True,indent=2))
