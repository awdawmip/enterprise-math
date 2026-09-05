#!/usr/bin/env python3
from collections import Counter
from itertools import product
from fractions import Fraction

from signed_brc import (
    endpoint_multiplicity, endpoint_weight, primitive_straight, return_multiplicity,
    shortest_event_count, shortest_path_multiplicity, spatial_norm_squared,
)

STEPS=[]
for i in range(6):
    p=[0]*6; p[i]=1; STEPS.append(tuple(p))
    m=[0]*6; m[i]=-1; STEPS.append(tuple(m))


def add(a,b): return tuple(x+y for x,y in zip(a,b))


def main():
    checks=0
    # Dynamic enumeration through length 6 against exact all-length formula.
    dist=Counter({(0,0,0,0,0,0):1})
    for length in range(0,7):
        assert sum(dist.values())==12**length; checks+=1
        for z,count in dist.items():
            assert count==endpoint_multiplicity(length,z); checks+=1
        if length<6:
            nxt=Counter()
            for z,count in dist.items():
                for step in STEPS: nxt[add(z,step)]+=count
            dist=nxt

    assert return_multiplicity(0)==1
    assert return_multiplicity(1)==0
    assert return_multiplicity(2)==12
    assert return_multiplicity(3)==0
    assert return_multiplicity(4)==396
    checks+=5

    # Shortest event/multipath and P000 primitive-line criterion.
    for z in product(range(-2,3),repeat=6):
        if z==(0,0,0,0,0,0): continue
        m=shortest_event_count(z)
        mult=shortest_path_multiplicity(z)
        assert endpoint_multiplicity(m,z)==mult
        assert m*m>=spatial_norm_squared(z)
        assert primitive_straight(z)==(sum(x!=0 for x in z)==1)
        if primitive_straight(z):
            assert mult==1 and m*m==spatial_norm_squared(z)
        else:
            assert mult>1 and m*m>spatial_norm_squared(z)
        checks+=5

    # Equal weights reduce weighted mass to ordinary multiplicity.
    wp=(1,1,1,1,1,1); wm=(1,1,1,1,1,1)
    probes=((0,0,0,0,0,0),(1,-1,0,0,0,0),(2,0,-1,0,0,0))
    for z in probes:
        base=shortest_event_count(z)
        for length in range(base,base+5):
            assert endpoint_weight(length,z,wp,wm)==Fraction(endpoint_multiplicity(length,z))
            checks+=1

    print("PASS_X6_SIGNED_BRC_V17")
    print("checks=",checks)
    print("return_2=12; return_4=396")
    print("primitive_straight <=> one-axis support <=> shortest_event_count=spatial_norm")

if __name__=="__main__": main()
