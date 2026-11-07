#!/usr/bin/env python3
"""R348: independent finite algebra spot-check for a UNIVERSAL formal kernel proof.
Tests small r,u against original signed K/J recurrence. The mathematical
infinite-index proof resides in R348_PROOF.zh-CN.md; this is not its substitute.
"""
import json
from fractions import Fraction
from math import comb
from pathlib import Path
import sympy as sp
from R348_verify import C,K,J,add,mul

x,t,y,z,q=sp.symbols('x t y z q')
h=sp.Rational(5,4)

def ki(i):
    return sp.expand(sum(v*t**j for j,v in enumerate(K(i)) if v))
def js(s):
    return sp.expand(sum(v*t**j for j,v in enumerate(J(s)) if v))

def compute(maxr=5):
    Kp=sp.Poly(sum(ki(i)*x**i for i in range(1,13)),t)
    Ap=sp.Poly(1+t+sum(js(s)*x**s for s in range(1,11)),t)
    assert sp.expand(Kp.nth(0)-2*x)==0
    assert sp.expand(Kp.nth(1)-(3*x-x*x))==0
    for a in range(maxr+2):
        assert sp.degree(Kp.nth(a),x) <= a+1 if Kp.nth(a)!=0 else True
        assert sp.degree(Ap.nth(a),x) <= a if Ap.nth(a)!=0 else True
    def yc(f,k):return sp.Poly(sp.expand(f.subs(x,(1-y)/2)),y).nth(k) if k>=0 else sp.Integer(0)
    N=[];E=[]
    for j in range(maxr+1):
        N.append(sp.Poly(sp.expand(sum(z**a*yc(Ap.nth(a),j-a) for a in range(j+1))),z))
        E.append(sp.Poly(sp.expand(-sum(z**a*yc(Kp.nth(a),j-a+1) for a in range(j+2))),z))
    assert E[0]==sp.Poly(1-h*z,z)
    assert N[0]==sp.Poly(1,z)
    g=[]
    for r in range(maxr+1):
        gr=N[r]*sp.Poly((1-h*z)**r,z)
        for j in range(1,r+1):
            gr-=E[j]*g[r-j]*sp.Poly((1-h*z)**(j-1),z)
        assert gr.degree() <= 2*r
        g.append(gr)

    lim=35
    kk=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,28):
        B.append(J(s))
        for i in range(1,min(12,s)+1):B[-1]=add(B[-1],mul(kk[i],B[s-i],lim),lim)

    count=0; cert=[]
    for r in range(maxr+1):
        for u in range(9):
            qq=r+u
            direct=sum((-1)**(u-w)*C(u,w)*2**(qq-w)*B[qq+w][qq] for w in range(u+1))
            symbolic=sp.Integer(0)
            for j in range(r+1):
                for (m,),v in g[j].terms():
                    # binom as falling polynomials, not generalized binomial outside the valid q range
                    bin1=sp.prod(qq-m+j-hh for hh in range(j))/sp.factorial(j)
                    bin2=sp.prod(2*qq-j-hh for hh in range(r-j))/sp.factorial(r-j)
                    symbolic+=v*sp.Integer(5)**(r-m)*sp.Integer(4)**m*bin1*bin2
            predicted=sp.Integer(5)**u*symbolic
            assert sp.simplify(predicted-direct)==0,(r,u,predicted,direct)
            count+=1
        cert.append({'r':r,'g_degree':g[r].degree(),'expected_upper_bound':2*r,'g_constant':str(g[r].nth(0))})
    return {'schema':'R348_KERNEL_FORMAL_PROOF_FINITE_SPOTCHECK_V1','max_r':maxr,
      'samples_compared':count, 'finite_raw_D_agreement':True,
      'K_t0':'2x','K_t1':'3x-x^2','E0':'1-5z/4',
      'E_polynomial_degree_bounds_checked':maxr+1,
      'N_polynomial_degree_bounds_checked':maxr+1,
      'g_degree_bounds_checked':cert,
      'note':'Finite checks only; unbounded result uses exact formal series proof in PROOF.md.'}

if __name__=='__main__':
    result=compute()
    loc=Path(__file__).parent
    (loc/'R348_KERNEL_EVIDENCE.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result,ensure_ascii=False))
