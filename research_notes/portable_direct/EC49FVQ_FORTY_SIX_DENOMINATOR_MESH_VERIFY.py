#!/usr/bin/env python3
"""EC49FVQ: exact finite certificate for a 46-layer rational-phase mesh."""
from fractions import Fraction
from math import gcd, lcm
from functools import reduce

P = 11
U = Fraction(4822040484, 8132285009)
G = Fraction(141024, 1653649)
mod = lambda q: q.numerator * pow(q.denominator, -1, P) % P
u, gamma, inv637 = mod(U), mod(G), pow(637, -1, P)
rows = []
for z in range(P):
    la, lb = (637 - 3*z) * inv637 % P, u * (1 + gamma*z) % P
    a, b = (1 - (1-z)*la) % P, (1 - (1-z)*lb) % P
    rows.append((z,a,b,la,lb))
assert [r for r in rows if r[3] == r[4]] == [(3,10,10,10,10)]
c, d = -3*inv637 % P, u*gamma % P

def direct_projective_no_root(h,n):
    for z,a,b,la,lb in rows:
        if z == 3:
            v = pow(la,n-1,P)*pow(a,h-1,P)*(n*a-h*(1-z)*la)%P
        else:
            v = (pow(a,h,P)*pow(la,n,P)-pow(b,h,P)*pow(lb,n,P))*pow((la-lb)%P,-1,P)%P
        if v == 0:
            return False
    return (pow(c,h+n,P)-pow(d,h+n,P))*pow((c-d)%P,-1,P)%P != 0

patterns = {(h%10,n%10) for h in range(1,11) for n in range(1,11)
    if all((pow(a,h,P)*pow(la,n,P)-pow(b,h,P)*pow(lb,n,P))*pow((la-lb)%P,-1,P)%P != 0
           for z,a,b,la,lb in rows if z != 3)
       and (pow(c,h+n,P)-pow(d,h+n,P))*pow((c-d)%P,-1,P)%P != 0}
assert len(patterns) == 44
cert = lambda h,n: (h%10,n%10) in patterns and (9*h+10*n)%11 != 0
assert all(cert(h,n) == direct_projective_no_root(h,n)
           for h in range(1,111) for n in range(1,111))
print('12100/12100 direct projective checks PASS')

base18 = [(1,0),(7,3),(13,4),(1,1),(1,2),(1,3),(1,4),(7,4),
    (13,5),(7,5),(1,5),(1,6),(7,6),(13,6),(1,7),(7,7),(13,7),(91,7)]
menu = base18 + [(3,e) for e in range(2,8)]
menu += [(r,e) for r in (47,11,23,53,27,31,29,61)
         for e in range((r-1).bit_length(),8)]
assert len(menu) == 46 and len(set(menu)) == 46
assert all(r%2 == 1 and 0 <= e <= 7 and r <= 2**e for r,e in menu)
L = reduce(lcm,(r for r,e in menu),1)
assert L == 84915883381329
M = 14080*L

def mask(j):
    points = set()
    for r,e in menu:
        step = L*2**e//r
        assert L*2**e % r == 0 and M % (step*lcm(110,r)) == 0
        den_mod = r*pow(2,j-e,110)%110
        points.update(step*h for h in range(1,M//step)
                      if gcd(h,2*r) == 1 and cert(h,den_mod-h))
    return sorted(points)

def max_cyclic_gap(points):
    return max(points[0]+M-points[-1],
               max(v-u for u,v in zip(points,points[1:])))

def discrepancy(points):
    n = len(points)
    t = [i*M-n*y for i,y in enumerate(points)]
    return Fraction(max(t)-min(t)+M,M)

for j in range(14,34):
    points=mask(j)
    expected_gap=198212141579760 if j%2 == 0 else 189733121337760
    expected_disc=Fraction(8434,297) if j%2 == 0 else Fraction(359,11)
    assert (len(points),max_cyclic_gap(points),discrepancy(points)) == \
        (42880,expected_gap,expected_disc)
    print('period',j,'points',len(points),'gap/k',str(Fraction(expected_gap,L)),
          'discrepancy',str(expected_disc))
print('20/20 exhaustive exponent-period states PASS')

for j in range(8,16):
    k=2**j
    points={0,L*k}
    for r,e in menu:
        den=r*2**(j-e)
        step=L*2**e//r
        points.update(step*h for h in range(1,den)
                      if gcd(h,den)==1 and cert(h,den-h))
    ordered=sorted(points)
    gap=max(v-u for u,v in zip(ordered,ordered[1:]))
    assert Fraction(gap,L) <= Fraction(880,377)
    print('direct',j,'denominator_bound',k,'certificates',len(points)-2,
          'gap/k',str(Fraction(gap,L)))
assert Fraction(42880,14080)==Fraction(67,22)
assert Fraction(2*198212141579760,L)==Fraction(1760,377)
print('THEOREM VERIFIED: H>=256, |I|>1760/(377H) implies certified phase in I')
print('Local count coefficient 67k/22; discrepancy oscillation <= 359/11')
print('ALL PASS')
