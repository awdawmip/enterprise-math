#!/usr/bin/env python3
"""Independent exact audit; no imports of experiment generators."""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import prod,comb
from pathlib import Path
import hashlib
import json
import csv
import gzip
import math

HERE=Path(__file__).resolve().parent


def tv(a,b):
    return sum((abs(a.get(x,F())-b.get(x,F())) for x in set(a)|set(b)),F())/2


def project(law,indices):
    out=defaultdict(F)
    for x,p in law.items(): out[tuple(x[j] for j in indices)]+=p
    return dict(out)


def decode(rows,key): return {tuple(r[key]):F(r['probability']) for r in rows}


def matrix_from_law(law):
    return tuple(tuple(sum((p*((x+(1,))[i])*((x+(1,))[j]) for x,p in law.items()),F())
                       for j in range(7)) for i in range(7))


def audit_joint():
    data=json.loads((HERE/'joint_results.json').read_text())
    laws={kind:decode(rows,'raw_x6') for kind,rows in data['initial_laws'].items()}
    for k,law in laws.items():
        assert sum(law.values(),F())==1
        assert all(p>0 for p in law.values())
    for mask in ([i] for i in range(6)):
        assert len({tuple(sorted(project(law,mask).items())) for law in laws.values()})==1
    assert project(laws['aligned'],[0,1,2])==project(laws['opposed'],[0,1,2])
    checked=0
    for row in data['rows']:
        kind,n=row['kind'],row['n']
        c={'aligned':F(1),'opposed':F(-1),'independent':F(0)}[kind]
        variance=1+n*n+2*n*c
        mixed=n+c
        fourth=1+4*n*c+6*n*n+4*n**3*c+n**4
        k4=fourth-3*variance*variance
        gamma=k4/(variance*variance) if variance else None
        assert F(row['variance_x1'])==variance
        assert F(row['covariance_x1_x4'])==mixed
        assert (None if row['gamma4_x1'] is None else F(row['gamma4_x1']))==gamma
        expected=[[F(int(i==j)) for j in range(7)] for i in range(7)]
        expected[0][0]=variance
        expected[0][3]=expected[3][0]=mixed
        expected_upper=[expected[i][j] for i in range(7) for j in range(i,7)]
        assert list(map(F,row['moment_upper_28']))==expected_upper
        # Closed affine power uses origin atoms, not stepwise numerical propagation.
        current={(x[0]+n*x[3],)+x[1:]:p for x,p in laws[kind].items()}
        assert len(current)==len(laws[kind])
        matrix=matrix_from_law(current)
        assert matrix==tuple(map(tuple,expected))
        assert F(row['initial_decorrelation_variance'])==1+n*n
        assert F(row['drop_covariance_every_step_variance'])==1+n
        checked+=1
    assert checked==195
    for n in range(65):
        full={kind:{(x[0]+n*x[3],)+x[1:]:p for x,p in law.items()} for kind,law in laws.items()}
        assert tv(full['aligned'],full['opposed'])==1
        assert tv(project(full['aligned'],[0,1,2]),project(full['opposed'],[0,1,2]))==(F(0) if n==0 else F(1))
    return {'status':'PASS','all_28_moment_and_gamma_rows':checked,
            'independent_method':'closed binomial fourth moment in initial two-sign correlation c, plus direct affine powers of stored initial atoms',
            'full_vs_projection_TV_times_checked':65,'zero_variance_rows':1,
            'projection_failure':'same (x1,x2,x3) and opposite x4 can route to different future x1; retained projection not closed under F',
            'closure_scope':'28 moments suffice for affine F and degree<=2 readouts; not full X6 law or arbitrary future operations'}


def audit_parity():
    data=json.loads((HERE/'parity_results.json').read_text())
    assert data['source_sha256']==hashlib.sha256((HERE/'parity_probe.py').read_bytes()).hexdigest()
    laws={name:decode(rows,'raw_chart') for name,rows in data['initial_laws'].items()}
    character_checks=0
    for name,law in laws.items():
        eps={'independent':0,'parity_plus':1,'parity_minus':-1}[name]
        for x in product((-1,1),repeat=6):
            expected=F(1+eps*prod(x),64)
            assert law.get(x,F())==expected
        # Walsh characters determine the complete binary joint law.
        for mask in range(64):
            character=sum((p*prod(x[j] for j in range(6) if mask&(1<<j)) for x,p in law.items()),F())
            expected=1 if mask==0 else eps if mask==63 else 0
            assert character==expected
            character_checks+=1
    rows=0
    for name,trajectory in data['trajectories'].items():
        eps={'independent':0,'parity_plus':1,'parity_minus':-1}[name]
        for row in trajectory:
            n=row['n']
            transformed=decode(row['law'],'raw_chart')
            assert len(transformed)==len(laws[name])
            for y,p in transformed.items():
                q=prod(y[1:])
                original=(y[0]-n*q,)+y[1:]
                assert p==laws[name][original]
            variance=1+n*n+2*n*eps
            fourth=1+6*n*n+n**4+4*n*(1+n*n)*eps
            assert F(row['variance'])==variance
            k4=fourth-3*variance*variance
            assert F(row['kappa4'])==k4
            expected_gamma=F(k4,variance*variance) if variance else None
            assert (None if row['gamma4'] is None else F(row['gamma4']))==expected_gamma
            rows+=1
    assert rows==27
    return {'status':'PASS','Walsh_character_checks':character_checks,'complete_trajectory_laws_checked':rows,
            'independent_method':'pointwise density (1+eps*product(x))/64, Walsh characters, direct inverse routing, binomial fourth moments',
            'degree_five_or_lower_initial_moments':'identical, including full BRC second-moment state',
            'repair_scope':'Q=product(x2..x6) is a joint observer. Retaining joint (X1,Q) permits declared affine update of that pair, not replacement of native X6 identity.'}



def spectral_cycle(count,ptext,n):
    import mpmath as mp
    mp.mp.dps=80
    p=mp.mpf(ptext)
    if p==0: return [mp.mpf(int(i==0)) for i in range(count)]
    if p==1: return [mp.mpf(int(i==n%count)) for i in range(count)]
    roots=[mp.exp(2j*mp.pi*k/count) for k in range(count)]
    coefficients=[(1-p+p*z)**n for z in roots]
    answer=[]
    for j in range(count):
        value=sum(coefficients[k]*roots[k]**(-j) for k in range(count))/count
        assert abs(value.imag)<mp.mpf('1e-65')
        assert value.real>-mp.mpf('1e-65')
        answer.append(value.real)
    return answer


def audit_transfer():
    import mpmath as mp
    data=json.loads((HERE/'transfer_results.json').read_text())
    assert data['audit']['status']=='PASS'
    assert data['source_sha256']==hashlib.sha256((HERE/'transfer_sweep.py').read_bytes()).hexdigest()
    path=HERE/data['csv']['path']
    assert data['csv']['sha256']==hashlib.sha256(path.read_bytes()).hexdigest()
    mp.mp.dps=80
    # Exact finite-binomial residue sum validates the independent spectral oracle.
    spectral_selfchecks=0
    for count in (6,12):
        for ptext in ('0.01','0.1','0.25','0.5','0.75'):
            p=F(ptext)
            for n in (0,1,2,17,37):
                exact=[F(0)]*count
                for k in range(n+1): exact[k%count]+=comb(n,k)*p**k*(1-p)**(n-k)
                reference=spectral_cycle(count,ptext,n)
                for actual,expected in zip(reference,exact):
                    assert abs(actual-mp.mpf(expected.numerator)/expected.denominator)<mp.mpf('1e-65')
                spectral_selfchecks+=1
    cases={case['id']:case for case in data['cases']}
    selected_times={0,1,2,6,11,12,17,37,257,1024,4096}
    groups={}
    for family,meta in data['families'].items():
        sites=list(map(tuple,meta['raw_sites']))
        count=meta['site_count']
        assert count==len(sites)==len(set(sites))
        assert (0,)*6 not in sites
        for i,cell in enumerate(sites):
            step=tuple(y-x for x,y in zip(cell,sites[(i+1)%count]))
            assert step==tuple(meta['advance_displacements'][i])
            if count==12:
                assert sum(abs(x) for x in step)==1
            else:
                assert sites[(i+1)%count]==(cell[-1],)+cell[:-1]
        population=sites+[(0,)*6]
        readouts={f'tv_axis_{i+1}':[i] for i in range(6)}
        readouts.update(tv_axes123=[0,1,2],tv_axes456=[3,4,5])
        per_family={}
        for label,indices in readouts.items():
            fibers=defaultdict(list)
            for k,x in enumerate(population): fibers[tuple(x[j] for j in indices)].append(k)
            per_family[label]=list(fibers.values())
        groups[family]=per_family
        uniform={tuple(x):F(1,count) for x in sites}
        anchor={(0,)*6:F(1)}
        stationary_axes=[tv(project(uniform,[i]),project(anchor,[i])) for i in range(6)]
        assert all(abs(float(q)-reported)<1e-15 for q,reported in zip(stationary_axes,meta['stationary_conditional_axis_tv']))
    max_projection_error=max_normalized_spectral_error=max_survival_relative_error=0.0
    spectral_cache={}
    references=[]
    times_seen={cid:0 for cid in cases}
    fit_values={cid:[] for cid in cases}
    total_rows=0
    with gzip.open(path,'rt',newline='') as handle:
        for row in csv.DictReader(handle):
            cid=row['case'];case=cases[cid];family=row['family'];n=int(row['n'])
            assert family==case['family'] and n==times_seen[cid]
            times_seen[cid]+=1
            count=data['families'][family]['site_count']
            survival=float(row['survival'])
            delta=[float(row[f'delta_site_{j:02d}']) for j in range(count)]+[float(row['delta_anchor'])]
            assert survival>0 and delta[-1]==-survival
            assert all(math.isfinite(x) for x in delta) and min(delta[:-1])>=0
            assert all(row[f'delta_site_{j:02d}']=='' for j in range(count,12))
            assert abs(math.fsum(delta)/survival)<3e-12
            full=math.fsum(abs(x) for x in delta)/2
            error=abs(full-float(row['tv_spatial']))/survival
            assert error<3e-12
            max_projection_error=max(max_projection_error,error)
            for label,fibers in groups[family].items():
                pushed_tv=math.fsum(abs(math.fsum(delta[k] for k in fiber)) for fiber in fibers)/2
                error=abs(pushed_tv-float(row[label]))/survival
                assert error<3e-12,(cid,n,label,error)
                max_projection_error=max(max_projection_error,error)
                assert pushed_tv<=full+3e-12*survival
            assert abs(math.fsum(float(row[f'tv_axis_{i+1}']) for i in range(6))-float(row['sum_axis_tv']))/survival<3e-12
            fit_values[cid].append((float(row['tv_axis_1']),float(row['tv_axes123']),float(row['tv_spatial'])))
            if n in selected_times:
                key=(count,case['p'],n)
                if key not in spectral_cache:spectral_cache[key]=spectral_cycle(*key)
                conditional=spectral_cache[key]
                exact_survival=(1-mp.mpf(case['d']))**n
                survival_error=float(abs(mp.mpf(row['survival'])/exact_survival-1))
                assert survival_error<3e-12
                max_survival_relative_error=max(max_survival_relative_error,survival_error)
                reference_errors=[float(abs(mp.mpf(row[f'delta_site_{j:02d}'])/exact_survival-conditional[j])) for j in range(count)]
                maximum=max(reference_errors)
                assert maximum<3e-12,(cid,n,maximum)
                max_normalized_spectral_error=max(max_normalized_spectral_error,maximum)
                references.append({'case':cid,'n':n,'maximum_site_error_divided_by_exact_survival':maximum})
            total_rows+=1
    assert total_rows==data['timepoint_rows']==172074
    assert all(n==data['horizon']+1 for n in times_seen.values())
    fit_count=0
    max_fit_metric_error=0.0
    for cid,case in cases.items():
        fits=case['short_window_fits']
        if 'axis1_C_over_n' not in fits:continue
        for index,label in enumerate(('axis1_C_over_n','axes123_C_over_n','full_spatial_C_over_n')):
            record=fits[label]
            assert record['status']=='FIT' and record['train']==[1,16] and record['heldout']==[2049,4096]
            values=[row[index] for row in fit_values[cid]]
            coefficient=sum((F(str(values[n]))/n for n in range(1,17)),F())/sum((F(1,n*n) for n in range(1,17)),F())
            assert abs(float(coefficient)-record['coefficient_C'])<1e-12
            errors=[float(coefficient)/n-values[n] for n in range(2049,4097)]
            metric=math.sqrt(math.fsum(e*e for e in errors)/math.fsum(values[n]**2 for n in range(2049,4097)))
            error=abs(metric-record['heldout_normalized_rmse'])/max(1,abs(record['heldout_normalized_rmse']))
            assert error<1e-12
            max_fit_metric_error=max(max_fit_metric_error,error)
            fit_count+=1
    assert fit_count==18
    return {'status':'PASS','exported_rows_checked':total_rows,'parameter_cases':len(cases),
            'exact_binomial_vs_spectral_selfchecks':spectral_selfchecks,
            'independent_spectral_reference_points':len(references),'spectral_precision':80,
            'maximum_site_error_divided_by_exact_survival':max_normalized_spectral_error,
            'maximum_survival_relative_error':max_survival_relative_error,
            'maximum_generic_pushforward_TV_error_divided_by_survival':max_projection_error,
            'independently_refitted_models':fit_count,'maximum_holdout_metric_scaled_error':max_fit_metric_error,
            'method':'DFT eigenvalue powers, exact finite-binomial residues, generic signed-measure pushforward by observer fibers; no generator import',
            'scope':'same fixed native X6 chart; full spatial law only; conditional channel kernels and explicit many-to-one spatial reset; archived histories remain richer',
            'reference_points':references}

def main():
    result={'researcher_id':'EM-BRCAUDIT-9D72AC','activity_id':'RA-BRCAUDIT-20261002-9D72AC',
            'formal_driver_acceptance':False,'joint':audit_joint(),'parity_self_crosscheck':audit_parity(),
            'transfer':audit_transfer()}
    result['status']='PASS'
    bound=['joint_transfer.py','joint_results.json','parity_probe.py','parity_results.json','transfer_sweep.py','transfer_results.json','transfer_series.csv.gz']
    result['bound_sha256']={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in bound}
    result['audit_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE/'audit_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'joint_rows':result['joint']['all_28_moment_and_gamma_rows'],
                      'parity_Walsh_checks':result['parity_self_crosscheck']['Walsh_character_checks']}))


if __name__=='__main__':main()
