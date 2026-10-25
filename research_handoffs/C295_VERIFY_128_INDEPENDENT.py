#!/usr/bin/env python3
"""C295 independent exact certificate checker. Python standard library only.
Reads compact K_i integers; independently expands all 79 positive rational
branches at 250 endpoints. A finite author check, NOT formal Driver review.
"""
from fractions import Fraction as R
from pathlib import Path
import base64, hashlib, json, zlib
import C275_STANDALONE_EXACT_REPLAY as src
import C288_ISOLATING_BOXES_EXACT as c288
import C293_AUTHOR_VERIFY_EXACT as c293

D=1<<128
RAW_SHA="f254bd0a36235f453ae87dabd6ed84da8a4af551c7115354ec4aacbdc1bb0f2e"
RECORD_SHA="a17907ffe877796d857c090270112a958c16d16c1e35119136e1fdad83d6416f"

def independent_F(v,W):
    total=R(0)
    for j in src.J:
        node=src.U[j]
        term=R(W[j])
        for i in range(4):
            p=v[i]
            term=(term*(src.Z-p)*abs(node-src.U[src.I[i]]))/(
                (src.Z-src.U[src.I[i]])*abs(node-p))
        total+=term
    for k,p in enumerate(v):
        term=R(src.Q)*src.A/src.H/((2-p*p)*(3-p*p))**3
        for j in src.J: term=term*(src.Z-src.U[j])/abs(p-src.U[j])
        for m,z in enumerate(v):
            if m!=k: term=term*(src.Z-z)/abs(p-z)
        total+=term
    return total

def certificate_K():
    rows=Path("C295_125_K128_CERTIFICATE.b64").read_text().splitlines()
    assert rows[0]=="EM_C295_125_DYADIC_128_INTEGER_CERTIFICATE_V1"
    assert rows[2]=="source_sha256="+RAW_SHA
    assert rows[3]=="records_sha256="+RECORD_SHA
    raw=zlib.decompress(base64.b64decode(rows[-1],validate=True))
    assert len(raw)==125*16
    assert hashlib.sha256(raw).hexdigest()==RAW_SHA
    return [int.from_bytes(raw[i*16:(i+1)*16],"big") for i in range(125)]

def verify():
    paths,_=c288.build_paths()
    coarse,cert24=c293.load_certificate()
    assert len(paths)==len(coarse)==125
    K=certificate_K()
    W,_=src.floor_fixed_masses()
    reconstructed=[]
    max_nbits=max_dbits=0
    min_margin=None
    for i,(p,(idx,k24),k128) in enumerate(zip(paths,coarse,K)):
        assert idx==i
        assert (k24<<104)<=k128<((k24+1)<<104)
        reconstructed.append(dict(index=i,dyadic_left_integer=str(k128),
                 width_denominator_exponent=128,coarse_C293_K=k24,
                 candidate_correction_evaluations=0))
        for o in (0,1):
            t=R(k128+o,D)
            v=tuple(w+t*d for w,d in zip(p["w"],p["d"]))
            assert src.valid(v)
            assert all(lo<=x<=hi for x,(lo,hi) in zip(v,p["box"]))
            q=independent_F(v,W)/src.Q
            assert (q<1 if o==0 else q>1),(i,o,"bad sign")
            margin=abs(q-1)
            min_margin=margin if min_margin is None else min(min_margin,margin)
            max_nbits=max(max_nbits,q.numerator.bit_length())
            max_dbits=max(max_dbits,q.denominator.bit_length())
    digest=hashlib.sha256(json.dumps(reconstructed,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
    assert digest==RECORD_SHA
    assert min_margin>R(1,2**142)
    assert max_nbits==max_dbits==55773
    print("C295_INDEPENDENT_125x2_128BIT_EXACT_PASS",
          "125 paths; 250 exact positive-branch signs; slack > 2^-142",
          "max_F_over_Q_fraction_bits 55773",flush=True)

if __name__=="__main__":
    verify()
