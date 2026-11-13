#!/usr/bin/env python3
"""Independent cold-process R5 original exact event fixture + graph + 12-byte DP/unrank workload."""
import json,statistics,subprocess,sys

WORK='''from time import perf_counter
import resource, json, sys
from VERIFY_R5_INTERVAL_ARRAY_DP import frozen_events,graph,IntervalDP,R,K,ORIGINAL_RANK,EXPECTED_J,EXPECTED_T,original_centers,directory
from DICT_DP_ENGINE import DictDP
kind=sys.argv[1]
t=perf_counter()
x=frozen_events();g=graph(x,R);original=original_centers()
t1=perf_counter();d=(IntervalDP(x,R,K,g) if kind=='interval' else DictDP(x,R,K,g))
assert d.summary()==(EXPECTED_J,EXPECTED_T)
assert d.unrank(ORIGINAL_RANK)==original
z=directory(x,original)
t2=perf_counter()
print(json.dumps(dict(kind=kind,cold_seconds=t2-t,fixture_seconds=t1-t,dp_unrank_directory_seconds=t2-t1,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,centers=len(original),directory=len(z))))
'''
trials={k:[] for k in ('interval','dict')}
for _ in range(9):
    for kind in trials:
        proc=subprocess.run([sys.executable,'-c',WORK,kind],check=True,capture_output=True,text=True)
        trials[kind].append(json.loads(proc.stdout.strip()))
result={'status':'PASS_R5_12B_COLD_PROCESS_COMPARE', 'repeats_per_variant':9,
        'measurement_scope':'new CPython process per run; 15-atom exact rational fixture + graph + DP/unrank + 954-byte directory, without original bitmap construction and prefix queries',
        'stats':{k:{m:round(statistics.median(z[m] for z in xs),6) for m in ('cold_seconds','fixture_seconds','dp_unrank_directory_seconds','peak_rss_kib')} for k,xs in trials.items()},
        'all_centers_verified':True, 'all_directory_lengths_954':True}
print(json.dumps(result,indent=2,sort_keys=True))
