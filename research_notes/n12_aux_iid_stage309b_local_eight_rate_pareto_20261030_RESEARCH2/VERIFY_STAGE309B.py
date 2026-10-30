#!/usr/bin/env python3
"""Independent direct 128-atom S,J,W,Y,X^3 enumeration (exact rational)."""
from fractions import Fraction as F
from itertools import product

def model_mass(s,j,w,y):
    p=F(1,4) if s==0 else F(3,4)
    return F(1,2)*(F(7,8) if j==s else F(1,8))*(F(3,4) if w==s else F(1,4))*(p if y else 1-p)

def score(u):
    original={}; reduced={}; joint=F(0)
    for s,j,w,y in product((0,1),repeat=4):
        a=model_mass(s,j,w,y)
        p=F(1,4) if s==0 else F(3,4)
        q0=model_mass(0,j,w,y);q1=model_mass(1,j,w,y)
        t=F(1,4) if q0>q1 else F(3,4)
        if (j,w,y)==(1,0,0):t+=u
        for xyz in product((0,1),repeat=3):
            k=sum(xyz)
            o=a*p**k*(1-p)**(3-k)
            r=a*t**k*(1-t)**(3-k)
            key=(w,y)+xyz
            original[key]=original.get(key,F(0))+o
            reduced[key]=reduced.get(key,F(0))+r
            joint+=abs(o-r)/2
    pub=sum((abs(original[k]-reduced[k]) for k in original),F(0))/2
    assert sum(original.values(),F(0))==sum(reduced.values(),F(0))==1
    return pub,joint

if __name__=='__main__':
    assert score(F(0))==(F(11,256),F(77,1024))
    for u in (F(1,2000),F(1,1000),F(1,900)):
        q=F(9,128)*u+F(3,32)*u*u-F(1,8)*u**3
        g=F(117,4096)*u-F(123,1024)*u*u+F(23,256)*u**3
        assert score(u)==(F(11,256)-q,F(77,1024)+g)
    print('INDEPENDENT_128_ATOM_SOURCE_PUBLIC_JOINT_EXACT_PASS')
