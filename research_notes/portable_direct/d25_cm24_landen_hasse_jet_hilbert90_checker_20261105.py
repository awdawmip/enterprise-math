#!/usr/bin/env python3
"""CM−24 split-class Hasse first-jet exact finite field/Hilbert90 checks."""
from math import isqrt
def prime(p):return p>=2 and all(p%k for k in range(2,isqrt(p)+1))
def add(x,y,p):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def neg(x,p):return ((-x[0])%p,(-x[1])%p)
def sub(x,y,p):return add(x,neg(y,p),p)
def mul(x,y,p):return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def inv(x,p):
    den=(x[0]*x[0]-2*x[1]*x[1])%p
    assert den
    return (x[0]*pow(den,-1,p)%p,-x[1]*pow(den,-1,p)%p)
def div(x,y,p):return mul(x,inv(y,p),p)
def power(x,n,p):
    o=(1,0)
    while n:
        if n&1:o=mul(o,x,p)
        x=mul(x,x,p);n//=2
    return o
def h_val_d(m,t,p):
    comb=[1]*(m+1);inverses=[0]*(m+1)
    if m:inverses[1]=1
    for j in range(2,m+1):inverses[j]=(p-(p//j)*inverses[p%j]%p)%p
    for j in range(1,m+1):comb[j]=comb[j-1]*(m-j+1)*inverses[j]%p
    hh=(0,0);hd=(0,0)
    for j in range(m,-1,-1):
        hd=add(mul(hd,t,p),hh,p)
        hh=add(mul(hh,t,p),(comb[j]*comb[j]%p,0),p)
    return hh,hd
def run(B=20000):
    total=0;nonzero=[];samples=[]
    for p in range(5,B+1):
        if p%24!=5 or not prime(p):continue
        rt=next((x for x in range(1,p) if x*x%p==6%p),None)
        assert rt is not None
        s=((3+rt)%p,(2+rt)%p)
        t=power(s,2,p);r=div(sub((1,0),s,p),add((1,0),s,p),p)
        assert power(s,p,p)==r
        H,Hd=h_val_d((p-1)//2,t,p)
        assert H!=(0,0),p
        rhs=mul(power(add((1,0),s,p),p-1,p),h_val_d((p-1)//2,power(r,2,p),p)[0],p)
        assert H==rhs,(p,'Landen value')
        D=div(Hd,H,p)
        num=add(sub((1,0),mul((7,0),power(t,2,p),p),p),mul((2,0),t,p),p)
        den=mul((16,0),mul(t,mul(sub((1,0),t,p),add((1,0),t,p),p),p),p)
        Dc=neg(div(num,den,p),p)
        delta=sub(D,Dc,p)
        g=div(mul((0,1),sub((1,0),s,p),p),power(add((1,0),s,p),2,p),p)
        c=div(delta,g,p)
        assert c[1]==0,(p,'Hilbert90 residual not scalar',c)
        if c[0]:nonzero.append((p,c[0]))
        lhs=mul(mul((2,0),s,p),D,p)
        term=mul(div(mul((4,0),r,p),power(add((1,0),s,p),2,p),p),power(D,p,p),p)
        rhs=neg(add(div((1,0),add((1,0),s,p),p),term,p),p)
        assert lhs==rhs,(p,'first jet',lhs,rhs)
        if p in (5,29,53,101):samples.append((p,rt,H,Hd,D,Dc,c))
        total+=1
    print('PASS split_primes=%d Landen_values=%d jets=%d H90=%d nonzero_c=%d'%(total,total,total,total,len(nonzero)))
    print('sample:',samples)
if __name__=='__main__':run()
