#!/usr/bin/env python3
"""Stage178 dual continuation ray from Stage177, exact rational and derivative cone audit."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K0=F(1870855299,8461318);L0=F(911522328,4230659)
dK=-F(1);dL=-F(169640,99621)
T=(8,2,0);U=(12,5,2);A=('P','Q','C')
fmt=lambda x:str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return s[0]+1,s[1]+int(i==0),s[2]+int(i==1)
@lru_cache(None)
def pair(s):
 v=[(K0*ell(s),dK*ell(s)),(L0,dL)]
 if s[0]<N:
  cs=[pair(child(s,i)) for i in range(3)]
  v.append((1+sum((P[i]*cs[i][0] for i in range(3)),F(0)),sum((P[i]*cs[i][1] for i in range(3)),F(0))))
 mn=min(x[0] for x in v);w=[a for a,x in zip(A,v) if x[0]==mn]
 md=min(v[A.index(a)][1] for a in w)
 chosen=next(a for a in w if v[A.index(a)][1]==md)
 if s==T:assert v[A.index('P')][1]==v[A.index('C')][1]
 if s==U:assert chosen=='C',(chosen,v)
 return (*v[A.index(chosen)],dict(zip(A,v)),chosen,tuple(w))
roots=[];zero=[];first=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);m,der,opts,chosen,w=pair(s)
   for act,(v,d) in opts.items():
    if act==chosen:continue
    gap=v-m;dg=d-der
    assert gap>=0
    if gap==0:
     assert dg>=0,(s,act,dg)
     zero.append((s,act,dg))
    elif dg<0:roots.append((-gap/dg,s,act,gap,dg))
assert roots
roots.sort();step=roots[0][0];close=[(s,act,gap,dg) for x,s,act,gap,dg in roots if x==step]
K=K0+dK*step;L=L0+dL*step
@lru_cache(None)
def bell(s):
 v=[K*ell(s),L]
 if s[0]<N:v.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
 m=min(v);return m,tuple(a for a,x in zip(A,v) if x==m),v
TIES={};strict=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,w,options=bell(s)
   if len(w)>1:TIES[str(s)]=list(w)
   strict.extend(x-v for x in options if x>v)
print('RAY dK dL',fmt(dK),fmt(dL),'T tangent zero:',[(s,a,fmt(d)) for s,a,d in zero],flush=True)
print('STEP',fmt(step),'K178',fmt(K),'L178',fmt(L),'H178',fmt(bell((0,0,0))[0]),flush=True)
print('CLOSURES',[(s,a,fmt(g),fmt(d))for s,a,g,d in close],flush=True)
print('ties',TIES,'strict_count',len(strict),'min_gap',fmt(min(strict)),'negative_candidates',len(roots),flush=True)
print('NEXT',[(fmt(x),s,a)for x,s,a,*_ in roots[:5]],flush=True)
assert len(strict)==1238 and min(strict)>0
cert={'schema':'EM_N14_STAGE178_DUAL_ONLY_V1','status':'DUAL_ONLY_NOT_PRIMAL_PROVED','parent':'STAGE177_AUTHOR_EXACT','ray':{'K177':fmt(K0),'L177':fmt(L0),'dK':fmt(dK),'dL':fmt(dL),'tangent_at':list(T)},'candidate':{'step':fmt(step),'K178':fmt(K),'L178':fmt(L),'H178':fmt(bell((0,0,0))[0]),'ties':TIES,'strict_gaps':len(strict),'min_gap':fmt(min(strict)),'negative_derivative_candidates':len(roots),'closures':[{'state':list(s),'action':a,'gap':fmt(g),'derivative':fmt(d)}for s,a,g,d in close]}}
Path(__file__).with_name('dual178.json').write_text(json.dumps(cert,indent=2)+'\n')
print('STAGE178_DUAL_SCAN_PASS')
