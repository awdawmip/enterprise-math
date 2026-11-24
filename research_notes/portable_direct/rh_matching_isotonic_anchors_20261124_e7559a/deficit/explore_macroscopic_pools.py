#!/usr/bin/env python3
"""Exploratory double-precision PAV geometry on midpoint and seam hats.

This is an experiment, not outward numerical certification.  The input universe
is every integer through 2^20 with actual ordinary-prime logarithmic weights.
The two drift parameters are exactly 0 and 1/ceil(sqrt(L)); conversion to double
occurs only inside this explicitly exploratory computation.
"""
from array import array
from bisect import bisect_left,bisect_right
from fractions import Fraction
from math import isqrt,log,fsum,sqrt
from pathlib import Path
import argparse,json


def pav(A,L,R,drift):
    pools=[]
    for n in range(L,R):
        mass=1.0/n-1.0/(n+1)
        pools.append([n,n+1,mass,mass*(A[n]+drift*n)])
        while len(pools)>1:
            a,b=pools[-2:]
            if a[3]/a[2]<=b[3]/b[2]:
                break
            pools[-2:]=[[a[0],b[1],a[2]+b[2],a[3]+b[3]]]
    return pools


def hat(n,L,x,R):
    return (n-L)/(x-L) if n<=x else (R-n)/(R-x)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-power',type=int,default=20)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('macroscopic_exploration.json'))
    args=parser.parse_args()
    B=2**args.max_power
    sieve=bytearray(b'\x01')*(B+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(B)+1):
        if sieve[p]:sieve[p*p::p]=b'\x00'*((B-p*p)//p+1)
    primes=[n for n in range(2,B+1) if sieve[n]]
    A=array('d',[0.0])*(B+1)
    theta=correction=0.0
    for n in range(1,B+1):
        if sieve[n]:
            y=log(n)-correction
            updated=theta+y
            correction=(updated-theta)-y
            theta=updated
        A[n]=theta-n
    packets=[]
    for j in range(10,args.max_power):
        L=2**j
        packets.append(('midpoint',L,3*L//2,2*L))
    for j in range(9,args.max_power):
        L,x,R=3*2**j,4*2**j,6*2**j
        if R<=B:packets.append(('seam',L,x,R))
    rows=[]
    for kind,L,x,R in packets:
        a,b,h=x-L,R-x,R-L
        background=fsum(hat(n,L,x,R)/n for n in range(L+1,R))
        prime_mass=fsum(hat(p,L,x,R)*log(p)/p for p in primes[bisect_right(primes,L):bisect_left(primes,R)])
        tau=background-prime_mass
        root=max(0.0,tau)*h**1.5/L
        q=isqrt(L)
        q+=q*q<L
        for drift_f in (Fraction(0),Fraction(1,q)):
            drift=float(drift_f)
            pools=pav(A,L,R,drift)
            crossing=next((pool for pool in pools if pool[0]<x<pool[1]),None)
            if crossing:
                u,v,mass,sum_a=crossing
                g=v-u
                pool_mean=sum_a/mass
                S=fsum((A[n]+drift*n-pool_mean)/(n*(n+1)) for n in range(u,x))
                residual_tau=h*x*S/(a*b)
                geometry_tau=(1-drift)*h*(x-u)*(v-x)/(2*a*b*u)
                pool_variance=fsum((A[n]+drift*n-pool_mean)**2/(n*(n+1)) for n in range(u,v))
                variance_tau=sqrt(max(0.0,h*h*(x-u)*(v-x)*pool_variance/(a*a*b*b*g)))
            else:
                u=v=x
                g=0
                residual_tau=geometry_tau=variance_tau=0.0
            chi=Fraction(h*h,4*a*b)
            drift_root=drift*background*h**1.5/L
            rows.append({'kind':kind,'L':L,'x':x,'R':R,'drift_exact':str(drift_f),
                         'pool_count':len(pools),'crossing_pool':[u,v],'G':g,'G_over_H':g/h,
                         'G_over_L_3_4':g/L**0.75,'chi_exact':str(chi),
                         'tau':tau,'true_positive_root_budget':root,
                         'crossing_residual_root_with_drift':max(0.0,residual_tau)*h**1.5/L+drift_root,
                         'crossing_variance_root_with_drift':variance_tau*h**1.5/L+drift_root,
                         'local_geometry_root_with_drift':geometry_tau*h**1.5/L+drift_root,
                         'max_geometry_root_with_drift':((1-drift)*float(chi)*g*g+drift*h*h)/(2*L**1.5),
                         'drift_root_payment':drift_root,
                         'computed_trend_contribution':tau-drift*background-residual_tau})
    result={'schema':'RH_MACROSCOPIC_POOL_EXPLORATION_V1','status':'EXPLORATORY_DOUBLE_PRECISION',
            'certified':False,'arithmetic':'IEEE double, Kahan cumulative theta, fsum reported local sums',
            'sieve_limit':B,'prime_count':len(primes),'packets':len(packets),'parameter_cases':len(rows),
            'scope':'Fixed dyadic midpoint and interlaced seam hats; no scaling theorem or certified endpoints.',
            'rows':rows}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'sieve_limit':B,'packets':len(packets),
                      'parameter_cases':len(rows),'rows':rows[-8:]},ensure_ascii=False))


if __name__=='__main__':main()
