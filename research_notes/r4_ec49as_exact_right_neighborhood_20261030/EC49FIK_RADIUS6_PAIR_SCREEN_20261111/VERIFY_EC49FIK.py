#!/usr/bin/env python3
"""Exact finite radius-six pairwise native-prefix BRC verifier."""
import argparse,collections,itertools,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,raw_key,pref,validate_profile
EXPECTED={('A',3):(9344,3740,5604,5604,0),('A',5):(4400,0,4400,3300,1100),
 ('A',7):(6582,5412,1170,390,780),('A',9):(8700,0,8700,8568,132),
 ('B',3):(9344,3740,5604,5604,0),('B',5):(4400,0,4400,3300,1100),
 ('B',7):(6582,5412,1170,390,780)}
def solve(profile,cat,B):
 rows,paths=validate_profile(profile); labs=[(r['window'],r['signature']) for r in rows]
 lidx={l:i for i,l in enumerate(labs)}; keys={raw_key(r['word']) for r in rows}
 support=collections.defaultdict(int);ksup=collections.defaultdict(int)
 for i,(r,pp) in enumerate(zip(rows,paths)):
  ksup[raw_key(r['word'])]|=1<<i
  for p in pp:support[p]|=1<<i
 assert len(keys)==7 and len(support)==94
 ids={};groups=collections.defaultdict(list)
 for l,w in cat:
  if raw_key(w) not in keys:continue
  pp=pref(w);bits=[]
  for p in pp:
   if p not in ids:ids[p]=len(ids)
   bits.append(1<<ids[p])
  groups[lidx[l]].append((tuple(support.get(p,0) for p in pp),bits,len(pp)))
 assert sum(map(len,groups.values()))==9838
 h2={i for i,(h,s) in enumerate(labs) if h==2}
 n=collections.Counter();failpairs=collections.Counter()
 for Q in itertools.combinations(range(24),6):
  if h2.intersection(Q):continue
  mask=sum(1<<j for j in Q)
  budget=sum((s&mask)==s for s in support.values())-1
  if budget!=B or any((s&mask)==s for s in ksup.values()):continue
  n['all']+=1;opts=[];no=False
  for j in Q:
   raw=set()
   for sup,edges,L in groups[j]:
    t=0
    while t<L and (sup[t]&~mask):t+=1
    if L-t<=B:raw.add(sum(edges[t:]))
   if not raw:no=True;break
   minimal=[]
   for candidate in sorted(raw,key=int.bit_count):
    if not any((old&candidate)==old for old in minimal):minimal.append(candidate)
   opts.append(tuple(minimal))
  if no:n['singleton_reject']+=1;continue
  n['singleton_pass']+=1;failed=None
  for (i,a),(j,b) in itertools.combinations(zip(Q,opts),2):
   if not any((x|y).bit_count()<=B for x in a for y in b):failed=(i,j);break
  if failed:n['pair_reject']+=1;failpairs[str(failed)]+=1
  else:n['pair_pass']+=1
 fields=('all','singleton_reject','singleton_pass','pair_reject','pair_pass')
 actual=tuple(n[x] for x in fields)
 assert actual==EXPECTED[(profile['profile_id'],B)],actual
 return {'profile':profile['profile_id'],'budget':B,'counts':dict(n),
         'first_bad_pair_hist':dict(failpairs),'legal_seven_key_words':9838,
         'native_prefix_bits':len(ids)}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--profile',choices=['A','B'],required=True)
 ap.add_argument('--budget',type=int,required=True);v=ap.parse_args()
 if (v.profile,v.budget) not in EXPECTED:ap.error('Unverified scope')
 cat=list(all_words());assert len(cat)==178850
 p=next(p for p in W['profiles'] if p['profile_id']==v.profile)
 print(json.dumps({'schema':'EC49FIK_PAIR_SCREEN_V1','frozen_pin':PIN,
                   'result':solve(p,cat,v.budget)},indent=2))
 print('EC49FIK_EXACT_PAIR_PASS')
