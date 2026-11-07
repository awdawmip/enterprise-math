#!/usr/bin/env python3
"""Exact finite-field checks for the author-side CM/Hasse-zero proof.
No native H0/B0 or Frobenius benchmark is claimed. Python 3 standard library only.
"""
from math import comb

def primes(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(n ** .5) + 1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * ((n-d*d)//d + 1)
    return [p for p in range(5,n+1) if sieve[p] and p%24 in (13,19)]

def binom_cross(u,v,p):
    a,row = 1,[1]
    for i in range(1,min(u,v)+1):
        a = a*(u-i+1)*(v-i+1)*pow(i*i,-1,p)%p
        row.append(a)
    return row

def fm(a,b,p):
    return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def fa(a,b,p):
    return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def fneg(a,p):
    return ((-a[0])%p,(-a[1])%p)
def fpow(a,n,p):
    v=(1,0)
    while n:
        if n&1: v=fm(v,a,p)
        a=fm(a,a,p);n>>=1
    return v
def fdiv(a,b,p):
    norm=(b[0]*b[0]-2*b[1]*b[1])%p
    assert norm,('division by zero',p,b)
    inv=pow(norm,-1,p)
    return fm(a,(b[0]*inv%p,-b[1]*inv%p),p)
def feval(coeff,t,p):
    out=(0,0)
    for c in reversed(coeff):
        out=fa(fm(out,t,p),(c,0),p)
    return out

def poly_mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            out[i+j]=(out[i+j]+ai*bj)%p
    return out
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def poly_substitution(q,p):
    out=[0]
    for c in reversed(q):
        out=poly_mul(out,[0,4%p,-4%p],p)
        out[0]=(out[0]+c)%p
    return trim(out)

def verify(p):
    assert pow(2,(p-1)//2,p)==p-1
    assert pow(-6%p,(p-1)//2,p)==p-1
    m=(p-1)//6
    a=binom_cross(m,2*m,p)
    ra=binom_cross(2*m,4*m,p)
    k=(p-3)//8 if p%8==3 else (p-5)//8
    b=binom_cross(k,3*k+1,p)
    rb=binom_cross((-pow(4,-1,p))%p,(-3*pow(4,-1,p))%p,p)
    euler=(p%8==5)
    if p<=200:
        assert poly_substitution(a,p)==trim(ra.copy())
        bp=poly_substitution(b,p)
        if euler:bp=trim(poly_mul(bp,[1,-2%p],p))
        assert bp==trim(rb.copy())
        n=(p-1)//2
        h=[(-1)**(n+j)*comb(n,j)*comb(2*n-2*j,n)%p
           for j in range(n//2+1)]
        assert h==rb
    for sign in (1,-1):
        s=(0,sign%p)
        xa=fdiv(fa((2,0),s,p),(4,0),p)
        yb=fdiv(fa((3,0),fm((2,0),s,p),p),(6,0),p)
        assert fm((4,0),fm(xa,fa((1,0),fneg(xa,p),p),p),p)==fdiv((1,0),(2,0),p)
        assert fm((4,0),fm(yb,fa((1,0),fneg(yb,p),p),p),p)==fdiv((1,0),(9,0),p)
        ja=fdiv(fm((27,0),fpow(fa((1,0),fm((8,0),xa,p),p),3,p),p),
                fm(xa,fpow(fa((1,0),fneg(xa,p),p),3,p),p),p)
        jb=fdiv(fm((64,0),fpow(fa((1,0),fm((3,0),yb,p),p),3,p),p),
                fm(yb,fpow(fa((1,0),fneg(yb,p),p),2,p),p),p)
        jcm=(2417472%p,sign*1707264%p)
        assert ja==jb==jcm,('CM j mismatch',p,sign)
        assert feval(ra,xa,p)==(0,0),('Hesse Hasse nonzero',p,sign)
        assert feval(rb,yb,p)==(0,0),('2-torsion Hasse nonzero',p,sign)
        assert feval(a,(pow(2,-1,p),0),p)==(0,0),('A nonzero',p)
        assert feval(b,(pow(9,-1,p),0),p)==(0,0),('B nonzero',p)

def main():
    target=primes(2000)
    assert len(target)==77,len(target)
    for p in target:verify(p)
    print('PASS: 77 target primes <= 2000; both Galois fibers; two curve Hasse zeros;')
    print('  both quadratic transformations (p<=200), exact CM j and inertness.')

if __name__=='__main__':
    main()
