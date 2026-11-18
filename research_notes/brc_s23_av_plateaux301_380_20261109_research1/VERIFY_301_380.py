#!/usr/bin/env python3
"""Reproduce S23/AV author-side endpoint certificates 301..380 in bounded slices."""
import argparse
import hashlib
import importlib.util
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "brc_s23_av_plateau20_20261108_r1" / "VERIFY_PLATEAUX20_200.py"
raw = p.read_bytes()
oid = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
assert oid == "261d7e22da0e62d667009cb50acfe77ac4e35c3f", oid
spec = importlib.util.spec_from_file_location("s23_predecessor", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
parser = argparse.ArgumentParser()
parser.add_argument("--start", type=int, default=301)
parser.add_argument("--end", type=int, default=380)
args = parser.parse_args()
assert 301 <= args.start <= args.end <= 380
total = 0
for i in range(args.start, args.end+1):
    x=m.check(i)
    assert x is not None,("coverage_failed",i)
    ix,H,M,n,bmax,cells,used,_=x
    a=m.get_witnesses(i)[-1][1]
    assert a*m.EU<i*m.DL and i*m.DU<(a+1)*m.EL
    assert ix==i
    total+=cells
    print("CERTIFIED_PLATEAU",ix,"H",H,"M",M,"narrow",n,"beta_bound",bmax,"critical_cells",cells,"witnesses_used",used,flush=True)
print("PASS_SEGMENT",args.start,args.end,"count",args.end-args.start+1,"cells",total,flush=True)
