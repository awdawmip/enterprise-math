#!/usr/bin/env python3
"""Self-contained EC49EXX signed native X6 reproduction, optional --solve for 171 integer DP checks."""
from pathlib import Path
from collections import Counter
import base64,gzip,json,hashlib,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'
if not SRC.is_dir(): SRC=HERE/'pinned_sources'
sys.path.insert(0,str(SRC))
from SCREEN_H5_EC49EXJ import build_input
b=base64.b64decode((HERE/'EC49EXX_SELF_CONTAINED_180.json.gz.b64').read_text().strip())
rows=json.loads(gzip.decompress(b).decode())
assert len(rows)==180 and len({r[0] for r in rows})==180
assert Counter(r[1] for r in rows)=={0:26,1:130,2:24}
solve='--solve' in sys.argv;memo=set()
with tempfile.TemporaryDirectory() as td:
    exe=Path(td)/'or_mask_dp'
    if solve:
        subprocess.run(['g++','-O3','-std=c++17',str(SRC/'EXACT_OR_MASK_DP.cpp'),'-o',str(exe)],check=True)
    for idx,mode,schedule,nodes,colors,cutoff in rows:
        s=tuple((tuple(k),m) for k,m in schedule)
        k8,m8=s[-1];L8=2*(sum(k8)-1)
        I=lambda k:2*(sum(min(a,b) for a,b in zip(k,k8))-1)
        gain=m8*max(0,L8-max([L8-3]+[I(k) for k,m in s[:-1]]))
        assert cutoff==(76 if mode==0 else 80)
        assert (gain==4 if mode==0 else gain==0)
        inp,n,w=build_input(s if mode==2 else s[:-1])
        assert n==nodes and int(inp.splitlines()[0].split()[1])==colors,(idx,n,nodes,colors)
        digest=hashlib.sha256(inp.encode()).hexdigest()
        cachekey=(digest,cutoff)
        if solve and cachekey not in memo:
            p=subprocess.run([str(exe),str(cutoff)],input=inp,text=True,capture_output=True,check=True)
            expected=f'BOUND_PASS minimum_total_at_least={cutoff} nodes={nodes} colors={colors}'
            assert p.stdout.strip()==expected,(idx,p.stdout)
        memo.add(cachekey)
print(json.dumps({'status':'PASS','cases':len(rows),'unique_input_cutoffs':len(memo),
                  'mode_counts':dict(Counter(r[1] for r in rows)),'reran_solver':solve},sort_keys=True))
