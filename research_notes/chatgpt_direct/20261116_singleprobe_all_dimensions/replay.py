"""Replay the four audits and the original components. Python 3.12+, C++17, POPCNT."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import os
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
SCIENCE=ROOT/'science'
JOBS=[('full/verify_nine.py',['--all-histories'],'full/nine_results.json'),
      ('paired/final_paired.py',['--full'],'paired/final_paired_results.json'),
      ('common/common_class_audit.py',[],'common/common_class_results.json'),
      ('native_probes.py',[],'final_native.json'),
      ('common/native_common.py',[],'common/native_common_results.json')]

def replay(item):
    script,flags,reference=item
    env=dict(os.environ,PYTHONPATH=str(ROOT))
    output=subprocess.check_output([sys.executable,'-B',str(SCIENCE/script),*flags],cwd=ROOT,env=env)
    assert json.loads(output)==json.loads((SCIENCE/reference).read_text()),reference
    return reference

if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:
        for path in pool.map(replay,JOBS): print('PASS',path,flush=True)
