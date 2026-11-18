#!/usr/bin/env python3
"""Independent Python integer-exact signed byte-prefix DP for selected d=6 cases."""
import collections,json,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import all_words,pref,raw_key,PIN
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
CAT=list(all_words());assert len(CAT)==178850
CASES=json.load(open(P/'EC49FLD_CASE_INDEX.json'))['cases']
COSTS=json.load(open(P/'COSTS_EC49FLD.json'))['ordered_costs']
assert len(CASES)==len(COSTS)==676
def calculate(keys):
 roots=collections.defaultdict(list)
 for lab,w in CAT:
  if raw_key(w) in keys:
   ps=pref(w);roots[ps[0]].append((lab,ps))
 choices=collections.defaultdict(list);costs={}
 for root,words in roots.items():
  labels=sorted({lab for lab,ps in words});idmap={lab:i for i,lab in enumerate(labels)}
  kids=[{}];term=[0]
  for lab,ps in words:
   node=0
   for p in ps:
    if p not in kids[node]:
     kids[node][p]=len(kids);kids.append({});term.append(0)
    node=kids[node][p]
   term[node]|=1<<idmap[lab]
  def dp(u):
   a={0:0}
   if term[u]:a[term[u]]=0
   for v in kids[u].values():
    b=dp(v);out={}
    for m,c in a.items():
     for n,d in b.items():
      z=m|n;w=c+d
      if w<out.get(z,10**9):out[z]=w
    a=out
   return {m:c+int(bool(m)) for m,c in a.items()} if u else a
  e=dp(0);cover=[10**9]*(1<<len(labels))
  for m,c in e.items():cover[m]=c
  for j in range(len(labels)):
   for mask in range(len(cover)):
    if not (mask>>j)&1:cover[mask]=min(cover[mask],cover[mask|(1<<j)])
  costs[root]=cover
  for lab,j in idmap.items():choices[lab].append((root,j))
 assert len(choices)==24
 order=sorted(choices,key=lambda l:len(choices[l]))
 acc={r:0 for r in costs};best=10**9
 def walk(i):
  nonlocal best
  if i==24:
   best=min(best,sum(costs[r][mask] for r,mask in acc.items()));return
  for r,j in choices[order[i]]:
   old=acc[r];acc[r]|=1<<j;walk(i+1);acc[r]=old
 walk(0)
 return best,len(roots)
if __name__=='__main__':
 ids=[0,179,228,269,293,299,458,675] if len(sys.argv)==1 else list(map(int,sys.argv[1:]))
 for i in ids:
  got,nroots=calculate({tuple(x) for x in CASES[i]['keyset']})
  assert got==COSTS[i],(i,got,COSTS[i])
  print('EC49FLD_INDEPENDENT_PASS',i,'cost',got,'roots',nroots,flush=True)
 print('EC49FLD_INDEPENDENT_ALL_SELECTED_PASS',len(ids),flush=True)
