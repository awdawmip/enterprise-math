#!/usr/bin/env python3
"""Exact Stages236–239 IID minimax: Fraction DP, independent ordered integer DFS."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json
P=(F(3,24),F(1,24),F(20,24));PN=(3,1,20);QN=(2,2,20)
STATES=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(STATES)==680
fmt=lambda x:f'{x.numerator}/{x.denominator}'
nexts=lambda s,j:(s[0]+1,s[1]+(j==0),s[2]+(j==1))
DATA=[
(236,F(131416,2095),F(1497492,23045),F(237666670990705,648489579282432),F(647346693246113,81061197410304),F(15323241207681715,41771181786955776),F(41467533247735739,5221397723369472),2,1238,3,10804),
(237,F(357144,5855),F(373248,5855),F(15323241207681715,41771181786955776),F(41467533247735739,5221397723369472),F(1077247581785,2925595459584),F(2841501441371,365699432448),7,1233,4071,293468),
(238,F(2127864,35755),F(2239488,35755),F(1077247581785,2925595459584),F(2841501441371,365699432448),F(180193047485,487599243264),F(1390895775373,182849716224),8,1232,14703,447586),
(239,F(12692184,217655),F(13436928,217655),F(180193047485,487599243264),F(1390895775373,182849716224),F(1446305583005,3900793946112),F(10912825831109,1462797729792),9,1231,46767,644072)]
def verify(t):
 stage,lp,lq,al,vl,ar,vr,k,gapcount,vertexcount,nodecount=t
 @lru_cache(None)
 def bell(s):
  n,a,b=s; d={'P':lq*F(2**(a+b),3**a),'Q':lp}
  if n<14:d['C']=1+sum(P[j]*bell(nexts(s,j))[0] for j in range(3))
  m=min(d.values());return m,tuple(z for z,v in d.items() if v==m),d
 H=bell((0,0,0))[0]
 ties=tuple(s for s in STATES if len(bell(s)[1])==2)
 assert len(ties)==k and not any(len(bell(s)[1])>2 for s in STATES)
 options=tuple(bell(s)[1] for s in ties)
 gaps=[v-bell(s)[0] for s in STATES for v in bell(s)[2].values() if v>bell(s)[0]]
 assert len(gaps)==gapcount and min(gaps)>0
 def action(s,bits):
  if s in ties:return options[ties.index(s)][bits[ties.index(s)]]
  assert len(bell(s)[1])==1
  return bell(s)[1][0]
 @lru_cache(None)
 def dp(s,bits):
  a=action(s,bits)
  if a!='C':return F(a=='Q'),F(a=='P'),F(0),F(0)
  cs=[dp(nexts(s,j),bits) for j in range(3)]
  return tuple(F(i>=2)+sum((P if i%2==0 else tuple(F(x,24) for x in QN))[j]*cs[j][i] for j in range(3)) for i in range(4))
 def dfs(bits):
  stack=[(0,0,0,1,1)];tot=[0,0,0,0];visits=0
  while stack:
   n,a,b,p,q=stack.pop();visits+=1
   choice=action((n,a,b),bits)
   if choice=='C':
    for j in range(3):stack.append((n+1,a+(j==0),b+(j==1),p*PN[j],q*QN[j]))
   else:
    d=24**(14-n)
    tot[1 if choice=='P' else 0]+=(q if choice=='P' else p)*d
    tot[2]+=n*p*d;tot[3]+=n*q*d
  return tuple(F(x,24**14) for x in tot),visits
 corners={};visits={}
 for bits in product((0,1),repeat=k):
  a=dp((0,0,0),bits);b,v=dfs(bits)
  assert a==b and a[2]+lp*a[0]+lq*a[1]==H and a[2]>a[3]
  corners[bits]=a;visits[bits]=v
 assert sum(visits.values())==nodecount
 vertices=[]
 for bits,v in corners.items():
  if v[0]==v[1]:vertices.append((v[0],v[2],v[3],(bits,), (F(1),)))
 for a,b in combinations(corners,2):
  v,w=corners[a],corners[b];e=v[0]-v[1];f=w[0]-w[1]
  if e*f>=0:continue
  u=-f/(e-f);o=tuple(u*v[i]+(1-u)*w[i] for i in range(4))
  assert 0<u<1 and o[0]==o[1] and o[2]>o[3]
  vertices.append((o[0],o[2],o[3],(a,b),(u,1-u)))
 assert len(vertices)==vertexcount
 lo=min(vertices,key=lambda x:x[0]);hi=max(vertices,key=lambda x:x[0])
 assert (lo[0],lo[1],hi[0],hi[1])==(al,vl,ar,vr)
 assert vl+(lp+lq)*al==H==vr+(lp+lq)*ar and ar>al
 def ext(v):return {'alpha':fmt(v[0]),'tP':fmt(v[1]),'tQ':fmt(v[2]),'policies':[''.join(map(str,z)) for z in v[3]],'weights':[fmt(z) for z in v[4]]}
 return {'stage':stage,'lp':fmt(lp),'lq':fmt(lq),'H':fmt(H),'slope':fmt(-lp-lq),'ties':ties,'options':options,'states':len(STATES),'strict_gaps':len(gaps),'min_gap':fmt(min(gaps)),'corners':{''.join(map(str,b)):[fmt(v) for v in x] for b,x in corners.items()},'nodes':{''.join(map(str,b)):x for b,x in visits.items()},'total_nodes':sum(visits.values()),'balanced_vertices':len(vertices),'balanced_distinct_errors':len({v[0] for v in vertices}),'left':ext(lo),'right':ext(hi),'delta':fmt(ar-al)}
if __name__=='__main__':
 results=[verify(t) for t in DATA]
 assert F(results[0]['right']['alpha'])==F(results[1]['left']['alpha'])
 assert F(results[0]['right']['tP'])==F(results[1]['left']['tP'])
 assert F(results[0]['slope'])<F(results[1]['slope'])
 out=Path(__file__).resolve().parent/'PORTABLE_EXACT_CERT_STAGE236_239.json'
 out.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
 for r in results:print('STAGE',r['stage'],'PASS',r['total_nodes'],'vertices',r['balanced_vertices'],'right_alpha',r['right']['alpha'])
 print('STAGE236_239_PORTABLE_EXACT_PASS',sum(r['total_nodes'] for r in results))
