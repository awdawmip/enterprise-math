#!/usr/bin/env python3
"""Exact integer oriented-matroid certificate for CBRC F7 r433."""
from collections import Counter
from itertools import combinations

A = ((2,-2,-1,2),(1,-1,-1,2),(-1,2,2,-2),(-1,2,1,-1))
L = ((1,-1),(1,1),(1,-2),(1,2))
P = ((1,0,0,0),(0,1,0,0))
Q = ((0,0,1,0),(0,0,0,1))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def matmul(M,N): return tuple(tuple(dot(row,col) for col in zip(*N)) for row in M)
F = matmul(L,P)+matmul(L,Q)+matmul(matmul(L,P),A)+matmul(matmul(L,Q),A)

def det3(M):
    (a,b,c)=M
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def nullvec(T):
    return tuple((-1)**i*det3(tuple(tuple(row[j] for j in range(4) if j!=i) for row in T)) for i in range(4))

def sign(x): return (x>0)-(x<0)

def compose(x,y): return tuple(a if a else b for a,b in zip(x,y))

coc=set()
for inds in combinations(range(16),3):
    v=nullvec(tuple(F[i] for i in inds))
    if not any(v): continue
    s=tuple(sign(dot(row,v)) for row in F)
    coc.add(s)
    coc.add(tuple(-x for x in s))
assert len(coc)==84, len(coc)

cov={(0,)*16}
frontier=set(coc)
while frontier:
    frontier-=cov
    if not frontier: break
    cov.update(frontier)
    frontier={compose(x,y) for x in frontier for y in coc}|{compose(y,x) for x in frontier for y in coc}
assert len(cov)==1225, len(cov)

def qaff(signs):
    """q_alpha = k*alpha + h/2, both coefficients integers."""
    a,b,c,d=signs
    if not any(signs): return (0,0)
    if a*b<=0 or c*d==0: return (0,1)
    if c*d<0: return (1,0)
    return (0,2)

def defect_aff(s):
    vals=[qaff(s[i:i+4]) for i in (0,4,8,12)]
    return tuple(vals[2][i]+vals[3][i]-vals[0][i]-vals[1][i] for i in range(2))

counts=Counter(defect_aff(s) for s in cov)
expected={
    (-2,2):26,(-2,3):20,(-2,4):2,
    (-1,0):4,(-1,1):152,(-1,2):76,
    (0,-1):120,(0,0):425,(0,1):120,
    (1,-2):76,(1,-1):152,(1,0):4,
    (2,-4):2,(2,-3):20,(2,-2):26,
}
assert counts==expected,(counts,expected)
# At alpha=2/3 exact defect is max |k*(2/3)+h/2| = 2/3.
assert max(abs(4*k+3*h) for (k,h) in counts)==4
print('PASS: 16 integer forms; 84 oriented cocircuits; 1225 covectors; 15 exact affine defect classes; alpha=2/3 yields maximum 2/3')
for (k,h),count in sorted(counts.items()):
    print(f'{k:+d}*alpha{h:+d}/2  count={count}')
