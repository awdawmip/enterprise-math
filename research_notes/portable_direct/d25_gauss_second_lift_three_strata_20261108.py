#!/usr/bin/env python3
"""Independent exact Z/p^3 regression for the general Gauss three-stratum second lift.
Only standard-library integer arithmetic; author-side mathematical evidence, not native H0/B0.
"""
from math import comb


def primes(n):
    out=[]
    for p in range(5,n+1):
        if all(p%d for d in range(2,int(p**0.5)+1)):
            out.append(p)
    return out


def model(p, tag):
    if tag == 'A':
        m=(p-1)//6
        return (m,2*m,1,6,1,3,1,2)
    if p%8==3:  # B3: (1/8,3/8)
        return ((p-3)//8,3*((p-3)//8)+1,1,8,3,8,1,9)
    # B5: (5/8,7/8) after Euler: (-k+p/8,-3k-1+3p/8)
    return ((p-5)//8,3*((p-5)//8)+1,1,8,3,8,1,9)


def verify(p, tag):
    u,v,ln,ld,mn,md,xn,xd=model(p,tag)
    assert 0 <= u < v < p and p%ld and p%md
    mod=p**3
    lam=ln*pow(ld,-1,mod)%mod
    mu=mn*pow(md,-1,mod)%mod
    h=[0]*p; h2=[0]*p
    fac=[1]*p
    for i in range(1,p):
        z=pow(i,-1,mod)
        h[i]=(h[i-1]+z)%mod
        h2[i]=(h2[i-1]+z*z)%mod
        fac[i]=fac[i-1]*i%mod
    ifac=[1]*p
    ifac[-1]=pow(fac[-1],-1,mod)
    for i in range(p-1,0,-1): ifac[i-1]=ifac[i]*i%mod
    inv2=pow(2,-1,mod)
    # Independent direct Gauss coefficient recurrence in the true rational parameters.
    direct=[]; c=1
    if tag=='A':
        num=lambda n: (6*n+1)*(3*n+1)
        den=18
    elif p%8==3:
        num=lambda n: (8*n+1)*(8*n+3)
        den=64
    else:
        num=lambda n: (8*n+5)*(8*n+7)
        den=64
    for n in range(p):
        direct.append(c)
        if n+1<p:
            c=c*num(n)*pow(den*(n+1)*(n+1),-1,mod)%mod
    ports=[[0]*p for _ in range(6)] # Q, pL, pT, p²S_low, p²S_mid, p²S_high
    for n in range(p):
        if n<=u:
            q=comb(u,n)*comb(v,n)%mod
            a1=(h[u-n]-h[u])%mod
            b1=(h[v-n]-h[v])%mod
            a2=(h2[u]-h2[u-n])%mod
            b2=(h2[v]-h2[v-n])%mod
            first=(lam*a1+mu*b1)%mod
            second=(first*first-lam*lam*a2-mu*mu*b2)*inv2%mod
            ports[0][n]=q
            ports[1][n]=p*q*first%mod
            ports[3][n]=p*p*q*second%mod
        elif n<=v:
            sign=-1 if ((u+n)%2) else 1
            t=sign*lam*fac[u]*fac[n-u-1]*fac[v]*ifac[v-n]*ifac[n]*ifac[n]%mod
            aex=(h[n-u-1]-h[u])%mod
            b1=(h[v-n]-h[v])%mod
            ports[2][n]=p*t%mod
            ports[4][n]=p*p*t*(lam*aex+mu*b1)%mod
        else:
            sign=-1 if ((u+v)%2) else 1
            z=sign*lam*mu*fac[u]*fac[n-u-1]*fac[v]*fac[n-v-1]*ifac[n]*ifac[n]%mod
            ports[5][n]=p*p*z%mod
        total=sum(port[n] for port in ports)%mod
        assert total==direct[n],(p,tag,n,total,direct[n])
    x=xn*pow(xd,-1,mod)%mod
    power=1; vals=[0]*6; raw=0
    for n in range(p):
        for j in range(6): vals[j]=(vals[j]+ports[j][n]*power)%mod
        raw=(raw+direct[n]*power)%mod
        power=power*x%mod
    assert sum(vals)%mod==raw
    # At the target CM zero, this is an exact lift through two p-adic digits.
    assert raw%p==0,(p,tag,'CM zero unexpectedly failed')
    carry=tuple((vals[j]//(p if j in (1,2) else p*p))%p for j in (1,2,3,4,5))
    return (raw//p)%(p*p),vals[0]//p%p,carry


def main():
    target=[p for p in primes(2500) if p%24 in (13,19)]
    sample={}
    for p in target:
        for tag in ('A','B'):
            result=verify(p,tag)
            if p in (13,19,43,67,373): sample[(p,tag)]=result
    print(f'PASS: {len(target)} target primes and {2*len(target)} A/B models; all {sum(2*p for p in target)} coefficients mod p^3')
    for p in (13,19,43,67,373):
        for tag in ('A','B'):
            lift,q,carry=sample[(p,tag)]
            print('p=',p,'tag=',tag,'G/p modp^2=',lift,'Q/p modp=',q,'ports L,T,S0,S1,S2 modp=',carry)

if __name__=='__main__':main()
