#!/usr/bin/env python3
"""Exact certificate for P000 Johnson-Plucker revision V2.

Pure standard library.  No floating point is used in theorem-critical checks.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

F = Fraction
LABELS = ("AB", "AC", "AD", "BC", "BD", "CD")
EDGES = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
INDEX = {e:i for i,e in enumerate(EDGES)}
N = 6

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
def mt(A): return [list(row) for row in zip(*A)]
def mvec(A,x): return [sum((A[i][j]*F(x[j]) for j in range(len(x))),F(0)) for i in range(len(A))]
def key(A): return tuple(tuple(v for v in row) for row in A)
def det(A):
    M=[row[:] for row in A]; n=len(M); d=F(1); s=1
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]),None)
        if p is None: return F(0)
        if p!=c: M[c],M[p]=M[p],M[c]; s=-s
        piv=M[c][c]; d*=piv
        for r in range(c+1,n):
            if M[r][c]:
                a=M[r][c]/piv
                for j in range(c,n): M[r][j]-=a*M[c][j]
    return F(s)*d
def rank(A):
    M=[row[:] for row in A]; rows=len(M); cols=len(M[0]); r=0
    for c in range(cols):
        p=next((i for i in range(r,rows) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        piv=M[r][c]; M[r]=[v/piv for v in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]:
                a=M[i][c]; M[i]=[M[i][j]-a*M[r][j] for j in range(cols)]
        r+=1
        if r==rows: break
    return r
def mpow(A,n):
    R=eye(len(A))
    while n:
        if n&1: R=mmul(R,A)
        A=mmul(A,A); n//=2
    return R
def generated_group(gens):
    I=eye(len(gens[0])); seen={key(I):I}; stack=[I]
    while stack:
        g=stack.pop()
        for h in gens:
            z=mmul(g,h); k=key(z)
            if k not in seen: seen[k]=z; stack.append(z)
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
    y=mvec(M,x); assert all(v.denominator==1 for v in y)
    return tuple(int(v) for v in y)
def mod2(A): return [[int(v)%2 for v in row] for row in A]
def rank_mod2(A):
    M=[row[:] for row in A]; rows=len(M); cols=len(M[0]); r=0
    for c in range(cols):
        p=next((i for i in range(r,rows) if M[i][c]&1),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        for i in range(rows):
            if i!=r and (M[i][c]&1): M[i]=[(a^b)&1 for a,b in zip(M[i],M[r])]
        r+=1
    return r
def mmul_mod2(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%2 for j in range(len(B[0]))] for i in range(len(A))]
def q(x): return x[0]*x[5]-x[1]*x[4]+x[2]*x[3]
def bq(x,y): return q(tuple(x[i]+y[i] for i in range(6)))-q(x)-q(y)
def t(x): return (x[0]*x[5],x[1]*x[4],x[2]*x[3])
def qorbit(x):
    a,b,c=t(x); S=a+b+c
    return tuple(sorted((S-2*a,S-2*b,S-2*c)))
def rho(x): return ((x[0]-x[5])%2,(x[1]-x[4])%2,(x[2]-x[3])%2,sum(x)%3)

I=eye(); J=ones()
# Johnson complement and adjacency.
C=zero(); AJ=zero()
for i,e in enumerate(EDGES):
    comp=tuple(sorted(set(range(4))-set(e))); C[INDEX[comp]][i]=F(1)
    for j,f in enumerate(EDGES):
        if i!=j and len(set(e)&set(f))==1: AJ[i][j]=F(1)
assert AJ==msub(msub(J,I),C)
P4=mscale(F(1,6),J)
P0=mscale(F(1,2),msub(I,C))
Pm2=msub(mscale(F(1,2),madd(I,C)),P4)
assert [rank(P4),rank(P0),rank(Pm2)]==[1,3,2]
for P in (P4,P0,Pm2): assert mmul(P,P)==P
for P,Qp in ((P4,P0),(P4,Pm2),(P0,Pm2)): assert mmul(P,Qp)==zero()
assert madd(madd(P4,P0),Pm2)==I

# a=(BCD) and b=(AB) on carrier labels.
A4={0:0,1:2,2:3,3:1}; B2={0:1,1:0,2:2,3:3}
Ua=edge_matrix(A4,False); Ub=edge_matrix(B2,False)
Wa=edge_matrix(A4,True); Wb=edge_matrix(B2,True)
GU=generated_group((Ua,Ub)); assert len(GU)==24
assert mpow(Ua,3)==I and mpow(Ub,2)==I and mpow(mmul(Ua,Ub),4)==I
for U in (Ua,Ub):
    assert mmul(U,C)==mmul(C,U)
    for P in (P4,P0,Pm2): assert mmul(U,P)==mmul(P,U)

# Hodge matrix and integral polarization.
H=zero()
H[5][0]=H[0][5]=F(1)
H[4][1]=H[1][4]=F(-1)
H[3][2]=H[2][3]=F(1)
assert mmul(H,H)==I and det(H)==F(-1) and rank(H)==6
for x in product(range(-2,3), repeat=6):
    # Sparse exact sanity: diagonal integral polarization convention.
    assert bq(x,x)==2*q(x)
    if x[0] in (-2,0,2) and x[1:]==(0,0,0,0,0):
        assert bq(x,(0,0,0,0,0,1))==x[0]

# Full symbolic basis check b_Q(x,y)=x^T H y on basis pairs.
E=[]
for i in range(6):
    e=[0]*6; e[i]=1; E.append(tuple(e))
for i in range(6):
    for j in range(6): assert bq(E[i],E[j])==H[i][j]

# Half-polarization signature basis: Gram diag(+,+,+,-,-,-).
s1=(1,0,0,0,0,1); s2=(0,1,0,0,-1,0); s3=(0,0,1,1,0,0)
a1=(1,0,0,0,0,-1); a2=(0,1,0,0,1,0); a3=(0,0,1,-1,0,0)
S=[s1,s2,s3,a1,a2,a3]
def B(x,y): return F(bq(x,y),2)
Gram=[[B(x,y) for y in S] for x in S]
assert Gram==[[F(1 if i==j and i<3 else -1 if i==j else 0) for j in range(6)] for i in range(6)]
assert rank(Gram)==6 and det(Gram)==-1
# The six eigenvectors form an index-8 sublattice of Z^6.
SB=[list(row) for row in zip(*S)]
assert abs(det([[F(v) for v in row] for row in SB]))==8
assert all(mvec(H,s)==list(map(F,s)) for s in (s1,s2,s3))
assert all(mvec(H,a)==[-F(v) for v in a] for a in (a1,a2,a3))

# Orientation/Pfaffian laws.
assert mmul(H,Wa)==mmul(Wa,H)
assert mmul(H,Wb)==mscale(-1,mmul(Wb,H))
assert mmul(mmul(mt(Wa),H),Wa)==H
assert mmul(mmul(mt(Wb),H),Wb)==mscale(-1,H)
for x in product((-1,0,1), repeat=6):
    assert q(apply_int(Wa,x))==q(x)
    assert q(apply_int(Wb,x))==-q(x)
# Orientation reversal is exactly H -> -H and swaps the declared bases.
Hrev=mscale(-1,H)
assert all(mvec(Hrev,s)==[-F(v) for v in s] for s in (s1,s2,s3))
assert all(mvec(Hrev,a)==list(map(F,a)) for a in (a1,a2,a3))

# Complement is distinct in characteristic zero but commutes with H.
assert C!=H and mmul(C,H)==mmul(H,C)
for x in product((-1,0,1), repeat=6): assert q(apply_int(C,x))==q(x)

# Characteristic-2 boundary: H=C, perfect alternating polar, N^2=0 rank 3.
H2=mod2(H); C2=mod2(C); I2=mod2(I)
assert H2==C2
assert rank_mod2(H2)==6
N2=[[(H2[i][j]-I2[i][j])%2 for j in range(6)] for i in range(6)]
assert rank_mod2(N2)==3
assert mmul_mod2(N2,N2)==[[0]*6 for _ in range(6)]
# Signed and unsigned edge matrices coalesce mod 2.
assert mod2(Wa)==mod2(Ua) and mod2(Wb)==mod2(Ub)
# Polarization is alternating and Q is not determined by it: Q+x1^2 has same polar.
def q2(x): return (x[0]*x[5]+x[1]*x[4]+x[2]*x[3])%2
def q2prime(x): return (q2(x)+x[0]*x[0])%2
def pol2(fun,x,y): return (fun(tuple((x[i]+y[i])%2 for i in range(6)))+fun(x)+fun(y))%2
for x in product((0,1),repeat=6):
    assert pol2(q2,x,x)==0
    for y in E:
        yy=tuple(v%2 for v in y)
        assert pol2(q2,x,yy)==pol2(q2prime,x,yy)
assert q2((1,0,0,0,0,0))!=q2prime((1,0,0,0,0,0))

# Exact rho covariance under the current generators.
def rho_a(r): return (r[2],r[0],r[1],r[3])
def rho_b(r): return (r[0],r[2],r[1],r[3])
for x in product(range(-2,3), repeat=6):
    r=rho(x)
    assert rho(apply_int(Ua,x))==rho_a(r)
    assert rho(apply_int(Ub,x))==rho_b(r)
    assert rho(apply_int(C,x))==r

# Preserve the index-24 Johnson integral splitting.
one=(1,1,1,1,1,1); d1=(1,0,0,0,0,-1); d2=(0,1,0,0,-1,0); d3=(0,0,1,-1,0,0)
l2a=(1,-1,0,0,-1,1); l2b=(1,0,-1,-1,0,1)
LB=[list(row) for row in zip(one,d1,d2,d3,l2a,l2b)]
assert abs(det([[F(v) for v in row] for row in LB]))==24
for v in (one,d1,d2,d3,l2a,l2b): assert rho(v)==(0,0,0,0)

# Smith normal form invariant factors by determinantal divisors; small 6x6 integer matrix.
from itertools import combinations
def bareiss_det(M):
    M=[list(map(int,row)) for row in M]; n=len(M)
    if n==0: return 1
    if n==1: return M[0][0]
    sign=1; prev=1
    for k in range(n-1):
        p=next((r for r in range(k,n) if M[r][k]!=0),None)
        if p is None: return 0
        if p!=k: M[k],M[p]=M[p],M[k]; sign=-sign
        piv=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n): M[i][j]=(M[i][j]*piv-M[i][k]*M[k][j])//prev
        prev=piv
    return sign*M[-1][-1]
def gcd(a,b):
    while b: a,b=b,a%b
    return abs(a)
def determinantal_divisor(M,k):
    g=0
    for rs in combinations(range(6),k):
        for cs in combinations(range(6),k):
            d=bareiss_det([[M[i][j] for j in cs] for i in rs]); g=gcd(g,d)
            if g==1: return 1
    return g
D=[1]
for k in range(1,7): D.append(determinantal_divisor(LB,k))
snf=[D[k]//D[k-1] for k in range(1,7)]
assert snf==[1,1,1,2,2,6]

# Q_orb invariance and frozen finite census values.
for x in product((-1,0,1),repeat=6):
    qo=qorbit(x)
    for g in GU: assert qorbit(apply_int(g,x))==qo

def census(vals):
    total=0; qc=Counter(); qop=set(); rz=0; qvar=0
    for x in product(vals,repeat=6):
        total+=1; qc[q(x)]+=1; qop.add(qorbit(x)); rz += rho(x)==(0,0,0,0)
        if len({q(apply_int(g,x)) for g in GU})>1: qvar+=1
    return total,qc,len(qop),rz,qvar
c01=census((0,1))
assert c01==(64,Counter({0:33,1:19,-1:9,2:3}),4,2,36)
c3=census((-1,0,1))
assert c3==(729,Counter({0:245,-1:174,1:174,-2:60,2:60,-3:8,3:8}),10,47,588)
c5=census((-2,-1,0,1,2))
assert c5[0]==15625 and c5[2:]==(84,733,14736)

print("P000_JOHNSON_PLUCKER_REVISION_V2_CHECK=PASS "
      "polar_rank=6 signature=3,3 char2_polar_rank=6 char2_nilpotent_rank=3 "
      "hodge_plus=3 hodge_minus=3 eigensublattice_index_Z=8 "
      "johnson=1+3+2 split_index=24 snf=1,1,1,2,2,6 "
      f"qorb_patterns_box5={c5[2]} rho_zero_box5={c5[3]} qvar_box5={c5[4]}")
