#!/usr/bin/env python3
"""Exact symbolic certificate for highest two H_r Newton coefficients.
Assumes the separately documented R330 rational coefficient-extraction lemma.
"""
import argparse,json
from fractions import Fraction
import sympy as S
from R333_VERIFY import K,J,build,dh_values,diffs

def run(max_r=32):
    y,z=S.symbols('y z'); a=S.Rational(4,5)
    x=(1-y)/2;t=y*z
    Ktot=sum(sum(S.Integer(c)*t**k for k,c in enumerate(K(i)))*x**i for i in range(1,13))
    A=sum(S.Integer(c)*t**k for k,c in enumerate([1,1]))+sum(sum(S.Integer(c)*t**k for k,c in enumerate(J(i)))*x**i for i in range(1,11))
    Kpoly=S.Poly(S.expand(Ktot),y);Apoly=S.Poly(S.expand(A),y)
    E=[S.factor(-Kpoly.nth(i+1)) for i in range(4)]
    assert S.simplify(E[0]-(1-S.Rational(5,4)*z))==0
    assert S.simplify(E[1]-z)==0
    assert S.simplify(E[2]-z*(11*z**2-16*z+4)/16)==0
    assert Apoly.nth(0)==1 and Apoly.nth(1)==0
    assert E[0].subs(z,a)==0 and E[2].subs(z,a)==-S.Rational(11,125)
    N=[Apoly.nth(i) for i in range(6)]
    g=[S.Integer(1)]
    for j in range(1,6):
        v=S.expand(N[j]*E[0]**j-sum(E[k]*g[j-k]*E[0]**(k-1) for k in range(1,j+1) if k<len(E)))
        g.append(v)
        assert S.simplify(v.subs(z,a)-(-a)**j)==0
        assert S.simplify(S.diff(v,z).subs(z,a)-(-a)**(j-1)*(-1-(j-1)*S.Rational(69,80)))==0
    r,j=S.symbols('r j',integer=True,nonnegative=True)
    n=r-j
    T=S.Rational(1,2)*j*(j+1)-S.Rational(1,2)*n*j-S.Rational(1,4)*n*(n-1)
    bracket=S.factor(T-j*(1+(j-1)*S.Rational(69,80)))
    universal=-r*(r-1)/4-S.Rational(9,80)*j*(j-1)
    assert S.simplify(bracket-universal)==0
    assert S.simplify(S.Rational(1,4)+S.Rational(9,80)*a*a/(2-a)**2-S.Rational(3,10))==0
    assert S.simplify(r*r-S.Rational(3,10)*r*(r-1)+r*(r-1)/2-r*(6*r-1)/5)==0
    b=build(max_r)
    for rr in range(1,max_r+1):
        c=diffs(dh_values(b,rr,extra=1))
        assert c[-1]==0 and c[-2]==6**rr
        assert c[-3]==Fraction(6**rr*(6*rr-1),5)
    return {'schema':'R333_PENULTIMATE_ALL_R_SYMBOLIC_CERTIFICATE_V1',
      'status':'PASS','dependency':'R330 Eq.(4) and deg(H_r)<=r, author-side',
      'E0':'1-5*z/4','E1':'z','E2':'z*(11*z**2-16*z+4)/16',
      'gprime_at_4_5':'(-4/5)**(j-1)*(-1-69*(j-1)/80)',
      'universal_top':'6**r','universal_penultimate':'6**r*(6*r-1)/5 for r>=1',
      'symbolic_bracket_identity':str(bracket),
      'integer_crosscheck_r':[1,max_r],
      'status_scope':'AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--max-r',type=int,default=32)
    p.add_argument('--out',default='R333_SYMBOLIC_EVIDENCE.json');a=p.parse_args()
    data=run(a.max_r)
    with open(a.out,'w',encoding='utf-8') as f:json.dump(data,f,indent=2);f.write('\n')
    print(json.dumps(data,indent=2))
