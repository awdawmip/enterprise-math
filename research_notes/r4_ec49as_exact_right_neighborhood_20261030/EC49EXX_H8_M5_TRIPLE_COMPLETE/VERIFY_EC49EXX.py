#!/usr/bin/env python3
"""EC49EXX: verify full 180-case raw evidence using the existing signed X6 native generator.
Run after extracting the EC49EXX_COMPLETE_EVIDENCE.tar.gz archive, or place the
original full EC49EXX_EXACT_CERTIFICATES.json.gz.b64 next to this file.
For repository layout, the source sibling is EC49EXJ_H8_M4_S6_GLOBAL_EXACT.
Optional --solve recompiles/reruns all 171 distinct C++ exact OR-mask instances.
"""
from pathlib import Path
from collections import Counter
import base64, gzip, json, hashlib, subprocess, sys, tempfile
HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "EC49EXJ_H8_M4_S6_GLOBAL_EXACT"
if not SRC.is_dir():
    SRC = HERE / "pinned_sources"
sys.path.insert(0, str(SRC))
from SCREEN_H5_EC49EXJ import build_input
FULL = HERE / "EC49EXX_EXACT_CERTIFICATES.json.gz.b64"
if not FULL.exists():
    raise SystemExit("Full raw 180-case ledger needed: extract EC49EXX_COMPLETE_EVIDENCE.tar.gz")
packed = base64.b64decode(FULL.read_text().strip())
rows = json.loads(gzip.decompress(packed).decode("utf-8"))["records"]
assert len(rows) == 180 and len({r["index"] for r in rows}) == 180
assert Counter(r["mode"] for r in rows) == {"H7_KEY_TAIL":26,"H7_MONOTONE":130,"H8_FULL":24}
solve = "--solve" in sys.argv
unique = {}
with tempfile.TemporaryDirectory() as tmp:
    exe = Path(tmp) / "or_mask_dp"
    if solve:
        subprocess.run(["g++","-O3","-std=c++17",str(SRC/"EXACT_OR_MASK_DP.cpp"),"-o",str(exe)],check=True)
    for r in rows:
        s = tuple((tuple(k),m) for k,m in r["schedule"])
        k8,m8 = s[-1]
        L8 = 2*(sum(k8)-1)
        overlap = lambda k: 2*(sum(min(a,b) for a,b in zip(k,k8))-1)
        g = m8*max(0,L8-max([L8-3]+[overlap(k) for k,m in s[:-1]]))
        assert r["mode"] in {"H7_KEY_TAIL","H7_MONOTONE","H8_FULL"}
        assert r["cutoff"] == (76 if r["mode"]=="H7_KEY_TAIL" else 80)
        if r["mode"]=="H7_KEY_TAIL": assert g==4
        else: assert g==0
        chosen = s if r["mode"]=="H8_FULL" else s[:-1]
        data,nodes,words=build_input(chosen)
        assert hashlib.sha256(data.encode()).hexdigest() == r["input_sha256"]
        assert nodes==r["nodes"]
        assert int(data.splitlines()[0].split()[1])==r["colors"]
        expected=f'BOUND_PASS minimum_total_at_least={r["cutoff"]} nodes={nodes} colors={r["colors"]}'
        assert r["stdout"]==expected
        key=(r["input_sha256"],r["cutoff"])
        if solve and key not in unique:
            proc=subprocess.run([str(exe),str(r["cutoff"])],input=data,text=True,capture_output=True,check=True)
            assert proc.stdout.strip()==expected, (r["index"],proc.stdout)
        unique[key]=True
print(json.dumps({"status":"PASS","cases":len(rows),"unique_inputs":len(unique),
                  "mode_counts":dict(Counter(r["mode"] for r in rows)),
                  "input_sha_verified":True,"reran_solver":solve},sort_keys=True))
