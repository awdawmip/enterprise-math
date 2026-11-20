#!/usr/bin/env python3
"""R51 exact arithmetic audit of R50; conditional positive-weight BRC root masses."""
from fractions import Fraction as F
from itertools import product
import json


def mass(p, s, r):
    return (p*s, (p-1)*s, 2*(p*p-1)*r, 2*p*r)


def c(q):
    return q*q-q-1


def coefficients(q):
    x = -F(c(q)*(q-1),q)
    y = F(c(q))
    d = F(1)
    h = -F(1) - F(c(q),q)
    return (x,y,d,h)


def contrast(q,z):
    return sum((a*b for a,b in zip(coefficients(q),z)), F(0))


def norm(q):
    return sum(abs(x) for x in coefficients(q))


def radius(p,s,r):
    if p == 1:
        return r/2
    return min(s/F(8*(p+1)), F(c(p))*r/2)


def audit():
    tests = 0
    for q in range(1,31):
        expected = F(2) if q==1 else F(2*q*(q-1))
        assert norm(q)==expected
        assert sum(coefficients(q))==0
        for signs in product((-1,1),repeat=4):
            noise=tuple(F(t) for t in signs)
            assert abs(contrast(q,noise)) <= norm(q)
            tests+=1
        best=tuple(F(1 if x>0 else -1 if x<0 else 0) for x in coefficients(q))
        assert abs(contrast(q,best))==norm(q)
        assert contrast(q,mass(q,F(2),F(1)))==0

    real=mass(4,F(1),F(99,10000))
    rival=mass(5,F(161,200),F(1,100))
    assert F(1)**2 > 4*F(99,10000)
    assert F(161,200)**2 > 4*F(1,100)
    residual=tuple(a-b for a,b in zip(real,rival))
    rival_bias=(max(residual)+min(residual))/2
    observation=tuple((a+b+rival_bias)/2 for a,b in zip(real,rival))
    eta=(max(residual)-min(residual))/4
    assert eta==F(249,5000) < F(1,20)
    assert all(abs(z-a)<=eta for z,a in zip(observation,real))
    assert all(abs(z-b-rival_bias)<=eta for z,b in zip(observation,rival))

    cases=0
    for p,(alpha,beta) in product(range(1,10), ((F(1),F(1)),(F(1),F(2)),(F(1,2),F(3,2)),(F(99,100),F(1,100)))):
        s=alpha+beta
        r=alpha*beta
        z0=mass(p,s,r)
        eta0=radius(p,s,r)/3
        assert eta0>0
        for q in range(1,41):
            if q==p:
                continue
            if p==1 or q==1:
                e0=z0[2]-z0[3]
                assert (e0 < -2*eta0 if p==1 else e0>2*eta0)
            else:
                assert abs(contrast(q,z0)) > 2*eta0*norm(q)
            cases+=1
    return {
        'status':'PASS', 'scope':'exact rational checks + general symbolic proof in R51 paper',
        'q_checked':'1..30', 'signed_noise_vertex_checks':tests,
        'correct_norm':'q=1:2; q>=2:2*q*(q-1)',
        'old_r50_radius_counterexample':{
            'p':4,'S':'1','P':'99/10000','q':5,'S_q':'161/200','P_q':'1/100',
            'rival_bias':str(rival_bias),'observed':list(map(str,observation)),
            'eta':str(eta),'r50_claimed_threshold':'1/20',
            'true_exact':list(map(str,real)), 'rival_unbiased_exact':list(map(str,rival))},
        'corrected_radius_contrast_checks':cases,
        'scientific_status':'AUTHOR_PROOF_AND_EXACT_CHECK_NOT_INDEPENDENTLY_REVIEWED',
        'native_triads':'NOT_MAPPED_TO_NATIVE_P000'
    }

if __name__=='__main__':
    print(json.dumps(audit(), ensure_ascii=False, indent=2, sort_keys=True))
