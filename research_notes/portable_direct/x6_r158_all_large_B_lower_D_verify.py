from itertools import product
from fractions import Fraction as Q
G={}
for v in product(range(-10,11),repeat=3):
    if not any(v) or next(z for z in v if z)<0 or max(sum(max(z,0) for z in v),sum(max(-z,0) for z in v))>10:continue
    x,y,z=v;h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    G[v]=tuple(abs(h[j]-h[i]) for i,j in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))
assert len(G)==1935
S=((136,1,0),(312,0,0),(136,0,1),(176,1,0),(0,1,1),(176,0,1))
A=(1,0,0);C=(5,-4,1);K=(5,-1,0);H=(9,-5,1);U=(4,-4,1);V=(6,-1,0)
W={V,A,C,K,H,U};bank=(V,A,K,H)
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
P0=[(Q(b),Q(d)) for b,d in [(20,0),(136,0),(136,528),(20,528)]]
cells=[(P0,())]
for v in bank:
    new=[]
    for P,act in cells:
        for j,n in enumerate(G[v]):
            if not n:continue
            R=P
            for k,m in enumerate(G[v]):R=clip(R,cmp(n,j,m,k))
            if area(R)>0:new.append((R,act+((n,j),)))
    cells=new
regions=[]
for P,act in cells:
    for n,j in sorted(set(act)):
        R=P
        for m,k in act:R=clip(R,cmp(m,k,n,j))
        if area(R)>0:regions.append((R,n,j))
assert sum(area(P) for P,n,j in regions)==area(P0)
fixed=0
for P,n,j in regions:
    for v,g in G.items():
        if v in W:continue
        assert any(all(ev(cmp(2*m,k,3*n,j),p)>=0 for p in P) for k,m in enumerate(g)),(v,n,j,P)
        fixed+=1
    for v in (U,C):
        assert any(all(ev(cmp(m,k,n,j),p)>=0 for p in P) for k,m in enumerate(G[v])),(v,n,j,P)
    R=clip(P,(-312,1,1))
    for v in (A,C,K,H):
        assert all(ev(cmp(2*m,k,3*n,j),p)<0 for k,m in enumerate(G[v]) for p in R)
print('MIDDLE CELLS, OUTSIDER CERTIFICATES, POST-PLATEAU RETENTION PASS',len(regions),fixed)
# Unbounded B>=136, D slabs. cmp is affine in B,D, so check the two base vertices and the B recession slope.
slabs=[(0,20,3,2,V),(20,176,6,1,V),(176,488,6,2,H),(488,528,3,1,H)]
fixed=0
for lo,hi,n,j,w in slabs:
    P=[(136,lo),(136,hi)]
    for r,exclude in [(2,set()),(3,W)]:
        for v,g in G.items():
            if v in exclude:continue
            assert any((l:=cmp(2*m,k,r*n,j))[1]>=0 and all(ev(l,p)>=0 for p in P) for k,m in enumerate(g)),(v,lo,r)
            fixed+=1
    for k,m in enumerate(G[w]):
        l=cmp(m,k,n,j);assert l[1]<=0 and all(ev(l,p)<=0 for p in P)
    assert G[w][j]==n
    if lo>=176:
        for v in (A,C,K,H):
            for k,m in enumerate(G[v]):
                l=cmp(2*m,k,3*n,j);assert l[1]<=0 and all(ev(l,p)<0 for p in P)
print('UNBOUNDED LARGE B CERTIFICATE PASS',fixed)
def score(v,B,D):return max(Q(m,ev(s,(B,D))) for m,s in zip(G[v],S))
def pred(B,D):
    eta=min(score(v,B,D) for v in bank)
    b=min(B,Q(136));u=min(396+5*B/4,468-b);v=468-b
    near={a for a,t in [(U,u),(V,v)] if D<t}
    near|={a for a,t in [(A,Q(320,3)),(C,Q(304,3)),(K,Q(200,3)),(H,Q(72))] if D>max(208-B,t)}
    return eta,near
count=0
for B in map(Q,[20,21,32,58,80,Q(304,3),102,Q(320,3),120,136,137,Q(424,3),176,208,312,1000000]):
    b=min(B,Q(136))
    cuts=sorted({Q(0),Q(20),312-b,488,Q(528),min(396+5*B/4,468-b),468-b}|{max(208-B,t) for t in [Q(320,3),Q(304,3),Q(200,3),Q(72)]})
    for D in sorted(set(cuts[1:])|{(a+b)/2 for a,b in zip(cuts,cuts[1:])}):
        scores={v:score(v,B,D) for v in G};eta=min(scores.values());near={v for v,f in scores.items() if 2*f<3*eta}
        assert (eta,near)==pred(B,D),(B,D,eta,near,pred(B,D));count+=1
print('FULL DIRECTION CROSSCHECK PASS',count)
