#!/usr/bin/env python3
"""Stage163 exact author dual-ray scan, NOT a primal interval proof."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
N=14;P=(F(1,8),F(1,24),F(5,6))
K=F(1776538556208,5886215131);L=F(5152927839848,17658645393)
R=(10,0,1);X=(7,3,3);ACTS='PQC'
fmt=lambda z:str(z.numerator)+('/'+str(z.denominator) if z.denominator!=1 else '')
def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
def add(a,b):return tuple(a[i]+b[i] for i in range(3))
def mul(c,a):return tuple(c*z for z in a)
def value(a,k=K,l=L):return a[0]+k*a[1]+l*a[2]
@lru_cache(None)
def vec(s):
 opts=options(s);vs=[value(v) for v in opts];mi=min(vs)
 winners=[i for i,o in enumerate(vs) if o==mi]
 chosen=2 if s==R else 1 if s==X else winners[0]
 if s not in (R,X):assert len(winners)==1
 assert chosen in winners
 return opts[chosen]
def options(s):
 out=[(F(0),ratio(s),F(0)),(F(0),F(0),F(1))]
 if s[0]<N:
  v=(F(1),F(0),F(0))
  for i in range(3):v=add(v,mul(P[i],vec(child(s,i))))
  out.append(v)
 return out
rc=options(R)[2]
dK=-F(1);dL=rc[1]/(1-rc[2])*dK
assert dL==F(-10592,12501)
xcont=options(X)[2];xq=options(X)[1]
dX=(xcont[1]-xq[1])*dK+(xcont[2]-xq[2])*dL
assert dX>0
candidates=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=n,a,b;v=vec(s)
   for i,o in enumerate(options(s)):
    gap=value(o)-value(v)
    der=(o[1]-v[1])*dK+(o[2]-v[2])*dL
    assert gap>=0
    if gap>0 and der<0:candidates.append((-gap/der,s,ACTS[i],gap,der))
step=min(z[0] for z in candidates)
new=[z for z in candidates if z[0]==step]
K3=K+step*dK;L3=L+step*dL
@lru_cache(None)
def bell(s):
 opts=[K3*ratio(s),L3]
 if s[0]<N:opts.append(1+sum(P[i]*bell(child(s,i))[0] for i in range(3)))
 return min(opts),opts
ties={};gaps=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=n,a,b;v,opts=bell(s)
   names=[ACTS[i] for i,o in enumerate(opts) if o==v]
   if len(names)>1:ties[str(s)]=names
   gaps.extend(o-v for o in opts if o>v)
assert step==F(19719048267802073097,3261849711321095041)
assert K3==F(163900037061,554150611)
assert L3==F(476600779976,1662451833)
assert new[0][1:3]==((8,4,1),'P') and len(new)==1
assert ties=={'(8, 4, 1)':['P','C'],'(10, 0, 1)':['Q','C']}
assert len(gaps)==1238 and min(gaps)==F(1577397669610597,79424873185738752)
result={'status':'AUTHOR_DUAL_ONLY','base':{'K':fmt(K),'L':fmt(L)},
'direction':{'dK':fmt(dK),'dL':fmt(dL),'X_continue_minus_Q_derivative':fmt(dX)},
'step':fmt(step),'K163':fmt(K3),'L163':fmt(L3),
'closures':[{'state':list(s),'action':a,'gap0':fmt(g),'gap_derivative':fmt(d)} for _,s,a,g,d in new],
'ties':ties,'positive_gaps':len(gaps),'min_gap':fmt(min(gaps)),
'candidate_gap_count':len(candidates),'primal_optimality':'NOT_PROVED'}
if __name__=='__main__':
 Path(__file__).with_name('candidate163.json').write_text(json.dumps(result,indent=2)+'\n')
 print('STAGE163 DUAL-ONLY PASS:',result)
