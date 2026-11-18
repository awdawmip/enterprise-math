#!/usr/bin/env python3
"""R5 sharp first mixed erasure/corruption + absolute analog noise threshold."""
import json,hashlib,sys
from pathlib import Path
sha="a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d"
raw=Path(sys.argv[1]).read_bytes(); assert hashlib.sha256(raw).hexdigest()==sha
src=json.loads(raw)
assert src["scientific_input"]=="435e77af0d180eac32bd1f9c4c464bc4010b7551"
C={}
for k in (214,223,294):
    a=[0]*256
    for t,v in src["all_budget_coefficients"][str(k)].items(): a[int(t)]=int(v)
    for bit in range(8):
        for b in range(256):
            if b&(1<<bit): a[b]+=a[b^(1<<bit)]
    C[k]=a
margin=min(max(abs(C[k][a]-C[k][b]) for k in C) for a in range(256) for b in range(a+1,256))
assert margin==76289178155959966960189440
saturating=[(a,b) for a in range(256) for b in range(a+1,256)
    if max(abs(C[k][a]-C[k][b]) for k in C)==margin]
assert len(saturating)==64 and (16,32) in saturating
assert len({tuple(C[k][b] for k in C) for b in range(256)})==256
print(json.dumps({"status":"PASS_R5_SHARP_MIXED_FAULT_LOW_ANALOG_NOISE",
 "min_max_gap":str(margin),"saturating_unordered_pairs":64,
 "mask_pair":[16,32],"low_noise_condition":"0<=2*eta<min_max_gap",
 "fixed_budget_formula":"731*(e+2*f+1)","adaptive_visible_erasure_budget_formula":"731+294*e"},indent=2))
