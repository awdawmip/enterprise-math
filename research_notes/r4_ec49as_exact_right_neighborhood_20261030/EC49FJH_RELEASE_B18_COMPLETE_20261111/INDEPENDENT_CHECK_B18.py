import ec49fjd_shared as e
from itertools import combinations
from collections import defaultdict,Counter
import json,hashlib,time,random
from pathlib import Path
P=Path(__file__).parent
rows=[json.loads(x) for x in (P/'B18_RESULTS.jsonl').read_text().splitlines()]
lines=(P/'B18_CASES.tsv').read_text().splitlines()
assert len(rows)==len(lines)==836
profilecounts=Counter()
for row,line in zip(rows,lines):
 v=line.split('\t');who,q,labels,options,zero=v
 assert row['profile']==who and row['Q']==q
 assert row['options']==len(options.split('|'))
 assert row['best_clipped']==19 and row['feasible_93']==0
 assert len(zero.split(';'))==75
 profilecounts[who]+=1
assert profilecounts=={'A':418,'B':418}
for pr in e.W['profiles']:
 ws,paths=e.validate_profile(pr)
 assert len(set().union(*paths))==94
 for data in filter(lambda r:r['profile']==pr['profile_id'],rows):
  Q=tuple(map(int,data['Q'].split(',')))
  F=set().union(*(paths[i] for i in range(24) if i not in Q))
  U=set().union(*(paths[i] for i in Q))
  assert len(F)==75 and len(U-F)==19
print('INDEPENDENT_WITNESS_AND_CASE_COVERAGE_PASS',dict(profilecounts))
e.B=18
for i in [0,10,100,400,417,418,600,833,835,836-1]:
 v=lines[i].split('\t');who,q,labels,options,zeros=v
 qs=tuple(map(int,q.split(',')));pr=next(p for p in e.W['profiles'] if p['profile_id']==who)
 ws,paths=e.validate_profile(pr)
 F=frozenset(set().union(*(paths[j] for j in range(24) if j not in qs)))
 ks=frozenset(e.raw_key(d['word']) for d in ws)
 lab=[tuple(map(int,l.split(','))) for l in labels.split(';')]
 lab2=tuple(l for l in lab if l[0]>=8)
 if len(lab2)<2:lab2=tuple(lab[:2])
 x=e.solve_high(F,lab2,ks)
 assert x['status'] in ('EXCLUDED_HIGH','SURVIVES_HIGH','EXCLUDED_MISSING_LABEL'),x
 print('CHECK',i,who,qs,'two_label_check',x['status'],x.get('min_cost_within_budget'),flush=True)
print('INDEPENDENT_SMALL_SUBPROBLEM_CHECK_PASS')
