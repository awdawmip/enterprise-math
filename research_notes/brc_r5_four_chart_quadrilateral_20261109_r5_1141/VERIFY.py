#!/usr/bin/env python3
"""Exact R5 four-chart 14-edge region and 16-edge coupling quadrilateral.
Standard library Fraction, exhaustive finite vertex enumeration, affine certificate.
"""
from fractions import Fraction as F
from itertools import combinations
def Q(s): return tuple(map(F,s.split()))
R=Q('1/10 1/2 3/4 1 5/4 3/2 19/10')
X0=Q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
X1=Q('1 1/10 1 27/800 1/100 27/400 1/100')
Y0=Q('871/1000 9/40 5/6 273/4000 21/100 143/1000 9/400')
Y1=Q('4673/6400 1311/6400 4673/6400 38759/512000 47301/256000 103999/512000 1311/64000')
SA=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),(3,3),(1,5),(2,5),(4,5),(5,5),(6,5))
SB=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),(0,5),(1,5),(3,5),(4,5),(5,5),(6,5))
U=tuple(sorted(set(SA)|set(SB)))
assert len(U)==16

def masses(f):
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
def model(p):
    g,a,u,v,w,z,G,A,B=p
    x=(g,a,g,u,v,w,z);P,Q=times(x)
    U0=-F(17,40)*A-F(19,80)*B-G/2-P+F(3,2)*Q-F(1,2)
    W0=-F(7,40)*A-F(39,80)*B-G/2+P-Q/2-F(1,2)
    return x,(G,A,B,U0,A/10+F(9,40)*B,W0,A/10)
def slacks(f):
    g,a,b,u,v,w,z=f
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def operator(support):
    return ([[F(i==a) for a,b in support] for i in range(7)]+
            [[F(j==b) for a,b in support] for j in range(7)]+
            [[R[a] if j==b else F(0) for a,b in support] for j in range(7)])
def target(x,y):
    nu=masses(x);mu=masses(y)
    return tuple(mu+nu+tuple(R[i]*nu[i] for i in range(7)))
def solve(A,b):
    n=len(A[0]);M=[list(map(F,row))+[F(t)] for row,t in zip(A,b)]
    piv=0
    for k in range(n):
        j=next((i for i in range(piv,len(M)) if M[i][k]),None)
        assert j is not None,('rank',k)
        M[piv],M[j]=M[j],M[piv]
        d=M[piv][k];M[piv]=[v/d for v in M[piv]]
        for i in range(len(M)):
            if i!=piv and M[i][k]:
                c=M[i][k];M[i]=[v-c*w for v,w in zip(M[i],M[piv])]
        piv+=1
    assert all(all(v==0 for v in row[:n]) and row[-1]==0 for row in M[n:])
    sol=tuple(M[i][-1] for i in range(n))
    assert tuple(sum(row[j]*sol[j] for j in range(n)) for row in A)==tuple(b)
    return sol
def rank(A):
    M=[list(map(F,row)) for row in A];j=0
    for col in range(len(M[0])):
        p=next((i for i in range(j,len(M)) if M[i][col]),None)
        if p is None:continue
        M[j],M[p]=M[p],M[j];d=M[j][col];M[j]=[v/d for v in M[j]]
        for i in range(j+1,len(M)):
            if M[i][col]:
                c=M[i][col];M[i]=[v-c*w for v,w in zip(M[i],M[j])]
        j+=1
        if j==len(M):break
    return j
def det(A):
    M=[list(map(F,row)) for row in A];n=len(M);d=F(1)
    assert all(len(row)==n for row in M)
    for j in range(n):
        p=next((i for i in range(j,n) if M[i][j]),None)
        if p is None:return F(0)
        if j!=p:M[j],M[p]=M[p],M[j];d=-d
        v=M[j][j];d*=v
        for i in range(j+1,n):
            if M[i][j]:
                c=M[i][j]/v
                for k in range(j+1,n):M[i][k]-=c*M[j][k]
                M[i][j]=F(0)
    return d

xh=tuple((a+b)/2 for a,b in zip(X0,X1))
yh=tuple((a+b)/2 for a,b in zip(Y0,Y1))
p0=tuple(xh[i] for i in (0,1,3,4,5,6))+tuple(yh[i] for i in (0,1,2))
assert model(p0)==(xh,yh)
assert p0==Q('1999/2000 2/15 67/1600 157/2400 109/1600 11/1200 51237/64000 2751/12800 30019/38400')
AU=operator(U)
assert rank(AU)==14
k1={(0,2):-F(5,13),(0,5):F(5,13),(2,2):F(18,13),
    (2,5):-F(18,13),(3,2):-F(1),(3,5):F(1)}
k2={(0,2):-F(15,13),(0,5):F(15,13),(2,2):F(28,13),
    (2,5):-F(28,13),(5,2):-F(1),(5,5):F(1)}
K1=tuple(k1.get(edge,F(0)) for edge in U)
K2=tuple(k2.get(edge,F(0)) for edge in U)
assert all(sum(row[i]*K1[i] for i in range(16))==0 for row in AU)
assert all(sum(row[i]*K2[i] for i in range(16))==0 for row in AU)
assert K1[U.index((3,5))]==1 and K2[U.index((5,2))]==-1
b0=target(xh,yh)
w0=solve(operator(SA),b0)
reference=tuple(dict(zip(SA,w0)).get(e,F(0)) for e in U)
assert min(w0)>0
vertices={}
for i,j in combinations(range(16),2):
    a,b,c,d=K1[i],K2[i],K1[j],K2[j]
    delta=a*d-b*c
    if delta==0:continue
    s=(-reference[i]*d+b*reference[j])/delta
    t=(-a*reference[j]+c*reference[i])/delta
    e=tuple(reference[k]+s*K1[k]+t*K2[k] for k in range(16))
    if all(v>=0 for v in e):vertices[(s,t)]=e
assert len(vertices)==4
zero_sets={frozenset(U[i] for i,v in enumerate(e) if not v) for e in vertices.values()}
expected={frozenset(v) for v in (
    ((0,5),(3,5)),((3,5),(5,2)),((2,5),(5,2)),((0,5),(2,5)))}
assert zero_sets==expected
assert all(sum(v>0 for v in e)==14 for e in vertices.values())
print('PASS_EXACT_16_EDGE_RANK',rank(AU),'NULLITY',16-rank(AU))
for (s,t),e in sorted(vertices.items()):
    print('VERTEX',s,t,'POSITIVE',sum(v>0 for v in e),
          'ZERO_EDGES',str(tuple(U[i] for i,v in enumerate(e) if not v)))
print('PASS_EXHAUSTIVE_120_CANDIDATE_PAIRS_FOUR_VERTICES')
supports=tuple(tuple(edge for edge in U if edge not in zz)
               for zz in sorted(expected,key=lambda a:tuple(sorted(a))))
assert len(supports)==4
p_basis=[p0]
for j in range(9):
    q=list(p0);q[j]+=1;p_basis.append(tuple(q))
for p in p_basis:
    x,y=model(p)
    assert times(x)==times(y)
    assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert sum(masses(x))==sum(masses(y))==F(1)
    assert sum(r*m for r,m in zip(R,masses(x)))==sum(r*m for r,m in zip(R,masses(y)))==F(1)
values={}
for chart,s in enumerate(supports):
    A=operator(s);sol=[solve(A,target(*model(p))) for p in p_basis]
    assert all(v>0 for v in sol[0])
    values.update({('chart'+str(chart),edge):
                   (sol[0][i],tuple(sol[j+1][i]-sol[0][i] for j in range(9)))
                   for i,edge in enumerate(s)})
    print('PASS_14_EDGE_CHART',chart,'MISSING',
          str(tuple(e for e in U if e not in s)),'MIN_EDGE',min(sol[0]))
for side,idx in [('source',0),('target',1)]:
    ls=[slacks(model(p)[idx]) for p in p_basis]
    values.update({(side,i):
                   (ls[0][i],tuple(ls[j+1][i]-ls[0][i] for j in range(9)))
                   for i in range(13)})
ratios=[]
for name,(v,gradient) in values.items():
    L=sum(abs(z) for z in gradient)
    if v==0:assert L==0,('non-permanent zero',name)
    elif L>0:ratios.append((v/L,name,v,L))
    else:assert v>0
rho,name,v,L=min(ratios,key=lambda q:q[0])
assert rho==F(5194221,10938329600)
assert name==('chart2',(3,5))
assert v==F(1731407,691200000)
assert L==F(854557,162000)
assert rho>F(1,2500)
print('PASS_FULL_NINE_PARAMETER_COMMON_BOX_RADIUS',F(1,2500))
print('EXACT_SHARP_CENTRAL_SLACK_OVER_L1',rho,
      'LIMITING',name,'SLACK',v,'L1',L)
def phi(p):
    x,y=model(p)
    return masses(y)[:5]+masses(x)[:3]
phis=[phi(p) for p in p_basis]
cols=[tuple(phis[j+1][i]-phis[0][i] for i in range(8))
      for j in (0,1,2,3,4,6,7,8)]
d=det(tuple(zip(*cols)))
assert d==-F(1111424393,139968000000)
print('PASS_OBSERVER_EIGHT_DIMENSIONAL_MINOR',d)
print('THEOREM_FOUR_DISTINCT_14_EDGE_CHARTS_OVER_COMMON_9D_PHYSICAL_BOX')
