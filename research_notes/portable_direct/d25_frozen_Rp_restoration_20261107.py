"""Exact modular D=-24 LIFT: independently pinned reflected R_p and weighted Clausen W_p.

Pure Python, no float, no new assumptions about the frozen theorem.
Only p=13,19 modulo 24 (prime), and all divisions have p-unit denominator.
"""
from math import isqrt

def primes(n):
    s=bytearray(b'\x01')*(n+1)
    s[:2]=b'\x00\x00'
    for k in range(2,isqrt(n)+1):
        if s[k]: s[k*k:n+1:k]=b'\x00'*((n-k*k)//k+1)
    return [p for p in range(13,n+1) if s[p] and p%24 in (13,19)]

def run(p, direct=False):
    assert p%24 in (13,19)
    m=(p-1)//6
    P=p**3
    B=[1]*p
    for k in range(p-1):
        B[k+1]=(B[k]*(6*k+1)*(3*k+1)*pow(36*(k+1)*(k+1),-1,P))%P
    g=sum(B)%P
    h=sum((12*k+1)*B[k] for k in range(p))%P
    assert g%p==0 and ((g//p)*h)%p==1
    Delta=(((g//p)*h-1)//p)%p if ((g//p)*h-1)%p==0 else None
    Delta2=((g*h-p)//(p*p))%p
    assert Delta==Delta2

    c=pow(10,-1,p)
    s0=s1=0
    R=0
    b=1
    for i in range(1,m+1):
        b=b*(m-i+1)*(2*m-i+1)*pow(2*i*i,-1,p)%p
        assert b==B[i]%p
        s0=(s0+c)%p
        s1=(s1+i*c)%p
        R=(R+2*b*((1+6*i)*s0-6*s1))%p
        if i<m:
            c=c*(36*i*i)*pow((6*i+5)*(3*i+2),-1,p)%p

    a=1
    W=0
    for k in range(p):
        W=(W+(6*k+1)*a)%P
        if k<p-1:
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,P)%P
    assert W%p**2==p%p**2
    residual=((W-p)//(p*p))%p

    if direct:
        T=0
        for i in range(1,m+1):
            for r in range(1,i+1):
                T+=(2*(1+6*(i-r))*B[i]*B[p-r])
        T%=P
        assert T%(p*p)==0
        assert (T//(p*p))%p==R
        assert (g*h-W)%P==T
        R2=0
        for i in range(1,m+1):
            for r in range(1,i+1):
                num=pow(2,r-1,p)*pow(__import__('math').factorial(r-1),2,p)%p
                den=(18*pow(6,-r,p)*pow(3,-r,p))%p
                for t in range(r):
                    den=(den*(6*t+5)*(3*t+2))%p
                C_direct=num*pow(den,-1,p)%p
                R2=(R2+2*(1+6*(i-r))*B[i]*C_direct)%p
        assert R2==R, (R,R2)

    assert ((Delta-R)%p)==residual, (p,Delta,R,W,residual)
    return dict(p=p,m=m,Delta=Delta,R=R,E=(Delta-R)%p,W2=residual)

if __name__=='__main__':
    ps=primes(5000)
    for p in ps:
        d=run(p,direct=p<=109)
        if p in (13,19,37,43,109,157,373,1093,3511):print(d)
    print('TOTAL', len(ps),'ALL PASS, max',max(ps))
