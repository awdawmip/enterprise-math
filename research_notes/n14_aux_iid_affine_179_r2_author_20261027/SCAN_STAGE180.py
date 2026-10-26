#!/usr/bin/env python3
"""Exact next tangent-ray scan from Stage180: hold S=Q/C tie, choose U=P."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K0=F(194705694,884339);L0=F(189622936,884339)
U=(12,5,2);S=(9,0,1);A=('P','Q','C')
fmt=lambda x:str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return s[0]+1,s[1]+int(i==0),s[2]+int(i==1)
@lru_cache(None)
def gradients(s):
 opts=[(K0*ell(s), (ell(s),F(0))),(L0,(F(0),F(1)))]
 if s[0]<N:
  z=[gradients(child(s,i)) for i in range(3)]
  opts.append((1+sum((P[i]*z[i][0] for i in range(3)),F(0)),tuple(sum((P[i]*z[i][1][j] for i in range(3)),F(0)) for j in (0,1))))
 best=min(x[0] for x in opts)
 winners=[a for a,o in zip(A,opts) if o[0]==best]
 assert (s not in (U,S)) or (winners==(['P','C'] if s==U else ['Q','C'])),(s,winners)
 if s==U:chosen='P'
 elif s==S:chosen='Q'
 else:chosen=next(a for a,o in zip(A,opts) if o[0]==best)
 return (*opts[A.index(chosen)],dict(zip(A,opts)),chosen,winners)
state=gradients(S)
gq=state[2]['Q'][1];gc=state[2]['C'][1]
dg=tuple(gc[j]-gq[j] for j in (0,1))
assert dg[1]!=0
dK=-F(1);dL=-dg[0]*dK/dg[1]
assert dL<0
print('S tie gradient C-Q:',list(map(fmt,dg)),'ray',fmt(dK),fmt(dL))
# For every Bellman state, validate best derivative policy and all root closures.
roots=[];zero=[];strict_before=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,grad,opts,chosen,winners=gradients(s)
   derivative=lambda g: dK*g[0]+dL*g[1]
   d=derivative(grad)
   for act,(val,g) in opts.items():
    if act==chosen:continue
    gap=val-v;dgap=derivative(g)-d
    assert gap>=0
    if not gap:
     zero.append((s,act,dgap))
     assert dgap>=0,(s,act,dgap)
    else:
     strict_before.append(gap)
     if dgap<0:roots.append((-gap/dgap,s,act,gap,dgap))
assert roots
roots.sort();step=roots[0][0]
K=K0+dK*step;L=L0+dL*step
assert K>0 and L>0
@lru_cache(None)
def bell(s):
 vals=[K*ell(s),L]
 if s[0]<N:vals.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
 m=min(vals);return m,tuple(a for a,val in zip(A,vals) if val==m),vals
strict=[];ties={}
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,w,opts=bell(s)
   if len(w)>1:ties[str(s)]=list(w)
   strict.extend(x-v for x in opts if x>v)
closures=[(s,a,g,d) for r,s,a,g,d in roots if r==step]
print('ZERO',[(str(s),a,fmt(d)) for s,a,d in zero]);print('STEP',fmt(step),'K180',fmt(K),'L180',fmt(L),'H',fmt(bell((0,0,0))[0]))
print('CLOSURES',[(str(s),a,fmt(g),fmt(d)) for s,a,g,d in closures]);print('TIES',ties,'STRICT',len(strict),'MIN',fmt(min(strict)),'ROOTS',len(roots))
print('NEXT',[(fmt(r),str(s),a) for r,s,a,_,_ in roots[:5]])
assert len(strict)>0 and min(strict)>0
cert={'schema':'EM_N14_STAGE180_DUAL_SCAN_V1','status':'DUAL_ONLY_NOT_PRIMAL_PROVED','parent':'STAGE179_AUTHOR_EXACT','ray':{'K179':fmt(K0),'L179':fmt(L0),'dK':fmt(dK),'dL':fmt(dL),'tangent_at':list(S)},'candidate':{'step':fmt(step),'K180':fmt(K),'L180':fmt(L),'H180':fmt(bell((0,0,0))[0]),'ties':ties,'strict_gaps':len(strict),'min_gap':fmt(min(strict)),'roots':len(roots),'closures':[{'state':list(s),'action':a,'gap':fmt(g),'derivative':fmt(d)}for s,a,g,d in closures]}}
Path(__file__).with_name('dual180.json').write_text(json.dumps(cert,indent=2)+'\n')
print('STAGE180_DUAL_SCAN_PASS')
