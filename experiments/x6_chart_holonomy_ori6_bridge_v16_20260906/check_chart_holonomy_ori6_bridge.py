#!/usr/bin/env python3
from collections import Counter, deque
from itertools import combinations, permutations, product

# ---------- S3 homomorphism uniqueness ----------
S3=tuple(permutations(range(3)))
ID3=(0,1,2)

def comp3(g,h): return tuple(g[h[i]] for i in range(3))
def parity3(p): return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

homs=[]
for bits in product((0,1),repeat=len(S3)):
    f=dict(zip(S3,bits))
    if f[ID3]!=0: continue
    if all(f[comp3(g,h)]==(f[g]^f[h]) for g in S3 for h in S3):
        homs.append(f)
assert len(homs)==2
nontrivial=next(f for f in homs if set(f.values())=={0,1})
assert all(nontrivial[p]==parity3(p) for p in S3)

# ---------- J(6,3) canonical replacement holonomy ----------
charts=tuple(combinations(range(6),3))

def adjacent(S,T): return len(set(S)&set(T))==2

def repl(S,T):
    shared=set(S)&set(T)
    removed=next(x for x in S if x not in shared)
    entering=next(x for x in T if x not in shared)
    return {x:(x if x in shared else entering) for x in S}

def compose_maps(f,g): return {x:f[g[x]] for x in g}

def holonomy_triangle(tri):
    S,T,U=tri
    return compose_maps(repl(U,S),compose_maps(repl(T,U),repl(S,T)))

def map_parity(h,S):
    p=tuple(S.index(h[x]) for x in S)
    return parity3(p)

triangles=tuple(
    tri for tri in combinations(charts,3)
    if all(adjacent(a,b) for a,b in combinations(tri,2))
)
assert len(triangles)==120
classes=Counter()
curved=[]
for tri in triangles:
    S=tri[0]; h=holonomy_triangle(tri)
    if all(h[x]==x for x in S):
        classes['flat']+=1
        assert map_parity(h,S)==0
    else:
        classes['curved']+=1; curved.append((tri,h))
        assert map_parity(h,S)==1
        assert sum(h[x]!=x for x in S)==2
assert classes=={'flat':60,'curved':60}

# ---------- local signed D12 and charge diagram ----------
N=6
ID=tuple(range(1,N+1))

def compose(g,h):
    out=[]
    for x in h:
        s=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(s*y)
    return tuple(out)

def power(g,n):
    out=ID
    for _ in range(n): out=compose(g,out)
    return out

def perm_parity6(g):
    p=[abs(x)-1 for x in g]
    return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2

def q_canonical():
    g=list(ID); g[0]=-2; g[1]=-3; g[2]=-1; return tuple(g)

def triadic_odd(pair,k):
    i,j=pair; g=list(ID)
    g[i]=-(j+1); g[j]=-(i+1); g[k]=-(k+1); return tuple(g)

def pair_only(pair):
    i,j=pair; g=list(ID); g[i]=j+1; g[j]=i+1; return tuple(g)

q=q_canonical(); o=triadic_odd((0,1),2)
assert power(q,6)==ID and power(o,2)==ID
assert compose(compose(o,q),o)==power(q,5)
G={ID}; queue=deque([ID])
while queue:
    x=queue.popleft()
    for gen in (q,o):
        y=compose(gen,x)
        if y not in G: G.add(y); queue.append(y)
assert len(G)==12

# positive-axis projection to S3 for the selected triad

def proj3(g):
    return tuple(abs(g[i])-1 for i in range(3))

# local charge equals parity of projection for all D12 elements
for g in G:
    assert perm_parity6(g)==parity3(proj3(g))

# fibers over S3 elements have size two
fibers={p:set() for p in S3}
for g in G: fibers[proj3(g)].add(g)
assert all(len(v)==2 for v in fibers.values())

# For every transposition, the two lifts are pair-only and triadic-commonnode types.
transpositions=[p for p in S3 if parity3(p)==1]
for p in transpositions:
    lifts=fibers[p]
    moved_counts=[]
    for g in lifts:
        counts=[]
        for i in range(3):
            src=[0]*6;src[i]=1
            dst=[0]*6; y=g[i];dst[abs(y)-1]=1 if y>0 else -1
            counts.append(sum(abs(a-b) for a,b in zip(src,dst)))
        moved_counts.append(tuple(counts))
    assert sorted(tuple(sorted(c)) for c in moved_counts)==[(0,2,2),(2,2,2)]

# ---------- lift each curved Johnson triangle ----------
# Use canonical base chart orientation (sorted S), and canonical all-minus twist.
# Its transposition holonomy identifies a pair; the remaining axis is the pointed third.
def embed_pair_event(S,h):
    swapped=tuple(sorted(x for x in S if h[x]!=x))
    k=next(x for x in S if h[x]==x)
    return triadic_odd(swapped,k)

for tri,h in curved:
    S=tri[0]
    ev=embed_pair_event(S,h)
    assert perm_parity6(ev)==1
    # projected selected-chart action equals chart holonomy exactly
    for x in S:
        assert abs(ev[x])-1==h[x]

print('PASS_X6_CHART_HOLONOMY_ORI6_BRIDGE_V16')
print('S3_to_C2_homomorphisms',len(homs))
print('nontrivial_bridge','sign/parity')
print('Johnson_triangles',len(triangles))
print('flat_triangles',classes['flat'])
print('curved_transposition_triangles',classes['curved'])
print('local_D12_order',len(G))
print('signed_lifts_per_S3_element',2)
print('triadic_commonnode_lift_unique_for_odd_holonomy',True)
print('chart_holonomy_automatically_physical',False)
