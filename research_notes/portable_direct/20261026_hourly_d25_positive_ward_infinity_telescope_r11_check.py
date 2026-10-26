#!/usr/bin/env python3
"""Positive Ward infinity adjoint: exact author check of genuine J+E.
Corrected Clausen only, modular p^2; no native CM or independent review.
"""
from functools import lru_cache
from pathlib import Path
from runpy import run_path

BASE=run_path(str(Path(__file__).with_name(
    '20261026_hourly_d25_ward_scalar_port_filtration_infinity_r11_check.py')))
jets=BASE['jets']
moments=BASE['moments']
prime_targets=BASE['prime_targets']
CHANNELS=((0,2),(1,2),(0,3))

def check(p):
    q=p*p;m=(p-1)//6;N=2*m-1
    u=jets(p)
    def scalar(a,r):
        return u[a][r] if a>=0 and 0<=r<p else 0
    @lru_cache(None)
    def M(a,b,n,s=0):
        if a<0 or b<0:return 0
        ans=0
        for j in range(max(1,1-n),min(2*m,2*m-n)+1):
            ell=j+n
            ans+=pow(j,s,q)*scalar(a,j)*scalar(b,p-ell)
        return ans%q
    def source(a,b,n):
        J=(3*M(a-1,b,n,1)-3*M(a-1,b,n+1,1)
          +4*m*M(a-1,b,n+1)+2*M(a-2,b,n+1)
          -3*((p-n)*M(a,b-1,n)-M(a,b-1,n,1))
          +(14*m-3*n)*M(a,b-1,n+1)
          -3*M(a,b-1,n+1,1)-2*M(a,b-2,n+1))
        E=((2*m*m*(a==0)+4*m*(a==1)+2*(a==2))*scalar(b,p-n-1)
          +scalar(a,2*m-n)*(-6*m*m*scalar(b,4*m)
            +8*m*scalar(b-1,4*m)-2*scalar(b-2,4*m)))
        return (J+E)%q
    def Y(a,b,n):
        return (M(a,b,n,1)-(p-n)*pow(2,-1,q)*M(a,b,n))%q

    mu={}
    for n in range(1,N+1):
        mu[n]=(pow(2,n,q)+(p-2*n+1)*mu.get(n-1,0))*pow(p-2*n,-1,q)%q
    assert mu[1]*(p-2)%q==2
    for n in range(2,N+1):
        assert (mu[n]*(p-2*n)-mu[n-1]*(p-2*n+1))%q==pow(2,n,q)

    d={}
    for a,b in CHANNELS:
        z=sum(mu[n]*source(a,b,n) for n in range(1,N+1))%q
        r=sum(pow(2,n,q)*Y(a,b,n) for n in range(1,N+1))%q
        assert z==r,(p,a,b,'POSITIVE_ADJOINT')
        for n in range(1,N+1):
            assert ((p-2*n)*Y(a,b,n)-(p-2*n-1)*Y(a,b,n+1)
                    -source(a,b,n))%q==0,(p,a,b,n)
        assert Y(a,b,N+1)==0
        ip0=sum(pow(2,n,q)*M(a,b,n) for n in range(1,N+1))%q
        ip1=sum(pow(2,n,q)*(6*n-1)*M(a,b,n) for n in range(1,N+1))%q
        kp=sum(pow(2,n,q)*M(a,b,n,1) for n in range(1,N+1))%q
        assert ip1==((6*p-1)*ip0-12*kp+12*z)%q
        previous=moments(p,u,a,b)
        assert (ip0,ip1)==(previous['I0'],previous['I1'])
        d[(a,b)]={'I0':ip0,'I1':ip1,'Kp':kp,'Zp':z}
    d02,d12,d03=[d[ab] for ab in CHANNELS]
    inv6=pow(6,-1,q)
    infinity=(d02['I1']+p*(-6*d02['I0']
              -(d12['I1']+d03['I1'])*inv6))%q
    source_inf=(-d02['I0']-12*(d02['Kp']-d02['Zp'])
       +p*inv6*(d12['I0']+d03['I0'])
       +2*p*(d12['Kp']+d03['Kp']-d12['Zp']-d03['Zp'])
       -p*p*(d12['I0']+d03['I0']))%q
    assert source_inf==infinity,(p,source_inf,infinity)
    if p==13: assert infinity==166
    if p==733: assert infinity==216796
    return {'p':p,'infinity':infinity,'ports':d}

if __name__=='__main__':
    tests=[check(p) for p in prime_targets(211)]
    tests.append(check(733))
    print('PASS positive-source Ward dual across 23 primes, true J+E and infinity')
    for d in tests:
        if d['p'] in (13,733):print(d)
