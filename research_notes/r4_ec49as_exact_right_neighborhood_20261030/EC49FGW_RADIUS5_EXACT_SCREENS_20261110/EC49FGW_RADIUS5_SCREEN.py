#!/usr/bin/env python3
"""EC49FGW: exact fifth-label perturbation profile, unrestricted-key singleton test.
Frozen original nine-state BRC / signed six-axis native path model. Uses integer-only
operations and covers all 5-of-24 labeled replacements for both EC49FGJ witnesses.
"""
import json,collections,itertools,time
from pathlib import Path
P=Path(__file__).parent
W=json.loads((P/'EC49FGJ_SEVEN_KEY_94_WITNESSES.json').read_text())
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert W['frozen_scientific_pin']==PIN
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
def pref(word):
 p=b'';out=[]
 for c in word:
  for d in STEPS[c]:
   p+=bytes((d+4,));out.append(p)
 return out

def raw_key(word):
 p=[v for c in word for v in STEPS[c]]
 return tuple(p.count(j) for j in (1,2,3))

def generator(h,key):
 x,y,z=key
 a=z-1;b=x+y-h-1;f=h+1-y-2*z;g=h+1-x
 if min(a,b,f,g)<0:return
 for c in range(b+1):
  n=[a,c,b-c,z,f,g]
  def rec(w,q):
   if len(w)==h:
    if SIG[q] in REQ[h]:yield (h,SIG[q]),w
    return
   for j,op in enumerate(OPS):
    if n[j] and T[q][j]!=8:
     n[j]-=1
     yield from rec(w+op,T[q][j]);n[j]+=1
  yield from rec('',0)

def all_words():
 for h in REQ:
  for x in range(1,h+2):
   for y in range(0,h+2):
    for z in range(1,(h+1)//2+1):
     if x+y>=h+1 and y+2*z<=h+1:
      yield from generator(h,(x,y,z))

def index_all(catalog):
 # Each signed prefix p maps label -> minimal full native length of an extending word.
 idx=collections.defaultdict(dict)
 base={};cnt=collections.Counter();keyset=set()
 for label,w in catalog:
  keyset.add(raw_key(w));ps=pref(w);L=len(ps);cnt[label]+=1
  base[label]=min(base.get(label,1000),L)
  for p in ps:
   m=idx[p]
   if L<m.get(label,1000):m[label]=L
 return idx,base,cnt,keyset

def validate_profile(profile):
 rows=sorted(profile['demands'],key=lambda d:(d['window'],d['signature']))
 assert len(rows)==24
 qlabels={(h,s) for h in REQ for s in REQ[h]}
 assert {(d['window'],d['signature']) for d in rows}==qlabels
 ps=[set(pref(d['word'])) for d in rows]
 for d in rows:
  assert len(d['word'])==d['window']
  q=0;pos=[0]*6
  for c in d['word']:
   q=T[q][OPS.index(c)];assert q!=8
   for ax in STEPS[c]:pos[abs(ax)-1]+=1 if ax>0 else -1
  assert SIG[q]==d['signature'] and pos==[2,0,0,0,0,0]
 assert len(set().union(*ps))==94
 return rows,ps

def experiment(profile,idx,base,full_catalog):
 rows,ps=validate_profile(profile)
 label=[(d['window'],d['signature']) for d in rows]
 ks=[raw_key(d['word']) for d in rows]
 assert len(set(ks))==7
 seven_set=set(ks)
 idx_fixed,base_fixed,nw_fixed,keys_fixed=index_all((lab,w) for lab,w in full_catalog if raw_key(w) in seven_set)
 assert len(keys_fixed)==7 and sum(nw_fixed.values())==9838
 sup=collections.defaultdict(int);key_sup=collections.defaultdict(int)
 for i, (pi,k) in enumerate(zip(ps,ks)):
  for p in pi:sup[p]|=1<<i
  key_sup[k]|=1<<i
 assert len(sup)==94
 bysup=collections.Counter(sup.values())
 allprefix=set(sup)
 hist=collections.Counter();release_hist=collections.Counter();key_loss_hist=collections.Counter()
 res=collections.Counter();promising=[]
 start=time.time()
 for Q in itertools.combinations(range(24),5):
  mask=sum(1<<i for i in Q)
  rem={p for p,s in sup.items() if s&mask==s}
  B=len(rem)-1
  hist[B]+=1
  if B<0:
   res['baseline_blocked']+=1
   continue
  res['baseline_survived']+=1
  released=tuple(sorted(k for k,s in key_sup.items() if s&mask==s))
  release_hist[str(released)]+=1
  key_loss_hist[len(released)]+=1
  F=allprefix-rem
  minima={label[i]:base[label[i]] for i in Q}
  for p in F:
   j=idx.get(p)
   if not j:continue
   Lp=len(p)
   for lab,L in j.items():
    if lab in minima and L-Lp<minima[lab]:minima[lab]=L-Lp
  unrestricted_reject=any(v>B for v in minima.values())
  if unrestricted_reject:
   res['unrestricted_singleton_rejected']+=1
  else:
   res['unrestricted_singleton_survived']+=1
   res['survive_B_'+str(B)]+=1
   if len(promising)<30:promising.append({'positions':Q,'labels':[label[i] for i in Q],
    'released_keys':released,'budget':B,'unrestricted_minima':{str(k):v for k,v in minima.items()}})
  if len(released)==0:
   res['no_key_release_positions']+=1
   fixed_min={label[i]:base_fixed[label[i]] for i in Q}
   for p in F:
    data=idx_fixed.get(p)
    if not data:continue
    Lp=len(p)
    for lab,L in data.items():
     if lab in fixed_min and L-Lp<fixed_min[lab]:fixed_min[lab]=L-Lp
   if any(m>B for m in fixed_min.values()):
    res['fixed_7key_singleton_rejected']+=1
   else:
    res['fixed_7key_singleton_survived']+=1
  if unrestricted_reject or (len(released)==0 and any(m>B for m in fixed_min.values())):
   res['combined_rejected']+=1
  else:
   res['combined_survived']+=1
 assert sum(hist.values())==42504
 return {'id':profile['profile_id'],'n5':42504,'histogram_budget':dict(sorted(hist.items())),
         'counts':dict(res),'released_key_count_histogram':dict(key_loss_hist),
         'released_key_patterns':dict(release_hist),
         'best_budget':max(hist),'promising_first30':promising,
         'distinct_support_masks':len(bysup),'elapsed_seconds':round(time.time()-start,2)}

if __name__=='__main__':
 t=time.time();catalog=list(all_words());print('CATALOG',len(catalog),flush=True)
 idx,base,cnt,keyset=index_all(catalog)
 print('INDEX',len(idx),'KEYS',len(keyset),'CANDIDATE_PER_LABEL',dict(cnt),'seconds',round(time.time()-t,1),flush=True)
 assert len(catalog)==178850 and len(keyset)==94
 reports=[]
 for pr in W['profiles']:
  r=experiment(pr,idx,base,catalog)
  reports.append(r);print(pr['profile_id'],r['counts'],'seconds',r['elapsed_seconds'],flush=True)
 output={'schema':'EC49FGW_RADIUS5_EXACT_UNRESTRICTED_SINGLETON_V1','frozen_scientific_pin':PIN,
         'witness_blob_sha1': 'e65c1598ad9fa2680558046ed1e59d83806536b8',
         'scope':'all five-label positions; complete 178850-word legal catalog, arbitrary raw cache keys for singleton necessity',
         'candidate_words':len(catalog),'raw_keys':len(keyset),'candidate_per_label':{str(k):v for k,v in cnt.items()},
         'prefix_index_size':len(idx),'profiles':reports}
 (P/'EXACT_REPORT_EC49FGW.json').write_text(json.dumps(output,ensure_ascii=False,indent=2,default=str)+'\n')
 print('EC49FGW_EXACT_PASS',flush=True)
