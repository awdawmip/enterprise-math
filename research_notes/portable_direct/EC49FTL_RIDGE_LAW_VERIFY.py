#!/usr/bin/env python3
"""Exact independent Fraction certificate for EC49FTL ridge law.
Parent input is the EC49FTH/EC49FTK published affine theorem;
no native Bellman or profile reconstruction is performed.
"""
from fractions import Fraction as F
from math import comb

def P(*v): return tuple(F(t) for t in v)
def add(x,y):
    return tuple((x[i] if i<len(x) else F(0))+(y[i] if i<len(y) else F(0)) for i in range(max(len(x),len(y))))
def sub(x,y): return add(x,tuple(-u for u in y))
def mul(x,y):
    z=[F(0)]*(len(x)+len(y)-1)
    for i,u in enumerate(x):
        for j,v in enumerate(y): z[i+j]+=u*v
    return tuple(z)
def scal(x,c): return tuple(F(c)*v for v in x)
def power(x,k):
    r=P(1)
    for _ in range(k): r=mul(r,x)
    return r
def int_b(p,lo,hi):
    return sum((v*(hi**(i+1)-lo**(i+1))/F(i+1) for i,v in enumerate(p)),F(0))

A0,A1=F(3,4),F(49,64)
B0,B1=F(7,16),F(57,128)
Z1=F(3,4)
area=(A1-A0)*(B1-B0)
ac=P(F(77,105),F(6,105))
alo=P(A0)
a1=P(A1)

def moment(p,q,high,k):
    low=P(0)
    for j in range(k+1):
        coef=F(comb(k,j),j+1)*p**j
        da=sub(power(ac,j+1),power(alo,j+1))
        low=add(low,scal(mul(da,power(q,k-j)),coef))
    upper=mul(sub(a1,ac),power(high,k))
    return int_b(add(low,upper),B0,B1)/area

# z* is affine in a below a_c(b), and is 3/4 above.
ez=moment(F(105,96),P(F(-5,96),F(-6,96)),P(Z1),1)
ez2=moment(F(105,96),P(F(-5,96),F(-6,96)),P(Z1),2)
# M is affine below a_c and constant in a above.
em=moment(F(525,8),P(F(-9,8),F(-462,8)),P(47,-54),1)
em2=moment(F(525,8),P(F(-9,8),F(-462,8)),P(47,-54),2)
psat=int_b(sub(a1,ac),B0,B1)/area
# G evaluated at z=3/4, for lower and upper a cells.
etop=moment(F(105),P(-3-36*Z1,-60),P(2+60*Z1,-54),1)

assert psat==F(19,42)
assert ez==F(964373,1290240)
assert ez2-ez**2==F(654049,69363302400)
assert em==F(494813,21504)
assert em2-em**2==F(60097,1204224)
assert etop==F(154009,6720)
assert em-etop==F(3307,35840)

# Independently calculate first two moments of clipped X=35U-V
# from its triangle/plateau density and atom at x=56/3.
cap=F(56,3)
def xmoment(k):
    left=sum(F(1,35)*(0-(-1)**(deg+1))/F(deg+1) for deg in (k+1,k))
    plateau=cap**(k+1)/F(35*(k+1))
    return left+plateau+F(19,42)*cap**k
ex,ex2=xmoment(1),xmoment(2)
origin=F(569,768)
assert origin+ex/F(2048)==ez
assert (ex2-ex**2)/F(2048**2)==ez2-ez**2
volume_mid=F(3307,10569646080)
assert em-etop==36*volume_mid/area
assert em-F(1317531013,61931520)==F(107530427,61931520)

print("EC49FTL_EXACT_FRACTION_CERT_PASS")
for k,v in [("P_boundary",psat),("P_interior",1-psat),
("E_zstar",ez),("Var_zstar",ez2-ez**2),
("E_max_gap",em),("Var_max_gap",em2-em**2),
("E_fixed_z_top",etop),("E_max_gain_vs_z_top",em-etop)]:
    print(k,str(v))
print("CDF_x_lt0=(x+1)^2/70; CDF_0_to_cap=(x+1/2)/35; atom=19/42 at x=56/3")
