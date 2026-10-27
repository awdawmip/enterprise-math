#!/usr/bin/env python3
"""Exact rational primal and Bellman certificates: N4 F' has partial TV masking."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import json

P,Q,C=(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))
N={1:{'A':(F(1,2),F(1,2),None),'B':(F(1,2),F(3,2),None)},
  2:{'AU':(F(1,6),F(1),'A'),'AV':(F(1,3),F(1,4),'A'),
     'BU':(F(1,4),F(1),'B'),'BV':(F(1,4),F(2),'B')}}
for t in (3,4):
 N[t]={}
 for parent,(q,r,_) in N[t-1].items():
  e=({'AU':F(1,10),'AV':F(0),'BU':F(4,5),'BV':F(0)}[parent] if t==3
     else F(0) if parent=='AV0' else F(3,50) if parent=='AV1' else F(1,20))
  for k,s in enumerate((-1,1)):
   N[t][parent+str(k)]=(q/2,r*(1+s*e),parent)
for t in N:
 assert len(N[t])==2**t and all(q>0 and r>0 for q,r,_ in N[t].values())
 assert sum(q for q,r,_ in N[t].values())==sum(q*r for q,r,_ in N[t].values())==1
 if t<4:
  for h,(q,r,_) in N[t].items():
   children=[(qc,rc) for qc,rc,pa in N[t+1].values() if pa==h]
   assert len(children)==2 and sum(qc for qc,rc in children)==q
   assert sum(qc*rc for qc,rc in children)==q*r
assert N[2]['AU'][1]==N[2]['BU'][1] and N[3]['AV0'][1]==N[3]['AV1'][1]

def baseline(t,h,r):
 if t==1:return C
 if t==2:return {'AU':P,'AV':C,'BU':C,'BV':P}[h]
 if t==3:return {'AV0':Q,'AV1':C,'BU0':C,'BU1':Q}.get(h,P)
 return Q if 100*r<F(2501,100) else P

def witness(kind,t,h,r):
 if kind=='3':
  if t==3 and h in ('AV0','AV1'):return (F(0),F(1,2),F(1,2))
  if t==4 and r==F(1,4):return (F(253,500),F(247,500),F(0))
  return baseline(t,h,r)
 if t==1:return C
 if t==2:
  if h in ('AU','BU'):
   return (F(496,1265),F(0),F(769,1265)) if kind=='2' else (F(30677,78510),F(0),F(47833,78510))
  if h=='AV':
   return (F(4,253),F(0),F(249,253)) if kind=='2' else (F(727,39255),F(0),F(38528,39255))
  return P
 if t==3:
  if h in ('AU0','AU1'):return Q
  if h in ('AV0','AV1'):
   if kind=='23':return (F(0),F(26911,77056),F(50145,77056))
   return (F(0),F(26911,38595),F(11684,38595)) if h=='AV0' else C
  if h=='BU0':return C
  if h=='BU1':return (F(0),F(23835,23839),F(4,23839)) if kind=='2' else (F(0),F(47650,47833),F(183,47833))
  return P
 if r==F(1,4):
  return (F(307,11684),F(11377,11684),F(0)) if kind=='2' else (F(18727,66860),F(48133,66860),F(0))
 return baseline(t,h,r)

def observations(policy):
 out=[F(0)]*16
 for leaf,(q,r4,_) in N[4].items():
  alive=F(1)
  for t,h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
   a=policy(t,h,N[t][h][1])
   assert all(x>=0 for x in a) and sum(a)==1 and (t<4 or a[2]==0)
   for j in (0,1):
    i=2*(t-1)+j;out[i]+=q*alive*a[j];out[8+i]+=q*r4*alive*a[j]
   alive*=a[2]
  assert alive==0
 assert sum(out[:8])==sum(out[8:])==1
 return tuple(out)

B=observations(baseline)
V={k:observations(lambda t,h,r:k and witness(k,t,h,r)) for k in ('2','3','23')}
for kind in V:
 for t in ({'2':(2,4),'3':(3,4),'23':(2,3,4)}[kind]):
  seen={}
  for h,(q,r,_) in N[t].items():
   a=witness(kind,t,h,r)
   if r in seen:assert seen[r]==a,(kind,t,h,r)
   seen[r]=a
TV=lambda v,off:sum(abs(v[i]-B[i]) for i in range(off,off+8))/2
assert [(TV(V[k],0),TV(V[k],8)) for k in ('2','3','23')]==[
 (F(1,506),F(1,506)),(F(1,2000),F(1,2000)),(F(727,314040),F(727,314040))]

W={
 '2':(tuple(map(F,['0','0','25/253','0','3/2024','25/253','25/253','-25/253'])),
      tuple(map(F,['0','0','-203/506','0','0','-197/506','-197/506','203/506']))),
 '3':(tuple(map(F,['1/10','1/10','97/1000','1/10','1/10','374/3875','1/10','-1/10'])),
      tuple(map(F,['2/5','2/5','-2/5','2/5','2/5','-617/1550','-2/5','2/5']))),
 '23':(tuple(map(F,['0','0','1293/13085','0','0','3736/39255','3871/39255','-1293/13085'])),
       tuple(map(F,['0','0','-10499/26170','0','0','-30353/78510','-30503/78510','10499/26170'])))}

def linear_score(v,wq,wp):return sum(wq[i]*v[i]+wp[i]*v[8+i] for i in range(8))

def minimum(kind,wq,wp):
 def cost(t,r,a):
  i=2*(t-1)+(a=='Q')
  return wq[i]+r*wp[i]
 t4={h:min(cost(4,r,'P'),cost(4,r,'Q')) for h,(q,r,_) in N[4].items()}
 t3={}
 for h,(q,r,_) in N[3].items():
  t3[h]={a:cost(3,r,a) for a in 'PQ'}
  t3[h]['C']=sum(q4*t4[ch]/q for ch,(q4,r4,par) in N[4].items() if par==h)
 roots={};count=0
 for a1 in product('PQC',repeat=2):
  root=dict(zip(('A','B'),a1));best=None
  for a2 in product('PQC',repeat=4 if kind=='3' else 3):
   count+=1
   at2=dict(zip(('AU','AV','BU','BV') if kind=='3' else ('U','AV','BV'),a2))
   val=sum(q*cost(1,r,root[h]) for h,(q,r,_) in N[1].items() if root[h]!='C')
   groups=defaultdict(list)
   for h,(q,r,par) in N[2].items():
    if root[par]!='C':continue
    a=at2['U' if kind!='3' and h in ('AU','BU') else h]
    if a!='C':val+=q*cost(2,r,a)
    else:
     for ch,(q3,r3,pa) in N[3].items():
      if pa==h:groups[ch if kind=='2' else r3].append(ch)
   for histories in groups.values():
    val+=min(sum(N[3][h][0]*t3[h][a] for h in histories) for a in 'PQC')
   if best is None or val<best:best=val
  roots[''.join(a1)]=best
 assert count==(729 if kind=='3' else 243)
 return min(roots.values()),roots,count

minima={};cert={}
for kind in ('2','3','23'):
 wq,wp=W[kind]
 m,roots,count=minimum(kind,wq,wp)
 osc=max(wq)-min(wq)+max(wp)-min(wp)
 gap=m-linear_score(B,wq,wp)
 assert osc==1 and gap==TV(V[kind],0)
 minima[kind]=gap/osc
 cert[kind]={'scoreQ':list(map(str,wq)),'scoreP':list(map(str,wp)),
  'F_score':str(linear_score(B,wq,wp)),'minimum':str(m),
  'oscillation_sum':str(osc),'gap':str(gap),'prefix_count':count,
  'root_minima':{k:str(v) for k,v in sorted(roots.items())}}
assert minima=={'2':F(1,506),'3':F(1,2000),'23':F(727,314040)}
result={
 'status':'PASS_EXACT_FRACTION_N4_FPRIME_PARTIAL_UNMASKING',
 'baseline_Fprime':list(map(str,B)),
 'witness_joint_laws':{k:list(map(str,V[k])) for k in V},
 'primal_TV_by_law':{k:dict(Q=str(TV(V[k],0)),P=str(TV(V[k],8))) for k in V},
 'exact_minimax':{k:str(v) for k,v in minima.items()},
 'strict_unmasking':'26911/79452120',
 'strict_subadditivity':'640753/3972606000',
 'duals':cert,
 'tree_node_counts':{str(t):len(N[t]) for t in N},
 'quantifier_scope':'one fixed tree, one fixed Fprime, full real independent behavioral strategies',
 'admission':'AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED; no native X6 transfer'
}
assert minima['23']-minima['2']==F(26911,79452120)>0
assert minima['2']+minima['3']-minima['23']==F(640753,3972606000)>0
print(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False))
