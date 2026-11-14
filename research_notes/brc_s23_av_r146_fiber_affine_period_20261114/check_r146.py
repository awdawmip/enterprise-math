#!/usr/bin/env python3
"""R146 exact phase-fiber affine periodicity: independent rational regression."""
from fractions import Fraction as Q
from itertools import product
from math import floor, ceil, gcd, lcm
import json


def support(word):
    m = len(word)
    s = [0]
    for x in word:
        s.append(s[-1] + x)
    a, b = Q(0), Q(1)
    for i in range(m):
        for j in range(i+1, m+1):
            h, d = j-i, s[j]-s[i]
            a = max(a, Q(d-1, h))
            b = min(b, Q(d+1, h))
    if a >= b:
        return None
    u = min(Q(s[j]+1) - j*a for j in range(m+1))
    ell = max(Q(s[j]) - j*b for j in range(m+1))
    return a, b, u, ell


def fiber_count(data, L):
    a, b, u, ell = data
    A, B = L*a-u, L*b-ell
    return ceil(B) - floor(A) - 1


def chronological_counts(m, L):
    xs={Q(0), Q(1)}
    for n in range(L, L+m+1):
        if n:
            for k in range(1, n):
                xs.add(Q(k,n))
    xs=sorted(xs)
    seen=set()
    for i in range(len(xs)-1):
        t=(xs[i]+xs[i+1])/2
        f=[(n*t).numerator//(n*t).denominator for n in range(L,L+m+1)]
        seen.add((f[0], tuple(f[i+1]-f[i] for i in range(m))))
    counts={}
    for N,w in seen:
        counts[w]=counts.get(w,0)+1
    return counts


def main():
    stats=dict(words=0, membership_checks=0, period_checks=0, error_checks=0,
               direct_chronological_cases=0, direct_word_checks=0,
               tv_checks=0, max_abs_error='0', max_positive_error='0')
    maximum=Q(0)
    maxpositive=Q(0)
    for m in range(1,12):
        words={}
        for w in product((0,1), repeat=m):
            d=support(w)
            if d is not None:
                words[w]=d
        stats['words']+=len(words)
        for w,(a,b,u,ell) in words.items():
            assert 0 <= u-ell <= 1
            P=lcm(a.denominator,b.denominator)
            step=P*(b-a)
            assert step.denominator==1 and step>0
            for L in (1,2,7,31,10**55+123):
                C=fiber_count((a,b,u,ell),L)
                assert C>=0
                Cnext=fiber_count((a,b,u,ell),L+P)
                assert Cnext-C==step
                stats['period_checks']+=1
                error=C-L*(b-a)
                assert Q(-1)<=error<Q(2)
                maximum=max(maximum, abs(error))
                maxpositive=max(maxpositive,error)
                stats['error_checks']+=1
        for L in (1,4,11,10**55+123):
            vals={w:fiber_count(d,L) for w,d in words.items()}
            stats['membership_checks']+=len(vals)
            mass=sum(vals.values())
            assert (m+1)*L <= mass <= (m+1)*L+m*(m-1)//2
            widths=sum((d[1]-d[0] for d in words.values()), Q(0))
            assert widths==m+1
            tv=sum((abs(Q(C,mass)-(d[1]-d[0])/Q(m+1)) for w,C in vals.items() for d in (words[w],)),Q(0))/2
            bound=Q(len(words)+Q(m*(m-1),4),(m+1)*L)
            assert tv <= bound
            stats['tv_checks']+=1
        if m<=6:
            for L in range(1,10):
                direct=chronological_counts(m,L)
                assert set(direct).issubset(set(words))
                for w,d in words.items():
                    assert fiber_count(d,L)==direct.get(w,0),(m,L,w)
                    stats['direct_word_checks']+=1
                stats['direct_chronological_cases']+=1
    stats['max_abs_error']=str(maximum)
    stats['max_positive_error']=str(maxpositive)
    stats['signature']='R146_FIBER_AFFINE_PERIODICITY_PASS'
    print(json.dumps(stats,ensure_ascii=False,indent=2))


if __name__=='__main__': main()
