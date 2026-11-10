#!/usr/bin/env python3
"""D25 W216 exact moment identity + finite first/fourth jet checks. AUTHOR_SIDE."""
from fractions import Fraction
from math import factorial, comb, isqrt

def a_rational(k):
    return Fraction(factorial(2*k)*factorial(3*k),factorial(k)**5*216**k)

def rational_check(N):
    a=[a_rational(k) for k in range(N)]
    M=[sum((comb(k,j)*a[k] for k in range(j,N)),Fraction(0)) for j in range(4)]
    lhs=27*(M[2]+2*M[3])-M[0]-11*M[1]
    rhs=-9*(Fraction(N)-Fraction(1,2))*(Fraction(N)-Fraction(2,3))*(Fraction(N)-Fraction(1,3))*a[-1]
    assert lhs==rhs,(N,lhs,rhs)

def strip(n,p):
    v=0
    while n%p==0:
        n//=p;v+=1
    return v,n

def stream(p,n,prec):
    mod=p**prec; inv36=pow(36,-1,mod);v,u=0,1
    for k in range(n):
        yield k, (pow(p,v,mod)*u)%mod if v<prec else 0,v
        if k==n-1:break
        numerator=inv36
        for x in (2*k+1,3*k+1,3*k+2):
            e,y=strip(x,p);v+=e;numerator=numerator*y%mod
        for x in (k+1,k+1,k+1):
            e,y=strip(x,p);v-=e;numerator=numerator*pow(y,-1,mod)%mod
        assert v>=0
        u=u*numerator%mod

def check(p):
    mod=p**4;big=p**8; M=[0]*4;blocks=[0]*4;av=[];vv=[]
    for k,a,v in stream(p,4*p,8):
        blocks[k//p]=(blocks[k//p]+(6*k+1)*a)%big
        if k<p:
            for j in range(4):
                if k>=j:M[j]=(M[j]+comb(k,j)*a)%mod
        if k<4:av.append(a);vv.append(v)
    C=[]
    for j in range(4):
        pv=p**vv[j]
        assert blocks[j]%pv==0 and av[j]%pv==0
        C.append((blocks[j]//pv)*pow(av[j]//pv,-1,mod)%mod)
    q=[sum((-1)**(j-i)*comb(j,i)*C[i] for i in range(j+1))%mod for j in range(4)]
    assert (27*(M[2]+2*M[3])-M[0]-11*M[1]+p**3)%mod==0
    chi=1 if p%3==1 else -1
    assert (q[0]-chi*p)%p**3==0
    assert (q[1]-6*chi*p)%p**3==0
    assert q[2]%p**3==0
    assert (q[3]-2*q[2])%mod==0 # finite-only; not a universal proof
    if M[0]%p==M[1]%p==0:
        assert (M[2]+2*M[3])%p==0
    return {'p':p,'moments_mod_p':[x%p for x in M],
            'q2_div_p3':q[2]//p**3,'q3_div_p3':q[3]//p**3}

def primes_through(n):
    s=bytearray(b'\x01')*(n+1);s[:2]=b'\x00\x00'
    for j in range(2,isqrt(n)+1):
        if s[j]:s[j*j::j]=b'\x00'*(((n-j*j)//j)+1)
    return [j for j in range(5,n+1) if s[j]]

if __name__=='__main__':
    for n in range(1,13):rational_check(n)
    primes=primes_through(2000)
    results=[check(p) for p in primes]
    assert len(results)==301
    target=[x for x in results if x['p']%24 in (13,19)]
    assert len(target)==77
    assert all(x['moments_mod_p'][:2]==[0,0] for x in target)
    print('PROVED_IDENTITY_RATIONAL_EXACT_CHECKS',12)
    print('FINITE_PRIME_CHECKS',len(primes),'TARGET_CLASSES',len(target))
    for p in (13,19,373,10069,10099):
        r=next((x for x in results if x['p']==p),None) or check(p)
        print('EXACT',r)
