#!/usr/bin/env python3
"""EC49FAC exact native X6/BRC strict-76 certificate replay.
Read published sibling EC49EXY TSV and EC49EXJ generator; no model substitution.
Usage: python3 REPLAY_EC49FAC.py /path/to/compiled/exact_or_mask_dp
"""
from pathlib import Path
import hashlib, subprocess, sys
R = Path(__file__).resolve().parent.parent
S = R / "EC49EXJ_H8_M4_S6_GLOBAL_EXACT"
X = R / "EC49EXY_H8_M5_EXACT_CROSS_FIBER_CAPS"
sys.path.insert(0, str(S))
from SCREEN_H5_EC49EXJ import words, build_input

rows=[]
for line in (X/"EC49EXY_DOUBLE_CANDIDATES.tsv").read_text().splitlines():
    if not line or line.startswith("#"): continue
    v=list(map(int,line.split())); a,b,c,d=v[2:6]
    groups=((a,b),(c,d))+tuple((h,) for h in range(2,9) if h not in (a,b,c,d))
    keys=[tuple(v[6+3*i:9+3*i]) for i in range(5)]
    p=tuple(sorted((h,keys[i],4 if keys[i][0]+keys[i][1]-h-1>=1 else 2)
        for i,hs in enumerate(groups) for h in hs))
    rows.append((line,p))
counts={fam:len(words(*fam)) for line,p in rows for fam in p}
ranked=sorted(rows,key=lambda x:(sum(counts[k] for k in x[1]),-int(x[0].split()[0])))
assert len(ranked)==12356
expected={}
for line in (Path(__file__).with_name("EC49FAC_CASE_RECEIPTS.tsv")).read_text().splitlines():
    if not line or line.startswith("#"):continue
    i,h,status=line.split()
    assert status=="BOUND_PASS:76"
    expected[int(i)]=h
assert len(expected)==75
solver=Path(sys.argv[1]).resolve()
for rank,sha in sorted(expected.items()):
    line,p=ranked[rank]
    source,n,word_count=build_input(tuple((k,t) for h,k,t in p))
    assert hashlib.sha256(source.encode()).hexdigest()==sha,(rank,"INPUT_DRIFT")
    r=subprocess.run([str(solver),"76"],input=source,text=True,capture_output=True,check=True)
    assert r.stdout.startswith("BOUND_PASS minimum_total_at_least=76 "), (rank,r.stdout)
    print(rank,sha,r.stdout.strip())
print("EC49FAC_VERIFIED_PASS cases=75 strict_cutoff=76")
