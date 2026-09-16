"""Exact derived test variant; retains the completed default-host evidence.

Enables the UPSTREAM numba optimization in both arms. All numerical cases,
thresholds, timestep and trial counts are unchanged. Both arms get an explicit
pre-timing warmup; the cost of that warmup is recorded rather than hidden.
"""
from pathlib import Path
import hashlib
import json
import os
import platform
import subprocess
import sys

root=Path(__file__).resolve().parent
source=(root/'host_validation.py').read_bytes()
assert hashlib.sha1(f'blob {len(source)}\0'.encode()+source).hexdigest() == '65e57df8f9cb790d88818d02867cb364d0c06bc4'
text=source.decode()
changes=[
("'--M', m, m, m, '--dealias',", "'--optimization', 'numba', '--M', m, m, m, '--dealias',"),
("out=HERE/'host_validation.json'", "out=HERE/'host_validation_numba.json'"),
("'dealias':'3/2-rule','nyquist_mask':True,", "'dealias':'3/2-rule','nyquist_mask':True,'native_optimization':'numba','upstream_fastmath_enabled':True,"),
("HERE/'host_validation.py'", "HERE/'host_validation_numba.py'"),
("trials={'fft':[],'hybrid':[]}; last={}", "warm_start=time.perf_counter()\n            trajectory(n,h,'fft'); trajectory(n,h,'hybrid')\n            case_warmup_seconds=time.perf_counter()-warm_start\n            trials={'fft':[],'hybrid':[]}; last={}"),
("row={**key,'comparisons':comparisons,'trials':trials,", "row={**key,'case_warmup_seconds':case_warmup_seconds,'comparisons':comparisons,'trials':trials,"),
("'first JIT warmup','disk output'", "'first pair-kernel JIT warmup','explicit both-arm per-case native optimization warmup','disk output'"),
("HERE/'host_validation_fatal.txt'", "HERE/'host_validation_numba_fatal.txt'"),
]
for old,new in changes:
    assert text.count(old)==1, (old,text.count(old))
    text=text.replace(old,new)
target=root/'host_validation_numba.py'
target.write_text(text)
meta={'schema':'CFD_OPTIMIZED_HOST_VARIANT_V1','base_test_git_blob':'65e57df8f9cb790d88818d02867cb364d0c06bc4','generated_test_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'variant_generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'native_optimization':'numba','upstream_sources_modified':False,'timed_cases_unchanged':True,'matched_tolerances':True,'warmup_both_arms':True,'cpu_count':os.cpu_count(),'processor':platform.processor(),'thread_env':{k:os.getenv(k) for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']}}
cpu=Path('/proc/cpuinfo')
if cpu.exists(): meta['cpu_model']=next((x.split(':',1)[1].strip() for x in cpu.read_text().splitlines() if x.startswith('model name')),None)
(root/'numba_variant_manifest.json').write_text(json.dumps(meta,indent=2)+'\n')
if '--generate-only' not in sys.argv:
    raise SystemExit(subprocess.call([sys.executable,str(target)]))
