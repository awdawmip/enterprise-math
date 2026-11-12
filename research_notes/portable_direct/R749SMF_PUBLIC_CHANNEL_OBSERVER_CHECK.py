"""R749SMF: exact rational observer/noise lattice verifier. Standard library only."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

S=(1,-1)
H=list(product(S, repeat=3))
W=list(product(S, repeat=3))

def q(a,b,c,z):
    x,y,t=z
    return F(2+a*x,4)*F(2+b*(y if a==1 else t),4)*F(2+c*y*t,4)

M=[[q(*w,z) for z in H] for w in W]

def rank(A):
    a=[list(row) for row in A]
    m=len(a); n=len(a[0]); i=0
    for j in range(n):
        piv=next((k for k in range(i,m) if a[k][j]),None)
        if piv is None:continue
        a[i],a[piv]=a[piv],a[i]
        div=a[i][j]
        a[i]=[x/div for x in a[i]]
        for k in range(i+1,m):
            if a[k][j]:
                fac=a[k][j];a[k]=[x-fac*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==m:break
    return i

def det(A):
    a=[list(row) for row in A]; n=len(a); accum=F(1)
    for j in range(n):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None:return F(0)
        if p!=j:a[p],a[j]=a[j],a[p];accum=-accum
        d=a[j][j];accum*=d
        for i in range(j+1,n):
            v=a[i][j]/d
            if v:
                for k in range(j+1,n):a[i][k]-=v*a[j][k]
                a[i][j]=F(0)
    return accum

assert all(sum(M[i][j] for i in range(8))==1 for j in range(8))
assert rank(M)==8 and abs(det(M))==F(1,4096)

marginal_ranks={}
for mask in range(8):
    idx=[i for i in range(3) if (mask>>i)&1]
    sub=list(product(S,repeat=len(idx)))
    A=[[sum(M[j][k] for j,w in enumerate(W) if tuple(w[i] for i in idx)==o) for k in range(8)] for o in sub]
    r=rank(A)
    assert r==2**len(idx),(idx,r)
    marginal_ranks[''.join('ABC'[i] for i in idx) or 'none']=r

# Each bit-flip channel has probabilities (1-e,e) for correct/incorrect.
def noisy(e):
    out=[]
    for o in W:
        row=[]
        for k in range(8):
            v=F(0)
            for j,w in enumerate(W):
                p=F(1)
                for i in range(3):p*= F(1)-e[i] if o[i]==w[i] else e[i]
                v+=p*M[j][k]
            row.append(v)
        out.append(row)
    return out

E=[F(0),F(1,4),F(1,2),F(3,4),F(1)]
counts={}
for eps in product(E,repeat=3):
    N=noisy(eps)
    active=sum(x!=F(1,2) for x in eps)
    r=rank(N)
    assert r==2**active, (eps,r,active)
    dd=abs(det(N))
    expected=F(1,4096)
    for e in eps:expected*=abs(1-2*e)**4
    assert dd==expected,(eps,dd,expected)
    counts[active]=counts.get(active,0)+1
    assert all(sum(N[i][j] for i in range(8))==1 for j in range(8))

mu_plus=[F(1+F(y*t,2),8) for x,y,t in H]
mu_minus=[F(1-F(y*t,2),8) for x,y,t in H]
for eps in product(E,repeat=3):
    N=noisy(eps)
    p_plus=[sum(N[i][j]*mu_plus[j] for j in range(8)) for i in range(8)]
    p_minus=[sum(N[i][j]*mu_minus[j] for j in range(8)) for i in range(8)]
    tv=sum(abs(p_plus[i]-p_minus[i]) for i in range(8))/2
    assert tv==abs(1-2*eps[2])/4,(eps,tv)

result={
 "status":"PASS", "scope":"R749SMD three-bit adaptive history controller; independent BSC on public outputs",
 "scientific_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
 "base_full_det":"1/4096", "marginal_ranks":marginal_ranks,
 "exact_BSC_triples_checked":125,"active_bit_rank_counts":{str(k):v for k,v in sorted(counts.items())},
 "exact_determinant_checks":125,"exact_TV_witness_checks":125,
 "minimal_affine_coordinates_by_informative_bit_count":{"0":0,"1":1,"2":3,"3":7},
 "witness_prior":"mu_±(x,y,t)=(1 ± yt/2)/8",
 "witness_TV":"abs(1-2*epsilon_C)/4"
}
print(json.dumps(result,ensure_ascii=False,indent=2))
with Path(__file__).with_name('R749SMF_PUBLIC_CHANNEL_OBSERVER_RESULTS.json').open('w',encoding='utf-8') as f:
    json.dump(result,f,ensure_ascii=False,indent=2)
    f.write('\n')
