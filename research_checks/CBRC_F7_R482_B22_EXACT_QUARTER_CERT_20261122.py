#!/usr/bin/env python3
"""F7 exact B22 quarter-grid minimax certificate (Python standard library only)."""
import base64
import hashlib
import itertools
import zlib
from collections import Counter
from pathlib import Path

B=22
RAW_SHA='a3ee263f0ea8a1d47aaed4c1a5dd6a6b346b3da9f3df03f3a3cfa40153799ba6'
ARTIFACT='F7_R482_B22_Exact_Quarter_Witness_20261122.b85'

def index():
    R=list(range(-2*B,2*B+1))
    T={r:range(2*r-min(B,r+B),2*r-max(-B,r-B)+1) for r in R}
    ix={}
    for i,r in enumerate(R):
        for u in R[i+1:]:
            for v in itertools.chain(T[r],T[u]):
                for rr in (r,u):
                    x,y=2*rr-v,rr-v
                    k=abs(x),y
                    if y and k not in ((2,1),(1,-1)) and k not in ix:
                        ix[k]=len(ix)
    return ix

def check():
    data=(Path(__file__).resolve().parent.parent/'research_artifacts'/ARTIFACT).read_text().strip()
    raw=zlib.decompress(base64.b85decode(data))
    assert hashlib.sha256(raw).hexdigest()==RAW_SHA
    ix=index()
    assert len(ix)==len(raw)==10096
    assert Counter(raw)=={2:7094,3:2433,4:569}
    def Q(x,y):
        if not y:return 0 if x==0 else 4
        k=abs(x),y
        if k in ((2,1),(1,-1)):return 2
        return raw[ix[k]]
    assert Q(0,0)==0 and Q(2,1)==Q(-1,-1)==2
    counts=Counter()
    for a,b,c,d in itertools.product(range(-B,B+1), repeat=4):
        k=a-2*b-c+2*d
        delta=Q(a+k,b+k)+Q(c-k,d-k)-Q(a,b)-Q(c,d)
        assert abs(delta)<=2
        counts[delta]+=1
    assert dict(counts)=={-2:122698,-1:980690,0:1998461,1:903104,2:95672}
    assert sum(counts.values())==45**4==4100625
    assert counts[-2]+counts[2]==218370
    print('CERTIFIED F7 exact e_B=1/2 for 1<=B<=22',
          'inputs',sum(counts.values()),'free Q values',len(raw),
          'max|4D|=2','tight',218370,'SHA256',RAW_SHA)

if __name__=='__main__':
    check()
