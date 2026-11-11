#!/usr/bin/env python3
"""Original E3 fixed-z formal differential and lambda derivative.
Exact ring: (Z/p^3 Z)[T]/(T^2-2). AUTHOR_SIDE/UNREVIEWED/NOT_NATIVE_H0B0.
"""
from math import comb

PRIMES=(13,19,37,43,109,139,157,373)
def add(x,y,q):return ((x[0]+y[0])%q,(x[1]+y[1])%q)
def mul(x,y,q):return ((x[0]*y[0]+2*x[1]*y[1])%q,(x[0]*y[1]+x[1]*y[0])%q)
def scale(x,a,q):return (x[0]*a%q,x[1]*a%q)

def formal(p):
    # E3: y^2+xy+(t/27)y=x^3, z=-x/y, w=-1/y.
    # (1-z)w-(t/27)w^2=z^3; omega=dz/(1-z-2(t/27)w).
    q=p**3;n=p-1
    a=scale((2,-1),pow(108,-1,q),q)
    w=[(0,0)]*(n+1); dw=[(0,0)]*(n+1)
    h=[(0,0)]*(n+1); dh=[(0,0)]*(n+1); h[0]=(1,0)
    for k in range(1,n+1):
        s=(0,0);ds=(0,0)
        for i in range(3,k-2):
            j=k-i
            s=add(s,mul(w[i],w[j],q),q)
            ds=add(ds,add(mul(dw[i],w[j],q),mul(w[i],dw[j],q),q),q)
        w[k]=add(w[k-1],add(((1,0) if k==3 else (0,0)),mul(a,s,q),q),q)
        dw[k]=add(dw[k-1],add(s,mul(a,ds,q),q),q)
        sh=(0,0);sdh=(0,0)
        for i in range(3,k+1):
            j=k-i
            sh=add(sh,mul(w[i],h[j],q),q)
            sdh=add(sdh,add(mul(dw[i],h[j],q),mul(w[i],dh[j],q),q),q)
        h[k]=add(h[k-1],scale(mul(a,sh,q),2,q),q)
        dh[k]=add(dh[k-1],scale(add(sh,mul(a,sdh,q),q),2,q),q)
    return h[n],scale(dh[n],pow(27,-1,q),q)

def binomial(p):
    # Independent direct Ditters/Lemma-12 coefficient formula.
    q=p**3;n=p-1;a=scale((2,-1),pow(108,-1,q),q)
    power=(1,0);prev=(1,0);h=(0,0);dh=(0,0)
    for j in range(n//3+1):
        c=comb(n-j,j)*comb(n-2*j,j)
        h=add(h,scale(power,c,q),q)
        if j:dh=add(dh,scale(prev,j*c*pow(27,-1,q),q),q)
        prev=power;power=mul(power,a,q)
    return h,dh

def scalar(p):
    # Frozen B_n=(1/6)_n(1/3)_n/[2^n(n!)^2].
    q=p**3;b=1;g=0;h=0
    for k in range(p):
        g=(g+b)%q;h=(h+(12*k+1)*b)%q
        if k<p-1:b=b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,q)%q
    return g,h

def main():
    for p in PRIMES:
        q=p**3
        H,Ht=formal(p)
        assert (H,Ht)==binomial(p),(p,'formal-vs-binomial')
        # t=(1-sqrt(1-lambda))/2; at lambda=1/2, dt/dlambda=T/4.
        Hlambda=mul(Ht,scale((0,1),pow(4,-1,q),q),q)
        W=add(H,scale(Hlambda,6,q),q)
        g,h=scalar(p)
        assert H[0]%p==g%p==0 and H[1]%p==0
        assert W[0]%p==h%p and W[1]%p==0
        D=((W[0]-h)%q,W[1])
        assert all(v%p==0 for v in D)
        carry=tuple(v//p%p for v in D)
        print('p',p,'H/p modp2',tuple(v//p%p**2 for v in H),
              'dH/dt modp',tuple(v%p for v in Ht),'weighted-source-vs-h carry',carry)
        if p==373:
            assert H==(46042747,33130606)
            assert Ht==(5280934,49750797)
            assert W==(39609787,41052007)
            assert h%139129==62835 and g==24495656
            assert D==(35373082,41052007) and carry==(92,24)
    print('PASS: 8 original-class formal/independent binomial checks; first-digit source bridge and p373 second-digit signed carrier')

if __name__=='__main__':main()
