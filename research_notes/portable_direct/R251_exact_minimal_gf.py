#!/usr/bin/env python3
"""R251: build exact minimal scalar rational GF from 63 rank-one mask blocks.

Frozen R234–R250 seven-source sticky-reset auxiliary observer. SymPy QQ,
no floating-point arithmetic. Does not assert any native X6/BRC port quotient.
"""
from __future__ import annotations
import json, hashlib, time
from pathlib import Path
import sympy as S
import R250_common_eigenvalue_certificate as R

z=S.Symbol('z')
ZERO=S.Poly(0,z,domain=S.QQ)
ONE=S.Poly(1,z,domain=S.QQ)
W=[144,576,1440,4320,17280,86400,518400]

def block(j, mask):
    _,a,b,pi=R.setup_parameter(j)
    ix=R.indices(mask)
    Z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(Z*(1-a[i])**2) for i in range(7)]
    d=len(ix)
    qx=R.poly_for_mask(mask,a,b)
    qz=S.Poly(sum(c*z**k for k,c in enumerate(qx.all_coeffs())),z,domain=S.QQ)
    assert qz.nth(0)==1 and qz.degree()==d
    # Weighted first d coefficients h_k=W*rho^T P_D^k 1 (k=0..d-1)
    v={i:S.S.One for i in ix}; h=[]
    for k in range(d):
        h.append(W[mask.bit_count()]*sum(rho[i]*v[i] for i in ix))
        m=sum(pi[i]*v[i] for i in ix)
        v={i:a[i]*v[i]+(1-a[i])*m for i in ix}
    num=S.Poly(sum(sum(qz.nth(t)*h[k-t] for t in range(k+1))*z**k for k in range(d)),z,domain=S.QQ)
    assert num.degree()<d
    return qz,num

def coefficients(polyP,polyQ,N):
    d=polyQ.degree(); p=[polyP.nth(k) if k<=polyP.degree() else S.S.Zero for k in range(N)]
    out=[]
    for k in range(N):
        c=p[k]-sum(polyQ.nth(t)*out[k-t] for t in range(1,min(d,k)+1))
        out.append(c)
    return out

def direct(j,N):
    _,a,b,pi=R.setup_parameter(j)
    Z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(Z*(1-a[i])**2) for i in range(7)]
    total=[S.S.Zero for _ in range(N)]
    for mask in range(63):
        ix=R.indices(mask)
        v={i:S.S.One for i in ix}
        for k in range(N):
            total[k]+=W[mask.bit_count()]*sum(rho[i]*v[i] for i in ix)
            m=sum(pi[i]*v[i] for i in ix)
            v={i:a[i]*v[i]+(1-a[i])*m for i in ix}
    return total

def main():
    t=time.monotonic()
    j=400
    blocks=[block(j,m) for m in range(63)]
    Q=ONE
    for den,num in blocks:
        Q=S.lcm(Q,den)
    Q=Q.mul_ground(1/Q.nth(0))
    assert Q.nth(0)==1, Q.nth(0)
    assert Q.degree()==229, Q.degree()
    print('LCM 63 mask characteristic reversals: degree',Q.degree(),'time',round(time.monotonic()-t,2),flush=True)
    P=ZERO
    for den,num in blocks:
        P+=num*Q.exquo(den)
    assert P.degree()<Q.degree(),P.degree()
    assert S.gcd(P,Q).degree()==0
    print('Numerator degree',P.degree(),'gcd degree',S.gcd(P,Q).degree(),'time',round(time.monotonic()-t,2),flush=True)
    verifyN=235
    cg=coefficients(P,Q,verifyN)
    cd=direct(j,verifyN)
    assert cg==cd
    print('Exact generating-function/direct 235 consecutive coefficients match; time',round(time.monotonic()-t,2),flush=True)
    # Final recurrence check at k=229..234 and the initial scalar data.
    assert all(sum(Q.nth(t)*cd[k-t] for t in range(Q.degree()+1))==0 for k in range(229,235))
    result={
     'schema':'ENTERPRISE_MATH_R251_EXACT_MINIMAL_GENERATING_FUNCTION_V1',
     'source_commit_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
     'r250_published_commit':'acb90adc07ec249069e3662140a8a53e794db615',
     'parameter':'s=2/5','subsets':63,'unreduced_modes':249,
     'minimal_denominator_degree':Q.degree(),'numerator_degree':P.degree(),
     'gcd_degree':S.gcd(P,Q).degree(),
     'numerator_constant':str(P.nth(0)),'denominator_constant':str(Q.nth(0)),
     'checked_direct_coefficients':verifyN,'checked_recursion_indices':'k=229..234',
     'exact_agreement':True,'arithmetic':'SymPy QQ rank-one mask propagation and polynomial LCM / division / Euclidean GCD',
     'claim_scope':'single rational anchor s=2/5; all-parameter polynomial formula proved symbolically in companion note',
     'q_coefficient_sha256':hashlib.sha256(json.dumps([str(Q.nth(k)) for k in range(230)],separators=(',',':')).encode()).hexdigest(),
     'p_coefficient_sha256':hashlib.sha256(json.dumps([str(P.nth(k)) for k in range(229)],separators=(',',':')).encode()).hexdigest(),
     'first_5_scalar_coefficients':[str(x) for x in cd[:5]],
     'all_pass':True
    }
    path=Path(__file__).with_name('R251_verification.json')
    path.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print('PASS',path,'SHA256',hashlib.sha256(path.read_bytes()).hexdigest(), 'total time',round(time.monotonic()-t,2),flush=True)
if __name__=='__main__':main()
