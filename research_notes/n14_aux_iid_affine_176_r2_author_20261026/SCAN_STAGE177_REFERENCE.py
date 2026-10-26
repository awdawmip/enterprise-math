#!/usr/bin/env python3
"""Exact Stage177 first-gap ray scan, dual-only. No Stage177 primal theorem."""
from fractions import Fraction as F
from functools import lru_cache
N=14
P=(F(1,8),F(1,24),F(5,6))
K0=F(1696807920718753587,7487608294325270)
L0=F(168348947995801752,748760829432527)
dK=-F(1);dL=-F(169640,99621)
W=(4,1,2);T=(8,2,0);A=('P','Q','C')
def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return s[0]+1,s[1]+int(i==0),s[2]+int(i==1)
@lru_cache(None)
def pair(s):
 v=[(K0*ell(s),dK*ell(s)),(L0,dL)]
 if s[0]<N:
  cs=[pair(child(s,i)) for i in range(3)]
  v.append((1+sum((P[i]*cs[i][0] for i in range(3)),F(0)),sum((P[i]*cs[i][1] for i in range(3)),F(0))))
 mn=min(x[0] for x in v);w=[a for a,x in zip(A,v) if x[0]==mn]
 selected='P' if s==T else 'Q' if s==W else w[0]
 assert selected in w
 assert v[A.index(selected)][1]==min(v[A.index(a)][1] for a in w)
 return (*v[A.index(selected)],dict(zip(A,v)),selected)
roots=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);m,der,opts,chosen=pair(s)
   for act,(v,d) in opts.items():
    if act==chosen:continue
    gap=v-m;dg=d-der
    assert gap>=0
    if gap==0:assert dg>=0
    elif dg<0:roots.append((-gap/dg,s,act))
roots.sort();step=roots[0][0]
K=K0+dK*step;L=L0+dL*step
@lru_cache(None)
def bell(s):
 v=[K*ell(s),L]
 if s[0]<N:v.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
 m=min(v)
 return m,tuple(a for a,x in zip(A,v) if x==m),v
ties={};strict=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,w,options=bell(s)
   if len(w)>1:ties[s]=w
   strict.extend(x-v for x in options if x>v)
assert len(ties)==2 and len(strict)==1238
assert ties=={T:('P','C'),(12,5,2):('P','C')}
assert len(roots)==758
assert step==F(87249936961344913535484,15838758709430926226465)
assert K==F(1870855299,8461318)
assert L==F(911522328,4230659)
assert bell((0,0,0))[0]==F(148336146012983121522325,905303534551638736896)
assert min(strict)==F(2003135,203071632)
print('STAGE177_DUAL_SCAN_REFERENCE_PASS')
