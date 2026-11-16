#!/usr/bin/env python3
"""R230: exact nested-source spectral collision, standard library only.

All primary dynamics and polynomial calculations use fractions.Fraction;
modular Hankel nonzero witnesses certify full rational rank.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from math import comb, factorial

ALPHA = tuple(map(F, ('1/5', '1/4', '3/4', '4/5')))
PI = tuple(map(F, ('3/8', '1/8', '3/8', '1/8')))
K = len(ALPHA)-1
L = 2
X = F(1,2)


def trim(p):
    q=list(p)
    while len(q)>1 and q[-1]==0: q.pop()
    return q

def add(p,q):
    return trim([(p[i] if i<len(p) else F(0))+(q[i] if i<len(q) else F(0)) for i in range(max(len(p),len(q)))])

def sub(p,q):
    return add(p,[-v for v in q])

def mul(p,q):
    v=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):v[i+j]+=a*b
    return trim(v)

def monic(p):
    p=trim(p)
    if p==[0]: return p
    return [v/p[-1] for v in p]

def divmod_poly(a,b):
    a=trim(a); b=trim(b)
    assert b!=[0]
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        t=a[-1]/b[-1]; j=len(a)-len(b); q[j]=t
        a=sub(a,[F(0)]*j+[t*v for v in b])
    return trim(q),a

def gcd_poly(a,b):
    while b!=[0]:a,b=b,divmod_poly(a,b)[1]
    return monic(a)

def lcm_poly(a,b):
    g=gcd_poly(a,b)
    q,r=divmod_poly(mul(a,b),g)
    assert r==[0]
    return monic(q)

def evaluate(p,x):
    v=F(0)
    for c in reversed(p):v=v*x+c
    return v

def block_poly(D):
    z=[F(1)]
    for i in D:z=mul(z,[-ALPHA[i],F(1)])
    for i in D:
        t=[F(1)]
        for j in D:
            if i!=j:t=mul(t,[-ALPHA[j],F(1)])
        z=sub(z,[(F(1)-ALPHA[i])*PI[i]*c for c in t])
    return monic(z)

def killed_secular(D,x):
    assert all(x!=ALPHA[i] for i in D)
    return sum(((F(1)-ALPHA[i])*PI[i]/(x-ALPHA[i]) for i in D),F(0))

def all_blocks():
    for r in range(K):
        for U in combinations(range(1,K+1),r):
            yield (0,)+U

def bell_stirling_2(n,k):
    S=[[0]*(k+2) for _ in range(n+1)]
    S[0][0]=1
    for a in range(1,n+1):
        for b in range(1,min(a,k)+1):S[a][b]=b*S[a-1][b]+S[a-1][b-1]
    return S[n][k]

def weights():
    return [factorial(r)*sum(bell_stirling_2(L+1,j+1) for j in range(min(r,L)+1)) for r in range(K+1)]

def ideals(W):
    return [sum(comb(K-r,j-r)*W[j] for j in range(r,K+1)) for r in range(K+1)]

def direct_sequence(N,W):
    T=ideals(W)
    Z=sum(PI[i]/(1-ALPHA[i]) for i in range(K+1))
    rho=[PI[i]/((1-ALPHA[i])*Z) for i in range(K+1)]
    P=[[ALPHA[i]*(i==j)+(1-ALPHA[i])*PI[j] for j in range(K+1)] for i in range(K+1)]
    dp={(i, (1<<(i-1)) if i>0 else 0):rho[i] for i in range(K+1)}
    seq=[]
    for n in range(1,N+1):
        seq.append(sum((v*T[mask.bit_count()] for (i,mask),v in dp.items()),F(0)))
        nd={}
        for (i,mask),v in dp.items():
            for j in range(K+1):
                key=(j,mask | ((1<<(j-1)) if j else 0))
                nd[key]=nd.get(key,F(0))+v*P[i][j]
        dp=nd
    return seq

def moddet(H,prime):
    n=len(H); a=[]
    for row in H:
        a.append([(x.numerator%prime)*pow(x.denominator,-1,prime)%prime for x in row])
    det=1
    for k in range(n):
        pivot=next((r for r in range(k,n) if a[r][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];det=-det
        v=a[k][k];det=det*v%prime
        inv=pow(v,-1,prime)
        for j in range(k+1,n):
            factor=a[j][k]*inv%prime
            for t in range(k+1,n):a[j][t]=(a[j][t]-factor*a[k][t])%prime
            a[j][k]=0
    return det%prime


def main():
    assert sum(PI)==1 and all(0<x<1 for x in ALPHA)
    A=(0,); B=(0,1,2)
    assert killed_secular(A,X)==killed_secular(B,X)==1
    assert killed_secular((1,2),X)==0
    assert evaluate(block_poly(A),X)==evaluate(block_poly(B),X)==0
    assert killed_secular((1,),X)==F(3,8) and killed_secular((2,),X)==-F(3,8)
    polys={','.join(map(str,D)):block_poly(D) for D in all_blocks()}
    q=[F(-1),F(1)]
    for c in polys.values():q=lcm_poly(q,c)
    d=len(q)-1
    assert d==16
    W=weights();T=ideals(W)
    assert W==[1,4,10,30] and T==[73,54,40,30]
    seq=direct_sequence(L+2*d+5,W)
    assert all(sum((q[j]*seq[n+j-1] for j in range(d+1)),F(0))==0 for n in range(L,L+d+5))
    H=[[seq[L-1+i+j] for j in range(d)] for i in range(d)]
    mods={str(p):moddet(H,p) for p in (1000000007,1000000009)}
    assert all(mods.values())
    assert len(polys)==7
    output={
      'status':'PASS','model':{'k':K,'L':L,'alpha':[str(a) for a in ALPHA],'pi':[str(p) for p in PI]},
      'nested_proper_blocks':{'small':list(A),'large':list(B),'shared_lambda':str(X)},
      'minimal_degree':d,'uncollided_upper_bound':17,'blocks':len(polys),
      'weights':W,'ideal_sizes':T,'hankel_determinants_mod':mods,
      'sequence_first_eight':[str(x) for x in seq[:8]],
      'recurrence_checked_at_n':list(range(L,L+d+5)),
      'full_hankel_n_range':[L,L+2*d-2],
      'general_claim_proof':'algebraic secular difference, not finite testing',
      'numerical_scope':'exact rational DP and polynomial gcd/lcm in this k=3 example; two nonzero modular determinants certify rational rank at least 16',
      'review':'NOT_REVIEWED','native_brc_integration':'NOT_EXECUTED'
    }
    with open('R230_nested_source_collision_verification.json','w',encoding='utf-8') as f:
        json.dump(output,f,ensure_ascii=False,sort_keys=True,indent=2)
        f.write('\n')
    print('PASS degree',d,'Hankel',mods,'first-8',output['sequence_first_eight'])
if __name__=='__main__':main()
