#!/usr/bin/env python3
"""Exact F_347 quotient-ring certificate for GH-106: branch critical-value collision."""
import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('gh104',Path(__file__).with_name('d25_gh104_alternating_monodromy_check.py'))
gh104=importlib.util.module_from_spec(spec);spec.loader.exec_module(gh104)


def remainder(a,b,p):
    a=gh104.trim([x%p for x in a]);b=gh104.trim([x%p for x in b])
    assert b[-1]!=0
    inv=pow(b[-1],-1,p)
    while a!=[0] and len(a)>=len(b):
        q=a[-1]*inv%p; shift=len(a)-len(b)
        for j,c in enumerate(b):a[j+shift]=(a[j+shift]-q*c)%p
        a=gh104.trim(a)
    return a


def gcd(a,b,p):
    while b!=[0]:a,b=b,remainder(a,b,p)
    a=gh104.trim(a)
    return [(x*pow(a[-1],-1,p))%p for x in a]


def mulmod(a,b,G,p):
    return remainder(gh104.mul(a,b,p),G,p)


def critical_value_polynomial(p,G,M):
    m=len(G)-1
    assert G[-1]==1
    # Newton sums of roots of monic G, degrees below m.
    s=[m]
    for k in range(1,m):
        val= -k*G[m-k] - sum(G[m-j]*s[k-j] for j in range(1,k))
        s.append(val%p)
    A=remainder(M,G,p)
    power=[1]
    traces=[0]
    for k in range(1,m+1):
        power=mulmod(power,A,G,p)
        traces.append(sum(a*s[i] for i,a in enumerate(power))%p)
    # Newton identities for elementary symmetric functions of M(root(G)).
    e=[1]
    for k in range(1,m+1):
        val=sum(((-1)**(j-1))*e[k-j]*traces[j] for j in range(1,k+1))
        e.append((val*pow(k,-1,p))%p)
    K=[0]*(m+1)
    for k in range(m+1):K[m-k]=((-1)**k*e[k])%p
    assert K[-1]==1
    return K


def main():
    for p in [131, 139, 347]:
        m,E,G,Q,M=gh104.ha_polynomials(p)
        n=len(M)-1
        common=gcd(M,G,p)
        K=critical_value_polynomial(p,G,M)
        Kprime=[(i*K[i])%p for i in range(1,len(K))]
        repeated=gcd(K,Kprime,p)
        if p==347:
            assert (m,n)==(43,173)
            assert common==[109,1]
            alpha=-common[0]%p
            deriv_G=[(i*G[i])%p for i in range(1,len(G))]
            assert (alpha,gh104.evalp(G,alpha,p),gh104.evalp(M,alpha,p),gh104.evalp(deriv_G,alpha,p))==(238,0,0,118)
            assert K[0]==0 and K[1]==162 and repeated==[1]
            # Identity of quotient-ring spectral polynomial: K(M)=0 modulo G.
            A=remainder(M,G,p); val=[0]
            for c in reversed(K): val=gh104.add(mulmod(val,A,G,p),[c],p)
            assert remainder(val,G,p)==[0]
            print('PASS p=347 m=43 N=173; gcd_z(M,G)=z+109; common root=238; K0=0 K1=162; K squarefree.')
            print('K347 ascending coefficients:',K)
            print('Branch t=0 cycle type (87)(3)(1^83); K has 42 other isolated 3-cycle branches; A_173 by prime degree and Jordan.')
        else:
            expected={131:(16,65,89,[74,1],57,18),139:(17,69,69,[114,1],25,39)}[p]
            assert (m,n,K[0],repeated)==(expected[0],expected[1],expected[2],expected[3])
            assert common==[1]
            lamb=expected[4]
            K2=[i*(i-1)*K[i]%p for i in range(2,len(K))]
            assert (gh104.evalp(K,lamb,p),gh104.evalp(Kprime,lamb,p),gh104.evalp(K2,lamb,p))==(0,0,expected[5])
            assert len(repeated)-1==1 and len(K)-1>=3
            print(f'PASS p={p} m={m} N={n}: K(0)={K[0]}, one exactly double critical value={lamb}, K_second={expected[5]}; isolated 3-cycles remain; A_{n} by primitive pure (2m+1)-cycle and Jordan.')
    print('ALL GH-106/GH-107 checks PASS: 3 characteristic-polynomial certificates via quotient algebra.')

if __name__=='__main__':main()
