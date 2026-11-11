#!/usr/bin/env python3
"""Exact six-demand unrestricted-key lower bounds for the 49 remaining BRC backgrounds.
Use pinned sibling EC49FGW original nine-state grammar and witnessed X6 paths.
Compile SOLVE_RADIUS6_UNRESTRICTED.cpp as solve_all and
INDEPENDENT_RADIUS6_UNRESTRICTED.cpp as independent_all before running.
"""
import collections,itertools,json,os,subprocess,sys,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,PIN,all_words,validate_profile,STEPS
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
qs=set()
for i,j in itertools.combinations(range(14,18),2):qs.add(tuple(sorted((i,j,18,19,20,21))))
for i in range(18):
 for j in (22,23):qs.add(tuple(sorted((i,18,19,20,21,j))))
for x in ((10,11,12,13,22,23),(14,15,16,17,22,23),(18,19,20,21,22,23)):
 qs.add(tuple(x))
for i in range(4):qs.add((i+10,i+14,18,19,20,21))
qs=sorted(qs);assert len(qs)==49
prof_data={}
for p in W['profiles']:
 rows,ps=validate_profile(p);prof_data[p['profile_id']]=dict(rows=rows,ps=ps)
D={}
for pid in ('A','B'):
 ps=prof_data[pid]['ps']
 D[pid]={q:93-len(set().union(*(ps[i] for i in range(24) if i not in q))) for q in qs}
assert D['A']==D['B']
assert collections.Counter(D['A'].values())=={11:6,15:32,17:8,18:2,23:1}
bylab=collections.defaultdict(list)
catalog=list(all_words());assert len(catalog)==178850
for lab,word in catalog:bylab[lab].append(bytes(s+4 for c in word for s in STEPS[c]).hex())
res=[]
for ix,Q in enumerate(qs):
 B=D['A'][Q]
 labels=[(prof_data['A']['rows'][i]['window'],prof_data['A']['rows'][i]['signature']) for i in Q]
 assert [(prof_data['B']['rows'][i]['window'],prof_data['B']['rows'][i]['signature']) for i in Q]==labels
 with tempfile.NamedTemporaryFile('w',delete=False,dir=HERE,suffix='.txt') as f:
  target=f.name;f.write('6\n')
  for lab in labels:
   words=bylab[lab];f.write(str(len(words))+'\n');f.write(''.join(w+'\n' for w in words))
  for pid in ('A','B'):
   ps=prof_data[pid]['ps'];F=sorted(set().union(*(ps[i] for i in range(24) if i not in Q)))
   assert len(F)==93-B
   f.write(f'{pid} {len(F)}\n');f.write(''.join(w.hex()+'\n' for w in F))
 try:
  def solve(program):
   p=subprocess.run([str(HERE/program),target],capture_output=True,text=True,timeout=45,check=True)
   out={}
   for line in p.stdout.splitlines():
    parts=line.split()
    if parts and parts[0] in ('B11_EXACT','INDEPENDENT_B11'):out[parts[1]]=int(parts[2])
   assert set(out)=={'A','B'},p.stdout
   return out
  first=solve('solve_all');second=solve('independent_all')
  assert first==second
  assert all(v<=B+1 for v in first.values())
  res.append({'Q':list(Q),'labels':labels,'B93':B,'fixed_prefixes':93-B,
    'unrestricted_new_prefixes':first,'status':{p:'EXACT_94' if v>B else 'KEY_CAP_REQUIRED' for p,v in first.items()}})
  print('CASE',ix+1,'Q',Q,'B',B,'A',first['A'],'Bprofile',first['B'],flush=True)
 finally:os.unlink(target)
summary={p:{'total':49,'exact94':sum(x['status'][p]=='EXACT_94' for x in res),
 'key_cap_needed':sum(x['status'][p]=='KEY_CAP_REQUIRED' for x in res)} for p in ('A','B')}
assert all(x['exact94']==45 and x['key_cap_needed']==4 for x in summary.values()),summary
(HERE/'EXACT_REPORT_EC49FIW.json').write_text(json.dumps({'schema':'EC49FIW_49_BRC_BACKGROUND_EXACT_V1',
 'pin':PIN,'legal_words':178850,'summary':summary,'cases':res},indent=2)+'\n')
print('EC49FIW_UNRESTRICTED_49_PASS',summary,flush=True)
