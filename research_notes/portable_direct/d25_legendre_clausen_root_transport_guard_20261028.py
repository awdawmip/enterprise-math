#!/usr/bin/env python3
"""Author-side exact modular check of the Legendre/Clausen Hensel-root transport.
No native H0/B0, Source claim, formal Result, or review is performed.
"""
from math import comb

TARGET_PRIMES=(13,19,37,43,61,67,211,373)

def inv(x,mod):
    return pow(x%mod,-1,mod)

def evaluate(cs,z,mod):
    value=0
    for c in reversed(cs):
        value=(value*z+c)%mod
    return value

def derivative(cs,order=1):
    if order==1:
        return [j*cs[j] for j in range(1,len(cs))]
    return [j*(j-1)*cs[j] for j in range(2,len(cs))]

def root_hensel(cs,p):
    mod=p**3
    z=1
    dcs=derivative(cs)
    assert evaluate(cs,z,p)==0
    assert evaluate(dcs,z,p)!=0
    for _ in range(3):
        z=(z-evaluate(cs,z,mod)*inv(evaluate(dcs,z,mod),mod))%mod
    assert z%p==1
    assert evaluate(cs,z,mod)==0
    return z

def one(p):
    m=(p-1)//6
    mod=p**3; P=[];G=[];E=[];F=[]
    inv2=inv(2,mod)
    b=1;u=1;v=1; H=[0]*(2*m+1);H2=[0]*(2*m+1)
    for k in range(1,2*m+1):
        H[k]=(H[k-1]+inv(k,mod))%mod
        H2[k]=(H2[k-1]+inv(k*k,mod))%mod
    for j in range(m+1):
        if j:
            b=b*(m-j+1)*(2*m-j+1)*inv(2*j*j,mod)%mod
            u=u*(1-p*inv2*inv(j,mod))%mod
            v=v*(1-p*inv2*inv(2*m-j+1,mod))%mod
        # Exact finite-product source labels: inverse denominator and Legendre.
        h=H[j];h2=H2[j]
        htail=(H[2*m]-H[2*m-j])%mod
        htail2=(H2[2*m]-H2[2*m-j])%mod
        P.append(b*v%mod)
        G.append(b*inv(u,mod)%mod)
        E.append(b*(h+htail)%mod)
        F.append(b*(h*h+h2-htail*htail+htail2)%mod)
        assert (G[j]-P[j]-p*inv2*E[j]-p*p*inv(8,mod)*F[j])%mod==0
    zP=root_hensel(P,p);zG=root_hensel(G,p)
    a=evaluate(derivative(P),zP,mod)
    b2=evaluate(derivative(P,2),zP,mod)
    e=evaluate(E,zP,mod)
    ep=evaluate(derivative(E),zP,mod)
    f=evaluate(F,zP,mod)
    root_delta=(zG-zP)%mod
    first=(-p*e*inv(2*a,mod))%mod
    correction=(-b2*e*e*inv(8*a*a*a,mod)+e*ep*inv(4*a*a,mod)-f*inv(8*a,mod))%mod
    pred=(first+p*p*correction)%mod
    assert root_delta==pred,(p,root_delta,pred)
    # Hypergeometric Legendre ODE gives P''/P'=-1/2 mod p at the CM root.
    assert (b2*inv(a,mod)+inv(2,mod))%p==0,(p,'ODE')
    simplified=(first+p*p*(e*e*inv(16*a*a,mod)+e*ep*inv(4*a*a,mod)-f*inv(8*a,mod)))%mod
    assert simplified==root_delta,(p,'simplified-root')
    shift_digit=(root_delta//p)%p
    assert shift_digit==(-e*inv(2*a,p))%p
    return dict(p=p,zP=zP,zG=zG,delta=root_delta,shift_digit=shift_digit,
                second_total=((root_delta-first)%mod//(p*p))%p,
                p2_curvature=(e*e*inv(16*a*a,p))%p,
                p2_Eprime=(e*ep*inv(4*a*a,p))%p,
                p2_F=(-f*inv(8*a,p))%p,
                E0=e%p,F0=f%p,derivative=a%p)

if __name__=='__main__':
    for p in TARGET_PRIMES:
        print('CERT',one(p))
    print('PASS_D25_ROOT_TRANSPORT_ALL_TARGET_INSTANCES',len(TARGET_PRIMES))
