#!/usr/bin/env python3
"""PREFIX-657: frozen 189-layer exact BRC exterior variance witness."""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json

N, DEN=189,1<<18
L,Z=F(3,20),F(1,8)
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
BASE={12:(F('47425.459'),F('47425.460')),
      24:(F('192190.134'),F('192190.135'))}
checks=0
def ck(a,s):
    global checks
    assert a,s
    checks+=1

@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n

@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*DEN//n
    ck(inside(n,k,mid),'center is accepted')
    if k==0:ll=lh=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            m=(lo+hi)//2
            if inside(n,k,m):hi=m
            else:lo=m
        ll,lh=lo,hi
    lo,hi=mid,DEN
    while hi-lo>1:
        m=(lo+hi)//2
        if inside(n,k,m):lo=m
        else:hi=m
    rl,rh=lo,hi
    if 4*(rl-lh)>DEN:return True
    if 4*(rh-ll)<DEN:return False
    raise AssertionError(('ambiguous width',n,k))

def rows_make():
    state={0:1}
    rows=[state.copy()]
    for n in range(1,N+1):
        nxt=defaultdict(int)
        for k,v in state.items():
            nxt[k]+=v;nxt[k+1]+=v
        state={k:v for k,v in nxt.items() if wide(n,k)}
        rows.append(state.copy())
    ck(sum(rows[24].values())==2**24,'row 24 intact')
    ck(sum(rows[25].values())==2**25-2,'first losses at 25')
    ck(all(sum(rows[n].values())==2**n for n in range(25)),'pre-25 complete')
    ck(not rows[189],'row 189 extinct')
    return rows

def survival(rows,x):
    a,b=x.numerator,x.denominator
    return [F(sum(v*a**k*(b-a)**(n-k) for k,v in rows[n].items()),b**n)
            for n in range(N)]

def moments(s,t):
    mu=sum(s)+sum(t)
    H=sum((n+1)*(s[n]+t[n]) for n in range(N))
    for n in range(N):
        if not s[n]:continue
        for m in range(N):
            if not t[m]:continue
            x=F(comb(n+m,n),2**(n+m+1))*s[n]*t[m]
            mu-=x
            H-=F(n+m+1,2)*x
    return mu,2*H-mu*mu

def bounds(x):
    k=x.numerator*1000//x.denominator
    lo,hi=F(k,1000),F(k+1,1000)
    ck(lo<x<hi,'strict thousandth enclosure')
    return lo,hi

def main():
    ck(F(1,8)<L<F(1,6),'proper p region')
    ck(F(3008,7)<21**2,'score derivative 21')
    rows=rows_make()
    s,t=survival(rows,L),survival(rows,Z)
    ck(all(0<=v<=1 for v in s+t),'event probabilities')
    mu,W=moments(s,t)
    ck(0<mu<378,'Gamma sum mean bound')
    ck(W>0,'variance positive')
    h=F(1,2**19)
    Dmu=N*21
    DH=21*sum(range(1,N+1))
    DW=2*DH+2*378*Dmu
    ck((Dmu,DH,DW)==(3969,377055,3754674),'gradient constants')
    ck(F(1,8)<=L-h and L+h<=F(1,6)
       and Z+h<=F(1,6),'rectangle in score region')
    slot={}
    for q in (12,24):
        lo,hi=bounds(q*q*W-q*mu)
        b0,b1=BASE[q]
        gap=lo-b1
        lip=q*q*DW+q*Dmu
        loss=2*h*lip
        ck(gap>0 and gap>loss,'entire rectangle wins')
        slot[str(q)]={
          'witness_variance_interval_strict':[str(lo),str(hi)],
          'prior_box_max_interval_strict':[str(b0),str(b1)],
          'point_advantage_lower':str(gap),
          'sup_coordinate_derivative_bound':str(lip),
          'rectangle_loss_upper':str(loss),
          'rectangle_advantage_lower':str(gap-loss)}
    for q in (12,15,18,21,24):
        a=F(q-12,12)
        ck((1-a)*F(slot['12']['rectangle_advantage_lower'])/12+
           a*F(slot['24']['rectangle_advantage_lower'])/24>0,
           'affine interpolation')
    result={
      'schema':'EM_PREFIX657_COMPARATIVE_VARIANCE_RECTANGLE_V1',
      'frozen_science_pin':PIN,'layers':N,
      'witness':['3/20','1/8'],
      'competitor_rectangle':{'p':[str(L-h),str(L+h)],
                              'z':[str(Z),str(Z+h)]},
      'model_mean_interval':[str(v) for v in bounds(mu)],
      'model_variance_interval':[str(v) for v in bounds(W)],
      'gradient_certification_domain':['1/8','1/6'],
      'score_derivative_bound':'21',
      'one_coordinate_gradient_bounds':{'mu':str(Dmu),'H':str(DH),'W':str(DW)},
      'slots':slot,'checks_passed':checks,'result':'ALL_CHECKS_PASS',
      'arithmetic':'Python Fraction exact rational and integer dyadic bisection',
      'scope':'Full-domain consequence requires exact parent domain to contain C',
      'dependencies':['PREFIX643','PREFIX655','PREFIX656']
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS',checks)

if __name__=='__main__':main()
