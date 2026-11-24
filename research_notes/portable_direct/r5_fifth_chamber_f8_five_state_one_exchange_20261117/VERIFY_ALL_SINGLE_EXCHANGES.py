#!/usr/bin/env python3
"""Exact f=8 one-exchange census for frozen R5 centers; Python3 stdlib + C++17."""
import base64
import collections
import hashlib
import json
import subprocess
import zlib
from pathlib import Path

P=Path(__file__).resolve().parent
cert=json.loads((P/"RESULTS_COMPACT.json").read_text())
raw=(P/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()==cert["counts_sha256"]
T=json.loads(raw)["counts_and_cohorts"]
H0=tuple(cert["H0"])
L=int(cert["tau_left"])
f=cert["f"]
assert len(H0)==5 and set(map(int,T))==set(range(214,315))
assert all(len(row["counts"])==256 for row in T.values())

def maximal_supports(values,tau):
    by_value={}
    for j,v in enumerate(values):
        by_value[v]=by_value.get(v,0)|(1<<j)
    possible=set()
    for start in by_value:
        possible.add(sum(bits for value,bits in by_value.items()
                         if start<=value<=start+tau))
    return tuple(sorted(a for a in possible
                        if not any(a!=b and (a&b)==a for b in possible)))

rows=[]
for i in range(5):
    for h in range(256):
        if h in H0:
            continue
        H=H0[:i]+(h,)+H0[i+1:]
        families={}
        for k in range(214,315):
            counts=T[str(k)]["counts"]
            fam=maximal_supports([int(counts[q]) for q in H],L)
            families.setdefault(fam,k)
        lines=[f"5 {len(families)}"]
        for fam,k in sorted(families.items(),key=lambda pair:pair[1]):
            lines.append(f"{k} {len(fam)} "+" ".join(map(str,fam)))
        (P/"_actions.tmp").write_text("\n".join(lines)+"\n")
        p=subprocess.run([str(P/"verify_exact_small"),str(P/"_actions.tmp"),str(f)],
                         capture_output=True,text=True,check=True)
        d=dict(part.split("=",1) for part in p.stdout.split() if "=" in part)
        rows.append(dict(replace_index=i,new_mask=h,V=int(d["V"]),
                         states=int(d["states"]),actions=len(families)))

levels=cert["value_levels"]
indices=bytes(levels.index(r["V"]) for r in rows)
assert indices==zlib.decompress(base64.b64decode(
    cert["per_neighbor_level_indices_zlib_base64"]))
assert hashlib.sha256(indices).hexdigest()==cert["value_indices_sha256"]
full_digest=hashlib.sha256(",".join(
    f"{r['replace_index']}:{r['new_mask']}:{r['V']}:{r['states']}:{r['actions']}"
    for r in rows).encode()).hexdigest()
assert full_digest==cert["extended_rows_digest_sha256"]
assert len(rows)==1255 and max(r["V"] for r in rows)==8326
assert dict(sorted(collections.Counter(r["V"] for r in rows).items()))=={
    int(k):v for k,v in cert["histogram"].items()}
print("PASS_R5_F8_ALL_1255_FIVE_STATE_SINGLE_EXCHANGES",
      "max=8326","H0=8335","rows=1255")
(P/"ALL_1255_RECOMPUTED.json").write_text(json.dumps(rows,indent=2)+"\n")
(P/"_actions.tmp").unlink(missing_ok=True)
