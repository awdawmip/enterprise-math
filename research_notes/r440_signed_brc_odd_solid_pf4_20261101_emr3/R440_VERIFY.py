#!/usr/bin/env python3
"""R440 exact signed-BRC contiguous-minor classification, odd r>=5.

All signs use unbounded Python integers.  Recomputes original signed H
independently by Catalan coefficients and both Bareiss and Leibniz.
The infinite r>=99 step uses the explicitly proved polynomial identity.
"""
from __future__ import annotations
from itertools import permutations
from functools import reduce
from math import comb, gcd
from hashlib import sha256
from fractions import Fraction
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def B(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0

def cat(k):
    return comb(2*k,k)//(k+1) if k>=0 else 0

def H_raw(r,s):
    if not (2<=s<=r): return 0
    delta=sum(B(r-s,q)*(B(2*s,r-2*q)-B(2*s,r-2*q-1)) for q in range(r-s+1))
    return B(r+s,2*s)*delta

def H_cat_odd(r,s):
    if not (r%2==1 and 2<=s<=r):return 0
    k=(r-1)//2
    return B(r+s,2*s)*sum(B(s-1,2*q)*4**q*cat(k-q) for q in range(k+1))

def det_bareiss(mat):
    n=len(mat)
    if n==1:return mat[0][0]
    a=[list(row) for row in mat]
    prev=1; sign=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]!=0),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0,(n,k,i,j)
                a[i][j]=num//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def det_leibniz(mat):
    n=len(mat); total=0
    for p in permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        v=(-1 if inversions&1 else 1)
        for i,j in enumerate(p):v*=mat[i][j]
        total+=v
    return total

def polynomial_P(k):
    return (7936*k**7-309248*k**6-3408516*k**5-14300148*k**4
            -33616293*k**3-46354824*k**2-35761465*k-11787442)

def run():
    digest=sha256(); cross=0; minors=0; pos=0; neg=0; zero=0
    by_r=[]; exceptions=[]; r99_scaled=None; r99_original=None
    for r in range(5,100,2):
        raw=[H_raw(r,s) for s in range(2,r+1)]
        alt=[H_cat_odd(r,s) for s in range(2,r+1)]
        assert raw==alt,(r,'Catalan disagreement')
        assert all(x>0 for x in raw),(r,'nonpositive H')
        cross+=len(raw)
        g=reduce(gcd,raw)
        a=[H_raw(r,r-h)//g for h in range(r-1)]
        n=r-2
        per_order=[]; failures=[]
        for p in range(1,5):
            counts={'positive':0,'negative':0,'zero':0}
            for d in range(n+1):
                M=[[a[d+j-i] if 0<=d+j-i<=n else 0 for j in range(p)] for i in range(p)]
                D=det_bareiss(M)
                assert D==det_leibniz(M),(r,p,d,'det-method disagreement')
                sgn=(D>0)-(D<0)
                counts['positive' if sgn>0 else 'negative' if sgn<0 else 'zero']+=1
                minors+=1;pos+=(sgn>0);neg+=(sgn<0);zero+=(sgn==0)
                digest.update(f'{r}/{p}/{d}/{D}\n'.encode())
                if sgn<=0:
                    failures.append({'p':p,'d':d,'det_normalized':str(D)})
                    exceptions.append({'r':r,'p':p,'d':d,'det_normalized':str(D)})
                if (r,p,d)==(99,4,96):
                    r99_scaled=D;r99_original=D*(g**4)
            per_order.append(counts)
        if 7<=r<=97:assert not failures,(r,failures[:2])
        if r==5:assert len(failures)==1 and failures[0]['p']==4 and failures[0]['d']==1
        if r==99:assert len(failures)==1 and failures[0]['p']==4 and failures[0]['d']==96
        by_r.append({'r':r,'gcd':str(g),'support_length':len(a),'by_order':per_order,
                     'exceptions':failures})
    assert (cross,minors,pos,neg,zero)==(2448,9792,9790,2,0)
    assert polynomial_P(48)==-71552034705250
    assert polynomial_P(49)==52661023196976
    B99=H_raw(99,2)
    assert Fraction(r99_original,B99**4)==Fraction(-((49+2)*polynomial_P(49)),436590000)
    record={
        'schema':'EM_R440_SIGNED_BRC_ODD_SOLID_PF4_V1',
        'status':'R440_EXACT_PASS / AUTHOR_SIDE_UNREVIEWED / NOT_ADMITTED',
        'date':'2026-11-01',
        'global_knowledge_read_commit':'bc1bcc8e37542f6acf0042cd9671ab44696adcc7',
        'em_current_control_read_commit':'42da097851a02b96f8ff2018f5c28096eec13866',
        'prior_math':'R432 analytic odd r>=99 obstruction at immutable 83a97192b7e2bb5cc7e741b005d36bca9632a653',
        'claim':'For odd r>=5, every solid Toeplitz minor of order <=4 is nonnegative iff 7<=r<=97; all 9384 in-support minors strictly positive. Not PF4 classification.',
        'proof_partition':'r=5 explicit negative; odd r=7..97 exhaustive 9384 exact checks; odd r>=99 R432 analytic 4x4 negative.',
        'coeff_crosschecks':cross,'solid_minors_checked':minors,
        'positive':pos,'negative':neg,'zero':zero,
        'finite_positive_odd_rows':46,'finite_positive_count':9384,
        'negative_exceptions':exceptions,
        'r99_R432_P_48':str(polynomial_P(48)),
        'r99_R432_P_49':str(polynomial_P(49)),
        'r99_analytic_ratio_verified':True,
        'r99_raw_negative_det':str(r99_original),
        'full_determinant_transcript_sha256':digest.hexdigest(),
        'by_row':by_r,
        'scope':'Consecutive row AND column sets, orders 1..4; no global PF4 inference for r>=29',
        'next':'r29 sparse minor PF4 classification or negative witness'
    }
    out=HERE/'R440_EVIDENCE.json'
    out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('R440_EXACT_PASS','coefficient_crosschecks',cross,'solid_minors',minors,
          'positive',pos,'negative',neg,'zero',zero,'all_odd_7_97_positive',9384,
          'sha256',digest.hexdigest())
    print('NEGATIVE_EXCEPTIONS',[(x['r'],x['p'],x['d']) for x in exceptions])
    print('R99_ANALYTIC_RATIO_MATCH',record['r99_analytic_ratio_verified'])
    return record

if __name__=='__main__':run()
