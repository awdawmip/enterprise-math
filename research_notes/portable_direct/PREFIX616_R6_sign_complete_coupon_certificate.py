#!/usr/bin/env python3
"""PREFIX-616-R6: exact sign-complete coupon stopping law.

Independent repeated one-step native-BRC signed-label likelihood is an inherited
input from PREFIX-610. All new computation here is exact conditional probability
arithmetic over that explicitly typed observation law, not a new native graph run.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb
import json
from pathlib import Path

checks = 0

def eq(a, b, label):
    global checks
    assert a == b, f"{label}: {a} != {b}"
    checks += 1


def masses(q, theta):
    assert q in (12, 24) and 1 <= len(theta) <= 12
    assert all(abs(48*t) < 1 for t in theta)
    p = tuple((1 + s*48*t) / (2*q) for t in theta for s in (1, -1))
    assert sum(p) <= 1 and all(x > 0 for x in p)
    return p


def subset_sums(p):
    """Return (u, inclusion-exclusion sign) for nonempty coupon subsets."""
    n = len(p)
    for mask in range(1, 1 << n):
        u = sum((p[i] for i in range(n) if (mask >> i) & 1), F(0))
        sign = 1 if mask.bit_count() % 2 else -1
        yield u, sign


def ie_law(p, horizon=None):
    sums = tuple(subset_sums(p))
    mean = sum((sign/u for u, sign in sums), F(0))
    second = sum((sign*(2/(u*u)-1/u) for u, sign in sums), F(0))
    variance = second - mean*mean
    assert variance >= 0
    def cdf(n):
        assert n >= 0
        return 1-sum((sign*(1-u)**n for u, sign in sums), F(0))
    return mean, variance, cdf


def dp_moments(p):
    """Independent subset Markov recurrence; no inclusion-exclusion."""
    n = len(p)
    full = (1 << n) - 1
    @lru_cache(None)
    def go(mask):
        if mask == full:
            return F(0), F(0)
        unseen = [i for i in range(n) if not ((mask>>i)&1)]
        prob=sum((p[i] for i in unseen),F(0))
        nxt=[(p[i],go(mask | (1<<i))) for i in unseen]
        em=(1+sum((pr*v[0] for pr,v in nxt),F(0)))/prob
        em2=(2*em-1+sum((pr*v[1] for pr,v in nxt),F(0)))/prob
        return em,em2
    e,s2=go(0)
    return e,s2-e*e


def dp_cdf(p, horizon):
    """Exact forward occupancy recursion, independent of inclusion-exclusion."""
    n=len(p)
    states={0:F(1)}
    neutral=F(1)-sum(p)
    result=[F(0)]
    full=(1<<n)-1
    for step in range(1,horizon+1):
        next_states={}
        for mask,v in states.items():
            next_states[mask]=next_states.get(mask,F(0))+v*neutral
            for j,pj in enumerate(p):
                key=mask | (1<<j)
                next_states[key]=next_states.get(key,F(0))+v*pj
        states=next_states
        eq(sum(states.values()), F(1), f"DP total n={step}")
        result.append(states.get(full,F(0)))
    return result


def uniform(q,d):
    """All theta=0. Exactly m=2d equally likely signed coupons."""
    m=2*d
    h=sum((F(1,j) for j in range(1,m+1)),F(0))
    h2=sum((F(1,j*j) for j in range(1,m+1)),F(0))
    mean=2*q*h
    variance=(2*q)**2*h2-2*q*h
    def cdf(n):
        return sum(((-1)**j*comb(m,j)*F(2*q-j,2*q)**n for j in range(m+1)),F(0))
    return mean, variance, cdf


def quantile(cdf, threshold):
    hi=1
    while cdf(hi)<threshold:
        hi*=2
    lo=0
    while lo+1<hi:
        mid=(lo+hi)//2
        if cdf(mid)>=threshold:hi=mid
        else:lo=mid
    eq(cdf(hi)>=threshold,True,'quantile reach')
    eq(hi==0 or cdf(hi-1)<threshold,True,'quantile predecessor')
    return hi


def frac(x): return f"{x.numerator}/{x.denominator}"


def main():
    results={'schema':'PREFIX616_R6_EXACT_SIGN_COMPLETE_STOPPING_V1',
             'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
             'parent_model':'PREFIX-610 signed-label one-step law',
             'uniform':{},'asymmetric':{},'rare_sign':{}}
    for d in (2,4,12):
        for q in (12,24):
            theta=[F(0)]*d
            mu,var,cdf=uniform(q,d)
            if d<=4:
                p=masses(q,theta)
                imean,ivar,icdf=ie_law(p)
                dmean,dvar=dp_moments(p)
                eq(mu,imean,f'uniform mean IE d{d} q{q}')
                eq(var,ivar,f'uniform var IE d{d} q{q}')
                eq(mu,dmean,f'uniform mean DP d{d} q{q}')
                eq(var,dvar,f'uniform var DP d{d} q{q}')
                for n in range(0,9):
                    eq(cdf(n),icdf(n),f'uniform CDF d{d} q{q} n{n}')
            if d==12:
                q95=quantile(cdf,F(95,100))
                q99=quantile(cdf,F(99,100))
            else:q95=q99=None
            results['uniform'][f'd{d}_q{q}']={
                'mean_exact':frac(mu),'variance_exact':frac(var),
                'mean_rounded':round(float(mu),6),'variance_rounded':round(float(var),6),
                'N95_min':q95,'N99_min':q99}
    # Asymmetric sign-biased examples, independent subset recurrences.
    for d,theta in [(2,(F(0),F(1,96))),
                    (4,(F(0),F(1,96),F(-1,192),F(1,192)))]:
        for q in (12,24):
            p=masses(q,theta)
            a,b,ca=ie_law(p)
            c,e=dp_moments(p)
            eq(a,c,f'asym E d{d} q{q}')
            eq(b,e,f'asym Var d{d} q{q}')
            if d==2:
                cdf2=dp_cdf(p,14)
                for n in range(15):
                    eq(cdf2[n],ca(n),f'asym CDF d{d} q{q} n{n}')
            results['asymmetric'][f'd{d}_q{q}']={
                'theta':[frac(t) for t in theta],
                'mean_exact':frac(a),'variance_exact':frac(b),
                'mean_rounded':round(float(a),6),
                'variance_rounded':round(float(b),6)}
        a=F(results['asymmetric'][f'd{d}_q12']['mean_exact'])
        b=F(results['asymmetric'][f'd{d}_q12']['variance_exact'])
        a2=F(results['asymmetric'][f'd{d}_q24']['mean_exact'])
        b2=F(results['asymmetric'][f'd{d}_q24']['variance_exact'])
        eq(a2,2*a,f'thinning mean d{d}')
        eq(b2,4*b+2*a,f'thinning variance d{d}')
    for d in (2,4,12):
        a=F(results['uniform'][f'd{d}_q12']['mean_exact'])
        b=F(results['uniform'][f'd{d}_q12']['variance_exact'])
        a2=F(results['uniform'][f'd{d}_q24']['mean_exact'])
        b2=F(results['uniform'][f'd{d}_q24']['variance_exact'])
        eq(a2,2*a,f'uniform thinning mean d{d}')
        eq(b2,4*b+2*a,f'uniform thinning variance d{d}')
    # One sign approaches a boundary; the rest remain uniformly observable.
    # Direction two's negative sign has p_rare = epsilon/(2q).
    for epsilon in (F(1,4),F(1,8),F(1,16),F(1,32),F(1,64)):
        theta=(F(0), (1-epsilon)/48)
        p=masses(12,theta)
        rare_index=3
        mu,var,_=ie_law(p)
        other_mu,_,_=ie_law(tuple(x for i,x in enumerate(p) if i!=rare_index))
        low=1/p[rare_index]
        eq(low<=mu<=low+other_mu,True,f'rare coupon sandwich eps={epsilon}')
        results['rare_sign'][frac(epsilon)]={
            'mean_exact':frac(mu),'mean_rounded':round(float(mu),6),
            'p_rare':frac(p[rare_index]),'rare_wait_mean':frac(low),
            'excess_mean':frac(mu-low),'remaining_coupon_mean_bound':frac(other_mu),
            'ratio_mean_to_rare_wait':frac(mu/low)}
    results['checks']=checks
    results['verification']='ALL_CHECKS_PASS'
    Path('/mnt/data/PREFIX616_R6_RESULTS.json').write_text(
       json.dumps(results,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS',checks)
    for k,v in results['uniform'].items():
        print(k,'E',v['mean_rounded'],'Var',v['variance_rounded'],'N95',v['N95_min'],'N99',v['N99_min'])
    for k,v in results['asymmetric'].items():
        print(k,'E',v['mean_rounded'],'Var',v['variance_rounded'])
    for k,v in results['rare_sign'].items():
        print('eps',k,'E',v['mean_rounded'],'ratio',v['ratio_mean_to_rare_wait'])

if __name__=='__main__':main()
