#!/usr/bin/env python3
"""Exact one-edge transverse lift of an R5 seven-LR-node Blackwell coupling.
All checks use Python standard library Fraction, including both end points.
"""
from fractions import Fraction as F
R=tuple(map(F,'1/10 1/2 3/4 1 5/4 3/2 19/10'.split()))
X=tuple(map(F,'999/1000 1/6 999/1000 1/20 29/240 11/160 1/120'.split()))
Y=tuple(map(F,'1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200'.split()))
S=((0,0),(0,1),(3,1),(5,1),(0,2),(2,2),(3,2),(2,3),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
E0=tuple(map(F,'33553/432000 3997/432000 3997/540000 0 510479933/29442744000 2893155797/8178540000 6636239129/147213720000 222511289/4089270000 318755011/3680343000 222511289/4089270000 172449787/1363090000 219439/545236000 172449787/2180944000 38053/432000'.split()))
D=tuple(map(F,'-247/1620 3211/14580 -22477/36450 3211/8100 -247/3645 494/2025 -3211/18225 -494/2025 3211/4050 -494/2025 494/2025 -3211/8100 247/1620 -247/1620'.split()))
HI=F(17774559,17507527960)
SA={(0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),(3,3),(1,5),(2,5),(4,5),(5,5),(6,5)}
SB={(0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),(0,5),(1,5),(3,5),(4,5),(5,5),(6,5)}
ATLAS=SA|SB

def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,(g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(f):
    g,a,b,u,v,w,z=f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)
def slack(f):
    g,a,b,u,v,w,z=f
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def x(e):return (*X[:6],X[6]+e)
def weights(e):return tuple(a+e*d for a,d in zip(E0,D))
def check(e):
    src=x(e);nu=mass(src);mu=mass(Y);W=weights(e)
    assert len(S)==len(set(S))==14 and len(W)==14
    assert src[0]==src[2] and Y[0]==1 and Y[6]==Y[1]/10
    assert min(slack(src)+slack(Y))>=0
    assert times(src)==times(Y)==(F(17609,6000),F(33857,12000))
    assert sum(nu)==sum(mu)==1 and min(nu+mu)>=0
    assert min(W)>=0
    for i in range(7):
        assert sum((v for (ii,j),v in zip(S,W) if ii==i),F(0))==mu[i]
    for j in range(7):
        assert sum((v for (i,jj),v in zip(S,W) if jj==j),F(0))==nu[j]
        assert sum((R[i]*v for (i,jj),v in zip(S,W) if jj==j),F(0))==R[j]*nu[j]
    Phi=F(23,5)*(mu[0]-nu[0])+3*(mu[1]-nu[1])+2*(mu[2]-nu[2])+mu[3]-nu[3]
    assert Phi==F(3211,8100)*e==W[S.index((5,1))]
    gap=sum((v for edge,v in zip(S,W) if edge not in ATLAS),F(0))
    assert gap==F(8555233477,73606860000)-F(51623,72900)*e
    return sum(v>0 for v in W),gap,Phi

assert HI<F(1,120)
assert -E0[S.index((5,5))]/D[S.index((5,5))]==HI
assert all(w>0 for w in E0 if w!=0) and E0[S.index((5,1))]==0
assert all(w+HI*d>=0 for w,d in zip(E0,D))
assert all(w+HI*d>0 for e,w,d in zip(S,E0,D) if e!=(5,5))
for e,n in ((F(0),13),(F(1,100000),14),(F(1,1000),14),(HI,13)):
    count,_,_=check(e)
    assert count==n
print('PASS_BOTH_ENDPOINTS_21_LR_COUPLING_EQUATIONS_AND_ALL_PHYSICAL_SLACKS')
print('PASS_AFFINE_IDENTITY_THEREFORE_ALL_REAL_EPSILON_IN_CLOSED_INTERVAL')
print('PASS_UNIQUE_TRANSVERSE_BRIDGE_EDGE_(5,1)_PHI_EXACT')
print('PASS_14_POSITIVE_EDGES_OPEN_INTERVAL_AND_13_AT_ENDPOINTS')
print('MAXIMAL_EPSILON_FOR_THIS_NONNEGATIVE_14_EDGE_AFFINE_CHART',HI)
print('EXACT_ATLAS_ESCAPE_COST','8555233477/73606860000 - (51623/72900)*epsilon')
print('EPSILON_1/1000',check(F(1,1000)))


# Four-parameter extension of the immutable PR #1873 exact verifier.
from itertools import product

def vector(s): return tuple(map(F, s.split()))
U=(vector('1/2 -7/2 1/2 1 0 0 0'),
   vector('-1/2 -1/2 -1/2 0 1 0 0'),
   vector('-3/2 5/2 -3/2 0 0 1 0'),
   vector('0 0 0 0 0 0 1'))
V=(vector('509/900 -1013/900 -19997/18000 421/4000 14/25 -2/125 182/125 2/125 -6211/18000 2/125 -2/125 -421/4000 -1/100 1/100'),
   vector('67/162 -871/1458 77869/58320 -11749/12960 134/729 -268/405 1742/3645 268/405 -11749/6480 268/405 -268/405 11749/12960 -67/162 67/162'),
   vector('1/100 2383/8100 123727/162000 -9511/36000 -616/2025 -1018/1125 -8008/10125 1018/1125 163/6000 1018/1125 -1018/1125 9511/36000 -509/900 509/900'),
   D)
rho_star=F(17774559,225414193300)

def combine(base, directions, params):
    return tuple(a+sum((p*d[k] for p,d in zip(params,directions)),F(0)) for k,a in enumerate(base))
def rank(rows):
    m=[list(map(F,row)) for row in rows]
    i=0
    for k in range(len(m[0])):
        pivot=next((t for t in range(i,len(m)) if m[t][k]),None)
        if pivot is None: continue
        m[pivot],m[i]=m[i],m[pivot]
        div=m[i][k];m[i]=[z/div for z in m[i]]
        for t in range(i+1,len(m)):
            f=m[t][k]
            if f:m[t]=[a-f*b for a,b in zip(m[t],m[i])]
        i+=1
        if i==len(m):break
    return i

nu0=mass(X);mu0=mass(Y)
for u,v in zip(U,V):
    dnu=tuple(a-b for a,b in zip(mass(combine(X,(u,),(F(1),))),nu0))
    assert u[0]==u[2]
    assert times(combine(X,(u,),(F(1),)))==times(X)
    for i in range(7): assert sum((z for (ii,j),z in zip(S,v) if ii==i),F(0))==0
    for j in range(7):
        assert sum((z for (i,jj),z in zip(S,v) if jj==j),F(0))==dnu[j]
        assert sum((R[i]*z for (i,jj),z in zip(S,v) if jj==j),F(0))==R[j]*dnu[j]

# Exact 24-by-21 augmented transport-flow constraint matrix.
cm=[[F(0)]*21 for _ in range(24)]
for k,(i,j) in enumerate(S):
    cm[i][k]=1;cm[7+j][k]=1;cm[14+j][k]=R[i]
for k in range(7):
    basis=tuple(F(int(t==k)) for t in range(7))
    dn=tuple(a-b for a,b in zip(mass(combine(X,(basis,),(F(1),))),nu0))
    dt=tuple(a-b for a,b in zip(times(combine(X,(basis,),(F(1),))),times(X)))
    for j in range(7):cm[7+j][14+k]=-dn[j];cm[14+j][14+k]=-R[j]*dn[j]
    cm[21][14+k]=F(int(k==0))-F(int(k==2))
    cm[22][14+k]=dt[0];cm[23][14+k]=dt[1]
assert rank(cm)==17 and rank([row[:14] for row in cm[:21]])==14
assert rank([[u[i] for u in U] for i in range(7)])==4
obs=[[mass(combine(X,(u,),(F(1),)))[i]-nu0[i] for u in U] for i in range(7)]
assert rank(obs)==3
(a,b,c)=([obs[i][k] for k in range(3)] for i in range(3))
det=a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
assert det==-F(295513,324000)
k=vector('-33345/591026 132145/295513 -33345/591026 1')
assert combine((F(0),)*14,V,k)==(F(0),)*14
assert combine((F(0),)*7,U,k)==vector('-49400/295513 -49400/295513 -49400/295513 -33345/591026 132145/295513 -33345/591026 1')

atlas_gap0=F(8555233477,73606860000)
atlas_gap_deriv=vector('-35053/36000 40873/23328 748223/324000 -51623/72900')
assert sum(E0[i] for i,e in enumerate(S) if e not in ATLAS)==atlas_gap0
for t in range(4):
    assert sum(V[t][i] for i,e in enumerate(S) if e not in ATLAS)==atlas_gap_deriv[t]

def verify_box(rho,positive):
    smallest_slack=[];smallest_edge=[];zeros=[]
    for eps in (HI/4,3*HI/4):
        for signs in product((-1,1),repeat=3):
            pp=tuple(rho*s for s in signs)+(eps,)
            xx=combine(X,U,pp); ee=combine(E0,V,pp)
            assert xx[0]==xx[2] and Y[0]==1 and Y[6]==Y[1]/10
            assert times(xx)==times(Y)==(F(17609,6000),F(33857,12000))
            nu=mass(xx); mu=mu0
            assert sum(nu)==sum(mu)==1 and min(nu+mu)>=0
            assert min(slack(xx)+slack(Y))>=0 and min(ee)>=0
            for i in range(7): assert sum((z for (ii,j),z in zip(S,ee) if ii==i),F(0))==mu[i]
            for j in range(7):
                assert sum((z for (i,jj),z in zip(S,ee) if jj==j),F(0))==nu[j]
                assert sum((R[i]*z for (i,jj),z in zip(S,ee) if jj==j),F(0))==R[j]*nu[j]
            phi=F(23,5)*(mu[0]-nu[0])+3*(mu[1]-nu[1])+2*(mu[2]-nu[2])+mu[3]-nu[3]
            assert phi==ee[S.index((5,1))]
            assert sum(ee[i] for i,e in enumerate(S) if e not in ATLAS)==atlas_gap0+sum(p*d for p,d in zip(pp,atlas_gap_deriv))
            smallest_slack.extend(z for i,z in enumerate(slack(xx)) if i!=4)
            smallest_edge.extend(ee)
            if 0 in ee:zeros.append((eps,signs,S[ee.index(F(0))]))
    if positive:assert not zeros
    return min(smallest_slack),min(smallest_edge),zeros

s,e,z=verify_box(F(1,100000),True)
assert s==F(39,40000) and e==F(15520417067,176656464000000)
s2,e2,z2=verify_box(rho_star,False)
assert s2==F(904888979,1127070966500) and e2==0
assert z2==[(HI/4,(-1,1,1),(5,1)),(3*HI/4,(1,-1,-1),(5,5))]
assert combine(E0,V,(-(rho_star+F(1,10**9)),rho_star+F(1,10**9),rho_star+F(1,10**9),HI/4))[S.index((5,1))]<0
print('PASS_R5_FOUR_PARAMETER_RANK_17_NULLITY_4_OBSERVER_RANK_3')
print('PASS_R5_RHO_1E-5_ALL_16_VERTICES',s,e)
print('PASS_R5_SHARP_RADIUS_ALL_16_VERTICES',rho_star,s2,e2)
print('PASS_R5_SHARP_BOX_BOUNDARY_ZEROS',z2)
print('PASS_R5_14_STRICT_EDGES_FOR_EVERY_REAL_PARAMETER_INSIDE_OPEN_RADIUS_BOX')
