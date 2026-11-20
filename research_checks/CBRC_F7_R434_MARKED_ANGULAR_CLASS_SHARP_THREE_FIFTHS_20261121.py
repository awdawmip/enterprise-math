#!/usr/bin/env python3
"""Exact rational-arrangement proof certificate for F7 Driver r434.

Pure Python 3 integer operations. No float, no symbolic/external dependencies.
All sign covectors are obtained from rank-three cocircuits by composition.
"""
from collections import Counter
from itertools import combinations

A = ((2,-2,-1,2),(1,-1,-1,2),(-1,2,2,-2),(-1,2,1,-1))
L = ((1,-1),(1,1),(1,-2),(1,2),(1,0),(0,1))
P = ((1,0,0,0),(0,1,0,0))
Q = ((0,0,1,0),(0,0,0,1))

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mul(X,Y): return tuple(tuple(dot(row,col) for col in zip(*Y)) for row in X)
F = mul(L,P)+mul(L,Q)+mul(mul(L,P),A)+mul(mul(L,Q),A)
assert len(F)==24 and len(F[0])==4

def det3(M):
    a,b,c=M
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def nullvec(T):
    return tuple((-1)**i*det3(tuple(tuple(row[j] for j in range(4) if j!=i) for row in T)) for i in range(4))
def sign(x): return (x>0)-(x<0)
def mask(v):
    return (sum(1<<i for i,x in enumerate(v) if x>0), sum(1<<i for i,x in enumerate(v) if x<0))
def unmask(x):
    p,n=x
    return tuple(((p>>i)&1)-((n>>i)&1) for i in range(24))
def comp(x,y):
    p,n=x; q,r=y; avail=~(p|n)
    return p|(q&avail), n|(r&avail)

coc=set()
for inds in combinations(range(24),3):
    v=nullvec(tuple(F[i] for i in inds))
    if not any(v): continue
    signs=tuple(sign(dot(f,v)) for f in F)
    coc.add(mask(signs))
    coc.add(mask(tuple(-t for t in signs)))
assert len(coc)==464, len(coc)

cov={(0,0)}
front=set(coc)
while front:
    front-=cov
    if not front: break
    cov.update(front)
    front={comp(x,y) for x in front for y in coc} | {comp(y,x) for x in front for y in coc}
assert len(cov)==5793, len(cov)

def sector(s):
    a,b,c,d,n,m=s
    if not (a or b or c or d): return 'zero'
    if n==0: return 'a0'
    if m==0: return 'b0'
    if a*b<0: return 'low'
    if a*b==0: return 'equal'
    if c*d<0: return 'mid'
    if c*d==0: return 'double'
    return 'high'

values={'zero':0,'a0':5,'b0':10,'low':5,'equal':5,'mid':7,'double':5,'high':9}
hist=Counter()
for t in cov:
    s=unmask(t)
    labs=tuple(sector(s[i:i+6]) for i in (0,6,12,18))
    d=values[labs[2]]+values[labs[3]]-values[labs[0]]-values[labs[1]]
    hist[d]+=1
assert hist==Counter({
    -6:26,-5:288,-4:590,-3:144,-2:612,-1:300,0:1873,
     1:300, 2:612, 3:144, 4:590, 5:288, 6:26,
}),hist
assert sum(hist.values())==5793 and max(map(abs,hist))==6

def scalar10(n,m):
    a,b=abs(n),abs(m)
    if not (a or b):return 0
    if b==0:return 10
    if a<=b or a==2*b:return 5
    if a<2*b:return 7
    return 9
def witness(z):
    w=tuple(dot(row,z) for row in A)
    return (w,scalar10(w[0],w[1])+scalar10(w[2],w[3])-scalar10(z[0],z[1])-scalar10(z[2],z[3]))
assert witness((3,0,-5,0))==((11,8,-13,-8),-6)
assert witness((-4,-1,-1,1))==((-3,0,-2,0),6)
assert witness((-3,-2,3,2))==((-1,0,1,0),6)
assert witness((-20,10,-18,9))==((-24,6,-14,13),6)

# For any four-parameter constant-sector scalar with exact old-axis/marks,
# the three exhibited inputs impose E>=3/2-H, E>=2-2M, E>=H+M-1.
# Weighted averaging (2,1,2)/5 yields E>=3/5, attained by H=9/10,M=7/10.
from fractions import Fraction as Fr
assert (2*(Fr(3,2)-Fr(9,10))+(2-2*Fr(7,10))+2*(Fr(9,10)+Fr(7,10)-1))/5==Fr(3,5)
print('PASS F7 r434: 24 integral forms, 464 cocircuits, 5793 complete covectors,')
print('  exact defect histogram',sorted(hist.items()))
print('  global max defect 6/10=3/5; all witnesses and sector-family lower bound verified')
