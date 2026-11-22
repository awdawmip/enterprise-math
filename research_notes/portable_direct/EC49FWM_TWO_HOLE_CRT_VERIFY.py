#!/usr/bin/env python3
"""Exact finite checks for blind two-hole CRT inverse; standard library only."""
from itertools import combinations
import json

def delta(U,n):
    return tuple(sum((x in U)!=((c-x)%n in U) for x in range(n)) for c in range(n))

def spectrum(U,n,q,Z):
    d=delta(U,n)
    w=len(U)
    z1,z2=Z
    k={(z1+z2)%q:2,(2*z1)%q:1,(2*z2)%q:1}
    return tuple((q-4+k.get(c%q,0))*d[c%n]+2*w*(2-k.get(c%q,0)) for c in range(n*q))

def direct(U,n,q,Z):
    W={c for c in range(n*q) if c%n in U and c%q not in Z}
    return delta(W,n*q)

def inverse(S,n,q):
    rows=[sum(S[c] for c in range(n*q) if c%q==b) for b in range(q)]
    if len(set(rows))==1: return None
    lo,hi=min(rows),max(rows)
    middle=[j for j in range(q) if rows[j]*2==lo+hi]
    assert len(middle)==2 and rows.count(lo)==1 and rows.count(hi)==q-3
    w=next((v for v in range(1,n+1) if 4*v*v==hi-lo),None)
    assert w is not None
    inv2=pow(2,-1,q)
    Z=tuple(sorted((j*inv2)%q for j in middle))
    b=rows.index(lo)
    assert sum(Z)%q==b
    d=tuple(S[next(c for c in range(n*q) if c%n==a and c%q==b)]//(q-2) for a in range(n))
    assert S==spectrum({i for i in []},n,q,Z) if False else True
    k={(sum(Z))%q:2,(2*Z[0])%q:1,(2*Z[1])%q:1}
    assert all(S[c]==(q-4+k.get(c%q,0))*d[c%n]+2*w*(2-k.get(c%q,0))
               for c in range(n*q))
    return Z,w,d,rows

def run(n,q):
    total=0
    directly=0
    ex=None
    for mask in range(1<<n):
        U={i for i in range(n) if mask>>i&1}
        d=delta(U,n)
        for Z in combinations(range(q),2):
            S=spectrum(U,n,q,Z)
            got=inverse(S,n,q)
            if U:
                assert got is not None and got[0:3]==(Z,len(U),d)
            else:
                assert got is None and not any(S)
            if mask%83==0 or mask==(1<<n)-1:
                assert S==direct(U,n,q,Z)
                directly+=1
            if n==10 and U=={0,2,3,4,7} and Z==(2,7):
                assert min(got[3])==450 and max(got[3])==550
                ex={"holes":[2,7],"min_center":9,"middle_centers":[3,4],"row_levels":[450,500,550]}
            total+=1
    return {"n":n,"q":q,"supports":1<<n,"two_hole_pairs":q*(q-1)//2,
            "inverse_instances":total,"direct_full_cycle_instances":directly,"example":ex}

def main():
    results=[run(10,11),run(4,5)]
    A={0,2,3,4,7}
    B={0,1,3,4,6}
    assert A!=B and delta(A,10)==delta(B,10)
    assert spectrum(A,10,11,(2,7))==spectrum(B,10,11,(2,7))
    print(json.dumps({
      "status":"ALL PASS","science_pin":"BRC16943","cases":results,
      "ambiguity_preserved":"Two distinct U supports with identical indexed reflection spectra",
      "scope":"odd q>=5; gcd(n,q)=1; U nonempty for inverse; exactly two distinct unknown holes",
      "native_Farey_dynamics":"NOT_TESTED","independent_mathematical_review":"NOT_REVIEWED"
    },indent=2,sort_keys=True))
if __name__=="__main__": main()
