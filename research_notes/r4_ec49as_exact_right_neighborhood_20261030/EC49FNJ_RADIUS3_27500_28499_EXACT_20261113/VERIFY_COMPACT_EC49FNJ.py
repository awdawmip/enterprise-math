#!/usr/bin/env python3
"""EC49FNJ: check 1,000 lossless costs, lawful native-X6 word witnesses;
optionally recheck exact 8-cardinality envelopes from complete rootfunc_*.txt.
Run: python VERIFY_COMPACT_EC49FNJ.py
Place frozen source and root-function files alongside for additional checks.
"""
import base64, hashlib, json, zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = json.loads((HERE / "EXACT_COMPACT_EC49FNJ.json").read_text())
assert D["frozen_scientific_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
vec = json.loads(zlib.decompress(base64.b85decode(D["costs_zlib_b85"])))
assert len(vec) == 1000 and min(vec) == 115 and max(vec) == 138
assert [27500+i for i,v in enumerate(vec) if v == 115] == [27511,27523]
assert vec.count(138) == 712
assert hashlib.sha256(("\n".join(map(str,vec))+"\n").encode()).hexdigest() == D["cost_decimal_sha256"]

# Frozen operation types: six ordered signed-native paths, no unsigned quotient.
OPS = "acdefg"
T = ((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
     (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
     (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG = (0,0,4,1,16,32,8,2,0)
STEPS = {"a":(-1,-1),"c":(1,2,-1,-2),"d":(2,1,-2,-1),
         "e":(3,1,1,-3),"f":(1,-1),"g":(2,-2)}
def prefixes(word):
    p = b""; out = []
    for ch in word:
        for ax in STEPS[ch]:
            p += bytes([ax+4]); out.append(p)
    return out
def check_grammar_word(label,word):
    h,signature=label
    assert len(word)==h and all(ch in OPS for ch in word)
    q=0; pos=[0]*6
    for ch in word:
        q=T[q][OPS.index(ch)]
        assert q!=8
        for ax in STEPS[ch]:
            pos[abs(ax)-1]+=1 if ax>0 else -1
    assert SIG[q]==signature and pos==[2,0,0,0,0,0]
    return True

labels = D["labels_by_root"]
A = D["base_witness_case_27511"]
B = D["second_witness_case_27523"]
for case in (27511,27523):
    w = A if case==27511 else B
    pairs=[];by_root={}
    for root in ("05","06"):
        words=A["ordered_lawful_words_"+root].copy()
        if case==27523:
            for lab,value in B["reuse_base_words_except"].get(root,{}).items():
                target=tuple(map(int,lab.split(",")))
                words[labels[root].index(list(target))]=value
        assert len(words)==len(labels[root])==12
        sub=list(zip(labels[root],words))
        assert all(check_grammar_word(label,word) for label,word in sub)
        by_root[root]=len({p for label,word in sub for p in prefixes(word)})
        pairs+=sub
    assert len({tuple(lab) for lab,_ in pairs})==24
    assert by_root=={"05":52,"06":63},by_root
    assert len({p for label,word in pairs for p in prefixes(word)})==115
    assert vec[case-27500]==115
    print("LEGAL_WORDS_PREFIXES_PASS",case,"cost",115,"root_costs",by_root)

assert D["shadow_transfer"]["case_27511"]["envelopes_by_cardinality_k1_to_k8"] == [4,2,2,2,3,4,9,13]
assert D["shadow_transfer"]["case_27523"]["envelopes_by_cardinality_k1_to_k8"] == [5,2,2,2,3,4,9,13]
assert all(min(D["shadow_transfer"]["case_"+str(i)]["envelopes_by_cardinality_k1_to_k8"])>=2 for i in (27511,27523))
print("LOSSLESS_VECTOR_AND_WITNESS_PASS",len(vec),"minima",[27511,27523],"max138_count",712)

# Full finite exclusion-gap proof check from the *original* exact root function data.
for case in (27511,27523):
    p=HERE/("rootfunc_%d.txt"%case)
    if not p.exists():
        print("ROOT_TABLE_REDERIVATION_PENDING",case,"provide full original rootfunc file")
        continue
    assert hashlib.sha256(p.read_bytes()).hexdigest() == D["shadow_transfer"]["case_"+str(case)]["root_table_sha256"]
    f={}
    for line in p.read_text().splitlines():
        a,b,c=line.strip().split()
        lab=[int(v) for v in b.split(",") if v]
        val=[int(v) for v in c.split(",") if v]
        assert len(val)==(1<<len(lab))
        f[int(a)]=(lab,val)
    assert set(f)=={5,6,7}
    Q=f[7][0]
    assert Q==D["shadow_transfer"]["root07_label_indices"]
    G=[];cost=[];savings=[]
    for mask in range(256):
        transfer={Q[j] for j in range(8) if mask>>j&1}
        saved=0
        for r in (5,6):
            labs,dp=f[r]
            retain=sum(1<<j for j,x in enumerate(labs) if x not in transfer)
            saved+=dp[-1]-dp[retain]
        c=f[7][1][mask]
        cost.append(c);savings.append(saved);G.append(c-saved)
    envelope=[min(cost[m] for m in range(1,256) if m.bit_count()==k)
              -max(savings[m] for m in range(1,256) if m.bit_count()==k)
              for k in range(1,9)]
    assert envelope==D["shadow_transfer"]["case_"+str(case)]["envelopes_by_cardinality_k1_to_k8"]
    assert G[0]==0 and min(G[1:])==2 and [m for m in range(1,256) if G[m]==2]==[60]
    assert G[60]==2
    print("EXACT_ROOT_ENVELOPE_PASS",case,envelope,"unique_minimal_nonempty_mask",60)
