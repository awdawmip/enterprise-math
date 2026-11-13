#!/usr/bin/env python3
"""Execute unchanged exact critical-cell checker at selected S23/AV indices.
From the repository root: python research_notes/brc_s23_av_plateaux401_410_two_candidate_inverse_20261109_r1/VERIFY_401_410.py 401
Run small disjoint ranges to preserve completed evidence under runtime limits.
"""
import hashlib, importlib.util, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/"research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py"
raw=SOURCE.read_bytes()
blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
assert blob=="261d7e22da0e62d667009cb50acfe77ac4e35c3f", ("pinned_checker_source_changed",blob)
spec=importlib.util.spec_from_file_location("s23_pinned_checker", SOURCE)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
assert len(sys.argv)>=2, "pass one or more indices 401..410"
for arg in sys.argv[1:]:
    i=int(arg)
    assert 401<=i<=410
    result=mod.check(i)
    assert result is not None, ("coverage_failed",i)
    ix,H,M,n,bmax,cells,used,items=result
    assert ix==i
    print("CERTIFIED_PLATEAU",ix,"H",H,"M",M,"narrow",n,"beta_bound",bmax,
          "critical_cells",cells,"witnesses_used",used,flush=True)
print("PASS_SELECTED_INDICES",",".join(sys.argv[1:]),flush=True)
