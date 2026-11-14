#!/usr/bin/env python3
"""Exact pairwise incompatibility max clique per native depth, for frozen six-key BRC survivors.
Prefix grouping can cover at most one label from each pairwise incompatible subset.
"""
from pathlib import Path
import sys,json,collections,time,os
T=time.monotonic();BASE=Path(__file__).resolve().parent
SRC=Path(os.environ.get('EC49FKM_INPUT_DIR',BASE.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
sys.path.insert(0,str(SRC));import EC49FGW_RADIUS5_SCREEN as g
assert g.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
FKO=Path(os.environ.get('EC49FKO_REPORT',BASE.parent/'EC49FKO_SIX_KEY_COMPLETE_DEPTH_20261111'/'EXACT_REPORT_EC49FKO.json'))
res=json.loads(FKO.read_text())['records']
LABELS=sorted((h,s) for h,ss in g.REQ.items() for s in ss)
LI={lab:i for i,lab in enumerate(LABELS)}
K=collections.defaultdict(lambda:collections.defaultdict(dict))
MINLEN=collections.defaultdict(lambda:[999]*24)
for lab,w in g.all_words():
 k=g.raw_key(w);bit=1<<LI[lab]
 MINLEN[k][LI[lab]]=min(MINLEN[k][LI[lab]],len(g.pref(w)))
 for d,p in enumerate(g.pref(w),1):
  db=K[k][d];db[p]=db.get(p,0)|bit
print('INIT',time.monotonic()-T,len(K),flush=True)

def max_incompatible(supports,forced):
    # Compatible iff there is a prefix available to both at this depth.
    vertices=[i for i in range(24) if (forced>>i)&1]
    c=[0]*24
    for mask in supports:
        m=mask&forced
        while m:
            bit=m&-m; i=bit.bit_length()-1
            c[i]|=(m^bit)
            m^=bit
    # Incompatibility is complement of pairwise sharing
    adj=[forced&~(1<<i)&~c[i] for i in range(24)]
    best=0
    # Recursive exact clique search, basic branch and bound
    def go(p,n):
        nonlocal best
        if not p:
            if n>best:best=n
            return
        if n+p.bit_count()<=best:return
        while p:
            vbit=p&-p;v=vbit.bit_length()-1
            go(p&adj[v],n+1)
            p^=vbit
            if n+p.bit_count()<=best:return
    go(forced,0)
    return best

assert len(res)==2004
survivors=[r for r in res if r['depth_lower']<94]
assert len(survivors)==741
start=int(os.environ.get('START','0')); end=int(os.environ.get('END',str(len(survivors))))
records=[]
for j in range(start,end):
 r=survivors[j]; keys=[tuple(k) for k in r['keys']]
 shortest=[min(MINLEN[k][i] for k in keys) for i in range(24)]
 improvement=0; better=[];new_bound=0
 for dep,N,M,old in r['layers']:
  forced=sum(1<<i for i,L in enumerate(shortest) if L>=dep)
  assert forced.bit_count()==N
  prefixes={}
  for k in keys:
   for p,mask in K[k][dep].items():prefixes[p]=prefixes.get(p,0)|mask
  value=max(old,max_incompatible(prefixes.values(),forced))
  new_bound+=value
  if value>old:better.append((dep,old,value))
 records.append(dict(survivor_index=j,keys=keys,old_bound=r['depth_lower'],new_bound=new_bound,improved_layers=better))
 if (j-start+1)%20==0:print('DONE',j+1,'elapsed',round(time.monotonic()-T,2),'excluded',sum(x['new_bound']>=94 for x in records),flush=True)
new_excluded=sum(x['new_bound']>=94 for x in records)
if start==0 and end==741:
 assert new_excluded==732 and len([x for x in records if x['new_bound']<94])==9
print('EC49FKP_PART',start,end,'new_excluded',new_excluded,'improved',sum(x['new_bound']>x['old_bound'] for x in records),'secs',round(time.monotonic()-T,2),flush=True)
output=Path(os.environ.get('EC49FKP_OUT',BASE/f'EC49FKP_{start}_{end}.json'))
output.write_text(json.dumps({'start':start,'end':end,'records':records},separators=(',',':'))+'\n')

if start==0 and end==741:
 print("EC49FKP_ALL_1995_EXCLUDED_9_SURVIVORS_PASS")
