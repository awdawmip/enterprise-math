"""Independently verify the exact witness and summarize measured, immutable logs.

No original pilot archive or SciPy required for this deterministic step.
"""
import hashlib
import json
import math
import statistics
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def digest(name):
    return hashlib.sha256((HERE/name).read_bytes()).hexdigest()


def summary(block,methods):
    assert len(block['orders'])==5 and set(block['runs'])==set(methods)
    assert all(sorted(order)==sorted(methods) for order in block['orders'])
    out = {}
    for method, runs in block['runs'].items():
        assert len(runs)==5
        for run in runs:
            rows = run['frames']
            assert len(rows)==12 and run['setup_s']>=0
            assert math.isclose(run['s'], run['setup_s']+sum(row['s'] for row in rows), abs_tol=1e-9)
            for row in rows:
                assert row['s']>0 and row['r']>=0 and row['e']>=0
                assert row['ok']==(row['e']<=1e-4 and row['r']<=1e-3 and row.get('info',0)==0)
                if method=='trigger':
                    assert row['bound']<=1e-4 and row['checks']>=1
                    # Finite arithmetic consistency check, not an outward error certificate.
                    assert row['e']<=row['bound']+1e-12
            assert all(x['ok']==y['ok'] for x,y in zip(rows,runs[0]['frames']))
        seconds = [run['s'] for run in runs]
        single = [run['setup_s']+run['frames'][0]['s'] for run in runs]
        flat = [row for run in runs for row in run['frames']]
        med_ms = 1000*statistics.median(seconds)
        out[method] = {
            'ms_12_frames_median':round(med_ms,3),
            'ms_amortized_per_frame':round(med_ms/12,3),
            'ms_one_shot_median':round(1000*statistics.median(single),3),
            'ms_12_frames_range':[round(1000*min(seconds),3),round(1000*max(seconds),3)],
            'passes_over_all_60':sum(row['ok'] for row in flat),
            'max_goal_error':max(row['e'] for row in flat),
            'max_true_residual':max(row['r'] for row in flat),
        }
        if method=='trigger':
            out[method]['each_run_decisions'] = dict(Counter(r['d'] for r in runs[0]['frames']))
            for run in runs:
                assert dict(Counter(r['d'] for r in run['frames']))==out[method]['each_run_decisions']
    return out


def main():
    plan = json.loads((HERE/'pressure_plan.json').read_text())
    primary = json.loads((HERE/'pressure_timings.json').read_text())
    controls = json.loads((HERE/'pressure_controls_timings.json').read_text())
    assert primary['bench_sha256']==controls['bench_sha256']==digest('pressure_bench.py')
    assert primary['plan_sha256']==digest('pressure_plan.json')
    assert controls['script_sha256']==digest('pressure_controls.py')
    assert primary['source_zip_sha256']==controls['source_zip_sha256']==plan['source_sha256']
    assert primary['source_manifest_files_verified']==34
    exact = json.loads(subprocess.check_output([sys.executable,str(HERE/'pressure_exact.py')],text=True))
    assert exact['rank2_cancellation']['qoi_error']=='-10101/270241'
    assert exact['rank2_cancellation']['true_relative_residual_squared']=='16/96004127'
    main_comparison = {}
    extra = {}
    for n in map(str,plan['grids']):
        grid = primary['grids'][n]
        assert grid['selected_tol']==0.001
        main_comparison[n] = {}
        extra[n] = {}
        for name in plan['cases']:
            report = summary(grid['cases'][name],plan['methods'])
            best = min(v['ms_12_frames_median'] for k,v in report.items()
                       if k!='trigger' and v['passes_over_all_60']==60)
            trigger = report['trigger']
            trigger['relative_to_fastest_other_qualified'] = round(trigger['ms_12_frames_median']/best,5)
            trigger['predeclared_20pct_win'] = trigger['passes_over_all_60']==60 and trigger['ms_12_frames_median']<=0.8*best
            main_comparison[n][name] = report
            methods = ['static_lu','trigger'] + ([] if name=='smooth' else ['face_lu'])
            extra[n][name] = summary(controls['grids'][n][name],methods)
    out = {
        'scope':'finite fixed model; timing files are measurements, not deterministic rerun promises',
        'raw_primary_sha256':digest('pressure_timings.json'),
        'raw_controls_sha256':digest('pressure_controls_timings.json'),
        'plan_sha256':primary['plan_sha256'],'archive_sha256':plan['source_sha256'],
        'archived_private_members_verified':34,'source_zip_members':35,'environment':primary['environment'],
        'max_process_rss_kib_primary_controls':[primary['whole_process_max_rss_kib'],controls['whole_process_max_rss_kib']],
        'primary_frames':1800,'additional_frames':960,'exact_witnesses':exact,
        'predeclared':main_comparison,'post_primary_controls':extra,
    }
    print(json.dumps(out,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
