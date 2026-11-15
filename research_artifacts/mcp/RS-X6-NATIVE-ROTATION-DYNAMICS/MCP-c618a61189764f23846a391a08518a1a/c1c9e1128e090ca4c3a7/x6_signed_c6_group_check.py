"""Exact finite enumerator of signed-triad C6 candidate group (algebraic, not physical)."""
from itertools import combinations, permutations, product
from collections import deque
from math import factorial
N=6
ONE=tuple(range(1,N+1))
def compose(a,b):
    return tuple((1 if x>0 else -1)*a[abs(x)-1] for x in b)
def gen(t):
    i,j,k=t
    g=list(ONE); g[i],g[j],g[k]=j+1,k+1,-(i+1)
    return tuple(g)
def power(g,n):
    x=ONE
    for _ in range(n): x=compose(g,x)
    return x
def even(g):
    p=[abs(x) for x in g]
    return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2==0
def closure(gs):
    seen={ONE}; q=deque([ONE])
    while q:
        x=q.popleft()
        for y in gs:
            z=compose(x,y)
            if z not in seen: seen.add(z);q.append(z)
    return seen
gs=[gen(t) for t in combinations(range(N),3)]
for g,t in zip(gs,combinations(range(N),3)):
    assert power(g,6)==ONE
    assert power(g,3)==tuple(-(i+1) if i in t else i+1 for i in range(N))
    assert all(power(g,k)!=ONE for k in range(1,6))
group=closure(gs)
expected={tuple(s*p for s,p in zip(signs,perm)) for perm in permutations(range(1,N+1)) if even(perm) for signs in product((-1,1),repeat=N)}
assert group==expected and len(group)==23040
assert len({tuple(abs(x) for x in g) for g in group})==factorial(N)//2
assert len({tuple(x>0 for x in g) for g in group})==2**N
desc={g for g in group if abs(sum(1 if x>0 else -1 for x in g))==N}
assert len(desc)==720 and len(group-desc)==22320
for g in gs:
    for w in product(list(range(-N,0))+list(range(1,N+1)),repeat=2):
        out=[0]*N; end=[0]*N
        for letter in w:
            end[abs(letter)-1]+=1 if letter>0 else -1
            im=(1 if letter>0 else -1)*g[abs(letter)-1]
            out[abs(im)-1]+=1 if im>0 else -1
        expected_end=[0]*N
        for i,v in enumerate(end):
            im=g[i];expected_end[abs(im)-1]+=v*(1 if im>0 else -1)
        assert out==expected_end
print({"generators":len(gs),"group_order":len(group),"sign_masks":64,"unsigned_A6":360,"finite_cover_descenders":len(desc),"not_descending":len(group-desc),"path_length_two":"PASS"})
