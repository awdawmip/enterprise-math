#!/usr/bin/env python3
"""Exact regression checker for PCF1 information-leakage audit.

This script verifies the audit bundle's structural invariants and the three
load-bearing arithmetic facts used by the return:
1) Prime Fusion H=91 coordinate/pointed/idempotent/sixth-power regression.
2) Nontrivial idempotent -> coprime factor split (finite regression).
3) Exact support formula for public-seed polynomial gcd probes.
Finite tests support the written general proofs; they are not theorem proof.
"""
from __future__ import annotations
import argparse, json
from math import gcd
from pathlib import Path

DEFAULT_BUNDLE = Path("research_artifacts/PCF1_information_leakage_audit/audit_bundle.json")
DEFAULT_GATE = Path("research_artifacts/PCF1_information_leakage_audit/downstream_gate.json")

def primes_upto(n:int):
    out=[]
    for x in range(2,n+1):
        if all(x%d for d in range(2,int(x**0.5)+1)):
            out.append(x)
    return out

def roots_mod(poly,p):
    return [x for x in range(p) if poly(x)%p==0]

def nontrivial_gcd_count(poly,p,q):
    H=p*q
    return sum(1 for x in range(H) if 1 < gcd(H,poly(x)) < H)

def test_h91():
    a,b=2,3
    N=a*a+b*b
    C=a*a-a*b+b*b
    H=N*C
    assert (N,C,H)==(13,7,91)
    r=(-a*pow(b,-1,H))%H
    assert r==60
    assert gcd(H,r*r+1)==N
    assert gcd(H,r*r+r+1)==C
    e=(-(r+pow(r,-1,H)))%H
    assert (e*e-e)%H==0
    assert gcd(e,H)==N
    assert gcd(e-1,H)==C
    x6=pow(r,6,H)
    assert gcd(H,x6+1)==N
    assert gcd(H,x6-1)==C

def test_idempotent_split(limit=250):
    for H in range(2,limit+1):
        for e in range(H):
            if (e*e-e)%H:
                continue
            A=gcd(e,H)
            B=gcd(e-1,H)
            assert gcd(A,B)==1
            assert A*B==H

def test_probe_support():
    polys=[
        (2,lambda x:x*x+1),
        (2,lambda x:x*x+x+1),
        (6,lambda x:x**6-1),
        (6,lambda x:x**6+1),
    ]
    ps=[p for p in primes_upto(43) if p>3]
    for i,p in enumerate(ps):
        for q in ps[i+1:]:
            for degree,poly in polys:
                rp=len(roots_mod(poly,p))
                rq=len(roots_mod(poly,q))
                exact=rp*(q-rq)+rq*(p-rp)
                observed=nontrivial_gcd_count(poly,p,q)
                assert observed==exact, (p,q,degree,rp,rq,observed,exact)
                assert exact/(p*q) <= degree/p+degree/q + 1e-15

def test_bundle(bundle,gate):
    assert bundle["primary_verdict"]=="AUDIT_COMPLETE_WITH_ADMISSIBLE_SET"
    assert len(bundle["matrix"])==15
    ids={r["route_id"] for r in bundle["matrix"]}
    assert len(ids)==15
    for obs in bundle["ADMISSIBLE_N_BLIND_OBSERVABLES"]:
        assert "N-BLIND" in obs["classification"]
    assert bundle["cross_route_dependency_map"]["key_missing_interface"].startswith("N_ONLY_ASYMMETRY_GENERATOR")
    assert gate["program_level_missing_object"]=="N_ONLY_ASYMMETRY_GENERATOR"
    pf=gate["tasks"]["RS-PRIME-COORD-FACTOR-PRIME-FUSION-NBLIND-REALIZATION"]
    forbidden=" | ".join(pf["forbidden_as_algorithmic_input"])
    for token in ("p,q","pointed r","idempotent e","M_{p,q}"):
        assert token in forbidden

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bundle",type=Path,default=DEFAULT_BUNDLE)
    ap.add_argument("--gate",type=Path,default=DEFAULT_GATE)
    args=ap.parse_args()
    bundle=json.loads(args.bundle.read_text())
    gate=json.loads(args.gate.read_text())
    test_bundle(bundle,gate)
    test_h91()
    test_idempotent_split()
    test_probe_support()
    print("PCF1_AUDIT_CHECK_PASS routes=15 idempotent_H<=250 probe_primes<=43 H91=PASS")

if __name__=="__main__":
    main()
