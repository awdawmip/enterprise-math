#!/usr/bin/env python3
"""C313 branchwise F7 fixed-divisor lower multiplicity in the C305 source circuit."""
from __future__ import annotations
import json,time
from collections import Counter
from math import gcd
import C311_COMPOSITE_CERTIFICATE as c311
import C310_JOINT_BRANCH_PRIME_CERT as c310

P=7

def root_val(poly,a,p=7):
    v=[x%p for x in poly]
    while len(v)>1 and v[-1]==0:v.pop()
    if not any(v):return None
    count=0
    while len(v)>1:
        # division by t-a using synthetic coefficients ascending
        res=[0]*(len(v)-1)
        res[-1]=v[-1]
        for j in range(len(v)-2,0,-1):res[j-1]=(v[j]+a*res[j])%p
        remainder=(v[0]+a*res[0])%p
        if remainder:break
        count+=1
        v=res
    return count

def inspect_one(i, paths, krecords, W, return_all=False):
    s,groups,prep,cancels,degree=c310.c305.prepare(i,paths[i],int(krecords[i][1]),W)
    L=c310.term_content_lower(s,prep)
    terms=c311.prepared_int_terms(prep,L)
    group_v={q:tuple(root_val(q,a) for a in range(P)) for q in groups}
    ncache={}
    all_mult=[];nonzero=[];structural_zero=0
    for j,(scalar,nums,powers) in enumerate(terms):
        if scalar%P==0:
            structural_zero+=1
            all_mult.append(None);continue
        av=[0]*P
        for q,e in groups.items():
            t=e-powers.get(q,0)
            if t:
                for a,val in enumerate(group_v[q]):
                    if val is None:raise AssertionError('Nonprimitive denominator polynomial modulo 7')
                    av[a]+=t*val
        for n in nums:
            if n not in ncache:ncache[n]=tuple(root_val(n,a) for a in range(P))
            if any(v is None for v in ncache[n]):
                # a numerator may be identically zero mod 7, yielding zero term
                av=None;structural_zero+=1;break
            for a,v in enumerate(ncache[n]):av[a]+=v
        if av is None:all_mult.append(None);continue
        nonzero.append(j); all_mult.append(av)
    if not nonzero:raise AssertionError('all-zero polynomial terms modulo 7')
    # m is a certified lower bound for total polynomial R; min across all nonzero terms and residues
    M=min(min(all_mult[j]) for j in nonzero)
    return {'index':i,'degree_P_upper':degree,'branch_count':len(terms),'nonzero_branch_polynomials_mod7':len(nonzero),
            'zero_branch_polynomials_mod7':structural_zero,'guaranteed_P7_multiplicity':M,
            'max_branch_min_multiplicity':max(min(all_mult[j]) for j in nonzero),
            'minimum_at_residue':[min(all_mult[j][a] for j in nonzero) for a in range(P)],
            'all_nonz_branch_names':nonzero if return_all else None}

if __name__=='__main__':
    paths,_=c310.c305.c288.build_paths()
    rr=json.loads(c311.FROZEN.read_text())
    assert rr['records_sha256']=='03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89'
    W,_=c310.c305.src.floor_fixed_masses()
    t0=time.monotonic();rows=[]
    for i in range(125):
        z=inspect_one(i,paths,rr['records'],W)
        rows.append(z)
        if i%25==0:print('C313_PART',i,z,flush=True)
    print('C313_TOTAL',len(rows),'m distribution',dict(sorted(Counter(x['guaranteed_P7_multiplicity'] for x in rows).items())),
          'minimum',min(x['guaranteed_P7_multiplicity'] for x in rows),
          'max',max(x['guaranteed_P7_multiplicity'] for x in rows), 'elapsed',round(time.monotonic()-t0,2),flush=True)
    with open('C313_BRANCHWISE_F7_AUDIT_125.json','w') as f:json.dump({'schema':'C313_F7_BRANCHWISE_FIXED_DIVISOR_LOWER_BOUND_V1','rows':rows},f,indent=2)
