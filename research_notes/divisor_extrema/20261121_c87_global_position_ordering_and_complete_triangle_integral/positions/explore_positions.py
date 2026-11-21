#!/usr/bin/env python3
"""Exploratory quadrature of the entire C87 position curve.

The exact chamber formula is evaluated stably near x=0 by its binomial
remainder after the identically vanishing constant and linear terms.
These floating values are observations, not interval certificates.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import argparse
import json
import math
import time

import numpy as np

HERE=Path(__file__).resolve().parent
LD=np.longdouble
P=LD(41)/20
GAMMA=LD(1)/20
CUTS=(0.,1/3,.5,2/3,1.)
C=2/((math.pi**2/6)*.95*1.05*2.05)
DATA=json.loads((HERE/'mellin_chambers.json').read_text())
TERMS={(ch['r_index'],ch['s_index']):[
       tuple(LD(F(t[k]).numerator)/F(t[k]).denominator
             for k in ('a_r','b_s','c_rs','weight'))for t in ch['terms']]
       for ch in DATA['chambers']}
BINOM=[LD(1)]
for k in range(1,30):BINOM.append(BINOM[-1]*(P-k+1)/k)
A2=float(F(211,244))*2**(-.05)-float(F(101,122))*4**(-.05)+float(F(23,61))


def index(v):return sum(v>=q for q in CUTS[1:-1])


def normalized_h(rows,r,x):
    """H(r,x)/x^2, avoiding cancellation as x tends to zero."""
    result=np.zeros_like(r,dtype=LD)
    if x<=LD(1)/8:
        for a,b,c,w in rows:
            t=b+c*r
            if a==0:
                result+=w*np.abs(t)**P*x**GAMMA
            else:
                z=t*x/a
                remainder=np.zeros_like(r,dtype=LD)
                for coefficient in reversed(BINOM[2:]):
                    remainder=remainder*z+coefficient
                result+=w*a**GAMMA*t*t*remainder
    else:
        for a,b,c,w in rows:
            result+=w*np.abs(a+(b+c*r)*x)**P
        result/=x*x
    return result


@lru_cache(None)
def nodes(n):
    a,b=np.polynomial.legendre.leggauss(n)
    return a.astype(LD),b.astype(LD)


def averaged_normalized(x,n):
    if x==0:return A2
    x=LD(x)
    bounds=sorted(set(list(CUTS)+[q/float(x)for q in CUTS[1:-1]if q<float(x)]))
    total=LD(0)
    v,w=nodes(n)
    for lo,hi in zip(bounds,bounds[1:]):
        ri=index((lo+hi)/2);si=index(float(x)*(lo+hi)/2)
        rows=TERMS[ri,si]
        splits={LD(lo),LD(hi)}
        for a,b,c,coefficient in rows:
            if c:
                zero=-(a+b*x)/(c*x)
                if lo<zero<hi:splits.add(zero)
        splits=sorted(splits)
        for a,b in zip(splits,splits[1:]):
            r=(a+b+(b-a)*v)/2
            total+=(b-a)/2*np.sum(w*r**GAMMA*normalized_h(rows,r,x),dtype=LD)
    return float(total)


def position(theta,n):
    q=theta/(1-theta)
    breaks={q,1.}
    # Changes in the order of r and rx chamber boundaries.
    for a in CUTS[1:]:
        for b in CUTS[1:]:
            x=a/b
            if q<x<1:breaks.add(x)
    # A zero of a power argument meeting a chamber edge can change the
    # radial sign partition. Include all such possible outer breakpoints.
    for rows in TERMS.values():
        for a,b,c,w in rows:
            for r in CUTS:
                if b+c*r:
                    x=float(-a/(b+c*r))
                    if q<x<1:breaks.add(x)
            for s in CUTS:
                if b:
                    x=float(-(a+c*s)/b)
                    if q<x<1:breaks.add(x)
    v,w=nodes(n)
    gap=slope=LD(0)
    breaks=sorted(breaks)
    for lo,hi in zip(breaks,breaks[1:]):
        # x=t^20 resolves the weak x^(1/20) behavior at the endpoint.
        a,b=LD(lo)**GAMMA,LD(hi)**GAMMA
        t=(a+b+(b-a)*v)/2
        x=t**20
        weights=(b-a)/2*w*20*t**19
        av=np.array([averaged_normalized(xx,n)for xx in x],dtype=LD)
        gap+=np.sum(weights*((1-theta)*x-theta)*av,dtype=LD)
        slope+=np.sum(weights*(1+x)*av,dtype=LD)
    aq=averaged_normalized(q,n)
    return {'theta':theta,'I_theta_minus_mid':float(-C*gap),
            'first_derivative':float(C*slope),
            'second_derivative':float(-C*(1+q)**3*aq),
            'A_over_x_squared_at_q':aq}


def run(n):
    start=time.time()
    positions=[0.,1/64,1/32,1/16,1/10,1/8,1/6,1/5,1/4,1/3,2/5,9/20,49/100,.5]
    values=[position(theta,n)for theta in positions]
    out={'schema':'C87_POSITION_EXPLORATION_V1','status':'exploratory_not_certified',
         'gauss_order_each_axis':n,'stable_axis_series_terms':len(BINOM)-2,
         'values':values,'seconds':time.time()-start}
    (HERE/f'position_exploration_{n}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    return out


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--n',type=int,default=32)
    args=ap.parse_args()
    run(args.n)
