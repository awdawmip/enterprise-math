#!/usr/bin/env python3
"""Exact revision-V2 certificate for RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION.

Pure standard library; exact arithmetic only.
"""
from fractions import Fraction
from itertools import product, combinations
from collections import Counter
from math import gcd
from pathlib import Path
import json

LABELS=("AB","AC","AD","BC","BD","CD")
EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
INDEX={e:i for i,e in enumerate(EDGES)}
N=6

def F(a,b=None): return Fraction(a) if b is None else Fraction(a,b)
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
def mvec(A,x):
    return [sum((A[i][j]*F(x[j]) for j in range(len(x))),F(0)) for i in range(len(A))]
def vdot(x,y): return sum((F(a)*F(b) for a,b in zip(x,y)),F(0))
def bilinear(A,x,y): return vdot(x,mvec(A,y))
def key(A): return tuple(tuple(v for v in row) for row in A)
def rank(A):
    M=[row[:] for row in A]
    if not M: return 0
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
        p,q=pi[u],pi[v]; s=1
        if p>q:
            p,q=q,p
            if signed: s=-1
        M[INDEX[(p,q)]][i]=F(s)
    return M
def apply_int(M,x):
    y=mvec(M,x)
    assert all(v.denominator==1 for v in y)
    return tuple(int(v) for v in y)

# Frozen carrier generators: a=(BCD), b=(AB).
A4={0:0,1:2,2:3,3:1}
B2={0:1,1:0,2:2,3:3}
Ua=edge_matrix(A4,False); Ub=edge_matrix(B2,False)
Wa=edge_matrix(A4,True);  Wb=edge_matrix(B2,True)
I=eye(); J=ones()

# Johnson adjacency/complement and rational projectors.
AJ=zero(); C=zero()
for i,e in enumerate(EDGES):
    for j,f in enumerate(EDGES):
        if i!=j and len(set(e)&set(f))==1: AJ[i][j]=F(1)
    comp=tuple(sorted(set(range(4))-set(e)))
    C[INDEX[comp]][i]=F(1)

P4=mscale(F(1,6),J)
P0=mscale(F(1,2),msub(I,C))
Pm2=msub(mscale(F(1,2),madd(I,C)),P4)
assert AJ==msub(msub(J,I),C)
assert mmul(C,C)==I
assert rank(P4)==1 and rank(P0)==3 and rank(Pm2)==2
assert madd(madd(P4,P0),Pm2)==I
for P in (P4,P0,Pm2):
    assert mmul(P,P)==P
for P,Qp in ((P4,P0),(P4,Pm2),(P0,Pm2)):
    assert mmul(P,Qp)==zero()
GU=generated_group((Ua,Ub))
assert len(GU)==24
for U in (Ua,Ub):
    assert mmul(U,C)==mmul(C,U)
    for P in (P4,P0,Pm2):
        assert mmul(U,P)==mmul(P,U)

# Hodge matrix in orientation A<B<C<D.
H=zero()
H[5][0]=H[0][5]=F(1)
H[4][1]=H[1][4]=F(-1)
H[3][2]=H[2][3]=F(1)
assert mmul(H,H)==I
assert det(H)==F(-1) and rank(H)==6

def q(x):
    return F(x[0])*F(x[5])-F(x[1])*F(x[4])+F(x[2])*F(x[3])
def polar(x,y):
    return (F(x[0])*F(y[5])+F(x[5])*F(y[0])
            -F(x[1])*F(y[4])-F(x[4])*F(y[1])
            +F(x[2])*F(y[3])+F(x[3])*F(y[2]))
def addv(x,y): return tuple(F(a)+F(b) for a,b in zip(x,y))

# Integral polarization b_Q=Q(x+y)-Q(x)-Q(y)=x^T H y.
test_vecs=[
    (0,0,0,0,0,0),(1,0,0,0,0,0),(0,1,-1,2,0,3),
    (2,-1,3,1,-2,4),(-3,2,0,-1,1,5)
]
for x in test_vecs:
    for y in test_vecs:
        assert q(addv(x,y))-q(x)-q(y)==polar(x,y)==bilinear(H,x,y)
    assert polar(x,x)==2*q(x)

# Half-polarization B_Q=b_Q/2 when 2 is invertible.
B=mscale(F(1,2),H)
assert det(B)==F(-1,64) and rank(B)==6
# Explicit orthogonal signature basis: +++---.
s1=(1,0,0,0,0,1)
s2=(0,1,0,0,-1,0)
s3=(0,0,1,1,0,0)
a1=(1,0,0,0,0,-1)
a2=(0,1,0,0,1,0)
a3=(0,0,1,-1,0,0)
sig_basis=(s1,s2,s3,a1,a2,a3)
G=[[bilinear(B,x,y) for y in sig_basis] for x in sig_basis]
assert G==[
    [F(1),0,0,0,0,0],
    [0,F(1),0,0,0,0],
    [0,0,F(1),0,0,0],
    [0,0,0,F(-1),0,0],
    [0,0,0,0,F(-1),0],
    [0,0,0,0,0,F(-1)],
]
# Integral Hodge eigensublattices have total index 8, so no Z-direct split.
SB=[list(row) for row in zip(*sig_basis)]
assert abs(det([[F(v) for v in row] for row in SB]))==8

# Hodge sectors and orientation reversal.
for v in (s1,s2,s3): assert mvec(H,v)==[F(z) for z in v]
for v in (a1,a2,a3): assert mvec(H,v)==[F(-z) for z in v]
Hrev=mscale(-1,H)
for v in (s1,s2,s3): assert mvec(Hrev,v)==[F(-z) for z in v]
for v in (a1,a2,a3): assert mvec(Hrev,v)==[F(z) for z in v]

# Exterior/Pfaffian and Hodge orientation law.
assert mmul(H,Wa)==mmul(Wa,H)                  # even a preserves sectors
assert mmul(H,Wb)==mscale(-1,mmul(Wb,H))       # odd b swaps sectors
assert mmul(mmul(mtranspose(Wa),H),Wa)==H
assert mmul(mmul(mtranspose(Wb),H),Wb)==mscale(-1,H)
for x in test_vecs:
    assert q(apply_int(Wa,x))==q(x)
    assert q(apply_int(Wb,x))==-q(x)

# Complement is not Hodge star in characteristic zero, though it preserves Q and commutes with H.
assert C!=H
assert mmul(C,H)==mmul(H,C)
assert mmul(mmul(mtranspose(C),H),C)==H
for x in test_vecs: assert q(apply_int(C,x))==q(x)

# Characteristic-2 boundary: b remains perfect alternating, q is only a quadratic refinement.
def mod2_matrix(A): return [[int(v)%2 for v in row] for row in A]
def mmul2(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%2
             for j in range(len(B[0]))] for i in range(len(A))]
def rank2(A):
    M=[row[:] for row in A]; r=0
    rows=len(M); cols=len(M[0])
    for c in range(cols):
        p=next((i for i in range(r,rows) if M[i][c]%2),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        for i in range(rows):
            if i!=r and M[i][c]%2:
                M[i]=[(M[i][j]^M[r][j]) for j in range(cols)]
        r+=1
    return r
H2=mod2_matrix(H); C2=mod2_matrix(C); I2=mod2_matrix(I)
assert H2==C2 and rank2(H2)==6
N2=[[H2[i][j]^I2[i][j] for j in range(N)] for i in range(N)]
assert mmul2(N2,N2)==[[0]*N for _ in range(N)]
assert rank2(N2)==3
def q2(x): return (x[0]*x[5]+x[1]*x[4]+x[2]*x[3])%2
def q2prime(x): return (q2(x)+x[0]*x[0])%2
def pol2(qf,x,y):
    z=[(a+b)%2 for a,b in zip(x,y)]
    return (qf(z)+qf(x)+qf(y))%2
f2vecs=list(product((0,1), repeat=6))
for x in f2vecs:
    assert pol2(q2,x,x)==0
for x in f2vecs:
    for y in ((1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,0,0,0,1)):
        b=sum(x[i]*H2[i][j]*y[j] for i in range(6) for j in range(6))%2
        assert pol2(q2,x,y)==b
        assert pol2(q2prime,x,y)==b
assert q2((1,0,0,0,0,0))!=q2prime((1,0,0,0,0,0))
# Signed and unsigned exterior actions collapse mod 2.
assert mod2_matrix(Wa)==mod2_matrix(Ua)
assert mod2_matrix(Wb)==mod2_matrix(Ub)

# Q_orb exact invariant for unsigned carrier.
def tvals(x): return (x[0]*x[5],x[1]*x[4],x[2]*x[3])
def qorbit(x):
    t1,t2,t3=tvals(x); S=t1+t2+t3
    return tuple(sorted((S-2*t1,S-2*t2,S-2*t3)))
for x in product((-1,0,1), repeat=6):
    vals={int(q(apply_int(g,x))) for g in GU}
    assert vals==set(qorbit(x))
    for g in GU:
        assert qorbit(apply_int(g,x))==qorbit(x)

# Integral Johnson splitting / index 24 / Smith factors.
one=[1,1,1,1,1,1]
d1=[1,0,0,0,0,-1]
d2=[0,1,0,0,-1,0]
d3=[0,0,1,-1,0,0]
l2a=[1,-1,0,0,-1,1]
l2b=[1,0,-1,-1,0,1]
Bint=[list(row) for row in zip(one,d1,d2,d3,l2a,l2b)]
assert abs(det([[F(v) for v in row] for row in Bint]))==24
def idet(M): return int(det([[F(v) for v in row] for row in M]))
def minor_gcd(M,k):
    vals=[]
    for rs in combinations(range(6),k):
        for cs in combinations(range(6),k):
            sub=[[M[i][j] for j in cs] for i in rs]
            vals.append(abs(idet(sub)))
    g=0
    for v in vals: g=gcd(g,v)
    return g
deltas=[1]+[minor_gcd(Bint,k) for k in range(1,7)]
snf=[deltas[k]//deltas[k-1] for k in range(1,7)]
assert deltas[-1]==24 and snf==[1,1,1,2,2,6]
def rho(x):
    return ((x[0]-x[5])%2,(x[1]-x[4])%2,(x[2]-x[3])%2,sum(x)%3)
for col in (one,d1,d2,d3,l2a,l2b):
    assert rho(col)==(0,0,0,0)
surj=[
    (1,2,0,0,0,0), # e1 in (Z/2)^3
    (2,1,0,0,0,0),
    (2,0,1,0,0,0),
    (0,0,0,0,2,2), # mod-3 generator
]
assert [rho(x) for x in surj]==[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
# Exact generator action on rho.
for x in product((0,1,2), repeat=6):
    r1,r2,r3,s=rho(x)
    assert rho(apply_int(Ua,x))==(r3,r1,r2,s)
    assert rho(apply_int(Ub,x))==(r1,r3,r2,s)
    assert rho(apply_int(C,x))==(r1,r2,r3,s)

# Frozen finite censuses retained as regression.
def census(vals):
    cq=Counter(); patterns=set(); rz=0; qvar=0
    for x in product(vals, repeat=6):
        qx=int(q(x)); cq[qx]+=1; patterns.add(qorbit(x))
        if rho(x)==(0,0,0,0): rz+=1
        if len({int(q(apply_int(g,x))) for g in GU})>1: qvar+=1
    return len(vals)**6, dict(sorted(cq.items())), len(patterns), rz, qvar
assert census((0,1))==(64,{-1:9,0:33,1:19,2:3},4,2,36)
assert census((-1,0,1))==(729,{-3:8,-2:60,-1:174,0:245,1:174,2:60,3:8},10,47,588)
n5,cq5,pat5,rz5,qvar5=census((-2,-1,0,1,2))
assert n5==15625 and pat5==84 and rz5==733 and qvar5==14736

# Materialized Gen-current regression table must match the exact laws above.
artifact_path=(Path(__file__).resolve().parents[1]/
    "research_artifacts/P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_REVISION_V2/regression_table_20260830.json")
artifact=json.loads(artifact_path.read_text(encoding="utf-8"))
assert artifact["schema"]=="P000_JOHNSON_PLUCKER_REVISION_V2_REGRESSION_V1"
rows={row["operator"]:row for row in artifact["rows"]}
assert rows["a_xi"]["vertex_permutation"]=="(B C D)"
assert rows["a_xi"]["parity"]==1
assert rows["a_xi"]["unsigned_edge_image_0based"]==[1,2,0,5,3,4]
assert rows["a_xi"]["johnson_projectors"]=="COMMUTES_P4_P0_PM2"
assert rows["a_xi"]["complement"]=="COMMUTES_C"
assert rows["a_xi"]["pfaffian_law"]=="Q(W_a x)=+Q(x)"
assert rows["a_xi"]["hodge_law"]=="H W_a=+W_a H; preserves H+ and H-"
assert rows["a_xi"]["rho_law"]=="(r1,r2,r3;s)->(r3,r1,r2;s)"
assert rows["a_xi"]["q_orb"]=="INVARIANT"
assert rows["b_xi"]["vertex_permutation"]=="(A B)"
assert rows["b_xi"]["parity"]==-1
assert rows["b_xi"]["unsigned_edge_image_0based"]==[0,3,4,1,2,5]
assert rows["b_xi"]["johnson_projectors"]=="COMMUTES_P4_P0_PM2"
assert rows["b_xi"]["complement"]=="COMMUTES_C"
assert rows["b_xi"]["pfaffian_law"]=="Q(W_b x)=-Q(x)"
assert rows["b_xi"]["hodge_law"]=="H W_b=-W_b H; swaps H+ and H-"
assert rows["b_xi"]["rho_law"]=="(r1,r2,r3;s)->(r1,r3,r2;s)"
assert rows["b_xi"]["q_orb"]=="INVARIANT"
assert rows["C"]["pfaffian_law"]=="Q(Cx)=Q(x)"
assert rows["C"]["hodge_law"]=="CH=HC; C!=H in characteristic 0"
assert rows["C"]["rho_law"]=="IDENTITY"
assert artifact["coefficient_ring_boundary"]["integral_polar_form_det"]==-1
assert artifact["coefficient_ring_boundary"]["half_polar_det"]=="-1/64"
assert artifact["coefficient_ring_boundary"]["hodge_eigenlattice_index_over_Z"]==8
assert artifact["coefficient_ring_boundary"]["characteristic_2"]==(
    "polar form perfect alternating; H=C mod 2; +/- sectors coalesce; q not determined by polar form"
)

print("P000_JOHNSON_PLUCKER_REVISION_V2_CHECK=PASS "
      "polar_rank=6 signature=3,3 char2_polar_rank=6 char2_nilpotent_rank=3 "
      "hodge_plus=3 hodge_minus=3 eigensublattice_index_Z=8 "
      "johnson=1+3+2 split_index=24 snf=1,1,1,2,2,6 "
      "qorb_patterns_box5=84 rho_zero_box5=733 qvar_box5=14736")
