#!/usr/bin/env python3
"""r435: exact full-Z4 signed-second-coordinate angular F7 certificate."""
from itertools import combinations
from collections import Counter
A=((2,-2,-1,2),(1,-1,-1,2),(-1,2,2,-2),(-1,2,1,-1))
L=((1,-1),(1,1),(1,-2),(1,2),(1,0),(0,1))
P=((1,0,0,0),(0,1,0,0));Q=((0,0,1,0),(0,0,0,1))
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def mul(X,Y):return tuple(tuple(dot(row,col) for col in zip(*Y)) for row in X)
F=mul(L,P)+mul(L,Q)+mul(mul(L,P),A)+mul(mul(L,Q),A)
def det3(M):
 a,b,c=M
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def nullvec(T):return tuple((-1)**i*det3(tuple(tuple(row[j] for j in range(4) if j!=i) for row in T)) for i in range(4))
def sign(x):return (x>0)-(x<0)
def mask(v):return (sum(1<<i for i,x in enumerate(v) if x>0),sum(1<<i for i,x in enumerate(v) if x<0))
def unmask(x):
 p,n=x
 return tuple(((p>>i)&1)-((n>>i)&1) for i in range(24))
def comp(x,y):
 p,n=x;q,r=y;avail=~(p|n)
 return p|(q&avail),n|(r&avail)
def q14(n,m):
 a,b=abs(n),abs(m)
 if a==b==0:return 0
 if b==0:return 14
 if a<=b:return 7
 if a<2*b:return 9 if m>0 else 11
 if a==2*b:return 7 if m>0 else 8
 return 13
def value(s):
 a,b,c,d,n,m=s
 if not any(s):return 0
 if m==0:return 14
 if n==0 or a*b<=0:return 7
 if c*d<0:return 9 if m>0 else 11
 if c*d==0:return 7 if m>0 else 8
 return 13
def defect(z):
 v=tuple(dot(row,z) for row in A)
 return q14(v[0],v[1])+q14(v[2],v[3])-q14(z[0],z[1])-q14(z[2],z[3])
assert len(F)==24
coc=set()
for inds in combinations(range(24),3):
 v=nullvec(tuple(F[i] for i in inds))
 if not any(v):continue
 s=tuple(sign(dot(f,v)) for f in F)
 coc.add(mask(s));coc.add(mask(tuple(-t for t in s)))
assert len(coc)==464
cov={(0,0)};front=set(coc)
while front:
 front-=cov
 if not front:break
 cov.update(front)
 front={comp(x,y) for x in front for y in coc}|{comp(y,x) for x in front for y in coc}
assert len(cov)==5793
hist=Counter()
for v in cov:
 s=unmask(v)
 d=value(s[12:18])+value(s[18:24])-value(s[:6])-value(s[6:12])
 hist[d]+=1
assert sum(hist.values())==5793
assert max(abs(d) for d in hist)==8
expected={-8:34,-7:248,-6:526,-5:150,-4:270,-3:148,-2:336,-1:398,0:1573,
          1:398,2:336,3:148,4:270,5:150,6:526,7:248,8:34}
assert dict(hist)==expected
witnesses=(((-46,17,-36,24),-1,1),((1,-1,4,1),1,1),
           ((-3,-2,3,2),1,1),((0,0,-1,1),1,2),
           ((46,-17,36,-24),-1,1),((-5,-1,-2,1),1,1))
for z,sg,weight in witnesses:assert sg*defect(z)==8
assert q14(2,1)==q14(-1,-1)==7
print("cocircuits:",len(coc),"covectors:",len(cov))
print("exact 14D histogram:",dict(sorted(hist.items())))
print("supremum |D| = 8/14 = 4/7; six-witness minimax certificate verified")
