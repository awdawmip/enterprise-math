from os import environ
from pathlib import Path
from time import perf_counter_ns
from statistics import median
import repeated_tail as repeated
import shared_tail as shared

import sys
source_root = Path(environ["EM_SOURCE_ROOT"]).resolve()
sys.path[:0] = [str(source_root / "src"), str(source_root / "experiments")]
from brc_table_free_tail_benchmark import certified_start, source_state

for bits,degree,a,b in ((188,2,61,127),(1128,8,521,607),(3482,2,1279,2203),(3482,32,1279,2203)):
    n=(2**a-1)*(2**b-1)
    inputs=[]
    for h in (1,2):
        threshold=certified_start(n,degree,h)
        for i in range(16):
            m=threshold+i
            inputs.append((source_state(n,m),m+h))
    for s,t in inputs:
        assert vars(shared.transport_certified_tail(s,t,degree=degree))==vars(repeated.transport_certified_tail(s,t,degree=degree))
    times={module:[] for module in (shared,repeated)}
    ratios=[]
    for rep in range(21):
        order=(shared,repeated) if rep%2 else (repeated,shared)
        for mod in order:
            start=perf_counter_ns()
            for j in range(50):
                for s,t in inputs:
                    mod.transport_certified_tail(s,t,degree=degree)
            times[mod].append((perf_counter_ns()-start)/1600)
        ratios.append(times[repeated][-1]/times[shared][-1])
    print(bits,degree,round(median(times[repeated])),round(median(times[shared])),round(median(ratios),3),sum(r>1 for r in ratios),flush=True)
