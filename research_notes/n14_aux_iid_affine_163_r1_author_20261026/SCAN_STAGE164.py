#!/usr/bin/env python3
"""Stage164 dual candidate only; continuation after Stage162 right endpoint.
Exact affine-gap scan on the R-retaining ray; any primal interval remains unproved.
"""
from fractions import Fraction as F
from functools import lru_cache
import json
N=14
P=(F(1,8),F(1,24),F(5,6))
K=F(163900037061,554150611)
L=F(476600779976,1662451833)
dK=-F(1);dL=-F(10592,12501)
R=(10,0,1);Y=(8,4,1)
ACTS='PQC'
def fmt(z):return str(z.numerator)+('/'+str(z.denominator) if z.denominator!=1 else '')
def lr(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,x):return s[0]+1,s[1]+(x==0),s[2]+(x==1)
def add(u,v):return tuple(x+y for x,y in zip(u,v))
def sub(u,v):return tuple(x-y for x,y in zip(u,v))
def sc(a,u):return tuple(a*x for x in u)
def dot(u,k=K,l=L):return u[0]+k*u[1]+l*u[2]
def der(u):return dK*u[1]+dL*u[2]
@lru_cache(None)
def aff(s):
  opts=[(F(0),lr(s),F(0)),(F(0),F(0),F(1))]
  if s[0]<N:
      c=(F(1),F(0),F(0))
      for x in range(3):c=add(c,sc(P[x],aff(child(s,x))))
      opts.append(c)
  vals=[dot(v) for v in opts];small=min(vals)
  tied=tuple(ACTS[i] for i,v in enumerate(vals) if v==small)
  if s==R: chosen='C'; assert tied==('Q','C')
  elif s==Y: chosen='P'; assert tied==('P','C')
  else: assert len(tied)==1,(s,tied);chosen=tied[0]
  return opts[ACTS.index(chosen)]
@lru_cache(None)
def actions(s):
  opts=[(F(0),lr(s),F(0)),(F(0),F(0),F(1))]
  if s[0]<N:
      c=(F(1),F(0),F(0))
      for x in range(3):c=add(c,sc(P[x],aff(child(s,x))))
      opts.append(c)
  return opts
allstates=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
zero=[];candidate=[];gaps=[]
for s in allstates:
    chosen=aff(s)
    for i,other in enumerate(actions(s)):
        d=sub(other,chosen);g=dot(d);z=der(d)
        assert g>=0,(s,i,g)
        if g==0:
            zero.append((s,ACTS[i],fmt(z)))
            assert z>=0,(s,i,z)
        else:
            if z<0:candidate.append((-g/z,s,ACTS[i],g,z))
            gaps.append(g)
assert candidate
first=min(v[0] for v in candidate)
closures=[(s,a,fmt(g),fmt(z)) for t,s,a,g,z in candidate if t==first]
K3=K+first*dK;L3=L+first*dL
@lru_cache(None)
def bell(s):
    vals=[K3*lr(s),L3]
    if s[0]<N:vals.append(F(1)+sum(P[x]*bell(child(s,x))[0] for x in range(3)))
    low=min(vals)
    return low,tuple(ACTS[i] for i,z in enumerate(vals) if z==low),tuple(z-low for z in vals)
newties={};positive=[]
for s in allstates:
    low,tied,ds=bell(s)
    if len(tied)>1:newties[str(s)]=tied
    positive.extend(d for d in ds if d>0)
print('K163',fmt(K3),'L163',fmt(L3),'t',fmt(first),'K+L',fmt(K3+L3))
print('zero at starting ray',zero)
print('new closures',closures)
print('candidate gap count',len(candidate),'strict',len(positive),'minimum',fmt(min(positive)))
print('new ties',newties,'root',fmt(bell((0,0,0))[0]))
assert len(allstates)==680 and len(positive)>0
record={'status':'AUTHOR_DUAL_ONLY','model':'external iid ternary N14','K162':fmt(K),'L162':fmt(L),'direction':{'dK':fmt(dK),'dL':fmt(dL)},'ray_first_closure_t':fmt(first),'K163':fmt(K3),'L163':fmt(L3),'closures':[{'state':list(s),'action':a,'gap0':g,'derivative':z} for s,a,g,z in closures],'stage164_ties':{k:list(v) for k,v in newties.items()},'positive_gaps':len(positive),'min_positive_gap':fmt(min(positive)),'number_positive_initial_candidates':len(candidate),'old_zero_gaps':[[list(s),a,z] for s,a,z in zero]}
with open('/mnt/data/stage164_candidate.json','w') as f:json.dump(record,f,indent=2)
