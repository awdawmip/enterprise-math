#!/usr/bin/env python3
"""Author-side tests for S23/AV arcsine-weighted adaptive decoder.

The fixed-fiber and global asymptotic theorems rely on the analytic proof, not
on finite tests in this file. Python standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import asin, sqrt, pi, log, ceil, floor, comb, lgamma, exp


def fiber(z):
    umin = max(F(1, 8), F(8, 7)*z)
    umax = min(F(1, 2), 2*z)
    return (1-umax)/(1-z), (1-umin)/(1-z)


def p_pair(a, c):
    z = (1-a)*c
    p = a/(1-z)
    return z, p


def clip(x):
    return min(0.99, max(0.5, x))


def weights(n, r):
    if n == r:
        return [1.0]
    m = n-r
    z = min(F(7, 16), max(F(1, 16), F(r, n)))
    plo, phi = fiber(z)
    w = ceil(4*sqrt(n*log(n+2)))+1
    lo = max(0, floor(m*plo)-w)
    hi = min(m, ceil(m*phi)+w)
    data = [1.0/sqrt(clip(k/m)*(1-clip(k/m))) for k in range(lo, hi+1)]
    total = sum(data)
    ans = [0.0]*(m+1)
    for k, weight in enumerate(data, lo):
        ans[k] = weight/total
    assert abs(sum(ans)-1) < 2e-12
    return ans


def binom_pmf(m, p):
    """Stable Binomial(m,p) for m<=about 100000."""
    if m == 0:
        return [1.0]
    k0 = max(0, min(m, int((m+1)*p)))
    vals = [0.]*(m+1)
    vals[k0] = 1.0
    for k in range(k0, m):
        vals[k+1] = vals[k] * (m-k)/(k+1)*p/(1-p)
    for k in range(k0, 0, -1):
        vals[k-1] = vals[k] * k/(m-k+1)*(1-p)/p
    den = sum(vals)
    return [x/den for x in vals]


def ordered_exact(n, z, p):
    """Full joint law for source alphabet (1,3,4), n<=5."""
    s = 1-z
    masses = {1: s*p, 3: z, 4: s*(1-p)}
    return {w: product_fractions(masses[x] for x in w) for w in product((1,3,4), repeat=n)}


def product_fractions(seq):
    ans = F(1)
    for v in seq:
        ans *= v
    return ans


def count_overlap_exact(n, z, p, q_rows):
    """Exact total variation overlap in count space for rational rows."""
    out = F(0)
    for r in range(n+1):
        m = n-r
        pr = F(comb(n, r)) * z**r * (1-z)**m
        for k in range(m+1):
            b = F(comb(m,k)) * p**k * (1-p)**(m-k)
            out += pr*min(b,q_rows[r][k])
    return out


def decoder_ordered_exact(n, z, q_rows):
    """Distribution on ordered output words for a Y-preserving count decoder."""
    ans = {}
    for word in product((1,3,4), repeat=n):
        r = word.count(3)
        m = n-r
        k = word.count(1)
        # Each input Y-mask has source probability z^r(1-z)^m.
        ans[word] = z**r*(1-z)**m*q_rows[r][k]/F(comb(m,k))
    return ans


def exact_small_checks():
    for n in (2,3,4):
        rows=[]
        for r in range(n+1):
            m=n-r
            raw=[F((k+1)*(m-k+1), 1) for k in range(m+1)]
            rows.append([w/sum(raw) for w in raw])
        for a,c in ((F(1,2),F(1,2)), (F(5,7),F(7,8)), (F(7,8),F(7,8))):
            z,p=p_pair(a,c)
            src=ordered_exact(n,z,p)
            dec=decoder_ordered_exact(n,z,rows)
            assert sum(src.values())==1 and sum(dec.values())==1
            full=sum((min(src[w], dec[w]) for w in src),F(0))
            count=count_overlap_exact(n,z,p,rows)
            assert full==count
    return "PASS_EXACT_ORDERED_COUNT_OVERLAP n=2,3,4 x 3 rational lawful pairs"


def geometry_checks():
    assert fiber(F(1,4)) == (F(2,3),F(20,21))
    C=lambda z: 2/sqrt(float(1-z))/(2*(asin(sqrt(float(fiber(z)[1])))-asin(sqrt(float(fiber(z)[0])))))
    base=C(F(1,4))
    assert 2.91965 < base < 2.91967
    for j in range(1,1500):
        z=F(1,16)+F(j,1500)*(F(7,16)-F(1,16))
        if z!=F(1,4):
            assert C(z)>=base-1e-10, (z,C(z),base)
    return "PASS_FIBER_GEOMETRY p=[2/3,20/21] at z=1/4, 1499 grid checks; C*=%.12f" % base


def finite_decoder_checks():
    for n in (40,400,20000):
        r=n//4
        m=n-r
        q=weights(n,r)
        z,p=p_pair(F(5,7),F(7,8))
        pmf=binom_pmf(m,float(p))
        overlap=sum(min(q[k],pmf[k]) for k in range(m+1))
        assert 0<overlap<=1+1e-12
        scaled=overlap*sqrt(m/log(m))
        print("n=%d R=%d conditional_overlap=%.12f scaled_conditional=%.9f"%(n,r,overlap,scaled))
    return "PASS_NUMERICAL_ADAPTIVE_DECODER_NORMALIZATION_AND_OVERLAP"


if __name__=='__main__':
    print(exact_small_checks())
    print(geometry_checks())
    print(finite_decoder_checks())
    print('PASS_S23_AV_ARCSINE_ADAPTIVE_ASYMPTOTIC_AUTHOR_CHECK_20261107')
