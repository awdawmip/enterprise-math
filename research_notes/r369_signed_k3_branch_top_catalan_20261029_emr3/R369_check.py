#!/usr/bin/env python3
"""R369: signed K3 t^2 branch deformation, exact infinite top formula + finite tests.

Run from Enterprise Math PR checkout:
 python research_notes/r369_signed_k3_branch_top_catalan_20261029_emr3/R369_check.py

Imports the original twelve signed K_i and J_s from the R346 PR source;
no archived coefficient CSV or historical ZIP is needed.
"""
from __future__ import annotations
import sys,json,hashlib
from fractions import Fraction
from pathlib import Path
from math import comb
from sympy import Symbol, Rational, expand, factor, Poly
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import C,K,J,add,mul,forward_differences as fd,eval_newton

TH=Symbol('theta')
VALUES=(Fraction(0),Fraction(1),Fraction(5,4),Fraction(15,8),Fraction(3))

def compute_rows(theta, maxr):
    """Exact original signed 12-term recurrence with only K3 t^2 shifted.

    The coefficient -8 of x^3*t^2 is replaced by -8*(1+theta).
    The original K and J are otherwise unchanged.
    """
    smax=3*(maxr+2)+2
    lim=2*(maxr+1)+6
    kernels=[None]+[K(i) for i in range(1,13)]
    assert kernels[3][2]==-8
    kernels[3][2]-=8*theta
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(s,12)+1):
            z=add(z,mul(kernels[i],B[s-i],lim),lim)
        B.append(z)
    def D(q,k):
        return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))
    L=[]
    for r in range(maxr+2):
        ds=fd([D(r+u,u)*Rational(1,5**u) for u in range(r+2)])
        assert expand(ds[-1])==0, ('degree bound finite check',theta,r)
        L.append(eval_newton([expand(x*5**r) for x in ds[:-1]],2*maxr+5))
    rows={}
    for r in range(1,maxr+1):
        qv=[expand(L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1])
            for v in range(2*r+1)]
        cv=[expand(v) for v in fd(qv)]
        assert len(cv)==2*r+1
        rows[r]=cv
    return rows,D

def main():
    # All-symbol exact 3-jet at corank r=1, from unmodified original K/J code.
    sym, Dsym=compute_rows(TH,1)
    c=[factor(x) for x in sym[1]]
    expected=[512*TH**2-2400*TH+2620,768*TH**2-2880*TH+2520,(30-16*TH)**2]
    assert all(expand(c[j]-expected[j])==0 for j in range(3)),(c,expected)
    # Crucial independent raw-D symbolic three-jet comparison; relies on no
    # extrapolation from three polynomial interpolation samples.
    raw_q=[]
    for k in (1,2,3):
        q=1+k
        M=Dsym(q,k)*Dsym(q+1,k+1)-Dsym(q,k+1)*Dsym(q+1,k)
        raw_q.append(expand(M*Rational(5**2,5**(2*k+1))))
    raw_newton=fd(raw_q)
    assert all(expand(raw_newton[j]-expected[j])==0 for j in range(3)),raw_newton
    examples={}
    for x in VALUES:
        row=[Fraction(t.subs(TH,x)) for t in c]
        turan=row[1]**2-row[0]*row[2]
        ulc=row[1]**2-4*row[0]*row[2]
        examples[str(x)]={'r1_newton_coefficients':[str(t) for t in row],
                           'ordinary_turan_defect':str(turan),
                           'ULC_defect':str(ulc),
                           'positive':all(z>0 for z in row)}
    assert examples['0']['r1_newton_coefficients']==['2620','2520','900']
    assert examples['0']['ordinary_turan_defect']=='3992400'
    assert examples['0']['ULC_defect']=='-3081600'
    assert examples['5/4']['r1_newton_coefficients']==['420','120','100']
    assert examples['5/4']['ordinary_turan_defect']=='-27600'
    assert examples['3']['r1_newton_coefficients']==['28','792','324']
    assert examples['3']['ULC_defect']=='590976'
    assert examples['15/8']['r1_newton_coefficients']==['-80','-180','0']

    # Independent finite direct-recurrence samples, q=0..10, no interpolation.
    # Verify every highest Newton coefficient against the universal formula.
    samples={}
    for t in VALUES:
        rows,D=compute_rows(t,10)
        one={}
        top_ok=0
        for r,coeff in rows.items():
            target=Fraction((30-16*t)**(2*r)*comb(2*r,r),r+1)
            assert coeff[-1]==target,(t,r,coeff[-1],target)
            top_ok+=1
        # Cross-check exact raw D minors at r=1 for several k:
        raw_ok=0
        for k in (1,2,3,4):
            q=k+1
            minor=D(q,k)*D(q+1,k+1)-D(q,k+1)*D(q+1,k)
            qpoly=sum(coeff*comb(k-1,j) for j,coeff in enumerate(rows[1]))
            assert minor==Fraction(5**(2*k+1),5**2)*qpoly,(t,k)
            raw_ok+=1
        one['top_catalan_checks']=top_ok
        one['direct_D_minor_identity_checks']=raw_ok
        one['top_r10']=str(rows[10][-1])
        samples[str(t)]=one

    out={
       'schema':'EM_R369_SIGNED_K3_TOP_CATALAN_V1',
       'date':'2026-10-29',
       'source_kernel':'original R346 signed 12-term K and J; only K3[t^2] = -8*(1+theta)',
       'theta_symbolic_jets_r1':[str(factor(v)) for v in expected],
       'all_r_conditional_formula':'Delta^(2r) Q_{theta,r}(0) = Catalan(r) * (30-16*theta)^(2r), r>=1, conditional on R363 all-index formal extraction and degree',
       'top_zero_parameter':'15/8',
       'r1_finite_unconditional_examples':examples,
       'finite_exact_checks_by_theta':samples,
       'symbolic_formula_checks':3,
       'symbolic_raw_D_minor_checks':3,
       'independent_finite_top_checks':len(samples)*10,
       'raw_D_minor_checks':len(samples)*4,
       'arithmetic':'integer, exact rational and symbolic polynomial; no floating signs',
       'classification':'AUTHOR_SIDE_EXACT / CONDITIONAL_ALL_R / EXACT_R1_COUNTEREXAMPLES / DRIVER_UNREVIEWED / NOT_ADMITTED',
       'native_x6':'no state embedding or dynamics transfer proven'
    }
    path=HERE/'R369_EVIDENCE.json'
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('R369_EXACT_PASS',json.dumps({
       'symbolic_r1':out['theta_symbolic_jets_r1'],
       'samples':out['finite_exact_checks_by_theta'],
       'r1_examples':examples,
       'evidence_sha256':hashlib.sha256(path.read_bytes()).hexdigest()
    },ensure_ascii=False))
    return out

if __name__=='__main__':main()
