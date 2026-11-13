#!/usr/bin/env python3
"""Exact post-R331 continuation of BRC Newton corank bands.

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

def check(lo,hi, prior_file=None):
    b=build(hi)
    triangle=sum(1 for s,row in enumerate(b) for q in range(s+1) if q<len(row) and row[q]>0)
    assert triangle==len(b)*(len(b)+1)//2
    outside=sum(x<0 for s,row in enumerate(b) for x in row[s+1:])
    cases=[];h=hashlib.sha256(); total=0
    for r in range(lo,hi+1):
        vals=dh_values(b,r,extra=1)
        co=diffs(vals[:r+1]);extra_coeff=diffs(vals)[-1]
        assert extra_coeff==0, (r,'failed out-of-sample degree check',extra_coeff)
        assert len(co)==r+1
        assert all(x>0 for x in co),(r,'nonpositive coefficient')
        assert co[-1]==6**r,(r,'leading degree certificate failure')
        for i,c in enumerate(co):h.update(f'{r},{i},{c.numerator}/{c.denominator}\n'.encode())
        total+=len(co)
        cases.append({'r':r,'positive_coefficient_count':len(co),'H_0':str(co[0]),'DeltaH_0':str(co[1]),'Delta^rH_0':str(co[-1]),'last_extra_difference':str(extra_coeff),'min_coefficient_positive':True})
        print('r',r,'PASS',len(co),'H0=',str(co[0])[:70],flush=True)
    # Version-lock one historical band against its independent R331 evidence.
    # This does not recalculate all 0..256 previous bands.
    historical=diffs(dh_values(b,256,extra=0))
    historic_bytes=''.join(f'256,{i},{c}\n' for i,c in enumerate(historical)).encode()
    h256=hashlib.sha256(historic_bytes).hexdigest()
    assert h256=='eaa453a67a463d27c336adfe80d9b4422c6d03f9e3583102855b6817a8e72a8a'
    prior_comparison={'r':256,'prior_uploaded_R331_r256_digest_match':True,'r256_sha256':h256,'count':257,'optional_historical_file_match':None}
    if prior_file:
        prior=json.load(open(prior_file));case=next(x for x in prior['cases'] if x['r']==256)
        provided=[Fraction(x) for x in case['newton_coefficients']]
        assert historical==provided
        prior_comparison['optional_historical_file_match']=True
    return {'schema':'R332_BRC_CORANK_EXTENSION_V1','status':'PASS','input_source':'R331_VERIFY.py at commit 98e7ccce13c07fa91c816314b01f0681dc7c264e',
       'r_interval':[lo,hi],'new_positive_unbounded_bands':hi-lo+1,'new_exact_positive_newton_coefficients':total,
       'source_polynomials_B_s_rows':[0,3*hi+2],'triangular_coefficients_positive':triangle,
       'outside_triangle_negative_retained':outside,'sha256_new_coefficients':h.hexdigest(),'cases':cases,
       'out_of_sample_degree_test':'extra H_r(r+1) exactly agrees with degree<=r interpolation for each new r',
       'historical_overlap_comparison':prior_comparison,
       'infinite_scope_dependency':'R330 exact bivariate rational generating identity establishing deg(H_r)<=r; independent review pending',
       'arithmetic':'Python arbitrary integers and fractions, no floats; signed tails retained',
       'interpretation':'AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--min-r',type=int,default=257);p.add_argument('--max-r',type=int,default=264)
    p.add_argument('--prior-file',default=None,help='Optional full R331 raw evidence for independent vector comparison')
    p.add_argument('--out',default='R332_EXACT_EVIDENCE.json');a=p.parse_args()
    data=check(a.min_r,a.max_r,a.prior_file)
    with open(a.out,'w') as f:json.dump(data,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({k:v for k,v in data.items() if k!='cases'},indent=2))
