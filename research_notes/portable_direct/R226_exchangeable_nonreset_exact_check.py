#!/usr/bin/env python3
"""R226: exact stationary reversible exchangeable Markov scalar ideal checks."""
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

K=6
A=F(7,10)
B=F(1,20)
C=F(1,10)
E=F(1,25)
D=F(7,10)
L=2
M=12
PI0=C/(C+K*B)
PI1=B/(C+K*B)
assert A+K*B==1 and C+D+(K-1)*E==1
assert PI0+K*PI1==1 and B!=E

def S2(n,t):
    if n==0: return int(t==0)
    if t==0: return 0
    return S2(n-1,t-1)+t*S2(n-1,t)

def W(r,m=M,L=L):
    import math
    return math.factorial(r)*m**L*sum(S2(L+1,j+1) for j in range(min(r,L)+1))
WEIGHTS=[W(r) for r in range(K+1)]
T=[sum(comb(K-r,j-r)*WEIGHTS[j] for j in range(r,K+1)) for r in range(K+1)]

def mat_vec(A,x):
    return [sum(a*b for a,b in zip(row,x)) for row in A]

def reduction_moments(nmax):
    # H-invariant killed-chain subspaces, counting all subsets of size r.
    result=[]
    vectors=[([F(1)],[A])]+[([F(1),F(1)],[[A,r*B],[C,D+(r-1)*E]]) for r in range(1,K+1)]
    for n in range(1,nmax+1):
        f=F(0)
        for r in range(K+1):
            v,M_r=vectors[r]
            if r==0:
                q=PI0*v[0]
            else:
                q=PI0*v[0]+r*PI1*v[1]
            f+=comb(K,r)*WEIGHTS[r]*q
        result.append(f)
        vectors=[(mat_vec(mat,v),mat) if r else ([A*v[0]],mat) for r,(v,mat) in enumerate(vectors)]
    return result

def direct_moments(nmax):
    # Track (set of seen nonneutral labels, current source), 256 reachable states.
    pi=[PI0]+[PI1]*K
    P=[[A]+[B]*K]
    for i in range(1,K+1):
        P.append([C]+[D if i==j else E for j in range(1,K+1)])
    states={(1<<(i-1) if i else 0,i):prob for i,prob in enumerate(pi)}
    out=[]
    for n in range(1,nmax+1):
        out.append(sum(prob*T[mask.bit_count()] for (mask,_),prob in states.items()))
        newer={}
        for (mask,i),prob in states.items():
            for j,p in enumerate(P[i]):
                new_mask=mask|(1<<(j-1) if j else 0)
                key=(new_mask,j)
                newer[key]=newer.get(key,F(0))+prob*p
        states=newer
    return out

# exact rational Gaussian elimination
def rank_frac(mat):
    a=[row[:] for row in mat]
    nrow=len(a); ncol=len(a[0]); rank=0
    for c in range(ncol):
        pivot=next((r for r in range(rank,nrow) if a[r][c]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        z=a[rank][c]
        for j in range(c,ncol): a[rank][j]/=z
        for r in range(rank+1,nrow):
            q=a[r][c]
            if q:
                for j in range(c,ncol): a[r][j]-=q*a[rank][j]
        rank+=1
        if rank==nrow:break
    return rank

def det_mod(mat,p):
    a=[[int(x.numerator%p)*pow(x.denominator%p,-1,p)%p for x in row] for row in mat]
    det=1
    for c in range(len(a)):
        pos=next((r for r in range(c,len(a)) if a[r][c]),None)
        if pos is None:return 0
        if pos!=c:
            a[c],a[pos]=a[pos],a[c]
            det=-det
        pivot=a[c][c]
        det=det*pivot%p
        inv=pow(pivot,-1,p)
        for r in range(c+1,len(a)):
            factor=a[r][c]*inv%p
            for j in range(c+1,len(a)):
                a[r][j]=(a[r][j]-factor*a[c][j])%p
            a[r][c]=0
    return det%p

seq=reduction_moments(2+2*12)
direct=direct_moments(8)
assert seq[:8]==direct
H=[[seq[1+i+j] for j in range(12)] for i in range(12)] # n starts at 2
assert rank_frac(H)==12
moduli=[1000000007,1000000009]
moddets=[dict(prime=p,det=det_mod(H,p)) for p in moduli]
assert all(x['det'] for x in moddets)
# a scalar 12th order recurrence from P_r characteristic polynomials plus x-1 and x-a
poly=[F(1)]
def mul_poly(x,y):
    ans=[F(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y): ans[i+j]+=a*b
    return ans
poly=mul_poly(poly,[-F(1),F(1)])
poly=mul_poly(poly,[-A,F(1)])
for r in range(1,K):
    tr=A+D+(r-1)*E
    dt=A*(D+(r-1)*E)-r*B*C
    poly=mul_poly(poly,[dt,-tr,F(1)])
assert len(poly)==13
for n in range(2,2+13):
    assert sum(poly[i]*seq[n-1+i] for i in range(len(poly)))==0
assert B*C != E*(A+E-D)
# full P is reversible and has eigenvalues 1, a-c, d-e (multiplicity k-1)
assert A-C>0 and D-E>0

def fmt(x):return str(x)
# General block-exchangeable projection check: group sizes (3,3), bound 38.
GROUPS=[3,3]
BLOCKS=[0,0,0,1,1,1]
BG=[F(1,40),F(1,50)]
CG=[F(1,25),F(1,30)]
EG=[[F(1,80),F(1,100)],[F(1,96),F(1,90)]]
assert BG[0]*EG[0][1]/CG[0]==BG[1]*EG[1][0]/CG[1]
DA=[1-CG[g]-sum((GROUPS[h]-(g==h))*EG[g][h] for h in range(2)) for g in range(2)]
A0=1-sum(GROUPS[g]*BG[g] for g in range(2))
P2=[[A0]+[BG[BLOCKS[j]] for j in range(6)]]
for i in range(6):
    g=BLOCKS[i]
    P2.append([CG[g]]+[DA[g] if i==j else EG[g][BLOCKS[j]] for j in range(6)])
assert all(sum(row)==1 for row in P2)
PI02=1/(1+sum(GROUPS[g]*BG[g]/CG[g] for g in range(2)))
PIG=[PI02*BG[g]/CG[g] for g in range(2)]
PI2=[PI02]+[PIG[BLOCKS[i]] for i in range(6)]
assert sum(PI2)==1
assert all(PI2[i]*P2[i][j]==PI2[j]*P2[j][i] for i in range(7) for j in range(7))

def block_reduced_moments(nmax):
    out=[F(0)]*nmax
    for r0 in range(GROUPS[0]+1):
        for r1 in range(GROUPS[1]+1):
            r=[r0,r1]
            included=[g for g in range(2) if r[g]]
            mat=[[A0]+[r[g]*BG[g] for g in included]]
            for g in included:
                mat.append([CG[g]]+[(DA[g]+(r[g]-1)*EG[g][g]) if g==h else r[h]*EG[g][h] for h in included])
            v=[F(1)]*len(mat)
            factor=comb(3,r0)*comb(3,r1)*WEIGHTS[r0+r1]
            for n in range(nmax):
                out[n]+=factor*(PI02*v[0]+sum(r[g]*PIG[g]*v[t+1] for t,g in enumerate(included)))
                v=mat_vec(mat,v)
    return out

def block_direct_moments(nmax):
    states={(1<<(i-1) if i else 0,i):prob for i,prob in enumerate(PI2)}
    out=[]
    for n in range(nmax):
        out.append(sum(prob*T[mask.bit_count()] for (mask,_),prob in states.items()))
        nxt={}
        for (mask,i),prob in states.items():
            for j,p in enumerate(P2[i]):
                key=(mask|(1<<(j-1) if j else 0),j)
                nxt[key]=nxt.get(key,F(0))+prob*p
        states=nxt
    return out
block_a=block_reduced_moments(6)
block_b=block_direct_moments(6)
assert block_a==block_b
block_dim=(GROUPS[0]+1)*(GROUPS[1]+1)+sum(GROUPS[g]*(GROUPS[1-g]+1) for g in range(2))-2
assert block_dim==38

output={
 'schema':'EM_R226_EXCHANGEABLE_NONRESET_REVERSIBLE_V1',
 'status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED',
 'inputs':{'m':M,'k':K,'L':L,'a':fmt(A),'b':fmt(B),'c':fmt(C),'d':fmt(D),'e':fmt(E),'pi0':fmt(PI0),'pi_each':fmt(PI1)},
 'W':WEIGHTS,'T':T,
 'full_markov_eigenvalues':['1',fmt(A-C),fmt(D-E)],
 'minimal_scalar_degree':12,
 'hankel_rank':12,
 'hankel_determinants_mod_primes':moddets,
 'exact_full_state_vs_reduced_moment_checks':len(direct),
 'moment_prefix':{str(n):fmt(seq[n-1]) for n in [2,3,4,8,12]},
 'characteristic_recurrence_ascending_coefficients':[fmt(x) for x in poly],
 'recurrence_checks':13,
 'distinct_roots_certificate':{'bc':fmt(B*C),'e_times_a_plus_e_minus_d':fmt(E*(A+E-D)),'unequal':True},
 'block_symmetric_check':{'group_sizes':GROUPS,'reduced_realization_bound':block_dim,'moment_comparisons':len(block_a),'first_terms':[fmt(x) for x in block_a[:4]],'result':'PASS'},
 'result':'PASS'}
path=Path(__file__).with_name('R226_verification.json')
path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:output[k] for k in ['minimal_scalar_degree','hankel_rank','hankel_determinants_mod_primes','exact_full_state_vs_reduced_moment_checks','moment_prefix','result']},indent=2))
