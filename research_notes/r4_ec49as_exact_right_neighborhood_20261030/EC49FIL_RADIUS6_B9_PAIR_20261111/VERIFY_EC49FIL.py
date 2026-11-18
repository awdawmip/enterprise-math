#!/usr/bin/env python3
"""Exact B9 pairwise native-prefix filter for radius-six B witness.
Science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import collections,itertools,json,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,raw_key,pref,validate_profile
B=9

def solve(profile,catalog):
 rows, paths = validate_profile(profile)
 labs=[(r['window'],r['signature']) for r in rows]
 lidx={lab:i for i,lab in enumerate(labs)}
 keys={raw_key(r['word']) for r in rows}
 supports=collections.defaultdict(int); key_supports=collections.defaultdict(int)
 for i,(r,ps) in enumerate(zip(rows,paths)):
  key_supports[raw_key(r['word'])]|=1<<i
  for p in ps:supports[p]|=1<<i
 assert len(keys)==7 and len(supports)==94
 ids={}; groups=collections.defaultdict(list)
 for lab,word in catalog:
  if raw_key(word) not in keys:continue
  ps=pref(word); bits=[]
  for p in ps:
   if p not in ids:ids[p]=len(ids)
   bits.append(1<<ids[p])
  groups[lidx[lab]].append((tuple(supports.get(p,0) for p in ps),bits,len(ps)))
 assert sum(map(len,groups.values()))==9838
 h2={i for i,(h,s) in enumerate(labs) if h==2}
 counters=collections.Counter(); fail_pairs=collections.Counter(); surviving=[]
 for Q in itertools.combinations(range(24),6):
  if h2.intersection(Q):continue
  mask=sum(1<<j for j in Q)
  budget=sum((s&mask)==s for s in supports.values())-1
  if budget!=B or any((s&mask)==s for s in key_supports.values()):continue
  counters['all']+=1; opts=[]; single_failed=False
  for j in Q:
   raw=set()
   for sup,bits,L in groups[j]:
    t=0
    while t<L and (sup[t]&~mask):t+=1
    if L-t<=B:raw.add(sum(bits[t:]))
   if not raw:single_failed=True;break
   minimal=[]
   for x in sorted(raw,key=int.bit_count):
    if not any((m & x)==m for m in minimal):minimal.append(x)
   opts.append(tuple(minimal))
  if single_failed:counters['singleton_reject']+=1;continue
  counters['singleton_pass']+=1; failed=None
  for (i,a),(j,b) in itertools.combinations(zip(Q,opts),2):
   if not any((x|y).bit_count()<=B for x in a for y in b):failed=(i,j);break
  if failed:counters['pair_reject']+=1;fail_pairs[str(failed)]+=1
  else:
   counters['pair_pass']+=1
   surviving.append(Q)
 return {'schema':'EC49FIL_RADIUS6_B9_PAIR_EXACT_V1','science_pin':PIN,'profile':profile['profile_id'],
         'budget':B,'cases_checked':counters['all'],'counts':dict(counters),
         'first_pair_failure':dict(fail_pairs),'survivors':[list(Q) for Q in surviving],
         'native_prefix_bits':len(ids),'legal_words_using_7_keys':9838}

if __name__=='__main__':
 start=time.time()
 catalog=list(all_words());assert len(catalog)==178850
 p=next(p for p in W['profiles'] if p['profile_id']=='B')
 res=solve(p,catalog)
 res['elapsed_seconds']=round(time.time()-start,3)
 target=HERE/'EXACT_REPORT_EC49FIL.json'
 target.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
 print({k:v for k,v in res.items() if k not in ('first_pair_failure','survivors')})
 print('survivors count',len(res['survivors']),'first_bad_pair',res['first_pair_failure'])
