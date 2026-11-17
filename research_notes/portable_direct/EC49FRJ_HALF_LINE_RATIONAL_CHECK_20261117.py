#!/usr/bin/env python3
"""EC49FRJ exact rational half-line proof obligation checker.

Full original unrestricted Bellman and independent integer DP certificates
are separate archived evidence; this file verifies recorded exact identities
and the finite high-price root-mass exclusion, without third-party libraries.
"""
from fractions import Fraction as F

A=(6,290,6,751); B=(5,293,5,704); C=(5,295,5,685)
D=(4,296,4,707); E=(4,298,4,688)
beta=F(620,3299)
def score(z,x,l):
    ur,ut,mr,mt=z
    return (1-l)*F(ur*x+ut,141)+l*F(mr*x+mt,310)

anchors=[
 (3,0,F(308,141)),(3,beta,F(7290,3299)),(3,1,F(70,31)),
 (20,0,F(8,3)),(20,beta,F(8718,3299)),(20,1,F(384,155)),
 (100000,0,F(400296,141)),(100000,1,F(400688,310))]
for x,l,v in anchors:
    assert min(score(D,x,l),score(E,x,l))==v
    assert score(E,x,l)-score(D,x,l)==(620-3299*l)/43710
assert 0<beta<1
X=100000
assert 3*X+141*(141-1)<4*X+296
assert 3*X+310*(141-1)<4*X+688
assert D[0]==D[2]==E[0]==E[2]==4
for l in [F(0),beta/2,beta,F(1,2),F(1)]:
    assert min(score(z,3,l) for z in (A,B,C))==min(score(z,3,l) for z in (D,E))
for x in [F(3),F(20),F(100000),F(10**20)]:
    for l in [F(0),beta/2,beta,(beta+1)/2,F(1)]:
        assert score(E,x,l)-score(D,x,l)==(620-3299*l)/43710
        assert (score(D,x,l)<=score(E,x,l))==(l<=beta)
print("EC49FRJ 8 rational anchors and high-price root-slope arithmetic PASS")
