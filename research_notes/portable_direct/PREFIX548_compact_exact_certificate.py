#!/usr/bin/env python3
"""Exact two-axis BRC/gate observer rank-27 certificate; frozen X6 pin f42f2906d77f24085c123f3ccfe9667d41caa96d."""
from collections import Counter,defaultdict
from itertools import product
S=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*k for k in S[a] if k!=abs(c))
P=tuple((a,p,e*k) for a in range(4) for k in S[a] for e in (-1,1) for p in near(a,e*k))
I={v:i for i,v in enumerate(P)}
def succ(i):
 a,p,c=P[i];b=next(b for b in range(4) if b!=a and abs(c) in S[b]);return tuple(I[x] for x in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
N=tuple(succ(i) for i in range(48));target=I[(0,1,-3)];V=tuple((i,b) for i in range(48) for b in (0,1));A=tuple(product(range(3),(0,1)))
R=((0,0),(1,0),(-1,0),(0,1),(0,-1));prime=1000000007
keep=tuple(i for i in range(28) if i!=14)
def sg(i,ax):
 c=P[i][2];return (1 if c>0 else -1) if abs(c)==ax else 0
def tau(i,j,ax,r):
 x,y=sg(i,ax),sg(j,ax);n=abs(x)+abs(y)-abs(y-r)+abs(x-r);assert n in (0,2);return n//2
def edge(v,a,r):
 i,b=V[v];slot,bit=a;j=N[i][slot];return 2*j+bit,(tau(i,j,1,r[0]),tau(i,j,2,r[1]),int(b==bit==1 and j==target))
def labels():
 F=[{(0,0):1} for _ in V];fp=[[] for _ in V]
 for d in range(6):
  for i in range(96):fp[i].append(tuple(sorted(F[i].items())))
  if d<5:
   new=[]
   for i in range(96):
    row=defaultdict(int)
    for a in A:
     j,(p1,p2,h)=edge(i,a,(0,0))
     for (u,v),n in F[j].items():row[u+p1,v+h]+=n
    new.append(dict(row))
   F=new
 seen={};ids=[seen.setdefault(tuple(x),len(seen)) for x in fp]
 assert len(seen)==28
 return ids
def quotient(ids,r):
 Q={}
 for i in range(96):
  row=Counter()
  for a in A:
   j,deg=edge(i,a,r);row[(ids[j],*deg)]+=1
  c=ids[i]
  if c in Q:assert Q[c]==row
  else:Q[c]=row
 assert len(Q)==28
 return Q
def determinant(Q):
 f=[1]*28;cols=[]
 for d in range(27):
  cols.append(f)
  f=[sum(n*pow(2,u,prime)*pow(5,v,prime)*pow(3,h,prime)*f[j] for (j,u,v,h),n in Q[i].items())%prime for i in range(28)]
 M=[[cols[d][i] for d in range(27)] for i in keep];det=1
 for k in range(27):
  p=next((j for j in range(k,27) if M[j][k]%prime),None);assert p is not None
  if p!=k:M[k],M[p]=M[p],M[k];det=-det
  value=M[k][k]%prime;det=det*value%prime;inv=pow(value,-1,prime)
  for j in range(k+1,27):
   m=M[j][k]*inv%prime
   for l in range(k+1,27):M[j][l]=(M[j][l]-m*M[k][l])%prime
   M[j][k]=0
 return det%prime
def certify():
 ids=labels();dets={}
 for r in R:
  Q=quotient(ids,r);row=Counter()
  for i,c in ((14,1),(3,1),(4,-1),(13,-1)):
   for j,n in Q[i].items():row[j]+=c*n
  assert not {k:v for k,v in row.items() if v}
  det=determinant(Q);assert det!=0;dets[str(r)]=det
 assert dets=={'(0, 0)':537344283,'(1, 0)':244920416,'(-1, 0)':819338349,'(0, 1)':559915505,'(0, -1)':435513067}
 return {'status':'ALL_CHECKS_PASS','classes':28,'two_axis_rank':27,'prime':prime,'evaluation':[2,5,3],'rows':keep,'columns':list(range(27)),'determinants':dets}
if __name__=='__main__':
 import json
 print(json.dumps(certify(),indent=2))
