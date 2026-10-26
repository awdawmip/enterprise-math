"""Portable exact C4-BRC path-pair checker (not the original Stage50 import)."""
from fractions import Fraction as Q
from itertools import product, combinations
from collections import defaultdict
R=(1,0,-1,0)
V=((1,0),(0,1),(-1,0),(0,-1))
def packet(a):
    return {j:(Q(abs(x)),0 if x>0 else 2) for j,x in enumerate(a) if x}
def mass(f):
    return sum((w*w for w,p in f.values()),Q(0))
def corr(f,r):
    re=im=Q(0)
    for j,(w,p) in f.items():
        if j+r in f:
            v,q=f[j+r]; x,y=V[(p-q)%4]; re+=w*v*x; im+=w*v*y
    return re,im
def external_direct(f,r,p):
    total=Q(0)
    for j in set(f)|{k+r for k in f}:
        paths=[]
        if j in f: paths.append(f[j])
        if j-r in f:
            w,q=f[j-r]; paths.append((w,(q+p+2)%4))
        for w,q in paths:
            for v,t in paths: total+=w*v*R[(t-q)%4]
    return Q(10,36)*total/(2*mass(f))
def external_formula(f,r,p):
    re,im=corr(f,r)
    return Q(5,18)*(1-(re,-im,-re,im)[p]/mass(f))
f=packet((1,4,4));g=packet((2,5,2))
assert mass(f)==mass(g)==33
assert [corr(f,r) for r in range(3)]==[corr(g,r) for r in range(3)]==[(33,0),(20,0),(4,0)]
checks=0
for h in (f,g):
    for r in range(5):
        for p in range(4):
            assert external_direct(h,r,p)==external_formula(h,r,p)
            checks+=1
for phases in product(range(4),repeat=3):
    h={j:(Q(j+1),phases[j]) for j in range(3)}
    for r in range(5):
        for p in range(4):
            assert external_direct(h,r,p)==external_formula(h,r,p)
            checks+=1
assert checks==1320
assert all(external_direct(f,r,p)==external_direct(g,r,p) for r in range(5) for p in range(4))
uf=packet((-1,4,4));ug=packet((-2,5,2))
assert corr(uf,1)==(12,0) and corr(ug,1)==(0,0)
assert (external_direct(uf,1,0),external_direct(ug,1,0))==(Q(35,198),Q(5,18))
def distinct(M):
    d=defaultdict(list)
    for a in product(range(1,M+1),repeat=3):
        h=packet(a)
        d[(mass(h),corr(h,1),corr(h,2))].append(a)
    return [(a,b) for group in d.values() for a,b in combinations(group,2) if a!=b[::-1]]
assert not distinct(4)
assert ((1,4,4),(2,5,2)) in distinct(5)
print('PREFIX279_PORTABLE_BRC_PAIR_PASS',checks,'exact C4 ordered-pair checks; gate delta=10/99; first nontrivial integer M=5')
