#!/usr/bin/env python3
"""C296 independent full-rational 79-branch crosscheck for 256bit roots (stdlib).
All 250 signs and all 250 positive outward enclosures; author-level only.
"""
from fractions import Fraction as F
import C275_STANDALONE_EXACT_REPLAY as s
import C288_ISOLATING_BOXES_EXACT as c288
from C296_DYADIC_INTERVAL_SIGNS import PositiveDyadicEvaluator
from C296_VERIFY_128_256_OUTWARD import decode_certificates

def independent_full_F(v, W):
    z=F(0)
    for j in s.J:
        node=s.U[j]
        term=F(W[j])
        for i in range(4):
            p=v[i]
            term=(term*(s.Z-p)*abs(node-s.U[s.I[i]]))/(
                (s.Z-s.U[s.I[i]])*abs(node-p))
        z+=term
    for k,p in enumerate(v):
        term=F(s.Q)*s.A/s.H/((2-p*p)*(3-p*p))**3
        for j in s.J:
            term=term*(s.Z-s.U[j])/abs(p-s.U[j])
        for m,x in enumerate(v):
            if m!=k:
                term=term*(s.Z-x)/abs(p-x)
        z+=term
    return z

def verify():
    _,k256=decode_certificates()
    paths,_=c288.build_paths()
    assert len(paths)==len(k256)==125
    W,_=s.floor_fixed_masses()
    evaluator=PositiveDyadicEvaluator(W)
    maxbits=0
    for i,(p,k) in enumerate(zip(paths,k256)):
        for side in (0,1):
            t=F(k+side,1<<256)
            v=tuple(w+t*d for w,d in zip(p['w'],p['d']))
            assert s.valid(v)
            full=independent_full_F(v,W)/s.Q
            lo,hi=evaluator.enclose(v,448)
            assert lo<=full*(1<<448)<=hi,(i,side,'containment')
            assert (full<1 if side==0 else full>1),(i,side,'exact sign')
            maxbits=max(maxbits,full.numerator.bit_length(),full.denominator.bit_length())
    assert maxbits==100989,maxbits
    print('C296_INDEPENDENT_EXACT_FRACTIONS_256_PASS; 250/250 signs and interval inclusions; max numerator/denominator bits=100989',flush=True)

if __name__=='__main__':verify()
