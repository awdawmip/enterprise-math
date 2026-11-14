#!/usr/bin/env python3
"""R749SOF exact complete transverse Walsh phases, reusing R749SOE's verified Bareiss engine."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, lcm
import json
import R749SOE_TRANSVERSE_WALSH_EXACT_CHECK as brc
S=brc.SIGNS
A=(1,2,4,7,8,11,13,14)
G1=(0,1,2,3,4,8,12)
G2=(0,1,2,3,4,5,6,8,9,10,12)
GM=(0,1,2,4,5,6,8,9,10,12)

def lower():
    for x in (F(0),F(1,2)):
        t=F(1,2)+x;s=F(1,2)
        ma=brc.law(t,s,1-x,-x,-x,0,0)
        mg=brc.law(t,s,x,-s,-s,x-s,x-s)
        plus=brc.law(t,s,x,s,s,1-t,1-t)
        minus=brc.law(t,s,x,-s,-s,t-1,t-1)
        assert all(min(mu)>=0 and sum(mu)==1 for mu in (ma,mg,plus,minus))
        assert brc.tv(plus,minus)==(2-t)/2
        for a,b,c in ((F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)),(t,s,F(0))):
            q=brc.center(a,b,c)
            event=lambda indices,mu:sum((q[i]-mu[i] for i in indices),F(0))
            la=event(A,ma);gi=event(G1,mg);gii=event(G2,mg);gm=event(GM,mg)
            assert la==(1-x-c)/2
            assert gi==(3*a+3*b-c)/16-x/2+F(3,16)
            assert gii==(-a-b+3*c)/16-x/2+F(7,16)
            assert gm==(-a-b+c)/8-x/4+F(1,2)
            assert (la+gi+3*gii)/5==F(2,5)-x/2
            if a==t and b==s:
                assert (3*la+8*gii)/11==F(9,22)-6*x/11
                assert (la+4*gm)/5==F(2,5)-2*x/5
    return 'PASS'

def check(name,lo,hi,center,radius):
    d=lcm(2,lo.denominator,hi.denominator)
    brc.ROWS=[tuple(row[i] for i in (0,2,3,4,5,6)) for row in S]+[(1,0,0,0,0,0),(-1,0,0,0,0,0)]
    brc.RHS=[-d-(d//2)*row[1] for row in S]+[int(d*lo),-int(d*hi)]
    seen=set();nonsingular=feasible=0
    for active in combinations(range(18),6):
        z=brc.solve(active)
        if z is None:continue
        nonsingular+=1
        if all(sum((a*b for a,b in zip(row,z)),F(0))>=v for row,v in zip(brc.ROWS,brc.RHS)):
            feasible+=1;seen.add(z)
    assert seen
    tight=0;max_excess=F(-2)
    for z in seen:
        t,h,u,v,w,zz=(a/d for a in z)
        mu=brc.law(t,F(1,2),h,u,v,w,zz);q=center(t)
        assert min(mu)>=0 and min(q)>=0 and sum(mu)==sum(q)==1
        excess=brc.tv(mu,q)-radius(t)
        max_excess=max(max_excess,excess)
        tight+=int(excess==0)
    assert max_excess==0,(name,max_excess)
    return dict(name=name,parameter_interval=[str(lo),str(hi)],active_sets=comb(18,6),nonsingular=nonsingular,feasible_bases=feasible,distinct_vertices=len(seen),tight=tight,max_excess=str(max_excess),violations=0)

def main():
    assert lower()=='PASS'
    tests=[
      ('FREE_I',F(1,2),F(3,5),lambda t:brc.center(F(1),F(1,5),F(1,5)),lambda t:F(13,20)-t/2),
      ('FREE_II',F(3,5),F(1),lambda t:brc.center(F(1),(1-t)/2,(1-t)/2),lambda t:(2-t)/4),
      ('CAL_I',F(1,2),F(9,16),lambda t:brc.center(t,F(1,2),(F(2)+t-F(1,2))/11),lambda t:F(9,22)-6*(t-F(1,2))/11),
      ('CAL_II',F(9,16),F(2,3),lambda t:brc.center(t,F(1,2),F(3,10)-t/5),lambda t:F(3,5)-2*t/5),
      ('CAL_III',F(2,3),F(1),lambda t:brc.center(t,F(1,2),t-F(1,2)),lambda t:(2-t)/4),
    ]
    return {'result':'PASS','unit':'R749SOF','scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'scope':'all real t in [1/2,1] with s=1/2; auxiliary Walsh source fiber; NOT_REVIEWED',
            'free':'13/20-t/2 on [1/2,3/5]; (2-t)/4 on [3/5,1]',
            'calibrated':'9/22-6(t-1/2)/11 on [1/2,9/16]; 3/5-2t/5 on [9/16,2/3]; (2-t)/4 on [2/3,1]',
            'gap':'strictly positive on [1/2,2/3); exactly zero on [2/3,1]',
            'lower_event_and_diameter_certificates':'PASS',
            'exact_joint_polytope_upper':[check(*a) for a in tests]}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
