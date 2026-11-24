#!/usr/bin/env python3
"""Exploration only: finite roots under several thickness regimes and grids."""
from pathlib import Path
from math import expm1,log,sqrt,fsum,isqrt
import argparse
import json
import mpmath as mp


def distinct_factors(limit):
    factors=[[] for _ in range(limit+1)]
    for p in range(2,limit+1):
        if not factors[p]:
            for n in range(p,limit+1,p):factors[n].append(p)
    return factors


def norm_interpolation(values,A,B,grid):
    energy=[];j=0
    for n in range(A,B+1):
        while j+1<len(grid)-1 and grid[j+1]<n:j+=1
        left,right=grid[j],grid[j+1]
        value=((right-n)*values[left]+(n-left)*values[right])/(right-left)
        energy.append((value/n)**2)
    return sqrt(fsum(energy))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('uniform_thickness_exploration.json'))
    args=parser.parse_args();mp.mp.dps=80
    maximum=16384;factors=distinct_factors(maximum);rows=[]
    for B in (256,1024,4096,16384):
        A=isqrt(B);L=log(B)
        regimes=[('1/B',1/B),('1/sqrt(B)',1/sqrt(B)),('1/log(B)^2',1/L**2),('1/log(B)',1/L),('1/sqrt(log(B))',1/sqrt(L)),('1/2',.5),('1',1.),('2',2.),('10',10.)]
        for name,a in regimes:
            am=mp.mpf(a);g=1/mp.zeta(1+am);delta=1-g/am
            gp=-mp.diff(mp.zeta,1+am)/mp.zeta(1+am)**2
            constant=1+mp.euler+(mp.euler-1)*g/am+(gp-1)/am
            e=[0.]*(B+1)
            for n in range(2,B+1):
                f=factors[n];prod=1.
                for p in f:prod*=-expm1(-a*log(p))
                e[n]=prod/a-(log(f[0]) if len(f)==1 else 0.)
            values=[0.]*(B+1);s0=0.;s1=0.
            for n in range(1,B+1):
                s0+=e[n];s1+=e[n]/n;values[n]=n*s1-s0
            main=float(delta)*sqrt(B)*L
            direct=sqrt(fsum((values[n]/n)**2 for n in range(A,B+1)))
            grids={'endpoints':[A,B],
                   'early_dense_then_endpoint':list(range(A,min(2*A,B)+1))+([B] if 2*A<B else []),
                   'dyadic':sorted({A,B,*[2**k for k in range(B.bit_length()) if A<2**k<B]})}
            ratios={key:norm_interpolation(values,A,B,grid)/main for key,grid in grids.items()}
            rows.append({'B':B,'A':A,'regime':name,'a_binary_float':a,'delta_high_precision':mp.nstr(delta,35),'constant_high_precision':mp.nstr(constant,35),'direct_root':direct,'normalized_direct_root':direct/main,'normalized_grid_roots':ratios,'endpoint_difference':values[B],'normalized_endpoint_difference':values[B]/(-float(delta)*B*L),'positive_difference_points':sum(values[n]>0 for n in range(A,B+1))})
    result={'schema':'EM_UNIFORM_SINGLE_THICKNESS_EXPLORATION_V1','status':'EXPLORATORY_FLOAT_NOT_INTERVAL_CERTIFICATE','source_arithmetic':'IEEE double with expm1 and a full factor sieve; main-term coefficients use mpmath 80 decimal digits','rows':rows,'scope':'Finite observations; does not validate the analytic uniform limit or provide a rigorous cutoff'}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'rows':len(rows),'all_difference_points_nonpositive':all(r['positive_difference_points']==0 for r in rows),'B16384':[{'regime':r['regime'],'root_ratio':r['normalized_direct_root'],'endpoint_ratio':r['normalized_endpoint_difference']} for r in rows if r['B']==16384]},ensure_ascii=False))


if __name__=='__main__':main()
