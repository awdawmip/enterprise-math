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


def tail_jet(rows, a, d):
    """Exact s_n(a/d) and first derivative w.r.t. real x."""
    s=[]; ds=[]
    for n,hist in enumerate(rows[:N]):
        val=0; der=0
        for k,v in hist.items():
            val+=v*a**k*(d-a)**(n-k)
            if k: der+=v*k*a**(k-1)*(d-a)**(n-k)
            if n-k: der-=v*(n-k)*a**k*(d-a)**(n-k-1)
        s.append(Q(val,d**n))
        ds.append(Q(der,d**(n-1)) if n else Q(0))
    return s,ds

def moment_jets(s,t,ds,dt):
    """Return mu, E[Y^2]/2 and their first derivatives."""
    mu=sum(s)+sum(t)
    H=sum((n+1)*(s[n]+t[n]) for n in range(N))
    mup=sum(ds)+sum(dt)
    Hp=sum((n+1)*(ds[n]+dt[n]) for n in range(N))
    for n,x in enumerate(s):
        for m,y in enumerate(t):
            w=Q(comb(n+m,n),2**(n+m+1))
            ab=w*x*y
            dab=w*(ds[n]*y+x*dt[m])
            mu-=ab; H-=Q(n+m+1,2)*ab
            mup-=dab; Hp-=Q(n+m+1,2)*dab
    return mu,H,mup,Hp

def main():
    rows,coefficient_checks=frozen_rows()
    zero,_=tail_jet(rows,0,1)
    z,dz=tail_jet(rows,53,1000)
    z0=[Q(0)]*N
    m0,h0,m0p,h0p=moment_jets(zero,z,z0,dz)
    m1,h1,m1p,h1p=moment_jets(z,z,dz,dz)
    dm=m1-m0; dmp=m1p-m0p
    dw=2*(h1-h0)-(m1*m1-m0*m0)
    dwp=2*(h1p-h0p)-2*(m1*m1p-m0*m0p)
    q0=dm/dw
    slope=(dmp*dw-dm*dwp)/(dw*dw)
    d12=12*(12*dw-dm);d24=24*(24*dw-dm)
    dz_cross=q0*(q0*dwp-dmp)
    assert coefficient_checks==8836
    assert dm>0 and dw>0 and dmp>0 and dwp<0
    assert d12<0<d24 and 17<q0<18
    assert Q(17948788665,10**9)<q0<Q(17948788666,10**9)
    assert Q(68846312,1000)<slope<Q(68846313,1000)
    assert dz_cross==-q0*dw*slope and dz_cross<0
    def entry(v):
        return {'sign':int(v>0)-int(v<0),
                'floor_scaled_1e8':int(v*10**8//1),
                'numerator_bits':v.numerator.bit_length(),
                'denominator_bits':v.denominator.bit_length()}
    result={
      'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'input_z':'53/1000','survivor_rows':189,
      'nonzero_histogram_cells':9529,
      'normalized_bernstein_coefficient_comparisons':coefficient_checks,
      'delta_mu':entry(dm),'delta_W':entry(dw),
      'delta_mu_z':entry(dmp),'delta_W_z':entry(dwp),
      'D12':entry(d12),'D24':entry(d24),
      'q0':entry(q0),'q0_z':entry(slope),
      'D_z_at_crossover':entry(dz_cross),
      'exact_q0_interval':[str(Q(17948788665,10**9)),str(Q(17948788666,10**9))],
      'exact_q0_z_interval':[str(Q(68846312,1000)),str(Q(68846313,1000))],
      'claim':'local unique smooth increasing diagonal-edge crossover branch',
      'status':'AUTHOR_DERIVED_EXACT_RATIONAL_CHECKED_UNREVIEWED_NOT_ADMITTED'}
    print('ALL_CHECKS_PASS; full rational signs and bounds',file=sys.stderr)
    print(json.dumps(result,indent=2))
if __name__=='__main__':
    main()
