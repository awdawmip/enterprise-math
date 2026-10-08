#!/usr/bin/env python3
"""Exact algebra and four targeted regressions; no prime-uniform claim from testing."""
import json
from pathlib import Path
import sympy as sp
from check_d25_predecessor import Q2, formal_H

def symbolic():
    x,y,a=sp.symbols('x y a'); D=2*y+x+a
    relation=y*y+x*y+a*y-x**3
    yt=-y/(27*D); yx=(3*x*x-y)/D
    u=-x/y
    ut=sp.diff(u,y)*yt
    ux=sp.diff(u,x)+sp.diff(u,y)*yx
    xt=x/(27*(y+x+2*a))
    tests=[ut-u/(27*D),ux-(y+x+2*a)/(D*y),ut+ux*xt,
           2*yt+sp.Rational(1,27)-(x+a)/(27*D)]
    for z in tests:
        num=sp.cancel(z).as_numer_denom()[0]
        assert sp.rem(num,relation,y)==0
    return {'implicit_curve_identities':len(tests)}

def one(p):
    N=p; M=p*p; zero=Q2(0,0,M); one=Q2(1,0,M); s=Q2(0,1,M)
    a=(2-s).div_scalar(108)
    def add(X,Y): return [X[i]+Y[i] for i in range(N+1)]
    def scale(X,c): return [z*c for z in X]
    def shift(X,k): return [zero]*k+X[:N+1-k]
    def mul(X,Y): return [sum((X[i]*Y[n-i] for i in range(n+1)),zero) for n in range(N+1)]
    def inv(X):
        z=[X[0].inv()]
        for n in range(1,N+1):z.append(-z[0]*sum((X[i]*z[n-i] for i in range(1,n+1)),zero))
        return z
    I=[one]+[zero]*N
    V=[one]
    for n in range(1,N+1):
        V.append(V[n-1]+(a*sum((V[i]*V[n-3-i] for i in range(n-2)),zero) if n>=3 else zero))
    S=add(I,scale(shift(I,1),-1)); S=add(S,scale(shift(V,3),-2*a)); H=inv(S)
    U=add(scale(I,-2),shift(I,1)); U=add(U,scale(shift(V,3),a))
    W=add(scale(I,-1),shift(I,1)); W=add(W,scale(shift(V,3),2*a))
    Q=scale(shift(mul(mul(V,inv(U)),inv(W)),4),s.div_scalar(108))
    Jx=scale(shift(mul(mul(mul(V,add(I,scale(shift(V,2),a))),H),mul(inv(U),inv(U))),4),-s.div_scalar(108))
    Hp,Ht,t=formal_H(p)
    assert H[p-1].tup()==Hp.tup()
    Jxi=(s*Ht).div_scalar(4)
    assert Jx[p-1].tup()==(Jxi-p*Q[p]).tup()
    assert Q[4].tup()==s.div_scalar(216).tup()
    q=Q2(Q[p].a,Q[p].b,p); j0=Q2(Jxi.a,Jxi.b,p)
    effect=-q*j0.inv()
    return {'p':p,'Q_p_mod_p':q.tup(),'Jxi_mod_p2':Jxi.tup(),
            'Jx_mod_p2':Jx[p-1].tup(),'Lx_minus_Lxi_if_same_exact_c':effect.tup(),
            'coordinate_chain_pass':True}

if __name__=='__main__':
    result={'symbolic':symbolic(),'targets':[one(p) for p in (13,19,37,43)],
            'scope':'FOUR_TARGETED_REGRESSIONS_ONLY; global identities have algebraic proofs in report'}
    out=json.dumps(result,indent=2,sort_keys=True)+'\n'
    Path(__file__).with_name('fixed_x_checks.json').write_text(out)
    print(out)
