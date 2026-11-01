#!/usr/bin/env python3
"""Independent cubic-Hasse vs reflected coefficients and two finite-log certificates."""
from math import comb

def hsource(p):
    d=(p-3)//4; h=[1]
    for j in range(d):
        h.append(h[-1]*(4*j+3)**3*pow((4*j+4)*(4*j+5)*(4*j+6),-1,p)%p)
    return h

def hasse(p):
    d=(p-3)//4; N=(p-1)//2; H=[0]*(d+1); i8=pow(8,-1,p)
    for j in range(d+1):
        b=comb(N,2*j)*comb(2*j,j)*pow(i8,j,p)%p
        for k in range(j+1): H[k]=(H[k]+b*comb(j,k))%p
    assert all(H[k]==0 for k in range(1,d+1,2))
    return H

def polyval(a,x,p):
    v=0
    for c in reversed(a):v=(v*x+c)%p
    return v

def compute(p,a):
    d=(p-3)//4; m=d//2; H=hasse(p); E=H[::2]; D=comb(3*m+1,m)%p
    G=[0]*(m+1)
    for k,v in enumerate(E):
        for j in range(k+1):G[m-k+j]=(G[m-k+j]+v*comb(k,j)*(-1)**(k-j))%p
    F=[v*pow(D,-1,p)%p for v in G]
    assert F[0]==1
    square=[0]*(d+1)
    for i,u in enumerate(F):
        for j,v in enumerate(F):square[i+j]=(square[i+j]+u*v)%p
    h=hsource(p)
    assert square==h
    def finite_log(t):
        z=(1-pow(t,p,p*p)-pow(1-t,p,p*p))%(p*p)
        assert z%p==0
        return z//p
    tail=sum((8*j+5)*v*pow(a,d+1+j,p)*pow(d+1+j,-1,p) for j,v in enumerate(h))%p
    mom=0; plus=0; minus=0
    Ep=[k*E[k]%p for k in range(1,len(E))]
    for y in range(p):
        r=(1-y)%p
        if not r:continue
        chi=pow(r,(p-1)//2,p)
        e=polyval(E,y,p); ed=polyval(Ep,y,p)
        l=finite_log(a*r%p)
        mom=(mom+chi*e*e*l)%p
        term=(16*r*e*ed-e*e)*l%p
        if chi==1:plus=(plus+term)%p
        else:minus=(minus+term)%p
    y0=(1-pow(a,-1,p))%p
    contact=8*pow(a,(p-1)//2,p)*pow(polyval(E,y0,p),2,p)%p
    assert (contact-3*mom)*pow(D,-2,p)%p==tail
    assert -(plus-minus)*pow(D,-2,p)%p==tail
    return tail,D,polyval(E,y0,p),mom,contact,plus,minus

def main():
    primes=[p for p in range(11,1000,8) if all(p%q for q in range(2,int(p**0.5)+1))]
    cases=0
    for p in primes+[3347]:
        for a in (list(range(1,p)) if p<=59 else [9]):
            r=compute(p,a)
            cases+=1
        if p==3347:
            assert r==(0,3073,783,1568,1357,1681,1681),r
            print('p=3347 result',r)
    print('PASS_GH100_GH101_COMPACT',len(primes)+1,'primes',cases,'parameter cases')

if __name__=='__main__':main()
