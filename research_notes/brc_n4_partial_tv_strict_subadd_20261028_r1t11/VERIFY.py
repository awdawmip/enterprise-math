"""N4 two-law partial-compression TV: exact rational primal/dual verifier."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json
N={1:{'A':(F(1,2),F(1,2),''),'B':(F(1,2),F(3,2),'')},
   2:{'AU':(F(1,6),F(1),'A'),'AV':(F(1,3),F(1,4),'A'),
      'BU':(F(1,4),F(1),'B'),'BV':(F(1,4),F(2),'B')}}
for t in (3,4):
 N[t]={}
 for p,(q,r,_) in N[t-1].items():
  e=({'AU':F(1,10),'AV':F(0),'BU':F(4,5),'BV':F(0)}[p] if t==3
     else (F(0) if p=='AV0' else F(3,50) if p=='AV1' else F(1,20)))
  for i,s in enumerate((-1,1)):N[t][p+str(i)]=(q/2,r*(1+s*e),p)
for t in N:
 assert len(N[t])==2**t
 assert all(q>0 and r>0 for q,r,_ in N[t].values())
 assert sum(q for q,r,_ in N[t].values())==sum(q*r for q,r,_ in N[t].values())==1
 if t>1:
  for p,(q,r,_) in N[t-1].items():
   ch=[(cq,cr) for cq,cr,pa in N[t].values() if pa==p]
   assert len(ch)==2 and sum(cq for cq,cr in ch)==q and sum(cq*cr for cq,cr in ch)==q*r
assert N[2]['AU'][1]==N[2]['BU'][1] and N[3]['AV0'][1]==N[3]['AV1'][1]
P,Q,C=(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))
def full(t,n,r):
 if t==1:return C
 if t==2:return {'AU':P,'AV':C,'BU':C,'BV':P}[n]
 if t==3:return {'AV0':Q,'AV1':C,'BU0':Q,'BU1':P}.get(n,P)
 return Q if 100*r<F(2501,100) else P
def s2(t,n,r):
 if t==1:return C
 if t==2:return {F(1):(F(2,5),F(0),F(3,5)),F(1,4):C,F(2):P}[r]
 if t==3:return {F(9,10):(F(7,19),F(0),F(12,19)),F(11,10):P,
                 F(1,4):(F(0),F(13,20),F(7,20)),F(1,5):Q,F(9,5):P,F(2):P}[r]
 return {F(189,200):Q,F(1,4):Q}.get(r,P)
def s3(t,n,r):
 if t<3:return full(t,n,r)
 if t==3:return (F(0),F(1,2),F(1,2)) if n in ('AV0','AV1') else full(t,n,r)
 return (F(253,500),F(247,500),F(0)) if r==F(1,4) else Q if r==F(47,200) else P
def vec(policy):
 out=[F(0)]*16
 for leaf,(q,r,_) in N[4].items():
  alive=F(1)
  for t,n in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
   a=policy(t,n,N[t][n][1]);assert sum(a)==1 and all(x>=0 for x in a)
   for j in (0,1):
    i=2*(t-1)+j;out[i]+=q*alive*a[j];out[i+8]+=q*r*alive*a[j]
   alive*=a[2]
  assert alive==0
 assert sum(out[:8])==sum(out[8:])==1
 return out
for t,names in N.items():
 for strategy,compressed_time in ((s2,2),(s3,3)):
  sig={}
  if t in (compressed_time,4):
   for n,(q,r,_) in names.items():
    a=strategy(t,n,r)
    if r in sig:assert sig[r]==a
    sig[r]=a
f,x2,x3=map(vec,(full,s2,s3))
def tv(x,law):return sum(abs(x[i]-f[i]) for i in range(law*8,law*8+8))/2
assert (tv(x2,0),tv(x2,1))==(F(7,380),F(7,380))
assert (tv(x3,0),tv(x3,1))==(F(1,2000),F(1,2000))
w2q=tuple(map(F,(0,0,3,45,45,-45,-45,-45)))
w2p=tuple(map(F,(0,0,-29,50,-50,50,50,50)))
w3q=(F(1,10),F(1,10),F(169,1750),F(1,10),F(374,3875),-F(11,125),F(1,10),-F(1,10))
w3p=(F(2,5),F(2,5),-F(697,1750),F(2,5),-F(617,1550),F(17,50),-F(2,5),F(2,5))
def score(v,wq,wp):return sum(wq[i]*v[i]+wp[i]*v[i+8] for i in range(8))
def oracle(wq,wp,kind):
 def cost(t,r,a):
  i=2*(t-1)+(a=='Q');return wq[i]+r*wp[i]
 c3={}
 for n,(q,r,_) in N[3].items():
  c3[n]={a:cost(3,r,a) for a in 'PQ'}
  c3[n]['C']=sum(cq/q*min(cost(4,cr,'P'),cost(4,cr,'Q'))
                   for h,(cq,cr,pa) in N[4].items() if pa==n)
 vals={};cases=0
 for one in product('PQC',repeat=2):
  a1=dict(zip(('A','B'),one));best=None
  for two in product('PQC',repeat=(3 if kind==2 else 4)):
   cases+=1
   a2=dict(zip(('U','AV','BV') if kind==2 else ('AU','AV','BU','BV'),two))
   z=sum(q*cost(1,r,a1[n]) for n,(q,r,_) in N[1].items() if a1[n]!='C')
   groups=defaultdict(list)
   for n,(q,r,pa) in N[2].items():
    if a1[pa]!='C':continue
    a=a2['U' if kind==2 and n in ('AU','BU') else n]
    if a!='C':z+=q*cost(2,r,a)
    else:
     for child,(cq,cr,cp) in N[3].items():
      if cp==n:groups[child].append(child)
   for label,pair in ((('AV' if kind==3 else None),('AV0','AV1')),('BV',('BV0','BV1'))):
    if label and pair[0] in groups:
     assert pair[1] in groups
     groups[label]=groups.pop(pair[0])+groups.pop(pair[1])
   for histories in groups.values():
    z+=min(sum(N[3][h][0]*c3[h][a] for h in histories) for a in 'PQC')
   best=z if best is None or z<best else best
  vals[''.join(one)]=best
 assert cases==(243 if kind==2 else 729)
 return min(vals.values()),{k:str(v) for k,v in sorted(vals.items())},cases
m2,roots2,cases2=oracle(w2q,w2p,2)
m3,roots3,cases3=oracle(w3q,w3p,3)
assert (score(f,w2q,w2p),m2)==(-F(467,12),-F(425,12))
assert (score(f,w3q,w3p),m3)==(-F(859,2800),-F(268,875))
assert (max(w2q)-min(w2q),max(w2p)-min(w2p))==(90,100)
assert (max(w3q)-min(w3q),max(w3p)-min(w3p))==(F(1,5),F(4,5))
assert m2-score(f,w2q,w2p)==F(7,2)
assert m3-score(f,w3q,w3p)==F(1,2000)
assert roots2['CC']=='-425/12' and roots3['CC']=='-268/875'
print(json.dumps({'status':'PASS_EXACT_FRACTION_N4_PARTIAL_TV_STRICT_SUBADD',
 'counts':{str(t):len(N[t]) for t in N},'prefix_cases':{'S2':cases2,'S3':cases3},
 'F':list(map(str,f)),'S2_witness':list(map(str,x2)),'S3_witness':list(map(str,x3)),
 'S2_dual':{'Q':list(map(str,w2q)),'P':list(map(str,w2p)),'full':str(score(f,w2q,w2p)),'minimum':str(m2),'roots':roots2},
 'S3_dual':{'Q':list(map(str,w3q)),'P':list(map(str,w3p)),'full':str(score(f,w3q,w3p)),'minimum':str(m3),'roots':roots3},
 'd2':str(F(7,380)),'d3':str(F(1,2000)),'d23':str(F(7,380)),
 'd2+d3-d23':str(F(1,2000)), 'review':'UNREVIEWED_NOT_ADMITTED'},indent=2,sort_keys=True))
