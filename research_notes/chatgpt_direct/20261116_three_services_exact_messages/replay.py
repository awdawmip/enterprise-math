"""Clean replay. Python 3.12+, C++17, unsigned 128-bit integers, POPCNT."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json,os,subprocess,sys

ROOT=Path(__file__).resolve().parent
SCIENCE=ROOT/'science'
JOBS=[
    ('check_eleven.py','eleven_results.json'),
    ('native_check.py','native_eleven.json'),
    ('mixed/check_mixed.py','mixed/result.json'),
    ('mixed/native_mixed.py','mixed/native_result.json'),
    ('saturated/saturated_cases.py','saturated/saturated_result.json'),
    ('reflection/replay_reflection.py','reflection/reflection_result.json'),
]
JOBS.extend([('cost/core_cost.py','cost/core_cost_results.json'),
             ('supplement/five_cores.py','supplement/five_cores_results.json')])


def replay(job):
    script,record=job
    raw=subprocess.check_output([sys.executable,'-B',str(SCIENCE/script)],cwd=ROOT,
                                env=dict(os.environ,PYTHONPATH=str(ROOT)))
    assert json.loads(raw)==json.loads((SCIENCE/record).read_text()),record
    return record


if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:
        for record in pool.map(replay,JOBS):print('PASS',record,flush=True)
