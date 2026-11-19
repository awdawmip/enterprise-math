#!/usr/bin/env python3
"""R284AI exact rational finite cross-check, Python standard library only."""
from fractions import Fraction as F
from itertools import product, permutations, combinations
from math import prod, factorial
import json


def determinant(matrix):
    n=len(matrix)
    if n==0: return F(1)
    a=[[F(x) for x in row] for row in matrix]
    out=F(1)
    for j in range(n):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None: return F(0)
        if p!=j:
            a[j],a[p]=a[p],a[j];out=-out
        pivot=a[j][j];out*=pivot
        for i in range(j+1,n):
            f=a[i][j]/pivot
            if f:
                for k in range(j+1,n):a[i][k]-=f*a[j][k]
            a[i][j]=F(0)
    return out


def rank(matrix):
    a=[[F(x) for x in row] for row in matrix]
    if not a:return 0
    n=len(a);m=len(a[0]);r=0
    for j in range(m):
        p=next((i for i in range(r,n) if a[i][j]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        pivot=a[r][j]
        for k in range(j,m):a[r][k]/=pivot
        for i in range(r+1,n):
            f=a[i][j]
            if f:
                for k in range(j,m):a[i][k]-=f*a[r][k]
        r+=1
        if r==n:break
    return r


def n_matrix(m,a,b):
    n=2*m
    out=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(m):
        out[i][m+i]=F(1)
        for j in range(m):out[m+i][j]=F(a[i]*b[j])
    return out


def pencil(m,a,b,t,scale=F(1)):
    n=n_matrix(m,a,b)
    return [[scale*n[i][j] + (t[i] if i==j else F(0)) for j in range(2*m)] for i in range(2*m)]


def formula(m,a,b,t,scale=F(1)):
    x=[t[i]*t[m+i] for i in range(m)]
    return prod(x)-scale**2*sum((a[i]*b[i]*prod(x[j] for j in range(m) if j!=i) for i in range(m)),F(0))


def port_matrix(m,a,b,t):
    q=2*m;k=q+1
    c=F(1,16*(k+m+1));delta=F(1,256*k);g=F(1,16)
    n=n_matrix(m,a,b)
    core=[[c*(1+(n[i][j] if i<q and j<q else 0)) + (t[i] if i==j and i<q else 0) for j in range(k)] for i in range(k)]
    assert min(min(row) for row in core)>0
    assert all(sum(row)<1 for row in core)
    assert k*delta+max(map(sum,core))<1 and 2*k*delta+g<1
    z=F(0);A=[[z]* (3*k) for _ in range(3*k)]
    for i in range(k):
        for j in range(k):
            A[i][j]=(1 if i==j else 0)-delta
            A[i][k+j]=-core[i][j]
            A[k+i][j]=-delta
            A[k+i][k+j]=(1 if i==j else 0)-delta
        A[k+i][2*k+i]=-g
        A[2*k+i][i]=-g
    return A,core,c,g


def run():
    checks={'pencil_exact':0,'principal_minor_exact':0,'sign_involution':0,'rank_exact':0,'port_exact':0}
    cases=[]
    for m in range(2,6):
        a=[F(i+1,i+2) for i in range(m)]
        b=[F(i+2,i+3) for i in range(m)]
        N=n_matrix(m,a,b)
        assert rank(N)==m+1
        checks['rank_exact']+=1
        if m<=4:
            for mask in range(1<<(2*m)):
                ids=[i for i in range(2*m) if (mask>>i)&1]
                minor=determinant([[N[i][j] for j in ids] for i in ids])
                if len(ids)==0:expected=F(1)
                elif len(ids)==2 and ids[0]<m and ids[1]==m+ids[0]:expected=-a[ids[0]]*b[ids[0]]
                else:expected=F(0)
                assert minor==expected,(m,ids,minor,expected)
                checks['principal_minor_exact']+=1
        for pi in permutations(range(m)):
            swapped=tuple((1 if j==0 else 0 if j==1 else j) for j in pi)
            assert prod(a[i]*b[pi[i]] for i in range(m))==prod(a[i]*b[swapped[i]] for i in range(m))
            checks['sign_involution']+=1
        for bits in product([F(0),F(1)],repeat=2*m):
            assert determinant(pencil(m,a,b,bits))==formula(m,a,b,bits)
            checks['pencil_exact']+=1
        if m<=3:
            for bits in product([F(0),F(1,2),F(1)],repeat=2*m):
                assert determinant(pencil(m,a,b,bits))==formula(m,a,b,bits)
                checks['pencil_exact']+=1
        cases.append({'m':m,'q':2*m,'rank_N':m+1,'corank':m-1,'nu':2*m-2,'cycle_packing':2*m,'gap':2*m-2,'weights_a':[str(x) for x in a],'weights_b':[str(x) for x in b]})
        if m<=3:
            k=2*m+1;c=F(1,16*(k+m+1))
            for v in (F(0),c/2,c):
                t=[v if (i%3!=1) else F(0) for i in range(2*m)]
                A,C,c,g=port_matrix(m,a,b,t)
                target=(-1)**k*g**(2*k)*c*formula(m,a,b,t,scale=c)
                assert determinant(A)==target
                assert determinant(C)==c*formula(m,a,b,t,scale=c)
                checks['port_exact']+=1
    return {'schema':'R284AI_EXACT_CHECK_V1','status':'PASS','arithmetic':'fractions.Fraction; exact Gaussian elimination','finite_scope':'m=2..5 rational rank-one weights, Boolean pencils; m=2..3 ternary pencils/Port; principal minors m=2..4','checks':checks,'cases':cases,'source_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34','review':'NOT_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
