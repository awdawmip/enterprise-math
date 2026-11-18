#!/usr/bin/env python3
"""R762DZ exact finite witness checker, positive BRC terminal group ring."""
from itertools import product
from math import comb
import hashlib
import json
import numpy as np

BRANCHES = ((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
def qform(i,j,k):
    return (2*i*j+i*k+2*j*k)%3

def character_leading():
    hist={0:0,1:0,2:0}
    for i,j,k in product(range(3),repeat=3):
        # P(zeta^i,zeta^j,zeta^k) coefficient at pi^2,
        # independently computed by (1+pi)^e binomial expansion.
        coeff=sum(comb(i*x+j*y+k*z,2) for x,y,z in BRANCHES)%3
        assert coeff==qform(i,j,k), (i,j,k,coeff)
        hist[coeff]+=1
    assert hist=={0:9,1:6,2:12}, hist
    return hist

def validate(q,horizon):
    d=q//3
    modulus=3**(horizon//d+1)
    a=np.zeros((q,q,q),dtype=np.int64)
    a[0,0,0]=1
    boundaries=[]
    for n in range(1,horizon+1):
        # Integer positive six-branch cyclic convolution; no FFT or floats.
        b=(a+np.roll(a,1,axis=0)+np.roll(a,1,axis=2)
           +np.roll(a,(1,1),axis=(0,1))
           +np.roll(a,(1,1),axis=(1,2))
           +np.roll(a,(1,1,1),axis=(0,1,2)))
        a=b%modulus
        m=n//d
        assert np.all(a%(3**max(0,m-2))==0),("lower",q,n)
        assert np.any(a%(3**(m+1))!=0),("upper",q,n)
        assert int(a.sum()%modulus)==pow(6,n,modulus),("mass",q,n)
        if n%d==0:
            v=0
            while v<horizon//d and np.all(a%(3**(v+1))==0):
                v+=1
            boundaries.append([n,v,m])
    return {
      "q":q,"horizon":horizon,"modulus":modulus,
      "bound_checks":2*horizon,"mass_checks":horizon,
      "boundaries":boundaries,
      "final_array_le_i64_sha256":hashlib.sha256(a.astype("<i8").tobytes()).hexdigest()
    }

def main():
    result={"character_residues":character_leading(),
            "finite_positive_brc_checks":[validate(9,54),validate(27,108)],
            "status":"PASS"}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
