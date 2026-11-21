#!/usr/bin/env python3
"""EC49FVN: exact 11-adic three-denominator periodic mesh certificate.
Parent EC49FVM@e101e5110c533803bbb1fd91b070f6419303f5ff
Frozen BRC16943 observation, NOT an X6-native experiment.
"""
from fractions import Fraction
from math import gcd, lcm

p = 11
U = Fraction(4822040484, 8132285009)
gamma = Fraction(141024, 1653649)
def mod(q):
    return q.numerator * pow(q.denominator, -1, p) % p
u, g = mod(U), mod(gamma)
inv637 = pow(637, -1, p)
rows = []
for z in range(p):
    la = (637 - 3*z) * inv637 % p
    lb = u * (1 + g*z) % p
    a = (1 - (1-z)*la) % p
    b = (1 - (1-z)*lb) % p
    rows.append((z, a, b, la, lb))
assert [row for row in rows if row[3] == row[4]] == [(3,10,10,10,10)]
c, d = (-3*inv637)%p, u*g%p

def projective_no_root(h,n):
    assert h>0 and n>0
    for z,a,b,la,lb in rows:
        if z==3:
            v=(pow(la,n-1,p)*pow(a,h-1,p)*(n*a-h*(1-z)*la))%p
        else:
            v=((pow(a,h,p)*pow(la,n,p)-pow(b,h,p)*pow(lb,n,p))
               *pow((la-lb)%p,-1,p))%p
        if v==0:
            return False
    return ((pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p))%p!=0

patterns={(h,n) for h in range(10) for n in range(10)
          if all((pow(a,h or 10,p)*pow(la,n or 10,p)
                  -pow(b,h or 10,p)*pow(lb,n or 10,p))
                 *pow((la-lb)%p,-1,p)%p!=0
                 for z,a,b,la,lb in rows if z!=3)
          and (pow(c,(h or 10)+(n or 10),p)
               -pow(d,(h or 10)+(n or 10),p))*pow((c-d)%p,-1,p)%p!=0}
assert len(patterns)==44

def valid(h,n):
    return (h%10,n%10) in patterns and (9*h+10*n)%11!=0

# Independently compare the compact residue predicate to full projective evaluation.
for h in range(1,111):
    for n in range(1,111):
        assert valid(h,n)==projective_no_root(h,n)

# Use y=91*k*phase. For denominators k, 7*k/8, 13*k/16,
# the integer y coordinates are 91*h,104*h,112*h, respectively.
# Their mask periods jointly divide 160160 in y.
Q, L = 91, 160160
assert lcm(110*91, 104*lcm(110,7),112*lcm(110,13)) == L

def periodic_points(j):
    kmod=pow(2,j,110)
    k7mod=7*pow(2,j-3,110)%110
    k13mod=13*pow(2,j-4,110)%110
    y=set()
    y.update(91*h for h in range(1,L//91) if gcd(h,2)==1 and valid(h,kmod-h))
    y.update(104*h for h in range(1,L//104) if gcd(h,14)==1 and valid(h,k7mod-h))
    y.update(112*h for h in range(1,L//112) if gcd(h,26)==1 and valid(h,k13mod-h))
    return sorted(y)

def direct(j):
    k=2**j
    y={0,91*k}
    for r,e,scale in [(1,0,91),(7,3,104),(13,4,112)]:
        den=r*(k//2**e)
        y.update(scale*h for h in range(1,den) if gcd(h,den)==1 and valid(h,den-h))
    y=sorted(y)
    return max(b-a for a,b in zip(y,y[1:])), len(y)-2

maxgap=0
maxdisc=Fraction(0)
for j in range(11,31):
    Y=periodic_points(j)
    assert len(Y)==800
    gaps=[b-a for a,b in zip(Y,Y[1:])]+[Y[0]+L-Y[-1]]
    gap=max(gaps)
    rho=Fraction(800,L)
    deviations=[Fraction(0)]
    for i,y in enumerate(Y):
        deviations.extend([i-rho*y,i+1-rho*y])
    deviations.append(Fraction(0))
    osc=max(deviations)-min(deviations)
    assert gap==(696 if j%2 else 793)
    assert osc==Fraction(812 if j%2 else 976,143)
    maxgap=max(maxgap,gap)
    maxdisc=max(maxdisc,osc)
    print('period',j,'points',len(Y),'max_y_gap',gap,'discrepancy_oscillation',osc)
assert maxgap==793 and maxdisc==Fraction(976,143)
for j in range(7,14):
    gap,n=direct(j)
    assert gap<=793
    assert gap=={7:546,8:712,9:696,10:793,11:696,12:793,13:696}[j]
    print('direct',j,'k',2**j,'count',n,'max_y_gap',gap)
print('ALL PASS: exact mask, 20-state periodic certificate, 793/(91*k) mesh, 5*k/11 density, 976/143 discrepancy.')
