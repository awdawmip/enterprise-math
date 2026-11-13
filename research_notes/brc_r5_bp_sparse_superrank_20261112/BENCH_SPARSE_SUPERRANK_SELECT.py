#!/usr/bin/env python3
"""Python 3 stdlib microbenchmark: 2,880 frozen preorder opening selects.
Run after VERIFY_R5_BP_SPARSE_SUPERRANK.py's standalone equivalent is available:
  R5_LOCAL_CORPUS_SCRIPT=/path/to/r5_bp_sparse_rank.py python BENCH_SPARSE_SUPERRANK_SELECT.py
This evaluator executes that exact local script, so DO NOT claim runnable GitHub
integration without installing it. Frozen BP stream may instead be supplied by
the pinned VERIFY_R5_BP_WAVELET_PORTABLE.py as shown in the research note.
"""
from bisect import bisect_right
from statistics import median
from time import perf_counter_ns
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json, os, runpy

script=os.environ.get('R5_LOCAL_CORPUS_SCRIPT')
if script:
    with redirect_stdout(StringIO()):
        ctx=runpy.run_path(script)
    bp=ctx['bp']
else:
    # Standalone repository checkout: recover frozen BP from pinned model
    # through the already verified original-corpus script.
    import sys
    base=Path(__file__).resolve().parents[1]/'brc_r5_bp_wavelet_prefix_20261112'
    sys.path.insert(0,str(base))
    with redirect_stdout(StringIO()):
        import VERIFY_R5_BP_WAVELET_PORTABLE as baseline
    bp=baseline.bp

N=len(bp)//2
assert N==2880 and len(bp)==5760
B=64; J=90; suffix=28987
opens=[pos for pos,bit in enumerate(bp) if bit]
results=[]
for G in (1,2,4,8,16,32,90):
    anchors=[sum(bp[:j*B]) for j in range(0,J,G)]
    def select(i):
        k=bisect_right(anchors,i)-1
        rank=anchors[k]
        for pos in range(k*G*B,len(bp)):
            if bp[pos]:
                if rank==i: return pos
                rank+=1
        raise AssertionError(i)
    assert [select(i) for i in range(N)]==opens
    durations=[]
    for _ in range(5):
        t=perf_counter_ns()
        checksum=0
        for i in range(N):
            checksum+=select(i)
        durations.append((perf_counter_ns()-t)/N)
    assert checksum==sum(opens)
    bits=2*N+J*7+len(anchors)*12+suffix
    results.append({'G':G,'anchors':len(anchors),'bits':bits,
                    'bytes':(bits+7)//8,
                    'select_ns_median_per_node':round(median(durations),1),
                    'checksum':checksum})
print(json.dumps(results,indent=2))
