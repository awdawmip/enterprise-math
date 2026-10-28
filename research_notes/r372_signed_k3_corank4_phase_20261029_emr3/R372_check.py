#!/usr/bin/env python3
"""R372 exact corank-4 phase, original signed BRC K/J, Bernstein proof.

Run from PR #1592 checkout (SymPy required):
  python research_notes/r372_signed_k3_corank4_phase_20261029_emr3/R372_check.py
This independently evaluates raw D determinants as integer polynomials in theta;
no Q interpolation or R348/R363 all-index degree theorem is invoked.
"""
from __future__ import annotations
import hashlib
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path
from sympy import Symbol, Poly, Rational, binomial, expand, diff

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J

x=Symbol('theta')
rat=lambda n:Rational(n,1000)

def trim(z):
    z=list(z)
    while z and z[-1]==0:z.pop()
    return tuple(z)

def padd(a,b):
    return trim((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                for i in range(max(len(a),len(b))))

def pmul(a,b):
    if not a or not b:return ()
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return trim(out)

def pscale(a,v):return trim(t*v for t in a)

def raw_c4():
    """Compute nine finite c_j(theta) from D(q,k), as exact theta-polynomial arrays."""
    smax,tcap=24,14
    kernels=[None]+[[((int(z),) if z else ()) for z in K(i)[:tcap+1]] for i in range(1,13)]
    assert kernels[3][2]==(-8,)
    kernels[3][2]=(-8,-8)  # only changed signed K3[t^2] branch
    B=[[() for _ in range(tcap+1)] for _ in range(smax+1)]
    B[0][0]=(1,); B[0][1]=(1,)
    for s in range(1,smax+1):
        js=J(s)
        for p in range(min(len(js),tcap+1)):
            if js[p]:B[s][p]=(int(js[p]),)
        for i in range(1,min(12,s)+1):
            for j,ki in enumerate(kernels[i]):
                if j>tcap:break
                if not ki:continue
                for p in range(j,tcap+1):
                    if B[s-i][p-j]:
                        B[s][p]=padd(B[s][p],pmul(ki,B[s-i][p-j]))
    def D(q,k):
        z=()
        for w in range(k+1):
            z=padd(z,pscale(B[q+w][q],(-1)**(k-w)*comb(k,w)*2**(q-w)))
        return z
    raw=[]
    for v in range(9):
        k=v+1;q=4+k
        M=padd(pmul(D(q,k),D(q+1,k+1)),pscale(pmul(D(q,k+1),D(q+1,k)),-1))
        raw.append(pscale(M,Fraction(5)**(7-2*k)))
    a=raw
    coeff=[]
    while a:
        coeff.append(a[0]);a=[padd(a[i+1],pscale(a[i],-1)) for i in range(len(a)-1)]
    return coeff,raw

def bernstein_cert(p,lo,hi):
    """All Bernstein coefficients b_k of p on [lo,hi] strictly positive.

    Let p(lo+(hi-lo)y)=sum a_i*y^i. Then b_k =
    sum_{i<=k} a_i*binom(k,i)/binom(n,i), with p on [0,1]
    represented by sum b_k*binom(n,k)y^k(1-y)^(n-k).
    """
    lo,hi=Rational(lo),Rational(hi)
    assert lo<hi
    P=Poly(p,x,domain='QQ').shift(lo)
    n=P.degree()
    a=[v*(hi-lo)**i for i,v in enumerate(reversed(P.all_coeffs()))]
    bs=[sum(a[i]*Rational(binomial(k,i),binomial(n,i)) for i in range(k+1))
        for k in range(n+1)]
    assert all(z>0 for z in bs), ('not strictly certified',str(lo),str(hi))
    return n+1

def run():
    theta_poly,raw=raw_c4()
    assert len(theta_poly)==9 and len(raw)==9
    c=[expand(sum(Rational(v.numerator,v.denominator)*x**i if isinstance(v,Fraction)
                   else int(v)*x**i for i,v in enumerate(p))) for p in theta_poly]
    assert all(all(isinstance(v,(int,Fraction)) and v.denominator==1 if isinstance(v,Fraction) else True for v in p)
               for p in theta_poly)
    assert [Poly(q,x).degree() for q in c]==[4,6,7,8,8,8,8,8,8]
    T=[expand(c[j]**2-c[j-1]*c[j+1]) for j in range(1,8)]
    U1=expand(7*c[1]**2-16*c[0]*c[2])
    a,b=rat(1469),rat(1470)
    lo,hi=rat(1710),rat(1711)
    crossover=Rational(9,4)
    cert={}
    for j,p in enumerate(c):cert[f'c{j}_positive']=bernstein_cert(p,-1,b)
    for j,p in enumerate(T[1:],2):cert[f'T{j}_positive']=bernstein_cert(p,-1,b)
    cert['U1_negative']=bernstein_cert(-U1,-1,b)
    cert['T1_positive_left']=bernstein_cert(T[0],-1,a)
    cert['T1_negative_right']=bernstein_cert(-T[0],b,hi)
    cert['T1_negative_derivative_root']=bernstein_cert(-diff(T[0],x),a,b)
    cert['c1_positive_left']=bernstein_cert(c[1],-1,lo)
    cert['c1_negative_right']=bernstein_cert(-c[1],hi,crossover)
    cert['c1_negative_derivative_root']=bernstein_cert(-diff(c[1],x),lo,hi)
    assert len(cert)==22
    tail=list(reversed(Poly(-c[0],x,domain='QQ').shift(crossover).all_coeffs()))
    assert tail==[1351200000,368160000000,1224192000000,1398784000000,3276800000]
    assert expand(c[8]-14*(30-16*x)**8)==0
    base=[int(q.subs(x,0)) for q in c]
    assert base==[10478580000000,74179222880000,250257279520000,
                  494571650400000,618103193760000,497471220000000,
                  251096760000000,72564660000000,9185400000000]
    out={
      'schema':'EM_R372_SIGNED_K3_CORANK4_EXACT_BERNSTEIN_V1',
      'source':'Original signed 12-branch K/J from R346; independent direct raw D determinant polynomial arithmetic',
      'parameter':'theta>-1, K3[t^2]=-8*(1+theta), all other K/J unchanged',
      'corank':4,'raw_D_polynomial_determinants':9,
      'coefficient_degrees':[4,6,7,8,8,8,8,8,8],
      'coefficients_at_theta0':list(map(str,base)),
      'coefficients_polynomials':[str(Poly(p,x).as_expr()) for p in c],
      'Turan_polynomials':[str(Poly(p,x).as_expr()) for p in T],
      'ULC1_polynomial':str(Poly(U1,x).as_expr()),
      'positive_Bernstein_certificates':cert,
      'bernstein_intervals':{
       'c0_through_c8,T2_through_T7,minus_U1':'[-1,1470/1000]',
       'T1_positive_left':'[-1,1469/1000]',
       'minus_T1_positive_right':'[1470/1000,1711/1000]',
       'minus_T1_prime_positive':'[1469/1000,1470/1000]',
       'c1_positive_left':'[-1,1710/1000]',
       'minus_c1_positive_right':'[1711/1000,9/4]',
       'minus_c1_prime_positive':'[1710/1000,1711/1000]'
      },
      'minus_c0_shift_theta_minus_9over4_coefficients_ascending':list(map(str,tail)),
      'sigma4':'unique zero of T1=c1^2-c0*c2 in (1469/1000,1470/1000)',
      'rho4':'unique zero of c1 in (1710/1000,1711/1000)',
      'r4_PF2':'iff -1<theta<=sigma4, including T1=0 boundary',
      'r4_PFinfty':'never on theta>-1, because U1<0 where PF2 holds',
      'joint_r1_to_r4_PF2':'iff -1<theta<=tau1 (R370, tau1 in (1.054,1.055))',
      'all_Q_indices':'conditional on independent audit of R348/R363 extraction and degree bound',
      'arithmetic':'exact integer/rational polynomial array recurrence, direct raw-D minors, symbolic Bernstein positivity',
      'status':'AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED / NATIVE_X6_TRANSFER_OPEN'
    }
    dest=HERE/'R372_EVIDENCE.json'
    dest.write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('R372_EXACT_PASS')
    print(json.dumps({'raw_D_determinants':9,'Bernstein_certificates':len(cert),
     'r4_PF2':out['r4_PF2'],'r4_PFinfty':out['r4_PFinfty'],
     'sha256_evidence':hashlib.sha256(dest.read_bytes()).hexdigest()},indent=2))
    return out

if __name__=='__main__':run()
