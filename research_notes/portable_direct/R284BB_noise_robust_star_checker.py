#!/usr/bin/env python3
"""R284BB: exact finite 3-Port noisy-star verification, stdlib only."""
from itertools import product
from random import Random
from math import factorial
import json

def coeff(C, X):
    a,b,c,d,e,f,g,h,i = C
    x0,x1,x2,z1,z2 = X
    A3 = x0*x1*x2
    A2 = -(a*x1*x2 + e*x0*x2 + i*x0*x1 + d*z1*x2 + g*z2*x1)
    A1 = (a*e*x2 + a*i*x1 + e*i*x0 - b*d*x2 - c*g*x1 - f*h*x0
          + (d*i-f*g)*z1 + (e*g-d*h)*z2)
    A0 = -a*e*i + a*f*h + b*d*i - b*f*g - c*d*h + c*e*g
    return A3,A2,A1,A0

def determinant_readout(C, X, t=1):
    a,b,c,d,e,f,g,h,i = C
    x0,x1,x2,z1,z2 = (t*q for q in X)
    M = [[x0-a,-b-z1,-c-z2],[-d,x1-e,-f],[-g,-h,x2-i]]
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
          - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
          + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def polynomial_readout(C, X, t=1):
    a3,a2,a1,a0 = coeff(C,X)
    return ((a3*t + a2)*t + a1)*t + a0

def gap(values):
    v=sorted(values)
    assert len(set(v)) == len(v)
    return min(b-a for a,b in zip(v,v[1:]))

def main():
    Cs=list(product((1,2),repeat=9))
    X=tuple(Random(28417).randint(1,10000) for _ in range(5)) # overridden below: use one RNG sequence
    rng=Random(28417)
    X=tuple(rng.randint(1,10000) for _ in range(5))
    assert X==(7340,6572,5070,7899,352)
    checks=0
    for C in Cs:
        for t in (0,1,2,7,30):
            assert polynomial_readout(C,X,t)==determinant_readout(C,X,t)
            checks += 1
    t=100
    Y=[polynomial_readout(C,X,t) for C in Cs]
    random_gap=gap(Y)
    assert random_gap==14595
    assert random_gap>2*7000
    assert max(t*v for v in X)==789900
    H,n,delta=2,3,7000
    L=factorial(n)*2**n*H**n
    B=max(4*L+4,4*delta+4)
    assert B==28004
    D=(B**1,B**2,B**4,B**8,B**16)
    Y2=[polynomial_readout(C,D) for C in Cs]
    deterministic_gap=gap(Y2)
    assert deterministic_gap==784224015
    assert deterministic_gap>2*delta
    result={
        "status":"PASS","n":n,"H":H,"matrices":len(Cs),
        "determinant_identity_exact_checks":checks,
        "random_seed":28417,"example_ray":list(X),"example_scale":t,
        "example_output_count":len(set(Y)),
        "example_min_pair_gap":random_gap,
        "example_max_control":max(t*v for v in X),
        "demonstrated_adversarial_error":delta,
        "deterministic_base":B,"deterministic_output_count":len(set(Y2)),
        "deterministic_min_pair_gap":deterministic_gap,
        "deterministic_max_control_bits":max(D).bit_length(),
        "deterministic_max_output_bits":max(abs(y) for y in Y2).bit_length(),
        "review_status":"NOT_REVIEWED"
    }
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=="__main__":
    main()
