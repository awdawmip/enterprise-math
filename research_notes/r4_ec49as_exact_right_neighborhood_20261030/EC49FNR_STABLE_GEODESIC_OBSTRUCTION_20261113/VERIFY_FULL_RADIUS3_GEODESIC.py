#!/usr/bin/env python3
"""EC49FNR: exact eight shortest-path obstructions in the full 38169-case frozen family.
Inputs: archived frozen cases.json; EC49FNQ 11-byte-row vector; fourteen actual native scan lines.
"""
import base64,hashlib,itertools,json,lzma,sys
from collections import deque
from pathlib import Path
assert len(sys.argv)==4, "usage: python3 VERIFY_FULL_RADIUS3_GEODESIC.py cases.json EDGE_VECTOR_EC49FNP.u8x11.xz.b64 EXACT_14_GATEKEEPER_SCANS.txt"
casebytes=Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(casebytes).hexdigest()=="d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33"
d=json.loads(casebytes)
assert d["pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab" and d["count"]==38169
K=list(map(frozenset,d["cases"]))
assert len(K)==38169 and len(set(K))==38169 and all(len(k)==7 for k in K)
indices={k:i for i,k in enumerate(K)}
raw=lzma.decompress(base64.b64decode(Path(sys.argv[2]).read_text().strip(),validate=True))
assert len(raw)==11000 and hashlib.sha256(raw).hexdigest()=="4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b"
V={32000+i:tuple(raw[11*i+7:11*i+10]) for i in range(1000)}
assert all(K[32000+i]==frozenset(raw[11*i:11*i+7]) for i in range(1000))
native={37743:(144,1,145),37819:(144,1,145),37759:(152,1,153),37852:(152,1,153),
33714:(154,2,155),33157:(142,1,149),33256:(154,2,155),33716:(154,1,155),
33159:(148,1,155),33332:(154,1,155),33272:(154,1,155),33854:(154,1,155),
33365:(161,1,162),33856:(160,1,161)}
lines=Path(sys.argv[3]).read_text().splitlines()
assert len(lines)==14
done=set()
for line in lines:
 i,C,m,second=map(int,line.split()[:4])
 assert i in native and (C,m,second)==native[i] and i not in done
 done.add(i);V[i]=(C,m,second-C)
assert done==set(native)
A=[set() for _ in range(1000)]
for i in range(1000):
 for j in range(i+1,1000):
  if len(K[32000+i]-K[32000+j])==1 and V[32000+i]==V[32000+j]:
   A[i].add(j); A[j].add(i)
assert sum(map(len,A))//2==11574
def dist1000(src,dst):
 q=deque([(src-32000,0)]);seen={src-32000}
 while q:
  u,n=q.popleft()
  if u==dst-32000:return n
  for v in A[u]:
   if v not in seen:
    seen.add(v);q.append((v,n+1))
 return None
pairs2=[(32275,32703),(32276,32719),(32315,32353),(32318,32353)]
pairs3=[(32703,32951),(32703,32953),(32719,32961),(32719,32963)]
needed=set(); result=[]
for u,v in pairs2+pairs3:
 dropped=K[u]-K[v];inserted=K[v]-K[u];d=len(dropped)
 assert len(inserted)==d and d in (2,3) and V[u]==V[v]
 assert dist1000(u,v)==d+1
 levels={}
 for n in range(1,d):
  choices=[frozenset((K[u]-set(rem))|set(add))
           for rem in itertools.combinations(dropped,n)
           for add in itertools.combinations(inserted,n)]
  assert len(choices)==len(set(choices))==len(list(itertools.combinations(dropped,n)))**2
  rows=[]
  for k in choices:
   j=indices.get(k)
   if j is not None:
    assert j in V, ("MISSING_EXACT_NATIVE_VALUE",j)
    if not 32000<=j<33000:needed.add(j)
   rows.append((j,j is not None and V[j]==V[u]))
  levels[n]=rows
 # A shortest unrestricted Johnson path must use these monotone candidates.
 paths=[(u,)]
 for n in range(1,d):
  paths=[p+(j,) for p in paths for j,match in levels[n]
         if match and len(K[p[-1]]-K[j])==1]
 assert not paths, ("FOUND_UNEXPECTED_STABLE_JOHNSON_GEODESIC",u,v,paths)
 counts={str(n):{"absent":sum(j is None for j,_ in rows),
                  "wrong":sum(j is not None and not match for j,match in rows),
                  "matching":sum(match for _,match in rows),
                  "matching_ids":sorted(j for j,match in rows if match)}
         for n,rows in levels.items()}
 if d==2:assert counts["1"]["absent"]==1 and counts["1"]["wrong"]==3
 if d==3:
  assert all(counts[str(n)]["absent"]==4 and counts[str(n)]["wrong"]==4
             and counts[str(n)]["matching"]==1 for n in (1,2))
  x=counts["1"]["matching_ids"][0];y=counts["2"]["matching_ids"][0]
  assert len(K[x]-K[y])!=1
 result.append({"pair":[u,v],"triple":list(V[u]),"Johnson_distance":d,
                "full_family_stable_distance":d+1,"candidate_levels":counts})
assert needed==set(native)
print(json.dumps({"frozen_pin":d and "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
"case_count":38169,"native_new_cases":sorted(native),"exact_global_obstructions":result},
ensure_ascii=False,sort_keys=True,indent=2))
