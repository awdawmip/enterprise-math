#!/usr/bin/env python3
"""PREFIX-675: exact global p=0 BRC edge sign + concavity certificate."""
from fractions import Fraction as F
from math import comb,factorial
from collections import defaultdict
from functools import lru_cache
import json
N,DEN,S=189,2**18,2**216
L,R=F(607,4096),F(609,4096)
@lru_cache(None)
def accept(n,k,a):
 return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n

@lru_cache(None)
def survive(n,k):
 if k>n//2:return survive(n,n-k)
 m=k*DEN//n
 assert accept(n,k,m)
 if k==0:lo1=hi1=0
 else:
  a,b=0,m
  while b-a>1:
   x=(a+b)//2
   if accept(n,k,x):b=x
   else:a=x
  lo1,hi1=a,b
 a,b=m,DEN
 while b-a>1:
  x=(a+b)//2
  if accept(n,k,x):a=x
  else:b=x
 if 4*(a-hi1)>DEN:return True
 if 4*(b-lo1)<DEN:return False
 raise ValueError(('ambiguous predicate',n,k))

def rows():
 s={0:1};out=[s.copy()]
 for n in range(1,N+1):
  t=defaultdict(int)
  for k,v in s.items():t[k]+=v;t[k+1]+=v
  s={k:v for k,v in t.items() if survive(n,k)}
  out.append(s.copy())
 assert not out[-1] and len(out)==190
 assert sum(map(len,out))==9529
 assert all(sum(out[n].values())==2**n for n in range(25))
 assert sum(out[25].values())==2**25-2
 assert all(out[n].get(k,0)==out[n].get(n-k,0) for n in range(N) for k in range(n+1))
 return out

def moment_poly(rr):
 M=[0]*N;K=[0]*N
 for m,row in enumerate(rr[:N]):
  a,b=F(1),F(m+1)
  for n in range(25):
   w=F(comb(n+m,n),2**(n+m+1))
   a-=w;b-=F(n+m+1,2)*w
  assert (a*S).denominator==(b*S).denominator==1
  A,B=int(a*S),int(b*S)
  for j,v in row.items():
   for k in range(j,m+1):
    t=v*(-1)**(k-j)*comb(m-j,k-j)
    M[k]+=A*t;K[k]+=B*t
 M[0]+=25*S;K[0]+=325*S
 return M,K

def derivative_poly(M,K,q):
 P=[0]*(len(M)*2-1)
 for i,x in enumerate(M):
  if x:
   for j,y in enumerate(M):
    if y:P[i+j]-=q*q*x*y
 for i in range(len(M)):P[i]+=2*q*q*S*K[i]-q*S*M[i]
 while P[-1]==0:P.pop()
 return [(i+1)*P[i+1] for i in range(len(P)-1)]

def quotient(d):
 out=[d[0]]
 for i in range(1,len(d)-1):out.append(d[i]+2*out[-1])
 assert d[-1]==-2*out[-1]
 return out

def bern(c):
 # d! times each Bernstein ordinate of a degree-d power polynomial.
 d=len(c)-1;fac=[factorial(i) for i in range(d+1)];out=[]
 for j in range(d+1):
  s=0;f=1
  for k in range(j+1):
   if k:f*=j-k+1
   if c[k]:s+=c[k]*f*fac[d-k]
  out.append(s)
 return out

def split(b):
 d=len(b)-1;curr=b[:]
 lo=[b[0]<<d];hi=[0]*(d+1);hi[d]=b[-1]<<d
 for r in range(1,d+1):
  curr=[curr[i]+curr[i+1] for i in range(len(curr)-1)]
  lo.append(curr[0]<<(d-r));hi[d-r]=curr[-1]<<(d-r)
 return lo,hi

def restrict(b,n,bits):
 for i in range(bits-1,-1,-1):
  lo,hi=split(b);b=hi if (n>>i)&1 else lo
 return b

def at(c,n,d):
 D=len(c)-1
 x=sum(v*n**i*d**(D-i) for i,v in enumerate(c) if v)
 return (x>0)-(x<0)

def edge_boxes(b):
 stack=[(F(0),F(1),b,0)];found=[];skipped=[]
 while stack:
  l,r,v,k=stack.pop()
  if l>=F(1,2):continue
  if L<=l and r<=R:skipped.append((l,r));continue
  sign=1 if r<=L else (-1 if l>=R else 0)
  if sign==1 and min(v)>0:found.append((l,r,'+'));continue
  if sign==-1 and max(v)<0:found.append((l,r,'-'));continue
  assert k<12,('uncertified cell',l,r)
  a,c=split(v);m=(l+r)/2
  stack.extend([(m,r,c,k+1),(l,m,a,k+1)])
 all_cells=sorted([(l,r) for l,r,_ in found]+skipped)
 assert all_cells[0][0]==0 and all_cells[-1][1]==F(1,2)
 assert all(all_cells[i][1]==all_cells[i+1][0] for i in range(len(all_cells)-1))
 assert sum((r-l for l,r in skipped),F(0))==R-L
 assert len(found)==15 and sum(s=='+' for _,_,s in found)==7
 assert sum(s=='-' for _,_,s in found)==8
 return found,skipped

def run():
 M,K=moment_poly(rows());outs={}
 for q in (12,24):
  d=derivative_poly(M,K,q);b=bern(quotient(d))
  found,skipped=edge_boxes(b)
  assert at(d,607,4096)==1 and at(d,609,4096)==-1
  assert at(d,1,2)==0
  dd=[(i+1)*d[i+1] for i in range(len(d)-1)];cb=bern(dd)
  assert max(restrict(cb,607,12))<0
  assert max(restrict(cb,608,12))<0
  assert at(quotient(d),0,1)>0 and at(quotient(d),1,2)<0
  outs[str(q)]={'degree_dV':len(d)-1,'degree_quotient':len(d)-2,
     'strict_sign_boxes':[(str(l),str(r),s) for l,r,s in found],
     'central_skipped_boxes':[(str(l),str(r)) for l,r in skipped],
     'strict_negative_curvature_boxes':[['607/4096','608/4096'],['608/4096','609/4096']]}
 print('ALL_CHECKS_PASS 12; strict Bernstein sign boxes=30; curvature boxes=4')
 print(json.dumps(outs,ensure_ascii=False,indent=2))
if __name__=='__main__':run()
