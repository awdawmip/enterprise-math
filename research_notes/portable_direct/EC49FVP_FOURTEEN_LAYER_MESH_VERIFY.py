#!/usr/bin/env python3
"""EC49FVP; exact 11-adic Bernoulli phase certificate mesh; Python stdlib."""
from fractions import Fraction
from math import gcd, lcm

P = 11
M = 1281280
U = Fraction(4822040484, 8132285009)
G = Fraction(141024, 1653649)
mod = lambda q: q.numerator * pow(q.denominator, -1, P) % P
u, g, i637 = mod(U), mod(G), pow(637, -1, P)
rows = []
for z in range(P):
    la, lb = (637 - 3*z)*i637 % P, u*(1 + g*z) % P
    a, b = (1 - (1-z)*la) % P, (1 - (1-z)*lb) % P
    rows.append((z, a, b, la, lb))
assert [r for r in rows if r[3] == r[4]] == [(3,10,10,10,10)]
c, d = -3*i637 % P, u*g % P

def exact(h, n):
    for z,a,b,la,lb in rows:
        if z == 3:
            q = pow(la,n-1,P)*pow(a,h-1,P)*(n*a-h*(1-z)*la) % P
        else:
            q = (pow(a,h,P)*pow(la,n,P)-pow(b,h,P)*pow(lb,n,P))*pow((la-lb)%P,-1,P)%P
        if q == 0:
            return False
    return (pow(c,h+n,P)-pow(d,h+n,P))*pow((c-d)%P,-1,P)%P != 0

patterns = set()
for h in range(1,11):
    for n in range(1,11):
        if all((pow(a,h,P)*pow(la,n,P)-pow(b,h,P)*pow(lb,n,P))*pow((la-lb)%P,-1,P)%P != 0
               for z,a,b,la,lb in rows if z != 3) and (pow(c,h+n,P)-pow(d,h+n,P))*pow((c-d)%P,-1,P)%P != 0:
            patterns.add((h%10,n%10))
assert len(patterns) == 44
cert = lambda h,n: (h%10,n%10) in patterns and (9*h+10*n)%11 != 0
assert all(cert(h,n)==exact(h,n) for h in range(1,111) for n in range(1,111))
print('12100/12100 projective predicate comparisons PASS')

base = [(1,0),(7,3),(13,4),(1,1),(1,2),(1,3),(1,4),(7,4)]
extra14 = [(13,5),(7,5),(1,5),(7,6),(7,7),(91,7)]
spec14 = base + extra14
extra18 = [(13,5),(7,5),(1,5),(1,6),(7,6),(13,6),(1,7),(7,7),(13,7),(91,7)]
spec18 = base + extra18
assert len(spec14)==14 and len(spec18)==18

def layer(j, spec):
    r,e=spec
    step=91*2**e//r
    assert 91*2**e % r == 0 and M % (step*lcm(110,r)) == 0 and j>e
    den=r*pow(2,j-e,110)%110
    return {step*h for h in range(1,M//step) if gcd(h,2*r)==1 and cert(h,den-h)}

def gap(y):
    v=sorted(y)
    return max(max(b-a for a,b in zip(v,v[1:])),v[0]+M-v[-1])

def discrepancy(y):
    v=sorted(y); n=len(v)
    t=[i*M-n*x for i,x in enumerate(v)]
    return Fraction(max(t)-min(t)+M,M)

for j in range(14,34):
    layers = [layer(j,s) for s in spec18]
    a=set().union(*(layers[spec18.index(s)] for s in spec14))
    b=set().union(*layers)
    assert (len(a),gap(a),discrepancy(a)) == (13080,390 if j%2==0 else 440,
          Fraction(1734,143) if j%2==0 else Fraction(463,44))
    assert (len(b),gap(b),discrepancy(b)) == (13860,390 if j%2==0 else 440,
          Fraction(21,2) if j%2==0 else Fraction(41,4))
print('20/20 complete periods: 14 layers 13080 points; 18 layers 13860 points PASS')
print('periodic max gap even=390 odd=440; 14 osc even=1734/143 odd=463/44')
print('18 osc even=21/2 odd=41/4; intensity=63k/64')

for j in range(8,16):
    k=2**j
    points={0,91*k}
    for r,e in spec14:
        den=r*2**(j-e)
        step=91*2**e//r
        points.update(step*h for h in range(1,den) if gcd(h,den)==1 and cert(h,den-h))
    sorted_p=sorted(points)
    exact_gap=max(y-x for x,y in zip(sorted_p,sorted_p[1:]))
    expected={8:350,9:364,10:390,11:440,12:390,13:440,14:390,15:440}[j]
    assert exact_gap == expected
    assert exact_gap <= (390 if j%2 == 0 else 440)
    print('direct',j,'k',k,'count',len(points)-2,'gap',exact_gap)
print('14-layer gap theorem |I| > 880/(91H) for H>=256 PASS')
assert Fraction(13860*91,M)==Fraction(63,64)
assert Fraction(13080*91,M)==Fraction(327,352)
leave_one_out=[]
for cut in range(14):
    selected=[s for i,s in enumerate(spec14) if i!=cut]
    worst=max(gap(set().union(*(layer(j,s) for s in selected))) for j in range(14,34))
    leave_one_out.append(worst)
assert leave_one_out == [640,560,520,520,455,520,520,637,455,448,455,455,455,455]
print('14-layer leave-one-out worst gaps:', leave_one_out)
print('ALL PASS')
