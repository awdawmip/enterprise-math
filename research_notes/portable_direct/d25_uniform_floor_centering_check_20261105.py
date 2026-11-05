#!/usr/bin/env python3
"""Uniform floor-centering checker for ORIGINAL 216/2304 half-endpoint jets.
Requires the published adjacent d25_matched_half_jet_transport_checker_20261105.py.
Neither program executes the native original-class H0/B0 experiment.
"""
import argparse
import json
from d25_matched_half_jet_transport_checker_20261105 import jets, half, prime, tuples

def uniform(p):
    h=(p-1)//2
    a=[(-h,1,2),(-(p//3),1,3),(-((2*p)//3),2,3)]
    b=[(-h,1,2),(-(p//4),1,4),(-((3*p)//4),3,4)]
    # Return parameter equality as exact numerator at denominator 12.
    assert sorted((m*cd+cn*p)*12//cd for m,cn,cd in a)==[4,6,8]
    assert sorted((m*cd+cn*p)*12//cd for m,cn,cd in b)==[3,6,9]
    return a,b

def check(p):
    assert p>3 and prime(p)
    a,b=uniform(p)
    A=jets(p,a,2,6)
    B=jets(p,b,9,8)
    wa,wb=half(p)
    mod=p**3
    assert (A[0]+p*A[1]+p*p*A[2])%mod==wa
    assert (B[0]+p*B[1]+p*p*B[2])%mod==wb
    if p%24 in (13,19):
        prev_a,prev_b=tuples(p)
        assert A==jets(p,prev_a,2,6)
        assert B==jets(p,prev_b,9,8)
    return p%24 in (13,19)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bound",type=int,default=4999)
    bound=ap.parse_args().bound
    results=[check(p) for p in range(5,bound+1) if prime(p)]
    print(json.dumps({
        "schema":"D25_FLOOR_CENTERING_CHECK_V1",
        "bound":bound,
        "primes_checked":len(results),
        "target_classes_checked":sum(results),
        "failures":0,
        "all_prime_half_jets":"EXACT_RECONSTRUCTION_VERIFIED",
        "native_H0B0":"NOT_EXECUTED"},indent=2))
if __name__=="__main__":main()
