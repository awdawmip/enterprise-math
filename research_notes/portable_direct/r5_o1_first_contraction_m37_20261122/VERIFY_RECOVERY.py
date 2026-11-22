#!/usr/bin/env python3
"""Independent extension of R5 finite-field witness computation to m=37..44.
Imports the same exact five-event evaluator; no external packages."""
import json
from pathlib import Path
from VERIFY_MODULAR import calc, W, L

rows=[]
for m in range(37,45):
    rr=[calc(m,d) for d in W]
    passing=[r["d"] for r in rr if r["witness"]]
    expected=W[:-1] if m<=43 else W
    assert passing == expected, (m,passing,expected)
    assert rr[-1]["R0"] == (0 if m<=43 else 10275)
    assert L == 229746052653717600
    rows.extend(rr)
    print("PASS",m,"witnesses",len(passing), "d43_R0",rr[-1]["R0"],flush=True)

out={
  "schema":"R5_O1_M37_44_RECOVERY_CERT_V1",
  "fixed_science":"enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15",
  "thresholds":[37,38,39,40,41,42,43,44],
  "root_orders":W,
  "rows":rows,
  "limitation":"Exact complex root43 cancellation for 37..43 is proved analytically in RESEARCH.md; mod-p zero is not sufficient for zero."
}
Path(__file__).with_name("R5_O1_M37_44_RECOVERY.json").write_text(json.dumps(out,sort_keys=True,indent=2)+"\n",encoding="utf-8")
print("ALL CHECKS PASS",len(rows),"modular pairs")
