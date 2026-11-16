#!/usr/bin/env python3
"""EC49FRC 83-node rigorous geometric enclosure, stdlib-only."""
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal, localcontext

OLD = """1 25/24 13/12 9/8 7/6 29/24 5/4 31/24 4/3 11/8 67/48 17/12 23/16 35/24 71/48 3/2 49/32 25/16 51/32 13/8 53/32 27/16 55/32 7/4 57/32 29/16 59/32 15/8 61/32 31/16 63/32 2 65/32 33/16 67/32 17/8 69/32 35/16 71/32 9/4 73/32 37/16 75/32 19/8 77/32 39/16 79/32 5/2 121/48 61/24 41/16 31/12 125/48 21/8 127/48 8/3 43/16 65/24 131/48 11/4 133/48 67/24 45/16 17/6 137/48 23/8 93/32 47/16 95/32 191/64 3""".split()
NEW = """65/48 21/16 61/48 59/48 19/16 55/48 189/64 187/64 185/64 159/64 157/64 155/64""".split()
old = sorted(map(F, OLD))
new = sorted(set(old) | set(map(F, NEW)))
assert len(old) == 71 and len(new) == 83 and old[0] == 1 and old[-1] == 3
K = lambda x: F(7557) - 169*x
G = lambda x: 310*(3-x)/K(x)
D = F(2185500)
beta = F(620,3299)
assert all(K(z)>0 and 0<=G(z)<=beta for z in new)
S = lambda p: sum(((b-a)*(G(a)-G(b)) for a,b in zip(p,p[1:])),F(0))
S71 = S(old)
S83 = S(new)
assert S71 == F(23383237761405693658612415,9219123521070604713679482144)
assert S83 == F(44429865301826323916995,20209109482201273759125792)
assert S71-S83 == F(228289751810965197513275,675658930655790769941590568)
for z in map(F,NEW):
 a=max(t for t in old if t<z); b=min(t for t in old if t>z)
 gain=D*(z-a)*(b-z)/K(z)*(1/K(a)+1/K(b))
 assert gain == (b-a)*(G(a)-G(b))-(z-a)*(G(a)-G(z))-(b-z)*(G(z)-G(b))
scale=10**30
def root_bounds(q):
 v=isqrt(q.numerator*scale*scale//q.denominator)
 lo,hi=F(v,scale),F(v+1,scale)
 assert lo*lo<=q<hi*hi
 return lo,hi
def bounds(a,b):
 la,ua=root_bounds(K(a))
 lb,ub=root_bounds(K(b))
 return 50*(b-a)/(ua+ub)**2,50*(b-a)/(la+lb)**2
def leader(p):
 a=[(x,y,*bounds(x,y)) for x,y in zip(p,p[1:])]
 w=max(a,key=lambda r:r[2])
 assert all(w[2]>r[3] for r in a if r is not w)
 return w
w71=leader(old)
w83=leader(new)
assert (w71[0],w71[1])==(F(4,3),F(11,8))
assert (w83[0],w83[1])==(F(13,12),F(9,8))
with localcontext() as ctx:
 ctx.prec=60
 dec=lambda q:Decimal(q.numerator)/Decimal(q.denominator)
 regret=lambda a,b:50*dec(b-a)/(dec(K(a)).sqrt()+dec(K(b)).sqrt())**2
 print("nodes",len(new),"intervals",len(new)-1)
 print("prior area",S71)
 print("new area",S83)
 print("gain",S71-S83)
 print("certified fraction",1-S83/2)
 print("certified percentage",100*dec(1-S83/2))
 print("old maximum interval",w71[0],w71[1],regret(w71[0],w71[1]))
 print("new maximum interval",w83[0],w83[1],regret(w83[0],w83[1]))
 print("strict radical ordering and all rational identities PASS")
