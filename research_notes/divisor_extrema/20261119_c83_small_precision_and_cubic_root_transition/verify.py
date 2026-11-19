"""C83 reproducibility entry point; default mode performs scoped quick checks.

Run --full to repeat the 512-grid certificate, all finite inventories and the
million-sample exploratory experiment.  No mode formally verifies the analytic
proofs.  Floating quadrature and Monte Carlo outputs remain non-certified.
"""
from argparse import ArgumentParser
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from itertools import product
import json
from math import isclose, isfinite, sqrt
from pathlib import Path
import platform
import subprocess
import sys
from time import perf_counter

import numpy as np
import sympy

ROOT = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def read_json(relative):
    return json.loads((ROOT/relative).read_text())


def module(relative, name):
    path = ROOT/relative
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true')
    parser.add_argument('--output', type=Path, default=ROOT/'checks.json')
    args = parser.parse_args()
    assert sys.flags.optimize == 0, 'Run without -O: the scientific scripts use assertions.'
    started = perf_counter()
    initial = {str(p.relative_to(ROOT)): digest(p) for p in ROOT.rglob('*.json')
               if p.name != 'checks.json'}
    checks = []

    def check(name, action):
        begin = perf_counter()
        try:
            details = action()
            row = {'name': name, 'status': 'passed', 'details': details}
        except Exception as exc:
            row = {'name': name, 'status': 'failed', 'error': repr(exc)}
        row['elapsed_seconds'] = round(perf_counter()-begin, 6)
        checks.append(row)
        print(name, row['status'], flush=True)

    def program(relative):
        command = [sys.executable, str(ROOT/relative)]
        p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if p.returncode:
            raise RuntimeError(f'{relative}: exit {p.returncode}\n{p.stdout}\n{p.stderr}')
        return {'command': command, 'exit_code': p.returncode,
                'stdout': p.stdout.strip(), 'stderr': p.stderr.strip(),
                'program_sha256': digest(ROOT/relative)}

    check('small_covolume_symbolic_identities', lambda: program('haar/check_small_asymptotics.py'))
    check('transition_curvature_and_slice_identities', lambda: program('critical/verify_transition.py'))
    check('finite_direction_exact_inner_integrals', lambda: program('haar/finite_direction_integral.py'))
    check('finite_direction_event_examples', lambda: program('haar/check_direction_events.py'))

    def regenerated():
        paths = ['critical/transition_checks.json', 'haar/direction_event_checks.json']
        assert all(digest(ROOT/p) == initial[p] for p in paths)
        event = read_json(paths[1])
        assert event['lattice_phase_cases'] == 8000
        assert sum(event['direction_histogram'].values()) == 8000
        assert event['direction_histogram']['3'] > 0
        return {'byte_identical_outputs': paths, 'exact_lattice_phase_cases': 8000,
                'scope': 'Exact finite examples and explicit identities; not the general analytic proof.'}
    check('regenerated_exact_outputs_match', regenerated)

    tail = module('tail/certify_constant.py', 'c83_tail')
    certificate = read_json('tail/constant_certificate.json')

    def certificate_arithmetic():
        assert certificate['grid'] == 512
        assert certificate['t0'] == '33/40'
        plo, phi = map(F, certificate['pi_interval'])
        aa, bb = tail.arctan_bounds(5), tail.arctan_bounds(239)
        assert plo < 16*aa[0]-4*bb[1] < 16*aa[1]-4*bb[0] < phi
        klo, khi = F(161, 80)/phi**2, F(161, 80)/plo**2
        tlo, thi = tail.twentieth_root_bounds(1, 2)
        tlo, thi = F(tlo, tail.ROOT_PRECISION), F(thi, tail.ROOT_PRECISION)
        assert tlo**20 <= F(1,2) <= thi**20
        mlo, mhi = [F(certificate['capped_minkowski_moment'][k]) for k in ('lower','upper')]
        ilo = mlo+klo*(F(40,19)*tlo-2*tail.T0)
        upper_lower_expression = mhi+khi*(F(40,19)*thi-2*tail.T0)
        assert ilo == F(certificate['improved_I3_lower_bound_expression']['lower'])
        assert upper_lower_expression == F(certificate['improved_I3_lower_bound_expression']['upper'])
        slo, shi = tail.twentieth_root_bounds(43, 200)
        slo, shi = F(slo,tail.ROOT_PRECISION), F(shi,tail.ROOT_PRECISION)
        assert slo**20 <= F(43,200) <= shi**20
        ihi = shi-F(8,465)*slo**31+khi*slo**(-19)/19
        assert ihi == F(certificate['I3_enclosure']['upper'])
        wlo, whi = tail.prefactor_bounds()
        assert [wlo,whi] == [F(certificate['high_precision_prefactor'][k]) for k in ('lower','upper')]
        alo, ahi = wlo*ilo, whi*ihi
        assert alo == F(certificate['A3_enclosure']['lower'])
        assert ahi == F(certificate['A3_enclosure']['upper'])
        assert F(73486,100000) < alo < ahi < F(820351,1000000)
        gap = wlo*F(49,760)*tlo/phi**2
        assert gap == F(certificate['outer_endpoint_leading_constant_gap_lower']['exact'])
        assert gap > F(533290878,10**11)
        return {'stored_grid': 512, 'grid_512_recomputed': False,
                'fresh_computations': ['Machin pi enclosure', 'Gamma-based prefactor enclosure',
                                       'twentieth-root inequalities', 'all final Fraction arithmetic'],
                'A3_outward_interval': certificate['A3_enclosure']['short_outward_interval'],
                'scope': 'Reconstructed from stored 512-grid moment endpoints; does not independently regenerate those endpoints.'}
    check('tail_certificate_exact_final_arithmetic', certificate_arithmetic)

    def coarse_tail():
        f0, f1 = tail.face_bounds(8,0), tail.face_bounds(8,1)
        lo, hi = 2*f0[0]+f1[0], 2*f0[1]+f1[1]
        fine_lo, fine_hi = [F(certificate['capped_minkowski_moment'][k]) for k in ('lower','upper')]
        assert lo <= fine_lo <= fine_hi <= hi
        return {'fresh_grid': 8, 'stored_grid': 512,
                'coarse_interval_display': [float(lo),float(hi)],
                'stored_interval_inside_fresh_coarse_interval': True,
                'scope': 'Fresh small-grid enclosure and nesting consistency, not a 512-grid rerun.'}
    check('tail_fresh_coarse_grid_enclosure', coarse_tail)

    finite = module('finite/transition_readings.py', 'c83_finite')
    records = read_json('finite/transition_readings.json')
    cases = [(8,2,7),(64,4,13),(64,16,12),(512,8,19),(512,32,18)]

    def finite_structure():
        assert [(r['c'],r['b'],r['p']) for r in records] == cases
        for r in records:
            c,b,p = r['c'],r['b'],r['p']
            assert r['n'] == c*(c-1)//2 and r['interval_bits'] == 176
            assert {tuple(o['offsets_halves']) for o in r['origins']} == set(product(range(2),repeat=3))
            assert len(r['origins']) == 8
            # Exact power-of-two logarithms; display values are only decimal labels.
            assert c & (c-1) == b & (b-1) == 0
            lc,lb = c.bit_length()-1,b.bit_length()-1
            logL = F(p)-F(7,4)*lc-F(1,2)*(lc-lb)
            assert isclose(r['L_display'],2**float(logL),rel_tol=1e-14)
            assert isclose(r['beta_display']**3,b**3/c,rel_tol=1e-14)
        return {'settings': cases, 'arrangement_setting_rows': sum(r['n'] for r in records),
                'distinct_inventory_catalogue_rows': sum(c*(c-1)//2 for c in sorted({r['c'] for r in records})),
                'origin_records': 40, 'interval_bits': 176}
    check('finite_catalogue_scales_and_coverage', finite_structure)

    def finite_counts():
        for r in records:
            for o in r['origins']:
                x=o['offsets_halves']
                assert o['second_difference_halves_mod2'] == (x[0]-2*x[1]+x[2])%2
                assert 0 <= o['endpoint_unique'] <= o['triple_unique'] <= r['n']
                assert 0 <= o['region_endpoint_unique'] <= o['region_triple_unique'] <= r['region_n']
                assert o['region_endpoint_unique'] <= o['endpoint_unique']
                assert o['region_triple_unique'] <= o['triple_unique']
            for first,last in product(range(2),repeat=2):
                rows=[o for o in r['origins'] if o['offsets_halves'][0]==first and o['offsets_halves'][2]==last]
                assert len({o['endpoint_unique'] for o in rows})==1
                assert len({o['region_endpoint_unique'] for o in rows})==1
        return {'origin_records_checked': 40, 'scope':'Saved finite counts and subset/measurement consistency.'}
    check('finite_singleton_and_origin_relations', finite_counts)

    def region_counts():
        result={c:sum(finite.source_region(c,v,w) for v in range(2,c+1) for w in range(2,v+1))
                for c in sorted({r['c'] for r in records})}
        assert all(result[r['c']]==r['region_n'] for r in records)
        return {'fresh_exact_integer_region_counts':result, 'physical_readings_recomputed':False}
    check('finite_source_region_integer_counts', region_counts)

    def native_small():
        original=finite.native_tail_ratios
        calls=0
        def tracked(*args):
            nonlocal calls
            out=original(*args);calls+=1
            assert all(isinstance(v,F) for v in out)
            return out
        finite.native_tail_ratios=tracked
        try: out=finite.calculate(*cases[0])
        finally: finite.native_tail_ratios=original
        assert out==records[0] and calls==84 and out['native_enclosures']==84
        return {'recomputed_case':cases[0], 'exact_record_equal':True,
                'native_rational_calls_and_enclosure_assertions':calls,
                'larger_physical_catalogues_recomputed':False}
    check('native_rational_and_bins_c8', native_small)

    triangle=module('tail/triangle_gap.py','c83_triangle')
    estimate=read_json('tail/triangle_gap_estimate.json')

    def triangle_deterministic():
        count=0
        for basis in [(1.,0.,0.,1.),(2.,0.,.25,.5),(.5,.5,-1.,1.),(.125,0.,.375,8.)]:
            for shift in [(.125,.25),(.375,.75),(.75,.5),(0.,0.)]:
                sample=triangle.exact_sample(basis,shift)
                values,radius,_,_=triangle.first_two(sample)
                assert triangle.brute_check(sample,radius)==values
                count+=1
        return {'deterministic_dyadic_cases':count, 'exact_full_brute_comparisons':count,
                'random_sampling_performed':False}
    check('triangle_first_two_exact_row_search', triangle_deterministic)

    def stored_monte_carlo():
        e=estimate
        assert e['status']=='NON_CERTIFIED_MONTE_CARLO'
        assert e['completed_samples']==e['requested_samples']==1000000 and e['failures']==[]
        assert sum(e['adaptive_expansion_histogram'].values())==1000000
        assert e['max_triangle_radius']==2*2**max(map(int,e['adaptive_expansion_histogram']))
        assert e['exact_brute_crosschecks']==64 and e['brute_crosschecks_skipped_for_size']==0
        assert isclose(e['kappa3_estimate'],2*sqrt(2)*e['gap_mean'],rel_tol=1e-14)
        assert len(e['batch_kappa3_means'])==20
        assert isclose(sum(e['batch_kappa3_means'])/20,e['kappa3_estimate'],rel_tol=1e-14)
        se=e['sample_standard_error'];mean=e['kappa3_estimate']
        assert se>0 and all(isfinite(x) for x in (se,mean))
        assert all(isclose(x,y,rel_tol=1e-14) for x,y in zip(e['normal_95_percent_interval_descriptive_only'],[mean-1.96*se,mean+1.96*se]))
        values=[v for _,v in sorted((float(k),v) for k,v in e['gap_quantiles'].items())]
        assert all(0<=a<=b for a,b in zip(values,values[1:]))
        return {'stored_samples_checked':1000000,'samples_regenerated':0,
                'scope':'Output counts and arithmetic only; no certified error or confidence interval.'}
    check('stored_exploratory_sample_consistency', stored_monte_carlo)

    def stored_quadrature():
        data=read_json('haar/quadrature_comparison.json')
        for row in data['rows']:
            assert isclose(row['difference'],row['rectangular_96']-row['old_96'],rel_tol=1e-12,abs_tol=1e-16)
            assert abs(row['difference'])<2e-7
        return {'stored_rows':len(data['rows']), 'quadrature_regenerated':False,
                'scope':'Exploratory numerical agreement, not rigorous integral enclosures.'}
    check('stored_outer_quadrature_arithmetic', stored_quadrature)

    if args.full:
        def full_tail():
            out=tail.calculate(512)
            for key in certificate:
                if key!='elapsed_seconds': assert out[key]==certificate[key],key
            return {'fresh_grid':512,'all_non_timing_fields_equal':True}
        check('full_512_grid_certificate',full_tail)
        def full_finite():
            for case,row in zip(cases,records): assert finite.calculate(*case)==row
            return {'recomputed_cases':cases,'all_records_equal':True}
        check('full_physical_catalogues',full_finite)
        def full_sampling():
            out=triangle.calculate(estimate['requested_samples'],estimate['seed'],20)
            # JSON stringifies integer histogram keys; timing and post-run metadata are excluded.
            out=json.loads(json.dumps(out))
            for key,value in out.items():
                if key!='elapsed_seconds': assert value==estimate[key],key
            return {'regenerated_samples':out['completed_samples'],
                    'all_generated_non_timing_fields_equal':True,'statistical_result_certified':False}
        check('full_exploratory_million_samples',full_sampling)

    def preserved():
        assert all(digest(ROOT/p)==h for p,h in initial.items())
        return {'scientific_json_files_unchanged':len(initial)}
    check('scientific_results_preserved',preserved)

    report={'description':'C83 scoped reproducibility checks',
            'scope_note':'The analytic theorems are proved in Markdown. These checks cover the named explicit identities, saved certificates and finite algorithms only.',
            'environment':{'python':sys.version,'numpy':np.__version__,'sympy':sympy.__version__,
                           'platform':platform.platform(),'python_optimization':sys.flags.optimize},
            'mode':'full' if args.full else 'quick',
            'execution_scope':{'physical_cases_recomputed':cases if args.full else [cases[0]],
                               'tail_grids_recomputed':[8,512] if args.full else [8],
                               'random_samples_regenerated':1000000 if args.full else 0,
                               'full_command':'python verify.py --full'},
            'checks':checks,'passed':sum(r['status']=='passed' for r in checks),
            'failed':sum(r['status']=='failed' for r in checks),
            'elapsed_seconds':round(perf_counter()-started,6),
            'finished_utc':datetime.now(timezone.utc).isoformat(),
            'input_sha256':{str(p.relative_to(ROOT)):digest(p) for p in sorted(ROOT.rglob('*'))
                            if p.is_file() and p.suffix in ('.py','.json') and p.name!='checks.json'
                            and '__pycache__' not in p.parts}}
    report['status']='passed' if not report['failed'] else 'failed'
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'passed':report['passed'],'failed':report['failed'],
                      'elapsed_seconds':report['elapsed_seconds'],'output':str(args.output)}))
    return 1 if report['failed'] else 0


if __name__=='__main__':
    raise SystemExit(main())
