#!/usr/bin/env python3
"""Exact R5 fixed-query erasure/corruption theorem verifier.
Usage: python VERIFY_R5_FIXED_ERASURE_CORRUPTION.py compact_stdout.json [EXACT_R5_ALL_101_BUDGETS.json]
"""
import hashlib, json, sys
from pathlib import Path
COMPACT_SHA="a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d"
FULL_SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
SOURCE_PIN="435e77af0d180eac32bd1f9c4c464bc4010b7551"

def verified(path, expected):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected, path
    return json.loads(raw)

def reconstruct(src):
    assert src["scientific_input"]==SOURCE_PIN
    assert src["budgets"]==[214,314] and src["masks"]==256
    c={}
    for k in range(214,315):
        a=[0]*256
        for t,v in src["all_budget_coefficients"][str(k)].items():
            a[int(t)]=int(v)
        assert all(v>=0 for v in a)
        for j in range(8):
            for b in range(256):
                if b&(1<<j): a[b]+=a[b^(1<<j)]
        c[k]=a
    return c

def main():
    if len(sys.argv) not in (2,3):
        raise SystemExit(__doc__)
    c=reconstruct(verified(sys.argv[1],COMPACT_SHA))
    crosscheck=len(sys.argv)==3
    if crosscheck:
        d=verified(sys.argv[2],FULL_SHA)
        for k in range(214,315):
            assert c[k]==list(map(int,d["counts_and_cohorts"][str(k)]["counts"])),k
    witness={"E":(16,17,214,221),"M":(16,80,223,291),"L":(16,32,294,313)}
    supports={}
    for name,(a,b,left,right) in witness.items():
        s=[k for k in range(214,315) if c[k][a]!=c[k][b]]
        assert s==list(range(left,right+1)),(name,s)
        supports[name]={"states":[a,b],"start":left,"end":right,"length":len(s)}
    assert len({tuple(c[k][b] for k in (214,223,294)) for b in range(256)})==256
    trials=[]
    for e,f in [(0,0),(1,0),(0,1),(1,1),(2,2)]:
        r=e+2*f+1
        q=[k for k in (214,223,294) for _ in range(r)]
        dmin=min(sum(c[k][a]!=c[k][b] for k in q)
                 for a in range(256) for b in range(a+1,256))
        assert dmin==r and sum(q)==731*r
        trials.append({"erasures":e,"corruptions":f,"queries":len(q),
                       "minimum_distance":dmin,"cost":sum(q)})
    output={
      "status":"PASS_R5_MIXED_ERASURE_CORRUPTION_EXACT_FIXED_SCHEDULE",
      "source_pin":SOURCE_PIN,"compact_sha256":COMPACT_SHA,
      "full_sha256":FULL_SHA if crosscheck else None,
      "full_table_crosschecked":crosscheck,
      "budget_count":101,"closure_masks":256,"counts_reconstructed":25856,
      "base_budgets":[214,223,294],"base_signature_count":256,
      "witness_supports":supports,
      "unbounded_exact_formula":"C_fixed(e,f)=731*(e+2*f+1) for all integers e,f>=0",
      "unique_optimal_multiset":"e+2*f+1 repeats of each of 214,223,294",
      "finite_trials":trials,
      "proof_kind":"general Hamming distance and disjoint-support weighted bound plus exhaustive finite exact witness and injectivity checks",
      "review":"NOT_REVIEWED"
    }
    print(json.dumps(output,indent=2,sort_keys=True))
if __name__=="__main__":main()
