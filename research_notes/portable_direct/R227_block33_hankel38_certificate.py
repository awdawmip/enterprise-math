#!/usr/bin/env python3
"""Independent exact 38-state Hankel certificate for 3+3 source block symmetry."""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json

GROUPS=(3,3)
TYPES=(0,0,0,1,1,1)
B=(Q(1,40),Q(1,50))
C=(Q(1,25),Q(1,30))
E=((Q(1,80),Q(1,100)),(Q(1,96),Q(1,90)))
D=tuple(1-C[g]-sum((GROUPS[h]-int(g==h))*E[g][h] for h in range(2)) for g in range(2))
A=1-sum(GROUPS[g]*B[g] for g in range(2))
PI0=1/(1+sum(GROUPS[g]*B[g]/C[g] for g in range(2)))
PIG=tuple(PI0*B[g]/C[g] for g in range(2))
assert (A,D,PI0,PIG)==(Q(173,200),(Q(181,200),Q(263,288)),Q(40,187),(Q(25,187),Q(24,187)))
assert PIG[0]*E[0][1]==PIG[1]*E[1][0]
assert A>Q(1,2) and all(d>Q(1,2) for d in D)

def S2(n,j):
    if n==0:return int(j==0)
    if j==0:return 0
    return S2(n-1,j-1)+j*S2(n-1,j)

K=6;M=12;L=2
W=[factorial(r)*M**L*sum(S2(L+1,j+1) for j in range(min(r,L)+1)) for r in range(K+1)]
T=[sum(comb(K-r,j-r)*W[j] for j in range(r,K+1)) for r in range(K+1)]
P=[[A]+[B[TYPES[i]] for i in range(K)]]
for i in range(K):
    g=TYPES[i]
    P.append([C[g]]+[D[g] if i==j else E[g][TYPES[j]] for j in range(K)])
PI=[PI0]+[PIG[TYPES[i]] for i in range(K)]
assert all(sum(row)==1 for row in P)
assert sum(PI)==1
assert all(PI[i]*P[i][j]==PI[j]*P[j][i] for i in range(K+1) for j in range(K+1))

def scalar_orbit_terms(nmax,field):
    """Computes f_1..f_nmax via the 3+3 orbit killed-subchain states."""
    result=[0]*nmax
    for r0 in range(4):
        for r1 in range(4):
            rs=(r0,r1)
            idx=[g for g in range(2) if rs[g]]
            mat=[[A]+[rs[g]*B[g] for g in idx]]
            for g in idx:
                mat.append([C[g]]+[(D[g]+(rs[g]-1)*E[g][g]) if g==h else rs[h]*E[g][h] for h in idx])
            mat=[[field(x) for x in row] for row in mat]
            left=[field(PI0)]+[field(rs[g]*PIG[g]) for g in idx]
            v=[field(Q(1))]*len(mat)
            factor=field(Q(comb(3,r0)*comb(3,r1)*W[r0+r1]))
            for n in range(nmax):
                result[n]+=factor*sum(left[i]*v[i] for i in range(len(v)))
                v=[sum(a*b for a,b in zip(row,v)) for row in mat]
    return result

def direct_terms(nmax):
    state={(0 if i==0 else 1<<(i-1),i):PI[i] for i in range(K+1)}
    out=[]
    for n in range(nmax):
        out.append(sum(p*T[mask.bit_count()] for (mask,_),p in state.items()))
        nxt={}
        for (mask,i),prob in state.items():
            for j,p in enumerate(P[i]):
                key=(mask if j==0 else mask|(1<<(j-1)),j)
                nxt[key]=nxt.get(key,Q(0))+prob*p
        state=nxt
    return out

exact=scalar_orbit_terms(6,Q)
assert exact==direct_terms(6)

def det_mod(mat,prime):
    matrix=[row[:] for row in mat]
    det=1
    for j in range(len(matrix)):
        pivot=next((i for i in range(j,len(matrix)) if matrix[i][j]),None)
        if pivot is None:return 0,j
        if pivot!=j:
            matrix[j],matrix[pivot]=matrix[pivot],matrix[j]
            det=-det
        val=matrix[j][j]
        det=det*val%prime
        inv=pow(val,-1,prime)
        for i in range(j+1,len(matrix)):
            factor=matrix[i][j]*inv%prime
            for v in range(j+1,len(matrix)):
                matrix[i][v]=(matrix[i][v]-factor*matrix[j][v])%prime
            matrix[i][j]=0
    return det%prime,len(matrix)

cert=[]
for prime,expected in [(1000000007,166715278),(1000000009,549336287)]:
    to_mod=lambda x:(x.numerator%prime)*pow(x.denominator%prime,-1,prime)%prime
    seq=[v%prime for v in scalar_orbit_terms(76,to_mod)]
    H=[[seq[1+i+j] for j in range(38)] for i in range(38)]
    determinant,rank=det_mod(H,prime)
    assert (determinant,rank)==(expected,38)
    cert.append({'prime':prime,'determinant':determinant,'rank':rank,'first_modular_terms':seq[:4]})

out={'schema':'EM_R227_BLOCK33_HANKEL38_V1','status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED',
     'k':K,'m':M,'L':L,'source_group_sizes':list(GROUPS),
     'a':str(A),'b':list(map(str,B)),'c':list(map(str,C)),'e':[[str(v) for v in row] for row in E],
     'd':list(map(str,D)),'stationary_pi0':str(PI0),'stationary_pi_group_each':list(map(str,PIG)),
     'reversible':True,'strictly_positive':True,'all_eigenvalues_positive_by_diagonal_dominance':True,
     'orbit_dimension_upper_bound':38,'exact_hankel_rank':38,'minimal_scalar_degree':38,
     'hankel_congruences':cert,'exact_256_state_comparisons':6,
     'exact_first_terms':[str(v) for v in exact[:4]],'result':'PASS'}
Path(__file__).with_name('R227_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'rank':out['exact_hankel_rank'],'determinants':cert,'exact_terms':out['exact_first_terms'],'result':out['result']},indent=2))
