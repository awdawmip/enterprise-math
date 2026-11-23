#!/usr/bin/env python3
"""Certified harmonic-envelope energy from sparse samples and endpoint moments.

All numerical arithmetic is outward integer intervals.  Only the first 256
harmonic terms are accumulated; subsequent H_n,H_n^(2) use finite
Euler--Maclaurin with an explicit rational remainder.  No full q cache is read.
"""
from fractions import Fraction as F
from functools import cache
from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import time

DIGITS = 80
S = 10**DIGITS
ZERO = (0, 0)
ONE = (S, S)
ANCHOR = 256
ORDER = 24
LOG_TERMS = 100


def ceildiv(a, b):
    return -((-a)//b)


def rat(x):
    x = F(x)
    return x.numerator*S//x.denominator, ceildiv(x.numerator*S, x.denominator)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def qmul(x, p, q=1):
    if isinstance(p, F):
        p, q = p.numerator, p.denominator*q
    if p < 0:
        return neg(qmul(x, -p, q))
    return x[0]*p//q, ceildiv(x[1]*p, q)


def mul(x, y):
    v = (x[0]*y[0], x[0]*y[1], x[1]*y[0], x[1]*y[1])
    return min(v)//S, ceildiv(max(v), S)


def square(x):
    a = 0 if x[0] <= 0 <= x[1] else min(x[0]**2, x[1]**2)
    return a//S, ceildiv(max(x[0]**2, x[1]**2), S)


def positive(x):
    return max(x[0], 0), max(x[1], 0)


def total(xs):
    lo = hi = 0
    for x in xs:
        lo += x[0]
        hi += x[1]
    return lo, hi


def overlap(x, y):
    return max(x[0], y[0]) <= min(x[1], y[1])


def decode(z):
    p = z['denominator_power_of_10']
    return tuple(int(v)*10**(DIGITS-p) for v in z['integer_bounds'])


def decimal(n, places=35, up=False):
    unit = 10**(DIGITS-places)
    v = ceildiv(n, unit) if up else n//unit
    sign = '-' if v < 0 else ''
    v = abs(v)
    return f'{sign}{v//10**places}.{v%10**places:0{places}d}'


def record(v):
    return {'lower':decimal(v[0]), 'upper':decimal(v[1], up=True),
            'integer_bounds':list(map(str, v)), 'denominator_power_of_10':DIGITS,
            'width_upper':str(F(v[1]-v[0], S))}


def bernoulli(nmax):
    b = [F(1)]
    for n in range(1, nmax+1):
        b.append(-sum((comb(n+1,k)*b[k] for k in range(n)), F(0))/(n+1))
    return b


BERNOULLI = bernoulli(2*ORDER)
# |B_m({x})| <= sum of absolute polynomial coefficients on [0,1].
BERNOULLI_SUP = sum((comb(2*ORDER,k)*abs(BERNOULLI[k])
                    for k in range(2*ORDER+1)), F(0))
LOW_H = [ZERO]
LOW_H2 = [ZERO]
for _n in range(1, ANCHOR+1):
    LOW_H.append(add(LOW_H[-1], rat(F(1,_n))))
    LOW_H2.append(add(LOW_H2[-1], rat(F(1,_n*_n))))


def log_unit(n, d):
    """ln(n/d), 1<=n/d<=2, by finite atanh and geometric tail."""
    z = F(n-d, n+d)
    term = rat(z)
    z2 = z*z
    result = ZERO
    for k in range(LOG_TERMS):
        result = add(result, qmul(term, 2, 2*k+1))
        term = qmul(term, z2)
    bound = F(2, 2*LOG_TERMS+1)*z**(2*LOG_TERMS+1)/(1-z2)
    return result[0], result[1]+rat(bound)[1]


LOG_TWO = log_unit(2, 1)


@cache
def log_int(n):
    k = n.bit_length()-1
    return add(qmul(LOG_TWO,k),log_unit(n, 1<<k))


@cache
def harmonics(n):
    if n <= ANCHOR:
        return LOW_H[n], LOW_H2[n]
    m = ANCHOR
    h = add(LOW_H[m], sub(log_int(n), log_int(m)))
    h = add(h, rat(F(1,2*n)-F(1,2*m)))
    h2 = add(LOW_H2[m], rat(F(1,m)-F(1,n)+F(1,2*n*n)-F(1,2*m*m)))
    for j in range(1, ORDER+1):
        bj = BERNOULLI[2*j]
        h = add(h, rat(bj/F(2*j)*(F(1,m**(2*j))-F(1,n**(2*j)))))
        h2 = add(h2, rat(bj*(F(1,m**(2*j+1))-F(1,n**(2*j+1)))))
    # Euler--Maclaurin remainder after the displayed ORDER terms.
    eh = rat(BERNOULLI_SUP/F(2*ORDER)*(F(1,m**(2*ORDER))-F(1,n**(2*ORDER))))[1]
    eh2 = rat(BERNOULLI_SUP*(F(1,m**(2*ORDER+1))-F(1,n**(2*ORDER+1))))[1]
    return (h[0]-eh,h[1]+eh), (h2[0]-eh2,h2[1]+eh2)


@cache
def moments(n):
    h, h2 = harmonics(n)
    return (rat(n), h, h2, sub(qmul(h,n+1),rat(n)),
            qmul(add(square(h),h2),1,2),
            add(sub(qmul(square(h),n+1),qmul(h,2*n+1)),rat(2*n)))


def coefficients(left,right,ql,qr,c):
    yl = add(ql,qmul(harmonics(left)[0],c*left))
    yr = add(qr,qmul(harmonics(right)[0],c*right))
    a = qmul(sub(yr,yl),1,right-left)
    b = sub(yl,qmul(a,left))
    return a,b


def value(n,a,b,c):
    return sub(add(qmul(a,n),b),qmul(harmonics(n)[0],c*n))


def sign(x):
    if x[0] > 0:
        return 1
    if x[1] <= 0:
        return -1
    raise ArithmeticError('Sign remains undecided at fixed precision; no tolerance decision is made.')


def concave_positive_segment(left,right,a,b,c):
    if left > right:
        return None
    assert c > 0
    lo,hi=left,right
    while lo < hi:
        mid=(lo+hi)//2
        delta=sub(a,qmul(add(harmonics(mid)[0],ONE),c))
        if sign(delta) < 0:
            hi=mid
        else:
            lo=mid+1
    peak=lo
    if sign(value(peak,a,b,c)) < 0:
        return None
    lo,hi=left,peak
    while lo < hi:
        mid=(lo+hi)//2
        if sign(value(mid,a,b,c)) > 0:
            hi=mid
        else:
            lo=mid+1
    first=lo
    lo,hi=peak,right
    while lo < hi:
        mid=(lo+hi+1)//2
        if sign(value(mid,a,b,c)) > 0:
            lo=mid
        else:
            hi=mid-1
    return first,lo


def positive_segments(left,right,a,b,c):
    if left > right:
        return []
    if c > 0:
        v=concave_positive_segment(left,right,a,b,c)
        return [] if v is None else [v]
    v=concave_positive_segment(left,right,neg(a),neg(b),-c)
    if v is None:
        return [(left,right)]
    return [(lo,hi) for lo,hi in [(left,v[0]-1),(v[1]+1,right)] if lo<=hi]


def segment_energy(left,right,a,b,c):
    ds=[sub(u,v) for u,v in zip(moments(right),moments(left-1))]
    s0,s1,s2,t0,t1,t2=ds
    return positive(total([mul(square(a),s0),mul(square(b),s2),qmul(t2,c*c),
        qmul(mul(mul(a,b),s1),2),qmul(mul(a,t0),-2*c),qmul(mul(b,t1),-2*c)]))


def cell_energy(left,right,ql,qr,c):
    a,b=coefficients(left,right,ql,qr,c)
    segments=positive_segments(left+1,right-1,a,b,c)
    return add(total(segment_energy(lo,hi,a,b,c) for lo,hi in segments),
               qmul(square(positive(qr)),1,right*right)),segments


def evaluate_partition(nodes,values,c):
    e=qmul(square(positive(values[nodes[0]])),1,nodes[0]**2)
    segments=[]
    for l,r in zip(nodes,nodes[1:]):
        v,support=cell_energy(l,r,values[l],values[r],c)
        e=add(e,v)
        segments.append({'cell':[l,r],'positive_segments':support})
    return e,segments


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--old-certificate',type=Path,required=True)
    parser.add_argument('--scan-check',action='store_true')
    args=parser.parse_args()
    doc=json.loads(args.input.read_text())
    old=json.loads(args.old_certificate.read_text())
    data={x['n']:decode(x['value']) for x in doc['samples']}
    nodes=sorted(data)
    aa,bb=doc['window']['A'],doc['window']['B']
    c=1+F(1,2*aa*aa)+F(1,10**6)
    start=time.perf_counter()
    eu,su=evaluate_partition(nodes,data,c)
    el,sl=evaluate_partition(nodes,data,F(-12))
    elapsed=time.perf_counter()-start
    assert overlap(eu,decode(old['final_upper_energy']))
    assert overlap(el,decode(old['final_lower_energy']))
    computed=harmonics.cache_info().misses
    output={'status':'PASS','arithmetic':'outward integer intervals; no floating-point sign tests',
      'decimal_digits':DIGITS,'harmonic_anchor':ANCHOR,'euler_maclaurin_order':ORDER,
      'log_series_terms':LOG_TERMS,'input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),
      'window':[aa,bb],'sample_count':len(nodes),'cell_count':len(nodes)-1,
      'upper_energy':record(eu),'lower_energy':record(el),
      'new_result_intersects_both_previous_exact_certificates':True,
      'harmonic_distinct_arguments':computed,'endpoint_moment_arguments':moments.cache_info().misses,
      'initial_harmonic_terms':ANCHOR,'energy_time_seconds':elapsed,
      'source_input':'Only existing 1270-point sample file; original full road not read.',
      'upper_supports':su,'lower_supports':sl,
      'scope':'Finite certified energy aggregation. It does not accelerate generating q samples.'}
    if args.scan_check:
        start=time.perf_counter()
        hs=[ZERO]
        h2s=[ZERO]
        for n in range(1,bb+1):
            hs.append(add(hs[-1],rat(F(1,n))))
            h2s.append(add(h2s[-1],rat(F(1,n*n))))
        # A genuinely separate harmonic construction checks every queried argument.
        harmonic_checks=0
        for n in range(aa-1,bb+1):
            if n in nodes or n in (aa-1,bb):
                assert overlap(harmonics(n)[0],hs[n])
                assert overlap(harmonics(n)[1],h2s[n])
                harmonic_checks+=1
        direct=[]
        for cc in [c,F(-12)]:
            e=qmul(square(positive(data[aa])),1,aa*aa)
            for left,right in zip(nodes,nodes[1:]):
                h=right-left
                for n in range(left+1,right):
                    chord=add(qmul(data[left],right-n,h),qmul(data[right],n-left,h))
                    hp=sub(add(qmul(hs[left],left*(right-n),h),
                               qmul(hs[right],right*(n-left),h)),qmul(hs[n],n))
                    v=add(chord,qmul(hp,cc))
                    e=add(e,qmul(square(positive(v)),1,n*n))
                e=add(e,qmul(square(positive(data[right])),1,right*right))
            direct.append(e)
        assert overlap(eu,direct[0]) and overlap(el,direct[1])
        output['scan_comparison']={'time_seconds':time.perf_counter()-start,
           'harmonic_checks':harmonic_checks,'integer_values_scanned':2*(bb-aa+1),
           'both_energy_intervals_intersect':True,'upper':record(direct[0]),'lower':record(direct[1])}
    # A billion-interior-point synthetic cell, with all population mass retained.
    left=10**12;right=left+10**9
    start=time.perf_counter()
    before=harmonics.cache_info().misses
    ebig,sbig=cell_energy(left,right,ZERO,ZERO,F(1))
    h=right-left
    lb=F(h**5-h,120*right**4)
    ub=F(h**5-h,120*left**4)
    assert ebig[0]>=rat(lb)[0] and ebig[1]<=rat(ub)[1]
    output['billion_gap']={'cell':[left,right],'interior_integer_count':h-1,
       'harmonic_distinct_arguments':harmonics.cache_info().misses-before,
       'energy':record(ebig),'elementary_lower':str(lb),'elementary_upper':str(ub),
       'positive_segments':sbig,'time_seconds':time.perf_counter()-start}
    output['max_harmonic_remainder']={'H':str(BERNOULLI_SUP/F(2*ORDER*ANCHOR**(2*ORDER))),
       'H2':str(BERNOULLI_SUP/F(ANCHOR**(2*ORDER+1)))}
    target=Path(__file__).with_name('fast_harmonic_energy_certificate.json')
    target.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ['status','sample_count','upper_energy','lower_energy',
          'harmonic_distinct_arguments','endpoint_moment_arguments','energy_time_seconds','billion_gap']},ensure_ascii=False))


if __name__=='__main__':
    main()
