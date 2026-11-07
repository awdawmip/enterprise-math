#!/usr/bin/env python3
"""EC49FDT exact finite 3-late-BRC-key rank feasibility; Python standard library.
Predecessor: EC49FDS/EC49FAW; frozen input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json,itertools,collections
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
LETTERS='acdefg'
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
CLAUSES=(18,20,33,40)
states={(0,0,0,0,0,0,0):1}
by_h={};summary=[]
for h in range(1,10):
 nxt=collections.defaultdict(int)
 for state,num in states.items():
  for a in range(6):
   nw=list(state[:6]);nw[a]+=1;nw.append(TRANS[state[6]][a]);nxt[tuple(nw)]+=num
 states=nxt
 masks=collections.defaultdict(int);all_valid=all_accepted=0
 for state,num in states.items():
  na,nc,nd,ne,nf,ng,q=state
  if ne!=na+1:continue
  all_valid+=num
  s=SIG[q]
  if not s:continue
  all_accepted+=num
  z=ne;r=nc+nd;k=(2*z+r+nf,r+ng,z)
  masks[k]|=s
 by_h[h]=dict(masks)
 summary.append((h,all_valid,all_accepted,len(masks),sum(all(m&c for c in CLAUSES) for m in masks.values())))
assert summary[1:9]==[(2,8,6,3,1),(3,51,38,6,4),(4,304,206,13,9),(5,1770,1062,21,17),(6,10224,5352,34,28),(7,58947,26644,49,43),(8,340064,131686,70,62),(9,1964862,647930,94,86)]
keys=sorted(set().union(*(set(by_h[h]) for h in range(4,10))))
assert len(keys)==155
rank=lambda m: all(m&c for c in CLAUSES)
def good(pair):
 return all(rank(sum_mask(pair,h)) for h in range(4,10))
def sum_mask(seq,h):
 m=0
 for k in seq:m|=by_h[h].get(k,0)
 return m
pairs=[p for p in itertools.combinations(keys,2) if good(p)]
assert len(pairs)==124
triples=with_pair=only_three=0;examples=[]
for tri in itertools.combinations(keys,3):
 if not good(tri):continue
 triples+=1
 if any(good(pair) for pair in itertools.combinations(tri,2)):with_pair+=1
 else:
  only_three+=1
  if len(examples)<10:examples.append(tri)
assert (triples,with_pair,only_three)==(23728,16994,6734)
degrees=collections.Counter(k for pair in pairs for k in pair)
wedges=sum(d*(d-1)//2 for d in degrees.values())
assert wedges==1978 and with_pair==124*(155-2)-wedges
# A 3-cycle cannot exist: any feasible pair needs H4 and H9 witnesses,
# and no complete full key can be feasible at both horizons.
report={'schema':'EC49FDT_THREE_LATE_KEY_RANK_CENSUS_V1','science_pin':PIN,
'scope':'rank-nine only, H4..H9, 3-key subsets from signature-admissible complete keys; no path quotas/prefix costs',
'horizon_summary':summary,'allowed_late_keys':155,'pairs_rank_feasible':len(pairs),
'triples_total':len(keys)*(len(keys)-1)*(len(keys)-2)//6,
'triples_rank_feasible':triples,'triple_supersets_of_feasible_pair':with_pair,
'triples_genuinely_3_required':only_three,'wedges_of_feasible_pair_graph':wedges,
'first_ten_three_only_triples':examples}
print(json.dumps(report,indent=2))
