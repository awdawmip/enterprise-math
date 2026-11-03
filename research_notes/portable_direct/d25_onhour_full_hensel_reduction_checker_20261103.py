#!/usr/bin/env python3
"""D25: exact low/middle/H2 four-source mod-p^3 bridge (stdlib, no floats)."""
import json
from math import comb

def inv(a,m): return pow(a%m,-1,m)
def primes(n):
    return [p for p in range(7,n+1) if p%6==1 and all(p%a for a in range(2,int(p**.5)+1))]

def check(p,original_binom=False):
    r=(p-1)//6; n=3*r; mod=p**3; pm=p*p
    chi=-1 if pow(6,(p-1)//2,p)==p-1 else 1
    q2=(pow(2,p-1,pm)-1)//p
    q3=(pow(3,p-1,pm)-1)//p
    eps=(3+(q2-3*q3)*inv(2,p))%p
    B=1; H1=H2=0
    lowA=lowB=lowC=0
    orig=1; Worig=0
    for k in range(p):
        if k<=2*r:
            weight=6*k+1
            lowA=(lowA+weight*B)%mod
            lowB=(lowB+weight*B*H1)%pm
            lowC=(lowC+weight*B*(H1*H1-H2)*inv(2,p))%p
            pred=B*(1+p*H1+p*p*(H1*H1-H2)*inv(2,p))%mod
            assert pred==orig,(p,k,'low-exact',pred,orig)
        Worig=(Worig+(6*k+1)*orig)%mod
        if k==p-1: break
        ratio_num=(2*k+1)*(3*k+1)*(3*k+2)
        orig=orig*ratio_num*inv(36*(k+1)**3,mod)%mod
        if k<2*r:
            d1=k-3*r;d2=k-2*r;d3=k-4*r
            a=(inv(2*d1,mod)+inv(3*d2,mod)+2*inv(3*d3,mod))%mod
            d=(inv(4*d1*d1,mod)+inv(9*d2*d2,mod)+4*inv(9*d3*d3,mod))%mod
            H1=(H1+a)%mod;H2=(H2+d)%mod
            B=B*(k-3*r)*(k-2*r)*(k-4*r)*inv(2*(k+1)**3,mod)%mod
    u0=1; f=1; E=0
    M0=M1=high=0
    for s in range(r):
        w=-2-6*s
        M0=(M0+w*u0)%pm
        M1=(M1+(3+w*E)*u0)%p
        high=(high+(6*s+4)*f)%p
        if s==r-1:break
        t=s+1
        R0=t*(36*t*t-1)*inv(9*(2*t-1)**3,pm)%pm
        u0=u0*inv(R0,pm)%pm
        f=f*t*(36*t*t-1)*inv(9*(2*t+1)**3,p)%p
        E=(E+inv(2*t,p)+3*inv(6*t-1,p)+3*inv(6*t+1,p)-3*inv(2*t-1,p))%p
    term0=lowA
    term1=p*(lowB-2*chi*M0)
    term2=p*p*(lowC-2*chi*(M1+eps*M0)+chi*inv(9,p)*high)
    reduced=(term0+term1+term2)%mod
    first_residue=(lowA+p*(lowB-2*chi*M0)-p)%mod
    assert first_residue%pm==0,(p,'first-digit')
    D=first_residue//pm
    C=lowC%p
    middle_second=(-2*chi*(M1+eps*M0))%p
    high_second=(chi*inv(9,p)*high)%p
    if (Worig-p)%pm==0:
        assert (D+C+middle_second+high_second)%p==((Worig-p)//pm)%p
    assert reduced==Worig,(p,'full',reduced,Worig)
    if original_binom:
        witness=sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*inv(216**k,mod) for k in range(p))%mod
        assert witness==Worig
    return dict(p=p,chi=chi,epsilon=eps,original_W=Worig,lowA=lowA,lowB=lowB,lowC=lowC,M0=M0%p,M0modp2=M0,M1=M1,high=high,D=D,C=C,middle_second=middle_second,high_second=high_second,reduced_W=reduced,second_digit_residual=((Worig-p)//pm)%p if (Worig-p)%pm==0 else None)

if __name__=='__main__':
    rs=[check(p,p in {7,13,19,37,43,373}) for p in primes(2000)]
    print('PASS full 3-source Hensel reduction',len(rs),'primes, 7<=p<=2000 and p=1 mod6')
    print('witnesses',json.dumps([x for x in rs if x['p'] in {7,13,19,37,43,373}],ensure_ascii=False))
    with open('d25_onhour_full_hensel_reduction_results_20261103.json','w') as f:
        json.dump({'status':'AUTHOR_EXACT_CHECKED','primes':len(rs),'test_p_range':'7..2000, p=1 (mod6)','original_integer_binomial_witnesses':[7,13,19,37,43,373],'examples':[x for x in rs if x['p'] in {7,13,19,37,43,373}]},f,indent=2)
