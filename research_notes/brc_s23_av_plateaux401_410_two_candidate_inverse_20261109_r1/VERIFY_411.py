#!/usr/bin/env python3
"""Run the byte-pinned exact S23/AV critical-cell checker at index 411."""
import hashlib, importlib.util
from pathlib import Path
root=Path(__file__).resolve().parents[2]
source=root/"research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py"
data=source.read_bytes()
digest=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
assert digest=="261d7e22da0e62d667009cb50acfe77ac4e35c3f",digest
spec=importlib.util.spec_from_file_location("s23_original",source)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
ret=mod.check(411)
assert ret is not None, "coverage_failed_411"
i,H,M,n,bmax,cells,used,_=ret
assert (i,H,M,n,bmax,cells,used)==(411,156320715,853215848,126,412,81910,51)
print("CERTIFIED_PLATEAU",i,"H",H,"M",M,"narrow",n,"beta_bound",bmax,
      "critical_cells",cells,"witnesses_used",used)
print("PASS_SEGMENT_411_411")
