#!/usr/bin/env python3
"""Re-run exact-native 96/49/48 Python integer timing (descriptive only)."""
import runpy, json
from pathlib import Path
from time import perf_counter_ns
from statistics import median
s=runpy.run_path(str(Path(__file__).with_name('PREFIX597_R2_compact_exact_checker.py')))
seq=[(tuple(1+((t+3*i)%4) for i in range(6)),t%6) for t in range(64)]
r0=[(7*i+1)%5 for i in range(96)]
methods={
 'literal576':lambda v,ss:s['direct'](v,ss),
 'optimized96':lambda v,ss:s['native_step'](v,*ss[0]) if len(ss)==1 else progressive(v,ss),
 'positive49':lambda v,ss:s['pos49'](v,ss),
 'tail48':lambda v,ss:s['tail'](v,ss),
 'tail48_sparse':lambda v,ss:s['sparse_tail'](v,ss),
}
def progressive(v,ss):
 for x,z in ss:v=s['native_step'](v,x,z)
 return v
rows=[]
for d in (2,8,32,64):
 expected=s['direct'](r0,seq[:d]);times={}
 for name,fn in methods.items():
  assert fn(r0,seq[:d])==expected,(name,d)
  observations=[]
  for _ in range(5):
   t=perf_counter_ns()
   assert fn(r0,seq[:d])==expected
   observations.append((perf_counter_ns()-t)/1000000)
  times[name]=round(median(observations),4)
 rows.append({'depth':d,'max_output_bit_length':max(k.bit_length() for k in expected),'median5_ms':times})
print(json.dumps({'schema':'PREFIX597_R2_REPLAY_TIMING','scientific_input':'f42f2906d77f24085c123f3ccfe9667d41caa96d','exact_full_output':True,'benchmarks':rows,'status':'PASS'},ensure_ascii=False,indent=2))
