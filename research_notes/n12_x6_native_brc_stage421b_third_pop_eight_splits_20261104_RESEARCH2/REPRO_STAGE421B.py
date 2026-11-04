#!/usr/bin/env python3
"""Exact eight-witness certificate: third POP splits each non-singleton 2-POP signature."""
from collections import defaultdict
from json import dumps
A,B=1,-1
G=((0,1,2,3),(4,5,12,13),(6,14,20),(7,15,21),(8,16,22),(9,17),(10,18,24),(11,19),(23,),(25,),(26,),(27,),(28,),(29,),(30,),(31,))
P=('POP',); C=('CANCEL',); X=('APP',B,B);Y=('APP',B,A)
CERT=((0,3,(P,P,P,X,C,X,C)),(4,13,(P,P,P,X,C,Y,C)),(6,20,(P,P,P,Y,C,X,C)),(7,21,(P,P,P,Y,C,X,C)),(8,22,(P,P,P,X,C,X,C)),(9,17,(P,X,C,C,P,P)),(10,24,(P,P,P,X,C,X,C)),(11,19,(P,C,P,P,X,C)))

def fiber(n):
 for r in range(2,n-2):
  for s in range(r+2,n):
   for i in (r,s):yield (r,s,i,(A,)*(i-1)+(B,)+(A,)*(n-i),(A,)*(r-1)+(B,)+(A,)*(s-r-1)+(B,)+(A,)*(n-s))

def obs(U,V):
 def one(w):
  hist=defaultdict(int)
  for edge in zip(w,w[1:]):hist[edge]+=1
  return len(w),tuple(w.count(k)-w.count(-k) for k in range(1,7)),tuple(sorted(hist.items()))
 return one(U),one(V),sum(u==v for u,v in zip(U,V))

def run(h,trace):
 U,V=list(h[3]),list(h[4]);pop=3;cancel=2
 seq=[]
 for op in trace:
  if op[0]=='POP':
   assert pop>0 and len(V)>0
   V.pop();pop-=1
  elif op[0]=='APP':
   U.append(op[1]);V.append(op[2])
  elif op[0]=='CANCEL':
   assert cancel>0 and len(U)>=2 and len(V)>=2 and U[-1]==-U[-2] and V[-1]==-V[-2]
   del U[-2:];del V[-2:];cancel-=1
  else:raise ValueError(op)
  seq.append(obs(U,V))
 return seq

def main():
 f=list(fiber(11));reps={}
 for h in f:reps.setdefault((h[3][-6:],h[4][-7:]),h)
 keys=list(reps);assert len(keys)==32
 result=[]
 for g,(i,j,T) in enumerate(CERT):
  assert i in G[g] and j in G[g]
  h1,h2=reps[keys[i]],reps[keys[j]]
  assert obs(h1[3],h1[4])==obs(h2[3],h2[4])
  x,y=run(h1,T),run(h2,T)
  assert x[:-1]==y[:-1],('early divergence',g)
  assert x[-1]!=y[-1],('not distinguished',g)
  differences=[]
  for k,name in enumerate(('P length/z/J','Q length/z/J','absolute K')):
   if x[-1][k]!=y[-1][k]:differences.append(name)
  result.append({'old_signature':g,'raw_suffix_key_indices':[i,j],
                 'history1':{'r':h1[0],'s':h1[1],'i':h1[2]},
                 'history2':{'r':h2[0],'s':h2[1],'i':h2[2]},
                 'operations':[list(op) for op in T],
                 'first_difference_at_step':len(T),
                 'changed_observer_components':differences,
                 'last_K_values':[x[-1][-1],y[-1][-1]],
                 'number_POP':sum(t[0]=='POP' for t in T),
                 'number_CANCEL':sum(t[0]=='CANCEL' for t in T)})
 assert len(result)==8
 return {'marker':'STAGE421B_THIRD_POP_EIGHT_STRICT_SPLITS_PASS',
         'claim':'For all n>=11, q_(3 Q POP,2 paired CANCEL)(F_n)>=24',
         'check_n':11,'old_2POP_minimal_classes':16,'strictly_split_old_classes':8,
         'explicit_distinguishing_traces':result,
         'scope':'Exact certificates on F11 with prefix-padding transfer to all n>=11; no third-POP upper bound or minimality proved',
         'frozen_science_global':'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
         'frozen_science_EM':'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',
         'p000_blob':'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'}
if __name__=='__main__':print(dumps(main(),indent=2,ensure_ascii=False))
