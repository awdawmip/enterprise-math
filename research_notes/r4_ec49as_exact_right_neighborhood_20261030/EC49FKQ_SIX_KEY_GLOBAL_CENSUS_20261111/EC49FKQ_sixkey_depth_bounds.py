#!/usr/bin/env python3
"""Exact depthwise native signed-X6 forced-label lower bounds for every six-key BRC covering set.
Reuses complete 178,850-word frozen input. The 2004 covering sets are exhaustive via
five mutually disjoint label key support families and one free sixth key.
"""
import collections,itertools,sys,json,time
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P/'EC49FJR'))
import EC49FGW_RADIUS5_SCREEN as g
labels=sorted((h,s) for h,ss in g.REQ.items() for s in ss); LI={x:i for i,x in enumerate(labels)}
keys=sorted({g.raw_key(w) for lab,w in g.all_words()});KI={k:i for i,k in enumerate(keys)}
assert len(keys)==94
mask=[0]*94;minlens=[[1000]*24 for _ in keys]
layers=[collections.defaultdict(dict) for _ in keys]
for lab,w in g.all_words():
 k=g.raw_key(w);j=KI[k];i=LI[lab];mask[j]|=1<<i
 pre=g.pref(w);minlens[j][i]=min(minlens[j][i],len(pre)); dd=layers[j]
 for d,p in enumerate(pre,1):dd[d][p]=dd[d].get(p,0)|(1<<i)
forced=[(2,16),(2,32),(3,16),(4,1),(7,1)]
families=[tuple(j for j,k in enumerate(keys) if mask[j]>>LI[x]&1) for x in forced]
assert [len(x) for x in families]==[1,1,2,7,34]
S=set()
FULL=(1<<24)-1
for tup in itertools.product(*families):
 b=set(tup);bm=0
 for j in b:bm|=mask[j]
 for j in range(94):
  if j not in b and bm|mask[j]==FULL:S.add(tuple(sorted((*b,j))))
assert len(S)==2004

def bound(K):
 L=[min(minlens[j][i] for j in K) for i in range(24)]
 assert max(L)<1000
 res=0;parts=[]
 for d in range(1,max(L)+1):
  forced=sum(1<<i for i in range(24) if L[i]>=d)
  n=forced.bit_count()
  if n==0:continue
  allpref={}
  for j in K:
   for p,mask in layers[j][d].items():allpref[p]=allpref.get(p,0)|mask
  m=max((v&forced).bit_count() for v in allpref.values())
  assert m>=1
  z=(n+m-1)//m
  res+=z;parts.append((d,n,m,z))
 return res,parts

start=time.time();out=[];hist=collections.Counter();below=[]
for t,K in enumerate(sorted(S),1):
 lb,parts=bound(K)
 hist[lb]+=1
 out.append({'keys':[list(keys[j]) for j in K],'lower_bound':lb,'layers':parts})
 if lb<=93:below.append(K)
 if t%200==0:print('done',t,'time',round(time.time()-start,2),'min',min(hist),'survivors',len(below),flush=True)
res={'schema':'EC49FKQ_SIX_KEY_FORCED_LAYER_BOUNDS_V1','frozen_pin':g.PIN,'word_count':178850,'label_count':24,'key_count':94,'six_key_covering_sets':len(S),'lower_bound_histogram':dict(sorted(hist.items())),'global_min_lower_bound':min(hist),'global_max_lower_bound':max(hist),'potential_93_sets':len(below),'records':out}
(P/'EC49FKQ_SIXKEY_DEPTH_REPORT.json').write_text(json.dumps(res,separators=(',',':'))+'\n')
(P/'EC49FKQ_SIXKEY_DEPTH_SUMMARY.json').write_text(json.dumps({k:v for k,v in res.items() if k!='records'},indent=2)+'\n')
print('EC49FKQ_DONE',len(S),'min',min(hist),'survivors',len(below),'seconds',round(time.time()-start,2),flush=True)
