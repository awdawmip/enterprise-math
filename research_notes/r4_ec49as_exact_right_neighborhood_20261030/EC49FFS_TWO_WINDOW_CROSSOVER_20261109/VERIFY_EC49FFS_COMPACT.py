#!/usr/bin/env python3
"""EC49FFS: complete 4<=a<b<=8 two-window BRC prefix-optimum census.
Frozen science: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab
Original signed-X6/DFA source Git blob: 6350340fbe869f17b5a50bd1ba30640db44a3a99.
"""
from collections import Counter
from itertools import combinations
import json
O='acdefg'; X={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0); SIG=(1,2,4,8); INF=10**9

def keys(h):
 for z in range(1,(h+1)//2+1):
  for x in range(2*z,h+2):
   for y in range(h+2-2*z):
    if x+y>=h+2: yield (x,y,z)

def words(h,k):
 x,y,z=k; n=[z-1,0,0,z,h+1-y-2*z,h+1-x]
 d=x+y-h-1
 assert min(n)>=0 and d>=1
 def rec(w,q):
  if not any(n):
   if S[q] in SIG: yield (w,S[q])
  else:
   for i in range(6):
    if n[i]:
     n[i]-=1
     yield from rec(w+O[i],T[q][i])
     n[i]+=1
 for c in range(d+1):
  n[1],n[2]=c,d-c
  yield from rec('',0)

def solve(a,b):
 demands=tuple((h,s) for h in (a,b) for s in SIG)
 bits={v:1<<i for i,v in enumerate(demands)}
 child=[{}]; terminal=[0]; label=[{}]; wc=Counter()
 for h in (a,b):
  for key in keys(h):
   for w,sig in words(h,key):
    path=tuple(z for o in w for z in X[o]); cnt=Counter(path)
    assert len(path)==2*(sum(key)-1)
    assert tuple(cnt[i] for i in (1,2,3))==key
    assert tuple(cnt[i]-cnt[-i] for i in range(1,7))==(2,0,0,0,0,0)
    wc[h]+=1;u=0
    for step in path:
     if step not in child[u]:
      child[u][step]=len(child);child.append({});terminal.append(0);label.append({})
     u=child[u][step]
    z=bits[h,sig];terminal[u]|=z;label[u][z]=(h,sig,key,w)
 def merge(d,e):
  out=d.copy()
  for i,ci in d.items():
   for j,cj in e.items():
    if j and not i&j:
     z=i|j;v=ci+cj+1
     if v<out.get(z,INF):out[z]=v
  return out
 N=len(child);dp=[None]*N
 for u in range(N-1,-1,-1):
  mask=terminal[u];d={0:0}
  z=mask
  while z:d[z]=0;z=(z-1)&mask
  for v in child[u].values(): d=merge(d,dp[v])
  dp[u]=d
 ALL=255;optimal=dp[0][ALL]; chosen=[]
 def recover(u,target):
  vs=list(child[u].values());mask=terminal[u];d={0:0}
  z=mask
  while z:d[z]=0;z=(z-1)&mask
  pre=[d]
  for v in vs:d=merge(d,dp[v]);pre.append(d)
  assert d[target]==dp[u][target]
  remain=target
  for i in range(len(vs)-1,-1,-1):
   v=vs[i];pick=None
   for z,val in dp[v].items():
    if not z&~remain and remain^z in pre[i] and pre[i][remain^z]+(val+1 if z else 0)==pre[i+1][remain]:pick=z;break
   assert pick is not None
   if pick:recover(v,pick)
   remain^=pick
  assert not(remain&~mask)
  for z,datum in label[u].items():
   if z&remain:chosen.append(datum)
 recover(0,ALL)
 assert len(chosen)==8
 prefixes=set()
 for h,s,k,w in chosen:
  p=tuple(x for o in w for x in X[o])
  prefixes.update(p[:i] for i in range(1,len(p)+1))
 assert len(prefixes)==optimal
 upper=min(4*a+16+8*(b-a),4*b+30)
 assert optimal==upper,(a,b,optimal,upper)
 return dict(a=a,b=b,exact_cost=optimal,upper_extension=4*a+16+8*(b-a),
 upper_independent=4*b+30,legal_keys={str(h):len(list(keys(h))) for h in (a,b)},
 candidate_words={str(k):v for k,v in wc.items()},trie_nodes=N,
 witness=[dict(h=h,signature=s,key=k,word=w) for h,s,k,w in chosen])

def main():
 rows=[solve(a,b) for a,b in combinations(range(4,9),2)]
 print(json.dumps({'schema':'EC49FFS_TWO_WINDOW_EXACT_FINITE_V1',
 'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'model_blob':'6350340fbe869f17b5a50bd1ba30640db44a3a99',
 'domain':'all 10 pairs 4<=a<b<=8',
 'theorem':'Cmin(a,b)=min(4a+16+8(b-a),4b+30) over this finite domain',
 'proof':'exhaustive eligible key and operation-word enumeration; 256-mask signed-X6-prefix trie DP; direct witness check',
 'rows':rows},indent=2))
if __name__=='__main__':main()
