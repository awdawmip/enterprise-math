#!/usr/bin/env python3
"""CBRC F7 r477: integer-verified B15 rational upper bound.
Numerical solver is a candidate generator only; proof check uses Python integers.
Reproduces a pinned witness SHA256 or verifies a saved raw-int32 vector.
"""
import argparse, hashlib, itertools, struct
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from CBRC_F7_R476_FINITE_FIBER_EXTENDED_LP_20261122 import build_matrix

B=15
DEN=100_000_000
EXPECTED_SHA="f03892d11b67ec8a6a687ae77d3ce24b14fc0d6edabb94d7489687ab5ca25bf1"

def index_keys():
    idx={}
    R=list(range(-2*B,2*B+1))
    T={r:range(2*r-min(B,r+B),2*r-max(-B,r-B)+1) for r in R}
    for i,r in enumerate(R):
        for u in R[i+1:]:
            for v in itertools.chain(T[r],T[u]):
                for rr in (r,u):
                    x,y=2*rr-v,rr-v
                    key=(abs(x),y)
                    if y!=0 and key not in ((2,1),(1,-1)) and key not in idx:
                        idx[key]=len(idx)
    return idx

def candidate():
    A,b,bounds,idx,_=build_matrix(B)
    r=linprog(np.zeros(A.shape[1]),A_ub=A,b_ub=b,bounds=bounds,
              method="highs-ipm",options={"time_limit":30})
    if r.status!=0 or r.x is None:
        raise RuntimeError(f"No numerical candidate: {r.message}")
    vals=[int(round(float(v)*DEN)) for v in r.x[:len(idx)]]
    return idx,vals

def verify(idx, vals):
    assert len(idx)==len(vals)==4730 and min(vals)>=2*DEN
    def q4(x,y):
        if y==0:return 0 if x==0 else 4*DEN
        k=(abs(x),y)
        if k in ((2,1),(1,-1)):return 2*DEN
        return vals[idx[k]]
    worst=0; arg=None; above=0
    for a,b,c,d in itertools.product(range(-B,B+1),repeat=4):
        k=a-2*b-c+2*d
        delta=q4(a+k,b+k)+q4(c-k,d-k)-q4(a,b)-q4(c,d)
        if abs(delta)>worst:
            worst=abs(delta);arg=(a,b,c,d)
        if abs(delta)>2*DEN:above+=1
    assert worst==2*DEN+1,(worst,arg)
    raw=struct.pack("<%di"%len(vals),*vals)
    sha=hashlib.sha256(raw).hexdigest()
    assert sha==EXPECTED_SHA,("Unexpected witness bytes",sha)
    print("B=",B,"quadruples=",(2*B+1)**4,"q variables=",len(vals))
    print("sha256=",sha,"max |D|=",f"{worst}/{4*DEN}",
          "half-error exceedances=",above,"attainment=",arg)
    return raw

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",type=Path)
    parser.add_argument("--write",type=Path)
    args=parser.parse_args()
    idx=index_keys()
    if args.verify:
        raw=args.verify.read_bytes()
        assert len(raw)==4*len(idx)
        vals=struct.unpack("<%di"%len(idx),raw)
    else:
        solver_idx,vals=candidate()
        assert solver_idx==idx
    raw=verify(idx, vals)
    if args.write:args.write.write_bytes(raw)

if __name__=="__main__":
    main()
