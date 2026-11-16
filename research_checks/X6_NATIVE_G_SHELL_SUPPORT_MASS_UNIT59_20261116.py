#!/usr/bin/env python3
"""Exact support-resolved signed X6 native quadratic-shell/BRC census (unit 59).
Frozen P000 V5: Z^6 signed primitive unit-axis steps; G=sum z_i^2;
T=sum |z_i|; N_BRC=T!/prod |z_i|!, no signed cancellation.
Two independent integer algorithms: coordinate DP and nondecreasing square partitions.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb, factorial, isqrt
import json, hashlib, sys

GMAX = 512
D = 6

def coordinate_dp():
    state = {(0,0,0):(1,1)} # (g,t,s) -> (#endpoints, natural BRC mass)
    for d in range(D):
        nxt = defaultdict(lambda:[0,0])
        for (g,t,s),(c,m) in state.items():
            for a in range(isqrt(GMAX-g)+1):
                g2=g+a*a; t2=t+a; s2=s+(a!=0)
                q=2 if a else 1
                v=nxt[g2,t2,s2]
                v[0]+=q*c
                v[1]+=q*m*comb(t2,a)
        state = {k:tuple(v) for k,v in nxt.items()}
    agg=defaultdict(lambda:[0,0])
    for (g,t,s),(c,m) in state.items():
        a=agg[g,s]
        a[0]+=c; a[1]+=m
    return {k:tuple(v) for k,v in agg.items()}

def partition_census():
    out=defaultdict(lambda:[0,0])
    fac6=factorial(D)
    def visit(mags, start, g, tsum, prod_fac):
        s=len(mags)
        if s:
            # Embeddings of a multiset of signed nonzero magnitudes on labeled axes.
            multiplicity_den=1
            j=0
            while j<s:
                k=j+1
                while k<s and mags[k]==mags[j]:k+=1
                multiplicity_den*=factorial(k-j)
                j=k
            number=(fac6//factorial(D-s))//multiplicity_den * (2**s)
            brc=factorial(tsum)//prod_fac
            out[g,s][0]+=number
            out[g,s][1]+=number*brc
        else:
            out[0,0]=[1,1]
        if s>=D:return
        for a in range(start,isqrt(GMAX-g)+1):
            visit(mags+(a,),a,g+a*a,tsum+a,prod_fac*factorial(a))
    visit((),1,0,0,1)
    return {k:tuple(v) for k,v in out.items()}

def shell(agg,g):
    rows=[]
    for s in range(0,D+1):
        c,m=agg.get((g,s),(0,0))
        if c:rows.append({'support':s,'endpoints':c,'natural_brc_mass':m})
    return {'g':g,'by_support':rows,'endpoints':sum(row['endpoints'] for row in rows),
            'natural_brc_mass':sum(row['natural_brc_mass'] for row in rows),
            'two_axis_endpoints':sum(row['endpoints'] for row in rows if row['support']<=2),
            'two_axis_brc_mass':sum(row['natural_brc_mass'] for row in rows if row['support']<=2)}

def main():
    dp=coordinate_dp()
    pp=partition_census()
    if dp != pp:
        failures=[(k,dp.get(k),pp.get(k)) for k in set(dp)|set(pp) if dp.get(k)!=pp.get(k)]
        raise RuntimeError(f'Independent methods disagree: {failures[:8]}')
    shells=[shell(dp,g) for g in range(GMAX+1)]
    # Prior unit58 frozen observed exact result, consistency check only.
    if shells[25]['endpoints']!=7812 or shells[25]['natural_brc_mass']!=2538954612:
        raise RuntimeError('Unit58 signed G25 cross-check failure')
    if shells[25]['two_axis_brc_mass']!=4212:
        raise RuntimeError('Unit46/58 support<=2 cross-check failure')
    # Geometric lower bound: a vector with s nonzero axes has G>=s.
    for v in shells:
        for row in v['by_support']:
            if v['g']<row['support']:
                raise RuntimeError('Support lower bound violated')
    positive=[v for v in shells[1:] if v['endpoints']]
    positive_with_high_support=[v for v in positive if v['endpoints']>v['two_axis_endpoints']]
    first=positive_with_high_support[0]['g'] if positive_with_high_support else None
    if first!=3:raise RuntimeError(f'Unexpected first positive >=3-support shell {first}')
    # Unit1 support parity and signed axis symmetry.
    for v in positive:
        if v['endpoints']%2 or v['natural_brc_mass']%2:
            raise RuntimeError('Reversal symmetry parity failure')
    report={'schema':'X6_SIGNED_G_SUPPORT_BRC_CENSUS_UNIT59_V1','status':'AUTHOR_EXECUTED_EXACT_UNREVIEWED_NOT_ADMITTED',
        'baseline_p000_commit':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
        'historical_corpus_commit':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
        'axes':D,'g_min':0,'g_max':GMAX,
        'independent_algorithms':['signed_abs_coordinate_dp_with_exact_binomials','multiset_square_partition_with_injective_axis_embeddings'],
        'first_non_two_axis_shell':first,'shells':shells}
    canonical=json.dumps(report,ensure_ascii=False,sort_keys=True,separators=(',',':'))
    full_sha=hashlib.sha256(canonical.encode()).hexdigest()
    report['canonical_without_sha256']=full_sha
    print(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))
    s512=shells[512]
    print('UNIT59_PASS', 'shells',len(shells),'G25',shells[25]['endpoints'],shells[25]['natural_brc_mass'],
          'G512',s512['endpoints'],s512['natural_brc_mass'],'first_high_support',first,
          'digest',full_sha,file=sys.stderr)

if __name__=='__main__':main()
