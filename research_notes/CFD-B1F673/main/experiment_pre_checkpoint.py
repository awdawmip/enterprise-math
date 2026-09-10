"""Reproducible held-out trajectories and observer-aware adapter contract tests."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, platform, sys, time
from pathlib import Path
import numpy as np
import scipy, numba
from hybrid import (Hybrid,Config,rk4,shear,probe,rotational_pairs,fft_rotational_with_k,
                    project,SerialSpectralDNSAdapter,propose_pruning,support_count)

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def rel(a,b): return float(np.max(np.abs(a-b))/max(np.max(np.abs(b)),1e-30))
def norm2(h):
    x=np.abs(h)**2
    return float(np.sqrt(np.sum(x[:,:,:,0])+2*np.sum(x[:,:,:,1:])))
def normdiv(h,k): return float(np.max(np.abs(np.sum(k*h,axis=0))))
def hermitian(h):
    ix=(-np.arange(h.shape[1]))%h.shape[1]
    return float(np.max(np.abs(h[:,:,:,0]-np.take(np.take(h[:,:,:,0],ix,axis=1),ix,axis=2).conjugate())))

def contract_tests():
    tests=[]
    for n,s,seed in [(16,16,89001),(24,64,89002),(32,128,89003)]:
        cfg=Config(n=n); model=Hybrid(cfg); h=probe.initial_state(n,s,seed)
        p,a=probe.extract_support(h,n)
        g=rotational_pairs(p,a,n,model.cutoff)
        gf=fft_rotational_with_k(h,n,model.k)*model.keep
        v,pressure=project(g,model.k,model.inv,model.keep)
        vf,pf=project(gf,model.k,model.inv,model.keep)
        direct_old=probe.grouped_rhs(p,a,n,model.cutoff)
        row={'n':n,'s':s,'seed':seed,'rotational_relative_error':rel(g,gf),
             'velocity_relative_error':rel(v,vf),'pressure_proxy_relative_error':rel(pressure,pf),
             'old_projected_baseline_error':rel(v,direct_old),'divergence_max':normdiv(v,model.k)}
        assert max(row[x] for x in ['rotational_relative_error','velocity_relative_error','pressure_proxy_relative_error','old_projected_baseline_error'])<2e-11,row
        tests.append(row)
    n=32; m=Hybrid(Config(n=n)); h=shear(n); p,a=probe.extract_support(h,n)
    g=rotational_pairs(p,a,n,m.cutoff); v,pp=project(g,m.k,m.inv,m.keep)
    _,wrong=project(v,m.k,m.inv,m.keep)
    witness={'flow':'u=(sin(y),0,0)','velocity_rhs_max':float(np.max(np.abs(v))),
             'correct_host_pressure_proxy_max':float(np.max(np.abs(pp))),
             'incorrect_projected_interface_proxy_max':float(np.max(np.abs(wrong)))}
    assert witness['correct_host_pressure_proxy_max']>0 and witness['velocity_rhs_max']==0
    adapter=[]
    for scale in (1.,1/n**3):
        for s in (32,512):
            h=probe.initial_state(n,s,99100+s); hh=h/scale
            called=[]
            def host(rhs,u_hat,work,Tp,VTp,K,u_dealias):
                called.append(True)
                rhs[:]=fft_rotational_with_k(np.asarray(u_hat)*scale,n,m.k)*m.keep/scale
                return rhs
            cb=SerialSpectralDNSAdapter(n,host,coefficient_scale_to_forward=scale,cutoff=m.cutoff,sparse_limit=128)
            out=np.zeros_like(h); cb(out,hh,None,None,None,m.k,None)
            truth=fft_rotational_with_k(h,n,m.k)*m.keep/scale
            e=rel(out,truth); assert e<2e-11
            adapter.append({'scale_to_forward':scale,'s':s,'relative_error':e,'dense_callback_called':bool(called)})
            assert bool(called)==(s>128)
    for kwargs in ({'comm_size':2},{'cutoff':n//3},{'domain':(1.,1.,1.)}):
        params=dict(coefficient_scale_to_forward=1.,cutoff=m.cutoff); params.update(kwargs)
        try: SerialSpectralDNSAdapter(n,lambda *args:None,**params)
        except ValueError: pass
        else: raise AssertionError('unsupported host accepted')
    mask=m.keep.copy(); v,e,status=propose_pruning(h,mask)
    assert np.array_equal(v+e,h) and status['status'].startswith('UNVERIFIED')
    # RK4 refinement at the SAME finite spatial operator, not PDE convergence.
    n=16; h=probe.initial_state(n,64,120987); cfg=Config(n=n,viscosity=.15)
    ys=[rk4(h,Hybrid(cfg,'fft'),.08/steps,steps) for steps in (8,16,32,128)]
    errors=[norm2(y-ys[-1]) for y in ys[:-1]]
    refinement={'steps':[8,16,32],'reference_steps':128,'horizon':.08,'errors':errors,
                'successive_error_ratios':[errors[0]/errors[1],errors[1]/errors[2]]}
    assert all(errors[i]>errors[i+1] for i in range(2)),refinement
    return {'status':'SCOPED_AUTHOR_REGRESSION_PASS_NOT_INDEPENDENT_REVIEW','operator_tests':tests,
            'pressure_interface_witness':witness,'adapter_contract_tests':adapter,
            'unsupported_host_rejections':3,'pruning_proposal_not_accepted':True,
            'time_refinement':refinement}

def run_case(case,repeats):
    n=case['n']; initial=case['input']
    h=shear(n) if initial=='shear' else probe.initial_state(n,case['s'],case['seed'])
    cfg=Config(n=n,viscosity=.01,sparse_limit=384,sticky_dense=True)
    modes=('fft','hybrid'); raw={x:[] for x in modes}; end={}; stats={}
    for r in range(repeats):
        for mode in (modes if r%2==0 else modes[::-1]):
            # Setup, validation, every detection, allocation, stage and final
            # finite check are included. Initial input generation is shared.
            start=time.perf_counter(); engine=Hybrid(cfg,mode)
            y=rk4(h,engine,.001,10); elapsed=time.perf_counter()-start
            raw[mode].append(elapsed); end[mode]=y; stats[mode]=dict(engine.stats)
    err=rel(end['hybrid'],end['fft'])
    assert err<2e-11,(case,err)
    engine=Hybrid(cfg)
    diagnostics={mode:{'energy_initial':norm2(h)**2/2,'energy_final':norm2(end[mode])**2/2,
                       'divergence_max':normdiv(end[mode],engine.k),'hermitian_zero_plane_max':hermitian(end[mode]),
                       'final_exact_nonzero_modes':support_count(end[mode])[0],
                       'final_modes_above_1e_12_diagnostic_only':probe.full_mode_count(end[mode])}
                 for mode in modes}
    for d in diagnostics.values():
        assert d['energy_final']<=d['energy_initial']*(1+1e-10)
        assert d['divergence_max']<2e-11 and d['hermitian_zero_plane_max']<2e-11
    if initial=='shear':
        exact=h*np.exp(-cfg.viscosity*.01)
        diagnostics['analytic_shear_relative_error']={mode:rel(end[mode],exact) for mode in modes}
        assert max(diagnostics['analytic_shear_relative_error'].values())<2e-11
    mf=float(np.median(raw['fft'])); mh=float(np.median(raw['hybrid']))
    return {'case':case,'steps':10,'dt':.001,'viscosity':.01,'sparse_limit':384,'pruning':False,
            'relative_trajectory_difference':err,'fft_median_seconds':mf,'hybrid_median_seconds':mh,
            'ratio_fft_over_hybrid':mf/mh,'raw_seconds':raw,'last_trial_stats':stats,'diagnostics':diagnostics}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--suite',choices=['contracts','32','64'],required=True)
    ap.add_argument('--repeats',type=int,default=5); args=ap.parse_args()
    here=Path(__file__).resolve().parent
    frozen=json.loads((here/'frozen_cases.json').read_text())
    baseline=here.parent/'prior_3d/probe.py'
    assert sha(baseline)=='1d10429616026f13643f0ba1641acd8c23f3aecd1dc7c03b429f5e0c4381eb09'
    t=time.perf_counter(); m=Hybrid(Config(n=16)); p,a=probe.extract_support(shear(16),16)
    rotational_pairs(p,a,16,m.cutoff); jit=time.perf_counter()-t
    result={'suite':args.suite,'created_at':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
            'status':'FINITE_TRAJECTORY_AUTHOR_TEST_NOT_INDUSTRIAL_OR_PDE_CERTIFICATE',
            'code_sha256':{x:sha(here/x) for x in ('hybrid.py','experiment.py','frozen_cases.json')},
            'baseline_sha256':sha(baseline),'versions':{'python':sys.version,'numpy':np.__version__,
            'scipy':scipy.__version__,'numba':numba.__version__,'platform':platform.platform()},
            'spectralDNS_available':importlib.util.find_spec('spectralDNS') is not None,
            'jit_or_cache_warmup_seconds_excluded':jit,'fft_workers':1,'compiled_sparse_parallel':False}
    if args.suite=='contracts': result['tests']=contract_tests()
    else:
        result['records']=[]
        for case in frozen['cases']:
            if case['n']!=int(args.suite): continue
            row=run_case(case,args.repeats); result['records'].append(row)
            print(json.dumps(row),flush=True)
    (here/('results_'+args.suite+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'suite':args.suite,'status':'PASS','output':str(here/('results_'+args.suite+'.json'))}),flush=True)
if __name__=='__main__': main()
