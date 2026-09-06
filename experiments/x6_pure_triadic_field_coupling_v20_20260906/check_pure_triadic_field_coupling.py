#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product

V=tuple(range(6))
TRIPLES=tuple(combinations(V,3))
TI={S:i for i,S in enumerate(TRIPLES)}
PAIRS=tuple(combinations(V,2))

# Saturated V18 integer basis of K=ker(pair shadow); pivot rows are identity.
B=[
[0,0,0,0,-1], [0,0,0,-1,0], [0,0,-1,0,0], [0,0,1,1,1],
[0,-1,0,0,0], [-1,0,0,0,0], [1,1,0,0,1], [1,1,1,1,1],
[-1,0,-1,0,-1], [0,-1,0,-1,-1], [0,1,0,1,1], [1,0,1,0,1],
[-1,-1,-1,-1,-1], [-1,-1,0,0,-1], [1,0,0,0,0], [0,1,0,0,0],
[0,0,-1,-1,-1], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]
]
PIV=(14,15,17,18,19)


def rank_q(M):
    A=[[Fraction(x) for x in row] for row in M]
    if not A:return 0
    m=len(A);n=len(A[0]);r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c];A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[x-f*y for x,y in zip(A[i],A[r])]
        r+=1
    return r


def matmul(A,C):
    return [[sum(A[i][k]*C[k][j] for k in range(len(C)))
             for j in range(len(C[0]))] for i in range(len(A))]

def transpose(A):return [list(x) for x in zip(*A)]

# Pair-shadow matrix P: 15 x 20.
P=[[1 if set(e).issubset(S) else 0 for S in TRIPLES] for e in PAIRS]
assert rank_q(P)==15 and rank_q(B)==5
assert matmul(P,B)==[[0]*5 for _ in range(15)]
assert [[B[r][c] for c in range(5)] for r in PIV]==[[1 if i==j else 0 for j in range(5)] for i in range(5)]


def inverse_perm(p):
    q=[0]*6
    for i,j in enumerate(p):q[j]=i
    return tuple(q)

def action20(p,x):
    pinv=inverse_perm(p)
    out=[0]*20
    for idx,S in enumerate(TRIPLES):
        pre=tuple(sorted(pinv[i] for i in S))
        out[idx]=x[TI[pre]]
    return tuple(out)

def action5(p):
    M=[[0]*5 for _ in range(5)]
    for c in range(5):
        x=tuple(B[r][c] for r in range(20))
        y=action20(p,x)
        coords=tuple(y[r] for r in PIV)
        assert all(y[r]==sum(B[r][k]*coords[k] for k in range(5)) for r in range(20))
        for r in range(5):M[r][c]=coords[r]
    return M

GENS=[]
PERMS=[]
for a in range(5):
    p=list(range(6));p[a],p[a+1]=p[a+1],p[a]
    p=tuple(p);PERMS.append(p);GENS.append(action5(p))

# Commutant equations XG=GX in 25 variables have rank 24.
comm_eq=[]
for G in GENS:
    for i in range(5):
        for j in range(5):
            row=[0]*25
            for k in range(5):
                row[5*i+k]+=G[k][j]
                row[5*k+j]-=G[i][k]
            comm_eq.append(row)
assert rank_q(comm_eq)==24

# Fixed vector equations have full rank five: no nonzero S6-fixed pure field.
fix_eq=[]
for G in GENS:
    for i in range(5):
        row=[G[i][j]-(1 if i==j else 0) for j in range(5)]
        fix_eq.append(row)
assert rank_q(fix_eq)==5

# Canonical Gram is invariant.
Ggram=matmul(transpose(B),B)
for R in GENS:
    assert matmul(matmul(transpose(R),Ggram),R)==Ggram

# Perfect-matching trades and V18 tight frame.
def matchings(items):
    items=tuple(items)
    if not items:
        yield ();return
    a=items[0]
    for q in range(1,len(items)):
        b=items[q]
        rest=items[1:q]+items[q+1:]
        for tail in matchings(rest):
            yield tuple(sorted(((min(a,b),max(a,b)),)+tail))
MATCH=tuple(sorted(set(matchings(V))))
assert len(MATCH)==15

def trade(M):
    v=[0]*20;plus=[];minus=[]
    for bits in product((0,1),repeat=3):
        S=tuple(sorted(M[r][bits[r]] for r in range(3)))
        idx=TI[S]
        if sum(bits)%2==0:
            v[idx]+=1;plus.append(idx)
        else:
            v[idx]-=1;minus.append(idx)
    return tuple(v),tuple(plus),tuple(minus)
TRADES=[trade(M) for M in MATCH]
F=[[sum(v[i]*v[j] for v,_,__ in TRADES) for j in range(20)] for i in range(20)]
assert matmul(F,F)==[[24*x for x in row] for row in F]
assert matmul(P,F)==[[0]*20 for _ in range(15)]

# S6 invariance of F under adjacent transpositions.
for p in PERMS:
    # action matrix U on 20 triad coordinates
    U=[]
    for i in range(20):
        e=[0]*20;e[i]=1
        U.append(action20(p,e))
    U=transpose(U)
    assert matmul(matmul(transpose(U),F),U)==F


def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mv(M,x):return tuple(sum(M[i][j]*x[j] for j in range(len(x))) for i in range(len(M)))
def C3(n,m):return dot(n,mv(F,m))

# Minimal trade context resolves pair-shadow-equivalent routes.
v,plus,minus=TRADES[0]
np=tuple(1 if i in plus else 0 for i in range(20))
nm=tuple(1 if i in minus else 0 for i in range(20))
assert tuple(sum(P[e][s]*np[s] for s in range(20)) for e in range(15)) == tuple(sum(P[e][s]*nm[s] for s in range(20)) for e in range(15))
assert C3(np,np)==48
assert C3(nm,np)==-48
assert C3(np,np)-C3(nm,np)==96
# General difference identity v^T F m = 24 v.m.
for m in (np,nm,tuple(range(20)),tuple((-1)**i for i in range(20))):
    assert C3(np,m)-C3(nm,m)==24*dot(v,m)

# Context-free S6 invariant scalar cannot distinguish n+ / n- because a swap
# inside one matching pair maps the two branches exactly.
M=MATCH[0]
a,b=M[0]
p=list(range(6));p[a],p[b]=p[b],p[a];p=tuple(p)
assert action20(p,np)==nm
assert action20(p,nm)==np

# The coupling is simultaneously S6 invariant.
for p in PERMS:
    for n,m in ((np,np),(np,nm),(tuple(range(20)),tuple(reversed(range(20))))):
        assert C3(action20(p,n),action20(p,m))==C3(n,m)

print('PASS_X6_PURE_TRIADIC_FIELD_COUPLING_V20')
print('pure_sector_dimension',5)
print('commutant_dimension',25-rank_q(comm_eq))
print('fixed_vector_dimension',5-rank_q(fix_eq))
print('invariant_bilinear_dimension',1)
print('canonical_coupling_trade_context_scores',(C3(np,np),C3(nm,np)))
print('minimal_trade_context_weight_exponent_gap',96)
print('context_free_S6_scalar_can_select_minimal_trade',False)
print('neighbor_context_can_select_when_pairing_nonzero',True)
