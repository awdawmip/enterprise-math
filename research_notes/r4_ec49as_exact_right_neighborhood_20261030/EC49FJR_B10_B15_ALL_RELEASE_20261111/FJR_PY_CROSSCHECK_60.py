from FJR_PY_CROSSCHECK import run
from ec49fjd_shared import *
from collections import defaultdict,Counter
from pathlib import Path
import json,time,hashlib
P=Path(__file__).parent
cases=json.loads((P/'FJR_CASE_SUMMARY.json').read_text())['cases']
rows=(P/'FJR_CASES.tsv').read_text().splitlines()
actual=[json.loads(x) for x in (P/'FJR_CPP_RESULTS.jsonl').read_text().splitlines()]
counts=Counter();tested=[]
st=time.perf_counter()
for i,case in enumerate(cases):
 key=(case['profile'],case['B'],case['released_n'])
 if case['admissible_keysets']!=1 or counts[key]>=2:continue
 v=run(rows[i].split('\t'))
 want=actual[i]['best_clipped']
 assert v==want,(case,v,want)
 tested.append({'profile':key[0], 'budget':key[1], 'released_n':key[2],'Q':case['Q'],'python_min_clipped':v,'cpp_min_clipped':want})
 counts[key]+=1
print('PY_CROSSCHECK_PASS',len(tested),'seconds',round(time.perf_counter()-st,2),'groups',dict(sorted((str(k),v) for k,v in counts.items())),flush=True)
(P/'FJR_PY_CROSSCHECK_REPORT.json').write_text(json.dumps({'count':len(tested),'samples':tested},indent=2)+'\n')
