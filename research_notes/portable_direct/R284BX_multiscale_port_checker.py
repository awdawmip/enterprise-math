#!/usr/bin/env python3
"""R284BX reproducible exact certificates; Python standard library only.

C ranges over {1,2}^{4x4} in lexicographic row-major order.
Output: R284BX_multiscale_port_verification.json with full gap witnesses.
"""
import bisect
import hashlib
import itertools
import json
import math
from pathlib import Path

# bits, prime, d0, d3, z1, z2, z3, exact minimum cyclic gap
CASES = (
    (28, 268435399, 988826, 637873, 224007, 661446, 310514, 1),
    (31, 2147483647, 509251, 307397, 372686, 124406, 494014, 3),
    (32, 4294967291, 202052, 981610, 339700, 614397, 346881, 10),
    (33, 8589934583, 860189, 661306, 462704, 258730, 853243, 16),
    (34, 17179869143, 221288, 961762, 295480, 300289, 588278, 34),
)

def signature(c):
    a,b1,b2,b3,u1,a11,x,y,u2,w,a22,z,u3,g,h,r=c
    t,s=6-a11,13-a22
    U=t*s-x*w
    V=-r*U-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2=s*u1+x*u2,t*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=U*u3+p1*g+p2*h
    J=-a*U-b1*p1-b2*p2
    K=-a*V-b1*q1-b2*q2-b3*q3
    return U,V,p1,p2,q1,q2,q3,J,K

def observe(sig,case):
    _,prime,d0,d3,z1,z2,z3,_=case
    U,V,p1,p2,q1,q2,q3,J,K=sig
    return (d0*(U*d3+V)-z1*(p1*d3+q1)-z2*(p2*d3+q2)
            -z3*q3+J*d3+K)%prime

def direct_det(c,case):
    _,prime,d0,d3,z1,z2,z3,_=case
    M=[[-c[4*i+j] for j in range(4)] for i in range(4)]
    for i,v in enumerate((d0,6,13,d3)): M[i][i]+=v
    for j,v in enumerate((z1,z2,z3),1): M[0][j]-=v
    total=0
    for perm in itertools.permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        total+=(-1 if inv%2 else 1)*math.prod(M[i][perm[i]] for i in range(4))
    return total%prime

def prime_by_trial(n):
    return n>2 and n%2==1 and all(n%d for d in range(3,math.isqrt(n)+1,2))

def verify():
    for bits,p,*_ in CASES:
        assert p.bit_length()==bits and prime_by_trial(p)
    universe=list(itertools.product((1,2),repeat=16))
    sigs=[signature(c) for c in universe]
    coeff_fibres={}
    for c,sig in zip(universe,sigs):
        key=sig[:8]
        if key in coeff_fibres:
            prior=coeff_fibres[key]
            assert prior[:3]+prior[4:]==c[:3]+c[4:] and prior[3]!=c[3]
        else: coeff_fibres[key]=c
    assert len(coeff_fibres)==32768
    assert min(s[6] for s in sigs)==59 and max(s[6] for s in sigs)==196
    results=[]
    for case in CASES:
        bits,p,d0,d3,z1,z2,z3,expected=case
        rowmajor=[observe(sig,case) for sig in sigs]
        digest=hashlib.sha256()
        for val in rowmajor: digest.update(val.to_bytes(8,"big"))
        ordered=sorted((val,i) for i,val in enumerate(rowmajor))
        vals=[v for v,_ in ordered]
        gaps=[vals[i+1]-vals[i] for i in range(65535)]+[p-vals[-1]+vals[0]]
        m=min(gaps)
        assert m==expected and m>0
        bound=(m-1)//2
        for i,v in enumerate(rowmajor):
            for e in (-bound,0,bound):
                received=(v+e)%p
                j=bisect.bisect_left(vals,received)
                near=min((j%65536,(j-1)%65536),
                         key=lambda k:min((vals[k]-received)%p,(received-vals[k])%p))
                assert ordered[near][1]==i
        checks=0
        for i in range(0,65536,257):
            assert direct_det(universe[i],case)==rowmajor[i]
            checks+=1
        first=gaps.index(m)
        results.append({
            "bits":bits,"prime":p,"d0_d3_z1_z2_z3":[d0,d3,z1,z2,z3],
            "matrix_count":65536,"distinct_residue_count":len(set(rowmajor)),
            "minimum_circular_gap":m,"number_of_minimum_gaps":gaps.count(m),
            "real_noise_guarantee":f"0 <= rho < {m}/2",
            "maximum_integral_error":bound,"decoded_tests":196608,
            "independent_det_checks":checks,
            "rowmajor_be64_sha256":digest.hexdigest(),
            "one_minimal_gap_pair":{
                "first_residue":ordered[first][0],
                "first_matrix_row_major":list(universe[ordered[first][1]]),
                "second_residue":ordered[(first+1)%65536][0],
                "second_matrix_row_major":list(universe[ordered[(first+1)%65536][1]])
            }
        })
    return {
        "schema":"EM_R284BX_MULTISCALE_FROZEN_DOUBLE_LEAF_FINITE_CERT_V1",
        "predecessor":"R284BW_SMALL_MODULUS_SHARP_NOISE_20261120.md",
        "model":"det(diag(d0,6,13,d3)-C-z1*E01-z2*E02-z3*E03) mod p",
        "alphabet":[1,2],"matrix_dimensions":[4,4],
        "frozen_controls_d1_d2":[6,13],"signature_fibres":32768,
        "q3_extrema":[59,196],"case_results":results,
        "independent_review":"NOT_REVIEWED"
    }

if __name__=="__main__":
    output=verify()
    path=Path(__file__).with_name("R284BX_multiscale_port_verification.json")
    path.write_text(json.dumps(output,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(output,indent=2,sort_keys=True))
