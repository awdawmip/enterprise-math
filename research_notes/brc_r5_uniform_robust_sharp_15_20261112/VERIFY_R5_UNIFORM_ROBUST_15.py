#!/usr/bin/env python3
"""Exact independent finite reproduction: frozen R5 robust sharp 15-step rectangle.
28 rational masses, 15 labeled atoms, same observer; Python stdlib only.
"""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from math import factorial

R=(2,10,15,20,25,30,38)
J=(1,2,5)
PORTS=(1,2,3,5)
V=tuple((i,j) for j in PORTS for i in range(7))
IX={v:k for k,v in enumerate(V)}
A=[[int(i==t) for i,j in V] for t in range(7)]
A += [[int(j==p) for i,j in V] for p in PORTS]
A += [[R[i]*int(j==p) for i,j in V] for p in PORTS]

def obs(y):
    return tuple(sum((row[k]*y[k] for k in range(28)),F(0)) for row in A)

X=tuple(map(F,('250555781039/3397584400000,854053219229681/5470110884000000,'
 '155682221/156288882400000,1/800000,1/800000,19487331497/781444412000000,'
 '1001314300627/47566181600000,1/800000,6101786845061/95132363200000,'
 '19640941861/6795168800000,1/800000,1/800000,1/800000,1326387507069/95132363200000,'
 '155682221/25142124560000000,155682221/25142124560000000,'
 '969901373288483/5782688648800000,1627075388860003/11721666180000000,'
 '14139282599219/169879220000000,165067666637733/7814444120000000,'
 '1696529496568917/144567216220000000,31271973479/25142124560000000,'
 '12993863727852929/4047882054160000000,7517305745629/5782688648800000,'
 '36686587724849/3907222060000000,1308842702731/169879220000000,'
 '331925821992147/7814444120000000,54684907960963337/2023941027080000000').split(',')))
assert len(X)==28 and min(X)>0

def basis(i):
    h=[0]*7
    h[0]=R[i]-R[6]; h[i]=R[6]-R[0]; h[6]=R[0]-R[i]
    assert sum(h)==sum(r*a for r,a in zip(R,h))==0
    return h

def atom(j,i):
    v=[0]*28
    for k,a in enumerate(basis(i)):
        v[IX[(k,j)]]+=a
        v[IX[(k,3)]]-=a
    assert not any(obs(v))
    return tuple(v)

coeff={1:(12,8,1,13,8),2:(3,13,7,4,2),5:(-15,-21,-8,-17,-10)}
assert all(sum(coeff[j][i] for j in J)==0 for i in range(5))
steps=[(j,i,F(coeff[j][i-1],36),atom(j,i)) for j in J for i in range(1,6)]
assert len(steps)==15
moves=[tuple(a*t for t in v) for j,i,a,v in steps]
D=tuple(sum((m[k] for m in moves),F(0)) for k in range(28))
assert not any(obs(D))
assert all(D[IX[(i,3)]]==0 for i in range(7))
eps=F(9,115400000)
assert min(-X[k]/D[k] for k in range(28) if D[k]<0)==eps
x=F(155682221,25142124560000000)
assert X[IX[(0,3)]]==X[IX[(1,3)]]==x
H=[0]*28
for i,c in ((1,-23),(2,28),(6,-5)):
    H[IX[(i,3)]]=c
    H[IX[(i,1)]]=-c
assert not any(obs(H))
L=F(-427508577031693280,628800490619)
U=F(1,23)
root=lambda q:(1-F(q)*eps/x)/23
rho=tuple(root(q) for q in (15,12,3))
assert L<rho[0]<rho[1]<rho[2]<0<U

# Exactly solve the parameter-feasible interval for every one of 2^15 masks.
N=1<<15
partial=[(F(0),)*28]+[None]*(N-1)
for s in range(1,N):
    b=s&-s; a=b.bit_length()-1
    partial[s]=tuple(partial[s^b][k]+moves[a][k] for k in range(28))

intervals=[]
for s in range(N):
    lo,hi=L,U
    for k in range(28):
        q=X[k]+eps*partial[s][k]
        slope=x*H[k]
        if slope>0: lo=max(lo,-q/slope)
        elif slope<0: hi=min(hi,-q/slope)
        elif q<0: lo,hi=F(1),F(0);break
    intervals.append((lo,hi) if lo<=hi else None)

valid_intervals=[a for a in intervals if a is not None]
assert len(valid_intervals)==16462
assert all(a[0]==L for a in valid_intervals)
exit_count=Counter(a[1] for a in valid_intervals if a[1]<U)
assert exit_count==Counter({rho[0]:3592,rho[1]:3347,rho[2]:2414})

robust=[s for s,a in enumerate(intervals) if a and a[1]==U]
assert len(robust)==7109
assert all(intervals[s]==(L,U) for s in robust)

# Exhaustive rectangle-vertex check: 7,109 masks x 4 vertices x 28 masses.
for s in robust:
    for r in (L,U):
        for e in (F(0),eps):
            assert all(X[k]+x*r*H[k]+e*partial[s][k]>=0 for k in range(28))

good=set(robust)
dp=[0]*N; dp[0]=1
for s in range(1,N):
    if s in good:
        b=s
        while b:
            p=b&-b
            dp[s]+=dp[s^p]
            b-=p
assert dp[-1]==3514190816

word=((2,2),(1,2),(1,3),(2,3),(2,5),(5,4),(1,4),(5,5),
      (2,4),(1,5),(5,1),(2,1),(5,3),(1,1),(5,2))
keys=[(j,i) for j,i,a,v in steps]
s=0
for label in word:
    s|=1<<keys.index(label)
    assert s in good
assert s==N-1

# Fresh exact modular rank certificate: every four-atom subspace per port.
p=2147483647
assert factorial(4)*36**4<p
directions=[]
for a,b,c in combinations(range(7),3):
    v=[0]*7
    v[a]=R[b]-R[c]; v[b]=R[c]-R[a]; v[c]=R[a]-R[b]
    directions.append(tuple(v[1:6]))
assert len(directions)==35

def normal_mod(rows):
    m=[[q%p for q in row] for row in rows]
    piv=[]
    for col in range(5):
        rank=len(piv)
        k=next((i for i in range(rank,4) if m[i][col]),None)
        if k is None:continue
        m[k],m[rank]=m[rank],m[k]
        inv=pow(m[rank][col],-1,p)
        m[rank]=[(a*inv)%p for a in m[rank]]
        for i in range(4):
            if i!=rank and m[i][col]:
                factor=m[i][col]
                m[i]=[(a-factor*b)%p for a,b in zip(m[i],m[rank])]
        piv.append(col)
        if len(piv)==4:break
    if len(piv)<4:return None
    free=next(i for i in range(5) if i not in piv)
    n=[0]*5;n[free]=1
    for i,col in enumerate(piv):n[col]=(-m[i][free])%p
    return tuple(n)

normals=set()
rank4=ranklt4=0
for quad in combinations(directions,4):
    n=normal_mod(quad)
    if n is None:ranklt4+=1
    else:rank4+=1;normals.add(n)
assert (rank4,ranklt4,len(normals))==(46198,6162,3468)
assert all(all(sum(n[i]*v[i] for i in range(5))%p for n in normals)
           for v in coeff.values())

print('FROZEN_FIXTURE_COMMIT','435e77af0d180eac32bd1f9c4c464bc4010b7551')
print('PARAMETER_INTERVAL',L,U)
print('EPSILON_INTERVAL',F(0),eps)
print('ADMISSIBLE_MASKS_ALL_R_AND_EPS',len(robust))
print('UNIVERSAL_COMPLETE_WORDS',dp[-1])
print('THREE_LOSS_GATES',rho)
print('SAME_FIXED_15_STEP_WORD_VALID_ON_ENTIRE_RECTANGLE',True)
print('RECTANGLE_ALL_FOUR_CORNERS_TESTED_EXACTLY',True)
print('MODULAR_FOUR_ATOM_SPANS_CHECKED',rank4+ranklt4,'DISTINCT_HYPERPLANES',len(normals))
print('RAY_SHARP_DISTANCE_FOR_ALL_R_AND_NONZERO_EPS',15)
print('PASS_R5_UNIFORM_ROBUST_SHARP_15_RECTANGLE')
