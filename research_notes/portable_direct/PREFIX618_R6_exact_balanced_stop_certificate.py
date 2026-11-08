#!/usr/bin/env python3
"""PREFIX-618 exact BRC signed-label stopping certificate, Python stdlib only.
Reuses PREFIX-617's d=2, beta=1/40, target p-diameter 1/4 observer.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import comb
from decimal import Decimal, localcontext
import json

D = 1 << 18  # roots certified inside dyadic mesh; any ambiguity raises
checks = 0

def inside(m, k, a):
    global checks
    checks += 1
    return 40*(m+1)*comb(m,k)*a**k*(D-a)**(m-k) > D**m

def wide(m, k):
    """Exact test that confidence-set diameter exceeds 1/4."""
    if k > m//2: return wide(m, m-k)
    mid = k*D//m
    assert inside(m,k,mid)
    if k == 0:
        left_lo = left_hi = 0
    else:
        lo, hi = 0, mid
        assert not inside(m,k,lo)
        while hi-lo > 1:
            x=(lo+hi)//2
            if inside(m,k,x): hi=x
            else: lo=x
        left_lo,left_hi=lo,hi
    lo,hi=mid,D
    assert not inside(m,k,hi)
    while hi-lo > 1:
        x=(lo+hi)//2
        if inside(m,k,x): lo=x
        else: hi=x
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>D: return True
    if 4*(right_hi-left_lo)<D: return False
    raise AssertionError('Need finer dyadic precision at m,k='+str((m,k)))

def survival():
    """A[m] counts fair sign-prefixes of length m surviving after m."""
    alive={0:1}; A=[1]; first=None
    for m in range(1,321):
        candidates=defaultdict(int)
        for k,v in alive.items():
            candidates[k]+=v; candidates[k+1]+=v
        alive={}; stopped=0
        for k,v in candidates.items():
            if wide(m,k): alive[k]=v
            else: stopped+=v
        A.append(sum(alive.values()))
        if stopped and first is None: first=m
        if not alive:
            return A,first,m
    raise AssertionError('No finite stopping certificate')

def mean_two_directions(A):
    """Poissonization of two independent direction-sign streams."""
    M=len(A)-1
    E1=sum((Q(a,2**m) for m,a in enumerate(A)), Q(0))
    cross=sum((Q(a*b*comb(m+n,m),2**(2*m+2*n+1))
              for m,a in enumerate(A) for n,b in enumerate(A) if a and b),Q(0))
    return E1, 2*E1-cross

A,first,last=survival()
assert (first,last,A[-1])==(25,189,0)
assert wide(188,94) and all(not wide(189,k) for k in range(190))
E1,mu=mean_two_directions(A)
assert E1>0 and mu>E1
r = 189
quota = 2*r - sum((Q(comb(a+b,a),2**(a+b+1))
                  for a in range(r) for b in range(r)),Q(0))
assert quota>mu
with localcontext() as ctx:
    ctx.prec=30
    dec=lambda v: str(Decimal(v.numerator)/Decimal(v.denominator))
    result=dict(schema='PREFIX618_R6_EXACT_BALANCED_V1', science_pin='f42f2906d77f24085c123f3ccfe9667d41caa96d',
      parameters=dict(d=2,beta='1/40',p=['1/2','1/2'],diameter='1/4',q=[12,24]),
      earliest_informative_stop=first, uniform_informative_stop=last,
      E_one_direction_informative_samples=str(E1), E_q12_native_trials=str(12*mu),
      E_q24_native_trials=str(24*mu), E_q12_decimal=dec(12*mu), E_q24_decimal=dec(24*mu),
      E_q12_uniform_189_count_quota=str(12*quota), E_q12_uniform_189_count_quota_decimal=dec(12*quota),
      E_q12_saving_from_sign_adaptive=dec(12*(quota-mu)),
      exact_integer_inequality_checks=checks, dyadic_grid_denominator=D, verification='ALL_CHECKS_PASS',
      scope='Exact finite prefix enumeration and exact Poisson integral in PREFIX-617 signed-label experiment')
print(json.dumps(result,indent=2))
