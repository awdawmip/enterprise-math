#!/usr/bin/env python3
"""Exact certificate for frozen BRC (pin f42f2906d77f24085c123f3ccfe9667d41caa96d)."""
from math import comb
from fractions import Fraction as Q
from collections import defaultdict
from functools import lru_cache
import json
import sys

N, DEN = 189, 1 << 18

@lru_cache(None)
def accept(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k) > DEN**n

@lru_cache(None)
def alive(n,k):
    if k>n//2:return alive(n,n-k)
    m=k*DEN//n
    assert accept(n,k,m)
    if k==0:lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if accept(n,k,t):b=t
            else:a=t
        lo,hi=a,b
    a,b=m,DEN
    while b-a>1:
        t=(a+b)//2
        if accept(n,k,t):a=t
        else:b=t
    if 4*(a-hi)>DEN:return True
    if 4*(b-lo)<DEN:return False
    raise ValueError((n,k,'ambiguous frozen decision'))

def frozen_rows():
    row={0:1};out=[row.copy()]
    for n in range(1,N+1):
        tmp=defaultdict(int)
        for k,v in row.items():tmp[k]+=v;tmp[k+1]+=v
        row={k:v for k,v in tmp.items() if alive(n,k)}
        out.append(row.copy())
    assert len(out)==190 and not out[189]
    assert sum(map(len,out))==9529
    assert all(sum(out[n].values())==2**n for n in range(25))
    assert sum(out[25].values())==2**25-2
    checks=0
    for n in range(1,N):
        assert all(out[n].get(k,0)==out[n].get(n-k,0) for k in range(n+1))
        for k in range(n//2):
            # Exact monotonicity of normalized Bernstein coefficients c_n(k).
            assert out[n].get(k+1,0)*comb(n,k)>=out[n].get(k,0)*comb(n,k+1)
            checks+=1
    return out,checks

def tail(row,a,d):
    return [Q(sum(v*a**k*(d-a)**(n-k) for k,v in hist.items()),d**n)
            for n,hist in enumerate(row[:N])]

def moments(s,t):
    mu=sum(s)+sum(t)
    h=sum((n+1)*(s[n]+t[n]) for n in range(N))
    for n,x in enumerate(s):
        if x==0:continue
        for m,y in enumerate(t):
            if y==0:continue
            a=x*y*Q(comb(n+m,n),2**(n+m+1))
            mu-=a
            h-=Q(n+m+1,2)*a
    return mu,2*h-mu*mu

def main():
    rr,count=frozen_rows()
    zero=tail(rr,0,1)
    data={}
    for a,d in [(13,250),(53,1000),(27,500)]:
        s=tail(rr,a,d)
        mu0,w0=moments(zero,s)
        mu1,w1=moments(s,s)
        dm,dw=mu1-mu0,w1-w0
        f12=12*(12*dw-dm)
        f24=24*(24*dw-dm)
        z=str(Q(a,d))
        if (a,d)==(13,250):assert f12>0 and f24>0
        elif (a,d)==(27,500):assert f12<0 and f24<0
        else:
            assert dw>0 and 17*dw<dm<18*dw
            assert f12<0<f24
        data[z]={
            'dmu_floor_1e6': (dm*10**6).__floor__(),
            'dvar_floor_1e6': (dw*10**6).__floor__(),
            'deltaV12_floor': f12.__floor__(),
            'deltaV24_floor': f24.__floor__(),
            'exact_signs': [1 if f12>0 else -1,1 if f24>0 else -1],
            'numerator_denominator_bit_lengths_V12': [f12.numerator.bit_length(),f12.denominator.bit_length()],
            'numerator_denominator_bit_lengths_V24': [f24.numerator.bit_length(),f24.denominator.bit_length()]
        }
    # At left/right endpoints, (Delta V_q)/q=q*Delta W-Delta mu is affine
    # in q; strict endpoint signs imply strict signs for EVERY real q in [12,24].
    # Therefore by continuity in z there exists a diagonal/edge crossing z(q)
    # in (13/250,27/500). At z=53/1000 the sign switches at q*=dm/dw.
    assert data['13/250']['exact_signs']==[1,1]
    assert data['27/500']['exact_signs']==[-1,-1]
    assert data['53/1000']['exact_signs']==[-1,1]
    result={'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'survivor_rows':189,'nonzero_histogram_cells':9529,
      'exact_unimodality_integer_comparisons':count,
      'scope':'all real q in [12,24]; first-stop Poissonized observer; p,z in [0,1/2]',
      'entries':data,'checks':'PASS','admission':'AUTHOR_EXACT_COMPUTATION_UNREVIEWED'}
    print('ALL_CHECKS_PASS; exact ratio comparisons =',count,file=sys.stderr)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result
if __name__=='__main__':main()
