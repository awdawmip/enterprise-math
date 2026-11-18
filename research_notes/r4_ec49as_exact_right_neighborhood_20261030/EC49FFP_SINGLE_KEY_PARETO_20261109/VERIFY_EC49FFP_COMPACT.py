"""EC49FFP: independently runnable one-key adjacent-horizon census.
Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Original X6/DFA model Git blob 6350340fbe869f17b5a50bd1ba30640db44a3a99.
"""
from collections import Counter
import json
A='acdefg'; S=(0,0,4,1,16,32,8,2,0)
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
W={(3,4):((4,2,1),),(4,5):((4,3,1),(5,2,1),(5,3,1)),(5,6):((4,4,1),(5,3,1),(5,4,1),(6,2,1),(6,2,2),(6,3,1),(6,4,1))}
EXPECTED={(3,4):(56,),(4,5):(62,62,72),(5,6):(68,60,78,68,74,78,88)}

def original_words(h,k):
 x,y,z=k;total=x+y-h-1
 for c in range(total+1):
  ct=[z-1,c,total-c,z,h+1-y-2*z,h+1-x]
  def rec(t,s):
   if not any(ct):
    if S[s] in (1,2,4,8): yield t,S[s]
    return
   for i in range(6):
    if ct[i]:
     ct[i]-=1
     yield from rec(t+A[i],T[s][i])
     ct[i]+=1
  yield from rec('',0)

def solve(horizons,k):
 need=tuple((h,s) for h in horizons for s in (1,2,4,8))
 trie=[{}];term=[0];cnt=Counter()
 for h in horizons:
  for word,sig in original_words(h,k):
   ct=Counter(x for op in word for x in OPS[op])
   assert tuple(ct[i]-ct[-i] for i in range(1,7))==(2,0,0,0,0,0)
   assert tuple(ct[i] for i in (1,2,3))==k
   cnt[h]+=1;p=0
   for x in (v for op in word for v in OPS[op]):
    if x not in trie[p]:
     trie[p][x]=len(trie);trie.append({});term.append(0)
    p=trie[p][x]
   term[p]|=1<<need.index((h,sig))
 dp=[None]*len(trie)
 for p in range(len(trie)-1,-1,-1):
  d={0:0};mask=term[p];sub=mask
  while sub:d[sub]=0;sub=(sub-1)&mask
  for child in trie[p].values():
   e=dp[child];f=d.copy()
   for a,va in d.items():
    for b,vb in e.items():
     if not a&b:
      i=a|b;v=va+vb+(b!=0)
      if v<f.get(i,10**9):f[i]=v
   d=f
  dp[p]=d
 return dp[0][255],len(trie),dict(cnt)

def main():
 result={}
 for hs,keys in W.items():
  rows=[]
  for k in keys:
   cost,nodes,counts=solve(hs,k)
   rows.append({'key':k,'cost':cost,'nodes':nodes,'counts':counts})
  assert tuple(row['cost'] for row in rows)==EXPECTED[hs],(hs,rows)
  result['H%d_H%d'%hs]=rows
 print(json.dumps({'status':'EXACT_INTEGER_DP_PASS','cases':sum(map(len,W.values())),'result':result},indent=2))
if __name__=='__main__':main()
