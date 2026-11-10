#!/usr/bin/env python3
"""Exact 18-arc face of frozen 7-likelihood-ratio R5 Blackwell model.
Source lineage: PR #1954, commit 6f01b6424cc5563db7976fa8131ef687c15091ca.
Self-contained: Python fractions and SymPy; no previous file execution.
"""
from fractions import Fraction as F
from itertools import combinations, product
import sympy as S

def Q(s):return tuple(F(t) for t in s.split())
def mass(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
      F(13,40)*a+b/80-u,(g-a)/2,
      1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
      (g-b)/2,F(3,40)*a+F(21,80)*b-w,
      u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,1+g+(a+b)/2+u+v+w)
def restrictions(p):
    x,y=p[:7],p[7:]
    return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,*(a-b for a,b in zip(times(x),times(y))))
def slacks(x):
    g,a,b,u,v,w,z=x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,
       F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def phys(p):return slacks(p[:7])+slacks(p[7:])
def jac(fun):
    zero=(F(0),)*14
    f0=fun(zero)
    return S.Matrix([[S.Rational(fun(tuple(F(j==k) for j in range(14)))[i]-f0[i])
         for k in range(14)]for i in range(len(f0))])
J=jac(restrictions)
N=J.nullspace()
P=S.Matrix.hstack(*(N[i] for i in (0,1,2,4,5,6,7,8)))
X=Q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y=Q('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
DY=Q('0 1 0 -1/4 -1/4 0 1/10')
H=F(17774559,17507527960)
p=tuple(X[:6]+(X[6]+H/2,))+tuple(y+F(1,100000)*d for y,d in zip(Y,DY))
assert restrictions(p)==(F(0),)*5
star=S.Rational(23,17050000)
tstar=S.Matrix([0,0,0,-star,star,0,0,-star])
pstar=S.Matrix(p)+P*tstar
center=S.Matrix(phys(tuple(F(v) for v in pstar)))
A=jac(phys)*P
R=S.Rational(49948501046391,3920403670319950000)
zc=R*S.Matrix([-1,1,1,-1,-1,-1,-1,1])
r=tuple(F(v) for v in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
def rhs(u):
    mu,nu=mass(u[7:]),mass(u[:7]);return mu+nu+tuple(r[j]*nu[j] for j in range(7))
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
FSET=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def edgecol(e):
    i,j=e;v=[F(0)]*21;v[i]=1;v[7+j]=1;v[14+j]=r[i];return S.Matrix(v)
C=S.Matrix.hstack(*(S.Matrix([edgecol(e)[i]*(20 if i>=14 else 1) for i in I]) for e in D))
FC=C[:,[D.index(e) for e in FSET]]
L=S.Matrix.vstack(*(t.T for t in FC.T.nullspace()))
hsc=S.Matrix([rhs(p)[i]*(20 if i>=14 else 1) for i in I]);B=jac(rhs)*P
T=S.Matrix([[B[I[i],k]*(20 if I[i]>=14 else 1) for k in range(8)] for i in range(15)])
q0=hsc+T*(tstar+zc)
assert FC.rank()==10 and L.shape==(5,15) and C.rank()==15
assert all(x>=0 for x in center + A*zc)
normal=(34101,-293725,-85599,42525,937899,293725,85599,-3287440)
assert list(64800*S.Matrix([[0,-25,1,1,1]])*L*T)==list(normal)

choice_groups=(((2,1),(3,1),(4,1)),((3,2),(4,2)),((0,3),(2,3)))
common=(1,5)
extra=tuple(e for gg in choice_groups for e in gg)+(common,)
face_arcs=FSET+extra
Fmat=C[:,[D.index(e) for e in face_arcs]]
assert len(D)==30 and len(face_arcs)==18 and Fmat.rank()==14
left=Fmat.T.nullspace()
assert len(left)==1 and (left[0].T*q0)[0]==0
slope=list(left[0].T*T)
ratio=slope[0]/normal[0]
assert ratio!=0 and slope==[ratio*v for v in normal]
assert [i for i,v in enumerate(center+A*zc) if v==0]==[4,15,23]
assert all(v>=0 for v in center+A*zc)
assert restrictions(tuple(F(v) for v in S.Matrix(p)+P*(tstar+zc))) == (F(0),)*5

vertices=set()
for chosen in product(*choice_groups):
    support=FSET+tuple(chosen)+(common,)
    M14=C[:,[D.index(e) for e in support]]
    assert M14.rank()==14
    weights,params=M14.gauss_jordan_solve(q0)
    assert params.rows==0 and all(v>0 for v in weights)
    full=S.Matrix.hstack(*(edgecol(e) for e in support))
    physical=S.Matrix(p)+P*(tstar+zc)
    assert full*weights==S.Matrix(rhs(tuple(F(v) for v in physical)))
    vec=[F(0)]*18
    for e,mass_e in zip(support,weights):vec[face_arcs.index(e)]=F(mass_e)
    vertices.add(tuple(vec))
assert len(vertices)==12
bar=tuple(sum(v[i] for v in vertices)/12 for i in range(18))
assert all(x>0 for x in bar)

bvec=S.Matrix([S.Rational(v) for v in next(iter(vertices))])
K=S.Matrix.hstack(*Fmat.nullspace()); assert K.shape==(18,4)
Kf=[[F(K[i,j]) for j in range(4)] for i in range(18)]
bf=[F(v) for v in bvec]
def four_solve(indices):
    a=[Kf[i][:]+[-bf[i]] for i in indices]
    for k in range(4):
        ix=next((j for j in range(k,4) if a[j][k]),None)
        if ix is None:return None
        a[k],a[ix]=a[ix],a[k]
        pivot=a[k][k]
        for j in range(k,5):a[k][j]/=pivot
        for i in range(k+1,4):
            if a[i][k]:
                ratio=a[i][k]
                for j in range(k,5):a[i][j]-=ratio*a[k][j]
    result=[F(0)]*4
    for k in range(3,-1,-1):result[k]=a[k][4]-sum(a[k][j]*result[j] for j in range(k+1,4))
    return result
nonsingular=0
feasible=set()
for indices in combinations(range(18),4):
    z=four_solve(indices)
    if z is None:continue
    nonsingular+=1
    point=tuple(bf[i]+sum(Kf[i][j]*z[j] for j in range(4)) for i in range(18))
    if all(m>=0 for m in point):feasible.add(point)
assert nonsingular==324 and len(feasible)==12 and feasible==vertices
assert all(sum(m>0 for m in vertex)==14 for vertex in feasible)
def affine_rank(points):
    if len(points)<2:return 0
    return S.Matrix([[S.Rational(v[i]-points[0][i]) for i in range(18)]
                     for v in points[1:]]).rank()
facets={}
for i,e in enumerate(face_arcs):
    on=[v for v in vertices if v[i]==0]
    if on:
        assert affine_rank(on)==3
        facets[e]=len(on)
assert facets=={(2,1):8,(3,1):8,(4,1):8,
               (3,2):6,(4,2):6,(0,3):6,(2,3):6}
assert all(sum(v[face_arcs.index(e)]==0 for e in facets)==4 for v in vertices)
edge_pairs=sum(
    sum(va[face_arcs.index(e)]==vb[face_arcs.index(e)]==0 for e in facets)==3
    for ii,va in enumerate(sorted(vertices)) for vb in sorted(vertices)[ii+1:])
assert edge_pairs==24
print('MODEL',len(D),'arcs; physical five equalities; 21 Blackwell rows; frozen point R=',R)
print('FACE',len(face_arcs),'arcs; rank',Fmat.rank(),'affine dimension',18-Fmat.rank())
print('PHYSICAL_WALL_NORMAL',normal,'span condition exact')
print('CARTESIAN_BRANCH_SUPPORTS',len(vertices),'all 14 strictly positive')
print('EXHAUSTIVE_4_FACET_COMBINATIONS',3060,'rank4 intersections',nonsingular,
      'distinct feasible',len(feasible),'exact arithmetic')
print('FULL_21_EQUATIONS_AND_PHYSICAL_SLACKS_ALL_12',True)
print('FACE_INTERIOR_ALL_18_POSITIVE',all(x>0 for x in bar))
print('SEVEN_FACETS',sorted(facets.items()))
print('ONE_DIMENSIONAL_EDGES',edge_pairs)
print('COMBINATORIAL_TYPE','Delta_2 x Delta_1 x Delta_1','f-vector',(12,24,19,7))
print('PASS_EXACT_FROZEN_R5_FACE_PRODUCT_CERTIFICATE')
