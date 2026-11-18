#!/usr/bin/env python3
"""R284AB: exact 2x2 two-way-feedback Port determinant and kernel checks."""
from fractions import Fraction as F
from itertools import product, permutations
import json

P=(0,1); AI=(2,3); BI=(4,5); Q=(6,7); S=AI+BI
L=((F(1,16),F(1,32)),(F(1,64),F(1,24)))
C=((F(1,16),F(1,16)),(F(1,16),F(1,16)))
D=((F(1,32),F(1,48)),(F(1,40),F(1,64)))
U=((F(1,20),F(1,36)),(F(1,48),F(1,28)))

def det(a):
    a=[r[:] for r in a]; n=len(a); d=F(1)
    for j in range(n):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None: return F(0)
        if piv!=j:a[j],a[piv]=a[piv],a[j];d=-d
        v=a[j][j];d*=v
        for i in range(j+1,n):
            t=a[i][j]/v
            for k in range(j+1,n): a[i][k]-=t*a[j][k]
            a[i][j]=0
    return d

def rank(a):
    a=[r[:] for r in a]; n=len(a); m=len(a[0]); k=0
    for j in range(m):
        t=next((i for i in range(k,n) if a[i][j]),None)
        if t is None:continue
        a[k],a[t]=a[t],a[k];v=a[k][j]
        for h in range(j,m):a[k][h]/=v
        for i in range(n):
            if i!=k:
                v=a[i][j]
                for h in range(j,m):a[i][h]-=v*a[k][h]
        k+=1
        if k==n:break
    return k

def inverse(a):
    n=len(a)
    x=[a[i][:]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next((i for i in range(j,n) if x[i][j]),None)
        assert k is not None
        x[j],x[k]=x[k],x[j];v=x[j][j]
        x[j]=[e/v for e in x[j]]
        for i in range(n):
            if i!=j:
                v=x[i][j];x[i]=[a-v*b for a,b in zip(x[i],x[j])]
    return [r[n:] for r in x]

def mul(x,y):
    return [[sum((x[i][k]*y[k][j] for k in range(len(y))),F(0)) for j in range(len(y[0]))] for i in range(len(x))]

def build(x=F(0),y=F(0),u=F(0),v=F(0),eta=F(0)):
    g=(F(1,8)+x,F(1,8)+y);h=(F(1,8)+u,F(1,8)+v)
    w=[[F(0)]*8 for _ in range(8)]
    for i in range(2):
        w[P[i]][AI[i]]=g[i];w[BI[i]][Q[i]]=h[i]
        for j in range(2):
            w[AI[i]][AI[j]]=L[i][j]
            w[AI[i]][BI[j]]=C[i][j]+(eta if (i,j)==(0,0) else 0)
            w[BI[i]][AI[j]]=D[i][j]
            w[BI[i]][BI[j]]=U[i][j]
    assert all(0<=e for row in w for e in row)
    assert all(sum(row)<1 for row in w)
    m=[[F(i==j)-w[i][j] for j in range(8)] for i in range(8)]
    a=[[m[i][j] for j in S+Q] for i in S+P]
    G=[[m[i][j] for j in S] for i in S]
    ps=[[w[i][j] for j in S] for i in P]
    sq=[[w[i][j] for j in Q] for i in S]
    transfer=mul(mul(ps,inverse(G)),sq)
    return m,a,G,transfer,g,h

num=0
for vals in product((F(0),F(1,64),F(1,16)),repeat=4):
    m,a,G,t,g,h=build(*vals)
    assert det(G)>0
    assert rank(a)==5 and det(a)==0 and rank(t)==1 and det(t)==0
    assert det(a)==det(G)*det(t)
    assert any(all(a[i][p[i]] for i in range(6)) for p in permutations(range(6)))
    num+=1

r0=build(u=0,v=0)[1];r1=build(u=F(1,16),v=0)[1]
l0=build(x=0,y=0)[1];l1=build(x=F(1,16),y=0)[1]
right_rank=rank(r0+r1)
left_rank=rank([[l0[i][j] for i in range(6)] for j in range(6)]+[[l1[i][j] for i in range(6)] for j in range(6)])
assert right_rank==left_rank==6

pert=0
for vals in product((F(0),F(1,64)),repeat=4):
    m,a,G,t,g,h=build(*vals,eta=F(1,32))
    expected=g[0]*g[1]*h[0]*h[1]*F(1,32)*F(1,16)
    assert det(a)==expected and rank(a)==6
    assert det(G)*det(t)==expected
    pert+=1

# Feedback loops exist: a1->b2->a2->b1->a1, with all four edges strictly positive.
# Identity holds even though the internal digraph is strongly connected.
assert C[0][1]*D[1][1]*C[1][0]*D[0][0]>0

out={
  "schema":"ENTERPRISE_MATH_R284AB_FEEDBACK_CERTIFICATE_V1", "status":"PASS",
  "arithmetic":"exact Fraction elimination, rank, inverse; no floating point",
  "internal_edges":{"L":[list(map(str,row)) for row in L],"C":[list(map(str,row)) for row in C],"D":[list(map(str,row)) for row in D],"U":[list(map(str,row)) for row in U]},
  "checks":{"3^4_feedback_stable_ranks_schur_perfect_matching":num,"2^4_center_edit_rank_restore":pert},
  "full_matrix_common_right_kernel_stacked_rank":right_rank,
  "full_matrix_common_left_kernel_stacked_rank":left_rank,
  "base_internal_G_determinant":str(det(build()[2])),
  "base_full_complement_determinant":str(det(build()[1])),
  "perturbation_eta_1_32_baseline_determinant":str(det(build(eta=F(1,32))[1])),
  "conclusion_scope":"auxiliary rational Port, not native BRC time evolution or physical residual"
}
print(json.dumps(out,indent=2))
