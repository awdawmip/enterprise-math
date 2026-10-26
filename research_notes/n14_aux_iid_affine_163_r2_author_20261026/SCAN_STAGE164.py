#!/usr/bin/env python3
"""Author-only next dual ray from Stage163 endpoint; candidate, not primal theorem."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
N=14
P=(F(1,8),F(1,24),F(5,6))
K=F(163900037061,554150611)
L=F(476600779976,1662451833)
R=(10,0,1);Y=(8,4,1)
ACTS='PQC'
fmt=lambda x: str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def scale(x,z):return tuple(x*v for v in z)
def ev(z,k=K,l=L):return z[0]+k*z[1]+l*z[2]
@lru_cache(None)
def policy_val(s):
    opts=options(s)
    costs=[ev(v) for v in opts]
    winners=[i for i,v in enumerate(costs) if v==min(costs)]
    if s==R:pick=2
    elif s==Y:pick=0
    else:
        assert len(winners)==1,(s,winners)
        pick=winners[0]
    assert pick in winners
    return opts[pick]
def options(s):
    ans=[(F(0),ratio(s),F(0)),(F(0),F(0),F(1))]
    if s[0]<N:
        z=(F(1),F(0),F(0))
        for i in range(3):z=add(z,scale(P[i],policy_val(child(s,i))))
        ans.append(z)
    return ans
rc=options(R)[2]
dK=-F(1); dL=rc[1]/(1-rc[2])*dK
assert dL<0
assert rc[1]*dK+(rc[2]-1)*dL==0
yp=options(Y)[0];yc=options(Y)[2]
derY=(yc[1]-yp[1])*dK+(yc[2]-yp[2])*dL
assert derY>0,('Y should become strict P',fmt(derY))
candidates=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=n,a,b;v=policy_val(s)
   for i,o in enumerate(options(s)):
    g=ev(o)-ev(v)
    d=(o[1]-v[1])*dK+(o[2]-v[2])*dL
    assert g>=0
    if g>0 and d<0:candidates.append((-g/d,s,ACTS[i],g,d))
assert candidates
step=min(x[0] for x in candidates)
K4=K+step*dK;L4=L+step*dL
assert K4>0 and L4>0
first=[a for a in candidates if a[0]==step]
@lru_cache(None)
def bell(s):
    opts=[K4*ratio(s),L4]
    if s[0]<N:opts.append(1+sum(P[i]*bell(child(s,i))[0] for i in range(3)))
    return min(opts),opts
ties={};gaps=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=n,a,b;v,opts=bell(s)
   winners=tuple(ACTS[i] for i,o in enumerate(opts) if o==v)
   if len(winners)>1:ties[str(s)]=winners
   gaps.extend(o-v for o in opts if o>v)
assert str(R) in ties
res={'status':'AUTHOR_DUAL_ONLY_STAGE164','source_stage163':'AUTHOR_EXACT_PRIMAL_STAGE163',
 'ray':{'dK':fmt(dK),'dL':fmt(dL),'Y_continue_minus_P_derivative':fmt(derY)},
 'step':fmt(step),'K164':fmt(K4),'L164':fmt(L4),
 'closures':[{'state':list(s),'action':action,'initial_gap':fmt(g),'gap_derivative':fmt(d)} for _,s,action,g,d in first],
 'ties':{k:list(v) for k,v in ties.items()},'positive_gaps':len(gaps),'min_gap':fmt(min(gaps)),
 'candidate_gap_count':len(candidates),'primal_optimality':'NOT_PROVED'}
for k,v in res.items():print(k,v)
if __name__=='__main__':
 p=Path(__file__).with_name('candidate164.json')
 p.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
 print('PASS Stage164 dual candidate only:',p)
