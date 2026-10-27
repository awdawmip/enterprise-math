#!/usr/bin/env python3
"""R333 exact continuation: new r=301..320 signed-tail BRC Newton certificates.

No truncation of signed tails; all signs use integer/Fraction operations.
The all-u inference relies on R330's exact rational extraction identity
which proves deg H_r<=r (author-side, not independently admitted).
"""
import argparse, hashlib, json
from fractions import Fraction
from math import comb

def C(n,k): return comb(n,k) if 0<=k<=n else 0

def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return z

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b):
                if w:z[i+j]+=v*w
    return z

def monomial(n,coeff,degree):
    return [0]*degree+[coeff*C(n,j) for j in range(n+1)]

def K(i):
    d=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    a=[0]
    for j,v in enumerate(d,1):
        if v:a=add(a,monomial(i+1-j,-v,i-1))
    return a

def J(s):
    a=[0]
    for v,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if v:a=add(a,monomial(n,v,s))
    return a

def build(R):
    b=[[1,1]]; kk=[None]+[K(i) for i in range(1,13)]
    for s in range(1,3*R+3):
        v=J(s)
        for i in range(1,min(s,12)+1):v=add(v,mul(kk[i],b[s-i]))
        b.append(v)
    return b

def dh_values(b, r, extra=1):
    vals=[]
    for u in range(r+1+extra):
        q=r+u
        d=sum((-1)**(u-v)*C(u,v)*2**(q-v)*b[q+v][q] for v in range(u+1))
        vals.append(Fraction(d,5**u))
    return vals

def diffs(vals):
    vals=list(vals); out=[]
    while vals:
        out.append(vals[0]);vals=[vals[i+1]-vals[i] for i in range(len(vals)-1)]
    return out

def check(lo,hi,prior_r332=None):
    b=build(hi)
    triangle=sum(1 for s,row in enumerate(b) for q in range(s+1) if q<len(row) and row[q]>0)
    assert triangle==len(b)*(len(b)+1)//2
    outside=sum(x<0 for s,row in enumerate(b) for x in row[s+1:])
    historical_overlap={'r':300,'full_prior_case_comparison':None}
    if prior_r332 is not None:
        with open(prior_r332,encoding='utf-8') as f:old=json.load(f)
        assert old['r_interval']==[257,300]
        case=next(c for c in old['cases'] if c['r']==300)
        actual=diffs(dh_values(b,300,extra=1))
        assert actual[-1]==0
        assert str(actual[0])==case['H_0']
        assert str(actual[1])==case['DeltaH_0']
        assert str(actual[-2])==case['Delta^rH_0']
        historical_overlap={'r':300,'full_prior_case_comparison':True,
            'checked_fields':['H_0','DeltaH_0','Delta^rH_0','last_extra_difference'],
            'r332_coefficient_range_sha256':old['sha256_new_coefficients']}
    cases=[];h=hashlib.sha256();total=0
    for r in range(lo,hi+1):
        vals=dh_values(b,r,extra=1)
        co=diffs(vals[:r+1]);extra_coeff=diffs(vals)[-1]
        assert extra_coeff==0,(r,'extra degree failure',extra_coeff)
        assert len(co)==r+1 and all(v>0 for v in co)
        assert co[-1]==6**r
        for i,c in enumerate(co):h.update(f'{r},{i},{c.numerator}/{c.denominator}\n'.encode('ascii'))
        total+=len(co)
        cases.append({'r':r,'positive_coefficient_count':len(co),
          'H0':str(co[0]),'H1_diff':str(co[1]),
          'highest':str(co[-1]),'extra_difference':str(extra_coeff)})
    return {'schema':'R333_BRC_CORANK_EXTENSION_V1','status':'PASS',
       'prior_immutable_R332_commit':'16b2209bda28aa8d8082331820e0e1e62410fef3',
       'r_interval':[lo,hi],'new_unbounded_bands':hi-lo+1,
       'new_exact_positive_newton_coefficients':total,
       'source_polynomials_B_s_rows':[0,3*hi+2],
       'triangular_coefficients_positive':triangle,
       'outside_triangle_negative_retained':outside,
       'sha256_new_coefficients':h.hexdigest(),'cases':cases,
       'extra_degree_checks':hi-lo+1,
       'highest_coefficient_equal_six_to_r':True,
       'historical_overlap_comparison':historical_overlap,
       'infinite_scope_dependency':'R330 exact rational extraction, deg H_r<=r; independent review pending',
       'arithmetic':'exact Python arbitrary precision integers and fractions; signed tails retained',
       'interpretation':'AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--min-r',type=int,default=301)
    p.add_argument('--max-r',type=int,default=320)
    p.add_argument('--prior-r332',default=None)
    p.add_argument('--out',default='R333_EXACT_EVIDENCE.json')
    a=p.parse_args()
    data=check(a.min_r,a.max_r,a.prior_r332)
    with open(a.out,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({k:v for k,v in data.items() if k!='cases'},indent=2))
