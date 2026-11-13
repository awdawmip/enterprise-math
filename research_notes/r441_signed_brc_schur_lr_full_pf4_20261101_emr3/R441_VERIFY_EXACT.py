#!/usr/bin/env python3
from itertools import combinations,permutations
from math import comb,gcd,prod
from functools import reduce
def B(n,k):return comb(n,k) if 0<=k<=n else 0
def H(r,s):return B(r+s,2*s)*sum(B(r-s,q)*(B(2*s,r-2*q)-B(2*s,r-2*q-1)) for q in range(r-s+1))
def det(mat):
 n=len(mat);a=[x[:] for x in mat];p=1;sg=1
 for k in range(n-1):
  if a[k][k]==0:
   for q in range(k+1,n):
    if a[q][k]:a[k],a[q]=a[q],a[k];sg=-sg;break
   else:return 0
  q=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    x=a[i][j]*q-a[i][k]*a[k][j]
    assert x%p==0
    a[i][j]=x//p
   a[i][k]=0
  p=q
 return sg*a[-1][-1]
for r,maxk in [(5,4),(7,5),(9,6),(11,6),(13,6),(15,6),(27,4),(29,4)]:
 raw=[H(r,r-i) for i in range(r-1)];g=reduce(gcd,raw);a=[v//g for v in raw];n=r-2
 for k in range(1,maxk+1):
  pos=neg=zero=0;first=None
  for jj in combinations(range(n+k),k):
   mat=[[a[j-i] if 0<=j-i<len(a) else 0 for j in jj] for i in range(k)]
   d=det(mat)
   if d>0:pos+=1
   elif d<0:
    neg+=1
    if first is None:first=(jj,d)
   else:zero+=1
  assert pos+neg+zero==comb(n+k,k)
  if first:
   jj,d=first;mat=[[a[j-i] if 0<=j-i<len(a) else 0 for j in jj] for i in range(k)]
   z=sum((-1)**sum(p[i]>p[j] for i in range(k) for j in range(i+1,k))*prod(mat[i][p[i]] for i in range(k)) for p in permutations(range(k)))
   assert z==d
  print("EXACT",r,k,pos,zero,neg,"first",first)
print("R441_INTEGER_EXACT_PASS")
