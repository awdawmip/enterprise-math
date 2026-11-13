#!/usr/bin/env python3
"""R129 exact one-parameter signed S23 clock-family word enumerator.
Python standard library; all fractions exact. No floating point.
"""
from fractions import Fraction as F
from math import gcd
from random import Random
from pathlib import Path
import json


def frac(v):
    return v - (v.numerator // v.denominator)


def signature(beta, x, s, r, m):
    t = frac(r * beta)
    return ''.join('1' if frac(x + (s + i) * beta) < t else '0' for i in range(m))


def integer_crossings(x, a):
    """0 < beta < 1; x + a*beta is integral; a is an integer."""
    if not a:
        return set()
    lo, hi = sorted((x, x + a))
    kmin = lo.numerator // lo.denominator + 1
    kmax = -((-hi.numerator) // hi.denominator) - 1  # ceil(hi)-1
    return {(F(k) - x) / a for k in range(kmin, kmax + 1)}


def critical_set(x, s, r, m):
    x = F(x)
    roots = integer_crossings(F(0), r)
    for i in range(m):
        roots.update(integer_crossings(x, s + i))
        roots.update(integer_crossings(x, s + i - r))
    assert all(F(0) < v < F(1) for v in roots)
    return sorted(roots)


def enumerate_words(x, s, r, m):
    x = F(x)
    roots = critical_set(x, s, r, m)
    cuts = [F(0)] + roots + [F(1)]
    probes = [F(0)] + roots + [(a+b)/2 for a,b in zip(cuts,cuts[1:])]
    words = {signature(beta, x, s, r, m) for beta in probes}
    return words, roots, probes


def interval_witness(beta, l, h, d):
    """Exact theta in (l,h) with {d*theta}=beta, or None."""
    assert d != 0 and 0 <= beta < 1 and l < h
    low, high = sorted((d*l-beta, d*h-beta))
    k = low.numerator // low.denominator + 1
    if F(k) >= high:
        return None
    theta = (k+beta)/d
    assert l < theta < h and frac(d*theta) == beta
    return theta


def interval_words(x, s, r, d, m, l, h):
    """Exact attained word -> rational theta, on arbitrary rational open interval."""
    x,l,h = F(x),F(l),F(h)
    assert d and l < h
    cuts = sorted(set([F(0),F(1)] + critical_set(x,s,r,m)
                      + [frac(d*l), frac(d*h)]))
    probes = [p for p in cuts if p < 1] + [(a+b)/2 for a,b in zip(cuts,cuts[1:])]
    found = {}
    for beta in probes:
        theta = interval_witness(beta,l,h,d)
        if theta is not None:
            word = signature(beta,x,s,r,m)
            found.setdefault(word,theta)
    return found, len(probes)


def integer_crossings_interval(x, a, l, h):
    if a == 0:
        return set()
    vals = (x+a*l,x+a*h)
    lo,hi = sorted(vals)
    kmin = lo.numerator // lo.denominator + 1
    kmax = -((-hi.numerator) // hi.denominator) - 1
    return {(F(k)-x)/a for k in range(kmin,kmax+1)}


def theta_oracle(x,s,r,d,m,l,h):
    """Independent uncompressed theta-domain exhaustive affine-boundary cut."""
    roots = integer_crossings_interval(F(0),r*d,l,h)
    for i in range(m):
        roots |= integer_crossings_interval(x,(s+i)*d,l,h)
        roots |= integer_crossings_interval(x,(s+i-r)*d,l,h)
    roots = sorted(v for v in roots if l<v<h)
    cuts = [l] + roots + [h]
    probes = roots + [(a+b)/2 for a,b in zip(cuts,cuts[1:])]
    return {''.join('1' if frac(x+(s+i)*d*t)<frac(r*d*t) else '0'
                    for i in range(m)) for t in probes}


def totient(n):
    return sum(gcd(k, n) == 1 for k in range(1,n+1))


def run():
    # Independent exact count: the special carry family has only Farey events.
    sharp = []
    for m in range(2, 31):
        w, roots, probes = enumerate_words(F(0),0,1,m)
        expected = 2 + sum(totient(q) for q in range(2,m))
        assert len(w) == expected, (m, len(w), expected)
        assert all(ww[0] == '1' for ww in w if ww != '0'*m)
        assert signature(F(0),F(0),0,1,m) == '0'*m
        sharp.append({'m':m,'expected':expected,'observed':len(w),'cut_count':len(roots)})

    rng = Random(12920261113)
    cases,check_count,point_count,distinct_total = [],0,0,0
    for z in range(220):
        m = rng.randrange(2,10)
        s = rng.randrange(-5,6)
        r = rng.randrange(-5,6)
        x = F(rng.randrange(-7,8),rng.randrange(1,9))
        words,roots,probes= enumerate_words(x,s,r,m)
        bound = max(abs(r)-1,0) + sum(abs(s+i)+abs(s+i-r) for i in range(m))
        assert len(roots) <= bound
        assert len(words) <= 2*len(roots)+2
        # Exact independent pointwise oracle across every critical/open cell;
        # at 1/7, 2/7, 1/2, 5/7, 6/7 of each cell, so no float used.
        intervals = list(zip([F(0)]+roots,roots+[F(1)]))
        observed={signature(F(0),x,s,r,m)}
        for beta in roots:
            observed.add(signature(beta,x,s,r,m))
            point_count+=1
        for a,b in intervals:
            prior=signature((a+b)/2,x,s,r,m)
            for j in (1,2,3,5,6):
                probe=a+(b-a)*F(j,7)
                actual=signature(probe,x,s,r,m)
                assert actual == prior,(z, m, s, r, x, a,b,probe,prior,actual)
                check_count += 1
            observed.add(prior)
        assert observed == words
        distinct_total+=len(words)
        if z<8:
            cases.append({'m':m,'s':s,'r':r,'x':str(x),'roots':len(roots),'words':len(words),'bound':bound})

    # Independent theta-domain completeness against beta-quotient enumeration,
    # including signed clocks, strict endpoints and >one-period intervals.
    interval_cases=180
    interval_probes=0
    for z in range(interval_cases):
        m=rng.randrange(2,8)
        s=rng.randrange(-3,4)
        r=rng.randrange(-3,4)
        d=rng.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
        x=F(rng.randrange(-5,6),rng.randrange(1,6))
        l=F(rng.randrange(-9,10),rng.randrange(1,7))
        h=l+F(rng.randrange(1,11),rng.randrange(1,7))
        got,nprobes=interval_words(x,s,r,d,m,l,h)
        reference=theta_oracle(x,s,r,d,m,l,h)
        assert set(got)==reference,(z, x,s,r,d,m,l,h,sorted(got),sorted(reference))
        for word,theta in got.items():
            assert l<theta<h
            assert ''.join('1' if frac(x+(s+i)*d*theta)<frac(r*d*theta) else '0'
                          for i in range(m)) == word
        interval_probes+=nprobes

    # Signed d is only a reparameterization: beta={d theta}.
    for d in (-17, -3, 3, 13):
        for j in range(0,51):
            theta=F(j,50*abs(d))
            beta=frac(d*theta)
            assert signature(beta,F(1,3),-2,3,8)==''.join(
                '1' if frac(F(1,3)+(-2+i)*d*theta)<frac(3*d*theta) else '0'
                for i in range(8))

    result={'status':'R129_COUPLED_CLOCK_PASS','exact_arithmetic':'fractions.Fraction','special_sharp_m_range':[2,30], 'sharp_counts':sharp,
            'random_seed':12920261113,'random_cases':220,'cell_interior_checks':check_count,
            'critical_singletons_checked':point_count,'total_distinct_words_across_cases':distinct_total,
            'sample_cases':cases,'signed_d_forward_checks':4*51,'interval_cases':interval_cases,'interval_candidate_probes':interval_probes,
            'proof_scope':'all rational x; signed integer s,r,d with d nonzero; arbitrary rational open theta intervals and complete beta period; real x admits analytic statement but exact computational output requires an x representation'}
    print(json.dumps({k:v for k,v in result.items() if k!='sharp_counts'},ensure_ascii=False,indent=2))
    with Path(__file__).with_name('verification_r129.json').open('w',encoding='utf8') as f:
        json.dump(result,f,ensure_ascii=False,sort_keys=True,indent=2)
        f.write('\n')

if __name__=='__main__':
    run()
