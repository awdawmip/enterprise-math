#!/usr/bin/env python3
"""D25 author-side Euler-Frobenius factor and Hensel guards; no native experiment."""
from math import comb

def primes_below(bound):
    sieve=bytearray(b'\1')*bound
    sieve[:2]=b'\0\0'
    for k in range(2,int(bound**0.5)+1):
        if sieve[k]:
            sieve[k*k:bound:k]=b'\0'*len(range(k*k,bound,k))
    return [p for p in range(5,bound) if sieve[p]]

def hits(p):
    r1=next((v*p-1)//8 for v in (1,3,5,7) if (v*p-1)%8==0)
    r3=next((v*p-3)//8 for v in (1,3,5,7) if (v*p-3)%8==0)
    return min(r1,r3),max(r1,r3)

def companion(p):
    a,b=hits(p); mod=p*p
    x=total=1; deriv=0
    for n in range(1,b+1):
        x=x*(8*n-7)*(8*n-5)*pow(576*n*n,-1,mod)%mod
        total=(total+x)%mod
        deriv=(deriv+n*x)%mod
    return total,deriv

def multiply(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            out[i+j]=(out[i+j]+u*v)%p
    return out

def factor_check(p):
    a,b=hits(p)
    m=a+b+1-p; c=p-1-b; d=p-1-a
    assert m==(p+1)//2 and c+m==a and 0<=c<d<p
    P=[comb(a,n)*comb(b,n)%p for n in range(a+1)]
    R=[comb(c,n)*comb(d,n)%p for n in range(c+1)]
    F=multiply([(-1)**n*comb(m,n)%p for n in range(m+1)],R,p)
    assert P==F
    z=pow(9,-1,p)
    val=sum(x*pow(z,n,p) for n,x in enumerate(R))%p
    jet=sum(n*x*pow(z,n,p) for n,x in enumerate(R))%p
    kp=sum(x*pow(z,n,p) for n,x in enumerate(P))%p
    dp=sum(n*x*pow(z,n,p) for n,x in enumerate(P))%p
    assert kp==pow(1-z,m,p)*val%p
    if val==0:
        assert dp==pow(1-z,m,p)*jet%p
        assert dp!=0
    return a,b,m,c,d,kp,dp

def main():
    cnt=0
    classes={13:[0,0],17:[0,0],19:[0,0],23:[0,0]}
    for p in primes_below(1000):
        a,b=hits(p)
        z=pow(9,-1,p)
        P=[comb(a,n)*comb(b,n)%p for n in range(a+1)]
        kp=sum(x*pow(z,n,p) for n,x in enumerate(P))%p
        dp=sum(n*x*pow(z,n,p) for n,x in enumerate(P))%p
        K,D=companion(p)
        assert K%p==kp and D%p==dp
        if kp==0:
            assert dp!=0
            eps=-(K//p)*z*pow(dp,-1,p)%p
            assert (K+p*eps*9*D)%(p*p)==0
            if p%24 in classes:
                classes[p%24][0]+=1
                classes[p%24][1]+=(eps==0)
            if p in (13,17,19,23,37,373):
                print('ROOT',p,'K',K,'theta',dp,'epsilon',eps)
        elif p%24 in classes:
            raise AssertionError(('inert root missing',p))
        if p%8 in (5,7):
            q=factor_check(p)
            assert (kp,dp)==(q[-2],q[-1])
            cnt+=1
    assert cnt==86
    assert classes=={13:[22,22],17:[23,0],19:[23,0],23:[22,22]},classes
    print('HENSEL_CLASS_COUNTS',classes)
    print('PASS_D25_EULER_FROBENIUS_SIMPLE_ROOT_HENSEL',cnt)

if __name__=='__main__': main()
