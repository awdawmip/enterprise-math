#!/usr/bin/env python3
"""C296 certified positive dyadic interval evaluator (stdlib-only).

Every returned integer interval [lo,hi] encloses 2**bits * (F(v)/Q).
It evaluates the frozen 79-branch *auxiliary positive rational model*;
no floating-point decisions and no native signed/phase BRC claim.
"""
from fractions import Fraction as F
from math import prod
import C275_STANDALONE_EXACT_REPLAY as s

def iprod(values):
    return prod(values, start=F(1))

def mul_positive(lo, hi, r, metrics=None):
    assert lo >= 0 and lo <= hi and r > 0
    n,d=r.numerator,r.denominator
    if metrics is not None:
        metrics["mul_count"]+=1
        metrics["max_factor_bits"]=max(metrics["max_factor_bits"],n.bit_length(),d.bit_length())
        metrics["max_temporary_product_bits"]=max(metrics["max_temporary_product_bits"],(lo*n).bit_length(),(hi*n+d-1).bit_length())
    res=(lo*n)//d, (hi*n+d-1)//d
    if metrics is not None:
        metrics["max_state_bits"]=max(metrics["max_state_bits"],res[0].bit_length(),res[1].bit_length())
    return res

def start_positive(r, bits, metrics=None):
    assert r>0
    z=r.numerator << bits
    d=r.denominator
    if metrics is not None:
        metrics["start_count"]+=1
        metrics["max_factor_bits"]=max(metrics["max_factor_bits"],r.numerator.bit_length(),d.bit_length())
        metrics["max_temporary_product_bits"]=max(metrics["max_temporary_product_bits"],z.bit_length(),(z+d-1).bit_length())
    result=z//d, (z+d-1)//d
    if metrics is not None:
        metrics["max_state_bits"]=max(metrics["max_state_bits"],result[0].bit_length(),result[1].bit_length())
    return result

class PositiveDyadicEvaluator:
    def __init__(self, W):
        # All frozen nodes/j labels are preserved. Every simplification is a
        # rational identity, not an aggregation of branch/provenance states.
        self.fixed=[]
        a=iprod(s.Z-s.U[k] for k in s.I)
        for j in s.J:
            coefficient=F(W[j],s.Q)*iprod(abs(s.U[j]-s.U[k]) for k in s.I)/a
            self.fixed.append((j, s.U[j], coefficient))
        self.moving_static=[(j,s.Z-s.U[j]) for j in s.J]

    def enclose(self, v, bits, metrics=None):
        assert isinstance(bits,int) and bits>=0 and s.valid(v)
        # Avoid cancellation: each individual rational summand is > 0.
        differences=[s.Z-x for x in v]
        lo_total=hi_total=0
        for j,node,coefficient in self.fixed:
            lo,hi=start_positive(coefficient,bits,metrics)
            for i in range(4):
                lo,hi=mul_positive(lo,hi,differences[i]/abs(node-v[i]),metrics)
            lo_total+=lo
            hi_total+=hi
        for k,p in enumerate(v):
            base=(s.A/s.H)/(((2-p*p)*(3-p*p))**3)
            lo,hi=start_positive(base,bits,metrics)
            for j,weight in self.moving_static:
                lo,hi=mul_positive(lo,hi,weight/abs(p-s.U[j]),metrics)
            for m,x in enumerate(v):
                if m!=k:
                    lo,hi=mul_positive(lo,hi,differences[m]/abs(p-x),metrics)
            lo_total+=lo
            hi_total+=hi
        return lo_total,hi_total

    def certified_sign(self,v,bits_schedule=(192,256,320,384,448,512,640,768)):
        for bits in bits_schedule:
            lo,hi=self.enclose(v,bits)
            one=1<<bits
            if hi<one:
                return -1,bits,(lo,hi)
            if lo>one:
                return 1,bits,(lo,hi)
        return 0,bits,(lo,hi)
