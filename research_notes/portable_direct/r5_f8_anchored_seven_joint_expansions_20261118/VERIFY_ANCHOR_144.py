#!/usr/bin/env python3
"""Verify R5 f=8 mask-144 complete anchored seven-state certificate.
Compile VERIFY_SEVEN.cpp as ./verify_seven; supply frozen count table.
--spot 4 replays the first 4 models at each endpoint; --all replays all 500.
"""
import argparse,base64,hashlib,json,subprocess,zlib
from pathlib import Path
from RECOMPUTE_ANCHORED_SEVEN import H0,L,U,PIN_SHA256,actions
POSSIBLE=[i for i in range(256) if i not in H0 and i!=144]
def rows(cert,side):
    raw=zlib.decompress(base64.b64decode(cert[side+"_encoded"]))
    assert hashlib.sha256(raw).hexdigest()==cert[side+"_row_sha256"]
    data=json.loads(raw)
    assert len(data)==250 and [r[0] for r in data]==POSSIBLE
    assert all(r[1]==8335 and r[2]>0 for r in data)
    assert sum(r[2] for r in data)==cert[side+"_aggregate_states"]
    return data
def solve(counts,mask,tau,exe):
    acts=actions(counts,H0+(144,mask),tau)
    inp=f"7 {len(acts)}\n"
    for k,sups in acts:
        inp+=f"{k} {len(sups)} "+' '.join(map(str,sups))+"\n"
    z=subprocess.run([str(exe),"8"],input=inp,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True,timeout=60)
    d=dict(p.split("=",1) for p in z.stdout.split() if "=" in p)
    return [mask,int(d["V"]),int(d["states"]),int(d["actions"])]
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True,type=Path)
    p.add_argument("--certificate",type=Path,default=Path("RESULTS_ANCHOR_144_COMPACT.json"))
    p.add_argument("--solver",type=Path,default=Path("./verify_seven"))
    p.add_argument("--spot",type=int,default=0)
    p.add_argument("--all",action="store_true")
    a=p.parse_args()
    assert hashlib.sha256(a.input.read_bytes()).hexdigest()==PIN_SHA256
    c=json.loads(a.certificate.read_text())
    assert c["anchor"]==144 and c["H0"]==list(H0) and c["f"]==8
    values={side:rows(c,side) for side in ("left","right")}
    n=250 if a.all else a.spot
    assert 0<=n<=250
    if n:
        t=json.loads(a.input.read_text())["counts_and_cohorts"]
        counts={k:[int(v) for v in t[str(k)]["counts"]] for k in range(214,315)}
        exe=a.solver.resolve()
        assert exe.is_file()
        for side,tau in (("left",L),("right",U-1)):
            for expected in values[side][:n]:
                assert solve(counts,expected[0],tau,exe)==expected,(side,expected)
    print("PASS_R5_F8_ANCHOR_144_250_MODELS_BOTH_ENDPOINTS",n)
if __name__=="__main__":
    main()
