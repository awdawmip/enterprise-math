#!/usr/bin/env python3
"""Independent, self-contained exact geometry check for EC49FRE.
No non-native scientific BRC operation: this checks only auxiliary x-grid bounds.
The native 12-seam physical BRC Bellman certificates are in the companion archive.
Requires CPython standard library, and no external data files.
"""
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal, localcontext

P86 = """1 49/48 25/24 17/16 13/12 53/48 9/8 55/48 7/6 19/16 29/24 59/48 5/4 61/48 31/24 21/16 4/3 65/48 11/8 67/48 17/12 23/16 35/24 71/48 3/2 49/32 25/16 51/32 13/8 53/32 27/16 55/32 7/4 57/32 29/16 59/32 15/8 61/32 31/16 63/32 2 65/32 33/16 67/32 17/8 69/32 35/16 71/32 9/4 73/32 37/16 75/32 19/8 77/32 155/64 39/16 157/64 79/32 159/64 5/2 121/48 61/24 41/16 31/12 125/48 21/8 127/48 8/3 43/16 65/24 131/48 11/4 133/48 67/24 45/16 17/6 137/48 23/8 185/64 93/32 187/64 47/16 189/64 95/32 191/64 3"""
ADD = """153/64 151/64 149/64 147/64 145/64 143/64 141/64 139/64 137/64 135/64 133/64 131/64"""
old = sorted(set(map(F,P86.split())))
new = sorted(set(old) | set(map(F,ADD.split())))
assert len(old)==86 and len(new)==98 and len(set(map(F,ADD.split())))==12
assert new[0]==1 and new[-1]==3

def K(x):
    return F(7557)-169*x

def G(x):
    return 310*(3-x)/K(x)

def area(nodes):
    return sum(((b-a)*(G(a)-G(b)) for a,b in zip(nodes,nodes[1:])),F(0))

def area_alternate(nodes):
    return F(2185500,169**2)*sum(
        (K(a)/K(b)+K(b)/K(a)-2 for a,b in zip(nodes,nodes[1:])),F(0))

S86,S98 = area(old),area(new)
assert S86==area_alternate(old)==F(10770320075410254305,5143575841741225186848)
assert S98==area_alternate(new)==F(296902200973874060795,160864097511408031554912)
assert S86-S98==F(423000,1703822659)
assert 1-S98/2==F(321431292821842189049029,321728195022816063109824)

SCALE=10**40
def sqrt_interval(a):
    assert a>0
    k=isqrt(a.numerator*SCALE*SCALE//a.denominator)
    lo,hi=F(k,SCALE),F(k+1,SCALE)
    assert lo*lo<=a<hi*hi
    return lo,hi

def regret_interval(a,b):
    al,au=sqrt_interval(K(a))
    bl,bu=sqrt_interval(K(b))
    return F(50)*(b-a)/(au+bu)**2,F(50)*(b-a)/(al+bl)**2

old_candidates=[(a,b,*regret_interval(a,b)) for a,b in zip(old,old[1:])]
new_candidates=[(a,b,*regret_interval(a,b)) for a,b in zip(new,new[1:])]
oldbest=max(old_candidates,key=lambda r:r[2])
newbest=max(new_candidates,key=lambda r:r[2])
assert tuple(oldbest[:2])==(F(19,8),F(77,32))
assert tuple(newbest[:2])==(F(2),F(65,32))
assert all(newbest[2]>z[3] for z in new_candidates if z is not newbest)
assert all(oldbest[2]>z[3] for z in old_candidates if z is not oldbest)
assert newbest[3]<oldbest[2]

# Exact check of the first split and a precise decimal readout only.
assert F(153,64) in new and F(153,64) not in old
with localcontext() as ctx:
    ctx.prec=65
    d=lambda v:Decimal(v.numerator)/Decimal(v.denominator)
    a,b=F(19,8),F(77,32)
    xstar=(Decimal(7557)-(d(K(a))*d(K(b))).sqrt())/Decimal(169)
    regret=lambda a,b:Decimal(50)*d(b-a)/(d(K(a)).sqrt()+d(K(b)).sqrt())**2
    print("EC49FRE EXACT VERIFIED: 86 -> 98 nodes, 97 intervals")
    print("S98 =",S98)
    print("S86-S98 =",S86-S98)
    print("Certified fraction =",1-S98/2)
    print("Certified percent =",d(100*(1-S98/2)))
    print("Old worst interval =",tuple(oldbest[:2]),"R/t =",regret(*oldbest[:2]))
    print("New worst interval =",tuple(newbest[:2]),"R/t =",regret(*newbest[:2]))
    print("New strict rational root enclosure =",str(newbest[2]),str(newbest[3]))
    print("Near-optimal first rational cut 153/64; |x*-153/64| =",abs(xstar-d(F(153,64))))
    print("NO physical BRC time/phase evolution was simulated")
