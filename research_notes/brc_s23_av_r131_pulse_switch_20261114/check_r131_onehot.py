#!/usr/bin/env python3
"""Exact one-hot window for nonzero d=1 in the S23 auxiliary model."""
from fractions import Fraction
import random
import json

def frac(z):
    return z - z.numerator // z.denominator

def word(theta, B, m):
    assert 0<theta<1 and B>=m+2
    return tuple(int(frac((B+i)*theta)<theta) for i in range(m))

def onehot_witness(B, i):
    return (Fraction(1,B+i)+Fraction(1,B+i-1))/2

def zero_witness(B,m):
    return Fraction(1,2*(B+m-1))

def test():
    cases=0;sample_count=0;cert_count=0
    for m in range(1,19):
        for B in range(m+2,m+43):
            pts=sorted({Fraction(1,B+i) for i in range(m)} | {Fraction(1,B-1)})
            assert len(pts)==m+1
            # All cuts and open cells of the window; left edge included; right excluded.
            queries=pts[:-1]+[(pts[i]+pts[i+1])/2 for i in range(m)]
            assert len(queries)==2*m
            for t in queries:
                w=word(t,B,m)
                assert sum(w)==1, (B,m,t,w)
                expected=tuple(int(Fraction(1,B+i)<=t<Fraction(1,B+i-1)) for i in range(m))
                assert w==expected,(B,m,t,w,expected)
                sample_count+=1
            for i in range(m):
                t=onehot_witness(B,i)
                assert word(t,B,m)==tuple(int(j==i) for j in range(m))
                cert_count+=1
            t=zero_witness(B,m)
            assert word(t,B,m)==(0,)*m
            cert_count+=1
            cases+=1
    B=10**120+39; m=64
    for i in (0,1,31,63):
        assert word(onehot_witness(B,i),B,m)==tuple(int(j==i) for j in range(m))
    assert word(zero_witness(B,m),B,m)==(0,)*m
    rng=random.Random(1315)
    rand=0
    for _ in range(5000):
        m=rng.randrange(1,64);B=m+2+rng.randrange(0,1_000_000)
        i=rng.randrange(m)
        t=onehot_witness(B,i)
        assert word(t,B,m)==tuple(int(j==i) for j in range(m))
        rand+=1
    return {'result':'R131_NONZERO_D_ONEHOT_PASS','B_cases':cases,'window_cut_cell_checks':sample_count,
            'certificate_checks':cert_count,'large_B_certificate_digits':len(str(10**120+39)),
            'random_cases':rand,'assumptions':'B>=m+2; m>=1; x=0, A=B, d=E=1; theta in (0,1)'}

if __name__=='__main__':
    print(json.dumps(test(),ensure_ascii=False,indent=2))
