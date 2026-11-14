#!/usr/bin/env python3
"""Exact rational checks for the R749SOU first-onset positive-gap collars.

Dependency: frozen 16-atom Walsh observer and R749SOS/SOT exact line theorem;
this checker verifies new constants, symmetry and representative fiber transports.
The all-real continuum assertion follows from the written analytic inequalities.
"""
from fractions import Fraction as F
import json

HALF=F(1,2)
T0=F(5,22)
T1=F(1,4)
M=(3,12,15,1,2,4,8)
W=[tuple(1 if (k&m).bit_count()%2==0 else -1 for m in M) for k in range(16)]

def law(t,s,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+t*a+s*b+h*c+u*d+v*e+w*f+z*g)/16 for a,b,c,d,e,f,g in W)

def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def G(t):
    return (22*t-5)/48

def ref(t,s):
    return law(t,s,min(t,s))

def rotate(k):
    return ((k&3)<<2)|((k&12)>>2)

def transport(p,t,s0,s1):
    d=abs(s1-s0)
    alpha=d/(1-max(t,s0))
    assert alpha<=1
    r=ref(t,s0)
    ans=tuple((1-alpha)*p[k]+alpha*r[k]+(s1-s0)*W[k][1]/16 for k in range(16))
    assert min(ans)>=0 and sum(ans)==1
    assert tv(p,ans)<=alpha+d/2
    return ans

def lower_witnesses(t):
    p=law(t,HALF,0,t,t,HALF,1-t)
    n=law(t,HALF,0,-t,-t,-HALF,t-1)
    a=law(t,HALF,t-HALF,0,0,-HALF-t,-HALF-t)
    b=law(t,HALF,t+HALF,0,0,t-HALF,t-HALF)
    for law_i in (p,n,a,b):
        assert min(law_i)>=0 and sum(law_i)==1
    assert tv(p,n)==(7-2*t)/8
    return p,n,a,b

def main():
    assert T1-T0==F(1,44)
    assert G(T0)==0 and G(T1)==F(1,96)
    assert G(T1)/8==F(1,768)
    assert G(T1)/(T1-T0)==F(11,24)
    assert G(T1)/(8*(T1-T0))==F(11,192)
    assert (T1-T0)*G(T1)/8==F(1,33792)
    assert 2*(T1-T0)*G(T1)/8==F(1,16896)
    c=1-F(3,1)/(4-G(T1))-F(3,16)
    assert c==F(371,6128) and c>0
    assert 1-F(15,2)*F(1,8)==F(1,16)
    assert HALF-G(T1)/8>T1

    sample_count=0
    for t in (T0,F(23,100),F(6,25),T1):
        p,n,a,b=lower_witnesses(t)
        d=G(t)/8
        for original in (p,n,a,b,ref(t,HALF)):
            for sign in (-1,1):
                new_s=HALF+sign*d
                v=transport(original,t,HALF,new_s)
                vv=transport(v,t,new_s,HALF)
                assert min(vv)>=0 and sum(vv)==1
                assert sum((x*W[k][0] for k,x in enumerate(v)),F(0))==t
                assert sum((x*W[k][1] for k,x in enumerate(v)),F(0))==new_s
                assert sum((x*W[k][0] for k,x in enumerate(vv)),F(0))==t
                assert sum((x*W[k][1] for k,x in enumerate(vv)),F(0))==HALF
                sample_count+=1
        for law_i in (p,n,a,b,ref(t,HALF)):
            push=tuple(law_i[rotate(k)] for k in range(16))
            assert sum(push)==1
            assert sum((x*W[k][0] for k,x in enumerate(push)),F(0))==HALF
            assert sum((x*W[k][1] for k,x in enumerate(push)),F(0))==t
            assert min(push)>=0
    x=(F(1,5),F(1,2),F(1,10),F(1,100),F(-1,100),F(1,50),F(-1,50))
    p=law(*x)
    q=law(x[1],x[0],x[2],x[5],x[6],x[3],x[4])
    assert tuple(p[rotate(k)] for k in range(16))==q
    assert min(p)>=0 and min(q)>=0
    return {
        'status':'PASS', 'research_id':'R749SOU',
        'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'range':'5/22<t<=1/4, |s-1/2|<=(22*t-5)/384',
        'gap_lower':'(371/6128)*(22*t-5)/48',
        'lower_side_improvement':'1/16 times G(t)',
        'swapped_region':'5/22<s<=1/4, |t-1/2|<=(22*s-5)/384',
        'per_wedge_area':'1/33792', 'union_area':'1/16896',
        'max_halfwidth':'1/768', 'tangent_slope':'11/192',
        'tested_exact_bidirectional_transport_instances':sample_count,
        'all_real_parameter_proof':'analytic Hausdorff transport + Lipschitz radii + pinned exact line theorem',
        'scientific_status':'AUTHOR_ANALYTIC_NOT_REVIEWED',
        'native_X6_correspondence':'OPEN'
    }

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
