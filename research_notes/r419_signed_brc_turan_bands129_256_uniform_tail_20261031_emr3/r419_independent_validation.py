#!/usr/bin/env python3
"""Independent raw signed coefficient and Catalan check of R419 generator evidence.
Does not import R419 generator or its polynomial routines.
"""
import json, hashlib
from math import comb
from pathlib import Path
root=Path(__file__).parent
p=root/'R419_FULL_EVIDENCE_129_256.json'
obj=json.loads(p.read_text(encoding='utf8'))
assert obj['range']==[129,256]
rows={(int(z['s']),int(z['epsilon'])):z for z in obj['rows']}
assert len(rows)==256

def cat(n):return comb(2*n,n)//(n+1)
def choose(n,k):return comb(n,k) if 0<=k<=n else 0

def raw_delta(r,q):
    # Expand (1+t^2)^(r-q), then (1-t)(1+t)^(2q)
    return sum(comb(r-q,k)*(choose(2*q,r-2*k)-choose(2*q,r-2*k-1)) for k in range(r-q+1))

def cat_delta(r,q):
    # Entirely different expression than raw; derived from Catalan convolution
    return sum(comb(q-1,j)*2**(q-1-j)*cat((r-q+j)//2)
               for j in range(q) if r-q+j>=0 and (r-q+j)%2==0)

def ev(coeff,x):
    y=0
    for c in reversed(coeff):y=y*x+int(c)
    return y
raw_checks=kernel_checks=polynomial_checks=0
for s in [129,130,160,192,224,256]:
    for eps in [0,1]:
        row=rows[s,eps]
        r0=int(row['r0'])
        A=row['A_coefficients_ascending'];B=row['B_coefficients_ascending']
        assert len(A)==len(B)==int(row['A_degree'])+1
        assert all(int(v)>0 for v in A+B)
        for x in [0,1,2,5,13,63,127]:
            r=r0+2*x
            vals=[]
            for q in [s-1,s,s+1]:
                d=raw_delta(r,q)
                assert d==cat_delta(r,q),(s,eps,x,q)
                raw_checks+=1;kernel_checks+=1
                vals.append(comb(r+q,2*q)*d)
            D=vals[1]**2-vals[0]*vals[2]
            c=comb(r+s,2*s)*cat(int(row['b0'])+x)
            assert D>0 and D*ev(B,x)==c*c*ev(A,x),(s,eps,x)
            polynomial_checks+=1
# Check all coefficient hashes and published summary digests without generator import.
summary=json.loads((root/'R419_EVIDENCE_SUMMARY_129_256.json').read_text())
assert summary['raw_evidence_sha256']==hashlib.sha256(p.read_bytes()).hexdigest()
positive=0
for r, m in zip(obj['rows'], summary['case_digests']):
    assert r['s']==m['s'] and r['epsilon']==m['epsilon']
    for letter in ['A','B']:
        seq=r[f'{letter}_coefficients_ascending']
        assert len(seq)==r[f'positive_{"numerator" if letter=="A" else "denominator"}_coefficients']
        assert all(int(z)>0 for z in seq)
        hash_val=hashlib.sha256(','.join(seq).encode()).hexdigest()
        assert hash_val==r[f'{letter}_sha256']==m[f'{letter}_sha256']
    positive+=len(r['A_coefficients_ascending'])
assert positive==summary['positive_numerator_coefficients']==summary['positive_denominator_coefficients']==49792
# Pure integer check of analytic sufficient-bound inequality (not a proof of all integers).
for s in range(7,513):
    delta_num=8*s+2;delta_den=(2*s+2)*(2*s+1)
    assert 3*s*delta_den < (2*s*s-s-1)*delta_num
print('R419_INDEPENDENT_PASS','parity_cases',256,'coefficients_per_sign',positive,
      'raw_delta_and_Catalan_pairs',raw_checks,'polynomial_identity_pairs',polynomial_checks,
      'analytic_bound_test_s7_to512',506)
print('SOURCE_SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
