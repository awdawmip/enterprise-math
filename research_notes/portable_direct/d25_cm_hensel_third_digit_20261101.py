#!/usr/bin/env python3
"""D25 p=19 mod24 signed-boundary contribution to third-digit CM Gauss root.
Author-only exact computation; native same-class H0/B0 experiment is distinct.
"""
from math import isqrt


def primes(limit):
    sieve=bytearray(b'\x01')*(limit+1); sieve[:2]=b'\x00\x00'
    for q in range(2,isqrt(limit)+1):
        if sieve[q]: sieve[q*q:limit+1:q]=b'\x00'*((limit-q*q)//q+1)
    return [p for p in range(19,limit+1) if sieve[p] and p%24==19]


def beta_gh_jets(p):
    m=p**3
    b=1;g=z=w=0
    for k in range(p):
        g=(g+b)%m
        z=(z+k*b)%m
        w=(w+k*(k-1)*b)%m
        if k+1<p:
            b=b*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,m)%m
    h=(g+16*z)%m
    D=9*z%(p*p)
    C=81*w%p
    return g,h,D,C


def reflected_u(p):
    t=(p-3)//8
    b=q=1;S=M=U=0
    for i in range(1,t+1):
        if i>1:
            r=i-2
            q=q*576*(r+1)**2*pow((8*r+13)*(8*r+15),-1,p)%p
        S=(S+q)%p
        M=(M+(i-1)*q)%p
        k=i-1
        b=b*(8*k+1)*(8*k+3)*pow(576*i*i,-1,p)%p
        U=(U+b*((8*i-7)*S-8*M))%p
    return U*6*pow(35,-1,p)%p


def polynomial_value(p,arg):
    mod=p**3
    t=s=1
    for k in range(p-1):
        t=t*(8*k+1)*(8*k+3)*arg*pow(64*(k+1)**2,-1,mod)%mod
        s=(s+t)%mod
    return s


def verify(limit=1500):
    for p in primes(limit):
        m=p**3; mm=p*p
        G,H,D,C=beta_gh_jets(p)
        U=reflected_u(p)
        h=H%mm; di=D%p
        assert G%p==0 and h%p and di
        g=((1+p*U)*pow(h,-1,mm))%mm
        assert G//p%mm==g, ('signed-tail p3 predecessor',p)
        d1=(-g*pow(di,-1,p))%p
        assert (g+d1*D)%p==0
        q=((g+d1*D)//p)%p
        d2=(-(q+d1*d1*pow(2,-1,p)*C)*pow(di,-1,p))%p
        # Isolate the boundary source by setting U to zero, not by erasing it.
        g0=pow(h,-1,mm)
        assert (g0+d1*D)%p==0
        q0=((g0+d1*D)//p)%p
        d20=(-(q0+d1*d1*pow(2,-1,p)*C)*pow(di,-1,p))%p
        assert (d2-d20)%p==d1*U%p
        z0=pow(9,-1,m)
        root=(z0+p*d1+mm*d2)%m
        assert polynomial_value(p,root)==0,(p,root,d1,d2)
        assert polynomial_value(p,(root+mm)%m)==mm*di%m
        if p in (19,43,67,139,211,523):
            print(dict(p=p,U=U,d1=d1,d2=d2,d2_without_signed_tail=d20,
                       signed_tail_shift=d1*U%p,root_modp3=root))
    print('PASS',len(primes(limit)),'p=19 mod24 primes <=',limit,
          'signed p^2 tail shift in third digit independently verified')

if __name__=='__main__': verify()
