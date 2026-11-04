from fractions import Fraction
from random import Random
from math import gcd

def rank(rows):
    if not rows: return 0
    a=[[Fraction(v) for v in row] for row in rows]
    k=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(k,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[k],a[pivot]=a[pivot],a[k]
        t=a[k][j];a[k]=[v/t for v in a[k]]
        for i in range(len(a)):
            if i!=k:
                t=a[i][j];a[i]=[x-t*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k

def select(M,H):
    T=[];ids=[]
    for i,row in enumerate(H):
        if rank(M+T+[row])>rank(M+T):
            T.append(row);ids.append(i)
    assert len(T)==rank(M+H)-rank(M)
    return T,ids

def in_span(rows,w):return rank(rows+[w])==rank(rows)

M=[[1,1,1,1,1],[0,1,0,2,1],[0,0,1,0,1]]
r1=[1,-2,0,1,0];r2=[1,-1,-1,0,1]
assert rank(M)==3 and rank(M+[r1,r2])==5
assert all(sum(a*b for a,b in zip(row,v))==0 for v in (r1,r2) for row in M)
weights=[(6,12,18,24,36),(6,12,18,24,35),(6,12,18,96,288),(6,12,18,25,35)]
def factor(n):
    r={};p=2
    while p*p<=n:
        while n%p==0:r[p]=r.get(p,0)+1;n//=p
        p+=1
    if n>1:r[n]=r.get(n,0)+1
    return r
for ww in weights:
    pp=[factor(x) for x in ww];primes=sorted({p for fac in pp for p in fac})
    H=[[fac.get(p,0) for fac in pp] for p in primes]
    T,ids=select(M,H)
    assert all(in_span(M+T,row) for row in H)
    want={(6,12,18,24,36):0,(6,12,18,24,35):1,
          (6,12,18,96,288):1,(6,12,18,25,35):2}[ww]
    assert len(T)==want
    print('weights=',ww,'primes=',primes,'rank=',want,'selected_rows=',ids)
baseW=[[1,2,1,3,2],[1,1,2,1,2]]
pd=[0,0,0,1,0];pe=[0,0,0,0,1]
assert len(select(M,baseW)[0])==0
assert len(select(M,baseW+[pd])[0])==1
assert len(select(M,baseW+[pd,pe])[0])==2
assert gcd(2,4)==2
print('source_rank_0_1_2; Smith_1x2=[2,4] nonzero_invariant=2')
rng=Random(483)
for trial in range(480):
    m=2+trial%6
    M0=[[1]*m]+[[rng.randint(-5,5) for _ in range(m)] for _ in range(trial%5)]
    H0=[[rng.randint(-4,4) for _ in range(m)] for _ in range(trial%6)]
    T,_=select(M0,H0)
    assert all(in_span(M0+T,row) for row in H0)
print('GENERAL_EXACT_INTEGER_MATRIX_TRIALS=480')
assert 6*35==210 and 12*18==216
print('WITNESS e35: 210 vs 216')
print('ALL_CHECKS_PASS')
