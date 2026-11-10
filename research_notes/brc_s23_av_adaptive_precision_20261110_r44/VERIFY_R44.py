#!/usr/bin/env python3
"""R44 exact nested-dyadic precision certificates for sqrt(2)-1 labelled rotation.
Scientific frozen reference: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
R42 and R43 dependencies preserved verbatim from the R43 evidence bundle.
"""
from __future__ import annotations
from bisect import bisect_right
from fractions import Fraction
from math import isqrt
import json
import hashlib
from pathlib import Path
from VERIFY_R42 import recurrence_selector,Uncertified
import REFERENCE_R41 as ref

FREEZE='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

def sqrt2_dyadic(bits):
    if bits < 1: raise ValueError('bits')
    d=1<<bits
    a=isqrt(2*d*d)
    return Fraction(a-d,d),Fraction(a+1-d,d)

def interval_nested(lower_bits,upper_bits):
    lo1,hi1=sqrt2_dyadic(lower_bits)
    lo2,hi2=sqrt2_dyadic(upper_bits)
    return lo1<=lo2<=hi2<=hi1

class OwnerCert:
    def __init__(self,bits,m):
        lo,hi=sqrt2_dyadic(bits)
        self.bits,self.m=bits,m
        self.D=1<<bits
        a=isqrt(2*self.D*self.D)
        self.u=2*a+1-2*self.D
        # denominator 2^bits, interval exactly one dyadic quantum
        self.q=2*self.D; self.delta=1
        self.sorted=sorted(((z*self.u)%self.q,z) for z in range(m))
        self.res=[r for r,z in self.sorted]
        for k in range(m):
            x,a=self.sorted[k]; y,b=self.sorted[(k+1)%m]
            gap=(y-x)%self.q
            if not (gap>abs(b-a) and self.q-gap>abs(b-a)):
                raise Uncertified(('historical-order',bits,k,a,b))

    def owner(self,t,r=None):
        if r is None:r=(t*self.u)%self.q
        k=(bisect_right(self.res,r)-1)%self.m
        a=self.sorted[k][1];b=self.sorted[(k+1)%self.m][1]
        left=(r-self.res[k])%self.q
        right=(self.res[(k+1)%self.m]-r)%self.q
        gap=(self.res[(k+1)%self.m]-self.res[k])%self.q
        if left+right!=gap or not ((left>abs(t-a) or (t==a and left==0)) and right>abs(t-b)):
            raise Uncertified(('source-near-owner-boundary',self.bits,t,k,left,right))
        return k


def adaptive_rolling(m,J,N,K,start_bits=3,budget=None,max_bits=256):
    assert m>=2 and N>=1 and K>=0
    b=start_bits
    failures=[]; refinements=[]; initialized=False
    while b<=max_bits:
        try:
            cert=OwnerCert(b,m)
            lo,hi=sqrt2_dyadic(b)
            tau,init_stat=recurrence_selector(lo,hi,m,J,N,budget=budget)
            initialized=True
            break
        except Uncertified as err:
            failures.append(('initial',b,str(err.args[0])[:140]))
            b+=1
    if not initialized:raise AssertionError(('initial failed',b,failures))
    initial_bits=b;vec=[list(tau)];source_labels=[]
    repairs=0;repair_floors=0
    modular_updates=0; phase_products=1; failed_sources=0
    r=(J*cert.u)%cert.q
    for step in range(K):
        t=J+step
        while True:
            try:
                label=cert.owner(t,r)
                break
            except Uncertified as err:
                failed_sources+=1; failures.append(('new_source',b,str(err.args[0])[:140]))
                old=b;b+=1
                if b>max_bits:raise AssertionError(('precision exhausted',t,b))
                assert interval_nested(old,b)
                cert=OwnerCert(b,m)
                refinements.append({'step':step,'t':t,'old_bits':old,'new_bits':b})
                r=(t*cert.u)%cert.q;phase_products+=1
        source_labels.append(label)
        tau[label]=t
        nextJ=t+1
        earliest=nextJ-N
        expired=[i for i,old in enumerate(tau) if old is not None and old<earliest]
        assert len(expired)<=1
        if expired:
            i=expired[0]
            repair_refined=False
            while True:
                lo,hi=sqrt2_dyadic(b)
                try:
                    selector=ref.CoboundarySelector(ref.Observer(lo,hi,m),nextJ,N)
                    new,counter=selector.solve([i]);break
                except (Uncertified,AssertionError):
                    old=b;b+=1
                    if b>max_bits:raise
                    assert interval_nested(old,b)
                    cert=OwnerCert(b,m)
                    repair_refined=True
                    refinements.append({'step':step,'t':t,'old_bits':old,'new_bits':b,'trigger':'repair'})
            tau[i]=new[i]
            repair_floors+=counter['certified_scalar_floor_evaluations']
            repairs+=1
            if repair_refined:
                r=(t*cert.u)%cert.q;phase_products+=1
        assert all(x is None or earliest<=x<nextJ for x in tau)
        vec.append(list(tau))
        if step+1<K:
            r+=cert.u
            if r>=cert.q:r-=cert.q
            modular_updates+=1
    return vec,{'start_bits':start_bits,'initial_certified_bits':initial_bits,
                'end_bits':b,'initial_scan':init_stat['scan'],
                'initial_fallback_owners':init_stat['fallback_owners'],
                'precision_refinements':refinements,'failed_certificate_trials':len(failures),
                'expired_maxima_repairs':repairs,'repair_scalar_floor_evaluations':repair_floors,
                'initializations_and_resets':phase_products,'rolling_modular_additions':modular_updates,
                'source_labels':source_labels}


def find_first_dyadic_bits(m,J,N,budget=None,bmax=100):
    for bits in range(2,bmax+1):
        try:
            lo,hi=sqrt2_dyadic(bits)
            cert=OwnerCert(bits,m)
            got,stat=recurrence_selector(lo,hi,m,J,N,budget=budget)
            return bits,got,stat
        except Uncertified:pass
    return None,None,None


def main():
    # Distinct scales ensure that fixed initial precision sometimes ceases to certify later incoming sources.
    cases=[('J100',16,100,120,512,3),('J1000',16,1000,500,512,3),
           ('J1e6',16,10**6,10000,64,3),('J1e9',16,10**9,10**8,32,3),
           ('short_N5',16,100,5,160,3),('negative',16,-30,24,128,3)]
    # Reference uses an independent 40-decimal enclosure, not the adaptive dyadic arithmetic.
    lo,hi=tuple(x-1 for x in ref.sqrt_enclose(2,10**40))
    obs=ref.Observer(lo,hi,16)
    outcomes=[]
    for name,m,J,N,K,b0 in cases:
        actual,stat=adaptive_rolling(m,J,N,K,b0,budget=min(N,4*m))
        for step,v in enumerate(actual):
            expected,_=ref.independent_last(obs.arcs,J+step-N,J+step,obs.mid)
            assert expected==v,(name,step,expected,v)
            if N<=160:
                assert ref.brute(obs,J+step,N)==v,(name,step,'brute')
        # Sparse observer rank update: changed labels alone determine extinction-rank differences.
        sparse_checks=0;max_changed=0
        for step,(before,after) in enumerate(zip(actual,actual[1:])):
            changed=[k for k,(a,b) in enumerate(zip(before,after)) if a!=b]
            max_changed=max(max_changed,len(changed))
            assert len(changed)<=2,(name,step,changed)
            for x in (J-N+step, J+step-N//2, J+step, J+step+1):
                rank=lambda vals:sum(v is None or v<x for v in vals)
                old_rank=rank(before);new_rank=rank(after)
                delta=sum(int(after[k] is None or after[k]<x)-int(before[k] is None or before[k]<x) for k in changed)
                assert new_rank-old_rank==delta,(name,step,x)
                sparse_checks+=1
        first,v0,_=find_first_dyadic_bits(m,J,N,budget=min(N,4*m))
        assert v0==actual[0]
        outcomes.append({'case':name,'m':m,'J':J,'N':N,'K':K,'verified_vectors':len(actual),
                'initial_minimal_bits':first,'sparse_rank_checks':sparse_checks,'max_changed_labels':max_changed, **{k:val for k,val in stat.items() if k!='source_labels'},
                'final_vector_sha256':hashlib.sha256(json.dumps(actual[-1],separators=(',',':')).encode()).hexdigest()})
        print('PASS',name,'initial',first,'end',stat['end_bits'],'refine',len(stat['precision_refinements']),
              'repairs',stat['expired_maxima_repairs'],'vectors',len(actual),flush=True)
    assert sum(x['sparse_rank_checks'] for x in outcomes)==4*sum(x['K'] for x in outcomes)
    assert sum(len(x['precision_refinements']) for x in outcomes)>0
    assert sum(x['expired_maxima_repairs'] for x in outcomes)>0
    finite_bound={'sqrt2_norm_bound':'dist(k*(sqrt2-1),Z)>1/(4|k|) for each nonzero integer k',
         'sufficient_interval_width':'2^-bits < 1/(4*M*M), M=max relevant |source-historical index| and historical differences',
         'conclusion':'all historical/source pair order certificates succeed at this precision for finite given source list'}
    cert={'scientific_input_pin':FREEZE,'statement':'certified nested-dyadic adaptive precision without replay of prior window labels',
          'validation':'exact integer/Fraction, Euclidean independent, finite brute checks',
          'author_review_status':'not independently reviewed','cases':outcomes,
          'theorem_uniform_bit_bound':finite_bound}
    Path(__file__).with_name('CERTIFICATE_R44.json').write_text(json.dumps(cert,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print('PASS_R44_ADAPTIVE_NESTED_DYADIC_STREAM_AND_INDEPENDENT_ORACLE',sum(x['verified_vectors'] for x in outcomes))

if __name__=='__main__':main()
