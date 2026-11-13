#!/usr/bin/env python3
"""Gray-code O(1) subset accumulator with exact frozen-R5 event frontiers."""
import argparse
import importlib.util
import json
import statistics
import time
import tracemalloc
import resource
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('frozen_frontier',HERE/'VERIFY_LINEAR_FRONTIER.py')
F=importlib.util.module_from_spec(spec)
spec.loader.exec_module(F)

def gray_events():
    w=F.WEIGHTS; k0=F.K0
    pools={3:set(),12:set(),15:set()}
    mask=0;n=0;k=0
    for i in range(1,1<<len(w)):
        j=(i&-i).bit_length()-1
        bit=1<<j
        mask^=bit
        if mask & bit:
            n-=w[j]; k-=k0[j]
        else:
            n+=w[j]; k+=k0[j]
        # In every iteration, mask equals i xor (i>>1).
        assert mask == (i ^ (i >> 1))
        if n>=3 and k%36==0:
            q=k//36
            if q in pools:pools[q].add(n)
    assert [len(pools[q]) for q in (3,12,15)] == [538,298,229]
    ratios=Counter(Fraction(n,q) for q in pools for n in pools[q])
    assert len(ratios)==953 and Counter(ratios.values())=={1:869,2:56,3:28}
    E=[0]
    for z in sorted(ratios): E.append(E[-1]+ratios[z])
    assert len(E)==954 and E[-1]==1065
    return E

def gray_events_fast():
    w=F.WEIGHTS; k0=F.K0
    pools={3:set(),12:set(),15:set()}
    mask=0;n=0;k=0
    for i in range(1,1<<len(w)):
        j=(i&-i).bit_length()-1
        bit=1<<j
        mask^=bit
        if mask & bit:
            n-=w[j]; k-=k0[j]
        else:
            n+=w[j]; k+=k0[j]
        if n>=3 and k%36==0:
            q=k//36
            if q in pools:pools[q].add(n)
    ratios=Counter(Fraction(n,q) for q in pools for n in pools[q])
    E=[0]
    for z in sorted(ratios):E.append(E[-1]+ratios[z])
    return E

METHODS={'baseline':F.frozen_events,'recurrence':F.fast_frozen_events,'gray':gray_events_fast}

def child(method,r):
    f=METHODS[method]
    t0=time.perf_counter_ns()
    tracemalloc.start()
    x=f()
    tbuild=time.perf_counter_ns()
    got=F.linear_midpoint_dp(x,r)[0]
    dt=time.perf_counter_ns()
    _,peak=tracemalloc.get_traced_memory()
    tracemalloc.stop()
    out={'method':method,'R':r,'K':got[0][0],'J':got[0][1],
         'ways':str(got[1]),'boundary_count':len(x),'event_count':x[-1],
         'build_ms':(tbuild-t0)/1e6,'build_and_dp_ms':(dt-t0)/1e6,
         'python_peak_bytes':peak,'rss_kb':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    print(json.dumps(out))

def parent():
    expected=F.frozen_events()
    assert F.fast_frozen_events()==expected==gray_events()==gray_events_fast()
    for r in (0,1,2,9,25,26,36):
        opt=F.linear_midpoint_dp(expected,r)[0]
        assert F.linear_midpoint_dp(gray_events_fast(),r)[0]==opt
    timings={m:[] for m in METHODS}
    full={m:[] for m in METHODS}
    for i in range(13):
        order=list(METHODS)
        if i%3==1:order=order[1:]+order[:1]
        if i%3==2:order=order[2:]+order[:2]
        for name in order:
            t=time.perf_counter_ns();x=METHODS[name]();timings[name].append((time.perf_counter_ns()-t)/1e6)
            assert x==expected
            t=time.perf_counter_ns();y=F.linear_midpoint_dp(x,2)[0]
            full[name].append((time.perf_counter_ns()-t)/1e6)
            assert y[0]==(213,1070)
    mem={}
    for method in METHODS:
        snapshots=[]
        for _ in range(5):
            tracemalloc.start()
            arr=METHODS[method]()
            _,peak=tracemalloc.get_traced_memory()
            tracemalloc.stop()
            assert arr==expected
            snapshots.append(peak)
        mem[method]=statistics.median(snapshots)
    separate={}
    for method in METHODS:
        rows=[]
        for _ in range(5):
            completed=subprocess.run([sys.executable,str(Path(__file__).resolve()),'child',method,'2'],capture_output=True,text=True,check=True)
            rows.append(json.loads(completed.stdout))
        assert len({(x['K'],x['J'],x['ways'],x['boundary_count'],x['event_count']) for x in rows})==1
        separate[method]={'median_build_ms_tracemalloc':statistics.median(row['build_ms'] for row in rows),
                           'median_pipeline_ms_tracemalloc':statistics.median(row['build_and_dp_ms'] for row in rows),
                           'median_peak_allocated_bytes':statistics.median(row['python_peak_bytes'] for row in rows),
                           'median_maxrss_kb':statistics.median(row['rss_kb'] for row in rows)}
    print(json.dumps({'status':'PASS_GRAY_EXACT', 'frozen_pin':F.PIN,'all_events_identical':True,
                      'single_process':{'median_build_ms':{k:round(statistics.median(v),4) for k,v in timings.items()},
                                        'median_dp_ms':{k:round(statistics.median(v),4) for k,v in full.items()},
                                        'median_build_peak_allocated_bytes':mem},
                      'fresh_process_R2':separate,
                      'experimental_scope':'event build and linear DP only; no full prefix-query trie'},indent=2))

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='child':child(sys.argv[2],int(sys.argv[3]))
    else:parent()
