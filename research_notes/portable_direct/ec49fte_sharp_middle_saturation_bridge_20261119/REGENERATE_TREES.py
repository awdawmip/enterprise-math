#!/usr/bin/env python3
"""Regenerate four EC49FTE original-index trees from the frozen native solver.

python REGENERATE_TREES.py /path/to/extracted/EC49FTE_SHARP_MIDDLE_SATURATION_BRIDGE_20261119 --out /tmp/trees
"""
import argparse, hashlib, json, sys
from fractions import Fraction as Q
from pathlib import Path
from collections import Counter

SAMPLES = {
    "Dmid": ("D", "49/64", "7/16", "1"),
    "Dhi": ("D", "4/5", "7/16", "1"),
    "Smain": ("S", "25/32", "7/16", "1"),
    "Tnonsat": ("S", "4/5", "7/16", "13/16"),
}
def main(root, out):
    root=Path(root).resolve()
    out=Path(out)
    out.mkdir(parents=True, exist_ok=True)
    cert=json.loads((Path(__file__).resolve().parent/"EXACT_CERT.json").read_text())
    sys.path.insert(0, str(root/"native_code"))
    from EC49FSA_THREE_OBSERVER_SOLVER import solve, V, PIN
    assert PIN==cert["frozen_source_commit"] and len(V)==228
    for w in cert["witness_trees"]:
        name=w["name"]
        ori,aa,bb,zz=SAMPLES[name]
        a,b,z=Q(aa),Q(bb),Q(zz)
        discounts={32:a,34:b,140:z} if ori=="D" else {32:b,34:a,140:z}
        info,tree=solve(discounts)
        data=(json.dumps(tree,sort_keys=True,ensure_ascii=False,separators=(",",":"))+"\n").encode()
        assert hashlib.sha256(data).hexdigest()==w["sha256"],name
        count=Counter()
        for i in range(141):
            node=tree
            seen=set()
            while "named_observer" in node:
                q=node["named_observer"]
                assert q not in seen
                seen.add(q)
                count[q]+=1
                node=node["children"][str(V[q][i])]
            assert node=={"leaf":i}
        assert [sum(count.values()),count[32],count[34],count[140]]==w["counts"]
        (out/(name+".json")).write_bytes(data)
        print("ORIGINAL_141_PROFILE_TREE_REGENERATED",name,w["sha256"],flush=True)
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("source_root")
    p.add_argument("--out",default="trees")
    args=p.parse_args()
    main(args.source_root,args.out)
