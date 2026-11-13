#!/usr/bin/env python3
"""Exact R5: sharp 15-atom maximal feasible ray; Python stdlib only."""
from fractions import Fraction as F
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

def obs(x):
    return tuple(sum((row[k]*x[k] for k in range(28)),F(0)) for row in A)

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
C=tuple(map(F,('10022571/135903376,74268405/475661816,0,0,0,0,10022571/475661816,'
 '0,122039541/1902647264,196521/67951688,0,0,0,26530335/1902647264,'
 '0,0,11485487/67951688,377644447/2548188300,5499155/67951688,0,831435/33975844,'
 '0,6092151/1902647264,0,0,680265/67951688,2161731/33975844,27135015/1902647264').split(',')))
assert len(X)==len(C)==28 and min(X)>0 and obs(X)==obs(C)
b=obs(C)

def basis(i):
    h=[0]*7
    h[0]=R[i]-R[6]
    h[i]=R[6]-R[0]
    h[6]=R[0]-R[i]
    assert sum(h)==sum(r*a for r,a in zip(R,h))==0
    return h

def atom(j,i):
    v=[F(0)]*28
    for k,a in enumerate(basis(i)):
        v[IX[(k,j)]]+=a
        v[IX[(k,3)]]-=a
    assert not any(obs(v))
    return tuple(v)

coeff={1:(12,8,1,13,8), 2:(3,13,7,4,2), 5:(-15,-21,-8,-17,-10)}
assert all(sum(coeff[j][i] for j in J)==0 for i in range(5))
steps=[(j,i,F(coeff[j][i-1],36),atom(j,i)) for j in J for i in range(1,6)]
D=tuple(sum((a*v[k] for _,_,a,v in steps),F(0)) for k in range(28))
assert any(D) and not any(obs(D))
assert all(D[IX[(i,3)]]==0 for i in range(7))
eps_max=min(-X[k]/D[k] for k in range(28) if D[k]<0)
assert eps_max==F(9,115400000)
end=tuple(x+eps_max*d for x,d in zip(X,D))
assert min(end)==0 and obs(end)==b

order=((2,2),(1,2),(1,3),(2,3),(2,5),(5,4),(1,4),(5,5),
       (2,4),(1,5),(5,1),(2,1),(5,3),(1,1),(5,2))
assert len(order)==len(set(order))==15
lookup={(j,i):(a,v) for j,i,a,v in steps}
state=list(X)
for j,i in order:
    a,v=lookup[(j,i)]
    state=[z+eps_max*a*t for z,t in zip(state,v)]
    assert min(state)>=0 and obs(state)==b
assert tuple(state)==end

def prefix_limit(seq):
    p=[F(0)]*28
    limit=None
    for j,i in seq:
        a,v=lookup[(j,i)]
        p=[z+a*t for z,t in zip(p,v)]
        for k in range(28):
            if p[k]<0:
                t=-X[k]/p[k]
                limit=t if limit is None else min(t,limit)
    return limit

sorted_order=tuple((j,i) for j in J for i in range(1,6))
sorted_limit=prefix_limit(sorted_order)
reordered_limit=prefix_limit(order)
assert sorted_limit==F(155682221,377131868400000000)
assert sorted_limit<eps_max and reordered_limit==eps_max

# Exact finite rank/non-membership certificate: all 4-atom dictionary spans.
P=2147483647
assert factorial(4)*36**4<P
directions=[]
for a,bb,c in combinations(range(7),3):
    v=[0]*7
    v[a]=R[bb]-R[c]
    v[bb]=R[c]-R[a]
    v[c]=R[a]-R[bb]
    directions.append(tuple(v[1:6]))
assert len(directions)==35

def mod_normal(rows):
    m=[[v%P for v in row] for row in rows]
    piv=[]
    for col in range(5):
        k=next((i for i in range(len(piv),4) if m[i][col]),None)
        if k is None:continue
        rank=len(piv)
        m[k],m[rank]=m[rank],m[k]
        inv=pow(m[rank][col],-1,P)
        m[rank]=[(v*inv)%P for v in m[rank]]
        for i in range(4):
            if i!=rank and m[i][col]:
                q=m[i][col]
                m[i]=[(v-q*t)%P for v,t in zip(m[i],m[rank])]
        piv.append(col)
        if len(piv)==4:break
    if len(piv)<4:return None
    free=next(i for i in range(5) if i not in piv)
    n=[0]*5
    n[free]=1
    for i,col in enumerate(piv):n[col]=(-m[i][free])%P
    return tuple(n)

normals=set()
rank4=lower=0
for quad in combinations(directions,4):
    n=mod_normal(quad)
    if n is None:lower+=1
    else:rank4+=1;normals.add(n)
assert (rank4,lower,len(normals))==(46198,6162,3468)
assert all(all(sum(n[i]*cj[i] for i in range(5))%P for n in normals)
           for cj in coeff.values())

print('FROZEN_OBSERVER_MATCH',obs(X)==obs(C))
print('X_FULL_SUPPORT',all(x>0 for x in X))
print('RAY_ENDPOINT_MAX_EPS',eps_max)
print('SORTED_15_WORD_FEASIBILITY_LIMIT',sorted_limit)
print('REORDERED_15_WORD_FEASIBILITY_LIMIT',reordered_limit)
print('ORDER',order)
print('ALL_15_INTERMEDIATE_STATES_NONNEGATIVE_AT_ENDPOINT',True)
print('SOURCE3_ROW_PRESERVED',all(end[IX[(i,3)]]==X[IX[(i,3)]] for i in range(7)))
print('EXACT_FOUR_DICTIONARY_CENSUS',rank4+lower,'RANK4',rank4,'RANK_LT4',lower,'NORMALS',len(normals))
print('RAY_ATOMIC_DISTANCE_FOR_ALL_0_LT_EPS_LE_MAX',15)
print('PASS_R5_SHARP_NONLOCAL_15_ATOM_FULL_FEASIBLE_RAY')
