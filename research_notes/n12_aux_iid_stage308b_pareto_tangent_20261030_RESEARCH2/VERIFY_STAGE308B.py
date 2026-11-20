#!/usr/bin/env python3
"""Independent three-bit word enumeration with generated, not copied, source branches."""
from fractions import Fraction as F
from itertools import product

one=F(1)
p=lambda s:F(1,4) if s==0 else F(3,4)

def bern(x,v): return x if v==1 else one-x

def weights(s,j,w,y):
    # Reconstruct conditional J,W,Y independently from the frozen source model.
    return (F(1,2)*(F(7,8) if j==s else F(1,8))
            *(F(3,4) if w==s else F(1,4))*bern(p(s),y))

def scores(u,v):
    def rate(j,w,y):
        if (j,w,y)==(1,0,0):return F(1,4)+u
        if (j,w,y)==(0,1,1):return F(3,4)-v
        masses=[weights(s,j,w,y) for s in (0,1)]
        return p(0) if masses[0]>masses[1] else p(1)
    P=T=F(0)
    for w,y in product(range(2),repeat=2):
        for xs in product(range(2),repeat=3):
            ideal=sim=F(0)
            for s,j in product(range(2),repeat=2):
                q=weights(s,j,w,y)
                ideal+=q*F(p(s)**sum(xs)*(1-p(s))**(3-sum(xs)))
                sim+=q*F(rate(j,w,y)**sum(xs)*(1-rate(j,w,y))**(3-sum(xs)))
                T+=abs(q*ideal_ratio(s,xs)-q*sim_ratio(rate(j,w,y),xs))/2
            P+=abs(ideal-sim)/2
    return P,T

def ideal_ratio(s,xs):
    return p(s)**sum(xs)*(1-p(s))**(3-sum(xs))

def sim_ratio(t,xs):
    return t**sum(xs)*(1-t)**(3-sum(xs))

if __name__=='__main__':
    assert sum((weights(s,j,w,y) for s,j,w,y in product(range(2),repeat=4)),F(0))==1
    assert scores(F(0),F(0))==(F(11,256),F(77,1024))
    split=scores(F(1,100),F(1,100))
    concentration=scores(F(1,50),F(0))
    assert split==(F(5193,125000),F(9695073,128000000))
    assert concentration==(F(20763,500000),F(9692067,128000000))
    assert split[0]-concentration[0]==F(9,500000)
    assert split[1]-concentration[1]==F(1503,64000000)
    print('INDEPENDENT_BRC_SOURCE_GENERATION_AND_THREE_BIT_WORDS_PASS')
    print('CHECKED_PUBLIC',split[0],concentration[0])
    print('CHECKED_JOINT',split[1],concentration[1])
