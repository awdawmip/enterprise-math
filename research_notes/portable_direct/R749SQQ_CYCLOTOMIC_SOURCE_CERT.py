#!/usr/bin/env python3
"""R749SQQ: exact positive-labeled-source cyclotomic boundary witness.
Python >=3.10, standard library; integer and Fraction arithmetic only.
"""
import json
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache

CASES = (
    {'label': 'order5', 's': (1, 1, 1, 2, 2, 2, 3), 'q': 5,
     'amplitude': F(945, 32)},
    {'label': 'order6', 's': (1, 1, 1, 2, 2, 3, 5), 'q': 6,
     'amplitude': F(4725, 32)},
)
SAMPLES = (500, 501, 1000, 1001, 4000, 4001, 12000, 12001, 24000, 24001)


def truncated_product(a, b, n):
    out = [F(0)] * (n + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= n:
                out[i + j] += x * y
    return out


def reciprocal_factor(s, n):
    # R_s(w) = s*w / (1-(1-w)^s), analytic at w=0 and R_s(0)=1.
    den = [F((-1)**j * comb(s, j+1), s) if j + 1 <= s else F(0)
           for j in range(n + 1)]
    out = [F(1)] + [F(0)] * n
    for k in range(1, n + 1):
        out[k] = -sum(den[j] * out[k-j] for j in range(1, k+1))
    return out


def binomial_polynomial(k):
    # Exact coefficients of binom(r+k,k) = prod_{j=1}^k(r+j)/k!.
    p = [F(1)]
    for j in range(1, k+1):
        nxt = [F(0)] * (len(p) + 1)
        for i, v in enumerate(p):
            nxt[i] += j*v
            nxt[i+1] += v
        p = nxt
    return [v/factorial(k) for v in p]


def smooth_mean(s, order, marked=0):
    # Population is sum(s_i*k_i) <= r-1, not <=r.
    d, h = len(s), s[marked]
    assert d >= order and h >= 1
    a = [F(1)] + [F(0)] * order
    for weight in s:
        a = truncated_product(a, reciprocal_factor(weight, order), order)
    a = truncated_product(a, [F(1), F(-1)]+[F(0)]*(order-1), order)
    hp = [F((-1)**j*comb(h, j)) if j <= h else F(0)
          for j in range(order+1)]
    b = truncated_product(a, reciprocal_factor(h, order), order)
    b = truncated_product(b, hp, order)
    c, v = [], []
    for t in range(order+1):
        c.append(sum(a[j]*binomial_polynomial(d-j)[d-t]
                     for j in range(t+1)))
        v.append(sum(b[j]*binomial_polynomial(d+1-j)[d+1-t]
                     for j in range(t+1)))
    out = []
    for t in range(order+1):
        out.append((v[t]-sum(c[j]*out[t-j] for j in range(1,t+1)))/c[0])
    return out


def prefix_dp(s, bound, marked=0):
    exact = [0]*bound
    marked_sum = [0]*bound
    exact[0] = 1
    for i, weight in enumerate(s):
        for t in range(weight, bound):
            exact[t] += exact[t-weight]
            marked_sum[t] += marked_sum[t-weight] + (exact[t-weight] if i==marked else 0)
    C, M = [0]*(bound+1), [0]*(bound+1)
    for r in range(1, bound+1):
        C[r] = C[r-1]+exact[r-1]
        M[r] = M[r-1]+marked_sum[r-1]
    return C, M


def brute(s, bound, marked=0):
    @lru_cache(None)
    def rec(i, available):
        if i == len(s):
            return (1, 0)
        a=b=0
        for k in range(available//s[i]+1):
            c,m = rec(i+1, available-k*s[i])
            a+=c
            b+=m+(k*c if i==marked else 0)
        return a,b
    return rec(0,bound-1)


def run():
    results=[]
    checks={'independent_enumerations':0,'source_deletion_equalities':0,
            'smooth_coefficient_assertions':0, 'oscillatory_amplitude_assertions':0}
    for case in CASES:
        s,q,expected=case['s'],case['q'],case['amplitude']
        d,h=len(s),s[0]
        even=[x for x in s if x%2==0]
        assert h==1 and len(even)==d-q+1
        # F_r(z)=z/(1-z)*product(1-z^s)^-1; at z=-1,
        # the Laurent leading coefficient in w=1+z is
        # A_{-1} = (-1)/(2*prod_{even}s_i*2**len(odd)).
        W=1
        for x in s: W*=x
        Aminus = F(-1, 2**(1+d-len(even)) * __import__('math').prod(even))
        predicted = -F(factorial(d)*W, (d+1)*factorial(len(even)-1))*Aminus
        assert predicted==expected
        checks['oscillatory_amplitude_assertions']+=1
        smooth=smooth_mean(s,q)
        assert smooth[0]==F(1,d+1)
        checks['smooth_coefficient_assertions']+=1
        C,M=prefix_dp(s,max(SAMPLES))
        running=0
        for r in range(1,max(SAMPLES)+1):
            running+=C[r-1]
            assert M[r]==running # deletion of marked unit source
            checks['source_deletion_equalities']+=1
        for r in range(1,33):
            assert (C[r],M[r])==brute(s,r)
            checks['independent_enumerations']+=1
        samples=[]
        for r in SAMPLES:
            obs=F(M[r],r*C[r])
            smooth_val=sum(a/F(r**j) for j,a in enumerate(smooth))
            scaled=r**q*(obs-smooth_val)
            error=scaled-expected*(-1)**r
            if r in (24000, 24001):
                assert abs(error) < (F(1) if q==5 else F(10))
            samples.append({'r':r,'exact_scaled_residual':str(scaled),
                            'predicted_periodic_lead':str(expected*(-1)**r),
                            'exact_difference':str(error)})
        results.append({'case':case['label'],'weights':list(s),'d':d,'q':q,
                        'max_nontrivial_pole_order':len(even),
                        'smooth_coefficients':list(map(str,smooth)),
                        'parity_amplitude':str(expected),
                        'r_samples':samples})
    # A very small exact shift/period sanity check for s=(1,2).
    assert smooth_mean((1,2),2)==[F(1,3),F(-1,6),F(-1,6)]
    C,M=prefix_dp((1,2),100)
    for r in range(1,101):
        actual=F(M[r],r*C[r])
        if r%2==0:
            assert actual==F(1,3)-F(1,6*r)
        else:
            assert actual==F((r-1)*(2*r+3),6*r*(r+1))
    return {'status':'PASS','model':'labeled nonnegative multiplicities, sum(s_i k_i)<=r-1',
            'arithmetic':'exact Python integers and fractions','inputs_pin':
            'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'checks':checks,'max_r':max(SAMPLES),'results':results,
            'verification_scope':'finite arithmetic checks; all-r asymptotics rely on the paper pole proof'}


if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
