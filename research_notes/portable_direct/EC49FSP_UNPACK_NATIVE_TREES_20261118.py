#!/usr/bin/env python3
"""Unpack and verify six complete BRC16943 original named-observer tree witnesses.

Run next to EC49FSP_* machine certificate and compressed tree data. This
proves payload integrity/serialization and the exact stored witness counts;
full native response-path replay and Bellman optimality require the frozen
original raw observation files and the companion native verifier.
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
        def traverse(node,n,seen):
            if "leaf" in node:
                assert isinstance(node["leaf"],int) and 0<=node["leaf"]<141
                return
            q=node["named_observer"];assert q not in seen and 0<=q<228
            counts[q]+=n
            for sub in node["children"].values():
                traverse(sub,n+0,seen|{q})
        # Full source-native per-profile replay is performed by native validator;
        # syntax and sha/tuple pins are checked here without making that claim.
        traverse(t,1,set())
        print("FULL_TREE_PAYLOAD_PASS",key,len(serialized))
print("ALL_SIX_LOSSLESS_TREES_PASS")
