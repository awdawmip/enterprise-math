#!/usr/bin/env python3
"""Exact S23/AV endpoint check, indices 221..300.
Run in an Enterprise Math checkout. Uses the prior proved critical-cell
reduction with its source at commit 19730a65ae527ed19cda441ccc0ed31b9d6f2639.
"""
from pathlib import Path
import importlib.util
root=Path(__file__).resolve().parents[1]
upstream=root/"brc_s23_av_plateau20_20261108_r1"/"VERIFY_PLATEAUX20_200.py"
spec=importlib.util.spec_from_file_location("s23_prior_exact_checker", upstream)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
results=[]
for i in range(221,301):
    row=module.check(i)
    assert row is not None, ("UNCOVERED_OR_MIXED_SIGN",i)
    ix,H,M,n,bmax,cells,usage,_=row
    assert ix==i
    results.append((i,H,M,n,bmax,cells,usage))
    print("PASS",i,H,M,n,bmax,cells,usage,flush=True)
assert len(results)==80
assert results[0][:3]==(221,84055896,458961026)
assert results[-1][:3]==(300,114102835,622887919)
assert max(r[3] for r in results)==92
assert max(r[5] for r in results)==43635
assert sum(r[5] for r in results)==2651142
print("PASS_S23_AV_PLATEAUX_221_TO_300",len(results),
      "new_integer_horizons",30427313,
      "critical_cells",2651142)
