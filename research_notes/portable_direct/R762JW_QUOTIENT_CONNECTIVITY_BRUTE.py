#!/usr/bin/env python3
"""Independent exhaustive quotient parity and connectivity screen.
Finite model: support graph quotient only; this does NOT show a realizable Euler multigraph.
"""
from itertools import combinations,product
from collections import Counter
import json
P=list(combinations(range(6),2));S=list(combinations(range(6),3));portid={p:i for i,p in enumerate(P)}
triangles=[tuple(portid[x] for x in combinations(s,2)) for s in S]
inactive=[(),(0,),(0,9),(0,9,14)]  # check index pairs: 01=0,23=9,45=14
assert [P[i] for i in inactive[3]]==[(0,1),(2,3),(4,5)]

def cover(m,ds):
  M=set(inactive[m]); V=[i for i in range(15) if i not in M]; A=set(V)
  parent={i:i for i in V}
  def root(x):
    while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
    return x
  def merge(x,y):
    rx,ry=root(x),root(y)
    if rx!=ry:parent[ry]=rx
  DS=set(ds)
  for k,tri in enumerate(triangles):
    if k not in DS and all(i in A for i in tri):
      merge(tri[0],tri[1]); merge(tri[1],tri[2])
  unique=sorted(set(root(v) for v in V))
  label={p:unique.index(root(p)) for p in V}
  c=len(unique)
  if c==1:return 1,True,True,0,0
  choice=[]; fixed=[]
  for k,tri in enumerate(triangles):
    active=[v for v in tri if v in A]
    if k in DS: choice.append([(label[u],label[v]) for u,v in combinations(active,2)])
    elif len(active)==2: fixed.append((label[active[0]],label[active[1]]))
  assert len(choice)==5
  outcomes=set(); connected=set()
  for selected in product(*choice):
    cur=[i for i in range(c)]
    def find(x):
      while x!=cur[x]:x=cur[x]
      return x
    for u,v in fixed+list(selected):
      ru,rv=find(u),find(v)
      if ru!=rv:cur[ru]=rv
    q=0
    for u,v in selected:q^=(1<<u)^(1<<v)
    outcomes.add(q)
    if len({find(i) for i in range(c)})==1: connected.add(q)
  even={q for q in range(1<<c) if q.bit_count()%2==0}
  return c,outcomes>=even,connected>=even,len(outcomes),len(connected)

def main():
  rows=[]
  for m in range(4):
    c_hist=Counter();connected_fail=0;parity_fail=0;first=None;connected_good=0
    for ds in combinations(range(20),5):
      c,parity,conn,pn,cn=cover(m,ds)
      c_hist[c]+=1
      if not parity:parity_fail+=1
      if conn:connected_good+=1
      else:
        connected_fail+=1
        if first is None:first={'D':[''.join(map(str,S[x])) for x in ds], 'c':c,'parity_cover_count':pn,'connected_cover_count':cn,'all_parity_count':2**(c-1)}
    row={'m':m,'component_counts':dict(c_hist),'parity_fail':parity_fail,'connected_fail':connected_fail,'connected_good':connected_good,'first_connected_failure':first}
    print(row,flush=True);rows.append(row)
  with open('/mnt/data/r762jw_connectivity.json','w') as f:json.dump({'schema':'R762JW_INDEPENDENT_QUOTIENT_CONNECTION_SCREEN_V1','rows':rows},f,indent=2)
if __name__=='__main__':main()
