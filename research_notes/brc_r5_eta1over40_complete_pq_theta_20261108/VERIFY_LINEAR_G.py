#!/usr/bin/env python3
"""Exact constructive G-face 10-edge Blackwell map: integer Fraction checks."""
from fractions import Fraction as F
from itertools import product
from VERIFY import mass, time, lawful, check, source, ZERO

def bounds(eta,u,w,z):
    return (0<=eta<=F(85544,451695) and
      0<=u<=min(F(13,40)+eta/80,(F(556036)-F(401539)*eta)/1710880) and
      0<=w<=min(F(3,40)+F(21,80)*eta,(F(128316)-F(650499)*eta)/1710880) and
      0<=z<=min(F(1,10),(F(85544)-F(451695)*eta)/855440))

def build(eta,u,w,z):
    assert bounds(eta,u,w,z)
    x=(F(1),F(1),eta,u,F(9,40)*eta+z,w,z)
    gp=F(1)-F(4469,21386)*eta
    up=u+F(3357,20128)*eta
    wp=w+F(124737,342176)*eta
    zp=z+F(433819,855440)*eta
    y=(gp,gp,F(0),up,zp,wp,zp)
    c=F(140975,1026528)*eta
    d=F(16917,42772)*eta
    m=mass(x)
    Q=[[ZERO]*7 for i in range(7)]
    Q[0][0]=m[0];Q[0][1]=c
    Q[1][1]=m[1]-F(9,5)*c
    Q[3][1]=F(4,5)*c;Q[3][3]=m[3]
    Q[4][4]=m[4];Q[4][5]=d
    Q[5][5]=m[5]-F(13,8)*d
    Q[6][5]=F(5,8)*d;Q[6][6]=m[6]
    return (x,y,tuple(map(tuple,Q)))

def main():
    n=0
    for eta in map(F,('0','1/40','29/900','1/30','31/900','1/10','1/8')):
        uc=min(F(13,40)+eta/80,(F(556036)-F(401539)*eta)/1710880)
        wc=min(F(3,40)+F(21,80)*eta,(F(128316)-F(650499)*eta)/1710880)
        zc=min(F(1,10),(F(85544)-F(451695)*eta)/855440)
        for pp,qq,tt in product(map(F,('0','1/3','2/3','1')),repeat=3):
            check(build(eta,uc*pp,wc*qq,zc*tt),'G')
            n+=1
    print('PARAMETER_EXACT_GRID_PASS',n)
    for eta,theta,p,q in product((F(29,900),F(31,900)),
                                  (F(19,40),F(21,40)),
                                  (F(19,40),F(21,40)),
                                  (F(19,40),F(21,40))):
        x=source(theta,p,q,eta)
        check(build(eta,x[3],x[5],x[6]),'G')
    print('OPEN_MIDDLE_RATIO_BOX_CORNERS_PASS',16)
    x=source(F(1,2),F(1,2),F(1,2),F(1,30))
    check(build(x[2],x[3],x[5],x[6]),'G')
    print('MIDDLE_EXACT_SOURCE_TWO_FACE_POINT_PASS')
    print('PASS_R5_EXPLICIT_10_EDGE_AFFINE_G_FACE_REAL_FAMILY')

if __name__=='__main__':main()
