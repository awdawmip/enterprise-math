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
