"""Exact BRC N4/S23 global gate attenuation probe certificate (author-side)."""
from fractions import Fraction as F
from itertools import product
from random import Random
import json

A=(0,0,0,1,1,1)
B=(2,2,3,2,2,4)
C=(5,6,7,8,9,10)
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))

def raw(a,b,c):
    return (a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c))

def probe(z,lam):
    u=[lam*z[j] if j<5 else z[j] for j in range(11)]
    r=[raw(u[A[j]],u[B[j]],u[C[j]]) for j in range(6)]
    return tuple(tuple(sum((F(M[i][j],20)*r[j][k] for j in range(6)),F(0))
                 for k in range(4)) for i in range(6))

def unmix(p):
    def combine(x,i,y,j,den=1):
        return tuple((x*p[i][k]+y*p[j][k])/den for k in range(4))
    return (combine(11,0,-10,1),combine(-9,0,10,1),p[2],
            combine(9,3,-5,4,4),combine(-1,3,5,4,4),p[5])

def invert(p,lam):
    r=unmix(p)
    z=[None]*11
    for source in range(6):
        a,b,c,d=r[source]
        assert a+b+c+d==1 and a<1 and a+b<1
        for index,value in ((A[source],a/lam),
                            (B[source],b/((1-a)*lam)),
                            (C[source],c/(1-a-b))):
            assert F(0)<=value<=1
            if z[index] is not None: assert z[index]==value
            z[index]=value
    assert all(v is not None for v in z)
    return tuple(z)

def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2

def distance(p,q):
    return max(tv(a,b) for a,b in zip(p,q))

def verify():
    lam=F(1,2)
    corners=list(product((F(0),F(1)),repeat=11))
    p_corners=[]
    for z in corners:
        p=probe(z,lam)
        for row in p:
            assert sum(row)==1 and all(F(0)<=x<=1 for x in row)
        assert invert(p,lam)==z
        p_corners.append(p)
    rng=Random(202611030602)
    rationals=[F(0),F(1),F(1,7),F(1,3),F(1,2),F(2,3),F(6,7)]
    sample=[tuple(rng.choice(rationals) for j in range(11)) for i in range(160)]
    for z in sample:
        assert invert(probe(z,lam),lam)==z
    checked=0
    for i in range(480):
        if i<240:
            q1=rng.randrange(len(corners));q2=rng.randrange(len(corners))
            z,w=corners[q1],corners[q2];p,q=p_corners[q1],p_corners[q2]
        else:
            z,w=rng.choice(sample),rng.choice(sample)
            p,q=probe(z,lam),probe(w,lam)
        eps=max(abs(a-b) for a,b in zip(z,w))
        d=distance(p,q)
        assert eps/F(84)<=d<=2*eps
        checked+=1
    # Endpoints cannot be injective on all 11 coordinates.
    u=(F(1),F(1),F(0),F(0),F(0),*(F(0) for _ in range(6)))
    v=(F(1),F(1),F(1),F(0),F(0),*(F(0) for _ in range(6)))
    assert u!=v and probe(u,F(1))==probe(v,F(1))
    w=(F(0),)*11
    x=(F(1),)+(F(0),)*10
    assert x!=w and probe(x,F(0))==probe(w,F(0))
    for lam in (F(1,7),F(1,3),F(2,3),F(6,7)):
        for i in range(80):
            z=rng.choice(sample)
            assert invert(probe(z,lam),lam)==z
    return {
        'marker':'PASS_BRC_S23_GLOBAL_GATE_ATTENUATION_INJECTIVITY_20261103',
        'frozen_scientific_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'observer':'six labeled source-mixed four-outcome distributions; no port collapse',
        'operator':'A_lambda z: multiply z[0:5] by lambda; preserve z[5:11]',
        'lambda_one_half': '1/2',
        'global_bound_lambda_one_half':'(1/84)*||z-w||inf <= d <= 2*||z-w||inf',
        'all_binary_corners_exact_reconstruction':len(corners),
        'rational_interior_points_reconstructed':len(sample),
        'additional_lambdas_reconstructed':4,
        'additional_lambda_tests':320,
        'rational_pair_bound_tests':checked,
        'both_endpoint_noninjectivity_witnesses':2,
        'arithmetic':'Python stdlib Fraction exact rational',
        'scope':'Finite execution checks; all-real cube injectivity and bounds follow from symbolic proof in PROOF.md',
        'formal_review':'NOT_PERFORMED; NOT_ADMITTED'
    }

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
