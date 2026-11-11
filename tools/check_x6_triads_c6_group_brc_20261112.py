from collections import deque
from itertools import combinations
from math import factorial

N=6
I=tuple(range(1,N+1))
def compose(a,b): return tuple((1 if v>0 else -1)*a[abs(v)-1] for v in b)
def power(a,k):
    x=I
    for _ in range(k): x=compose(a,x)
    return x
def gen(t):
    i,j,k=t; a=list(I); a[i-1]=j; a[j-1]=k; a[k-1]=-i
    return tuple(a)
def flip(T): return tuple(-x if x in T else x for x in I)
G=[]
for t in combinations(I,3):
    g=gen(t); G.append(g)
    assert power(g,3)==flip(t) and power(g,6)==I
for i in I:
    a,b,c=next(combinations([j for j in I if j!=i],3))
    h=compose(compose(flip((i,a,b)),flip((i,a,c))),flip((i,b,c)))
    assert h==flip((i,))
seen={I}; Q=deque([I])
while Q:
    g=Q.popleft()
    for s in G:
        h=compose(s,g)
        if h not in seen: seen.add(h); Q.append(h)
assert len(seen)==23040
assert all(sorted(abs(x) for x in s)==list(I) for s in seen)
assert all(sum(abs(s[i])>abs(s[j]) for i in range(6) for j in range(i+1,6))%2==0 for s in seen)
def path_count(length,z):
    D={(0,)*6:1}
    for _ in range(length):
        E={}
        for x,v in D.items():
            for i in range(6):
                for d in (-1,1):
                    y=list(x);y[i]+=d;y=tuple(y)
                    E[y]=E.get(y,0)+v
        D=E
    return D.get(z,0)
e1=(1,0,0,0,0,0);e2=(0,1,0,0,0,0);e3=(0,0,1,0,0,0)
def displacement(a,b):return tuple(y-x for x,y in zip(a,b))
def min_branches(z):
    m=sum(map(abs,z));out=factorial(m)
    for c in z:out//=factorial(abs(c))
    return out
assert min_branches(displacement(e1,e2))==2
assert min_branches(displacement(e2,e3))==2
assert min_branches(displacement(e1,e3))==2
assert path_count(4,displacement(e1,e3))==120
print("PASS",len(G),len(seen),2*2,120,2)


# Every unoriented triad has an algebraic 12-Cell outer microcycle.
def basis(i,sign=1): return tuple(sign if j==i else 0 for j in range(6))
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def norm2(a): return sum(x*x for x in a)
def apply(g,x):
    y=[0]*6
    for i,u in enumerate(x):
        y[abs(g[i])-1]+=(1 if g[i]>0 else -1)*u
    return tuple(y)
for tri in combinations(range(6),3):
    i,j,k=tri
    a=[basis(i),basis(j),basis(k),basis(i,-1),basis(j,-1),basis(k,-1)]
    mid=[plus(a[r],a[(r+1)%6]) for r in range(6)]
    cells=[v for r in range(6) for v in (a[r],mid[r])]
    g=gen(tuple(t+1 for t in tri))
    assert len(set(cells))==12
    assert [norm2(v) for v in cells]==[1,2]*6
    assert all(sum(map(abs,minus(cells[(t+1)%12],cells[t])))==1 for t in range(12))
    assert all(apply(g,cells[t])==cells[(t+2)%12] for t in range(12))
    assert all(neg(cells[t])==cells[(t+6)%12] for t in range(12))
print("PASS all 20 triads: 12 distinct Cells, primitive edges, F2=R, F6=-id")
