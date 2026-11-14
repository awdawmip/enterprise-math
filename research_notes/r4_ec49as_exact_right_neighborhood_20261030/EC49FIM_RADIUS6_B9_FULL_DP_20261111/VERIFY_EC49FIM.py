#!/usr/bin/env python3
"""Exact 6-demand feasibility on B9 pair-screen survivors, frozen signed-X6 BRC catalog."""
import argparse,base64,collections,gzip,json,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,raw_key,pref,validate_profile
B=9

def minimal_sets(sets):
 # Exact subset dominance; a smaller prefix-union always substitutes the larger.
 kept=[]
 for v in sorted(set(sets),key=int.bit_count):
  if not any((u&v)==u for u in kept): kept.append(v)
 return kept

def solve(profile_id):
 full=list(all_words());assert len(full)==178850
 p=next(p for p in W['profiles'] if p['profile_id']==profile_id)
 rows,paths=validate_profile(p);labs=[(r['window'],r['signature']) for r in rows]
 lidx={lab:i for i,lab in enumerate(labs)}
 keys={raw_key(r['word']) for r in rows}
 sup=collections.defaultdict(int);ksup=collections.defaultdict(int)
 for i,(row,prefs) in enumerate(zip(rows,paths)):
  ksup[raw_key(row['word'])]|=1<<i
  for e in prefs:sup[e]|=1<<i
 ids={};groups=collections.defaultdict(list)
 for lab,w in full:
  if raw_key(w) not in keys:continue
  ps=pref(w);bits=[]
  for e in ps:
   if e not in ids:ids[e]=len(ids)
   bits.append(1<<ids[e])
  groups[lidx[lab]].append((tuple(sup.get(e,0) for e in ps),bits,len(ps)))
 assert sum(map(len,groups.values()))==9838
 fil_report='EXACT_REPORT_EC49FIL_A.json' if profile_id=='A' else 'EXACT_REPORT_EC49FIL.json'
 f=HERE/fil_report
 if f.exists():previous=json.loads(f.read_text())
 else:previous=json.loads(gzip.decompress(base64.b64decode((HERE/(fil_report+'.gz.b64')).read_text().strip())))
 asserts=[];witnesses=[];stats=[]
 for Q in previous['survivors']:
  mask=sum(1<<j for j in Q)
  assert sum((s&mask)==s for s in sup.values())-1==B
  assert not any((s&mask)==s for s in ksup.values())
  candidates=[]
  for j in Q:
   raw=set()
   for support,es,L in groups[j]:
    t=0
    while t<L and support[t]&~mask:t+=1
    if L-t<=B:raw.add(sum(es[t:]))
   opts=minimal_sets(raw)
   assert opts
   candidates.append((j,opts))
  candidates.sort(key=lambda a:len(a[1]))
  states=[0];trace=[]
  for j,opts in candidates:
   next_states=set()
   for v in states:
    for d in opts:
     U=v|d
     if U.bit_count()<=B:next_states.add(U)
   states=minimal_sets(next_states)
   trace.append({'label_index':j,'options':len(opts),'states':len(states)})
   if not states:break
  if len(trace)==6 and states:witnesses.append({'Q':Q,'min_union_upper_bound':min(v.bit_count() for v in states)})
  else:asserts.append({'Q':Q,'failed_at_depth':len(trace),'trace':trace})
  stats.append({'Q':Q,'trace':trace})
 assert len(witnesses)+len(asserts)==132
 return {'schema':'EC49FIM_B9_SIX_WAY_EXACT_V1','frozen_pin':PIN,'profile':profile_id,'input_cases':132,
 'impossible':len(asserts),'possible':len(witnesses),'witnesses':witnesses,
 'failed_depth_hist':dict(collections.Counter(x['failed_at_depth'] for x in asserts)),
 'trace':stats}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--profile',choices=['A','B'],required=True)
 args=parser.parse_args()
 start=time.time();result=solve(args.profile);result['elapsed_seconds']=round(time.time()-start,3)
 (HERE/('EXACT_REPORT_EC49FIM_'+args.profile+'.json')).write_text(json.dumps(result,indent=2)+'\n')
 print({k:v for k,v in result.items() if k not in ('trace','witnesses')},flush=True)
 print('witnesses',result['witnesses'][:10],flush=True)
