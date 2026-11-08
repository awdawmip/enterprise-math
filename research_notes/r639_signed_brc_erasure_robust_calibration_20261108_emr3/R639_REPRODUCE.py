"""R639: exact six-axis 5-adic calibration; signed R462 K branches, stdlib only."""
from itertools import combinations, permutations
from math import comb
from collections import Counter

c=(0,5,1,2,3,4)

def det(m):
    if not m:return 1
    a=[list(r) for r in m];n=len(a);previous=1;sgn=1
    for k in range(n-1):
        if not a[k][k]:
            p=next((i for i in range(k+1,n) if a[i][k]),None)
            if p is None:return 0
            a[k],a[p]=a[p],a[k];sgn=-sgn
        d=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=a[i][j]*d-a[i][k]*a[k][j]
                assert v%previous==0
                a[i][j]=v//previous
            a[i][k]=0
        previous=d
    return sgn*a[-1][-1]

def v5(n):
    assert n;n=abs(n);e=0
    while n%5==0:n//=5;e+=1
    return e

def matrix(ids):return [[c[i]**k for k in range(len(ids))] for i in ids]

def adj(m):
    n=len(m)
    if n==1:return [[1]]
    return [[(-1)**(i+j)*det([[m[r][s] for s in range(n) if s!=i]
        for r in range(n) if r!=j]) for j in range(n)] for i in range(n)]

def recover(m,y,N):
    d=det(m);e=v5(d);mod=5**N
    assert N>e
    inv=pow((d//5**e)%5,-1,5)
    out=[]
    for r in adj(m):
        a=sum(x*v for x,v in zip(r,y))%mod
        assert a%5**e==0
        out.append((a//5**e*inv)%5)
    return out

def brc_K(i):
    b=lambda n,k:comb(n,k) if 0<=k<=n else 0
    ds=(-b(4,i)+b(2,i-1),b(5,i-1)-b(5,i-2),b(7,i-2),-b(9,i-3))
    out=[0]*(i+16)
    for j,v in enumerate(ds,1):
        if not v or i+1-j<0:continue
        for k in range(i+2-j):out[k+i-1]-=v*b(i+1-j,k)
    return out
P=[brc_K(i) for i in range(1,13,2)]
assert [P[j][2*j] for j in range(6)]==[2,-8,6,106,83,9]

sizes={};coefficient_checks=0;counterexamples=0;erasure_checks=0;orientation_checks=0
for q in range(1,7):
    cases=list(combinations(range(6),q));digits=[]
    for ids in cases:
        m=matrix(ids);e=v5(det(m));special=(0 in ids and 1 in ids)
        assert e==int(special)
        digits.append(e+1)
        for t in range(11):
            h=[(k+2)*(t*t+7*t+1)+(k*k+3)*(-1)**t for k in range(q)]
            y=[sum(m[r][k]*h[k] for k in range(q))%(5**(e+1)) for r in range(q)]
            assert recover(m,y,e+1)==[v%5 for v in h]
            coefficient_checks+=q
        if special:
            f=[0,1]
            for i in ids:
                if i in (0,1):continue
                z=c[i];g=[0]*(len(f)+1)
                for k,v in enumerate(f):g[k]-=z*v;g[k+1]+=v
                f=g
            assert len(f)==q and f[-1]==1
            assert all(sum(m[r][k]*f[k] for k in range(q))%5==0 for r in range(q))
            counterexamples+=1
        for a in (1,2,4):
            d=a+8
            h=[[(i-3)*(t+1)+2*(i+1)*(t%3) for t in range(d+1)] for i in range(q)]
            recovered=[]
            for t in range(d+1):
                y=[sum(m[r][k]*h[k][t] for k in range(q))%(5**(e+1)) for r in range(q)]
                recovered.append(recover(m,y,e+1))
            assert recovered==[[h[k][t]%5 for k in range(q)] for t in range(d+1)]
            for pi in permutations(range(6)):
                sig=[]
                for label in pi:
                    first=next((t for t in range(d+1) if 0<=t-a<len(P[label]) and P[label][t-a]%5),None)
                    sig.append(5 if first is None else (first-a)//2)
                assert tuple(sig)==pi
                orientation_checks+=1
    summary={'mod5':digits.count(1),'mod25':digits.count(2)}
    if q<6:
        robust=Counter()
        for ids in combinations(range(6),q+1):
            worst=max(v5(det(matrix(tuple(i for i in ids if i!=lost))))+1 for lost in ids)
            robust[worst]+=1;erasure_checks+=len(ids)
        summary.update(erasure_mod5=robust[1],erasure_mod25=robust[2])
    sizes[q]=summary
assert sum(v['mod5']+v['mod25'] for v in sizes.values())==63
assert (counterexamples,orientation_checks,erasure_checks)==(16,136080,186)
print('R639_VANDERMONDE_ERASURE_EXACT_PASS', sizes, 'coefficient',coefficient_checks,
      'kernels',counterexamples,'erasure',erasure_checks,'BRC orientations',orientation_checks)
