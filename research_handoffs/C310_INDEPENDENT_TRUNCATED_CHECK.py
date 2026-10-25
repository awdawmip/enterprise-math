#!/usr/bin/env python3
"""Independent C310 p^2 witness crosscheck with truncated stdlib coefficient arithmetic.

Re-evaluates all 19 exact coefficient witnesses without NumPy/full convolution.
This shares the frozen C305 upstream polynomial circuit and does not independently
review the upstream C300 cancellation identity.
"""
from __future__ import annotations
import json
from pathlib import Path
from math import gcd
from functools import reduce
import C305_MODULAR_NEWTON_CONTENT as c305

BASE=Path(__file__).resolve().parent

def coefficient(term,groups,lower,mod,k):
    co,nums,power=term
    contents=[reduce(gcd,n,0) for n in nums]
    a=co
    for c in contents:a*=c
    assert a%lower==0
    a=(a//lower)%mod
    if a==0:return 0
    u=[a]
    for q,e in groups.items():
        for _ in range(e-power.get(q,0)):
            f=[int(x%mod) for x in q]
            v=[0]*min(k+1,len(u)+len(f)-1)
            for j,x in enumerate(u):
                if x:
                    for ell,y in enumerate(f[:max(0,len(v)-j)]):
                        v[j+ell]=(v[j+ell]+x*y)%mod
            u=v
    for n,c in zip(nums,contents):
        f=[int((x//c)%mod) for x in n]
        v=[0]*min(k+1,len(u)+len(f)-1)
        for j,x in enumerate(u):
            if x:
                for ell,y in enumerate(f[:max(0,len(v)-j)]):
                    v[j+ell]=(v[j+ell]+x*y)%mod
        u=v
    return u[k] if k<len(u) else 0

def main():
    rows=json.loads((BASE/'C310_JOINT_BRANCH_PRIME_CERT.json').read_text())['rows']
    source=json.loads((c305.ROOT/'C293_125_REFINED_BRACKETS.json').read_text())
    paths,_=c305.c288.build_paths()
    W,_=c305.src.floor_fixed_masses()
    assert len(rows)==19
    for row in rows:
        i=row['index'];p=row['prime'];k=row['first_nonzero_coefficient_mod_p2']
        mod=p*p
        s,groups,terms,_,_=c305.prepare(i,paths[i],int(source['records'][i][1]),W)
        lower=s
        for co,nums,_ in terms:
            v=abs(co)
            for n in nums:v*=reduce(gcd,n,0)
            lower=gcd(lower,v)
        assert str(lower)==row['lower_content_decimal']
        residue=sum(coefficient(term,groups,lower,mod,k) for term in terms)%mod
        assert residue==row['coefficient_residue_at_witness_mod_p2'],(i,residue)
        assert residue!=0
        print('C310_INDEPENDENT_TRUNCATED_PASS',i,'mod',mod,
              'coefficient',k,'residue',residue,flush=True)
    print('C310_INDEPENDENT_19_PASS')

if __name__=='__main__':
    main()
