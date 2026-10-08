#!/usr/bin/env python3
"""Task-specific exact low-jet regressions; no finite run is a uniform proof.

Arithmetic reuse: Q2 class from the preserved predecessor module, whose SHA256
is 83dd3574edcd55d6b42eba80de17f65c13238fe63dc0fa8d921697d5c90d748d.
Its main scan is never invoked. This file evaluates only p=13 and p=19.
"""
from math import comb
import hashlib
import json
from pathlib import Path
from check_d25_predecessor import Q2

def mul(a,b,n):
    z=Q2(0,0,a[0].m); out=[z for _ in range(n+1)]
    for i in range(min(len(a),n+1)):
        for j in range(min(len(b),n+1-i)):
            out[i+j]=out[i+j]+a[i]*b[j]
    return out

def power_coefficient(a,k,n):
    z=Q2(0,0,a[0].m); v=[z for _ in range(n+1)];v[0]=Q2(1,0,z.m)
    for _ in range(k):v=mul(v,a,n)
    return v[n]

def HJ(n,t,s):
    h=Q2(0,0,t.m);j=Q2(0,0,t.m)
    for k in range(n//3+1):
        c=comb(n-k,k)*comb(n-2*k,n-3*k)
        c=Q2(c,0,t.m).div_scalar(27**k)
        h=h+c*t**k
        if k:j=j+k*c*t**(k-1)
    return h,s*j.div_scalar(4)

def one(p):
    wide=p**4; work=p**3;s=Q2(0,1,wide);t=(2-s).div_scalar(4)
    hj=[HJ(n,t,s) for n in range(p)]
    assert hj[-1][0].a%p==hj[-1][0].b%p==0
    log=[Q2(0,0,work)]
    for n,(h,j) in enumerate(hj,1):
        if n==p:log.append(Q2(h.a//p,h.b//p,work))
        else:log.append(Q2(h.a,h.b,work).div_scalar(n))
    phi=[Q2(0,0,work) for _ in range(p+1)]
    # Formal-group multiplication [-p] is characterized by log(phi)=-p*log.
    for n in range(1,p+1):
        v=-p*log[n]
        for k in range(2,n+1):v=v-log[k]*power_coefficient(phi,k,n)
        phi[n]=v
    for n in range(1,p+1):
        lhs=phi[n]
        for k in range(2,n+1):lhs=lhs+log[k]*power_coefficient(phi,k,n)
        assert lhs.tup()==(-p*log[n]).tup()
        assert phi[n].a%p==phi[n].b%p==0
    rows=[]
    for c in [1,6]:
        bs=[Q2(h.a,h.b,work)+c*Q2(j.a,j.b,work) for h,j in hj]
        composed=Q2(0,0,work)
        for n in range(1,p):
            composed=composed+bs[n-1].div_scalar(n)*power_coefficient(phi,n,p)
        # n=p only uses phi_1^p=(-p)^p. Its divided contribution has
        # valuation at least p-1>=3 and is zero at current precision.
        assert phi[1].tup()==Q2(-p,0,work).tup() and p-1>=3
        defect=composed+bs[-1]
        b0=Q2(bs[-1].a,bs[-1].b,p)
        assert (composed.a%p,composed.b%p)==(0,0)
        assert (defect.a%p,defect.b%p)==b0.tup()
        assert (b0*b0.inv()).tup()==(1,0)
        rows.append({'candidate_c':c,'b_p_minus_1_mod_p':b0.tup(),
                     'composition_coefficient_mod_p':(0,0),
                     'defect_coefficient_mod_p':b0.tup()})
    return {'p':p,'log_identity_through_degree':p,
            'actual_minus_p_jet_coefficients_all_in_pA':True,'candidates':rows}

def main():
    prior=Path(__file__).with_name('check_d25_predecessor.py')
    digest=hashlib.sha256(prior.read_bytes()).hexdigest()
    assert digest=='83dd3574edcd55d6b42eba80de17f65c13238fe63dc0fa8d921697d5c90d748d'
    out={'status':'REGRESSION_ONLY','arithmetic_dependency_sha256':digest,
         'uniform_proof':'D25_LITERAL_DP_EIGENLIFT_OBSTRUCTION.md Sections 1-2',
         'scope':'Actual d=3 curve low jets; c=1,6 are candidate fixtures, not identified source normalizations.',
         'cases':[one(13),one(19)],'failures':0}
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
