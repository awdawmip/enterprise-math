#!/usr/bin/env python3
"""Pure-Python second algorithm for C312 witness rows, sharing frozen upstream circuit.

Its truncated polynomial recurrence and shared numerator modular evaluation
are distinct from C312 primary NumPy convolution and normalized branch evaluation.
"""
from __future__ import annotations
import json
from pathlib import Path
from math import gcd
from functools import reduce
import C311_INDEPENDENT_CERTIFICATE_CHECK as independent
import C311_COMPOSITE_CERTIFICATE as modular
import C310_JOINT_BRANCH_PRIME_CERT as c310

# Exact independent Kronecker-packed nonnegative polynomial convolution; at most
# 354 summands contribute to any coefficient, so digit width 2*bits(p)+10
# prevents carries and the extracted coefficients are reduced modulo p.

def packed_multiply(a,b,p,k):
    if not a or not b:return []
    n=min(len(a)+len(b)-1,k+1)
    width=2*p.bit_length()+10
    X=sum(int(x)<<(width*j) for j,x in enumerate(a) if x)
    Y=sum(int(x)<<(width*j) for j,x in enumerate(b) if x)
    Z=X*Y
    mask=(1<<width)-1
    ans=[]
    for j in range(n):
        ans.append((Z&mask)%p)
        Z>>=width
    return ans

def independent_coefficient(k,p,groups,prepared,L):
    vals={q:tuple(int(v%p) for v in q) for q in groups}
    total=0
    for scalar,nums,power in prepared:
        factors=[]
        for n in nums:
            c=reduce(gcd,n,0)
            scalar*=c
            factors.append(tuple(int((v//c)%p) for v in n))
        assert scalar%L==0
        scalar=scalar//L%p
        if not scalar:continue
        poly=[scalar]
        for q,e in groups.items():
            for _ in range(e-power.get(q,0)):
                poly=packed_multiply(poly,vals[q],p,k)
        for n in factors:
            poly=packed_multiply(poly,n,p,k)
        if len(poly)>k:total=(total+poly[k])%p
    return total

HERE=Path(__file__).resolve().parent

def main():
    src=json.loads((HERE/'C312_106_ZERO_EXTRA_CONTENT_CERT.json').read_text())
    assert len(src['rows'])==src['path_count']
    rr=json.loads((c310.c305.ROOT/'C293_125_REFINED_BRACKETS.json').read_text())
    paths,_=c310.c305.c288.build_paths()
    W,_=c310.c305.src.floor_fixed_masses()
    seen=set();coefficient_count=0;comp_count=0;functional_checks=0
    for row in src['rows']:
        i=row['path_index'];assert i not in seen;seen.add(i)
        s,groups,prepared,cancels,degree=c310.c305.prepare(i,paths[i],int(rr['records'][i][1]),W)
        # Independent scalar-content gcd calculation from raw terms:
        L=s
        for coeff,nums,_ in prepared:
            u=abs(coeff)
            for n in nums:u*=reduce(gcd,n,0)
            L=gcd(L,u)
        assert L == int(row['L_dec'])
        S=int(row['S_dec']);assert s==L*S
        H=int(row['H_dec'])
        product=H
        cache={}
        for witness in row['small_prime_powers']:
            p,e,k,r=(witness[x] for x in ('prime','exponent_in_S','degree','residue'))
            assert independent.is_small_prime(p), ('unverified prime',i,p)
            assert 1<=r<p and e>=1
            product*=p**e
            got=independent_coefficient(k,p,groups,prepared,L)
            assert got==r,(i,p,k,got,r)
            coefficient_count+=1
            if p<=11:
                # Verify the finite residue-class observation independently
                # from the original integer-factorized branch evaluation.
                ints=modular.prepared_int_terms(prepared,L)
                residues=[modular.eval_R_mod(p,t,groups,ints) for t in range(p)]
                assert (not any(residues))==witness['all_integer_samples_zero_mod_p']
                functional_checks+=1
        assert product==S
        cert=row['composite_bezout']
        if H>1:
            assert cert is not None and cert['T']==1
            # Independent direct numerator circuit, no normalized term division:
            v=independent.eval_shared_num_and_divide(prepared,groups,L,H,1)
            assert v==int(cert['R_mod_H_dec']),(i,'H',v)
            assert gcd(v,H)==1
            assert (v*int(cert['inverse_mod_H_dec']))%H==1
            comp_count+=1
        else:
            assert cert is None
        assert str(L)==row['determined_gcd_s_content_P_dec']
        print('C312_INDEPENDENT_PASS',i,'coefficient_checks',len(row['small_prime_powers']),flush=True)
    assert seen==set(range(125))-set(c310.EXCEPTIONAL)
    # C311 predecessor proof covers precisely the disjoint exceptional 19.
    old=json.loads((HERE/'C311_19_COMPOSITE_CONTENT_CERTIFICATE.json').read_text())
    assert {r['path_index'] for r in old['rows']}==set(c310.EXCEPTIONAL)
    assert len(seen)+len(old['rows'])==125
    print('C312_INDEPENDENT_ALL_PASS',len(seen),'coefficient_witnesses',coefficient_count,
          'composite_evaluations',comp_count,'functional_prime_sweeps',functional_checks,'C311_complement',len(old['rows']),flush=True)
if __name__=='__main__':main()
