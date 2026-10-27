#!/usr/bin/env python3
"""R328 author-side exact rational generating-function certificate (SymPy).

Derives coefficients of y^j in P(z,y) = y*A((1-y)/2,yz)/(1-K((1-y)/2,yz)),
uses R326 pole-order lemma and Vandermonde to compute D_(q,q-r), r=0..4.
The general fixed-r asymptotic requires the argument in the proof note.
"""
import argparse, json
from math import comb
import sympy as sp

x,y,z,t,q,u=sp.symbols('x y z t q u')
h=sp.Rational(5,4)

def C(n,k):return comb(n,k) if 0<=k<=n else 0

def K_i(i):
    d=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),
       C(7,i-2),-C(9,i-3))
    return -t**(i-1)*sum(v*(1+t)**(i+1-j) for j,v in enumerate(d,1) if v)

def J_s(s):
    terms=(( -C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2))
    return sp.expand(t**s*sum(val*(1+t)**power for val,power in terms if val))

R=4
K=sp.expand(sum(K_i(i)*x**i for i in range(1,13)))
A=sp.expand(1+t+sum(J_s(i)*x**i for i in range(1,11)))
H=[sp.factor(K.coeff(t,j)) for j in range(R+2)]
Av=[sp.factor(A.coeff(t,j)) for j in range(R+1)]
assert H[0]==2*x
assert sp.simplify(H[1]-(3*x-x*x))==0
assert sp.simplify(H[2]-4*x*x*(1-2*x))==0
assert sp.simplify(Av[0]-1)==0
assert sp.simplify(Av[1]-(1-2*x))==0
x_y=(1-y)/2
num=[];den=[]
for ell in range(R+1):
    a=0
    for j in range(ell+1):
        a+=z**j * sp.Poly(sp.expand(Av[j].subs(x,x_y)),y).coeff_monomial(y**(ell-j))
    num.append(sp.factor(a))
    d=sp.Integer(1) if ell==0 else sp.Integer(0)
    for j in range(1,ell+2):
        d-=z**j*sp.Poly(sp.expand(H[j].subs(x,x_y)),y).coeff_monomial(y**(ell-j+1))
    den.append(sp.factor(d))
assert sp.simplify(den[0]-(1-h*z))==0
assert sp.simplify(den[1]-z)==0
assert num[0]==1 and num[1]==0
G=[None]*(R+1)
for ell in range(R+1):
    G[ell]=sp.cancel((num[ell]-sum(den[j]*G[ell-j] for j in range(1,ell+1)))/den[0])
expected=[
    sp.Integer(1),
    6*q,
    sp.Rational(2,5)*(45*q**2-27*q-46),
    sp.Rational(4,5)*(45*q**3-81*q**2-82*q-40),
    sp.Rational(2,25)*(675*q**4-2430*q**3-51*q**2-2386*q+4080),
]
results=[]
for r in range(R+1):
    expression=sp.Integer(0)
    for j in range(r+1):
        numerator=sp.cancel(G[j]*(1-h*z)**(j+1))
        part=sp.Integer(0)
        for (m,),value in sp.Poly(sp.expand(numerator),z).terms():
            # 4^q h^(q-m) = 5^(q-r) * 5^(r-m) * 4^m.
            coeff=sp.Integer(5)**(r-m)*sp.Integer(4)**m
            for v in range(j):coeff*= (q-m+j-v)
            coeff/=sp.factorial(j)
            part+=value*coeff
        for v in range(r-j):part *= (2*q-j-v)
        part/=sp.factorial(r-j)
        expression+=part
    assert sp.simplify(expression-expected[r])==0, (r,sp.factor(expression-expected[r]))
    shifted=sp.Poly(sp.expand(expected[r].subs(q,r+u)),u)
    assert all(c>0 for c in shifted.all_coeffs()),(r,shifted)
    assert sp.degree(expected[r],q)==r
    assert sp.simplify(sp.LC(sp.Poly(expected[r],q))-sp.Integer(6)**r/sp.factorial(r))==0
    results.append({
       'r':r,
       'formula_D_over_5_power':str(sp.factor(expected[r])),
       'shifted_at_q_eq_r_plus_u':str(shifted.as_expr()),
       'shifted_coefficients_descending':[str(c) for c in shifted.all_coeffs()],
       'leading_coefficient':str(sp.LC(sp.Poly(expected[r],q))),
       'positive_for_all_q_ge_r':True,
    })
assert G[0]==1/(1-h*z) or sp.simplify(G[0]-1/(1-h*z))==0
assert sp.simplify(G[1]+z/(1-h*z)**2)==0
out={
  'schema':'ENTERPRISE_MATH_R328_SYMBOLIC_EVIDENCE_V1',
  'status':'PASS',
  'method':'exact rational generating series, Vandermonde, symbolic polynomial identities and positive shifts',
  'H0':str(H[0]),'H1':str(H[1]),'H2':str(H[2]),
  'A0':str(Av[0]),'A1':str(Av[1]),
  'denominator_zero_order':str(den[0]),
  'denominator_first_order':str(den[1]),
  'numerator_y0':str(num[0]),'numerator_y1':str(num[1]),
  'G_y_coefficients':[str(sp.factor(v)) for v in G],
  'verified_bands':results,
  'general_asymptotic':'fixed r: D_(q,q-r)=5^(q-r)*(6^r q^r/r!+O_r(q^(r-1))) as q tends to infinity',
  'general_asymptotic_argument':'unique pole order r+1 comes from (-y*z)^r/(1-5*z/4)^(r+1); lower terms have pole order <=r',
  'review_status':'AUTHOR_SYMBOLIC_VERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED'
}
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--json',required=True)
    args=parser.parse_args()
    with open(args.json,'w',encoding='utf-8') as f:
        json.dump(out,f,indent=2,ensure_ascii=False)
        f.write('\n')
    print('R328 SYMBOLIC PASS',[(v['r'],v['formula_D_over_5_power']) for v in results])
