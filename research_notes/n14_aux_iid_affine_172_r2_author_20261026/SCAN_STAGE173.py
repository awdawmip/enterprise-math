#!/usr/bin/env python3
"""Exact first closure scan from Stage172 along the R-tie dual ray.
Pure dual candidate; does not assert Stage173 primal feasibility.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
N=14
P=(F(1,8),F(1,24),F(5,6))
K0=F(2453276570264541,10128738563455)
L0=F(7332367848199016,30386215690365)
dK=F(-1);dL=F(-10592,12501)
R=(10,0,1);Y=(5,4,1)
A=('P','Q','C')
fmt=lambda x:str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return(s[0]+1,s[1]+(i==0),s[2]+(i==1))
@lru_cache(None)
def pair(s):
    vals=[(K0*ell(s),dK*ell(s)),(L0,dL)]
    if s[0]<N:
        ch=[pair(child(s,i)) for i in range(3)]
        vals.append((1+sum((P[i]*ch[i][0] for i in range(3)),F(0)),
                     sum((P[i]*ch[i][1] for i in range(3)),F(0))))
    m=min(v[0] for v in vals)
    winners=[a for a,v in zip(A,vals) if v[0]==m]
    if s==R:selected='Q'
    elif s==Y:selected='P'
    else:selected=winners[0]
    assert selected in winners,(s,winners)
    return *vals[A.index(selected)],dict(zip(A,vals)),selected,tuple(winners)
steps=[];gap0=[]
for n in range(N+1):
  for a in range(n+1):
    for b in range(n-a+1):
      s=(n,a,b);v,d,options,sel,w=pair(s)
      for ac,(v2,d2) in options.items():
        if ac==sel:continue
        gap=v2-v;dg=d2-d
        assert gap>=0,(s,ac,gap)
        if gap==0:
            gap0.append((s,ac,dg))
            assert (s==R and ac=='C' and dg==0) or (s==Y and ac=='C' and dg>0),(s,ac,dg)
        elif dg<0:steps.append((-gap/dg,s,ac,gap,dg))
assert len(gap0)==2
assert steps
steps.sort();minimum=steps[0][0]
closes=[(s,ac,g,d) for t,s,ac,g,d in steps if t==minimum]
K=K0+dK*minimum;L=L0+dL*minimum
@lru_cache(None)
def bell(s):
    vals=[K*ell(s),L]
    if s[0]<N:vals.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
    m=min(vals);return m,tuple(a for a,v in zip(A,vals) if v==m),vals
TIES={};positive=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,w,opts=bell(s)
   if len(w)>1:TIES[str(s)]=list(w)
   positive.extend(x-v for x in opts if x>v)
print('Ray',fmt(dK),fmt(dL),'candidate_count',len(steps))
print('FIRST_CLOSE',fmt(minimum),'K',fmt(K),'L',fmt(L),'root',fmt(bell((0,0,0))[0]))
print('CLOSURES',[(s,ac,fmt(g),fmt(d)) for s,ac,g,d in closes])
print('NEXT_5',[(fmt(t),s,ac) for t,s,ac,*_ in steps[:5]])
print('TIES',TIES,'strict_gaps',len(positive),'smallest',fmt(min(positive)))
cert={'status':'STAGE173_DUAL_ONLY','model':'EXTERNAL_N14_TERNARY_IID','stage172_source':'certificate172.json','ray':{'K172':fmt(K0),'L172':fmt(L0),'dK':fmt(dK),'dL':fmt(dL)},'candidate':{'step':fmt(minimum),'K':fmt(K),'L':fmt(L),'H':fmt(bell((0,0,0))[0]),'ties':TIES,'strict_gaps':len(positive),'min_strict_gap':fmt(min(positive)),'number_of_negative_slope_candidates':len(steps),'closures':[{'state':list(s),'action':ac,'gap':fmt(g),'derivative':fmt(d)} for s,ac,g,d in closes]}}
Path(__file__).with_name('dual173.json').write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
