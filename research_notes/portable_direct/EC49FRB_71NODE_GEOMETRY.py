#!/usr/bin/env python3
"""Exact 71-node BRC class16943 continuum enclosure; Python standard library only.
Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Inherits 59 previously certified price nodes from PR #2595.
"""
from fractions import Fraction as F
from math import isqrt

baseline={F(1),F(13,12),F(7,6),F(5,4),F(4,3),F(17,12),F(3,2),
F(13,8),F(7,4),F(15,8),F(2),F(17,8),F(9,4),F(19,8),F(5,2),
F(31,12),F(8,3),F(11,4),F(17,6),F(23,8),F(3),F(47,16),F(39,16),
F(35,16),F(37,16),*(F(n,16) for n in (25,27,29,31,33)),
*(F(n,24) for n in (61,63,65,67)),F(11,8),F(35,24),F(25,24),
F(9,8),F(29,24),F(31,24),*(F(n,32) for n in (79,93,95)),
F(75,32),F(77,32),F(73,32),F(191,64)}
assert len(baseline)==47
previous=sorted(baseline|{F(n,32) for n in range(49,72,2)})
assert len(previous)==59
added=list(map(F,["137/48","45/16","133/48","131/48","43/16",
"127/48","125/48","41/16","121/48","71/48","23/16","67/48"]))
assert len(set(added))==12 and not set(added)&set(previous)
current=sorted(set(previous)|set(added))
assert len(current)==71 and current[0]==1 and current[-1]==3
K=lambda x:F(7557)-169*x
G=lambda x:F(310)*(3-x)/K(x)
seams=list(map(F,["2170/339583","310/37769","3410/340259",
"130/10987","310/22729","5270/341273","5890/341611",
"2170/113983","7130/342287","22630/350737","10/151","23870/351413"]))
assert all(G(x)==s for x,s in zip(added,seams))
def area(grid):
 return sum(((b-a)*(G(a)-G(b)) for a,b in zip(grid,grid[1:])),F(0))
old,new=area(previous),area(current)
assert old==F(469038291667513006195,157330981467832904648352)
assert new==F(23383237761405693658612415,9219123521070604713679482144)
assert 1-new/2==F(18414863804379803733700351873,18438247042141209427358964288)
D=F(2185500)
gain=F(0)
for z in added:
 a=max(v for v in previous if v<z);b=min(v for v in previous if v>z)
 term=D*(z-a)*(b-z)/K(z)*(1/K(a)+1/K(b))
 assert term>0
 gain+=term
assert old-new==gain==F(307332495155375,690889274591866119)
for a,b in zip(current,current[1:]):
 assert G(a)-G(b)==D*(b-a)/(K(a)*K(b))
scale=10**25
def root_interval(z):
 n=isqrt(z.numerator*scale*scale//z.denominator)
 lo,hi=F(n,scale),F(n+1,scale)
 assert lo*lo<=z<hi*hi
 return lo,hi
def regret_brackets(a,b):
 la,ha=root_interval(K(a))
 lb,hb=root_interval(K(b))
 return F(50)*(b-a)/(ha+hb)**2,F(50)*(b-a)/(la+lb)**2
vals=[(a,b,*regret_brackets(a,b)) for a,b in zip(current,current[1:])]
winner=max(vals,key=lambda row:row[2])
assert (winner[0],winner[1])==(F(4,3),F(11,8))
assert all(winner[2]>row[3] for row in vals if row is not winner)
assert winner[3]<F(71073007447662,10**18)
print("EC49FRB_71_NODE_GEOMETRY_EXACT_PASS")
print("prices",len(current),"intervals",len(vals))
print("area",new,"certified_fraction",1-new/2)
print("exact_gain",gain)
print("strict_regret_winner_interval",winner[:2])
print("regret_rational_interval",winner[2:])
