#!/usr/bin/env python3
"""Exact rational audit of EC49FRP interval formulas. Run with Python stdlib."""
from fractions import Fraction as F
BETA=F(620,3299)
KAPPA=F(3299,43710)
D=(4,296,4,707)
E=(4,298,4,688)
def cost(v,x,l):
    ur,ut,mr,mt=v
    return (1-l)*F(ut+x*ur,141)+l*F(mt+x*mr,310)
def optimum(x,l):return min(cost(D,x,l),cost(E,x,l))
def deterministic(x,a,b):
    return KAPPA*min(BETA-a,b-BETA) if a<BETA<b else F(0)
def randomized(x,a,b):
    return KAPPA*(BETA-a)*(b-BETA)/(b-a) if a<BETA<b else F(0)
def brute_two(x,a,b):
    return min(max(cost(v,x,a)-optimum(x,a),cost(v,x,b)-optimum(x,b)) for v in (D,E))
assert F(19,3299)==(1-BETA)/141
assert F(2,3299)==BETA/310
assert cost(D,3,BETA)==cost(E,3,BETA)==F(7290,3299)
assert KAPPA==F(2,141)+F(19,310)
assert (7311-19*309)//2==720 and (7290-19*308)//2==719
xs=[F(3),F(13,4),F(4),F(20),F(100000)]
e=sorted(set([F(0),F(1),BETA,F(1,10),F(1,6),F(1,5),F(1,4),F(1,3),BETA-F(1,100),BETA+F(1,100),F(1,2)]))
checks=0
for x in xs:
    for a in e:
        for b in e:
            if not a<b:continue
            assert deterministic(x,a,b)==brute_two(x,a,b)
            r=randomized(x,a,b)
            assert F(0)<=r<=deterministic(x,a,b)
            if a<BETA<b:
                p=(BETA-a)/(b-a)
                assert p*cost(D,x,a)+(1-p)*cost(E,x,a)-optimum(x,a)==r
                assert p*cost(D,x,b)+(1-p)*cost(E,x,b)-optimum(x,b)==r
                assert r/deterministic(x,a,b)==max(BETA-a,b-BETA)/(b-a)
            else:assert r==0
            checks+=1
assert checks==275
a,b=BETA-F(1,100),BETA+F(1,100)
assert deterministic(F(3),a,b)==KAPPA/100
assert randomized(F(3),a,b)==KAPPA/200
print("PASS",checks,"exact rational (price, prior interval) checks")
