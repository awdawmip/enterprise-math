#!/usr/bin/env python3
"""R762IK exact S6-orbit and constructive Euler witness checker (integer arithmetic).

The verified domain is the eleven high-count k=0 histogram families (plus the 14-port exception).
Every returned Port-edge multiset is checked for support counts, degree parity,
all fifteen active ports, and connectedness. Axis permutations transport it
through each complete orbit. Requires Python 3 standard library only.
"""
from itertools import combinations, permutations, product
from collections import Counter, defaultdict
P=list(combinations(range(6),2));S=list(combinations(range(6),3));pidx={p:i for i,p in enumerate(P)};sidx={s:i for i,s in enumerate(S)};TRI=[tuple(pidx[p] for p in combinations(s,2)) for s in S]
EDGES=[tuple(combinations(TRI[s],2)) for s in range(20)]
edge_to_s={tuple(sorted(e)):s for s in range(20) for e in EDGES[s]}
assert len(edge_to_s)==60
PERMS=[tuple(sidx[tuple(sorted(g[i] for i in s))] for s in S) for g in permutations(range(6))]

def parity_edge(a,b):return (1<<a)^(1<<b)
def possible_paths(s,edge,allowed,inactive_port=None):
 a,b=edge;out=[]
 for w in range(15):
  if w in edge or w==inactive_port:continue
  e1=tuple(sorted((a,w)));e2=tuple(sorted((w,b)))
  if inactive_port in e1 or inactive_port in e2:continue
  if e1 not in edge_to_s or e2 not in edge_to_s:continue
  s1=edge_to_s[e1];s2=edge_to_s[e2]
  if s1 not in allowed or s2 not in allowed:continue
  out.append(((s1,e1),(s2,e2)))
 return out

def assign(odd,even,missing,targets,defect_edges,paths,inactive_port=None):
 allS=set(range(20))-set(missing)
 full=allS-set(odd)-set(even)-set(targets)
 changed=defaultdict(int)
 for path in paths:
  for s,e in path:changed[s]^=parity_edge(*e)
 edges=[]
 for s in full:
  parity=changed[s]
  if parity==0:
   edges.extend((s,*e) for e in EDGES[s])
  else:
   oddedges=[e for e in EDGES[s] if parity_edge(*e)==parity]
   assert len(oddedges)==1
   oe=oddedges[0];ee=next(e for e in EDGES[s] if e!=oe)
   edges.extend([(s,*oe),(s,*ee),(s,*ee)])
 for s in even:
  choice=next(e for e in EDGES[s] if inactive_port is None or inactive_port not in e)
  edges.extend([(s,*choice)]*2)
 for s in tuple(odd)+tuple(targets):edges.append((s,*defect_edges[s]))
 cnt=Counter(s for s,a,b in edges)
 assert all(cnt[s] == (1 if s in odd or s in targets else 2 if s in even else 3) for s in allS)
 assert len(cnt)==len(allS)
 assert not any(sum(int((a==v)+(b==v)) for s,a,b in edges)%2 for v in range(15))
 g=[set() for _ in P]
 for s,a,b in edges:g[a].add(b);g[b].add(a)
 active={v for s,a,b in edges for v in (a,b)}
 if inactive_port is None and len(active)!=15:return None
 if inactive_port is not None and (inactive_port in active or len(active)!=14):return None
 start=next(iter(active));stack=[start];seen={start}
 while stack:
  for v in g[stack.pop()]:
   if v not in seen:seen.add(v);stack.append(v)
 if seen != active:return None
 return edges

def solve(odd=(),even=(),missing=(),inactive_port=None):
 allS=set(range(20))-set(missing)
 full=allS-set(odd)-set(even)
 original=sum(1 if s in odd else 2 if s in even else 3 for s in allS)
 nremove=max(0,(original-55+1)//2)
 if nremove==0:return None
 for targets in combinations(sorted(full),nremove):
  allowed=full-set(targets)
  defects=tuple(odd)+tuple(targets)
  for es in product(*(tuple(e for e in EDGES[s] if inactive_port is None or inactive_port not in e) for s in defects)):
   de=dict(zip(defects,es))
   path_opts=[possible_paths(s,e,allowed,inactive_port) for s,e in zip(defects,es)]
   if any(not opts for opts in path_opts):continue
   for pp in product(*path_opts):
    arr=assign(odd,even,missing,targets,de,pp,inactive_port)
    if arr is not None:return {'odd':odd,'even':even,'missing':missing,'targets':targets,'defects':de,'paths':pp,'edges':arr,'original':original,'new':len(arr)}
 return None

def orbit_reps(groups):
 space=set(tuple(tuple(g) for g in entry) for entry in groups)
 result=[]
 while space:
  rep=min(space); orb={tuple(tuple(sorted(g[i] for i in group)) for group in rep) for g in PERMS}
  assert orb<=space
  space.difference_update(orb)
  result.append((rep,len(orb)))
 return result

CASES=[('T20',[((),(),())]),('E1',[((),(i,),()) for i in range(20)]),('E2',[((),c,()) for c in combinations(range(20),2)]),('E3',[((),c,()) for c in combinations(range(20),3)]),('U1',[((i,),(),()) for i in range(20)]),('U1E1',[((i,),(j,),()) for i in range(20) for j in range(20) if i!=j]),('M1',[((),(),(i,)) for i in range(20)]),('E4',[((),c,()) for c in combinations(range(20),4)]),('U2',[(c,(),()) for c in combinations(range(20),2)]),('U1E2',[((i,),tuple(j),()) for i in range(20) for j in combinations([x for x in range(20) if x!=i],2)]),('M1E1',[((),(j,),(i,)) for i in range(20) for j in range(20) if j!=i])]

TOTAL=0
for name,arr in CASES:
 orbits=orbit_reps(arr)
 print('FAMILY',name,'objects',len(arr),'orbits',len(orbits),'sizes',[n for x,n in orbits],flush=True)
 for rep,n in orbits:
  ans=solve(*rep)
  print(' ',name,rep,'orbit_size',n,'answer',bool(ans),'original',ans['original'] if ans else None,'new',ans['new'] if ans else None,'targets',ans['targets'] if ans else None,flush=True)
  if ans is None:raise RuntimeError((name,rep))
  TOTAL+=n
assert TOTAL == 10606
# Exceptional 14-active-Port source: the only four non-T supports are
# the four supports incident to one pair-port, whose vertex can be unused.
# With E4 = 012,013,014,015 (indices 0,1,2,3), Port 01 is index 0.
exception = solve(even=(0,1,2,3), inactive_port=pidx[(0,1)])
assert exception is not None and exception['new'] <= 55
print('14-active-Port exceptional E4 orbit:', 'original', exception['original'],
      'new', exception['new'], 'targets', exception['targets'])
print('PASS R762IK: 56 S6 representative Euler witnesses cover', TOTAL, 'histograms')
