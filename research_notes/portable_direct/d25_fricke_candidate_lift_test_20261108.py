#!/usr/bin/env python3
"""Discriminating test: Hasse-derivative-ratio lift of signed Fricke first-digit coupling.
This tests a proposed lift, NOT a proven canonical second-digit coefficient.
"""
from math import comb
from d25_gauss_second_lift_three_strata_20261108 import primes,model,verify

def J(p,tag):
    u,v,_,_,_,_,xn,xd=model(p,tag)
    mod=p*p; x=xn*pow(xd,-1,mod)%mod
    power=1; tot=0
    for n in range(u+1):
        tot=(tot+n*comb(u,n)*comb(v,n)*power)%mod
        power=power*x%mod
    return tot

def calc(p):
    mod=p*p
    a,_,port_a=verify(p,'A'); b,_,port_b=verify(p,'B')
    ja,jb=J(p,'A'),J(p,'B')
    assert jb%p !=0
    if p%24==19:
        t=ja*pow(6*jb,-1,mod)%mod
        r=2*pow(9,-1,mod)%mod
    else:
        t=(-ja*pow(8*jb,-1,mod))%mod
        r=(-4*pow(27,-1,mod))%mod
    sa=sum(port_a[2:])%p; sb=sum(port_b[2:])%p
    basea=(a-p*sa)%mod
    baseb=(b-p*sb)%mod
    total=(t*a-r*b)%mod
    base=(t*basea-r*baseb)%mod
    assert total%p==base%p==0,(p,total,base)
    s_port=(t*sa-r*sb)%p
    assert (base//p+s_port)%p==total//p%p
    return dict(p=p, t_mod_p=t%p, r_mod_p=r%p,t1=t//p,r1=r//p, JA=ja, JB=jb, gA=a, gB=b, SA=sa, SB=sb, D_base=base//p%p,D_S=s_port,D_total=total//p%p)

def main():
    samples={}
    count_nonzero=0
    for p in primes(2500):
        if p%24 not in (13,19):continue
        obj=calc(p)
        if obj['D_total']!=0:count_nonzero+=1
        if p in (13,19,43,67,373):samples[p]=obj
    print('candidate lift: 94 primes, nonzero second digit residual=',count_nonzero)
    for p in sorted(samples):print(samples[p])

if __name__=='__main__':main()
