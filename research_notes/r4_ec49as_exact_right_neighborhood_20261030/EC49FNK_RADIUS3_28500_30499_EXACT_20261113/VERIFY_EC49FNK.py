#!/usr/bin/env python3
"""Verify the repository-contained lossless EC49FNK exact finite certificate.

For full 178850-word catalogue and native C++ rerun, use full evidence bundle.
This checks the published 2000-cost vector, original word legality and
signed ordered native-prefix witnesses, complete root DP tables, all 256
third-root exchange costs for each of three minimizing configurations.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import base64, hashlib, json, zlib

HERE = Path(__file__).resolve().parent
cert = json.loads((HERE / "EXACT_CERTIFICATE_EC49FNK.json").read_text())
table = json.loads((HERE / "ROOT_TABLES_EC49FNK.json").read_text())
def unpack(s):
    return json.loads(zlib.decompress(base64.b85decode(s)).decode("utf-8"))
assert cert["pin"] == table["pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert cert["interval"] == {"start":28500,"end_exclusive":30500,"count":2000,"total":38169}
v = unpack(cert["costs_zlib_b85"])
assert len(v) == 2000 and all(isinstance(x,int) for x in v)
assert min(v)==cert["minimum"]==86
assert [28500+i for i,x in enumerate(v) if x==86]==cert["minimum_indices"]==[30266,30393,30396]
assert max(v)==cert["maximum"]==222
assert [28500+i for i,x in enumerate(v) if x==222]==cert["maximum_indices"]==[29146]
sha = hashlib.sha256(("\n".join(map(str,v))+"\n").encode()).hexdigest()
assert sha == cert["hashes"]["newline_cost_vector_sha256"], (sha,cert["hashes"])
OPS = "acdefg"
STATE = ((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
         (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
         (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG = (0,0,4,1,16,32,8,2,0)
STEP = {"a":(-1,-1),"c":(1,2,-1,-2),"d":(2,1,-2,-1),
        "e":(3,1,1,-3),"f":(1,-1),"g":(2,-2)}
REQ = {2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
       6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
expected_labels = {(h,s) for h,ss in REQ.items() for s in ss}
def inspect(label,word):
    assert len(word)==label[0]
    q=0; cell=[0]*6; signed_prefix=b""; out=[]
    for c in word:
        assert c in OPS
        q=STATE[q][OPS.index(c)]
        assert q!=8
        for d in STEP[c]:
            cell[abs(d)-1] += 1 if d>0 else -1
            signed_prefix += bytes((d+4,))
            out.append(signed_prefix)
    assert SIG[q]==label[1] and cell==[2,0,0,0,0,0]
    return out
diff={}
for ix in cert["minimum_indices"]:
    case=cert["cases"][str(ix)]
    assert case["keys"]=={
       30266:[0,4,5,11,32,34,49],
       30393:[0,4,5,11,32,46,49],
       30396:[0,4,5,11,32,46,61]}[ix]
    words=case["words"]
    assert len(words)==24 and {tuple(x["label"]) for x in words}==expected_labels
    allp=set()
    for item in words:
        allp.update(inspect(item["label"],item["word"]))
    assert len(allp)==86, (ix,len(allp))
    rt={int(k):t for k,t in unpack(table["exact_root_tables"][str(ix)]["tables_zlib_b85"]).items()}
    assert set(rt)=={5,6,7}
    assert [rt[5]["costs"][-1],rt[6]["costs"][-1]]==[43,43]
    Q=rt[7]["labels"]; assert len(Q)==8 and len(set(Q))==8
    gaps=[]; third=[]; saved=[]
    for m in range(256):
        T={Q[j] for j in range(8) if m>>j&1}
        save=0
        for r in (5,6):
            labels=rt[r]["labels"];cs=rt[r]["costs"]
            assert len(cs)==(1<<len(labels))
            rem=sum(1<<j for j,l in enumerate(labels) if l not in T)
            save+=cs[-1]-cs[rem]
        third.append(rt[7]["costs"][m])
        saved.append(save)
        gaps.append(third[-1]-save)
    assert len(rt[7]["costs"])==256
    assert gaps==unpack(case["exchange_gaps_zlib_b85"])
    assert gaps[0]==0 and min(gaps[1:])==8
    assert [m for m in range(1,256) if gaps[m]==8]==[85,170,255]
    env=[min(third[m] for m in range(1,256) if m.bit_count()==k)
         -max(saved[m] for m in range(1,256) if m.bit_count()==k)
         for k in range(1,9)]
    assert env==case["envelopes"]
    diff[ix]=gaps
    print("PASS",ix,"86 signed prefixes, 8 strict root-gap, envelopes",env)
for a,b in combinations(cert["minimum_indices"],2):
    x=diff[a];y=diff[b]
    actual=[sum(i>j for i,j in zip(x,y)),sum(i==j for i,j in zip(x,y)),sum(i<j for i,j in zip(x,y))]
    assert actual==cert["gap_compare"][f"{a}_vs_{b}"]
print("CERTIFICATE_PASS",len(v),"exact costs, argmin",cert["minimum_indices"])
