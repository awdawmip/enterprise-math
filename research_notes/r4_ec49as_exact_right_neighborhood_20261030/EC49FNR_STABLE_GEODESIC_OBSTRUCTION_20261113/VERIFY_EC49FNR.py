#!/usr/bin/env python3
"""Exact EC49FNR graph theorem; accepts the immutable EC49FNQ vector as argv[1].
No native optimization is repeated; all arithmetic is finite integer/set arithmetic.
"""
import base64,collections,hashlib,itertools,json,lzma,sys
from pathlib import Path
from collections import Counter,defaultdict,deque
assert len(sys.argv)==2, 'usage: python VERIFY_EC49FNR.py EDGE_VECTOR_EC49FNP.u8x11.xz.b64'
raw=lzma.decompress(base64.b64decode(Path(sys.argv[1]).read_text().strip(),validate=True))
assert len(raw)==11000
assert hashlib.sha256(raw).hexdigest()=='4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b'
rows=[tuple(raw[11*i:11*(i+1)]) for i in range(1000)]
keys=[frozenset(r[:7]) for r in rows]; triple=[tuple(r[7:10]) for r in rows]
assert len(set(keys))==1000 and all(len(k)==7 for k in keys)
# Exhaustive Johnson adjacency checked against independent six-subset index.
E={(i,j) for i in range(1000) for j in range(i+1,1000) if len(keys[i]-keys[j])==1}
index=defaultdict(list)
for i,k in enumerate(keys):
 for subset in itertools.combinations(sorted(k),6): index[subset].append(i)
E2=set()
for ids in index.values():
 E2.update(tuple(sorted((i,j))) for i,j in itertools.combinations(ids,2))
assert E==E2 and len(E)==27942
adj=[set() for _ in keys]
for i,j in E:
 if triple[i]==triple[j]:adj[i].add(j);adj[j].add(i)
assert sum(map(len,adj))//2==11574
# Independent reachability layers: first arrivals at graph distances 1..4.
layer1=[set(x) for x in adj]
layer2=[set().union(*(adj[j] for j in layer1[i]))-{i}-layer1[i] if layer1[i] else set() for i in range(1000)]
layer3=[set().union(*(adj[j] for j in layer2[i]))-{i}-layer1[i]-layer2[i] if layer2[i] else set() for i in range(1000)]
layer4=[set().union(*(adj[j] for j in layer3[i]))-{i}-layer1[i]-layer2[i]-layer3[i] if layer3[i] else set() for i in range(1000)]
by_pair=Counter(); exceptions=[]
for i in range(1000):
 for distance,layer in enumerate((layer1,layer2,layer3,layer4),1):
  for j in layer[i]:
   if j<=i:continue
   d=len(keys[i]-keys[j]);by_pair[(d,distance)]+=1
   if distance>d:exceptions.append([32000+i,32000+j,d,distance,list(triple[i])])
assert dict(by_pair)=={(1,1):11574,(2,2):4814,(2,3):4,(3,3):162,(3,4):4}
assert len(exceptions)==8 and all(e[3]-e[2]==1 for e in exceptions)
# All four length-2 Johnson intermediates of each dJ=2,dG=3 pair fail stability.
ids={k:i for i,k in enumerate(keys)}
blocked=[]
for i0,j0,d,dist,sig in exceptions:
 if d!=2:continue
 i=i0-32000;j=j0-32000
 mids=[ids.get(frozenset((keys[i]-{o})|{n})) for o in keys[i]-keys[j] for n in keys[j]-keys[i]]
 assert len(mids)==4
 missing=sum(t is None for t in mids)
 wrong=sum(t is not None and triple[t]!=triple[i] for t in mids)
 blocked.append([i0,j0,missing,wrong])
assert len(blocked)==4 and all(m==1 and w==3 for _,_,m,w in blocked)
# Independent BFS component census, including disconnected and isolated vertices.
visited=set(); total=0
for start in range(1000):
 if start in visited:continue
 q=[start];visited.add(start)
 for x in q:
  for y in adj[x]:
   if y not in visited:visited.add(y);q.append(y)
 total+=len(q)*(len(q)-1)//2
assert total==16558==sum(by_pair.values())
result={'input_sha256':hashlib.sha256(raw).hexdigest(),'connected_pairs':total,
 'distance_histogram':{f'{a},{b}':count for (a,b),count in sorted(by_pair.items())},
 'isometric_pairs':16550,'strict_detour_pairs':8,'max_detour_excess':1,
 'exceptions':sorted(exceptions),'blocked_two_step_intermediates':sorted(blocked)}
print(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False))
