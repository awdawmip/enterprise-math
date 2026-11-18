#!/usr/bin/env python3
"""Exact R5 adaptive probe expected-cost certificate (offline observer queries)."""
from pathlib import Path
import csv, hashlib, json, collections
from fractions import Fraction
P=Path(__file__).resolve().parent
SHAS={
'EXACT_R5_ALL_101_BUDGETS.json':'50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b',
'interior_distinguishing_budget_witnesses.csv':'3d2706270c490433b7c6fab8a4b606b570e771c27e35aed37260969225bacc32'}
for f,s in SHAS.items(): assert hashlib.sha256((P/f).read_bytes()).hexdigest()==s,f
T=json.loads((P/'EXACT_R5_ALL_101_BUDGETS.json').read_text())['counts_and_cohorts']
C={k:[int(v) for v in T[str(k)]['counts']] for k in range(214,315)}
S=list(map(int,json.loads((P/'stages_18.json').read_text())['stage_taus']))
assert len(S)==18
W=list(csv.DictReader((P/'interior_distinguishing_budget_witnesses.csv').open()))
assert len(W)==620
p={}
def root(a):
 p.setdefault(a,a)
 if p[a]!=a:p[a]=root(p[a])
 return p[a]
for w in W:
 a=(int(w['xA']),int(w['yA']));b=(int(w['xB']),int(w['yB']))
 a,b=root(a),root(b)
 if a!=b:p[max(a,b)]=min(a,b)
comp=collections.defaultdict(set)
for x in p:comp[root(x)].add(x)
assert len(comp)==108
cache={}
def support(a,k,j):
 key=(a,k,j)
 if key in cache:return cache[key]
 x,y=a; raw=C[k]; points=sorted((raw[h],i) for i,h in enumerate((18,24,82,34,17,x,144,208,y)))
 masks=set()
 for left,_ in points:
  masks.add(sum(1<<i for v,i in points if left<=v<=left+S[j]))
 ans=tuple(sorted(m for m in masks if not any(m!=n and m&n==m for n in masks)))
 cache[key]=ans
 return ans
triple=collections.Counter();two=collections.Counter();class_details=[]
for anchor,vs in sorted(comp.items()):
 wrows=[r for r in W if (int(r['xA']),int(r['yA'])) in vs]
 budgets={int(r['witness_budget_list']) for r in wrows}
 assert len(budgets)==1
 budget=budgets.pop()
 if budget==220:
  groups={support(a,220,2) for a in vs}
  assert len(groups)==2
  two['220']+=len(vs)
 else:
  daughters=collections.defaultdict(list)
  for a in sorted(vs):daughters[(support(a,214,4),support(a,214,8))].append(a)
  if len(daughters)==2:
   assert len({support(a,214,3) for a in vs})==2
   two['214']+=len(vs)
  else:
   assert len(daughters)==3 and budget==214
   sizes=sorted(len(v) for v in daughters.values())
   assert sizes in ([1,1,1],[2,2,2])
   reps=[v[0] for v in daughters.values()]
   useful=[]
   for k in range(214,315):
    for j in range(18):
     q=[support(a,k,j) for a in reps]
     assert len(set(q))<=2,(anchor,k,j,'one_probe_would_suffice')
     if len(set(q))==2:useful.append((k,j))
   assert useful==[(214,j) for j in range(4,16)],(anchor,useful)
   triple[tuple(sizes)]+=1
   class_details.append({'anchor':anchor,'members':len(vs),'sizes':sizes,'useful_probes':len(useful)})
assert two=={'214':128,'220':128} and triple=={(1,1,1):16,(2,2,2):24}
N=30876; fixed=256+192*2;adaptive=256+192*Fraction(5,3)
assert fixed==640 and adaptive==576
result={'schema':'R5_ADAPTIVE_PROBE_UNIFORM_CERT_V1','status':'EXACT_FINITE_CHECKED_NOT_REVIEWED',
        'frozen_source_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'input_sha256':SHAS,'population':N,'three_daughter_classes':40,
        'three_daughter_multiplicities':{'1+1+1':16,'2+2+2':24},
        'budgets_checked':101,'stages_checked':18,'triple_class_probe_checks':40*101*18,
        'three_daughter_useful_probes':[[214,j] for j in range(4,16)],
        'fixed_extra_probes_sum':fixed,'adaptive_expected_probes_sum':int(adaptive),
        'fixed_mean':str(Fraction(fixed,N)),'adaptive_mean':str(Fraction(adaptive,N)),
        'relative_saving':str(Fraction(fixed-adaptive,fixed)),
        'cached_exact_support_signatures':len(cache),
        'no_new_Bellman_result':True,'class_details':class_details}
(P/'R5_ADAPTIVE_UNIFORM_RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('PASS_R5_ADAPTIVE_UNIFORM',len(class_details),result['triple_class_probe_checks'],
      len(cache),result['fixed_mean'],result['adaptive_mean'],result['relative_saving'])
