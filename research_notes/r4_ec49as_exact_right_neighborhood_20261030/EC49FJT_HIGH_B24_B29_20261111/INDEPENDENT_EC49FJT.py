#!/usr/bin/env python3
"""Independent Python prefix-set-antichain DP against C++ trie for 20 grouped cases."""
from pathlib import Path
import sys,json,time,collections,hashlib
P=Path(__file__).resolve().parent
sys.path.insert(0,str((P/'../EC49FJR').resolve()))
from FJR_PY_CROSSCHECK import run
rows=(P/'FJT_CASES.tsv').read_text().splitlines()
res=[json.loads(x) for x in (P/'FJT_CPP_RESULTS.jsonl').read_text().splitlines()]
counts=collections.Counter();samples=[]
t0=time.monotonic()
selected={0,1,8,9,13,16,22,29,89}
for i,(row,rec) in enumerate(zip(rows,res)):
 if i not in selected:continue
 label=(rec['profile'],93-int(len(row.split('\t')[4].split(';')))) # correct B=93-|F|
 # two cases per profile/B
 if counts[label]>=2:continue
 val=run(row.split('\t'))
 assert val==rec['best_clipped'], (i,label,val,rec)
 counts[label]+=1
 samples.append({'case_index':i,'profile':label[0], 'B':label[1], 'positions':rec['Q'],'independent_python_lower_bound_clipped':val})
 print('PY_PASS',i,label,val,flush=True)
report={'schema':'EC49FJT_INDEPENDENT_PATHSET_CROSSCHECK_V1','coverage':'9 selected A-profile cases: B24/25/27/28/29','crosschecks':len(samples),'samples':samples}
(P/'FJT_PY_CROSSCHECK_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
print('EC49FJT_INDEPENDENT_PASS',len(samples),'elapsed',round(time.monotonic()-t0,3),flush=True)
