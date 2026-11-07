#!/usr/bin/env python3
"""R329 auxiliary ordered-six BRC: exact Newton diagonal symbolic checks.
Source definitions from R328 immutable commit 271b843..., no physical propagation.
"""
import sympy as sp
from math import comb
import json,argparse
x,t,y,z,q,u = sp.symbols('x t y z q u')
h=sp.Rational(5,4)

def C(n,k):return comb(n,k) if 0<=k<=n else 0

def K_i(i):
    d=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2), C(7,i-2),-C(9,i-3))
    return -t**(i-1)*sum(v*(1+t)**(i+1-j) for j,v in enumerate(d,1) if v)
def J_s(s):
    parts=((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2))
    return sp.expand(t**s*sum(c*(1+t)**e for c,e in parts if c))

def calculate(R):
    K=sp.Poly(sum(K_i(i)*x**i for i in range(1,13)),t)
    A=sp.Poly(1+t+sum(J_s(i)*x**i for i in range(1,11)),t)
    H=[K.nth(j) for j in range(R+2)]
    Av=[A.nth(j) for j in range(R+1)]
    assert H[0]==2*x and sp.expand(H[1]-(3*x-x*x))==0
    assert sp.expand(H[2]-4*x*x*(1-2*x))==0
    # Raw rational transform N(y,z) = A(x(y),yz) and E(y,z) = (1-K(x(y),yz))/y.
    def yc(f,p):return sp.Poly(sp.expand(f.subs(x,(1-y)/2)),y).nth(p) if p>=0 else sp.Integer(0)
    N=[];E=[]
    for ell in range(R+1):
        N.append(sp.Poly(sp.expand(sum(z**j*yc(Av[j],ell-j) for j in range(ell+1))),z).as_expr())
        E.append(sp.Poly(sp.expand((1 if ell==0 else 0) if False else -sum(z**j*yc(H[j],ell-j+1) for j in range(ell+2))),z).as_expr())
    # for ell 0: coefficient [y^1] of 1-K has from 1 term 0, H0=2x=1-y giving +1, so fine
    assert sp.expand(E[0]-(1-h*z))==0,(E[0], 'E0')
    assert sp.expand(E[1]-z)==0,(E[1], 'E1')
    assert N[0]==1 and N[1]==0
    g=[];diff=[];results=[]
    for r in range(R+1):
        # G_r = g_r/(1-h*z)^(r+1).
        numerator=sp.Poly(N[r],z)*sp.Poly((1-h*z)**r,z)
        for j in range(1,r+1):
            numerator -= sp.Poly(E[j],z)*g[r-j]*sp.Poly((1-h*z)**(j-1),z)
        g.append(numerator)
        assert numerator.degree()<=2*r,(r,numerator.degree())
        # D_q,q-r / 5^(q-r) = sum_j [z^m]g_j * 5^(r-m)*4^m * binom(q-m+j,j)* binom(2q-j,r-j)
        expr=sp.Integer(0)
        for j in range(r+1):
            for (m,),val in g[j].terms():
                bin1=sp.prod(q-m+j-v for v in range(j))/sp.factorial(j)
                bin2=sp.prod(2*q-j-v for v in range(r-j))/sp.factorial(r-j)
                expr+=val*sp.Rational(5)**(r-m)*sp.Integer(4)**m*bin1*bin2
        expr=sp.Poly(sp.expand(expr),q)
        shift=sp.Poly(sp.expand(expr.as_expr().subs(q,r+u)),u)
        assert expr.degree()==r,(r,expr.degree())
        assert expr.LC()==sp.Integer(6)**r/sp.factorial(r),(r,expr.LC())
        results.append({'r':r,'q_polynomial':str(expr.as_expr()),'shift_poly':str(shift.as_expr()),
           'shift_coeffs':[str(c) for c in shift.all_coeffs()],
           'all_shift_coefficients_positive':all(c>0 for c in shift.all_coeffs()),
           'min_shift_coeff':str(min(shift.all_coeffs())),'G_numerator_z_degree':numerator.degree()})
        print('r',r,'shift positive',results[-1]['all_shift_coefficients_positive'],'min',results[-1]['min_shift_coeff'],flush=True)
    return {'schema':'EM_R329_DIAGONAL_SYMBOLIC_V1','max_r':R,'status':'PASS' if all(r['all_shift_coefficients_positive'] for r in results) else 'SIGN_SHIFT_FAIL','results':results,
            'source':'R328 immutable 271b843173aac0830792d3df4ecb0537eb022ee2',
            'model':'ordered six-edge positive-weight BRC auxiliary combinatorial recurrence, signed tails retained'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--max-r',type=int,default=8);ap.add_argument('--json',required=True);args=ap.parse_args()
    res=calculate(args.max_r)
    with open(args.json,'w') as f:json.dump(res,f,indent=2)
    print(res['status'])
