#!/usr/bin/env python3
"""EC49FJD: exact B=11 released-key six-path proof. Run next to frozen inputs."""
from ec49fjd_shared import *
from collections import Counter,defaultdict
from pathlib import Path
import hashlib,json,gzip,time
P=Path(__file__).resolve().parent
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert len(cat)==178850 and len(cover)==94 and len(W['profiles'])==2
allkeys=frozenset(cover)
reports=[]
for pr in W['profiles']:
 t=time.monotonic();rows,paths=validate_profile(pr)
 ks=[raw_key(d['word']) for d in rows]
 ksup=defaultdict(int);psup=defaultdict(int)
 for i,(k,ps) in enumerate(zip(ks,paths)):
  ksup[k]|=1<<i
  for prefstep in ps:psup[prefstep]|=1<<i
 originalkeys=frozenset(ksup)
 assert len(originalkeys)==7 and len(psup)==94
 counts=Counter();ledger=[];memo={}
 for Q in combinations(range(24),6):
  qmask=sum(1<<i for i in Q)
  removed=sum(s&qmask==s for s in psup.values())
  if removed!=12:continue
  released=frozenset(k for k,s in ksup.items() if s&qmask==s)
  if not released:continue
  F=frozenset(p for p,s in psup.items() if s&qmask!=s)
  assert len(F)==82
  labs=tuple((rows[i]['window'],rows[i]['signature']) for i in Q)
  fixed=originalkeys-released
  forced=all(not key_cover(labs,fixed,len(released),ban) for ban in released)
  high=tuple(l for l in labs if l[0]>=8)
  low=tuple(l for l in labs if l[0]<8)
  allowed=originalkeys if forced else allkeys
  def query(sub):
   key=(F,tuple(sorted(sub)),forced)
   if key not in memo:memo[key]=solve_high(F,sub,allowed)
   return memo[key]
  one=query(high)
  cert=high if one['status'].startswith('EXCLUDED') else None
  status=('FORCED_HIGH' if forced else 'UNRESTRICTED_HIGH') if cert is not None else None
  if cert is None:
   for lab in low:
    subset=high+(lab,)
    if query(subset)['status'].startswith('EXCLUDED'):
     cert=subset;status='FORCED_PLUS_ONE' if forced else 'UNRESTRICTED_PLUS_ONE'
     break
  if cert is None:
   if not query(labs)['status'].startswith('EXCLUDED'):
    raise AssertionError(f'93-edge candidate unresolved: {pr["profile_id"]} {Q}')
   cert=labs;status='FORCED_FULL6' if forced else 'UNRESTRICTED_FULL6'
  witness=query(cert)
  assert witness['status'].startswith('EXCLUDED')
  counts[status]+=1
  ledger.append({'Q':list(Q),'forced_to_original_seven_keys':forced,
                 'certificate_labels':[list(x) for x in cert],
                 'certificate_rounds':witness.get('rounds',[]),'category':status})
 assert len(ledger)==3918,(pr['profile_id'],len(ledger))
 expected=Counter({'FORCED_HIGH':2880,'FORCED_PLUS_ONE':1032,
                   'UNRESTRICTED_HIGH':1,'UNRESTRICTED_PLUS_ONE':4,'UNRESTRICTED_FULL6':1})
 assert counts==expected,counts
 reports.append({'profile_id':pr['profile_id'],'removed_native_prefix_edges':12,
                 'fixed_native_prefix_edges':82,'budget_for_total_93':11,
                 'original_legal_94_edge_witness':True,'total_positions':len(ledger),
                 'status_counts':dict(counts),'unique_dp_subproblems':len(memo),'ledger':ledger})
 print('PASS',pr['profile_id'],dict(counts),'elapsed_s',round(time.monotonic()-t,3),flush=True)
full={'schema':'EC49FJD_RELEASE_B11_EXACT_LEDGER_V1','science_pin':PIN,
      'model_origin':'EC49FGW_RADIUS5_SCREEN.py at pinned original model',
      'legal_word_count':len(cat),'raw_cache_key_count':len(cover),
      'original_witness':'EC49FGJ_SEVEN_KEY_94_WITNESSES.json',
      'replacement_size':6,'profiles':reports,
      'claim':'For A/B, all released-key Q with |F(Q)|=82 have exact optimal total=94.'}
fullbytes=(json.dumps(full,sort_keys=True,separators=(',',':'),ensure_ascii=False)+'\n').encode('utf-8')
(P/'EXACT_LEDGER_EC49FJD.json.gz').write_bytes(gzip.compress(fullbytes,compresslevel=9,mtime=0))
sha=hashlib.sha256(fullbytes).hexdigest()
summary={'schema':'EC49FJD_RELEASE_B11_SUMMARY_V1','frozen_pin':PIN,
  'exact_ledger_sha256':sha,'exact_ledger_uncompressed_bytes':len(fullbytes),
  'legal_word_count':len(cat),'raw_cache_key_count':len(cover),
  'profiles':[{k:v for k,v in r.items() if k!='ledger'} for r in reports],
  'total_positions':sum(r['total_positions'] for r in reports),
  'proof':'Exhaustive key-cover plus inclusion-minimal exact signed-prefix antichain DP. Empty state at budget 11; unchanged witness is an attainable 94-edge completion.'}
(P/'EXACT_SUMMARY_EC49FJD.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
print('EC49FJD_ALL_7836_PASS',sha,len(fullbytes),flush=True)
