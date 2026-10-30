"""Exact author-side checks for the D25 terminating-parameter Gauss 2-jet reduction.

No native Enterprise Math execution or source checkpoint is claimed.
"""
from __future__ import annotations

from math import isqrt


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b'\x01') * limit
    sieve[0:2] = b'\x00\x00'
    for d in range(2, isqrt(limit - 1) + 1):
        if sieve[d]:
            sieve[d*d:limit:d] = b'\x00' * (((limit-1-d*d)//d) + 1)
    return [k for k in range(2,limit) if sieve[k]]


def study(p: int, check_clausen: bool=False) -> dict:
    assert p >= 7 and p % 6 == 1
    m = (p-1)//6
    mod = p**3
    inv6 = pow(6,-1,mod)
    inv18 = pow(18,-1,mod)
    jet0,jet1,jet2 = [1]+[0]*(p-1), [0]*p, [0]*p
    for k in range(p-1):
        a0=(k-m)*(k-2*m)
        a1=(3*k-4*m)*inv6%mod
        invd=pow(2*(k+1)**2,-1,mod)
        jet2[k+1]=(a0*jet2[k]+a1*jet1[k]+inv18*jet0[k])*invd%mod
        jet1[k+1]=(a0*jet1[k]+a1*jet0[k])*invd%mod
        jet0[k+1]=(a0*jet0[k])*invd%mod
    assert not any(jet0[m+1:])
    assert not any(jet1[2*m+1:])
    inv2=pow(2,-1,mod)
    inv12=pow(12,-1,mod)
    inv36=pow(36,-1,mod)
    e2=(5*m)*(4*m)*inv2*jet2[p-1]%mod
    assert e2%p==pow(36,-1,p), (p,'universal Gauss boundary')
    assert jet2[p-1]%p==pow(10,-1,p), (p,'p-free exit digit')
    # Exact terminating-parameter triangular Gauss differential system.
    # L0=theta^2-X/2*(theta-m)*(theta-2m).
    for k in range(p+1):
        cur0=jet0[k] if k<p else 0
        cur1=jet1[k] if k<p else 0
        cur2=jet2[k] if k<p else 0
        prev0=jet0[k-1] if k else 0
        prev1=jet1[k-1] if k else 0
        prev2=jet2[k-1] if k else 0
        L0=lambda cur,prev: (k*k*cur-(k-1-m)*(k-1-2*m)*inv2*prev)%mod
        assert L0(cur0,prev0)==0, (p,k,'zero-jet ODE')
        assert L0(cur1,prev1)==(((3*(k-1)-4*m)*inv12*prev0)%mod if k else 0), (p,k,'first-jet ODE')
        rhs=((3*(k-1)-4*m)*inv12*prev1+inv36*prev0 - (e2 if k==p else 0))%mod if k else 0
        assert L0(cur2,prev2)==rhs, (p,k,'second-jet ODE')
    if p%24 not in (13,19):
        return {'p':p,'m':m,'triangular_only':True,'boundary':e2%p}
    # The mod-p^3 sums carry enough digits for the p^3 LIFT target.
    s0=sum(jet0)%mod
    s1=sum(jet1)%mod
    s2=sum(jet2)%mod
    q0=sum((12*k+1)*v for k,v in enumerate(jet0))%mod
    q1=sum((12*k+1)*v for k,v in enumerate(jet1))%mod
    assert s0%p==0, (p,'missing CM0')
    u0=(s0//p+s1)%(p*p)
    u1=s2%p
    v0=q0%(p*p)
    v1=q1%p
    assert (u0*v0-1)%p==0, (p,'missing first digit')
    # At degree >= p, only P0*P2 contributes to the p^2 Clausen tail.
    prefix0=prefix1=Rjet=0
    for i in range(1,m+1):
        ai=jet2[p-i]%p
        prefix0=(prefix0+ai)%p
        prefix1=(prefix1+i*ai)%p
        Ri=((1+6*i)*prefix0-6*prefix1)%p
        Rjet=(Rjet+2*jet0[i]*Ri)%p
    delta_jet=((u0*v0-1)//p+u1*v0+u0*v1-Rjet)%p
    # Independently form original rational Gauss and 216 weighted terms via their ratios.
    g=h=0
    b=1
    bcoeff=[]
    for k in range(p):
        bcoeff.append(b)
        g=(g+b)%mod
        h=(h+(12*k+1)*b)%mod
        if k+1<p:
            b=b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod)%mod
    assert g%p==0
    assert g==(s0+p*s1+p*p*s2)%mod
    assert h%(p*p)==(q0+p*q1)% (p*p)
    A=0
    a=1
    aa=[]
    for k in range(p):
        aa.append(a)
        A=(A+(6*k+1)*a)%mod
        if k+1<p:
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,mod)%mod
    assert (A-p)%(p*p)==0, (p,'unexpected first digits')
    d_raw=((A-p)%mod)//(p*p)
    Rraw=0
    C=pow(10,-1,p)
    tailprefix=tailweighted=0
    for i in range(1,m+1):
        tailprefix=(tailprefix+C)%p
        tailweighted=(tailweighted+i*C)%p
        Rraw=(Rraw+2*(bcoeff[i]%p)*((1+6*i)*tailprefix-6*tailweighted))%p
        C=C*36*i*i*pow((6*i+5)*(3*i+2),-1,p)%p
    assert Rjet==Rraw, (p,Rjet,Rraw)
    assert (g*h-A)%(p**3)==(p*p*Rraw)%(p**3), (p,'Clausen high-degree mismatch')
    assert d_raw==delta_jet, (p,d_raw,delta_jet)
    assert d_raw==0, (p,'LIFT finite verification failed')
    if check_clausen:
        # Original full power-series Clausen coefficients (n<p) and
        # high-degree coefficient transfer to the P0/P2 jet (n>=p).
        for n in range(2*p-1):
            z=sum(bcoeff[k]*bcoeff[n-k]
                  for k in range(max(0,n-p+1),min(p-1,n)+1))%mod
            if n<p:
                assert z==aa[n],(p,n,z,aa[n])
            else:
                jet_tail=2*p*p*sum(
                    jet0[i]*jet2[n-i]
                    for i in range(m+1) if 0<=n-i<p
                )%mod
                assert z==jet_tail,(p,n,z,jet_tail)
    return dict(p=p,m=m,P0_over_p=(s0//p)%p,P1=s1%p,P2=s2%p,
                Q0=q0%p,Q1=q1%p,u0=u0%p, R=Rraw, delta=delta_jet,
                carry=((u0*v0-1)//p)%p, second=(u1*v0+u0*v1)%p,
                tail_jet_top=jet2[p-1]%p,boundary=e2%p)


if __name__=='__main__':
    all_primes=[p for p in primes_below(5000) if p%6==1]
    targets=0
    for p in all_primes:
        r=study(p,check_clausen=(p<=61 and p%24 in (13,19)))
        if p%24 in (13,19):
            targets+=1
        if p in (13,19,37,157,373):
            print('ANCHOR',r)
    print('SUMMARY',len(all_primes),'primes p<5000 p mod6=1 with exact triangular Gauss 2-jet ODE;',targets,'target-class primes with original mod-p^3 Clausen/LIFT checks')
    print('PASS_GH178_GH179_TERMINATING_GAUSS_JET_AND_TRIANGULAR_CONNECTION_EXACT')
