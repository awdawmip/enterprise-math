#!/usr/bin/env python3
"""Exact lattice/decoder checks for rank-3 FACE/PATH FCC chart readouts."""
from itertools import combinations, product
from fractions import Fraction
from collections import Counter

NAMES=('AB','AC','AD','BC','BD','CD')
EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
V=((1,1,0),(1,0,1),(0,1,-1),(0,1,1),(1,0,-1),(1,-1,0))
CHARTS=tuple(combinations(range(6),3))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def det(M):
    # rows
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def matrix(S): return tuple(tuple(V[S[j]][i] for j in range(3)) for i in range(3))
def matvec(M,x): return tuple(sum(M[i][j]*x[j] for j in range(3)) for i in range(3))
def matmul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def transpose(A): return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))
def gram(M): return matmul(transpose(M),M)
def adj(M):
    return (
      ( M[1][1]*M[2][2]-M[1][2]*M[2][1], M[0][2]*M[2][1]-M[0][1]*M[2][2], M[0][1]*M[1][2]-M[0][2]*M[1][1]),
      ( M[1][2]*M[2][0]-M[1][0]*M[2][2], M[0][0]*M[2][2]-M[0][2]*M[2][0], M[0][2]*M[1][0]-M[0][0]*M[1][2]),
      ( M[1][0]*M[2][1]-M[1][1]*M[2][0], M[0][1]*M[2][0]-M[0][0]*M[2][1], M[0][0]*M[1][1]-M[0][1]*M[1][0]),
    )
def inv(M):
    d=det(M); A=adj(M)
    return tuple(tuple(Fraction(A[i][j],d) for j in range(3)) for i in range(3))
def graph_type(S):
    deg=[0]*4
    for i in S:
        a,b=EDGES[i]; deg[a]+=1;deg[b]+=1
    return {(3,1,1,1):'STAR',(2,2,2,0):'FACE',(2,2,1,1):'PATH'}[tuple(sorted(deg,reverse=True))]
def char_coeff(G):
    tr=sum(G[i][i] for i in range(3))
    G2=matmul(G,G); tr2=sum(G2[i][i] for i in range(3))
    e2=(tr*tr-tr2)//2
    return (1,-tr,e2,-det(G)) # lambda^3 + c1 lambda^2 + c2 lambda + c3

def in_fcc(y): return sum(y)%2==0

rank3=[]; star=[]
for S in CHARTS:
    M=matrix(S); typ=graph_type(S); d=det(M)
    if typ=='STAR':
        assert d==0; star.append(S)
    else:
        assert abs(d)==2
        assert all(sum(V[i])%2==0 for i in S)
        rank3.append(S)
        expected=(1,-6,9,-4) if typ=='FACE' else (1,-6,10,-4)
        assert char_coeff(gram(M))==expected
assert len(rank3)==16 and len(star)==4

# Every rank-3 chart is a Z-basis of the FCC parity lattice. Exact bounded decode
# exercises the symbolic index argument on a nontrivial cube.
decode_checks=0
for S in rank3:
    M=matrix(S); Mi=inv(M)
    for y in product(range(-4,5),repeat=3):
        x=matvec(Mi,y)
        integral=all(v.denominator==1 for v in x)
        assert integral==in_fcc(y)
        if integral:
            xi=tuple(int(v) for v in x)
            assert matvec(M,xi)==y
            decode_checks+=1

# Every transition between two rank-3 carrier bases is integral unimodular.
transition_checks=0
for S in rank3:
    MS=matrix(S)
    for T in rank3:
        Tinv=inv(matrix(T)); A=matmul(Tinv,MS)
        assert all(x.denominator==1 for row in A for x in row)
        Ai=tuple(tuple(int(x) for x in row) for row in A)
        assert abs(det(Ai))==1
        transition_checks+=1

# STAR is exactly the lossy planar type: the good 120-oriented rays sum to zero.
star_orientation_checks=0
for S in star:
    good=[]
    for ss in product((-1,1),repeat=3):
        W=[tuple(ss[r]*x for x in V[i]) for r,i in enumerate(S)]
        if all(dot(W[a],W[b])==-1 for a,b in combinations(range(3),2)):
            good.append(W)
    assert len(good)==2
    for W in good:
        assert tuple(sum(W[r][i] for r in range(3)) for i in range(3))==(0,0,0)
        star_orientation_checks+=1

# Representative spectral polynomials:
# STAR lambda(lambda-3)^2; FACE (lambda-4)(lambda-1)^2;
# PATH (lambda-2)(lambda^2-4lambda+2).
for S in CHARTS:
    typ=graph_type(S); c=char_coeff(gram(matrix(S)))
    if typ=='STAR': assert c==(1,-6,9,0)
    elif typ=='FACE': assert c==(1,-6,9,-4)
    else: assert c==(1,-6,10,-4)

print('PASS_X6_NONFCC_FCC_BASIS_DECODER_V5')
print('rank3_FCC_basis_charts',len(rank3))
print('STAR_planar_lossy_charts',len(star))
print('bounded_exact_decodes',decode_checks)
print('unimodular_rank3_transitions',transition_checks)
print('STAR_120_kernel_checks',star_orientation_checks)
print('FCC_lattice_parity','x+y+z even')
print('FACE_spectrum','4,1,1')
print('PATH_spectrum','2,2+sqrt(2),2-sqrt(2)')
