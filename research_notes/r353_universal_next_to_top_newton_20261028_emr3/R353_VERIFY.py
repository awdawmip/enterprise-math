#!/usr/bin/env python3
"""R353 author-side exact audit of two universal top Newton differences.
The signed K/J definitions are transcribed from immutable R346_verify.py
blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1.
No native X6 correspondence or independent reviewer role is asserted.
"""
import argparse
import json
from fractions import Fraction
from hashlib import sha256
from math import comb, factorial
from pathlib import Path


def C(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def add(a,b,lim):
    z=[0]*min(lim,max(len(a),len(b)))
    for i,x in enumerate(a[:len(z)]): z[i]+=x
    for i,x in enumerate(b[:len(z)]): z[i]+=x
    return z

def mul(a,b,lim):
    z=[0]*min(lim,len(a)+len(b)-1)
    for i,x in enumerate(a[:len(z)]):
        if x:
            for j,y in enumerate(b[:len(z)-i]):
                if y: z[i+j]+=x*y
    return z

def monomial(n,coef,shift):
    return [0]*shift+[coef*C(n,j) for j in range(n+1)] if n>=0 else [0]

def K(i):
    ds=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    z=[0]
    for j,v in enumerate(ds,1):
        if v: z=add(z,monomial(i+1-j,-v,i-1),30)
    return z

def J(s):
    z=[0]
    for v,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if v: z=add(z,monomial(n,v,s),30)
    return z

def diffs(v):
    a=list(v);out=[]
    while a:
        out.append(a[0]);a=[a[i+1]-a[i] for i in range(len(a)-1)]
    return out

def eval_newton(d,count):
    d=list(d);ans=[]
    for _ in range(count):
        ans.append(d[0])
        for j in range(len(d)-1): d[j]+=d[j+1]
    return ans

def run(max_r=20):
    Hmax=max_r+1; smax=3*Hmax+2;lim=2*Hmax+2
    kk=[None]+[K(i) for i in range(1,13)]
    # Exact, independently read low-order signed polynomial tests
    k_t=[[(i,K(i)[a]) for i in range(1,13) if len(K(i))>a and K(i)[a]] for a in range(4)]
    assert k_t[0]==[(1,2)]
    assert k_t[1]==[(1,3),(2,-1)]
    assert k_t[2]==[(2,4),(3,-8)]
    assert k_t[3]==[(2,4),(3,-8),(4,-11)]
    assert J(1)[:3]==[0,-2,-1]
    assert sum(Fraction(K(i)[3],2**i) for i in (2,3,4))==Fraction(-11,16)
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(s,12)+1): z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
    L={}; H_diffs={}; checked=[]
    for r in range(Hmax+1):
        vals=[]
        for u in range(r+2):
            q=r+u
            D=sum((-1)**(u-w)*C(u,w)*2**(q-w)*B[q+w][q] for w in range(u+1))
            vals.append(Fraction(D,5**u))
        ds=diffs(vals)
        assert ds[-1]==0,('degree',r)
        assert ds[-2]==6**r,('leading',r)
        if r>=1:
            # H_r(u)=a_r*u**r+b_r*u**(r-1)+... ; Newton-to-monomial conversion.
            a=Fraction(ds[-2],factorial(r))
            b=Fraction(ds[-3],factorial(r-1))-a*comb(r,2)
            assert b/a==Fraction(r*(7*r+3),10),('H_second',r,b/a)
        dL=[int(x*5**r) for x in ds[:-1]]
        assert all(Fraction(d)==x*5**r for d,x in zip(dL,ds[:-1]))
        L[r]=eval_newton(dL,2*max_r+3)
        H_diffs[r]=ds[:-1]
    for r in range(1,max_r+1):
        values=[L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1]
                for v in range(2*r+1)]
        d=diffs(values)
        cat=comb(2*r,r)//(r+1)
        expect_top=30**(2*r)*cat
        expect_next=Fraction(17*r+11,10)*expect_top
        assert d[-1]==expect_top,('top',r,d[-1],expect_top)
        assert d[-2]==expect_next,('second',r,d[-2],expect_next)
        assert all(x>0 for x in d),('finite_nonpositive',r)
        assert all(isinstance(x,int) for x in d),('integer',r)
        checked.append({'r':r,'delta_top':str(d[-1]),'delta_next':str(d[-2]),
                        'delta_next_over_top':f'{Fraction(d[-2],d[-1])}',
                        'all_Newton_coefficients_strict_positive':True})
    payload={'schema':'EM_R353_TOP_TWO_NEWTON_V1',
             'kind':'AUTHOR_SIDE_CONDITIONAL_PROOF_WITH_FINITE_EXACT_AUDIT',
             'scope':'12 signed-term ordered-hex BRC auxiliary combinatorial model',
             'conditional_dependency':'R348 (A1-A5), unreviewed',
             'native_X6_correspondence_claim':False,
             'global_snapshot':'awdawmip/chatgpt-global-knowledge@163fdf8de7c64b7144be359707fbcb0fb0e98733',
             'em_source_snapshot':'awdawmip/enterprise-math@1a4ecdf75121035e7613f78598c88c41c930429f',
             'recurrence_sha1_source_blob':'1579ceb717ab1945227eca4f7a1878bf4ffa73e1',
             'smax':smax,'t_degree_range':[0,lim-1],
             'r_tested':[1,max_r], 'count':max_r,
             'all_rational_integers_exact':True,'no_float_signs':True,
             'universal_H_second_ratio':'b_r/a_r=r*(7*r+3)/10, r>=1',
             'universal_Q_next_to_top_ratio':'Delta^(2r-1)Q_r(0)/Delta^(2r)Q_r(0)=(17r+11)/10, r>=1',
             'all_tested_claims_pass':True, 'entries':checked,
             'provenance':'independently transcribed exact signed K/J, full B_s and raw D finite-difference values; same combinatorial source model'
             }
    path=Path(__file__).with_name('R353_EVIDENCE.json')
    path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('R353_PASS',max_r,'smax',smax,'r1_ratio',checked[0]['delta_next_over_top'],
          'rmax_ratio',checked[-1]['delta_next_over_top'],
          'evidence_sha256',sha256(path.read_bytes()).hexdigest())
    return payload
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--max-r',type=int,default=20)
    ns=ap.parse_args()
    assert 1<=ns.max_r<=100
    run(ns.max_r)
