#!/usr/bin/env python3
"""C301 author replay: exact denominator coefficient content and strip height.
Requires C300 frozen companion files from the supplied C301 portable archive.
Uses only Python stdlib. No Source/admission/native-BRC claims.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd
import json
import C298_SHARED_DENOMINATOR_EXACT as base
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as source

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b):
            if y: c[i+j]+=x*y
    return c

def ceil_strict_log2(r):
    assert r>0
    h=max(0,r.numerator.bit_length()-r.denominator.bit_length()+1)
    while r>=F(1<<h):h+=1
    while h>0 and r<F(1<<(h-1)):h-=1
    assert r<F(1<<h)
    return h

def check():
    paths,_=c288.build_paths()
    ref=json.loads(Path("C293_125_REFINED_BRACKETS.json").read_text())
    prev=json.loads(Path("C300_AUTHOR_AUDIT_20261025.json").read_text())["path_rows"]
    expected=json.loads(Path("C301_125_COMPACT_HEIGHT_CERT.json").read_text())["rows"]
    W,_=source.floor_fixed_masses()
    assert len(paths)==len(ref["records"])==len(prev)==len(expected)==125
    for i,(path,rec,old,witness) in enumerate(zip(paths,ref["records"],prev,expected)):
        assert rec[0]==witness[0]==i
        lo=F(rec[1],1<<24)
        hi=F(rec[1]+1,1<<24)
        v0=[w+lo*d for w,d in zip(path["w"],path["d"])]
        v1=[w+hi*d for w,d in zip(path["w"],path["d"])]
        assert source.valid(v0) and source.valid(v1)
        # Original factor/signed-orientation normalization belongs to C298.
        terms=base.make_terms(path,lo,hi,W)
        s,groups=base.certificate_one(i,path,int(rec[1]),W)[1]
        occur=defaultdict(set)
        for j,(_,factors) in enumerate(terms):
            for _,den in factors:
                _,q=base.primitive_factor(den)
                occur[q].add(j)
        # C299/C300 already proved EXACT cancellation of these two pairs;
        # identifying them by branch membership does not re-prove residue zero.
        cancelled={q for q in groups if len(q)==2
                   and occur[q] in ({75,77},{76,78})}
        assert len(cancelled)==2
        nonlinear=set()
        for w,d in zip(path["w"],path["d"]):
            if not d: continue
            x2=base.poly_mul([w,d],[w,d])
            a=base.poly_add([F(2)],[-x for x in x2])
            b=base.poly_add([F(3)],[-x for x in x2])
            q=base.poly_mul(a,b)
            q3=base.poly_mul(base.poly_mul(q,q),q)
            _,primitive=base.primitive_factor(
                base.normalize_pair([F(1)],q3)[1])
            assert primitive in groups
            nonlinear.add(primitive)
            assert 0<w+lo*d<1 and 0<w+hi*d<1
        coeff=[1]
        U=F(s)
        for q,e in sorted(groups.items()):
            if q in cancelled:continue
            assert len(q)<=2 or q in nonlinear
            assert base.poly_eval(q,lo)>0 and base.poly_eval(q,hi)>0
            U*=max(base.poly_eval(q,lo),base.poly_eval(q,hi))**e
            for _ in range(e):coeff=multiply(coeff,q)
        content=0
        for a in coeff: content=gcd(content,abs(a))
        assert content==1
        assert len(coeff)-1==old["reduced_degree"]
        hc=(s*sum(abs(x) for x in coeff)).bit_length()
        hs=ceil_strict_log2(U)
        assert hc<=old["reduced_denominator_l1_height_bound_bits"]
        assert hs<=hc
        assert witness==[i,hc,hs,s.bit_length()],(i,witness,hc,hs)
    print("C301_REFERENCE_REPLAY_125_EXACT_PASS")
if __name__=="__main__":check()
