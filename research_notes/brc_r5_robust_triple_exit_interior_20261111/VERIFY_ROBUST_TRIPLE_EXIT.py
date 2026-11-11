#!/usr/bin/env python3
"""Exact robust triple-exit certificate in fixed R5 seven-ratio Blackwell fiber."""
from fractions import Fraction as Q
R=(2,10,15,20,25,30,38)
S=(1,2,3,5)
V=tuple((i,j) for j in S for i in range(7)); IX={a:i for i,a in enumerate(V)}
A=[[int(i==k) for i,j in V] for k in range(7)]
A += [[int(j==p) for i,j in V] for p in S]
A += [[R[i]*int(j==p) for i,j in V] for p in S]
C=tuple(map(Q,('10022571/135903376,74268405/475661816,0,0,0,0,10022571/475661816,'
 '0,122039541/1902647264,196521/67951688,0,0,0,26530335/1902647264,'
 '0,0,11485487/67951688,377644447/2548188300,5499155/67951688,0,831435/33975844,'
 '0,6092151/1902647264,0,0,680265/67951688,2161731/33975844,27135015/1902647264').split(',')))
b=tuple(sum((row[i]*C[i] for i in range(28)),Q(0)) for row in A)
def step(x,j,row,t):
    h=[Q(0)]*28
    for i,v in row.items(): h[IX[(i,3)]]=Q(v);h[IX[(i,j)]]=-Q(v)
    assert all(sum(a*v for a,v in zip(ar,h))==0 for ar in A)
    y=tuple(a+t*v for a,v in zip(x,h))
    assert all(z>=0 for z in y)
    assert tuple(sum((ar[i]*y[i] for i in range(28)),Q(0)) for ar in A)==b
    return y
def slack(x,m):
    c=x[IX[(6,3)]]
    t=c/Q(30-R[m]);return x[IX[(m,3)]]-8*t, x[IX[(5,5)]]-(38-R[m])*t
def mask(x):return tuple(i for i in range(7) if x[IX[(i,3)]]>0)
assert mask(C)==(2,3,4,6)
eps=Q(1,10000)
C1=step(C,5,{2:-13,4:23,6:-10},eps)
assert mask(C1)==(2,3,4,6)
assert all(slack(C1,m)[0]>0 and slack(C1,m)[1]>0 for m in (2,3,4))
print('PERTURBATION_EPS',eps,'SOURCE3_MASK',mask(C1))
for m in (2,3,4):
    t=C1[IX[(6,3)]]/Q(30-R[m])
    y=step(C1,5,{m:-8,5:38-R[m],6:R[m]-30},t)
    assert mask(y)==(2,3,4,5)
    print('STRICT_EXIT',m,'t',t,'slack',*slack(C1,m),'terminal_mask',mask(y))
piv=(16,1,17,18,0,8,26,27,5,20,13,22,2)
allowed=[k for k,(i,j) in enumerate(V) if j!=3 or i in (2,3,4,6)]
free=[k for k in allowed if k not in piv]
assert len(allowed)==25 and len(free)==12
T=Q(1,800)
aug=[[Q(A[r][k]) for k in piv]+[b[r]-T*sum(A[r][k] for k in free)] for r in range(15)]
for col in range(13):
    pivot=next(r for r in range(col,15) if aug[r][col])
    aug[col],aug[pivot]=aug[pivot],aug[col]
    q=aug[col][col]
    aug[col]=[x/q for x in aug[col]]
    for r in range(15):
        if r!=col:
            q=aug[r][col]
            if q:aug[r]=[x-q*y for x,y in zip(aug[r],aug[col])]
assert all(not any(row[:13]) and row[13]==0 for row in aug[13:])
w=[Q(0)]*28
for k in free:w[k]=T
for k in range(13):w[piv[k]]=aug[k][-1]
assert all(w[k]>0 for k in allowed)
assert tuple(sum((ar[i]*w[i] for i in range(28)),Q(0)) for ar in A)==b
eta=Q(1,1000)
Z=tuple((1-eta)*c+eta*d for c,d in zip(C1,w))
assert all(Z[k]>0 for k in allowed) and all(Z[k]==0 for k in range(28) if k not in allowed)
assert all(slack(Z,m)[0]>0 and slack(Z,m)[1]>0 for m in (2,3,4))
for m in (2,3,4):
    t=Z[IX[(6,3)]]/Q(30-R[m])
    Y=step(Z,5,{m:-8,5:38-R[m],6:R[m]-30},t)
    assert mask(Y)==(2,3,4,5)
    allowed_B=[k for k,(i,j) in enumerate(V) if j!=3 or i in (2,3,4,5)]
    assert len(allowed_B)==25 and all(Y[k]>0 for k in allowed_B)
print('FACE_INTERIOR_WITNESS', 'allowed_dynamic_positive',sum(Z[k]>0 for k in allowed),'eta',eta)
print('FACE_INTERIOR_EXIT_MIN_MARGIN',min(min(slack(Z,m)) for m in (2,3,4)))
print('PASS_EXACT_R5_ROBUST_TRIPLE_EXIT_FACE_INTERIOR')
