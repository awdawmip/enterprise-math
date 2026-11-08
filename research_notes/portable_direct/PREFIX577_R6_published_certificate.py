#!/usr/bin/env python3
"""PREFIX-577-R6 exact full six-axis/gate covariance, stdlib-only.
Scientific model: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Native kernel dependency: PREFIX565 blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from PREFIX565_positive_marginal_certificate import PHASES,ACTIONS,ZERO_ROOT,ROOTS,SCIENCE_PIN,edge
from PREFIX566_gate_quotient_certificate import marginal_gate_rows,weighted_quotient

def main():
    assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
    E=[[edge(i,a,ZERO_ROOT) for a in ACTIONS] for i in range(96)]
    assert Counter(j for row in E for j,w in row)==Counter({i:6 for i in range(96)})
    assert all(sum(w[:6])==1 for row in E for j,w in row)
    for root in ROOTS:
        for i,row in enumerate(E):
            ci=PHASES[i//2][2]
            for a,(j,w0) in zip(ACTIONS,row):
                target,w=edge(i,a,root)
                assert j==target and w[6]==w0[6]
                for k in range(6):
                    ck=PHASES[j//2][2]
                    d=(int(ck==root[k]*(k+1))-int(ci==root[k]*(k+1))) if root[k] else 0
                    assert w[k]==w0[k]+d
    ids,Q,growth=weighted_quotient(marginal_gate_rows(ZERO_ROOT))
    assert len(Q)==37 and ids[0]==ids[48] and growth==[1,4,13,21,33,37]
    assert E[0][0][1][:6]!=(E[48][0][1][:6])
    n=96;m=7
    P=[[F(0) for _ in range(n)] for _ in range(n)]
    R=[[F(0) for _ in range(m)] for _ in range(n)]
    for i,row in enumerate(E):
        for j,w in row:
            P[i][j]+=F(1,6)
            for k in range(m):R[i][k]+=F(w[k],6)
    mu=[sum(R[i][k] for i in range(n))/n for k in range(m)]
    assert mu==[F(1,6)]*6+[F(1,192)]
    # Exact seven-RHS rational Gauss-Jordan; h[0]=0.
    A=[[F(int(i==j))-P[i][j] for j in range(1,n)]
       +[R[i][k]-mu[k] for k in range(m)] for i in range(1,n)]
    for col in range(n-1):
        r=next(r for r in range(col,n-1) if A[r][col]);A[col],A[r]=A[r],A[col]
        d=A[col][col];A[col]=[v/d for v in A[col]]
        for r in range(n-1):
            if r!=col and A[r][col]:
                t=A[r][col];A[r]=[A[r][j]-t*A[col][j] for j in range(n-1+m)]
    H=[[F(0)]*m]+[row[n-1:] for row in A]
    assert all(sum((F(int(i==j))-P[i][j])*H[j][k] for j in range(n))==R[i][k]-mu[k]
               for i in range(n) for k in range(m))
    S=[[F(0) for _ in range(m)] for _ in range(m)]
    for i,row in enumerate(E):
        es=[[F(w[k])-mu[k]+H[j][k]-H[i][k] for k in range(m)] for j,w in row]
        assert all(sum(e[k] for e in es)==0 for k in range(m))
        for e in es:
            for k in range(m):
                for l in range(k,m):S[k][l]+=e[k]*e[l]/(n*6)
    for k in range(m):
        for l in range(k):S[k][l]=S[l][k]
    C=[row[:6] for row in S[:6]]
    assert all(C[i][j]==F(int(i==j),18)-F(1,216)-F(int(i==(j^1)),36)
               for i in range(6) for j in range(6))
    assert [S[i][6] for i in range(6)]==[F(x,6912) for x in (11,-7,11,-7,-4,-4)]
    assert S[6][6]==F(1127,221184)
    assert all(sum(S[i][j] for j in range(6))==0 for i in range(m))
    g=[S[i][6] for i in range(6)]
    sym=[(g[i]+g[i^1])/2 for i in range(6)]
    anti=[(g[i]-g[i^1])/2 for i in range(6)]
    assert S[6][6]-36*sum(t*t for t in sym)-12*sum(t*t for t in anti)==F(367,73728)
    return {'status':'ALL_CHECKS_PASS','mean':[str(x) for x in mu],
            'covariance_rate':[[str(x) for x in row] for row in S],
            'poisson_row_equations':n*m,'root_edge_checks':len(ROOTS)*n*len(ACTIONS),
            'axis_spectrum':{'0':1,'1/36':2,'1/12':3},
            'full_rank':6,'gate_residual':'367/73728'}

if __name__=='__main__':
    import json
    print(json.dumps(main(),ensure_ascii=False,indent=2))
