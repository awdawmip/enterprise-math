#!/usr/bin/env python3
"""Exact Gram-certificate checks for R284AJ; imports R284AI elimination."""
from fractions import Fraction as F
from itertools import product, combinations
from math import prod
import json
from R284AI_rank_one_scc_cancellation_checker import determinant, rank


def gram_family(m, r):
    U=[[F((i+1)**j, m**(r-1)) for j in range(r)] for i in range(m)]
    C=[[sum((U[i][k]*U[j][k] for k in range(r)), F(0)) for j in range(m)] for i in range(m)]
    return U, C


def pencil(C, u, v):
    m=len(C)
    A=[[F(0) for _ in range(2*m)] for _ in range(2*m)]
    for i in range(m):
        A[i][i]=u[i]; A[i][m+i]=F(1)
        A[m+i][m+i]=v[i]
        for j in range(m):A[m+i][j]=C[i][j]
    return A


def coeff_formula(C,u,v):
    m=len(C); x=[u[i]*v[i] for i in range(m)]
    value=F(0)
    for k in range(m+1):
        for I in combinations(range(m),k):
            d=determinant([[C[i][j] for j in I] for i in I])
            value+=(-1)**k*d*prod(x[j] for j in range(m) if j not in I)
    return value


def port(C,t):
    m=len(C);q=2*m;k=q+1
    N=[[F(0) for _ in range(q)] for _ in range(q)]
    for i in range(m):
        N[i][m+i]=F(1)
        for j in range(m):N[m+i][j]=C[i][j]
    max_n_row=max(map(sum,N))
    c=F(1,16*(k+max_n_row+1));delta=F(1,256*k);g=F(1,16)
    core=[[c*(1+(N[i][j] if i<q and j<q else 0)) + (t[i] if i==j and i<q else 0) for j in range(k)] for i in range(k)]
    assert min(map(min,core))>0 and max(map(sum,core))<1
    assert delta*k+max(map(sum,core))<1 and 2*delta*k+g<1
    A=[[F(0) for _ in range(3*k)] for _ in range(3*k)]
    for i in range(k):
        for j in range(k):
            A[i][j]=(1 if i==j else 0)-delta
            A[i][k+j]=-core[i][j]
            A[k+i][j]=-delta
            A[k+i][k+j]=(1 if i==j else 0)-delta
        A[k+i][2*k+i]=-g
        A[2*k+i][i]=-g
    return A,core,c,g,N


def run():
    checks={'principal_minors':0,'pencil_exact':0,'rank':0,'port_exact':0}
    cases=[]
    for m,r in [(m,r) for m in range(2,5) for r in range(1,m)]+[(5,3)]:
        U,C=gram_family(m,r)
        assert rank(U)==r and rank(C)==r
        checks['rank']+=2
        for k in range(m+1):
            for I in combinations(range(m),k):
                d=determinant([[C[i][j] for j in I] for i in I])
                assert d>=0 and (k<=r or d==0)
                if k==r:assert d>0
                checks['principal_minors']+=1
        for vals in product([F(0),F(1)],repeat=2*m):
            assert determinant(pencil(C,vals[:m],vals[m:]))==coeff_formula(C,vals[:m],vals[m:])
            checks['pencil_exact']+=1
        cases.append({'m':m,'r':r,'q':2*m,'rank_N':m+r,'nu':2*(m-r),'gap':2*(m-r)})
        if (m,r) in [(3,2),(4,2)]:
            for j in range(2 if m==4 else 3):
                k=2*m+1;c=F(1,16*(k+max(map(sum,C))+2))
                ts=[F(0) if i%3==1 else c*F(j,2) for i in range(2*m)]
                A,core,cc,g,N=port(C,ts)
                D=[[cc*N[i][h]+(ts[i] if i==h else F(0)) for h in range(2*m)] for i in range(2*m)]
                assert determinant(core)==cc*determinant(D)
                assert determinant(A)==(-1)**k*g**(2*k)*determinant(core)
                checks['port_exact']+=1
    return {'schema':'R284AJ_EXACT_GRAM_CHECK_V1','status':'PASS','arithmetic':'Fraction exact','scope':'m=2..4 all r=1..m-1, plus m=5 r=3; Boolean 2m edit grids; five full Port instances','checks':checks,'cases':cases,'source_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34','review':'NOT_REVIEWED'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
