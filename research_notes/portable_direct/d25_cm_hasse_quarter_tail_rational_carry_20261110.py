"""Exact D25 Hasse quarter-tail, even/odd observers, and independent p² Gauss checks."""
from math import isqrt

def prime(n): return n>1 and all(n%d for d in range(2,isqrt(n)+1))
def ops(m):
    def add(x,y): return ((x[0]+y[0])%m,(x[1]+y[1])%m)
    def mul(x,y): return ((x[0]*y[0]+2*x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0])%m)
    def scale(x,n): return (x[0]*n%m,x[1]*n%m)
    return add,mul,scale
def leg(n,y,m):
    add,mul,scale=ops(m); a,b=(1,0),y
    if n==0: return a
    for k in range(1,n):
        a,b=b,scale(add(scale(mul(y,b),2*k+1),scale(a,-k)),pow(k+1,-1,m))
    return b
def run(p):
    assert p%24==13 and prime(p)
    q=(p-1)//4
    add,mul,scale=ops(p)
    s=(pow(2,-1,p),-pow(3,-1,p)%p)
    sb=(pow(2,-1,p),pow(3,-1,p))
    c=[1]
    for k in range(q):
        c.append(c[-1]*(k-q)*(k+q+1)*pow(k+1,-2,p)%p)
    a=[0]*p
    for n in range(1,p):
        a[n]=sum(c[k]*pow(n-k,-1,p) for k in range(max(0,n-(p-1)),min(q,n-1)+1))%p
    direct=(0,0); spow=(1,0)
    for coef in a:
        direct=add(direct,scale(spow,coef)); spow=mul(spow,s)
    u=[sum(c[k]*pow(k-r,-1,p) for k in range(r+1,q+1))%p for r in range(q)]
    d=pow(36,-1,p)
    tail=scale(sb,u[0]); spow=(1,0)
    for r in range(1,q):
        tail=add(tail,scale(spow,d*u[r])); spow=mul(spow,s)
    assert direct==tail
    T=[2,1]; D=[0,-2*pow(3,-1,p)%p]
    for r in range(2,q):
        T.append((T[-1]-d*T[-2])%p)
        D.append((D[-1]-d*D[-2])%p)
    tr=(u[0]+d*sum(u[r]*T[r-1] for r in range(1,q)))%p
    odd=(u[0]*pow(3,-1,p)+d*pow(2,-1,p)*sum(u[r]*D[r-1] for r in range(1,q)))%p
    assert tr==2*tail[0]%p and odd==tail[1]
    m=p*p; add2,mul2,scale2=ops(m)
    y=(0,2*pow(3,-1,m)%m)
    aa,bb=leg(q,y,m),leg(3*q,y,m)
    assert aa[0]==bb[0]==0 and aa[1]%p==bb[1]%p==0
    g=(3*(aa[1]//p)+bb[1]//p)*pow(4,-1,p)%p
    s2=(pow(2,-1,m),-pow(3,-1,m)%m)
    original=(0,0); x=(1,0);v=1
    for k in range(p):
        original=add2(original,scale2(x,v))
        if k<p-1:
            v=v*(4*k+1)*(4*k+3)*pow(16*(k+1)**2,-1,m)%m
            x=mul2(x,s2)
    assert original==(0,(p*g)%m), (p,original,g)
    return (p,q,tr,g,u[0],odd,(tr-24*g)%p)

if __name__=='__main__':
    data=[run(p) for p in range(13,1000,24) if prime(p)]
    assert len(data)==22
    assert all(row[-1]==0 for row in data) # computational observation, NOT a proof
    print('22 prime exact checks PASS; p<1000; all modules original/auxiliary kept separate')
    for r in data:
        if r[0] in (13,37,373,613,997): print(r)
