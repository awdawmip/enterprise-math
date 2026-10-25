#!/usr/bin/env python3
"""C310: exact prime-field joint-branch content certificates.

Author-level auxiliary scalar computation conditional on upstream C300;
does not establish a native BRC/X6 law or any mathematical admission.
"""
from __future__ import annotations
import json, argparse, time
from math import gcd
from functools import reduce
from collections import Counter
from pathlib import Path
import numpy as np
import C305_MODULAR_NEWTON_CONTENT as c305

BASE=Path(__file__).resolve().parent
EXCEPTIONAL=[3,6,7,8,11,12,17,26,27,29,30,33,34,38,56,75,76,97,108]
PRIME_THREE={3,8,38,56}

def term_content_lower(s,prepared):
    """Direct 79-term gcd bound, with no historical complete-Newton oracle."""
    g=s
    for co,nums,_ in prepared:
        v=abs(co)
        for n in nums:v*=reduce(gcd,n,0)
        g=gcd(g,v)
    return g

def pmul(a,b,p):
    if len(a)==0 or len(b)==0:return np.array([],dtype=np.int64)
    c=np.convolve(a,b)%p
    j=len(c)
    while j>1 and not c[j-1]:j-=1
    return c[:j]

def polysum(a,b,p):
    c=np.zeros(max(len(a),len(b)),dtype=np.int64)
    c[:len(a)]+=a
    c[:len(b)]+=b
    return c%p

def poly_branch_mod(p,groups,prepared,lower):
    group_items=list(groups.items())
    q_mod={q:np.array([int(v%p) for v in q],dtype=np.int64) for q,e in group_items}
    out=np.array([0],dtype=np.int64)
    term_nonzero=term_vanishes=maxdegree=0
    for coeff,nums,exps in prepared:
        contents=[reduce(gcd,n,0) for n in nums]
        scalar=coeff
        for c in contents:scalar*=c
        assert scalar%lower==0
        scalar//=lower
        if scalar%p==0:
            term_vanishes+=1
            continue
        term_nonzero+=1
        term=np.array([scalar%p],dtype=np.int64)
        for q,e in group_items:
            for _ in range(e-exps.get(q,0)):
                term=pmul(term,q_mod[q],p)
        for n,c in zip(nums,contents):
            n0=np.array([int((x//c)%p) for x in n],dtype=np.int64)
            term=pmul(term,n0,p)
        maxdegree=max(maxdegree,len(term)-1)
        out=polysum(out,term,p)
    return out,term_nonzero,term_vanishes,maxdegree

def monic_factor(q,p):
    v=tuple(int(x%p) for x in q)
    while len(v)>1 and v[-1]==0:v=v[:-1]
    assert v!=(0,),"every primitive factor must remain nonzero modulo p"
    c=v[-1]
    return c,tuple((x*pow(c,-1,p))%p for x in v)

def factor_signature(term,groups,lower,p):
    coeff,nums,denpower=term
    scal=coeff
    contents=[reduce(gcd,n,0) for n in nums]
    for c in contents:scal*=c
    assert scal%lower==0
    scal=scal//lower%p
    bag=Counter()
    for q,e in groups.items():
        for _ in range(e-denpower.get(q,0)):
            c,f=monic_factor(q,p)
            scal=scal*c%p
            if len(f)>1:bag[f]+=1
    for n,c0 in zip(nums,contents):
        c,f=monic_factor(tuple(x//c0 for x in n),p)
        scal=scal*c%p
        if len(f)>1:bag[f]+=1
    return scal,bag

def pairwise_certificate(groups,prepared,lower,p):
    survivors=[]
    for j,term in enumerate(prepared):
        coeff,nums,power=term
        a=coeff
        for n in nums:a*=reduce(gcd,n,0)
        assert a%lower==0
        if (a//lower)%p:survivors.append(j)
    assert len(survivors)==2,('not exactly a pair',survivors)
    (ua,fa),(ub,fb)=(factor_signature(prepared[j],groups,lower,p) for j in survivors)
    assert ua%p and ub%p and (ua+ub)%p==0
    assert fa==fb,('factor bags mismatch',survivors)
    return dict(survivors=survivors,normalized_scalars_mod_p=[ua,ub],
                equal_monic_factor_multiset=True,
                total_monic_factor_occurrences=sum(fa.values()),
                distinct_monic_factors=len(fa))

def main(indices):
    frozen=json.loads((c305.ROOT/'C293_125_REFINED_BRACKETS.json').read_text())
    paths,_=c305.c288.build_paths()
    W,_=c305.src.floor_fixed_masses()
    result=[]
    for i in indices:
        t0=time.monotonic()
        s,groups,prepared,cancels,d=c305.prepare(i,paths[i],int(frozen['records'][i][1]),W)
        lower=term_content_lower(s,prepared)
        assert i in EXCEPTIONAL
        p=3 if i in PRIME_THREE else 2
        assert s%lower==0 and s%p==0
        pair=pairwise_certificate(groups,prepared,lower,p)
        out,nz,zero,maxd=poly_branch_mod(p,groups,prepared,lower)
        assert np.count_nonzero(out)==0,(i,p,'mod-p nonzero')
        degree_upper=max(sum((len(q)-1)*e for q,e in groups.items()),d+2)
        assert maxd<=degree_upper
        outp2,_,_,_=poly_branch_mod(p*p,groups,prepared,lower)
        p2count=int(np.count_nonzero(outp2))
        assert p2count>0,(i,'unexpected p^2 divisibility')
        witness=next((int(k),int(v)) for k,v in enumerate(outp2) if v%(p*p))
        obj=dict(index=i,prime=p,degree_reduced=d,degree_full_upper=degree_upper,
                 terms=len(prepared),terms_nonzero_mod_p=nz,
                 terms_vanishing_mod_p=zero,**pair,
                 residual_coefficients_mod_p_nonzero=0,
                 residual_coefficients_mod_p2_nonzero=p2count,
                 first_nonzero_coefficient_mod_p2=witness[0],
                 coefficient_residue_at_witness_mod_p2=witness[1],
                 proposed_prime=p,lower_content_decimal=str(lower),
                 lower_content_bits=lower.bit_length(),
                 degree_mod_p2=len(outp2)-1,
                 seconds=round(time.monotonic()-t0,3))
        result.append(obj)
        print('C310_PRIME_PASS',i,'prime',p,'p2_nonzero',p2count,
              'index',witness[0],flush=True)
    doc={'schema':'C310_JOINT_BRANCH_PRIME_CERT_V1',
         'model':'C195/H168 auxiliary 79-branch positive rational scalar, C293 frozen paths',
         'source_C293_sha256':frozen['records_sha256'],
         'source_c309':'research/c309-structural-content-prefix-20261026-research2@3b1d56d2b8256c0372f382abe0ad0125d5173c6c',
         'scope':'Prime candidate from C309 frontier; term gcd recomputed directly without C306 G oracle. Author exact mod p and p^2 coefficients; C300 factorization assumed; not native BRC/X6',
         'rows':result}
    (BASE/'C310_JOINT_BRANCH_PRIME_CERT.json').write_text(json.dumps(doc,indent=2)+'\n')
    print('C310_ALL',len(result),'PASS')

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--indices',default=','.join(map(str,EXCEPTIONAL)))
    args=ap.parse_args()
    main([int(x) for x in args.indices.split(',')])
