#!/usr/bin/env python3
"""Exact frozen BRC catalogue; enumerate d=5 two-key neighborhood."""
import json,sys,itertools,collections
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import all_words,raw_key,pref,PIN
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
cat=list(all_words());assert len(cat)==178850
labs=sorted({lab for lab,w in cat});ids={lab:i for i,lab in enumerate(labs)}
assert len(labs)==24
bykey=collections.defaultdict(list);cov={};roots_by_key=collections.defaultdict(set)
for lab,w in cat:
 k=raw_key(w);steps=pref(w)[-1].hex()
 bykey[k].append((ids[lab],steps))
 cov[k]=cov.get(k,0)|(1<<ids[lab]);roots_by_key[k].add(steps[:2])
keys=sorted(cov);assert len(keys)==94
base={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
full=(1<<24)-1
counts=collections.Counter();cases=[]
for rem in itertools.combinations(sorted(base),2):
 kept=base-set(rem);leftcov=0
 for k in kept:leftcov|=cov[k]
 for add in itertools.combinations([k for k in keys if k not in base],2):
  def dist(a,b):return sum(abs(x-y) for x,y in zip(a,b))
  d=min(dist(rem[0],add[0])+dist(rem[1],add[1]),dist(rem[0],add[1])+dist(rem[1],add[0]))
  if d!=5:continue
  cover=(leftcov|cov[add[0]]|cov[add[1]])==full
  counts['total_d5']+=1;counts['cover_d5' if cover else 'uncovered_d5']+=1
  if cover:
   ks=sorted(kept|set(add));roots=set().union(*(roots_by_key[k] for k in ks))
   cases.append({'removed':[list(t) for t in rem],'added':[list(t) for t in add],
                 'keyset':[list(t) for t in ks],'roots':sorted(roots),'n_roots':len(roots),'d':d})
cases.sort(key=lambda a:(a['n_roots'],a['removed'],a['added']))
counts['roots']=dict(collections.Counter(c['n_roots'] for c in cases))
assert (counts['total_d5'],counts['cover_d5'],counts['uncovered_d5'])==(2305,473,1832)
assert counts['roots']=={3:210,4:263}
(P/'EC49FLC_CASE_INDEX.json').write_text(json.dumps({'frozen_pin':PIN,'count':dict(counts),'cases':cases},indent=2)+'\n')
with (P/'EC49FLC_CASES.txt').open('w') as f:
 f.write(str(len(cases))+'\n')
 for case in cases:
  rows=[r for k in map(tuple,case['keyset']) for r in bykey[k]]
  f.write(str(len(rows))+'\n')
  for lab,s in rows:f.write(str(lab)+' '+s+'\n')
print('EC49FLC_GENERATION_PASS',json.dumps(dict(counts)),flush=True)
