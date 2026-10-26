#!/usr/bin/env python3
"""Exact author check of corrected-Clausen Q/p^2 modulo p^3, including high-high.
Not native CM, independent review, Source checkpoint or formal acceptance.
"""
from math import isqrt

def primes(limit):
    for p in range(7,limit+1,6):
        if all(p%d for d in range(2,isqrt(p)+1)):
            yield p

def jets(p,order=5):
    m=(p-1)//6; q=p**3
    half=p*pow(2,-1,q)%q
    u=[[1]+[0]*(order-1)]
    for n in range(p-1):
        a,b=n-m,n-2*m
        invden=pow((n+1)*(n+1-half)%q,-1,q)
        t=3*(n+1)*invden%q
        den=[invden*pow(t,k,q)%q for k in range(order)]
        num=[a*b,-2*a-b,2]+[0]*(order-3)
        tmp=[sum(u[n][i]*num[k-i] for i in range(k+1))%q for k in range(order)]
        u.append([sum(tmp[i]*den[k-i] for i in range(k+1))%q
                  for k in range(order)])
    assert all(u[n][0]==0 for n in range(m+1,p))
    assert all(u[n][1]==0 for n in range(2*m+1,p))
    return u

def original(p):
    mod=p**5; r=[1]
    for n in range(p-1):
        den=36*(n+1)**2
        r.append(r[-1]*(6*n+1)*(3*n+1)*pow(den,-1,mod)%mod)
    total=sum((6*(a+b)+1)*r[a]*r[b]
              for a in range(p) for b in range(p-a,p))%mod
    assert total%(p*p)==0
    return total//(p*p),total

def check(p):
    m=(p-1)//6; q=p**3; u=jets(p)
    inv6,inv18,inv36,inv1296=[pow(x,-1,q) for x in (6,18,36,1296)]
    inv2=pow(2,-1,q)
    powers=[pow(inv2,n,q) for n in range(p)]
    A0=A1=A2=0
    lowhigh=0
    for j in range(1,2*m+1):
        rlo=(u[j][0]-p*inv6*u[j][1]+p*p*inv36*u[j][2])%q*powers[j]%q
        for ell in range(1,j+1):
            n=p-ell
            al=6*(j-ell)+1
            w=powers[j]*powers[n]%q
            z0=al*u[j][0]*u[n][2]
            z1=6*u[j][0]*u[n][2]-al*inv6*(u[j][1]*u[n][2]+u[j][0]*u[n][3])
            z2=al*inv36*(u[j][2]*u[n][2]+u[j][1]*u[n][3]+u[j][0]*u[n][4])-(u[j][1]*u[n][2]+u[j][0]*u[n][3])
            A0+=w*z0*inv18
            A1+=w*z1*inv18
            A2+=w*z2*inv18
            rhi_over=(u[n][2]*inv36-p*inv6*inv36*u[n][3]+p*p*inv1296*u[n][4])%q*powers[n]%q
            lowhigh+=2*(al+6*p)*rlo*rhi_over
    lowhigh%=q
    reconstructed=(A0+p*A1+p*p*A2)%q
    assert lowhigh==reconstructed,(p,lowhigh,reconstructed)
    highhigh=0
    for a in range(2*m+1,p):
        for b in range(max(2*m+1,p-a),p):
            highhigh+=(6*(a+b)+1)*powers[a]*powers[b]*u[a][2]*u[b][2]
    highhigh%=p
    highhigh_norm=p*p*highhigh*inv1296%q
    third=(lowhigh+highhigh_norm)%q
    actual,raw=original(p)
    assert actual==third,(p,actual,third,lowhigh,highhigh_norm)
    return dict(p=p,Q_over_p2_mod_p3=actual,Q_mod_p5=raw,
                low_high=lowhigh,high_high=highhigh_norm,
                high_high_normalized_coefficient=highhigh*inv1296%p)

if __name__=="__main__":
    results=[check(p) for p in primes(211)]
    assert len(results)==22
    print("PASS 22 target primes through 211: original cutoff equals complete low-high plus high-high expansion")
    for p in (7,13,19,31,37,43):
        print(next(r for r in results if r["p"]==p))
    print("P733",check(733))
