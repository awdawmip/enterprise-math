import ec49fjd_shared as M
from EC49FGW_RADIUS5_SCREEN import *
from collections import Counter,defaultdict
from itertools import combinations
import time,json
M.B=17
out=[]
for pr in W['profiles']:
 start=time.monotonic();rows,paths=validate_profile(pr)
 ks=[raw_key(d['word']) for d in rows];ksup=defaultdict(int);psup=defaultdict(int)
 for i,(k,ps) in enumerate(zip(ks,paths)):
  ksup[k]|=1<<i
  for p in ps:psup[p]|=1<<i
 orig=frozenset(ksup)
 memo={};counts=Counter();ledger=[]
 for Q in combinations(range(24),6):
  qm=sum(1<<i for i in Q)
  if sum(s&qm==s for s in psup.values())!=18:continue
  released=frozenset(k for k,s in ksup.items() if s&qm==s)
  if not released:continue
  F=frozenset(p for p,s in psup.items() if s&qm!=s)
  labs=tuple((rows[i]['window'],rows[i]['signature']) for i in Q)
  forced=all(not M.key_cover(labs,orig-released,len(released),ban) for ban in released)
  if not forced:
   counts['UNFORCED']+=1;ledger.append({'Q':Q,'status':'UNFORCED'});continue
  high=tuple(l for l in labs if l[0]>=8)
  low=tuple(l for l in labs if l[0]<8)
  def query(sub):
   key=(F,tuple(sorted(sub)))
   if key not in memo: memo[key]=M.solve_high(F,sub,orig)
   return memo[key]
  cert=high if query(high)['status'].startswith('EXCLUDED') else None
  typ='HIGH'
  if cert is None:
   for depth in range(1,len(low)+1):
    for sublow in combinations(low,depth):
     sub=high+sublow
     if query(sub)['status'].startswith('EXCLUDED'):
      cert=sub;typ=f'PLUS_{depth}';break
    if cert is not None:break
  if cert is None:
   typ='UNRESOLVED';print('SURVIVE',pr['profile_id'],Q,flush=True)
  counts[typ]+=1; ledger.append({'Q':Q,'status':typ,'cert':cert})
 print('COMPLETE',pr['profile_id'],dict(counts),'memo',len(memo),'s',round(time.monotonic()-start,2),flush=True)
 out.append({'id':pr['profile_id'],'counts':dict(counts),'memo':len(memo),'cases':ledger})
json.dump(out,open('/mnt/data/em_run4/B17_FINISH_REPORT.json','w'),indent=2)
