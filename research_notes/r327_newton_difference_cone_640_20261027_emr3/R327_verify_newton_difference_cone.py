#!/usr/bin/env python3
"""R327: exact BRC Newton triangular certificate and finite-difference cone.

Reuses the original 12-term integer B recurrence (R325) without floating point.
R326 proves Phi_q(q+u) is degree <=q, with B_{q+u}[q]=2^(q+u) Phi_q(q+u).

For 0<=u<=q set N_{q,u}=2^(q-u)*B_{q+u}[q].
Then N_{q,u}=2^(2q)*Phi_q(q+u) is an integer; every k-th forward
value D_{q,k}=(Delta^k N_{q,.})[0] is an exact integer. If all D_{q,k}>0
then all Phi_q(q+u)=2^(-2q)*sum_k D_{q,k} binom(u,k)>0 for integer u>=0.

Usage: python R327_verify_newton_difference_cone.py --max-q 640 --json out.json
"""
import argparse, hashlib, json, time
from fractions import Fraction
from math import comb, factorial

PRIOR_R325_SHA = "b007bb869980282dc2dc88101e762db65d2b55fa29d553e56a7ea5a237ac0821"
PRIOR_R326_SHA = "3a3decdf78a2db0fe4726b4e2ad097582994f32e05bd14663624cc3c3314e3c8"

def C(n,k): return comb(n,k) if 0<=k<=n else 0

def kernel(i):
    d=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),
       C(7,i-2), -C(9,i-3))
    out=[0]*(2*i+1)
    for j,v in enumerate(d,1):
        if v:
            p=i+1-j
            assert p>=0
            for k in range(p+1):out[i-1+k]-=v*C(p,k)
    while out and out[-1]==0:out.pop()
    return out

def source(s):
    if s>10:return []
    out=[0]*(2*s+2)
    for v,p in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if v:
            for k in range(p+1):out[s+k]+=v*C(p,k)
    while out and out[-1]==0:out.pop()
    return out

def scan(max_q=640):
    t0=time.monotonic()
    K=[None]+[kernel(i) for i in range(1,13)]
    assert K[1]==[2,3] and K[2]==[0,-1,4,4]
    samples=[[] for _ in range(max_q+1)]
    history={0:[1,1]}
    triangle_hash=hashlib.sha256()
    difference_hash=hashlib.sha256()
    original_check_sha=None
    triangle_checked=0
    min_forward_num=None
    min_forward_at=None
    boundary={}
    negative_tail_count=0
    for s in range(2*max_q+1):
        if s==0:b=history[0]
        else:
            b=source(s)
            b.extend([0]*(2*s+2-len(b)))
            for i in range(1,min(s,12)+1):
                v=history[s-i]
                for j,c in enumerate(K[i]):
                    if c:
                        for q,a in enumerate(v):b[q+j]+=c*a
            while b and b[-1]==0:b.pop()
            history[s]=b
            if s>=12:del history[s-12]
        assert len(b)<=2*s+2
        assert b[0]==(1<<s)
        for q in range(s+1):
            coeff=b[q] if q<len(b) else 0
            assert coeff>0,(s,q,coeff)
            triangle_hash.update(str(coeff).encode('ascii')+b'\n')
            triangle_checked+=1
        for q in range((s+1)//2,min(s,max_q)+1):
            assert s<=2*q
            samples[q].append(b[q]<<(2*q-s))
        negative_tail_count+=sum(1 for v in b[s+1:] if v<0)
        if s==1024:
            original_check_sha=triangle_hash.hexdigest()
            assert original_check_sha==PRIOR_R325_SHA,(original_check_sha,PRIOR_R325_SHA)
        if s in (0,13,64,128,512,1024,1280):
            boundary[str(s)]={'degree':len(b)-1,
                              'diagonal':str(b[s]),
                              'negative_outside':sum(v<0 for v in b[s+1:])}
    differences=[]
    total_differences=0
    min_integer_by_q={}
    for q in range(max_q+1):
        row=samples[q]
        assert len(row)==q+1,(q,len(row))
        D=[]
        for k in range(q+1):
            v=row[0]
            assert v>0,(q,k,v)
            D.append(v)
            difference_hash.update(f'{q}|{k}|{v}\n'.encode('ascii'))
            if min_forward_num is None or v<min_forward_num:
                min_forward_num=v;min_forward_at=[q,k]
            row=[row[j+1]-row[j] for j in range(len(row)-1)]
            total_differences+=1
        differences.append(D)
        if q in (0,1,13,64,65,128,256,512,max_q):
            min_integer_by_q[str(q)]={'min_forward_numerator':str(min(D)),
                                        'boundary_B_qq':str(D[0]//(1<<q))}
    assert total_differences==(max_q+1)*(max_q+2)//2
    # Independent translation of 65 prior fixed-q monomial certificates:
    # Delta basis to ordinary u^m basis via exact integer falling-factorial
    # polynomials, then Fraction denominators, same serialization as R326.
    prior_crosscheck=None
    if max_q>=64:
        old_sha=hashlib.sha256()
        old_sha.update(b'0|1\n')
        fall=[1]
        for q in range(1,65):
            nxt=[0]*(len(fall)+1)
            for m,v in enumerate(fall):
                nxt[m]-=(q-1)*v
                nxt[m+1]+=v
            fall=nxt
            # construct binomial-basis sum using previous falling polynomials
            power=[Fraction(0) for _ in range(q+1)]
            f=[1]
            for k in range(q+1):
                coeff=Fraction(differences[q][k], (1<<(2*q))*factorial(k))
                for m,v in enumerate(f):power[m]+=coeff*v
                nf=[0]*(len(f)+1)
                for m,v in enumerate(f):
                    nf[m]-=k*v
                    nf[m+1]+=v
                f=nf
            assert all(c>0 for c in power)
            old_sha.update((str(q)+'|'+','.join(str(c) for c in power)+'\n').encode('ascii'))
        prior_crosscheck=old_sha.hexdigest()
        assert prior_crosscheck==PRIOR_R326_SHA,(prior_crosscheck,PRIOR_R326_SHA)
    return {
       'status':'PASS',
       'method':'exact integer forward differences and R326 degree bound; no floating-point',
       'max_q':max_q,'max_s_direct':2*max_q,
       'unbounded_strips':'all integer 0<=q<=%d, s>=q'%max_q,
       'stronger_result':'all forward differences Delta^j Phi_q(q+u)>0 for 0<=j<=q and integer u>=0',
       'newton_forward_integer_numerators_checked':total_differences,
       'forward_integer_sha256':difference_hash.hexdigest(),
       'min_forward_integer_numerator':str(min_forward_num),
       'min_forward_integer_location':min_forward_at,
       'triangle_coefficients_checked':triangle_checked,
       'triangle_sha256':triangle_hash.hexdigest(),
       'triangle_positive_range':[0,2*max_q],
       'triangle_R325_1024_sha256_match':original_check_sha==PRIOR_R325_SHA,
       'triangle_R325_1024_sha256':original_check_sha,
       'R326_65_strips_power_basis_sha256_match':prior_crosscheck==PRIOR_R326_SHA,
       'R326_65_strips_power_basis_sha256':prior_crosscheck,
       'negative_outside_triangle_count':negative_tail_count,
       'samples':boundary,'forward_samples':min_integer_by_q,
       'elapsed_seconds':round(time.monotonic()-t0,3),
       'proof_dependency':'R326 uniform fixed-q degree <=q theorem (not independent Driver-admitted)',
       'review_status':'AUTHOR_EXACT_COMPUTER_ASSISTED / DRIVER_UNREVIEWED / NOT_ADMITTED'
    }

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-q',type=int,default=640)
    parser.add_argument('--json')
    args=parser.parse_args()
    result=scan(args.max_q)
    print(json.dumps({k:v for k,v in result.items() if k not in ('samples','forward_samples')},ensure_ascii=False,indent=2))
    if args.json:
        with open(args.json,'w',encoding='utf-8') as f:
            json.dump(result,f,ensure_ascii=False,indent=2)
            f.write('\n')
