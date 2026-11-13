#!/usr/bin/env python3
"""R129.4: gcd-normalized S23 one-parameter exact event enumeration.
Only stdlib exact Fraction; signed coefficients and strict open theta interval.
"""
from fractions import Fraction as F
from math import gcd
from random import Random
from pathlib import Path
import json
from check_r129 import frac, integer_crossings, integer_crossings_interval, interval_witness


def gcd3(A,d,E):
    return gcd(gcd(abs(A),abs(d)),abs(E))


def normalized_word(beta,x,a,q,e,m):
    t=frac(e*beta)
    return ''.join('1' if frac(x+(a+i*q)*beta)<t else '0' for i in range(m))


def normalized_critical(x,a,q,e,m):
    roots=integer_crossings(F(0),e)
    for i in range(m):
        t=a+i*q
        roots.update(integer_crossings(x,t))
        roots.update(integer_crossings(x,t-e))
    return sorted(roots)


def general_words(x,A,d,E,m,l,h):
    x,l,h=F(x),F(l),F(h)
    assert m>=1 and l<h
    g=gcd3(A,d,E)
    if g==0:
        # Threshold {E theta}=0, so every strict bit is false.
        return {'0'*m:(l+h)/2}, 0, 0
    a,q,e=A//g,d//g,E//g
    roots=normalized_critical(x,a,q,e,m)
    B=max(abs(e)-1,0)+sum(abs(a+i*q)+abs(a+i*q-e) for i in range(m))
    assert len(roots)<=B
    cuts=sorted(set([F(0),F(1)] + roots + [frac(g*l),frac(g*h)]))
    probes=[beta for beta in cuts if beta<1]+[(u+v)/2 for u,v in zip(cuts,cuts[1:])]
    result={}
    for beta in probes:
        theta=interval_witness(beta,l,h,g)
        if theta is None:
            continue
        word=normalized_word(beta,x,a,q,e,m)
        assert word==''.join('1' if frac(x+(A+i*d)*theta)<frac(E*theta) else '0'
                             for i in range(m))
        result.setdefault(word,theta)
    assert len(result) <= 2*len(roots)+2
    return result,len(roots),B


def raw_oracle(x,A,d,E,m,l,h):
    roots=integer_crossings_interval(F(0),E,l,h)
    for i in range(m):
        roots |= integer_crossings_interval(x,A+i*d,l,h)
        roots |= integer_crossings_interval(x,A+i*d-E,l,h)
    roots=sorted(v for v in roots if l<v<h)
    cuts=[l]+roots+[h]
    probes=roots+[(u+v)/2 for u,v in zip(cuts,cuts[1:])]
    return {''.join('1' if frac(x+(A+i*d)*theta)<frac(E*theta) else '0'
                    for i in range(m)) for theta in probes}


def run():
    rng=Random(129420261113)
    ordinary=200
    huge=24
    rank_one=100
    event_sum=0
    root_sum=0
    for z in range(ordinary+huge):
        m=rng.randrange(1,9)
        a=rng.randrange(-5,6);q=rng.randrange(-5,6);e=rng.randrange(-5,6)
        x=F(rng.randrange(-7,8),rng.randrange(1,8))
        scale=rng.choice([1,2,3,5,8]) if z<ordinary else 10**rng.randrange(30,102)
        A,d,E=a*scale,q*scale,e*scale
        g=gcd3(A,d,E)
        l=F(rng.randrange(-6,7),rng.randrange(1,6))
        width=F(rng.randrange(1,9),rng.randrange(1,6)) if z<ordinary else F(rng.randrange(1,4),max(1,g))
        h=l+width
        got,K,B=general_words(x,A,d,E,m,l,h)
        expected=raw_oracle(x,A,d,E,m,l,h)
        assert set(got)==expected,(z,A,d,E,m,x,l,h,sorted(got),sorted(expected))
        event_sum+=K
        root_sum+=B

    # Exact agreement with prior R129 rank-one special family, both signs of d.
    from check_r129 import interval_words
    for z in range(rank_one):
        m=rng.randrange(2,9)
        s=rng.randrange(-5,6);r=rng.randrange(-5,6)
        d=rng.choice([-7,-4,-3,-2,-1,1,2,4,5])
        A=s*d;E=r*d
        x=F(rng.randrange(-7,8),rng.randrange(1,8))
        l=F(rng.randrange(-5,6),rng.randrange(1,6))
        h=l+F(rng.randrange(1,8),rng.randrange(1,6))
        old,_=interval_words(x,s,r,d,m,l,h)
        new,_,_=general_words(x,A,d,E,m,l,h)
        assert set(old)==set(new)

    # Numerical magnitude of the common gcd is irrelevant to beta event count.
    profile=[]
    for scale in (1,10**20,10**80,10**160):
        A,d,E=2*scale,3*scale,5*scale
        x=F(1,3)
        results,K,B=general_words(x,A,d,E,12,F(0),F(1,scale))
        assert results
        profile.append({'scale_digits':len(str(scale)),'critical_roots':K,'bound':B,'word_count':len(results)})
    assert len({p['critical_roots'] for p in profile})==1
    assert len({p['word_count'] for p in profile})==1

    result={'status':'R129_GCD_NORMALIZED_PASS','seed':129420261113,'ordinary_exact_theta_cases':ordinary,
            'huge_scale_exact_theta_cases':huge,'rank_one_equivalence_cases':rank_one,
            'critical_root_total':event_sum,'critical_root_bound_total':root_sum,
            'scale_invariance_profile':profile,'arithmetic':'fractions.Fraction',
            'scope':'all rational x,l,h, integer A,d,E,m>=1; original S23 auxiliary Boolean observer'}
    with Path(__file__).with_name('verification_r129_gcd.json').open('w',encoding='utf8') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    run()
