#!/usr/bin/env python3
"""PREFIX-545 exact scalar/controlled observer quotients; frozen scientific pin f42f2906..."""
from collections import Counter,defaultdict
import json
S=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*k for k in S[a] if k!=abs(c))
P=tuple((a,p,e*k) for a in range(4) for k in S[a] for e in (-1,1) for p in near(a,e*k))
I={v:i for i,v in enumerate(P)}
def succ(i):
 a,p,c=P[i];b=next(b for b in range(4) if b!=a and abs(c) in S[b]);return tuple(I[x] for x in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
N=tuple(succ(i) for i in range(48));T=I[(0,1,-3)]
V=tuple((i,b) for i in range(48) for b in (0,1));A=tuple((k,b) for k in range(3) for b in (0,1))
def sign(i):return (1 if P[i][2]>0 else -1) if abs(P[i][2])==1 else 0
def tau(r,i,j):
 z=abs(sign(i))+abs(sign(j))-abs(sign(j)-r)+abs(sign(i)-r)
 assert z%2==0 and z//2 in (0,1)
 return z//2
def edge(r,v,a):
 i,b=v;k,c=a;j=N[i][k];return (j,c),(tau(r,i,j),int(b==c==1 and j==T))
def step(r,F):
 out=[]
 for v in V:
  row=defaultdict(int)
  for a in A:
   w,(p,h)=edge(r,v,a)
   for (x,y),n in F[2*w[0]+w[1]].items():row[p+x,h+y]+=n
  out.append(dict(row))
 return out
def quotient(r):
 F=[{(0,0):1} for _ in V];fp=[[] for _ in V];growth=[]
 for d in range(6):
  for i in range(96):fp[i].append(tuple(sorted(F[i].items())))
  growth.append(len({tuple(x) for x in fp}))
  if d<5:F=step(r,F)
 ids={};cls=[ids.setdefault(tuple(x),len(ids)) for x in fp]
 assert len(ids)==28
 Q={}
 for i,v in enumerate(V):
  row=Counter()
  for a in A:
   w,(p,h)=edge(r,v,a);row[cls[2*w[0]+w[1]],p,h]+=1
  if cls[i] in Q:assert Q[cls[i]]==row
  else:Q[cls[i]]=row
 assert len(Q)==28 and sum(map(len,Q.values()))==73 and sum(sum(x.values()) for x in Q.values())==168
 return cls,Q,growth
def qstep(Q,F):
 out=[]
 for c in range(28):
  row=defaultdict(int)
  for (j,p,h),k in Q[c].items():
   for (x,y),n in F[j].items():row[x+p,y+h]+=k*n
  out.append(dict(row))
 return out
def controlled(r):
 old=[0]*96;growth=[]
 while True:
  lookup={};new=[]
  for v in V:
   sig=tuple((edge(r,v,a)[1],old[2*edge(r,v,a)[0][0]+edge(r,v,a)[0][1]]) for a in A)
   new.append(lookup.setdefault(sig,len(lookup)))
  growth.append(len(lookup))
  if len(set(new))==len(set(old)):
   assert all((new[i]==new[j])==(old[i]==old[j]) for i in range(96) for j in range(96));break
  old=new
 assert len(set(new))==51
 preds={i for i in range(48) if T in N[i]};assert len(preds)==3
 assert all((new[i]==new[j])==(V[i][0]==V[j][0] and (V[i][1]==V[j][1] or V[i][0] not in preds)) for i in range(96) for j in range(96))
 return growth

def native(s,b0,D):
 W={(s,b0,0,0):1};out=[];r=sign(s)
 for d in range(D+1):
  row=defaultdict(int)
  for (i,b,k,h),n in W.items():
   rest=k-abs(sign(i)-r);assert rest>=0 and rest%2==0
   row[rest//2,h]+=n
  assert sum(row.values())==6**d
  out.append(dict(row))
  if d==D:break
  nxt=defaultdict(int)
  for (i,b,k,h),n in W.items():
   for j in N[i]:
    for c in (0,1):nxt[j,c,k+abs(sign(i))+abs(sign(j)),h+int(b==c==1 and j==T)]+=n
  W=nxt
 return out

def run(D=24):
 assert len(P)==len(I)==48 and T not in N[T] and sum(map(len,N))==144 and D>=7
 summary={'status':'ALL_CHECKS_PASS','frozen_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','ports':96,'scalar_classes':28,'controlled_classes':51,'all_port_polynomial_checks':0,'native_endpoint_checks':0,'classes_by_r':{}}
 calc={}
 for r in (-1,0,1):
  cls,Q,growth=quotient(r);control=controlled(r);calc[r]=(cls,Q)
  summary['classes_by_r'][str(r)]={'scalar_depth_0_to_5':growth,'controlled_depth_1_to_stable':control,'scalar_class_sizes':dict(Counter(Counter(cls).values()))}
  F=[{(0,0):1} for _ in V];G=[{(0,0):1} for _ in range(28)]
  for d in range(D+1):
   assert all(F[i]==G[cls[i]] for i in range(96))
   summary['all_port_polynomial_checks']+=96
   if d<D:F=step(r,F);G=qstep(Q,G)
  assert all(sum(h.values())==6**D for h in F)
 for s in range(48):
  cls,Q=calc[sign(s)];n0=native(s,0,7);n1=native(s,1,7)
  G=[{(0,0):1} for _ in range(28)]
  for d in range(8):
   assert G[cls[2*s]]==n0[d] and G[cls[2*s+1]]==n1[d]
   summary['native_endpoint_checks']+=2
   if d<7:G=qstep(Q,G)
 return summary
if __name__=='__main__':
 import sys
 print(json.dumps(run(int(sys.argv[1]) if len(sys.argv)>1 else 24),indent=2,ensure_ascii=False,sort_keys=True))
