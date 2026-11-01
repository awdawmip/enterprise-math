#!/usr/bin/env python3
"""Exact portable D25 coordinate certificate; NOT native H0/B0 execution."""
import argparse
from math import comb

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for j in range(2,int(n**0.5)+1):
        if sieve[j]:
            sieve[j*j:n+1:j]=b'\x00'*((n-j*j)//j+1)
    return [k for k in range(2,n+1) if sieve[k]]

def f_jet(p,z,m):
    c,zp=1,1
    invz=pow(z,-1,m); invz2=invz*invz%m
    s=d=dd=0
    for k in range(p):
        term=c*zp%m
        s=(s+term)%m
        d=(d+k*term*invz)%m
        dd=(dd+k*(k-1)*term*invz2)%m
        if k+1<p:
            c=c*(8*k+1)*(8*k+3)*pow(64*(k+1)**2,-1,m)%m
            zp=zp*z%m
    return s,d,dd

def q_jet(p,z):
    t=(p-5)//8; a=5*t+3; m=p*p
    q=d=0; zp=1; iz=pow(z,-1,m)
    for j in range(t+1):
        cj=(-1)**j*comb(t,j)*comb(a+j,j)
        v=cj*zp%m
        q=(q+v)%m
        d=(d+j*v*iz)%m
        zp=zp*z%m
    return q,d

def check(p):
    assert p>=13 and p%8==5
    m=p**3; z=pow(9,-1,m); zf=pow(z,p,m)
    q9=((pow(9,p-1,m)-1)//p)%(p*p)
    assert (zf-z)%m==(-p*z*q9+p*p*z*q9*q9)%m
    f,df,ddf=f_jet(p,z,m)
    ff,_,_=f_jet(p,zf,m)
    pred=(-p*z*q9*df+p*p*q9*q9*(z*df+z*z*ddf*pow(2,-1,m)))%m
    assert (ff-f)%m==pred,('Frobenius second-order',p)
    if f%p==0:
        assert df%p!=0 and ff%p==0
        assert (ff//p)%p==((f//p)-(z%p)*(q9%p)*df)%p
    if p%24!=13: return None
    q,dq=q_jet(p,z)
    assert q%p==0 and dq%p!=0 and f%p==0
    K=(8*(z%p)*(1-z)*dq)%p
    sigma=K*df%p
    h=(p-1)//2
    assert sigma==(8*z*pow(1-z,h+2,p)*dq*dq)%p and sigma!=0
    ml=(K*(f//p))%p; mf=(K*(ff//p))%p
    assert (mf-ml)%p==(-(z%p)*(q9%p)*sigma)%p
    root=(z-p*(f//p)*pow(df%p,-1,p))%(p*p)
    assert f_jet(p,root,p*p)[0]==0
    shift=((root-zf%(p*p))%(p*p))//p
    assert shift==(-(f//p)*pow(df%p,-1,p)+(z%p)*(q9%p))%p
    g=None
    if f%(p*p)==0:
        g=(f//(p*p))%p
        r3=(z-p*p*g*pow(df%p,-1,p))%m
        assert f_jet(p,r3,m)[0]==0
        expected=(p*z*q9-p*p*(z*q9*q9+g*pow(df%p,-1,p)))%m
        assert (r3-zf)%m==expected
    return (p,q9%p,z%(p*p),zf%(p*p),f%m,df%p,ml,mf,sigma,shift,g)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--limit',type=int,default=3000)
    args=ap.parse_args()
    pp=[p for p in primes_upto(args.limit) if p>=13 and p%8==5]
    rr=[v for p in pp if (v:=check(p)) is not None]
    print('p q9_modp z_modp2 teich_modp2 F_modp3 Fprime_modp M_rational M_teich sigma root_minus_teich_over_p G_over_p2_modp')
    for v in rr:
        if v[0] in (13,37,61,109,373): print(*v)
    print('PASS_D25_FROBENIUS_COORDINATE_DEFECT',
          'tested_p_5mod8=',len(pp),'tested_p_13mod24=',len(rr),
          'q9_zero_in_target=',sum(v[1]==0 for v in rr),
          'second_digit_eligible=',sum(v[-1] is not None for v in rr),
          'limit=',args.limit)
