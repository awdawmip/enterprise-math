#!/usr/bin/env python3
"""Exact PREFIX547: requires adjacent published PREFIX545 and PREFIX546 certificates.
Scientific pin: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import Counter,defaultdict
import json
import PREFIX545_compact_exact_certificate as b
import PREFIX546_shared_gauge_certificate as g

FREE=(14,24,25,26,27)
KEEP=tuple(i for i in range(28) if i not in FREE)
R=({14:1,3:1,4:-1,13:-1},
   {24:1,6:1,10:-1,18:1,19:-1,22:-1},
   {25:1,8:1,12:-1,20:1,21:-1,23:-1},
   {26:1,12:1,17:-1,20:-1},
   {27:1,6:1,16:-1,22:-1})
A=((0,0,0,0,0),(0,0,2,0,0),(0,2,0,0,0),
   (0,0,0,0,-2),(0,0,0,-2,0))
PIV={x:i for i,x in enumerate(KEEP)}
E=[({PIV[i]:1} if i in PIV else
    {PIV[j]:-v for j,v in R[FREE.index(i)].items() if j!=i})
   for i in range(28)]

def validate(Q,signs):
 assert all(sum(x.values())==0 for x in R)
 assert all(len({signs[j] for j in x})==1 for x in R)
 for i,x in enumerate(R):
  for j in range(28):
   a=Counter()
   for k,v in x.items():
    for (dest,p,h),n in Q[k].items():
     if dest==j:a[p,h]+=v*n
   want=Counter({(0,0):sum(A[i][k]*R[k].get(j,0) for k in range(5))})
   assert +a==+want and +(-a)==+(-want)

def transfer(Q):
 out=[]
 for i in KEEP:
  row=Counter()
  for (dest,p,h),n in Q[i].items():
   for j,coeff in E[dest].items():row[j,p,h]+=n*coeff
  out.append({k:v for k,v in row.items() if v})
 assert sum(map(len,out))==75
 return out

def step(T,F):
 out=[]
 for row in T:
  h=defaultdict(int)
  for (j,p,z),v in row.items():
   for (u,w),n in F[j].items():h[u+p,w+z]+=v*n
  out.append({k:v for k,v in h.items() if v})
 return out

def reconstruct(i,F):
 out=defaultdict(int)
 for j,v in E[i].items():
  for k,n in F[j].items():out[k]+=v*n
 return {k:v for k,v in out.items() if v}

def minor(Q):
 prime=1000000007;q=2;z=3
 cols=[];vec=[1]*28
 for d in range(23):
  cols.append(vec)
  vec=[sum(n*pow(q,p,prime)*pow(z,h,prime)*vec[j]
           for (j,p,h),n in Q[i].items())%prime for i in range(28)]
 M=[[cols[d][i] for d in range(23)] for i in KEEP]
 det=1
 for k in range(23):
  pivot=next(i for i in range(k,23) if M[i][k]%prime)
  if pivot!=k:M[k],M[pivot]=M[pivot],M[k];det=-det
  v=M[k][k]%prime;det=det*v%prime;inv=pow(v,-1,prime)
  for i in range(k+1,23):
   t=M[i][k]*inv%prime
   for j in range(k+1,23):M[i][j]=(M[i][j]-t*M[k][j])%prime
   M[i][k]=0
 return det%prime

def run(D=24):
 ids,Q,signs=g.shared()
 assert len(set(ids))==28
 total=0;native=0;det={};terms={}
 for r in (-1,0,1):
  validate(Q[r],signs);T=transfer(Q[r]);det[str(r)]=minor(Q[r]);assert det[str(r)]
  terms[str(r)]={'monomials':sum(map(len,T)),
                 'negative':sum(v<0 for row in T for v in row.values())}
  old=[{(0,0):1} for _ in range(28)];new=[{(0,0):1} for _ in range(23)]
  for d in range(D+1):
   for port in range(96):
    assert old[ids[port]]==reconstruct(ids[port],new);total+=1
   if d<D:old=b.qstep(Q[r],old);new=step(T,new)
 for s in range(48):
  r=b.sign(s);v=[{(0,0):1} for _ in range(23)]
  reference=b.native(s,0,10)
  for d in range(11):
   assert reconstruct(ids[2*s],v)==reference[d];native+=1
   if d<10:v=step(transfer(Q[r]),v)
 assert total==3*96*(D+1)
 return {'status':'ALL_CHECKS_PASS','dimension':23,'relations':5,
         'relation_coefficient_checks':3*5*28,'polynomial_checks':total,
         'independent_native_checks':native,'exact_depth':[0,D],
         'minor':{'prime':1000000007,'q':2,'z':3,'rows':KEEP,'d':[0,22],
                  'determinants':det},'transfers':terms}

if __name__=='__main__':
 import sys
 print(json.dumps(run(int(sys.argv[1]) if len(sys.argv)>1 else 24),indent=2,sort_keys=True))
