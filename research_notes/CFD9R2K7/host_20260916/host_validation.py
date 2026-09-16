"""Actual pinned spectralDNS/shenfun validation, not a mock host.

Run with CFD_UPSTREAM_ROOT and CFD_PRIOR_ROOT pointing to the exact checkouts.
Uses the host's context, Vortex callback, pressure/diffusion, transforms and RK4.
Only the outer benchmark loop (no disk I/O) and candidate callback are ours.
"""
from __future__ import annotations
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
import time
import traceback
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
UPSTREAM = Path(os.environ['CFD_UPSTREAM_ROOT']).resolve()
PRIOR = Path(os.environ['CFD_PRIOR_ROOT']).resolve()
sys.path.insert(0, str(UPSTREAM))
sys.path.insert(0, str(PRIOR/'research_notes/CFD-B1F673/main'))
import spectralDNS
from mpi4py import MPI
import hybrid as inherited
from native_adapter import NativeVortexAdapter

TASK = 'RS-CFD-SPECTRAL-HYBRID-20260910'
DT = 0.002
STEPS = 12
REPEATS = 5
LIMIT = 128
MATRIX = [
    (16, 'shear', None), (16, 'taylor_green', None),
    (16, 'random32', 916601), (16, 'edge', 916602),
    (32, 'shear', None), (32, 'taylor_green', None),
    (32, 'random32', 916603), (32, 'random256', 916604),
]


def blob(path):
    b = Path(path).read_bytes()
    return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()


def context(n):
    m = str(int(np.log2(n)))
    s = spectralDNS.get_solver(parse_args=[
        '--M', m, m, m, '--dealias', '3/2-rule', '--nu', '0.01',
        '--dt', str(DT), '--T', str(STEPS*DT), '--integrator', 'RK4',
        '--planner_effort', '{"fft":"FFTW_ESTIMATE"}', '--no-verbose', 'NS'])
    c = s.get_context()
    c.Source.fill(0)
    return s, c


def candidate(s, c):
    return NativeVortexAdapter(c, s.params, s.getConvection('Vortex'),
        inherited.rotational_pairs, inherited.probe.extract_support,
        comm_size=MPI.COMM_WORLD.Get_size(), sparse_limit=LIMIT)


def initial(n, name, seed):
    if name.startswith('random'):
        return inherited.probe.initial_state(n, int(name[6:]), seed)*0.1
    h = np.zeros((3,n,n,n//2+1), dtype=np.complex128)
    if name == 'shear':
        return inherited.shear(n)
    if name == 'taylor_green':
        for sx in [-1,1]:
            for sy in [-1,1]:
                h[0,sx % n,sy % n,1] = -1j*sx/8
                h[1,sx % n,sy % n,1] = 1j*sy/8
        return h
    if name == 'edge':
        rng = np.random.default_rng(seed)
        k = n//2-1
        for p in [np.array([k,1,0]), np.array([-k+1,0,1])]:
            a = rng.normal(size=3)+1j*rng.normal(size=3)
            a -= p*np.dot(p,a)/np.dot(p,p)
            a *= 0.1
            h[:, p[0] % n, p[1] % n, p[2]] = a
            if p[2] == 0:
                h[:, -p[0] % n, -p[1] % n, 0] = a.conjugate()
        return h
    raise ValueError(name)


def error(a, b):
    absolute = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    scale = float(np.max(np.abs(np.asarray(a))))
    return {'absolute_max': absolute, 'relative_max': absolute/max(scale,1e-30),
            'reference_scale': scale, 'pass': absolute <= 5e-12+5e-11*scale}


def output(s, c):
    s.ComputeRHS(c.dU,c.U_hat,s,**c)
    s.get_velocity(**c); s.get_pressure(**c)
    return {name: np.asarray(a).copy() for name,a in [
        ('velocity_hat',c.U_hat), ('rhs_hat',c.dU), ('pressure_proxy',c.P_hat),
        ('velocity_real',c.U), ('modified_pressure_real',c.P)]}


def one_rhs(n, h):
    s,c = context(n); c.U_hat[:] = h
    dense = s.getConvection('Vortex')
    s.conv = dense; a = output(s,c)
    adapter = candidate(s,c); adapter.validate_initial(c.U_hat)
    assert abs(adapter.normalization_constant-1) < 1e-13, 'test inputs require unit host normalization'
    s.conv = adapter; b = output(s,c)
    comparisons = {key:error(a[key],b[key]) for key in a}
    if not all(v['pass'] for v in comparisons.values()):
        raise AssertionError(json.dumps(comparisons))
    k = np.stack(np.broadcast_arrays(*c.K))
    divergence = float(np.max(np.abs(np.sum(k*b['rhs_hat'],axis=0))))
    if divergence > 2e-10:
        raise AssertionError('projected RHS divergence exceeds tolerance')
    return {'comparisons':comparisons,'projected_rhs_divergence_max':divergence,
            'normalization_constant':adapter.normalization_constant,
            'host_K_shapes':[list(x.shape) for x in c.K],
            'host_dealiased_shape':list(c.u_dealias.shape),
            'native_cutoff':adapter.cutoff,'adapter_stats':adapter.stats,
            'pressure_proxy_max':float(np.max(np.abs(a['pressure_proxy'])))}


def trajectory(n, h, mode):
    started=time.perf_counter()
    s,c = context(n); c.U_hat[:] = h
    adapter = candidate(s,c) if mode == 'hybrid' else None
    if adapter is not None:
        adapter.validate_initial(c.U_hat)
        assert abs(adapter.normalization_constant-1) < 1e-13
    s.conv = adapter if adapter is not None else s.getConvection('Vortex')
    s.params.t=0.0; s.params.tstep=0
    integrate = s.getintegrator(c.dU,c.u,s,c)
    stepping=time.perf_counter()
    for _ in range(STEPS):
        _,_,dt_used=integrate()
        s.params.t+=dt_used; s.params.tstep+=1
        if not np.isfinite(c.u).all():
            raise FloatingPointError('nonfinite native trajectory')
    after_steps=time.perf_counter()
    values=output(s,c)
    finished=time.perf_counter()
    return values, {'total_seconds':finished-started,
                    'setup_seconds':stepping-started,
                    'native_RK4_seconds':after_steps-stepping,
                    'final_readout_seconds':finished-after_steps,
                    'stats':adapter.stats if adapter is not None else None}


def main():
    assert MPI.COMM_WORLD.Get_size() == 1
    assert blob(UPSTREAM/'spectralDNS/solvers/NS.py') == '6a11909d1e2c1d529d382952c4c9d77e7073645c'
    assert blob(PRIOR/'research_notes/CFD-B1F673/main/hybrid.py') == '984b0b902302394aa84105bc99aa69e7388d4185'
    out=HERE/'host_validation.json'
    report={'schema':'CFD_PINNED_NATIVE_HOST_VALIDATION_V1', 'task_id':TASK,
        'claim_id':'CFD9R2K7-HOST-20260916','researcher_id':'EM-CFD-49157B',
        'activity_id':'RA-CFD-HOST-20260916-68a17c',
        'source_sha':os.getenv('GITHUB_SHA'),'workflow_run_id':os.getenv('GITHUB_RUN_ID'),
        'status':'RUNNING','upstream_commit':'835b01b1e820b5c56559b9a028293e57526bfbf9',
        'inherited_commit':'e40e5303234c5e8bd725528aad9bff9edf0c059d',
        'original_NS_source_modified':False,'original_RK4_source_modified':False,
        'actual_spectralDNS_host_executed':True,'actual_shenfun_FFTW_executed':True,
        'native_solver_outer_IO_loop_executed':False,'pruning_used':False,
        'continuous_PDE_certificate':False,'independent_review':False,
        'domain':[float(2*np.pi)]*3,'dealias':'3/2-rule','nyquist_mask':True,
        'dt':DT,'steps':STEPS,'repeats':REPEATS,'sparse_limit':LIMIT,
        'frozen_matrix':MATRIX,'python':sys.version,'platform':platform.platform(),
        'versions':{p:importlib.metadata.version(p) for p in ['numpy','scipy','shenfun','mpi4py','mpi4py-fft','numba']},
        'cost_included':['context allocation and FFTW_ESTIMATE planning','adapter setup and host normalization calibration','initial validation','support detection','all nonlinear evaluations','native projection/diffusion','native RK4 algebra','per-step finite checks','final velocity and modified-pressure readout'],
        'cost_excluded':['initial shared input generation','dependency installation','first JIT warmup','disk output','report writing'],
        'rhs_cases':[],'trajectory_cases':[],'failures':[],
        'source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [HERE/'native_adapter.py',HERE/'host_validation.py']}}
    def save():
        out.write_text(json.dumps(report,indent=2)+'\n')
    save()
    t=time.perf_counter()
    p,a=inherited.probe.extract_support(inherited.shear(16),16)
    inherited.rotational_pairs(p,a,16,7)
    report['JIT_warmup_seconds']=time.perf_counter()-t
    for n,name,seed in MATRIX:
        h=initial(n,name,seed)
        key={'n':n,'input':name,'seed':seed}
        try:
            report['rhs_cases'].append({**key,**one_rhs(n,h)})
        except Exception:
            report['failures'].append({**key,'stage':'RHS','traceback':traceback.format_exc()})
            save(); continue
        save()
        try:
            # Non-timed one-step host FFT planning/cache use is not hidden:
            # each timed trajectory below builds its own full context afresh.
            trials={'fft':[],'hybrid':[]}; last={}
            for repeat in range(REPEATS):
                order=['fft','hybrid'] if repeat%2 == 0 else ['hybrid','fft']
                for mode in order:
                    values,timing=trajectory(n,h,mode)
                    trials[mode].append(timing); last[mode]=values
                comparisons={x:error(last['fft'][x],last['hybrid'][x]) for x in last['fft']}
                if not all(v['pass'] for v in comparisons.values()):
                    raise AssertionError(json.dumps(comparisons))
            tm={m:float(np.median([v['total_seconds'] for v in trials[m]])) for m in trials}
            shear_error=None
            if name=='shear':
                exact=h*np.exp(-0.01*DT*STEPS)
                shear_error=error(exact,last['hybrid']['velocity_hat'])
                if not shear_error['pass']: raise AssertionError('analytic shear test failed')
            row={**key,'comparisons':comparisons,'trials':trials,'median_total_seconds':tm,
                 'ratio_fft_over_hybrid':tm['fft']/tm['hybrid'], 'analytic_shear_error':shear_error}
            report['trajectory_cases'].append(row)
            print(json.dumps({**key,'ratio':row['ratio_fft_over_hybrid'],'stats':trials['hybrid'][-1]['stats']}),flush=True)
        except Exception:
            report['failures'].append({**key,'stage':'TRAJECTORY','traceback':traceback.format_exc()})
        save()
    report['status']='PASS_BOUNDED_AUTHOR_NATIVE_HOST_TESTS' if not report['failures'] else 'FAIL_BOUNDED_NATIVE_HOST_TESTS'
    save(); print(report['status'],flush=True)
    return 1 if report['failures'] else 0


if __name__=='__main__':
    try:
        raise SystemExit(main())
    except Exception:
        (HERE/'host_validation_fatal.txt').write_text(traceback.format_exc())
        raise
