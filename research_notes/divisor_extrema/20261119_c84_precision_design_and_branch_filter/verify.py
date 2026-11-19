"""C84 reproducibility entry point.

Default: fast exact identities, certificate arithmetic, and saved finite-result
checks. --full additionally regenerates the expensive certificates and complete
physical catalogues in a temporary copy. Analytic proofs remain in Markdown.
"""
from argparse import ArgumentParser
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
from time import perf_counter
import numpy as np
import sympy
import mpmath

ROOT=Path(__file__).resolve().parent
SCIENCE_JSON=['finite/one_third_certificate.json','finite/one_dimensional_values.json',
              'finite/endpoint_values.json','position/native_position_comparison.json',
              'position/global_tail_exploration.json',
              'branches/six_branch_gap_certificate.json','triangle/certificate.json']


def digest(path):return sha256(path.read_bytes()).hexdigest()
def read(relative):return json.loads((ROOT/relative).read_text())
def module(relative,name):
    path=ROOT/relative;sys.path.insert(0,str(path.parent))
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def main():
    p=ArgumentParser(description=__doc__);p.add_argument('--full',action='store_true');p.add_argument('--output',type=Path,default=ROOT/'checks.json');args=p.parse_args()
    assert sys.flags.optimize==0,'Run without -O: scientific scripts use assertions.'
    start=perf_counter();checks=[]
    original={r:digest(ROOT/r) for r in SCIENCE_JSON if (ROOT/r).exists()}
    def check(name,action):
        begun=perf_counter()
        try:row={'name':name,'status':'passed','details':action()}
        except Exception as e:row={'name':name,'status':'failed','error':repr(e)}
        row['elapsed_seconds']=round(perf_counter()-begun,6);checks.append(row)
        print(name,row['status'],flush=True)
    def program(relative):
        command=[sys.executable,str(ROOT/relative)]
        result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
        if result.returncode:raise RuntimeError(f'{relative}: exit {result.returncode}\n{result.stdout}\n{result.stderr}')
        return {'command':command,'exit_code':result.returncode,'stdout':result.stdout.strip(),
                'stderr':result.stderr.strip(),'program_sha256':digest(ROOT/relative)}
    for relative in ['finite/verify_one_dimensional.py','finite/verify_certificate.py',
                     'position/check_position.py','branches/verify_branch_identities.py',
                     'branches/verify_triangle_tail_series.py']:
        check(relative,lambda r=relative:program(r))

    def branch_corners():
        m=module('branches/certify_six_branch_gap.py','c84_branch_check')
        r=read('branches/six_branch_gap_certificate.json')['target_rectangle']
        hlo,hhi=map(F,r['h_interval']);ulo,uhi=map(F,r['G_over_C_interval'])
        for row in r['roots']:
            side={'left':0,'right':1}[row['side']];dlo,dhi=map(F,row['d_interval'])
            increasing=row['segment']!='second negative-lobe root'
            if increasing:
                assert m.compare_u(dlo,side,hhi,ulo)<0
                assert m.compare_u(dhi,side,hlo,uhi)>0
            else:
                assert m.compare_u(dlo,side,hlo,uhi)>0
                assert m.compare_u(dhi,side,hhi,ulo)<0
        return {'boxes':6,'fresh_exact_boundary_signs':12,
                'full_root_isolation_recomputed':False,
                'scope':'Exact signs at saved rectangle box endpoints; monotonic branch classification is proved analytically.'}
    check('six_branch_rectangle_corner_signs',branch_corners)

    def position_counts():
        data=read('position/native_position_comparison.json');rows=data['cases']
        assert [(x['c'],x['outer_gap']) for x in rows]==[(8,4),(64,16),(256,64)]
        for x in rows:
            c,B=x['c'],x['outer_gap']
            assert x['n']==c*(c-1)//2 and x['read_intervals']==4*x['n']
            assert x['stocks']==[c,c+B//4,c+B//2,c+B]
            assert x['interval_bits']==176
            assert x['rational_enclosures']==(112 if c==8 else 0)
            ps=sorted({o['p'] for o in x['outcomes']})
            for prec in ps:
                block=[o for o in x['outcomes'] if o['p']==prec]
                assert len(block)==8
                assert {tuple(o['origins_halves']) for o in block}==set(product(range(2),repeat=3))
                for o in block:
                    assert 0<=o['endpoint']<=min(o['quarter'],o['midpoint'])<=max(o['quarter'],o['midpoint'])<=x['n']
                    same=[u for u in block if u['origins_halves'][0]==o['origins_halves'][0] and u['origins_halves'][2]==o['origins_halves'][2]]
                    assert len({u['endpoint'] for u in same})==1
            assert len({w['kind'] for w in x['witnesses']})==len(x['witnesses'])
            for w in x['witnesses']:
                assert w['kind'] in ['quarter_only','midpoint_only']
                assert w['source'] in w['same_losing_cell_labels']
                assert len(w['same_losing_cell_labels'])>=2
                assert all(2<=v[1]<=v[0]<=c for v in w['same_losing_cell_labels'])
        large=rows[-1]
        low=[o for o in large['outcomes'] if o['p']==10]
        high=[o for o in large['outcomes'] if o['p']==20]
        assert max(o['quarter'] for o in low)<min(o['midpoint'] for o in low)
        assert max(o['midpoint'] for o in high)<min(o['quarter'] for o in high)
        assert sum(x['n'] for x in rows)==34684
        assert sum(x['read_intervals'] for x in rows)==138736
        return {'catalogue_arrangements':34684,'read_intervals':138736,
                'origin_precision_rows':sum(len(x['outcomes']) for x in rows),
                'reversal_inventory':256,'low_p':10,'high_p':20,
                'physical_catalogues_recomputed':False,
                'scope':'Saved finite counts, endpoint consistency and strict count reversal; no new full catalogue generation.'}
    check('saved_physical_position_results',position_counts)

    def native_source():
        expected={'position/critical_bins.py':'a6e3afd2affbe6728469b09f8ab1bf9e8367cda4fcefd3de89a2ede77d8cda34',
                  'position/native.py':'2d0ea55c826fbb28f4bb3de39d12269d8f8e7ce624afb50873ea4de94dcec6fa'}
        assert all(digest(ROOT/p)==h for p,h in expected.items())
        return {'identical_original_evaluator_sha256':expected,
                'source':'C82 immutable science commit 4628b5b87d2cf41a385228ad04bf163c06aa6586; reused by C83/C84.'}
    check('original_finite_evaluator_sources',native_source)

    triangle_available=all((ROOT/p).exists() for p in ['TRIANGLE_CONSTANT.md','triangle/certificate.json','triangle/certify_constant.py'])
    # The triangle module's quick verification interface is connected when its
    # final certificate is present; no pending output is silently counted as a pass.
    if triangle_available:
        def triangle_certificate():
            m=module('triangle/certify_constant.py','c84_triangle_certificate')
            if not hasattr(m,'verify_saved_certificate'):
                raise RuntimeError('Triangle certificate exists but its quick verification interface is not yet connected.')
            return m.verify_saved_certificate(ROOT/'triangle/certificate.json')
        check('triangle_constant_certificate',triangle_certificate)

    if args.full:
        with tempfile.TemporaryDirectory(prefix='c84-full-reproduction-') as t:
            copy=Path(t)/'C84';shutil.copytree(ROOT,copy,ignore=shutil.ignore_patterns('__pycache__'))
            def full_run(relative,arguments,output):
                command=[sys.executable,str(copy/relative)]+arguments
                r=subprocess.run(command,cwd=copy,capture_output=True,text=True)
                if r.returncode:raise RuntimeError(f'{relative}: exit {r.returncode}\n{r.stdout}\n{r.stderr}')
                got=json.loads((copy/output).read_text());wanted=read(output)
                for key in ['elapsed_seconds','seconds']:
                    got.pop(key,None);wanted.pop(key,None)
                assert got==wanted
                return {'command':command,'exit_code':0,'matches_saved_result':output,'stdout':r.stdout.strip()}
            check('full_one_third_2048_grid',lambda:full_run('finite/certify_one_third.py',['--grid','2048','--output',str(copy/'finite/one_third_certificate.json')],'finite/one_third_certificate.json'))
            check('full_six_branch_isolation',lambda:full_run('branches/certify_six_branch_gap.py',[],'branches/six_branch_gap_certificate.json'))
            check('full_native_position_catalogues',lambda:full_run('position/native_reading_compare.py',[],'position/native_position_comparison.json'))
            if triangle_available:
                def full_triangle():
                    d=read('triangle/certificate.json')
                    return full_run('triangle/certify_constant.py',
                                    ['--mesh',str(d['area_mesh_per_unit']),
                                     '--tail-mesh',str(d['tail_mesh_per_unit']),
                                     '--output',str(copy/'triangle/certificate.json')],
                                    'triangle/certificate.json')
                check('full_triangle_constant',full_triangle)

    def preserved():
        assert all(digest(ROOT/r)==h for r,h in original.items())
        return {'scientific_json_files_unchanged':len(original)}
    check('scientific_results_preserved',preserved)
    result={'description':'C84 scoped reproducibility checks','mode':'full' if args.full else 'quick',
            'scope_note':'The analytic theorems are proved in the Markdown notes. Program checks cover only their explicit identities, named certificates and finite data.',
            'triangle_certificate_available':triangle_available,
            'pending_components':[] if triangle_available else ['triangle_constant_certificate'],
            'environment':{'python':sys.version,'numpy':np.__version__,'sympy':sympy.__version__,'mpmath':mpmath.__version__,'platform':platform.platform(),'python_optimization':sys.flags.optimize},
            'checks':checks,'passed':sum(x['status']=='passed' for x in checks),
            'failed':sum(x['status']=='failed' for x in checks),'elapsed_seconds':round(perf_counter()-start,6),
            'finished_utc':datetime.now(timezone.utc).isoformat(),
            'input_sha256':{str(p.relative_to(ROOT)):digest(p) for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and (p.suffix=='.py' or str(p.relative_to(ROOT)) in SCIENCE_JSON)}}
    result['status']='passed' if result['failed']==0 else 'failed'
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    if result['failed']:raise SystemExit(1)

if __name__=='__main__':main()
