from itertools import product
from math import comb

E={0:[(2,-1,-1),(2,1,-1)],1:[(0,-1,-1),(0,1,-1)],2:[(1,1,1),(2,1,-1)]}
W=['01010101','00001100','01010110','00000100','01101011','10101010','00001010']
S=[(0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)]
def step(st,a):
 q,r,e,k=st; q1,eta,b=E[q][a]
 return (q1,2 if r==2 or (r==1 and a==0) else 1 if a==0 else 0,eta*e,eta*k+b)
def run(w):
 st=(0,0,1,0)
 for x in w:st=step(st,int(x))
 return st
def det(a):
 a=[r[:] for r in a];p=1;n=len(a)
 for i in range(n-1):
  assert a[i][i]!=0
  x=a[i][i]
  for j in range(i+1,n):
   for k in range(i+1,n):
    t=a[j][k]*x-a[j][i]*a[i][k]
    assert t%p==0
    a[j][k]=t//p
  for j in range(i+1,n):a[j][i]=0
  p=x
 return a[-1][-1]
def s(m):return comb(m,m//2) if m%2==0 else 0
assert run('000')==(0,2,1,-1) and run('101')==(0,0,1,-1)
for st,w in zip(S,W):assert run(w)==(*st,1,0)
for n in range(1,18):assert det([[s(i+j) for j in range(n)] for i in range(n)])==2**(n-1)
a=run('01101011');b=run('10101010')
assert {step(a,x)[0:1]+(int(step(a,x)[1]==2),)+step(a,x)[2:] for x in (0,1)} != {step(b,x)[0:1]+(int(step(b,x)[1]==2),)+step(b,x)[2:] for x in (0,1)}
for m in range(14):
 assert sum(sum(w)==0 for w in product((-1,1),repeat=m))==s(m)
print('PASS: exact Hankel determinants n=1..17; source collisions; seven same-effect witnesses; full packets; ±1 raw enumeration m=0..13')
