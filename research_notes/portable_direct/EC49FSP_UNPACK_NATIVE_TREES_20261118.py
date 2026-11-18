#!/usr/bin/env python3
"""Unpack/verify six original BRC16943 named-observer tree witnesses.

Reads the machine certificate and compressed tree data from this GitHub folder.
Checks compressed bytes, canonical tree hashes, all 141 distinct leaves and
the path-use count vectors. To validate named response edges and global Bellman
optimality, use the source-native checker with frozen original observations.
"""
import base64,hashlib,json,zlib
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
C=json.loads((HERE/"EC49FSP_NATIVE_BRC_PRICE_SWAP_CORNER_MACHINE_CERT_20261118.json").read_text())
B64=(HERE/"EC49FSP_SIX_FULL_NATIVE_TREES_ZLIB_BASE64_20261118.txt").read_text().strip()
Z=base64.b64decode(B64,validate=True)
assert hashlib.sha256(Z).hexdigest()=="5ad5532a425d326d23bd07c75cf5cba386e54bca95cb18cce027bf74c9c8def1"
RAW=zlib.decompress(Z)
assert hashlib.sha256(RAW).hexdigest()=="5ae336ef641609af5da34bb8ce849634c31b24bbe3c126f392ebac363bd746da"
assert len(RAW)==24626
trees=json.loads(RAW)
assert len(trees)==6
for orient,rows in C["phases"].items():
    for r in rows:
        key=("D" if orient=="direct" else "S")+"_"+"_".join(map(str,r["witness"]))
        assert key in trees
        t=trees[key]
        serialized=json.dumps(t,sort_keys=True,separators=(",",":"),ensure_ascii=False)
        assert hashlib.sha256(serialized.encode()).hexdigest()==r["tree_sha256"]
        counts=Counter()
        def visit(node,used):
            if "leaf" in node:
                s=node["leaf"]
                assert isinstance(s,int) and 0<=s<141
                return {s}
            q=node["named_observer"]
            assert isinstance(q,int) and 0<=q<228 and q not in used
            groups=[visit(sub,used|{q}) for sub in node["children"].values()]
            assert len(groups)>1
            leaves=set()
            for g in groups:
                assert not (leaves&g)
                leaves|=g
            counts[q]+=len(leaves)
            return leaves
        assert visit(t,set())==set(range(141))
        assert (sum(counts.values()),counts[32],counts[34],counts[140])==tuple(r["witness"])
        print("FULL_TREE_STRUCTURE_AND_COUNTS_PASS",key)
print("ALL_SIX_LOSSLESS_TREES_PASS")
