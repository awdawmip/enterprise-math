#!/usr/bin/env python3
"""Independent native-code cost-subset DP (not C++ pair_group recurrence)."""
from functools import cache
import json,sys
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
OBS=(0,0,4,1,16,32,8,2,0)
OP='acdefg';length=(2,4,4,4,2,2);INF=100000
GROUPS=((0,),(1,4),(2,5),(3,))
BL={'':frozenset((1,2,3)),'c':frozenset((3,)),'d':frozenset((3,)),'e':frozenset((1,2))}
def score(S):
 return sum(length[j] for j in S)-int(1 in S and 4 in S)-int(2 in S and 5 in S)
def run(h):
 @cache
 def valid(k,e,a,f,q):
  if 2*e+f>h or abs(e-a-1)>h-k:return False
  if k==h:return e==a+1 and e>=1 and OBS[q] in (1,2,4,8)
  return any(valid(k+1,e+(j==3),a+(j==0),f+(j==4),T[q][j]) for j in range(6))
 @cache
 def solve(k,e,a,f,q,prefix):
  row=[INF]*16;row[0]=0
  if k==h:
   row[1<<(1,2,4,8).index(OBS[q])]=0;return tuple(row)
  child={}
  for j in range(6):
   E,A,F=e+(j==3),a+(j==0),f+(j==4);Q=T[q][j]
   if valid(k+1,E,A,F,Q):child[j]=solve(k+1,E,A,F,Q,OP[j] if k==0 else 'x')
  base=BL.get(prefix,frozenset())
  for group in GROUPS:
   opts=[(0,0)]
   if len(group)==1:
    j=group[0]
    if j in child:
     opts.extend((mask,child[j][mask]+score(base|{j})-score(base)) for mask in range(1,16) if child[j][mask]<INF)
   else:
    j,t=group
    for x in range(16):
     if x and (j not in child or child[j][x]>=INF):continue
     for y in range(16):
      if (x&y) or (not(x or y)) or (y and (t not in child or child[t][y]>=INF)):continue
      selected={z for z,m in ((j,x),(t,y)) if m}
      opts.append((x|y,(child[j][x] if x else 0)+(child[t][y] if y else 0)+score(base|selected)-score(base)))
   new=row[:]
   for mask,v in enumerate(row):
    if v>=INF:continue
    for om,cost in opts:
     if (mask&om)==0 and v+cost<new[mask|om]:new[mask|om]=v+cost
   row=new
  return tuple(row)
 answer=28+solve(0,0,0,0,0,'')[15]
 return {'h':h,'exact_cost':answer,'cached_rows':solve.cache_info().currsize}
if __name__=='__main__':
 for h in map(int,sys.argv[1:]):print(json.dumps(run(h)))