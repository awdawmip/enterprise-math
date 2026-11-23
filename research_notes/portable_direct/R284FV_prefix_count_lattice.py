#!/usr/bin/env python3
"""R284FV exact prefix obstruction on seven-pattern stable-cut survivors.
Source: R284FT integral-flow prefix lemma; standard-library integers only.
"""
from collections import deque
from functools import lru_cache
from itertools import product
from pathlib import Path
import sys
Q,U=7,1
PHASE={p:(0,p&1,(p>>1)&1,(p>>2)&1) for p in range(1,8)}
LATEST={p:tuple(next(e for e in ((i-1-t)%4 for t in range(4)) if PHASE[p][e]!=PHASE[p][(e+1)%4]) for i in range(4)) for p in range(1,8)}
class Flow:
 def __init__(self):self.g=[[] for _ in range(17)]
 def add(self,a,b,n):
  self.g[a].append([b,n,len(self.g[b])]);self.g[b].append([a,0,len(self.g[a])-1])
 def maximum(self):
  total=0
  while True:
   prev=[None]*17;prev[0]=(-1,-1);q=deque([0])
   while q and prev[16] is None:
    v=q.popleft()
    for k,(w,c,_) in enumerate(self.g[v]):
     if c and prev[w] is None:prev[w]=(v,k);q.append(w)
   if prev[16] is None:return total
   amt=10**9;v=16
   while v: a,k=prev[v];amt=min(amt,self.g[a][k][1]);v=a
   v=16
   while v: a,k=prev[v];b,_,back=self.g[a][k];self.g[a][k][1]-=amt;self.g[b][back][1]+=amt;v=a
   total+=amt

def prefix_distance(x,i,j,target,succ):
 net=Flow();d=0
 for p in range(1,8):
  free=x[p-1]-succ.get(p,0)
  if free and PHASE[p][i]!=PHASE[p][j]:
   d+=free;net.add(0,p,free);net.add(p,8+LATEST[p][i],free);net.add(p,12+LATEST[p][j],free)
  fixed=succ.get(p,0)
  if fixed and PHASE[p][target]!=PHASE[p][j]:
   d+=fixed;net.add(0,12+LATEST[p][j],fixed)
 for k in range(4):net.add(8+k,16,Q);net.add(12+k,16,Q)
 return d-net.maximum()

def safe_path(x,edge):
 tgt=(edge+1)%4
 types=tuple(p for p in range(1,8) if x[p-1] and PHASE[p][edge]!=PHASE[p][tgt])
 finish=tuple(x[p-1] for p in types)
 @lru_cache(None)
 def safe(prefix):
  for miss in product(*(range(min(Q,t)+1) for t in prefix)):
   if sum(miss)>Q:continue
   succ={p:t-m for p,t,m in zip(types,prefix,miss)}
   for third in range(4):
    if third not in (edge,tgt) and prefix_distance(x,edge,third,tgt,succ)<=2*U:return False
   if sum(succ.values())<=2*U and prefix_distance(x,edge,tgt,tgt,succ)<=2*U:return False
  return True
 front=deque([(0,)*len(types)]);seen={(0,)*len(types)}
 while front:
  t=front.popleft()
  if t==finish:return True
  for k in range(len(types)):
   if t[k]==finish[k]:continue
   nxt=t[:k]+(t[k]+1,)+t[k+1:]
   if nxt not in seen:
    seen.add(nxt)
    if safe(nxt):front.append(nxt)
 return False

def main():
 global Q
 Q=int(sys.argv[1]);n=int(sys.argv[2])
 assert 7<=Q<=10 and n in (4*Q+8,4*Q+9)
 path=Path(sys.argv[3] if len(sys.argv)>3 else '.')/f'R284FV_q{Q}_n{n}_stable.txt'
 hist=[tuple(map(int,line.split())) for line in path.read_text().splitlines()]
 assert all(len(x)==7 and sum(x)==n for x in hist)
 a=[x for x in hist if safe_path(x,0)]
 b=[x for x in a if safe_path(x,1)]
 print('q',Q,'n',n,'stable',len(hist),'edge0',len(a),'edge1',len(b),'first',a,'both',b)
 expected_stable=7 if n==4*Q+8 else 66
 expected_first=1 if n==4*Q+8 else 10
 assert (len(hist),len(a),len(b))==(expected_stable,expected_first,0), (Q,n)
if __name__=='__main__':main()
