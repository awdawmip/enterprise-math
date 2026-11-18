#!/usr/bin/env python3
"""Exact native tree witness replayer and optional independent original-family Bellman check."""
import argparse,base64,hashlib,json,sys,zlib
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native-dir",required=True)
    ap.add_argument("--certificate",default="EC49FSL_THREE_PRICE_SWAP_MACHINE_CERTIFICATE.json")
    ap.add_argument("--trees",default="EC49FSL_FOUR_NATIVE_SWAP_TREES_JSON_ZLIB_BASE64.txt")
    ap.add_argument("--full-bellman",action="store_true")
    args=ap.parse_args()
    data=json.loads(Path(args.certificate).read_text())
    assert data["science_pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
    sys.path.insert(0,args.native_dir)
    from EC49FQI_NATIVE_DATA import V,PIN
    assert PIN==data["science_pin"] and len(V)==228 and all(len(v)==141 for v in V)
    trees=json.loads(zlib.decompress(base64.b64decode(Path(args.trees).read_text().strip())))
    assert len(trees)==len(data["points"])==4
    for point in data["points"]:
        tree=trees[point["case"]]
        assert hashlib.sha256(json.dumps(tree,sort_keys=True,separators=(",",":")).encode()).hexdigest()==point["tree_sha256"]
        cnt=Counter();depth=0
        for state in range(141):
            node=tree;seen=set();d=0
            while "named_observer" in node:
                q=node["named_observer"]
                assert 0<=q<228 and q not in seen
                cnt[q]+=1;d+=1;seen.add(q)
                node=node["children"][str(V[q][state])]
            assert node=={"leaf":state}
            depth=max(depth,d)
        assert tree["named_observer"]==point["root"]
        assert depth==point["max_depth"]
        assert (sum(cnt.values()),cnt[32],cnt[34],cnt[140])==(point["U"],point["N32"],point["N34"],point["N140"])
        costs={q:F(point[k]) for q,k in [(32,"a"),(34,"b"),(140,"z")]}
        total=F(point["U"])-sum(costs[q]*cnt[q] for q in costs)
        assert total==F(point["F"])
        if args.full_bellman:
            from EC49FSA_THREE_OBSERVER_SOLVER import solve
            from EC49FSA_FSB_INDEPENDENT_CHECK import certify
            best,_=solve(costs)
            assert F(best["numerator"],best["denominator"])==total==F(certify(costs)["value"])
        print("PASS",point["case"],total,"root",point["root"],"depth",depth,flush=True)
    by={p["case"]:F(p["F"]) for p in data["points"]}
    assert by["A"]-by["B"]==F(81,16)>0
    assert by["control_A"]==by["control_B"]==F(3481,16)
    print("PASS: exact third-observer induced price-swap asymmetry 81/16; 4 complete trees")

if __name__=="__main__":
    main()
