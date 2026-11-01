#!/usr/bin/env python3
"""Finite exact original-coefficient multiscale test for the D25 signed 216/2304 bridge.

Published scope: FINITE CERTIFICATE ONLY; no all-prime Dwork claim, no H0/B0 native computation.
"""
from math import comb
import json, hashlib
from pathlib import Path

OUT=Path(__file__).with_suffix('.check.json')


def unit(x,p):
    v=0
    while x%p==0:
        x//=p;v+=1
    return x,v


def original_weighted(n,p,N):
    """Full original weighted sums at cutoff n using p-adic unit + valuation.

    Given binomial numerators A_k=(2k)!(3k)!/k!^5 and
    B_k=(4k)!/k!^4, this is EXACT arithmetic in Z/p^N.
    """
    M=p**N; inv36=pow(36,-1,M);inv288=pow(288,-1,M)
    powers=[p**j for j in range(N+1)]
    vals=[0,0]; units=[1,1]; sums=[0,0]
    for k in range(n):
        for t,weight in enumerate((6*k+1,8*k+1)):
            if vals[t]<N:
                sums[t]=(sums[t]+weight*units[t]*powers[vals[t]])%M
        if k+1==n: break
        q,zq=unit(k+1,p)
        iq3=pow(pow(q,3,M),-1,M)
        num=((2*k+1,3*k+1,3*k+2),(4*k+1,2*k+1,4*k+3))
        for j,triplet in enumerate(num):
            un=1;zn=0
            for t in triplet:
                u,z=unit(t,p);un=(un*u)%M;zn+=z
            vals[j]+=zn-3*zq
            assert vals[j]>=0,(p,k,j,vals[j])
            units[j]=units[j]*un*iq3*(inv36 if j==0 else inv288)%M
    return tuple(sums)


def raw_integer_pair(n,p,N):
    """Independent reference path: actual binomial integers and modular powers."""
    M=p**N;d1=pow(216,-1,M);d2=pow(2304,-1,M)
    w=s=0;x=y=1
    for k in range(n):
        c=comb(2*k,k)**2
        w=(w+(6*k+1)*c*comb(3*k,k)*x)%M
        s=(s+(8*k+1)*c*comb(4*k,2*k)*y)%M
        x=x*d1%M;y=y*d2%M
    return w,s


def valuation_mod(a,p,N):
    a%=p**N
    if a==0:return N
    k=0
    while a%p==0:a//=p;k+=1
    return k


def certify(p,rmax):
    chi=1 if p%3==1 else -1
    N=max(8,3*rmax+2)
    M=p**N
    rows=[]; prev=None; initial_gamma=None
    for r in range(1,rmax+1):
        cutoff=p**r
        w,s=original_weighted(cutoff,p,N)
        if p<=43 and r<=2:
            assert (w,s)==raw_integer_pair(cutoff,p,N),(p,r)
        E=(w-2*s+chi**r*p**r)%M
        vv=valuation_mod(E,p,N)
        assert vv>=r+3,(p,r,vv)
        digit=E//p**(r+3)%p
        if r==1:initial_gamma=digit
        assert digit==(chi**(r-1)*initial_gamma)%p,(p,r,digit,initial_gamma)
        DW=DS=None
        if prev is not None:
            DW=valuation_mod(w-chi*p*prev[0],p,N)
            DS=valuation_mod(s-chi*p*prev[1],p,N)
            assert min(DW,DS)>=3*r,(p,r,DW,DS)
        rows.append({'r':r,'cutoff':cutoff,'v_E_capN':vv,
            'signed_digit':digit,'v_Dwork_W_capN':DW,'v_Dwork_S_capN':DS,
            'W_mod_pN':w,'S_mod_pN':s,'E_mod_pN':E})
        prev=(w,s)
    return {'p':p,'chi':chi,'precision_exp':N,'initial_fourth_digit':initial_gamma,'rows':rows}


def main():
    rmax={p:2 for p in [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,109,139,211,373]}
    rmax.update({5:5,7:4,11:4,13:4,19:3})
    rec=[certify(p,n) for p,n in rmax.items()]
    fingerprints=''.join('%s:%s:%s:%s\n'%(i['p'],row['r'],row['E_mod_pN'],row['signed_digit']) for i in rec for row in i['rows'])
    summary={'classification':'AUTHOR_DERIVED_FINITE_ONLY_NOT_CANONICAL_SOURCE',
        'method':'exact original binomial coefficient valuations, unit modular arithmetic; independent integer formula p<=43/r<=2',
        'number_of_primes':len(rec),'number_of_cutoffs':sum(len(i['rows']) for i in rec),
        'all_checked_Dwork_v_at_least_3r':True,
        'all_checked_leading_transfer_gamma_r_equals_chi_power_gamma_1':True,
        'record_sha256':hashlib.sha256(fingerprints.encode()).hexdigest(),
        'records':rec}
    OUT.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    for i in rec:
        print('p=',i['p'],'chi=',i['chi'],'r/digit/vE/vDW/vDS=',[(x['r'],x['signed_digit'],x['v_E_capN'],x['v_Dwork_W_capN'],x['v_Dwork_S_capN']) for x in i['rows']])
    print('wrote',OUT, 'records',summary['number_of_cutoffs'],summary['record_sha256'])

if __name__=='__main__':main()
