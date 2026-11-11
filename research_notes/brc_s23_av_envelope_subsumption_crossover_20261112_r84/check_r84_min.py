#!/usr/bin/env python3
"""R84 independent rational certificate / time-support quotient verification.
Auxiliary circle-source model, not a native BRC dynamical result.
"""
from fractions import Fraction as F
from math import floor, ceil
from random import Random
import json, pathlib

def frac(z): return z-floor(z)

def excluded(times,r,q,L,U,j=0,x=F(0),a=4,b=8):
    assert times and all(t%q==r for t in times)
    ka=floor(a*L);kb=floor(b*L)
    assert ka==floor(a*U) and kb==floor(b*U)
    assert all(a*z-ka<b*z-kb for z in (L,U))
    theta0=F(1,q)
    assert L<=theta0<=U
    beta=frac(F(r,q)+x-j*theta0)
    lo,hi=min(times),max(times)
    products=[(t-j)*(z-theta0) for t in (lo,hi) for z in (L,U)]
    sm,sp=beta+min(products),beta+max(products)
    qlo=min(a*L-ka,a*U-ka);qhi=max(b*L-kb,b*U-kb)
    return ceil(sm-qhi)>floor(sp-qlo)

def member(t,theta,j=0,x=F(0),a=4,b=8):
    A=frac(a*theta);B=frac(b*theta)
    z=frac(x+(t-j)*theta)
    return (A<=z<B) if A<B else (z>=A or z<B) if A>B else False

def latest(E,theta):
    return max((t for t,branch in E if member(t,theta)),default=None)

def run():
    q=16;anchor=F(1,q);L=anchor-F(1,100000);U=anchor+F(1,100000)
    base={(16,0),(80,0),(12,0),(76,0)}
    for r,ts in ((0,[16,80]),(12,[12,76])):
        assert excluded(ts,r,q,L,U)
        assert excluded(ts+[(ts[0]+ts[1])//2],r,q,L,U)
        assert excluded([ts[0]],r,q,L,U)
    e1=base|{(48,1),(44,1)}
    e2=e1|{(48,2)}
    for n in range(201):
        z=L+(U-L)*F(n,200)
        assert latest(base,z)==latest(e1,z)==latest(e2,z)==None
    new=e1|{(5,9)}
    for n in range(201):
        z=L+(U-L)*F(n,200)
        assert latest(new,z)==5
    A=F(1,4);B=F(31,120)
    assert excluded([0],0,4,A,B,j=0,x=F(0),a=1,b=2)
    assert member(40,B,j=0,x=F(0),a=1,b=2)
    assert not excluded([0,40],0,4,A,B,j=0,x=F(0),a=1,b=2)
    assert latest({(5,1)},anchor)==latest({(5,2)},anchor)==5
    assert {(5,1)}!={(5,2)}
    rng=Random(8420261112);successful=0;checks=0
    for trial in range(500):
        r=rng.choice((0,12));k=rng.randrange(-12,12);gap=rng.randrange(2,10)
        ts=[r+16*k,r+16*(k+gap)]
        mid=r+16*(k+rng.randrange(1,gap))
        assert min(ts)<mid<max(ts)
        if not excluded(ts,r,q,L,U):continue
        assert excluded(ts+[mid],r,q,L,U)
        assert excluded([ts[0]],r,q,L,U)
        assert excluded([ts[1]],r,q,L,U)
        for i in range(8):
            z=L+(U-L)*F(rng.randrange(1001),1000)
            assert all(not member(t,z) for t in ts+[mid])
            checks+=3
        successful+=1
    assert successful>100
    out={'schema':'EM_R84_EXACT_CERTIFICATE_TEST_V1','trials':500,
         'successfully_certified_random_envelopes':successful,
         'random_pointwise_checks':checks,'directed_pointwise_checks':603,
         'counterexample':{'old_source_time':0,'inserted_source_time':40,
           'anchor':[1,4],'interval_right':[31,120],'new_membership_at_right':True},
         'status':'ALL_ASSERTIONS_PASS',
         'scope':'R71 interval-exclusion envelopes; time-only latest readout; same observer, original labels, anchor; rational stable noncrossing interval'}
    p=pathlib.Path(__file__).with_name('verification_r84_min.json')
    p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print('R84_MIN_PASS',successful,checks)
if __name__=='__main__':run()
