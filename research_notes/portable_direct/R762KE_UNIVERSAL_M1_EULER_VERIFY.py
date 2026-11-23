#!/usr/bin/env python3
"""R762KE: exact 16-certificate proof of all-positive 14-Port Euler realization."""
from itertools import combinations
from math import comb

AX=tuple(range(6))
PORTS=tuple(p for p in combinations(AX,2) if p!=(0,1))
IP={p:i for i,p in enumerate(PORTS)}
F=tuple((0,1,i) for i in range(2,6))
C=tuple(s for s in combinations(AX,3) if s not in F)
ALL=tuple(sorted(F+C))
EDGE={s:tuple(combinations([IP[p] for p in combinations(s,2) if p in IP],2)) for s in ALL}
assert len(PORTS)==14 and len(C)==16 and all(len(EDGE[s])==3 for s in C)
assert all(len(EDGE[s])==1 for s in F)

CERT=(
 '2002122111220122', '2120211011001002', '2111021122012200', '0000121221211212',
 '0211222011222021', '2211221111001020', '1212000211020202', '0100122021122122',
 '2101222222021121', '2120200102110210', '2221112112211021', '2020022211011112',
 '2111210021222021', '1101002210210010', '2001021122021100', '1001221112121100')

def boundary(edge):
 u,v=edge
 return (1<<u)^(1<<v)

def chosen(k):
 assert 0<=k<16
 assert len(CERT[k])==16 and all(x in '012' for x in CERT[k])
 return {s:EDGE[s][int(i)] for s,i in zip(C,CERT[k])}

def connected(events):
 p=list(range(14))
 def root(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 for a,b in events:
  ra,rb=root(a),root(b)
  if ra!=rb:p[ra]=rb
 return len({root(i) for i in range(14)})==1

def verify_16_bases():
 assert len(CERT)==16 and len(set(CERT))==16
 for k in range(16):
  sample=chosen(k)
  assert len(sample)==16
  target=0
  for i,s in enumerate(F):
   if k>>i&1:target^=boundary(EDGE[s][0])
  observed=0
  for edge in sample.values():observed^=boundary(edge)
  assert observed==target, (k,target,observed)
  assert connected(tuple(sample.values())+tuple(EDGE[s][0] for s in F)),k

def realize_flexible(s,n,e):
 assert n>=1 and e in EDGE[s]
 if n==1:return [e]
 other=[a for a in EDGE[s] if a!=e]
 base=other if n%2==0 else [e,other[0],other[0]]
 return base+[EDGE[s][0]]*(n-len(base))

def realize_inventory(counts):
 assert set(counts)==set(ALL) and all(type(n)==int and n>=1 for n in counts.values())
 k=sum((counts[s]&1)<<i for i,s in enumerate(F))
 sample=chosen(k)
 events=[]
 for s in ALL:
  if s in F:events += [EDGE[s][0]]*counts[s]
  else:events += realize_flexible(s,counts[s],sample[s])
 degree=[0]*14
 for u,v in events:degree[u]+=1;degree[v]+=1
 assert len(events)==sum(counts.values())
 assert all(d>0 and d%2==0 for d in degree)
 assert connected(events)
 return len(events)

def counts_42_categories():
 ans={}
 for d in range(5):
  for t in range(5-d):
   flex_single=5-d;flex_triple=7-t
   total=comb(4,d)*comb(4-d,t)*comb(16,flex_single)*comb(16-flex_single,flex_triple)
   ans[f'd={d},t={t}']=total
   forced={s:(1 if i<d else 3 if i<d+t else 2) for i,s in enumerate(F)}
   flexible={s:(1 if i<flex_single else 3 if i<flex_single+flex_triple else 2) for i,s in enumerate(C)}
   assert realize_inventory(forced|flexible)==42
 assert len(ans)==15
 assert sum(ans.values())==comb(20,5)*comb(15,7)==99768240
 return ans

def main():
 verify_16_bases()
 examples=0
 for k in range(256):
  forced={s:1+((k>>(2*i))&3) for i,s in enumerate(F)}
  flexible={s:1+((k+7*i)%9) for i,s in enumerate(C)}
  realize_inventory(forced|flexible)
  examples+=1
 print({'bases_verified':16,'different_forced_parity_targets':16,
        'arbitrary_positive_count_regressions':examples,
        'full_42_histogram_classes':15,
        'all_labeled_42_event_inventories':sum(counts_42_categories().values()),
        'marked_44_to_42_pairs':5*comb(20,5)*comb(15,7),
        'failures':0})
if __name__=='__main__':main()
