#!/usr/bin/env python3
"""Finite adversarial audit of R348(A1-A5) q<m boundary, not independent peer review.
Computes source coefficients from the signed 12-term BRC polynomial recurrence
and finite formal y-z kernel directly. No floating point sign decisions.
"""
import json,sys
from fractions import Fraction
from pathlib import Path
from math import comb
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul
x,t,y,z=sp.symbols('x t y z')

def polynomial_from_list(lst,symbol):
    return sum(sp.Integer(v)*symbol**j for j,v in enumerate(lst))

def check(maxr=6, maxu=9):
    kval=sp.Poly(sum(polynomial_from_list(K(i),t)*x**i for i in range(1,13)),t)
    aval=sp.Poly(1+t+sum(polynomial_from_list(J(i),t)*x**i for i in range(1,11)),t)
    h=sp.Rational(5,4)
    assert sp.simplify(kval.nth(0)-2*x)==0
    assert sp.simplify(kval.nth(1)-(3*x-x*x))==0
    for a in range(maxr+2):
        fk=kval.nth(a);fa=aval.nth(a)
        if fk!=0:assert sp.degree(fk,x)<=a+1
        if fa!=0:assert sp.degree(fa,x)<=a
    def shift_coeff(f,j):
        return sp.Poly(sp.expand(f.subs(x,(1-y)/2)),y).nth(j) if j>=0 else sp.S.Zero
    N=[]; E=[]
    for j in range(maxr+1):
        N.append(sp.Poly(sp.expand(sum(z**a*shift_coeff(aval.nth(a),j-a) for a in range(j+1))),z))
        E.append(sp.Poly(sp.expand(-sum(z**a*shift_coeff(kval.nth(a),j-a+1) for a in range(j+2))),z))
    assert E[0]==sp.Poly(1-h*z,z)
    assert N[0]==sp.Poly(1,z)
    g=[]
    for r in range(maxr+1):
        v=N[r]*sp.Poly((1-h*z)**r,z)
        for j in range(1,r+1):v-=E[j]*g[r-j]*sp.Poly((1-h*z)**(j-1),z)
        assert v.degree()<=2*r
        g.append(v)
    lim=40;kk=[None]+[K(i) for i in range(1,13)]; B=[[1,1]]
    maxs=maxr+2*maxu
    for s in range(1,maxs+1):
        row=J(s)
        for i in range(1,min(12,s)+1):row=add(row,mul(kk[i],B[s-i],lim),lim)
        B.append(row)
    count=0; q_below_m_terms=0; zeros_witnessed=0
    for r in range(maxr+1):
        for u in range(maxu+1):
            q=r+u
            direct=sum((-1)**(u-w)*C(u,w)*2**(q-w)*B[q+w][q] for w in range(u+1))
            val=sp.S.Zero
            for j in range(r+1):
                for (m,),gcoef in g[j].terms():
                    # For q<m, the coefficient z^(q-m) is absent. The
                    # actual binomial upper q-m+j must be between 0 and j-1.
                    if q<m:
                        q_below_m_terms+=1
                        upper=q-m+j
                        assert 0<=upper<j,('R348_boundary_fail',r,u,j,m,q,upper)
                        assert sp.binomial(upper,j)==0
                        zeros_witnessed+=1
                        continue
                    term=gcoef*sp.Integer(5)**(r-m)*sp.Integer(4)**m*sp.binomial(q-m+j,j)*sp.binomial(2*q-j,r-j)
                    val+=term
            predicted=5**u*val
            assert sp.simplify(predicted-direct)==0,(r,u, predicted,direct)
            count+=1
    ev={ 'schema':'R356_R348_FORMAL_EXTRACTION_BOUNDARY_FINITE_AUDIT_V1',
         'max_r':maxr, 'max_u':maxu, 'compared_r_u_pairs':count,
         'q_lt_m_terms_explicitly_checked':q_below_m_terms,
         'boundary_zero_terms_verified':zeros_witnessed,
         'g_degree_bound_through_r':maxr,
         'signed_KJ_recurrence':True, 'precision':'exact_sympy_rational_integer',
         'result':'PASS',
         'scope':'finite audit only; mathematical all-index R348 proof requires independent reviewer and native X6 transfer remains open' }
    (HERE/'R356_R348_AUDIT_EVIDENCE.json').write_text(json.dumps(ev,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(ev,ensure_ascii=False))
    return ev
if __name__=='__main__':check()
