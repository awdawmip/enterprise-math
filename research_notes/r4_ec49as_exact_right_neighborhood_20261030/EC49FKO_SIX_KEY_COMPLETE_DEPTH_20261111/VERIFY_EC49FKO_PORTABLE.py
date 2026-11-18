#!/usr/bin/env python3
"""EC49FKO: exact six-raw-key BRC cover census and native-prefix depth sieve.
Frozen nine-state X6 input pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import collections,itertools,functools,json,os,sys
from pathlib import Path
P=Path(__file__).resolve().parent
SRC=Path(os.environ.get('EC49FKM_INPUT_DIR', P.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
sys.path.insert(0,str(SRC));import EC49FGW_RADIUS5_SCREEN as g
assert g.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
labels=sorted((h,s) for h,ss in g.REQ.items() for s in ss)
idx={lab:i for i,lab in enumerate(labels)}
K=collections.defaultdict(lambda:{'labels':0,'minlength':[999]*24,'depth':collections.defaultdict(dict)})
words=0
for lab,word in g.all_words():
 words+=1;k=g.raw_key(word);rec=K[k];bit=1<<idx[lab];p=g.pref(word)
 rec['labels']|=bit;rec['minlength'][idx[lab]]=min(rec['minlength'][idx[lab]],len(p))
 for depth,prefix in enumerate(p,1):
  d=rec['depth'][depth];d[prefix]=d.get(prefix,0)|bit
assert words==178850 and len(K)==94 and len(labels)==24
S=((2,16),(2,32),(3,16),(4,1),(7,1))
families=[tuple(sorted(k for k,d in K.items() if d['labels']&(1<<idx[lab]))) for lab in S]
assert list(map(len,families))==[1,1,2,7,34]
assert all(not(set(a)&set(b)) for i,a in enumerate(families) for b in families[i+1:])
full=(1<<24)-1; covers=set()
for core in itertools.product(*families):
 for extra in K:
  if extra in core:continue
  keys=tuple(sorted((*core,extra)))
  if keys in covers:continue
  if functools.reduce(int.__or__,(K[k]['labels'] for k in keys),0)==full:covers.add(keys)
assert len(covers)==2004
K0={(2,1,1),(3,0,1),(3,1,1)}
U=((3,3,1),(4,2,1),(5,1,1),(5,1,2))
V=((5,5,1),(6,4,1),(7,3,1),(7,3,2))
allfive=[K0|{u,v} for u in U for v in V]
results=[];counts=collections.Counter()
for keys in sorted(covers):
 L=[min(K[k]['minlength'][i] for k in keys) for i in range(24)]
 assert max(L)<999
 total=0;layers=[]
 for depth in range(1,max(L)+1):
  forced=sum(1<<i for i,x in enumerate(L) if x>=depth)
  prefixes={}
  for k in keys:
   for word_prefix,mask in K[k]['depth'][depth].items():
    prefixes[word_prefix]=prefixes.get(word_prefix,0)|mask
  M=max((mask&forced).bit_count() for mask in prefixes.values())
  N=forced.bit_count();r=(N+M-1)//M;total+=r;layers.append((depth,N,M,r))
 hasfive=any(base.issubset(keys) for base in allfive)
 counts[(hasfive,total>=94)]+=1
 results.append({'keys':keys,'depth_lower':total,'contains_five_key_cover':hasfive,'layers':layers})
assert counts=={(True,True):823,(True,False):553,(False,True):440,(False,False):188}
assert min(rec['depth_lower'] for rec in results)==67
obj={'schema':'EC49FKO_SIX_KEY_COMPLETE_DEPTH_CERTIFICATE_V1','frozen_pin':g.PIN,
     'legal_words':words,'full_keys':len(K),'labels':len(labels),'six_key_complete_covers':len(covers),
     'containing_five_key_cover':1376,'strict_minimal_six_key_covers':628,
     'depth_excludes_at_most_93':1263,'depth_sieve_survivors':741,'records':results}
out=Path(os.environ.get('EC49FKO_OUT',P/'EXACT_REPORT_EC49FKO.json'))
out.write_text(json.dumps(obj,indent=2)+'\n')
print('EC49FKO_ALL_SIX_KEY_EXACT_PASS',len(covers),'excluded',1263,'survivors',741,'lower_min',67)
