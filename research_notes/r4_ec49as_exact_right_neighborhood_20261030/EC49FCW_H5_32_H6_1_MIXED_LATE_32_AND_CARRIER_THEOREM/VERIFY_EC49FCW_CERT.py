#!/usr/bin/env python3
"""Validate the committed lossless 32-row exact search certificate."""
import base64,gzip,hashlib,json
from pathlib import Path
p=Path(__file__).with_name("EC49FCW_FULL32.json.gz.b64")
raw=gzip.decompress(base64.b64decode(p.read_text().strip()))
assert hashlib.sha256(raw).hexdigest()=="e139eb9f36312795b8033979290769a4be8fdd923a58974796d893e1b2f2e96a"
j=json.loads(raw)
assert j["index_range"]==[1120,1152] and len(j["rows"])==32
assert j["dual_representation_checks"]==32 and j["all_optimum"]==158
for i,row in enumerate(j["rows"]):
    assert row["index"]==1120+i and row["slots"][:2]==["5:32","6:1"]
    assert row["literal"]=="PASS" and not row["result"]["improvement"]
    assert row["result"]["states"][-1]==0
    assert row["result"]["fixed"]+row["result"]["strict_cap"]==158
print("PASS: 32 rows, lossless checksum, recorded dual results")
