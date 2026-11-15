#!/usr/bin/env python3
"""Exact rational five-phase certificate for frozen N=4 S23 K17, 1/2 <= s <= 3/5.
Reuses immutable earlier rigorous interval primitives, located at sibling research note.
"""
from fractions import Fraction as Q
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path

EARLIER='brc_n4_s23_k17_phase_s25_to_s12_20261105_research1'
source=Path(__file__).resolve().parents[1]/EARLIER/'VERIFY.py'
spec=spec_from_file_location('s23_cert_prior',source)
p=module_from_spec(spec)
spec.loader.exec_module(p)

BREAKS=[Q(1,2),Q(6,11),Q(5,9),Q(4,7),Q(7,12),Q(3,5)]
EXPECTED=[[(0,17),(10,2),(11,0)],[(0,17),(11,1)],
          [(0,17),(9,4),(11,1)],[(0,17),(7,7),(11,1)],[(0,17),(12,0)]]
CASES=[(10,2),(11,1),(9,4),(7,7),(12,0)]

def feasible(s):
    return [(m,17-2*m+(m*s).__floor__()) for m in range(13)
            if 17-2*m+(m*s).__floor__()>=0]

def hull(points):
    out=[]
    for x,y in points:
        while len(out)>1:
            (u,v),(w,z)=out[-2:]
            if (w-u)*(y-z)-(z-v)*(x-w)>=0:out.pop()
            else:break
        out.append((x,y))
    return out

def main():
    breaks=sorted({Q(k,m) for m in range(1,13) for k in range(m+1)
                   if Q(1,2)<=Q(k,m)<=Q(3,5)})
    assert breaks==BREAKS,(breaks,BREAKS)
    for l,r,expected in zip(BREAKS,BREAKS[1:],EXPECTED):
        actual=hull(feasible((l+r)/2))
        assert actual==expected,(l,r,actual)
        print('HULL',l,r,actual)
    boundary=hull(feasible(Q(3,5)))
    assert boundary==[(0,17),(10,3),(12,0)],boundary
    print('BOUNDARY HULL',Q(3,5),boundary)
    for (l,r),(m,n) in zip(zip(BREAKS,BREAKS[1:]),CASES):
        p.candidate_monotone(m,n,l,r,parts=12)
        p.winning_at_left(m,n,l)
        p.losing_at_right(m,n,l+Q(1,1000))
    p.linear_increasing(17,11,Q(1,2),Q(6,11),parts=2)
    p.linear_increasing(16,11,Q(5,9),Q(4,7),parts=2)
    p.linear_increasing(16,11,Q(4,7),Q(7,12),parts=2)
    t,h,b=p.info(Q(3,5))
    p.positive('S_3_5_10T3B_BEATS_17B',p.sub(p.add(p.mul(10,t),p.mul(3,h)),p.mul(17,b)))
    p.positive('S_3_5_10T3B_BEATS_12T',p.sub(p.mul(3,h),p.mul(2,t)))
    assert p.COUNT==84,p.COUNT
    print('ASSERTIONS',p.COUNT)
    print('PASS_BRC_S23_K17_PHASE_HALF_TO_THREE_FIFTHS_20261105')
if __name__=='__main__':main()
