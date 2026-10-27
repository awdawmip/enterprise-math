#!/usr/bin/env python3
"""R330 exact finite diagonal certificate, derived from R329 (immutable d00a6699).
All calculations use SymPy exact rationals; auxiliary six-edge signed-tail K/J model.
"""
import argparse, json, hashlib, time
from math import comb
import sympy as sp
x,t,y,z,q,u=sp.symbols('x t y z q u')
h=sp.Rational(5,4)
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def K_i(i):
    d=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    return -t**(i-1)*sum(v*(1+t)**(i+1-j) for j,v in enumerate(d,1) if v)
def J_s(s):
    parts=((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2))
    return sp.expand(t**s*sum(c*(1+t)**e for c,e in parts if c))
def run(R):
    K=sp.Poly(sum(K_i(i)*x**i for i in range(1,13)),t)
    A=sp.Poly(1+t+sum(J_s(i)*x**i for i in range(1,11)),t)
    H=[K.nth(j) for j in range(R+2)]
    Av=[A.nth(j) for j in range(R+1)]
    assert H[0]==2*x and sp.expand(H[1]-(3*x-x*x))==0
    assert sp.expand(H[2]-4*x*x*(1-2*x))==0
    def yc(f,p):return sp.Poly(sp.expand(f.subs(x,(1-y)/2)),y).nth(p) if p>=0 else sp.Integer(0)
    N=[];E=[]
    for ell in range(R+1):
        N.append(sp.Poly(sp.expand(sum(z**j*yc(Av[j],ell-j) for j in range(ell+1))),z).as_expr())
        E.append(sp.Poly(sp.expand(-sum(z**j*yc(H[j],ell-j+1) for j in range(ell+2))),z).as_expr())
    assert sp.expand(E[0]-(1-h*z))==0
    assert sp.expand(E[1]-z)==0
    assert N[0]==1 and N[1]==0
    g=[];results=[];violations=[]
    for r in range(R+1):
        numer=sp.Poly(N[r],z)*sp.Poly((1-h*z)**r,z)
        for j in range(1,r+1):
            numer-=sp.Poly(E[j],z)*g[r-j]*sp.Poly((1-h*z)**(j-1),z)
        g.append(numer)
        assert numer.degree()<=2*r,(r,numer.degree())
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
        positive=all(c>0 for c in shift.all_coeffs())
        bad=[{'exponent':int(m[0]),'value':str(v)} for m,v in shift.terms() if v<=0]
        if bad:violations.append({'r':r,'bad':bad})
        results.append({'r':r,'shift_coeffs':[str(c) for c in shift.all_coeffs()], 'positive':positive, 'constant':str(shift.nth(0)), 'degree':int(shift.degree()), 'num_z_degree':int(numer.degree())})
        print('r',r,'positive',positive,'min_coeff',str(min(shift.all_coeffs()))[:70],flush=True)
    out={'schema':'EM_R330_DIAGONAL_SYMBOLIC_V1','max_r':R,'all_positive':not violations, 'violations':violations,'results':results,'source':'R329 d00a6699e12ba3e1bcdc58abbb674636546d98e9', 'arithmetic':'SymPy exact QQ'}
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--max-r',type=int,default=20);ap.add_argument('--json',required=True);args=ap.parse_args()
    a=run(args.max_r)
    with open(args.json,'w') as f:json.dump(a,f,indent=2,ensure_ascii=False);f.write('\n')
    print('FINAL',a['all_positive'])
