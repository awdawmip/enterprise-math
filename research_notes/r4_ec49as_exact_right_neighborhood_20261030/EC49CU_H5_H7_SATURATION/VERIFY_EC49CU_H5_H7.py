#!/usr/bin/env python3
"""Literal native signed-X6 positive-BRC minors plus exact-Q formal upper.
Usage: python3 VERIFY_EC49CU_H5_H7.py LITERAL_H5.json LITERAL_H6.json LITERAL_H7.json
No third-party dependencies; performs no probabilistic inference.
"""
import sys,json
from fractions import Fraction
from itertools import product
from collections import defaultdict
P=1000003
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3)}
W=((2,3,3,2,1,1),(3,2,3,2,1,1))
def suffix(word):return sum((list(OPS[x]) for x in word),[])
def endpoint(path):
 z=[0]*6
 for s in path:
  assert type(s) is int and 1<=abs(s)<=6
  z[abs(s)-1]+=1 if s>0 else -1
 return tuple(z)
def tag(path):
 a=b=False
 for x,y in zip(path,path[1:]):
  if x==1 and y==2:a=True
  if x==2 and y==1:b=True
 return 2*int(a)+int(b)
def weight(path,j):
 if j==2:return 1
 z=1
 for s in path:
  if s>0:z*=W[j][s-1]
 return z
def det_mod(M):
 n=len(M);assert n and all(len(row)==n for row in M)
 A=[[x%P for x in row] for row in M];ans=1
 for j in range(n):
  p=next((i for i in range(j,n) if A[i][j]),None)
  if p is None:return 0
  if p!=j:A[p],A[j]=A[j],A[p];ans=(-ans)%P
  v=A[j][j];ans=ans*v%P;inv=pow(v,-1,P)
  for i in range(j+1,n):
   if A[i][j]:
    c=A[i][j]*inv%P
    for k in range(j,n):A[i][k]=(A[i][k]-c*A[j][k])%P
 return ans
def qstep(q,s):
 a,b=divmod(q,3)
 a=2 if a==2 or (a==1 and s==2) else int(s==1)
 b=2 if b==2 or (b==1 and s==1) else int(s==2)
 return 3*a+b
def addQ(row,basis):
 v=[Fraction(x) for x in row]
 for j,w in sorted(basis.items()):
  if v[j]:
   f=v[j];v=[x-f*y for x,y in zip(v,w)]
 k=next((i for i,x in enumerate(v) if x),None)
 if k is None:return
 v=[x/v[k] for x in v]
 for j,w in list(basis.items()):
  if w[k]:
   f=w[k];basis[j]=[x-f*y for x,y in zip(w,v)]
 basis[k]=v
def formal(h):
 bases=defaultdict(dict)
 for k in range(1,h+1):
  for ops in product('abcde',repeat=k):
   tail=suffix(ops);end=endpoint(tail);t=tuple(-x for x in end)
   labels=[]
   for q in range(9):
    for s in tail:q=qstep(q,s)
    a,b=divmod(q,3);labels.append(2*int(a==2)+int(b==2))
   for j in range(4):addQ((int(q==j) for q in labels),bases[t])
 return {k:len(v) for k,v in bases.items()}
def verify(filename):
 raw=open(filename,'r',encoding='utf-8').read();src=json.loads(raw)
 h=src['h'];n=src['N'];assert h in (5,6,7) and n==2*h+8
 assert src['modulus']==P and len(src['fibers'])==(h+1)**2
 expect=18*h*h+24*h+12;f=formal(h)
 assert len(f)==(h+1)**2 and 3*sum(f.values())==expect
 seen=set();total=0;summary=[]
 for fiber in src['fibers']:
  end=tuple(fiber['endpoint']);assert end not in seen and end in f
  seen.add(end);paths=fiber['paths'];rows=fiber['rows'];d=len(rows)
  assert d==f[end] and len(paths)==3*d==fiber['rank']==fiber['target']
  for p in paths:assert len(p)==n and endpoint(p)==end
  M=[]
  for j in range(3):
   for word,label in rows:
    assert 1<=len(word)<=h and all(x in OPS for x in word) and label in range(4)
    tail=suffix(word);assert tuple(a+b for a,b in zip(end,endpoint(tail)))==(0,)*6
    M.append([weight(p+tail,j) if tag(p+tail)==label else 0 for p in paths])
  residue=det_mod(M)
  assert residue!=0,(h,end)
  total+=3*d;summary.append((end,3*d,residue))
 assert seen==set(f) and total==expect
 print('PASS h=',h,'n=',n,'genuine_rank=',total,'exact_h=',3*(11*h*h+15*h+8)//2,'nonzero_fibers=',len(summary))
 print('mod residues:',summary)
if __name__=='__main__':
 assert len(sys.argv)>=2
 for filename in sys.argv[1:]:verify(filename)
