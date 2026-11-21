#!/usr/bin/env python3
"""EC49FVR: exact two-scale 46-layer phase mesh (standard library only)."""
from fractions import Fraction as Q
from functools import reduce
from math import gcd, lcm
p = 11
U, Gamma = Q(4822040484, 8132285009), Q(141024, 1653649)
red = lambda x: x.numerator*pow(x.denominator, -1, p)%p
u, g, inv = red(U), red(Gamma), pow(637, -1, p)
rows = []
for z in range(p):
    la, lb = (637-3*z)*inv%p, u*(1+g*z)%p
    a, b = (1-(1-z)*la)%p, (1-(1-z)*lb)%p
    rows.append((z, a, b, la, lb))
c, d = -3*inv%p, u*g%p

def direct(h, n):
    for z,a,b,la,lb in rows:
        if z == 3:
            v = pow(la,n-1,p)*pow(a,h-1,p)*(n*a-h*(1-z)*la)%p
        else:
            v = (pow(a,h,p)*pow(la,n,p)-pow(b,h,p)*pow(lb,n,p))*pow((la-lb)%p,-1,p)%p
        if not v: return False
    return (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p != 0

pat={(h%10,n%10) for h in range(1,11) for n in range(1,11)
     if all((pow(a,h,p)*pow(la,n,p)-pow(b,h,p)*pow(lb,n,p))*pow((la-lb)%p,-1,p)%p
            for z,a,b,la,lb in rows if z != 3)
     and (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p}
assert len(pat)==44
cert=lambda h,n: (h%10,n%10) in pat and (9*h+10*n)%11 != 0
assert all(cert(h,n)==direct(h,n) for h in range(1,111) for n in range(1,111))
print('12100 direct projective checks PASS')

base=[(1,0),(7,3),(13,4),(1,1),(1,2),(1,3),(1,4),(7,4),
      (13,5),(7,5),(1,5),(1,6),(7,6),(13,6),(1,7),(7,7),(13,7),(91,7)]
menu=base+[(3,e) for e in range(2,8)]+[(r,e) for r in (47,11,23,53,27,31,29,61)
                                             for e in range((r-1).bit_length(),8)]
assert len(menu)==46 and len(set(menu))==46
L=reduce(lcm,(r for r,e in menu),1)
assert L==84915883381329
C=2*L
M=14080*C

def layer(j, r, e, level):
    # physical denominator d = 2**level*r*2**(j-e); y=C*2**j*(h/d)
    step=C*2**e//(2**level*r)
    assert C*2**e%(2**level*r)==0
    assert M%step==0 and M//step%lcm(110,2*r)==0
    n=(r*pow(2,j+level-e,110))%110
    return {step*h for h in range(1,M//step) if gcd(h,2*r)==1 and cert(h,n-h)}

def gap(points):
    a=sorted(points)
    return max(a[0]+M-a[-1], *(v-u for u,v in zip(a,a[1:])))

CAND=Q(490,143)
expected={0:(Q(490,143),Q(280,143),Q(7,4)),
          1:(Q(10465,3294),Q(3680,1647),Q(91,64))}
for j in range(14,34):
    current=set().union(*(layer(j,r,e,0) for r,e in menu))
    # All candidate denominators at level j+1 occur at ratios 2*r/2**e.
    additions={}
    for r,e in menu:
        t=Q(2*r,2**e)
        additions.setdefault(t,set()).update(layer(j,r,e,1))
    upper=Q(0)
    witness=None
    for t in sorted(additions):
        if t<=1:
            current.update(additions[t]); continue
        # On the interval H/k < t, this is the full admitted current mask.
        g=Q(gap(current),C)
        if t*g>upper:
            upper=t*g
            witness=(upper,g,t)
        assert t*g<=CAND, (j,t,g)
        current.update(additions[t])
    assert witness==expected[j%2],(j,witness)
    assert len(current)==92960,(j,len(current))
    print('j',j,'max t*gap =',upper,'attained just below ratio',witness[2],
          'gap*k=',witness[1], 'all_points=',len(current))
print('20/20 complete exponent classes PASS')

# Independent finite H spot checks (integer heights, every numerator enumerated directly).
for j in range(8,12):
    k=2**j
    for H in (k, (3*k)//2, (7*k)//4-1, (7*k)//4, 2*k-1):
        points={0,C*k}
        for level in (0,1):
            for r,e in menu:
                den=(2**level)*r*2**(j-e)
                if den>H: continue
                step=C*k//den
                assert C*k%den==0
                points.update(step*h for h in range(1,den)
                              if gcd(h,den)==1 and cert(h,den-h))
        a=sorted(points)
        maxgap=max(b-a for a,b in zip(a,a[1:]))
        assert Q(maxgap,C*k)*H <= CAND
    print('direct finite-height checks PASS at j=',j)
print('THEOREM H>=256: any interval length >490/(143H) contains a certified phase')
print('ALL PASS')
