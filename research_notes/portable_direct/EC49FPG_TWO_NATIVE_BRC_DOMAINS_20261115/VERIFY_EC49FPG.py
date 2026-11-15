#!/usr/bin/env python3
"""Exact finite BRC rooted-vs-terminal certificate, classes 16943 and 16995.

Run: python VERIFY_EC49FPG.py EVIDENCE_DIR
Needs frozen_original_master.txt and EC49FPG_PROFILE.csv (full evidence bundle).
The source and complete root-cost table are pinned by exact SHA256.
No floating point, sampling, MILP, or optimizer feasibility assumption.
"""
import csv,hashlib,itertools,json,sys
from pathlib import Path
from collections import defaultdict,Counter
R=(3,5,6,7); REPS=(16943,16995)
B=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
P=B/'frozen_original_master.txt'; T=B/'EC49FPG_PROFILE.csv'
assert hashlib.sha256(P.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
assert hashlib.sha256(T.read_bytes()).hexdigest()=='a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
with P.open() as f:
 nk,nw,nc=map(int,f.readline().split());assert (nk,nw,nc)==(94,178850,38169)
 fam=[];words=[];tw=0
 for _ in range(nk):
  a=[0]*4;ws=[];n=int(f.readline());tw+=n
  for _ in range(n):
   l,c=f.readline().split();l=int(l);bb=bytes.fromhex(c);assert bb[0] in R
   a[R.index(bb[0])]|=1<<l;ws.append((l,bb))
  fam.append(a);words.append(ws)
 assert tw==nw
 cases=[tuple(map(int,f.readline().split())) for _ in range(nc)]
def domain(keys):
 ret=[0]*24
 for k in keys:
  for ri,m in enumerate(fam[k]):
   while m:
    b=m&-m;ret[b.bit_length()-1]|=1<<ri;m^=b
 assert all(ret)
 return tuple(ret)
allclasses=defaultdict(list)
for i,cs in enumerate(cases):allclasses[domain(cs)].append(i)
assert len(allclasses)==625
entries=defaultdict(dict)
with T.open() as f:
 for row in csv.DictReader(f):
  c,r,m,o,s,v=[int(row[k]) for k in ('config','root','must','opt','subset','cost')]
  assert (r,s) not in entries[c]
  entries[c][r,s]=(v,m,o)
assert set(entries)==set(sum((allclasses[domain(cases[i])] for i in REPS),[]))

def python_native_trie_cost(config,root,dom):
 """Separate byte-level exact integer prefix-coverage DP (not the C++ implementation)."""
 labels=sorted(l for l,m in enumerate(dom) if m>>R.index(root)&1)
 pos={l:j for j,l in enumerate(labels)}
 children=[{}];ends=[0]
 for k in cases[config]:
  for label,bb in words[k]:
   if bb[0]!=root:continue
   at=0
   for byte in bb[1:]:
    if byte not in children[at]:
     children[at][byte]=len(children);children.append({});ends.append(0)
    at=children[at][byte]
   ends[at]|=1<<pos[label]
 def descend(v):
  states={0:0}
  if ends[v]:states[ends[v]]=0
  for u in children[v].values():
   d=descend(u);upd={}
   for a,ca in states.items():
    for b,cb in d.items():
     mask=a|b;cc=ca+cb
     if cc<upd.get(mask,10**9):upd[mask]=cc
   states=upd
  return {m:cc+(m!=0) for m,cc in states.items()}
 exact=descend(0);F=[10**9]*(1<<len(labels))
 for mask,v in exact.items():F[mask]=v
 for j in range(len(labels)):
  for mask in range(1<<len(labels)):
   if not mask>>j&1:F[mask]=min(F[mask],F[mask|1<<j])
 must=sum(1<<l for l,m in enumerate(dom) if m==1<<R.index(root))
 opts=[l for l in labels if dom[l].bit_count()>1]
 out={}
 for bs in itertools.product((0,1),repeat=len(opts)):
  sub=sum(1<<l for l,yes in zip(opts,bs) if yes)
  want=must|sub; mask=sum(1<<pos[l] for l in labels if want>>l&1)
  out[sub]=F[mask]
 return out

results=[];total=Counter();independent=[]
for rep in REPS:
 d=domain(cases[rep]);ids=allclasses[d]
 opts=[l for l in range(24) if d[l].bit_count()>1]
 actions=list(itertools.product(*[tuple(r for j,r in enumerate(R) if d[l]>>j&1) for l in opts]))
 root_coords={r:sorted(sum(1<<l for l,b in zip(ropts,bs) if b)
                      for bs in itertools.product((0,1),repeat=len(ropts)))
              for r in R for ropts in [[l for l in opts if d[l]>>R.index(r)&1]]}
 ncoord=sum(len(s) for s in root_coords.values())
 assert all(len(entries[i])==ncoord for i in ids)
 pclasses=defaultdict(list);tclasses=defaultdict(list);pof={};tof={}
 for i in ids:
  e=entries[i];p=[]
  for j,r in enumerate(R):
   must=sum(1<<l for l,x in enumerate(d) if x==1<<j)
   optmask=sum(1<<l for l in opts if d[l]>>j&1)
   for sub in root_coords[r]:
    v,m,o=e[r,sub];assert m==must and o==optmask and v>=0
    p.append(v)
  pt=tuple(p);pclasses[pt].append(i);pof[i]=pt
  tt=[]
  for action in actions:
   sub={r:0 for r in R}
   for l,r in zip(opts,action):sub[r]|=1<<l
   tt.append(sum(e[r,sub[r]][0] for r in R))
  Tt=tuple(tt);tclasses[Tt].append(i);tof[i]=Tt
 np=sum(len(g)*(len(g)-1)//2 for g in pclasses.values())
 nt=sum(len(g)*(len(g)-1)//2 for g in tclasses.values())
 gauges=[]
 for group in tclasses.values():
  for a,b in itertools.combinations(group,2):
   if pof[a]!=pof[b]:gauges.append([a,b])
 unique=list(tclasses.values());repids=[q[0] for q in unique]
 rows=[tof[i] for i in repids]
 unresolved={(a,b) for a in range(len(rows)) for b in range(a+1,len(rows))}
 chosen=[]
 while unresolved:
  best=max(range(len(actions)),key=lambda q:(sum(rows[a][q]!=rows[b][q] for a,b in unresolved),-q))
  split={(a,b) for a,b in unresolved if rows[a][best]!=rows[b][best]}
  if not split:break
  unresolved-=split;chosen.append(best)
 assert not unresolved
 signatures=[tuple(v[q] for q in chosen) for v in rows]
 assert len(set(signatures))==len(tclasses)
 repaired_count=None
 if rep==16943:
  distinct_p_reps=[group[0] for group in pclasses.values()]
  repaired_count=len(set(tuple(tof[i][q] for q in chosen)+(entries[i][5,0][0],) for i in distinct_p_reps))
  assert repaired_count==len(pclasses)==141
 for c in sorted(set([ids[0],ids[-1]] + sum(gauges, []))):
  for r in R:
   computed=python_native_trie_cost(c,r,d)
   assert set(computed)==set(root_coords[r])
   assert all(computed[sub]==entries[c][r,sub][0] for sub in computed)
  independent.append({'class':rep,'configuration':c,'entries':ncoord})
 rec={'representative':rep,'complete_member_count':len(ids),'member_ids':ids,
      'optional_labels':opts,'action_count':len(actions),'root_cost_coordinates_per_config':ncoord,
      'root_cost_entries':len(ids)*ncoord,'terminal_evaluations':len(ids)*len(actions),
      'all_config_pairs':len(ids)*(len(ids)-1)//2,'root_profile_classes':len(pclasses),
      'terminal_classes':len(tclasses),'root_equal_pairs':np,'terminal_equal_pairs':nt,
      'nonzero_terminal_invisible_gauge_pairs':len(gauges),'gauges':gauges,
      'gauge_root_offsets':[{
        'pair':[a,b],
        'offsets':{str(r):sorted(set(entries[b][r,sub][0]-entries[a][r,sub][0] for sub in root_coords[r])) for r in R},
        'sum_offsets':sum(entries[b][r,0][0]-entries[a][r,0][0] for r in R),
        'all_constant':all(len(set(entries[b][r,sub][0]-entries[a][r,sub][0] for sub in root_coords[r]))==1 for r in R)
       } for a,b in gauges],
      'fixed_query_upper_bound':len(chosen),'query_indices':chosen,
      'selected_signature_count':len(set(signatures)),
      'four_terminal_plus_one_P05_baseline_profile_count':repaired_count}
 results.append(rec)
 for k in ('complete_member_count','root_cost_entries','terminal_evaluations','all_config_pairs','root_equal_pairs','terminal_equal_pairs','nonzero_terminal_invisible_gauge_pairs'):
  total[k]+=rec[k]
 print('CLASS',rep,'configs',len(ids),'Pclasses',len(pclasses),'Tclasses',len(tclasses),'gauge_pairs',len(gauges),'queries',chosen,flush=True)
assert [x['complete_member_count'] for x in results]==[310,242]
assert [x['root_profile_classes'] for x in results]==[141,112]
assert [x['terminal_classes'] for x in results]==[139,112]
assert results[0]['gauges']==[[17928,38165],[24541,38166]]
assert results[0]['gauge_root_offsets'][0]['offsets']=={'3':[0],'5':[-4],'6':[4],'7':[0]}
assert results[0]['gauge_root_offsets'][1]['offsets']=={'3':[0],'5':[-2],'6':[2],'7':[0]}
assert [x['query_indices'] for x in results]==[[64,140,72,31],[92,190,47,4,80,9]]
assert dict(total)=={'complete_member_count':552,'root_cost_entries':49272,'terminal_evaluations':123048,'all_config_pairs':77056,'root_equal_pairs':3480,'terminal_equal_pairs':3482,'nonzero_terminal_invisible_gauge_pairs':2}
print('EC49FPG_FINITE_CHECK_PASS',json.dumps({'classes':results,'totals':dict(total),'independent_byte_trie_checks':independent},sort_keys=True))
