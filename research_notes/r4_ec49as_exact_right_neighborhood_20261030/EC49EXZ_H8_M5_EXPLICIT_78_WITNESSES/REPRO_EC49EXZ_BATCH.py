#!/usr/bin/env python3
"""Reproduce the smallest 200 EC49EXY double-collision schedule DP screens.
Run from the GitHub research tree after compiling the published EC49EXJ DP binary.
No imported solver results. Path sources are already published in sibling folders.
"""
import json,sys,hashlib,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent.parent
S=R/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'
X=R/'EC49EXY_H8_M5_EXACT_CROSS_FIBER_CAPS'
sys.path.insert(0,str(S))
from SCREEN_H5_EC49EXJ import words,build_input
rows=[]
for line in (X/'EC49EXY_DOUBLE_CANDIDATES.tsv').read_text().splitlines():
    if line.startswith('#'):continue
    v=list(map(int,line.split()))
    a,b,c,d=v[2:6]
    groups=((a,b),(c,d))+tuple((h,) for h in range(2,9) if h not in (a,b,c,d))
    keys=[tuple(v[6+3*i:9+3*i]) for i in range(5)]
    p=tuple(sorted((h,keys[i],4 if keys[i][0]+keys[i][1]-h-1>=1 else 2)
                    for i,hs in enumerate(groups) for h in hs))
    rows.append((line,p))
counts={fam:len(words(*fam)) for line,p in rows for fam in p}
ranked=sorted(rows,key=lambda x:(sum(counts[k] for k in x[1]),-int(x[0].split()[0])))
assert len(ranked)==12356
solver=Path(sys.argv[1]) if len(sys.argv)>1 else S/'exact_or_mask_dp'
stop=int(sys.argv[2]) if len(sys.argv)>2 else 200
assert 1<=stop<=len(ranked)
evidence=[]
for i,(schedule,pairs) in enumerate(ranked[:stop]):
    inp,n,words_count=build_input(tuple((k,t) for h,k,t in pairs))
    proc=subprocess.run([str(solver),'80'],input=inp,text=True,capture_output=True,check=True)
    evidence.append({'rank':i,'schedule':schedule,'native_words':words_count,
       'trie_nodes':n,'input_sha256':hashlib.sha256(inp.encode()).hexdigest(),
       'receipt':proc.stdout.strip()})
out=Path(__file__).with_name('EC49EXZ_REPLAYED_BATCH.jsonl')
out.write_text(''.join(json.dumps(row)+'\n' for row in evidence))
print(json.dumps({'status':'PASS','cases':len(evidence),'below_80':sum('PASS min_extra=' in x['receipt'] for x in evidence),
  'at_least_80':sum('BOUND_PASS' in x['receipt'] for x in evidence)},indent=2))
