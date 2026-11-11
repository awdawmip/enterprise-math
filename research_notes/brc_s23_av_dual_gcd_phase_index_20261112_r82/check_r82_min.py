#!/usr/bin/env python3
"""Compact exact R82 reproduction: gcd, normalized readout, class certificates."""
from fractions import Fraction as Q
from math import gcd, floor, ceil
from random import Random

def frac(x): return x-floor(x)

def winner(events,a,b,j,x,theta):
    A,B=frac(a*theta),frac(b*theta)
    if A==B:return None
    def inside(z):return (A<=z<B) if A<B else (z>=A or z<B)
    return max(((t,k) for t,k in events if inside(frac(x+(t-j)*theta))),default=None)

def gap_gcd(events,j,a,b):
    times=sorted(set(t for t,k in events))
    if not times:return gcd(abs(a),abs(b))
    d=0
    for u,v in zip(times,times[1:]):d=gcd(d,v-u)
    return gcd(gcd(abs(a),abs(b)),gcd(d,abs(times[0]-j)))

def direct_gcd(events,j,a,b):
    d=gcd(abs(a),abs(b))
    for t,k in events:d=gcd(d,abs(t-j))
    return d

def normalized_winner(events,a,b,j,x,theta,g):
    eta=g*theta; A,B=frac(a//g*eta),frac(b//g*eta)
    if A==B:return None
    def inside(z):return (A<=z<B) if A<B else (z>=A or z<B)
    return max(((t,k) for t,k in events if inside(frac(x+(t-j)//g*eta))),default=None)

def out_class(times,r,p,q,a,b,j,x,L,U):
    anchor=Q(p,q);ka,kb=floor(a*L),floor(b*L)
    assert ka==floor(a*U) and kb==floor(b*U)
    assert a*L-ka<b*L-kb and a*U-ka<b*U-kb
    beta=frac(Q(r,q)+x-j*anchor)
    products=[(t-j)*(z-anchor) for t in (min(times),max(times)) for z in (L,U)]
    sm,sp=beta+min(products),beta+max(products)
    qlo=min(a*L-ka,a*U-ka);qhi=max(b*L-kb,b*U-kb)
    return ceil(sm-qhi)>floor(sp-qlo)

rng=Random(8220261112)
for n in range(2500):
    E={(rng.randrange(-20,21),rng.randrange(5)) for _ in range(rng.randrange(1,24))}
    a,b,j=(rng.randrange(-30,31) for _ in range(3))
    g=gap_gcd(E,j,a,b);assert g==direct_gcd(E,j,a,b)
    theta=Q(rng.randrange(-60,61),rng.randrange(1,50))
    x=Q(rng.randrange(-15,16),rng.randrange(1,40))
    if g>0:
        assert winner(E,a,b,j,x,theta)==normalized_winner(E,a,b,j,x,theta,g)
        assert winner(E,a,b,j,x,theta)==winner(E,a,b,j,x,theta+Q(1,g))
for N in (1,2,4,8,16,32,64,128,256):
    E={(16*k,0) for k in range(1,N+1)}|{(16*k-4,1) for k in range(1,N+1)}
    theta0=Q(1,16);L=theta0-Q(1,1000*N);U=theta0+Q(1,1000*N)
    assert gap_gcd(E,0,4,8)==4
    groups={r:sorted(t for t,k in E if t%16==r) for r in (0,12)}
    assert all(out_class(ts,r,1,16,4,8,0,Q(0),L,U) for r,ts in groups.items())
    assert winner(E,4,8,0,Q(0),theta0) is None
    new=E|{(16*N+5,2)}
    assert gap_gcd(new,0,4,8)==1
    assert winner(new,4,8,0,Q(0),theta0)==(16*N+5,2)
print('R82_MIN_PASS',2500,9)
