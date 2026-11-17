#!/usr/bin/env python3
"""EC49FRJ direct named BRC terminal-observer fiber checker.

Run from the complete self-contained archive code/ directory. Requires its
original frozen source and EC49FQI_NATIVE_DATA parser; no Bellman computations.
"""
from pathlib import Path
import sys,hashlib,json,collections
B=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(B/"code"))
from EC49FQI_NATIVE_DATA import V,reps,weights,MASTER,CSV,PIN
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(B/"source/frozen_original_master.txt")==MASTER
assert sha(B/"source/EC49FPG_PROFILE.csv")==CSV
assert len(V)==228 and all(len(v)==141 for v in V)
assert len(reps)==len(weights)==141 and sum(weights)==310
fibers=collections.defaultdict(list)
for i in range(141):
    fibers[tuple(V[q][i] for q in range(144))].append(i)
pairs=sorted((v for v in fibers.values() if len(v)>1),key=lambda v:v[0])
assert len(fibers)==139 and pairs==[[8,139],[46,140]]
witness=[]
for i,j in pairs:
    assert weights[i]==weights[j]==1
    assert all(V[q][i]==V[q][j] for q in range(144))
    distinguishing=[q for q in range(144,228) if V[q][i]!=V[q][j]]
    assert distinguishing==list(range(148,164))
    signature=[V[q][i] for q in range(144)]
    h=hashlib.sha256(json.dumps(signature,separators=(",",":")).encode()).hexdigest()
    witness.append({"pair":[i,j],"original_representatives":[reps[i],reps[j]],"multiplicities":[weights[i],weights[j]],"signature_sha256":h,"root_distinguishing_queries":distinguishing,"root_148_responses":[V[148][i],V[148][j]]})
assert [w["original_representatives"] for w in witness]==[[17928,38165],[24541,38166]]
assert [w["signature_sha256"] for w in witness]==[
    "459efc71c5edd35e17e4af59e04d6ded59fcdea3b2490b95e1707548cc691bd1",
    "2422bf2e88480d75ca011075b53dc9a6829636ebefb2b585a482d31f2a4b690a"]
assert [w["root_148_responses"] for w in witness]==[[66,62],[66,64]]
print("EC49FRJ terminal observer fiber PASS: 139 signatures; two pairs; sharp Ru>=4 Rm>=4")
