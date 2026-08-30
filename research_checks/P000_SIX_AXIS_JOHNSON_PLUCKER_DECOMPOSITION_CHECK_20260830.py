#!/usr/bin/env python3
"""Exact certificate for RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION.

No floating point, no factorization oracle, no external packages.
"""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import gcd

LABELS = ("AB","AC","AD","BC","BD","CD")
EDGES = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
INDEX = {e:i for i,e in enumerate(EDGES)}
N = 6

def F(x, y=None): return Fraction(x) if y is None else Fraction(x,y)
def zero(n=N,m=N): return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n=N):
    M=zero(n,n)
    for i in range(n): M[i][i]=F(1)
    return M
def ones(n=N,m=N): return [[F(1) for _ in range(m)] for _ in range(n)]
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mscale(c,A): return [[F(c)*v for v in row] for row in A]
def mmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def mtranspose(A): return [list(row) for row in zip(*A)]
def mpow(A,n):
    R=eye(len(A))
    while n:
        if n&1: R=mmul(R,A)
        A=mmul(A,A); n//=2
    return R
def meq(A,B): return A==B
def mvec(A,x):
    return [sum((A[i][j]*F(x[j]) for j in range(len(x))),F(0)) for i in range(len(A))]
def key(A): return tuple(tuple(v for v in row) for row in A)
def trace(A): return sum((A[i][i] for i in range(len(A))),F(0))
def rank(A):
    M=[row[:] for row in A]
    r=0
    rows=len(M); cols=len(M[0])
    for c in range(cols):
        p=next((i for i in range(r,rows) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        piv=M[r][c]
        M[r]=[v/piv for v in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]:
                a=M[i][c]
                M[i]=[M[i][j]-a*M[r][j] for j in range(cols)]
        r+=1
        if r==rows: break
    return r
def det(A):
    M=[row[:] for row in A]
    n=len(M); d=F(1); sign=1
    for c in range(n):
        p=next((i for i in range(c,n) if M[i][c]),None)
        if p is None: return F(0)
        if p!=c:
            M[c],M[p]=M[p],M[c]; sign*=-1
        piv=M[c][c]; d*=piv
        for i in range(c+1,n):
            if M[i][c]:
                a=M[i][c]/piv
                for j in range(c,n):
                    M[i][j]-=a*M[c][j]
    return F(sign)*d
def generated_group(gens):
    I=eye(len(gens[0]))
    seen={key(I):I}; stack=[I]
    while stack:
        g=stack.pop()
        for h in gens:
            z=mmul(g,h); k=key(z)
            if k not in seen:
                seen[k]=z; stack.append(z)
    return list(seen.values())

def edge_matrix(pi,signed=False):
    M=zero()
    for i,(u,v) in enumerate(EDGES):
        p,q=pi[u],pi[v]
        s=1
        if p>q:
            p,q=q,p
            if signed: s=-1
        M[INDEX[(p,q)]][i]=F(s)
    return M

# carrier a=(BCD), b=(AB)
A4={0:0,1:2,2:3,3:1}
B2={0:1,1:0,2:2,3:3}
Ua=edge_matrix(A4,False)
Ub=edge_matrix(B2,False)
Wa=edge_matrix(A4,True)
Wb=edge_matrix(B2,True)
I=eye(); J=ones()

# Johnson J(4,2) adjacency and complement
AJ=zero(); C=zero()
for i,e in enumerate(EDGES):
    for j,f in enumerate(EDGES):
        if i!=j and len(set(e)&set(f))==1: AJ[i][j]=F(1)
    comp=tuple(sorted(set(range(4))-set(e)))
    C[INDEX[comp]][i]=F(1)

assert meq(AJ, msub(msub(J,I),C))
assert meq(mmul(C,C),I)
assert rank(msub(AJ,mscale(4,I)))==5       # dim eigenspace 4 = 1
assert rank(AJ)==3                         # dim kernel = 3
assert rank(madd(AJ,mscale(2,I)))==4       # dim eigenspace -2 = 2
assert meq(mmul(mmul(AJ,madd(AJ,mscale(2,I))),msub(AJ,mscale(4,I))),zero())

P4=mscale(F(1,6),J)
P0=mscale(F(1,2),msub(I,C))
Pm2=msub(mscale(F(1,2),madd(I,C)),P4)
for P in (P4,P0,Pm2):
    assert meq(mmul(P,P),P)
for P,Qp in ((P4,P0),(P4,Pm2),(P0,Pm2)):
    assert meq(mmul(P,Qp),zero())
assert meq(madd(madd(P4,P0),Pm2),I)
assert rank(P4)==1 and rank(P0)==3 and rank(Pm2)==2
assert meq(mmul(AJ,P4),mscale(4,P4))
assert meq(mmul(AJ,P0),zero())
assert meq(mmul(AJ,Pm2),mscale(-2,Pm2))

# Frozen unsigned carrier S4 and exceptional complement.
assert meq(mpow(Ua,3),I)
assert meq(mpow(Ub,2),I)
assert meq(mpow(mmul(Ua,Ub),4),I)
GU=generated_group((Ua,Ub))
assert len(GU)==24
assert key(C) not in {key(g) for g in GU}
assert len(generated_group((Ua,Ub,C)))==48
for g in (Ua,Ub):
    assert meq(mmul(g,C),mmul(C,g))
    for P in (P4,P0,Pm2):
        assert meq(mmul(g,P),mmul(P,g))

# K4 cocircuits (stars) and circuits (triangles).
stars={
    "A":frozenset((0,1,2)),
    "B":frozenset((0,3,4)),
    "C":frozenset((1,3,5)),
    "D":frozenset((2,4,5)),
}
circuits={
    "ABC":frozenset((0,1,3)),
    "ABD":frozenset((0,2,4)),
    "ACD":frozenset((1,2,5)),
    "BCD":frozenset((3,4,5)),
}
def support_image(M,S):
    out=set()
    for j in S:
        nz=[i for i in range(N) if M[i][j]]
        assert len(nz)==1
        out.add(nz[0])
    return frozenset(out)
assert support_image(Ua,stars["A"])==stars["A"]
assert support_image(Ua,stars["B"])==stars["C"]
assert support_image(Ua,stars["C"])==stars["D"]
assert support_image(Ua,stars["D"])==stars["B"]
assert support_image(Ub,stars["A"])==stars["B"]
assert support_image(Ub,stars["B"])==stars["A"]
assert support_image(Ub,stars["C"])==stars["C"]
assert support_image(Ub,stars["D"])==stars["D"]
# Complement swaps each vertex-star with the opposite triangle.
assert support_image(C,stars["A"])==circuits["BCD"]
assert support_image(C,stars["B"])==circuits["ACD"]
assert support_image(C,stars["C"])==circuits["ABD"]
assert support_image(C,stars["D"])==circuits["ABC"]

# Oriented K4 incidence rank=3; four triangle vectors lie in the cycle kernel.
Inc=[
    [-1,-1,-1, 0, 0, 0],
    [ 1, 0, 0,-1,-1, 0],
    [ 0, 1, 0, 1, 0,-1],
    [ 0, 0, 1, 0, 1, 1],
]
Inc=[[F(v) for v in row] for row in Inc]
assert rank(Inc)==3
cycle_vecs=(
    [1,-1,0,1,0,0],
    [1,0,-1,0,1,0],
    [0,1,-1,0,0,1],
    [0,0,0,1,-1,1],
)
for v in cycle_vecs:
    assert mvec(Inc,v)==[F(0)]*4

# Natural exterior action W != unsigned edge permutation U.
assert meq(mpow(Wa,3),I)
assert meq(mpow(Wb,2),I)
assert meq(mpow(mmul(Wa,Wb),4),I)
assert len(generated_group((Wa,Wb)))==24
assert not meq(Wb,Ub) and not meq(Wa,Ua)
# Character separation: transposition and double-transposition already prove non-isomorphism.
DT={0:1,1:0,2:3,3:2}
Udt=edge_matrix(DT,False); Wdt=edge_matrix(DT,True)
assert (trace(Ub),trace(Udt))==(F(2),F(2))
assert (trace(Wb),trace(Wdt))==(F(0),F(-2))

# Hodge star for A<B<C<D: *12=34, *13=-24, *14=23.
H=zero()
H[5][0]=H[0][5]=F(1)
H[4][1]=H[1][4]=F(-1)
H[3][2]=H[2][3]=F(1)
assert meq(mmul(H,H),I)
assert det(H)==F(-1)
assert rank(H)==6
assert meq(mmul(H,Wa),mmul(Wa,H))            # a even
assert meq(mmul(H,Wb),mscale(-1,mmul(Wb,H))) # b odd
# Natural exterior Pfaffian transforms by the vertex permutation sign.
assert meq(mmul(mmul(mtranspose(Wa),H),Wa),H)
assert meq(mmul(mmul(mtranspose(Wb),H),Wb),mscale(-1,H))

# Unsigned complement only shares the three edge-pairs with Hodge star.
assert not meq(C,H)
assert meq(mmul(C,H),mmul(H,C))
assert meq(mmul(mmul(mtranspose(C),H),C),H)

def q(x):
    return x[0]*x[5]-x[1]*x[4]+x[2]*x[3]
def t(x):
    return (x[0]*x[5],x[1]*x[4],x[2]*x[3])
def apply_int(M,x):
    y=mvec(M,x)
    assert all(v.denominator==1 for v in y)
    return tuple(int(v) for v in y)

# Q is not a frozen unsigned-carrier invariant; its carrier orbit is S-2*t_i.
probe=(1,0,0,0,0,1)
assert q(probe)==1 and q(apply_int(Ua,probe))==-1
def qorbit(x):
    t1,t2,t3=t(x); S=t1+t2+t3
    return tuple(sorted((S-2*t1,S-2*t2,S-2*t3)))
assert set(q(apply_int(g,probe)) for g in GU)==set(qorbit(probe))

# Even sign-insensitive valuation/gcd data of Q can change in one unsigned carrier orbit.
probe3=(2,1,0,0,1,1) # t=(2,1,0): Q orbit {-1,1,3}
vals3={q(apply_int(g,probe3)) for g in GU}
assert vals3=={-1,1,3}
assert {gcd(abs(v),3) for v in vals3}=={1,3}
probe2=(3,1,0,0,1,1) # t=(3,1,0): Q orbit {-2,2,4}
vals2={q(apply_int(g,probe2)) for g in GU}
assert vals2=={-2,2,4}
def vp(n,p):
    n=abs(n)
    if n==0: return None
    r=0
    while n%p==0: r+=1; n//=p
    return r
assert {vp(v,2) for v in vals2}=={1,2}

# Symmetric invariant quadratic forms for the unsigned action have exactly
# three coefficient orbits: diagonal, adjacent edge-pairs, complement pairs.
pairs=[(i,j) for i in range(N) for j in range(i,N)]
def pair_image(g,p):
    i,j=p
    ii=next(r for r in range(N) if g[r][i])
    jj=next(r for r in range(N) if g[r][j])
    return tuple(sorted((ii,jj)))
unseen=set(pairs); orbits=[]
while unseen:
    p=next(iter(unseen))
    O={pair_image(g,p) for g in GU}
    orbits.append(O); unseen-=O
assert sorted(map(len,orbits))==[3,6,12]
# H has nonconstant coefficients on the 3 complement pairs, so it is not in the commutant.
assert not meq(mmul(Ua,H),mmul(H,Ua))
assert not meq(mmul(Ub,H),mmul(H,Ub))

# Integral 1+3+2 splitting lattice and exact index-24 obstruction.
one=[1,1,1,1,1,1]
d1=[1,0,0,0,0,-1]
d2=[0,1,0,0,-1,0]
d3=[0,0,1,-1,0,0]
l2a=[1,-1,0,0,-1,1]
l2b=[1,0,-1,-1,0,1]
B=list(map(list,zip(one,d1,d2,d3,l2a,l2b)))
B=[[F(v) for v in row] for row in B]
assert abs(det(B))==24
def residue(x):
    return ((x[0]-x[5])%2,(x[1]-x[4])%2,(x[2]-x[3])%2,sum(x)%3)
for col in (one,d1,d2,d3,l2a,l2b):
    assert residue(col)==(0,0,0,0)
# Explicit surjectivity witnesses for (Z/2)^3 x Z/3.
assert residue((1,2,0,0,0,0))==(1,0,0,0)
assert residue((2,1,0,0,0,0))==(0,1,0,0)
assert residue((2,0,1,0,0,0))==(0,0,1,0)
assert residue((-2,0,0,0,0,0))==(0,0,0,1)
# Therefore kernel(residue) has index 24 and equals the direct-sum lattice.
def split_integral(x):
    return residue(x)==(0,0,0,0)
# Direct projector criterion regression over a finite test box.
for x in product(range(-2,3), repeat=6):
    ps=[mvec(P,x) for P in (P4,P0,Pm2)]
    integral=all(v.denominator==1 for p in ps for v in p)
    assert integral==split_integral(x)

# Factor-blind finite censuses: Cartesian boxes, no factoring used in generation.
def census(vals):
    qdist=Counter(); qorb=Counter(); split=0; qvary=0
    for x in product(vals, repeat=6):
        qdist[q(x)]+=1
        qo=qorbit(x); qorb[qo]+=1
        split += int(split_integral(x))
        qvary += int(len(set(qo))>1)
    return len(vals)**6,qdist,len(qorb),split,qvary
c01=census((0,1))
assert c01[0]==64 and c01[1]==Counter({0:33,1:19,-1:9,2:3})
assert c01[2:]==(4,2,36)
c1=census((-1,0,1))
assert c1[0]==729
assert c1[1]==Counter({0:245,-1:174,1:174,-2:60,2:60,-3:8,3:8})
assert c1[2:]==(10,47,588)
c2=census((-2,-1,0,1,2))
assert c2[0]==15625
assert c2[1]==Counter({-12: 8, -10: 48, -9: 24, -8: 204, -7: 120, -6: 568, -5: 408, -4: 1230, -3: 848, -2: 1920, -1: 1278, 0: 2313, 1: 1278, 2: 1920, 3: 848, 4: 1230, 5: 408, 6: 568, 7: 120, 8: 204, 9: 24, 10: 48, 12: 8})
assert c2[2:]==(84,733,14736)

print("PASS")
print("Johnson spectrum multiplicities: 4^1, 0^3, (-2)^2")
print("Unsigned carrier group order: 24; with complement: 48")
print("Natural exterior carrier group order: 24; character differs from unsigned edge module")
print("Pfaffian Q: signed-relative under natural exterior S4; not invariant under frozen unsigned carrier S4")
print("Integral spectral-splitting quotient: (Z/2)^3 x Z/3, index 24")
print("Census totals: 64, 729, 15625")
