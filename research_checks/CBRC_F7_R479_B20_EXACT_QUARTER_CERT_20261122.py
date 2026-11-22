#!/usr/bin/env python3
"""Standalone exact-integer F7 B20 minimax certificate checker (Python stdlib).
No numerical optimization is used. The compressed certificate gives Q=4*q.
"""
import base64,hashlib,itertools,struct,sys,zlib
from pathlib import Path
B=20
SHA='c393685154755cf9f5c943334ceb247fe1c2ad73bcf8835fcdb41c1087012a36'
NAME='F7_R479_B20_Exact_Quarter_Witness_20261122.b85'

def index():
    R=list(range(-2*B,2*B+1))
    T={r:range(2*r-min(B,r+B),2*r-max(-B,r-B)+1) for r in R}
    ix={}
    for i,r in enumerate(R):
        for u in R[i+1:]:
            for v in itertools.chain(T[r],T[u]):
                for rr in (r,u):
                    x,y=2*rr-v,rr-v
                    k=(abs(x),y)
                    if y and k not in ((2,1),(1,-1)) and k not in ix:ix[k]=len(ix)
    return ix

def check(path):
    raw=zlib.decompress(base64.b85decode(path.read_text(encoding='ascii').strip()))
    assert hashlib.sha256(raw).hexdigest()==SHA
    ix=index(); assert len(ix)==len(raw)==8358
    assert min(raw)==2 and max(raw)==4
    def Q(x,y):
        if not y:return 0 if x==0 else 4
        k=(abs(x),y)
        if k in ((2,1),(1,-1)):return 2
        return raw[ix[k]]
    worst=0;arg=None;ntight=0;nnz=0
    for a,b,c,d in itertools.product(range(-B,B+1),repeat=4):
        k=a-2*b-c+2*d
        delta=Q(a+k,b+k)+Q(c-k,d-k)-Q(a,b)-Q(c,d)
        if abs(delta)>worst:worst=abs(delta);arg=(a,b,c,d)
        if abs(delta)==2:ntight+=1
        if delta:nnz+=1
    assert worst==2 and ntight==158624 and nnz==1453374
    print('CERTIFIED: F7 e_B=1/2 for 1<=B<=20;',
          'inputs',41**4,'q_variables',len(raw),'max|4D|',worst,
          'tight_inputs',ntight,'nonzero_inputs',nnz,
          'attainment_input',arg,'sha256',SHA)

if __name__=='__main__':
    default=Path(__file__).resolve().parent.parent/'research_artifacts'/NAME
    check(Path(sys.argv[1]) if len(sys.argv)>1 else default)
