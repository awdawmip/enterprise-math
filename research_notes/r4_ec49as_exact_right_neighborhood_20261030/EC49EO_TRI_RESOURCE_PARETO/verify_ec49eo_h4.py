#!/usr/bin/env python3
"""Exact conditional H=4 optimization with M=2 and S=4 in original native-X6 system."""
import importlib.util, contextlib, io, itertools,json
from collections import defaultdict
spec=importlib.util.spec_from_file_location('v','/mnt/data/ec49eo/verify_ec49eo.py')
v=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(v)
ref={v.transfer(w):w for w in v.base}
p=(4,2,1,0,0,0)
groups={}
for h in (3,4):
 grouped=defaultdict(list)
 for tup in itertools.product('abcdefg',repeat=h):
  w=''.join(tup)
  if v.displacement(w)==(2,0,0,0,0,0) and v.counts(w)==p and v.transfer(w) in ref:
   grouped[ref[v.transfer(w)]].append(w)
 assert all(grouped[k] for k in v.base)
 groups[h]=grouped
# Build bitsets for all distinct native primitive edges across 8 groups and base.
allw=set(v.base)
for h in groups:
 for vs in groups[h].values(): allw.update(vs)
all_edges=sorted(v.edges(allw))
lookup={e:i for i,e in enumerate(all_edges)}
def bitw(w):return sum(1<<lookup[e] for e in v.edges((w,)))
bits={w:bitw(w) for w in allw}
base_bits=0
for w in v.base: base_bits|=bits[w]
min_E=999; best=None; done=0
order=list(v.base)
for ws3 in itertools.product(*(groups[3][key] for key in order)):
 m3=base_bits
 for w in ws3:m3|=bits[w]
 for ws4 in itertools.product(*(groups[4][key] for key in order)):
  mask=m3
  for w in ws4:mask|=bits[w]
  cost=mask.bit_count();done+=1
  if cost<min_E: min_E=cost;best=(ws3,ws4)
assert v.rank(best[0])==v.rank(best[1])==9
assert all(len({v.counts(w) for w in ws})==1 for ws in best)
assert len({v.transfer(w) for w in v.base+best[0]+best[1]})==4
report={ 'unit':'EC49EO-H4','status':'PASS','condition':'H4,M=2,S=4','minimum_E':min_E,
 'search_count':done,'group_sizes':{str(h):[len(groups[h][k]) for k in order] for h in (3,4)},
 'h2_words':v.base,'h3_words':best[0],'h4_words':best[1],
 'key_vectors':[v.counts(v.base[0]),v.counts(best[0][0])],
 'bound_proven':'Exact complete search of all one-per-base-signature representatives in sole p=(4,2,1) common h3/h4 positive fiber; additional words cannot lower union edge count.'}
print(json.dumps(report,indent=2))
