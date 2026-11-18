#!/usr/bin/env python3
"""Exact rational-interval witness certificate for N(h)=2,455,069,
at the single endpoint H=2000, using certified all-other-cell witnesses.
"""
from fractions import Fraction
from bisect import bisect_right
from time import perf_counter

def log_bounds(z,N=45):
    term=z;s=Fraction(0)
    for j in range(N):
        s+=2*term/(2*j+1)
        term*=z*z
    return s,s+2*term/((2*N+1)*(1-z*z))

l2,u2=log_bounds(Fraction(1,3))
l9,u9=log_bounds(Fraction(1,9))
l15,u15=log_bounds(Fraction(1,15))
a,b=3*l2-u15,3*u2-l15
c,d=l9+l15,u9+u15
Q=10**26
lo=a*Q//d
hi=b*Q//c+1
assert Fraction(lo,Q)<a/d and b/c<Fraction(hi,Q)
assert hi-lo<=2
print('PASS_RATIONAL_R_INTERVAL',lo,hi,Q)

# Theorem1 guarantees the base exceptional cell needs n*=p+q.
# All translated epsilon cells have witness k=p-k0, ell=q-v0
# for the shift (v0,k0) with v0+k0<=h-510.
p,q=2074774,380295
nstar=p+q
n0=15000
assert 7**510>10**431
assert 10**p>7**(p+q)
assert 7**(p+q+510)>10**(p+431)
assert 7**(p+q-1)>10**(p-1)

t0=perf_counter()
for h in range(2000,2001):
    values=[(v,k) for v in range(h+1) for k in range(h-v+1)]
    values.sort(key=lambda vk:lo*vk[0]-Q*vk[1])
    keys=[lo*v-Q*k for v,k in values]
    assert len(values)==(h+1)*(h+2)//2
    for j in range(len(values)-1):
        v1,k1=values[j];v2,k2=values[j+1]
        dv,dk=v2-v1,k2-k1
        assert (lo if dv>=0 else hi)*dv>Q*dk, (h,j)
    index={pair:j for j,pair in enumerate(values)}
    special=set()
    for v0 in range(h-510+1):
        for k0 in range(h-510-v0+1):
            j=index[(v0,k0)]+1
            assert values[j]==(v0+79,k0+431), (h,v0,k0,j,values[j])
            special.add(j)
            # Explicit length<=nstar certified witness for special interval:
            k,ell=p-k0,q-v0
            assert k>=0 and ell>=0 and k+ell<=nstar
            lv,lk=values[j-1];rv,rk=values[j]
            assert (k+lk)*Q>hi*(ell+lv)
            assert (k+rk)*Q<lo*(ell+rv)
    assert len(special)==(h-509)*(h-508)//2
    # Base gap among special yields the lower bound nstar for ALL h:
    assert values[index[(0,0)]+1]==(79,431)
    flags=bytearray(len(values)+1)
    covered=0
    for ell in range(n0+1):
        kstart=max(0,lo*ell//Q-h-2)
        kend=min(n0-ell,hi*(ell+h)//Q+2)
        if kstart>kend: continue
        for k in range(kstart,kend+1):
            j=bisect_right(keys,Q*k-lo*ell)
            if j in special or flags[j]: continue
            if j:
                lv,lk=values[j-1]
                if (k+lk)*Q<=hi*(ell+lv): continue
            if j<len(values):
                rv,rk=values[j]
                if (k+rk)*Q>=lo*(ell+rv): continue
            flags[j]=1;covered+=1
        if covered==len(flags)-len(special): break
    missing={j for j,flag in enumerate(flags) if not flag}
    assert missing==special,(h,len(missing),len(special),list(sorted(missing-special))[:10])
    print('CERTIFIED_EXACT_N',h,'N=',nstar,'SPECIAL=',len(special),'OTHER_CELLS=',covered,'LAST_ELL=',ell)
print('PASS_S23_AV_EXACT_N_H2000_ENDPOINT_20261108',round(perf_counter()-t0,2),'sec')
