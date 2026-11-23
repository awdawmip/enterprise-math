from itertools import product
from fractions import Fraction as Q
G={}
for v in product(range(-10,11),repeat=3):
    if not any(v) or next(z for z in v if z)<0 or max(sum(max(z,0) for z in v),sum(max(-z,0) for z in v))>10:continue
    x,y,z=v;h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    G[v]=tuple(abs(h[j]-h[i]) for i,j in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))
assert len(G)==1935
P=[v for v,g in G.items() if not any(u!=v and all(a<=b for a,b in zip(h,g)) for u,h in G.items())]
assert len(P)==12 and all(any(all(a<=b for a,b in zip(G[u],g)) for u in P) for g in G.values())
V,A,K,H,J,E=(6,-1,0),(1,0,0),(5,-1,0),(9,-5,1),(4,-1,0),(6,-4,1)
W=(V,A,K,H,J,E)
assert set(W)<=set(P)
# projective coordinates b=B/(1+B+D), d=D/(1+B+D)
S=((136,-135,-136),(312,-312,-312),(136,-136,-135),(176,-175,-176),(0,1,1),(176,-176,-175))
T=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(0),Q(1))]
def ev(l,p):return l[0]+l[1]*p[0]+l[2]*p[1]
def cmp(n,j,m,k):return tuple(n*b-m*a for a,b in zip(S[j],S[k]))
def clip(P,l):
    R=[]
    for a,b in zip(P,P[1:]+P[:1]):
        x,y=ev(l,a),ev(l,b)
        if x>=0:R.append(a)
        if x*y<0:R.append(tuple((x*t-y*s)/(x-y) for s,t in zip(a,b)))
    return list(dict.fromkeys(R))
def area(P):return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(P,P[1:]+P[:1])) if len(P)>2 else 0
# If a row can strictly beat the bank, continuity gives an open set. In at least one active channel j, all six-bank comparisons can be chosen strictly; their closure then has positive area. Conversely a positive-area surviving cell (excluding identically-zero strict comparisons) would have strict interior.
for v in P:
    if v in W:continue
    counts=[]
    for j,n in enumerate(G[v]):
        if not n:continue
        R=T
        for k,m in enumerate(G[v]):R=clip(R,cmp(n,j,m,k))
        cells=[R] if area(R)>0 else []
        for w in W:
            new=[]
            for Qp in cells:
                for k,m in enumerate(G[w]):
                    l=cmp(m,k,n,j)
                    if l==(0,0,0):continue
                    X=clip(Qp,l)
                    if area(X)>0:new.append(X)
            cells=new
        counts.append(len(cells))
        assert not cells,(v,j)
    print('EXCLUDED FROM OPTIMIZER BANK',v,counts)
# Unique full-lattice optimizers prove every bank member necessary.
witnesses=[(V,1,1),(A,4,521),(K,46,495),(H,91,430),(J,139,1119),(E,1,1652)]
for v,B,D in witnesses:
    s=(136+B,312,136+D,176+B,B+D,176+D)
    f={u:max(Q(a,b) for a,b in zip(g,s)) for u,g in G.items()};m=min(f.values());assert [u for u in f if f[u]==m]==[v],(v,B,D,m,[u for u in f if f[u]==m])
    second=min(a for u,a in f.items() if u!=v)
    print('UNIQUE',v,B,D,m,second)
print('SIX-WITNESS GLOBAL IRREDUNDANT BANK PASS')
