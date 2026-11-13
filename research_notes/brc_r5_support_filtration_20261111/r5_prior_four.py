#!/usr/bin/env python3
"""R5 fixed-fiber source-3 four-target mask census. Exact Fraction certificate.
Reuses frozen PR #2017 seven-ratio witness via PR #2059 VERIFY_SHARP_FACE.py.
No floating point or solver is used in verification.
"""
from fractions import Fraction as F
from itertools import combinations

R=(2,10,15,20,25,30,38); S=(1,2,3,5)
ARCS=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7)
           if j not in (0,6) or i==j)
E0=tuple(map(F,('219346331/10192753200,7664319/135903376,'
 '2813871/16987922,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,393042/8493961,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,'
 '5251441/33975844,166713611/1274094150,'
 '2500147/33975844,393042/8493961,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,'
 '7664319/135903376,451274777/3397584400').split(',')))
assert len(ARCS)==len(E0)==30 and min(E0)>0
M=[sum((z for (ii,j),z in zip(ARCS,E0) if ii==i and j in S),F(0)) for i in range(7)]
Q={j:sum((z for (i,jj),z in zip(ARCS,E0) if jj==j),F(0)) for j in S}
T={j:sum((R[i]*z for (i,jj),z in zip(ARCS,E0) if jj==j),F(0)) for j in S}
assert T[3]==20*Q[3]
V=tuple((i,j) for j in S for i in range(7))
# 15 rows, 28 source-target variables; two row identities, rank 13.
A=[[int(ii==i) for ii,jj in V] for i in range(7)]
A += [[int(jj==j) for ii,jj in V] for j in S]
A += [[R[ii]*int(jj==j) for ii,jj in V] for j in S]
b=M+[Q[j] for j in S]+[T[j] for j in S]
assert all(sum(F(A[r][k])*E0[ARCS.index(V[k])] for k in range(28))==b[r]
           if r<7 else True for r in range(7))

def rank(mat):
    z=[list(map(F,row)) for row in mat]
    if not z: return 0
    m,n=len(z),len(z[0]);row=0
    for col in range(n):
        k=next((k for k in range(row,m) if z[k][col]),None)
        if k is None:continue
        z[row],z[k]=z[k],z[row]
        piv=z[row][col];z[row]=[t/piv for t in z[row]]
        for i in range(row+1,m):
            t=z[i][col]
            if t:z[i]=[x-t*y for x,y in zip(z[i],z[row])]
        row+=1
        if row==m:break
    return row

def solve_overdetermined(piv,rhs):
    n=len(piv)
    z=[[F(A[r][k]) for k in piv]+[rhs[r]] for r in range(len(b))]
    row=0
    for col in range(n):
        k=next((k for k in range(row,len(z)) if z[k][col]),None)
        assert k is not None
        z[row],z[k]=z[k],z[row]
        factor=z[row][col];z[row]=[x/factor for x in z[row]]
        for i in range(len(z)):
            if i==row:continue
            t=z[i][col]
            if t:z[i]=[a-t*c for a,c in zip(z[i],z[row])]
        row+=1
    assert all(not any(t[:n]) and t[-1]==0 for t in z[n:])
    return [z[i][-1] for i in range(n)]

# Each rational primal witness has 12 nonpivot variables set to t,
# while 13 pivot variables are solved uniquely by the 15 exact equations.
PRIMAL={
 (1,3,4,6):(F(1,900),(17,15,2,18,1,9,0,26,20,27,23,7,3)),
 (2,3,4,5):(F(1,500),(16,1,17,18,0,27,8,19,5,22,13,7,9)),
 (2,3,4,6):(F(1,800),(16,1,17,18,0,8,26,27,5,20,13,22,2))
}
# Farkas y: each allowed column a_k satisfies y.a_k>=0
# while y.b<0, excluding nonnegative solutions.
DUAL={
 (1,2,3,6):('21/25','1/5','-1/70','-8/35','-1','-1','-1',
              '-1','-1','-22/35','1','2/25','2/25','3/70','0'),
 (1,2,4,6):('4/5','0','-5/28','-1','-15/28','-1','-1',
              '-1','-1','-5/14','1','1/10','1/10','1/28','0'),
 (1,3,5,6):('21/25','1/5','-1/5','-8/35','-1','-23/35','-1',
              '-1','-1','-22/35','1','2/25','2/25','3/70','0'),
 (1,4,5,6):('4/5','0','-1/2','-1','-15/28','-5/7','-1',
              '-1','-1','-5/14','1','1/10','1/10','1/28','0')
}
# Reproduce seven locally candidate masks via exact moment extrema.
locally=[];rejected={'capacity':0,'moment':0,'boundary':0}
for J in combinations(range(7),4):
    total=sum((M[i] for i in J),F(0))
    if total<Q[3]:rejected['capacity']+=1;continue
    def moment(reverse):
        remain=Q[3];score=F(0)
        for i in sorted(J,key=lambda i:R[i],reverse=reverse):
            w=min(M[i],remain);remain-=w;score+=R[i]*w
        assert remain==0
        return score
    lo,hi=moment(False),moment(True)
    if lo<T[3]<hi:
        assert total>Q[3]
        locally.append(J)
    elif lo<=T[3]<=hi:rejected['boundary']+=1
    else:rejected['moment']+=1
assert len(locally)==7 and rejected=={'capacity':9,'moment':19,'boundary':0}
# Supports with at most 3 targets fail even box feasibility.
for size in (1,2,3):
    for J in combinations(range(7),size):
        if sum((M[i] for i in J),F(0))<Q[3]:continue
        def smaller_moment(reverse):
            remain=Q[3];total=F(0)
            for i in sorted(J,key=lambda i:R[i],reverse=reverse):
                m=min(remain,M[i]);total+=R[i]*m;remain-=m
            assert remain==0
            return total
        assert not smaller_moment(False)<=T[3]<=smaller_moment(True)
# The three 12-dimensional faces are pairwise disjoint:
# J1346&J2345 have intersection {3,4}, J1346&J2346: {3,4,6}.
# All these R>=20; mean 20 would require only target 3,
# but target 3 capacity < Q3. J2345&J2346: {2,3,4}, insufficient capacity.
assert Q[3]-M[3]==F('2330939/8493961')>0
assert Q[3]-sum((M[i] for i in (2,3,4)),F(0))==F('196521/16987922')>0
assert set(locally)==set(PRIMAL)|set(DUAL)
assert rank(A)==13

for J in locally:
    allowed=[k for k,(i,j) in enumerate(V) if j!=3 or i in J]
    if J in PRIMAL:
        t,piv=PRIMAL[J];free=[k for k in allowed if k not in piv]
        assert len(piv)==13 and len(free)==12
        rhs=[b[r]-t*sum(A[r][k] for k in free) for r in range(15)]
        vals={k:t for k in free}
        vals.update(zip(piv,solve_overdetermined(piv,rhs)))
        assert len(vals)==25 and all(w>0 for w in vals.values())
        x=[vals.get(k,F(0)) for k in range(28)]
        assert all(sum(A[r][k]*x[k] for k in range(28))==b[r] for r in range(15))
        ee=[E0[ARCS.index((i,j))] if j in (0,6) else x[V.index((i,j))]
            for i,j in ARCS]
        assert all(ee[k]>0 for k,arc in enumerate(ARCS) if arc[1]!=3 or arc[0] in J)
        assert sum(w>0 for w in ee)==27
        arcs=[arc for arc,w in zip(ARCS,ee) if w>0]
        C=[[int(ii==i) for ii,jj in arcs] for i in range(7)]
        C += [[int(jj==j) for ii,jj in arcs] for j in range(7)]
        C += [[R[ii]*int(jj==j) for ii,jj in arcs] for j in range(7)]
        assert rank(C)==15 and len(arcs)-rank(C)==12
        print('EXTENDS',J,'free=',str(t),'min=',str(min(vals.values())),
              'full_support=27','face_dim=12')
    else:
        y=list(map(F,DUAL[J]))
        products=[sum(y[r]*A[r][k] for r in range(15)) for k in allowed]
        objective=sum(y[r]*b[r] for r in range(15))
        assert min(products)>=0 and objective<0
        print('INFEASIBLE',J,'farkas_y_dot_b=',str(objective),'min_yA=',str(min(products)))
print('MIN_SOURCE3_SUPPORT',4,'FOUR_SUPPORT_FACE_COMPONENTS',3,
      'FACE_DIMENSIONS',(12,12,12),'PAIRWISE_INTERSECTIONS','EMPTY')
print('LOCAL_FOUR_MASKS',len(locally),'GLOBAL_REALIZABLE',len(PRIMAL),
      'GLOBAL_INFEASIBLE',len(DUAL),'NONLOCAL',35-len(locally))
print('PASS_EXACT_R5_SOURCE3_GLOBAL_FOUR_MASK_CENSUS_3_OF_7')
