"""D25 native scalar LIFT: exact valuation-band formula; author-side checker.
Uses frozen D=-24 B[k+1]/B[k] = (6k+1)(3k+1)/(36(k+1)^2).
"""
from math import isqrt
from fractions import Fraction

def primes(n):
    a = bytearray([1])*(n+1); a[:2] = b'\0\0'
    for k in range(2,isqrt(n)+1):
        if a[k]: a[k*k::k] = bytes(len(a[k*k::k]))
    return [p for p in range(7,n+1) if a[p] and p%24 in (13,19)]

def check(p):
    m=(p-1)//6; mod=p**3; b=1
    f=[1]*p
    for k in range(1,p): f[k]=f[k-1]*k%p
    fi=[1]*p; fi[-1]=pow(f[-1],-1,p)
    for k in range(p-1,0,-1): fi[k-1]=fi[k]*k%p
    inv2=pow(2,-1,p); inv6=pow(6,-1,p); inv18=pow(18,-1,p)
    g=[0,0,0]; h=[0,0,0]; mid=high=0
    for k in range(p):
        e=0 if k<=m else 1 if k<=2*m else 2
        g[e]=(g[e]+b)%mod; h[e]=(h[e]+(12*k+1)*b)%mod
        if e==0:
            v=f[m]*f[2*m]*fi[m-k]*fi[2*m-k]*fi[k]**2*pow(inv2,k,p)%p
        elif e==1:
            v=(-1)**(m+k)*f[m]*f[2*m]*f[k-m-1]*fi[2*m-k]*fi[k]**2*pow(inv2,k,p)*inv6%p
            mid=(mid+(12*k+1)*v)%p
        else:
            v=(-1)**m*f[m]*f[2*m]*f[k-m-1]*f[k-2*m-1]*fi[k]**2*pow(inv2,k,p)*inv18%p
            high=(high+v)%p
        assert b%(p**e)==0 and b%(p**(e+1))!=0
        assert b//p**e%p==v, (p,k,e)
        if k<p-1: b=b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod)%mod
    assert g[0]%p==0 and g[1]%p==0 and g[2]%(p*p)==0
    U=((g[0]+g[1])%mod)//p; H0=h[0]%(p*p)
    assert (U*H0)%p==1
    c0=((U*H0-1)%(p*p))//p
    c1=U*mid%p; c2=H0*high%p
    delta=(c0+c1+c2)%p
    G=(sum(g)%mod)//p; H=sum(h)%(p*p)
    assert ((G*H-1)%(p*p))//p==delta
    assert h[1]//p%p==mid and g[2]//(p*p)%p==high
    return (p,c0,c1,c2,delta)

def independent_rational(p):
    m=(p-1)//6; b=Fraction(1); g=h=Fraction(0)
    for k in range(p):
        g+=b; h+=(12*k+1)*b
        if k<p-1: b*=Fraction((6*k+1)*(3*k+1),36*(k+1)**2)
    def res(q,n):
        q=Fraction(q); mod=p**n
        assert q.denominator%p
        return q.numerator*pow(q.denominator,-1,mod)%mod
    G=res(g/p,2);H=res(h,2)
    assert G*H%p==1
    return (G*H-1)%(p*p)//p

if __name__=='__main__':
    rows=[check(p) for p in primes(5000)]
    for p in primes(90):assert check(p)[-1]==independent_rational(p)
    print('166-prime check:',len(rows),'PASS')
    print('independent rational:',len(primes(90)),'PASS')
    print('nonzero upper contributions:',sum(r[3]!=0 for r in rows))
    for row in rows[:13]: print(*row)
