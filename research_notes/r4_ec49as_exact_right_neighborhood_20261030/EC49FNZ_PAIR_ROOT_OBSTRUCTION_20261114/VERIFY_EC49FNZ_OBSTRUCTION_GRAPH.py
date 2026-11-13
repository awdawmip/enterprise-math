#!/usr/bin/env python3
"""Exact per-demand and per-pair root-cover forcing graph for nine frozen FNY cuts.

Needs VERIFY_EC49FNY_INDEPENDENT.py from the immutable EC49FNY evidence
archive in the same directory; the original native master file and 198-row
FNY certificate are command-line arguments. Does not reuse C++ DP tables.
"""
import itertools,sys,hashlib
from pathlib import Path
import VERIFY_EC49FNY_INDEPENDENT as old
ROOTS=old.ROOTS
master=Path(sys.argv[1]); cert=Path(sys.argv[2]);
assert hashlib.sha256(master.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
words,keys=old.frozen(master)
prof={r:old.table(words,keys,r) for r in ROOTS}
opts={l:[r for r in ROOTS if l in prof[r][1]] for l in range(24)}
# Local root-cost oracle, preserving distinct label and root types.
def cost(masks):
 out=0
 for pos,r in enumerate(ROOTS):
  ix=prof[r][1]; f=prof[r][2]; m=0
  for l in range(24):
   if masks[pos]>>l&1: m|=1<<ix[l]
  out+=f[m]
 return out

def with_assign(masks,labels,rs):
 arr=list(masks)
 for l,r in zip(labels,rs):arr[ROOTS.index(r)]|=1<<l
 return cost(arr)

rows={}
for line in cert.read_text().splitlines():
 if not line.startswith('WITNESS '):continue
 spl=line.split();k=(spl[3],tuple(map(int,spl[-4:])))
 rows[k]=spl
assert len(rows)==9
print('GRAPH_EXACT_BASELINE frozen_master='+hashlib.sha256(master.read_bytes()).hexdigest()+' count=9')
patterns=[]
for (enc,masks),p in rows.items():
 _,src,tgt,_,src_lb,target_lb,B,h1,l1,h2,l21,l22,*_=p
 base=cost(masks);B=int(B);unassigned=[l for l in range(24) if not any(mask>>l&1 for mask in masks)]
 single={l:min(with_assign(masks,(l,),(r,)) for r in opts[l]) for l in unassigned}
 pair={(i,j):min(with_assign(masks,(i,j),(ri,rj)) for ri in opts[i] for rj in opts[j]) for i,j in itertools.combinations(unassigned,2)}
 assert base==int(target_lb) and max(single.values())==int(h1) and (max(pair.values()) if pair else max(single.values()))==int(h2)
 forcing=[(i,j,val) for (i,j),val in pair.items() if val>B]
 single_force=[(l,x) for l,x in single.items() if x>B]
 top_pairs=[(i,j) for (i,j),v in pair.items() if v==max(pair.values())]
 top_singles=[l for l,v in single.items() if v==max(single.values())]
 # A pair is novel irreducible if neither singleton itself forces.
 irreducible=[(i,j,v) for i,j,v in forcing if single[i]<=B and single[j]<=B]
 patterns.append({'enc':enc,'base':base,'h1':int(h1),'h2':int(h2),'u':len(unassigned),'p':len(pair),'forcing':len(forcing),'strict_irreducible':len(irreducible),'top_pairs':top_pairs,'top_singles':top_singles,'irreducible':irreducible,'singles':single,'pairs':pair,'masks':masks})
 print('PATTERN',enc,'base',base,'unassigned',len(unassigned),'pair_count',len(pair),'H1',h1,'H2',h2,'forcing_singletons',single_force,'forcing_pairs',len(forcing),'irreducible_pairs',irreducible,'top_pairs',top_pairs,'top_singles',top_singles)
 if irreducible:
  for i,j,v in irreducible:
   print('IRREDUCIBLE_MATRIX',enc,'labels',i,j,'rows',opts[i],'cols',opts[j],'values',[[with_assign(masks,(i,j),(ri,rj)) for rj in opts[j]] for ri in opts[i]],'single_roots',[(i,[(r,with_assign(masks,(i,),(r,))) for r in opts[i]]),(j,[(r,with_assign(masks,(j,),(r,))) for r in opts[j]])])
pair_deltas=[h-(row['singles'][i]+row['singles'][j]-row['base']) for row in patterns for (i,j),h in row['pairs'].items()]
assert sorted(pair_deltas)==[-1]+[0]*10
special=next(row for row in patterns if row['enc']=='159571690231449')
assert special['base']==153 and special['singles'][17]==161 and special['singles'][21]==157 and special['pairs'][(17,21)]==164
M=[[with_assign(special['masks'],(17,21),(r,s)) for s in opts[21]] for r in opts[17]]
assert opts[17]==[3,6,7] and opts[21]==[3,6,7]
assert M==[[164,165,173],[169,165,174],[172,169,168]]
print('ROOT_SHARING_COUNTEREXAMPLE',special['enc'],'labels',(17,21),'baseline',153,'single_minima',(161,157),'distinct_min_cost',165,'same_root_03',164,'matrix',M)
print('PAIR_ADDITIVITY_CENSUS equal=10 subadditive_by_one=1 superadditive=0')
assert sum(x['h1']<=155 for x in patterns)==2
print('SUMMARY pair_total',sum(x['p'] for x in patterns),'forcing_total',sum(x['forcing'] for x in patterns),'irreducible_total',sum(x['strict_irreducible'] for x in patterns))
print('TOP_PAIR_UNION',sorted(set(q for x in patterns for q in x['top_pairs'])))

assert sorted(x['u'] for x in patterns)==[1,1,2,2,2,2,2,3,3]
assert sum(x['p'] for x in patterns)==11
assert sum(x['forcing'] for x in patterns)==11
assert sum(x['strict_irreducible'] for x in patterns)==2
assert sorted(x['base'] for x in patterns if x['strict_irreducible'])==[150,152]
assert all(set(x['top_pairs']).issubset({(17,19),(17,21),(19,21)}) for x in patterns)
print('EC49FNZ_EXACT_CHECK_PASS patterns=9 singles=2 doubles=5 triples=2 pairs=11 forcing=11 irreducible=2')
