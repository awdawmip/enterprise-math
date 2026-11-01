#!/usr/bin/env python3
"""R467 exact author-side right-edge certificate reproduction; reuse the published R466 mathematical kernel."""
import importlib.util
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / 'r466_signed_brc_right_edge_193_200_20261102_emr3' / 'R465_EXECUTED_REPRODUCE.py'
spec = importlib.util.spec_from_file_location('r467_reused_kernel', PRIOR)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
expected = {r['s']:r for r in json.loads((HERE/'R467_EVIDENCE.json').read_text())['rows']}
lo = int(sys.argv[1]) if len(sys.argv)>1 else 201
hi = int(sys.argv[2]) if len(sys.argv)>2 else 208
assert 201<=lo<=hi<=208
for s in range(lo,hi+1):
    got = mod.core.s_certificate(s,detail=True)
    ref = expected[s]
    for key in ('k0','r_min','degree_p2','degree_p3','strict_positive_coefficients','sha256'):
        assert got[key]==ref[key],(s,key,got[key],ref[key])
    print('R467_CERTIFICATE_PASS',s,got['sha256'],flush=True)
print('R467_AUTHOR_EXACT_PASS',lo,hi,flush=True)
