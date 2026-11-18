#!/usr/bin/env python3
"""Independent literal signed-prefix, original 9-state DFA, exact Q-rank audit."""
from fractions import Fraction
from pathlib import Path
from collections import Counter
import json
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
S={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
BUCKET={1:(2,3,2,3,3,2,4,3,4),2:(2,2,2,3,3,2,2,3,4),4:(1,1,4,1,3,4,4,3,4),8:(1,1,1,1,1,4,4,3,4),16:(0,0,2,1,3,2,2,3,4),32:(0,1,0,1,1,2,4,3,4)}
W={
2:{16:'fe',32:'ge'},3:{16:'feg',32:'gef'},
4:{1:'gefd',2:'fegd',4:'cefg',8:'gefc'},
5:{16:'feggf',32:'geffg'},
6:{1:'gefdfg',2:'fegdgf',4:'feggfc',8:'geffgc'},
7:{1:'gefdfgf',2:'fegdgff',4:'feggfcf',8:'geffgcg'},
8:{1:'geffgfgd',2:'feggffgd',4:'feggfcfg',8:'geffgcgf'},
9:{16:'feggffggf',32:'geffgfggf'}
}
def rank(M):
 A=[list(map(Fraction,row)) for row in M];m=len(A);n=len(A[0]);r=0
 for j in range(n):
  pivot=next((i for i in range(r,m) if A[i][j]),None)
  if pivot is None:continue
  A[r],A[pivot]=A[pivot],A[r]
  d=A[r][j]
  for k in range(j,n):A[r][k]/=d
  for i in range(r+1,m):
   if A[i][j]:
    f=A[i][j]
    for k in range(j,n):A[i][k]-=f*A[r][k]
  r+=1
  if r==m:break
 return r

def check():
 P=set(); Ks=set();runs=[];native_by_h={}
 for h in sorted(W):
  labs=set(W[h]); M=[[int(BUCKET[s][i]==b) for s in sorted(labs) for b in range(5)] for i in range(9)]
  rk=rank(M); assert rk==9,(h,rk)
  hkeys=set()
  for sig,w in W[h].items():
   assert len(w)==h
   q=0
   for ch in w:q=T[q][OPS.index(ch)]
   assert SIG[q]==sig,(h,sig,w,SIG[q])
   assert Counter(w)['e']==Counter(w)['a']+1
   L=tuple(step for c in w for step in S[c]);assert all(L.count(i)-L.count(-i)==(2 if i==1 else 0) for i in (1,2,3))
   k=tuple(L.count(i) for i in (1,2,3));assert k[0]>0 and k[2]>0
   hkeys.add(k);Ks.add(k)
   P.update(L[:j] for j in range(1,len(L)+1))
  runs.append({'h':h,'labels':sorted(labs),'rational_rank':rk,'cumulative_edges':len(P),'full_keys':[list(t) for t in sorted(hkeys)]})
 assert len(P)==93 and len(Ks)==8 and len([x for x in Ks if min(x)>0])==7
 res={'model':'FROZEN_ORIGINAL_24_LABEL_WITNESS_RELAXED_CACHE_KEYS','word_count':sum(len(x) for x in W.values()),'edges':len(P),'full_keys':sorted(Ks),'distinct_full_keys':len(Ks),'strictly_positive_keys':sum(min(x)>0 for x in Ks),'runs':runs}
 with open(str(Path(__file__).with_name('WITNESS_AUDIT_EC49FGD.json')),'w') as f:json.dump(res,f,indent=2);f.write('\n')
 print('INDEPENDENT_WITNESS_PASS',len(P),'keys',len(Ks),'positive',res['strictly_positive_keys']);return res
if __name__=='__main__':check()
