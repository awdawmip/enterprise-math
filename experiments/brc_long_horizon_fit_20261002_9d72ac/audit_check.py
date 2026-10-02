#!/usr/bin/env python3
"""Independent audit: Taylor-matrix powers and direct distributions.

Does not import either data generator. Deterministic numerical/model checks,
not independent empirical observations or a formal Driver acceptance.
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import math
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDITOR = 'EM-BRCAUDIT-9D72AC'


def poly_add(a, b):
    return [x+y for x,y in zip(a,b)]


def poly_mul(a,b):
    return [sum((a[i]*b[k-i] for i in range(k+1)),D(0)) for k in range(5)]


def matrix_mul(a,b):
    return [[poly_add(poly_mul(a[i][0],b[0][j]),poly_mul(a[i][1],b[1][j]))
             for j in range(2)] for i in range(2)]


def tilted_matrix_moments(rho,n,precision=100):
    """Raw moments via T(z)^n Taylor jets, independent of cumulant recurrence."""
    with localcontext() as ctx:
        ctx.prec=precision
        r=D(3).sqrt()-2 if rho=='critical' else D(str(rho))
        signs=(-1,1)
        matrix=[[[((1+r*s*t)/2)*D(t)**k/D(math.factorial(k)) for k in range(5)]
                 for t in signs] for s in signs]
        accum=[[[D(int(i==j))]+[D(0)]*4 for j in range(2)] for i in range(2)]
        remaining=n
        while remaining:
            if remaining & 1:
                accum=matrix_mul(accum,matrix)
            remaining >>= 1
            if remaining:
                matrix=matrix_mul(matrix,matrix)
        mgf=[sum((accum[i][j][k] for i in range(2) for j in range(2)),D(0))/2
             for k in range(5)]
        assert abs(mgf[0]-1)<D(10)**(-precision+10)
        assert abs(mgf[1])<D(10)**(-precision+10)
        variance=2*mgf[2]
        fourth=24*mgf[4]
        kappa4=fourth-3*variance*variance
        gamma=kappa4/(variance*variance) if variance else None
        return dict(variance=+variance,kappa4=+kappa4,gamma4=+gamma if gamma is not None else None)


def enumerate_markov(rho,n):
    dist={(s,0):F(1,2) for s in (-1,1)}
    for _ in range(n):
        new={}
        for (s,x),mass in dist.items():
            for t in (-1,1):
                key=(t,x+t)
                new[key]=new.get(key,F(0))+mass*(1+rho*s*t)/2
        dist=new
    var=sum((p*x*x for (_,x),p in dist.items()),F(0))
    fourth=sum((p*x**4 for (_,x),p in dist.items()),F(0))
    k4=fourth-3*var*var
    return dict(variance=var,kappa4=k4,gamma4=k4/(var*var) if var else None)


def rel_error(actual,expected):
    return abs(actual-expected)/max(abs(expected),D('1e-90'))


def independent_self_checks():
    maximum=D(0)
    comparisons=0
    with localcontext() as ctx:
        ctx.prec=100
        for r in [F(-1),F(-3,4),F(-1,2),F(0),F(1,2),F(3,4),F(1)]:
            for n in range(1,13):
                spectral=tilted_matrix_moments(D(r.numerator)/D(r.denominator),n)
                enumerated=enumerate_markov(r,n)
                for key in spectral:
                    q=enumerated[key]
                    expected=None if q is None else D(q.numerator)/D(q.denominator)
                    actual=spectral[key]
                    assert (actual is None)==(expected is None)
                    if expected is not None:
                        error=abs(actual-expected)/max(D(1),abs(expected))
                        maximum=max(maximum,error)
                        assert error<D('1e-80'),(r,n,key,error)
                    comparisons+=1
        critical=[]
        for n in [32,128,1024,8192,65536]:
            lower=tilted_matrix_moments('critical',n,80)
            upper=tilted_matrix_moments('critical',n,120)
            error=rel_error(lower['gamma4'],upper['gamma4'])
            assert error<D('1e-65'),(n,error)
            scaled=upper['gamma4']*D(n*n)
            # Asymptotic finite-n boundary prediction; exponentially small error.
            d=D(1)/D(3).sqrt()
            predicted=-1/(D(n)*d+D(1)/3)**2
            exponential_error=rel_error(upper['gamma4'],predicted)
            if n>=128:
                assert exponential_error<D('1e-65'),(n,exponential_error)
            critical.append(dict(n=n,precision_80_vs_120_relative_error=str(error),
                                 n_squared_gamma4=str(scaled),boundary_prediction_relative_error=str(exponential_error)))
    return dict(method='independent tilted 2x2 matrix Taylor jets, binary exponentiation',
                distribution_scalar_comparisons=comparisons,distribution_max_scaled_error=str(maximum),
                critical_precision_and_boundary_checks=critical)



def audit_weighted():
    import numpy as np
    summary=json.loads((HERE/'weighted_results.json').read_text())
    assert summary['status']=='PASS'
    assert hashlib.sha256((HERE/'weighted_sweep.py').read_bytes()).hexdigest()==summary['source_sha256']
    total_rows=0
    max_sum_error=0.0
    max_identity_error=0.0
    checked_fits=0
    max_metric_error=0.0
    references=[]
    for fileinfo in summary['trajectory_files']:
        path=HERE/fileinfo['file']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==fileinfo['sha256']
        ptext=None
        observed=[]
        variances=[]
        fourth_sums=[]
        targets={997,4093,131072}
        selected={}
        with gzip.open(path,'rt',newline='') as handle:
            for expected_n,row in enumerate(csv.DictReader(handle),1):
                assert int(row['n'])==expected_n
                ptext=row['p'] if ptext is None else ptext
                assert row['p']==ptext
                v,q,g,e=(float(row[k]) for k in ('variance','sum_fourth_weights','gamma4','effective_count'))
                assert all(math.isfinite(x) for x in (v,q,g,e))
                assert v>0 and q>0 and g<0 and e>0
                max_identity_error=max(max_identity_error,abs(g/(-2*q/v**2)-1),abs(e/(v*v/q)-1))
                observed.append(g);variances.append(v);fourth_sums.append(q)
                if expected_n in targets:
                    selected[expected_n]=(v,q,g)
        assert len(observed)==131072==fileinfo['data_rows']
        total_rows+=len(observed)
        p=float(ptext)
        # Fresh direct sums at unadvertised intermediate n; no zeta or prefix sum reuse.
        for count,(v,q,g) in selected.items():
            direct2=math.fsum(j**(2*p) for j in range(1,count+1))
            direct4=math.fsum(j**(4*p) for j in range(1,count+1))
            expected=(direct2,direct4,-2*direct4/direct2**2)
            errors=[abs(a/b-1) for a,b in zip((v,q,g),expected)]
            maximum=max(errors)
            assert maximum<2e-13,(ptext,count,errors)
            max_sum_error=max(max_sum_error,maximum)
            references.append(dict(p=ptext,n=count,max_relative_error=maximum))
        if ptext not in ('-0.5','-0.25','0','1'):
            continue
        y=np.array(observed)
        v=np.array(variances)
        n=np.arange(1,len(y)+1,dtype=float)
        for record in summary['fits'][ptext]:
            name=record['candidate']
            if name=='inverse_neff':
                continue  # Algebraic identity is checked at all exported points.
            start,end=record['train_start'],record['train_end']
            train=slice(start-1,end)
            if name in ('free_time_power','free_width_power'):
                x=np.log(n if name=='free_time_power' else np.sqrt(v))
                design=np.column_stack((np.ones(end-start+1),x[train]))
                intercept,slope=np.linalg.lstsq(design,np.log(-y[train]),rcond=None)[0]
                prediction=-np.exp(intercept+slope*x)
                assert math.isclose(-slope,record['fitted_exponent'],rel_tol=1e-8,abs_tol=1e-10)
            else:
                if name=='constant': shape=np.ones_like(n)
                elif name=='inverse_time': shape=1/n
                elif name=='inverse_time_squared': shape=1/n**2
                elif name=='inverse_width_squared': shape=1/v
                elif name=='theoretical_regime':
                    if p==-0.5: shape=1/np.log1p(n)**2
                    elif p==-0.25: shape=np.log1p(n)/n
                    else: shape=1/n
                else: raise AssertionError(name)
                amplitude=np.linalg.lstsq(shape[train,None],y[train],rcond=None)[0][0]
                assert math.isclose(amplitude,record['amplitude'],rel_tol=1e-10,abs_tol=1e-12)
                prediction=amplitude*shape
            for metric_name in ('heldout_all_later','heldout_next_block','heldout_far_half'):
                recorded=record[metric_name]
                a,b=recorded['start'],recorded['end']
                assert a>end and b<=len(y)
                delta=prediction[a-1:b]-y[a-1:b]
                metric=float(np.linalg.norm(delta)/np.linalg.norm(y[a-1:b]))
                error=abs(metric-recorded['relative_rmse'])/max(1,abs(recorded['relative_rmse']))
                assert error<1e-9,(ptext,name,start,end,metric_name,error)
                max_metric_error=max(max_metric_error,error)
            checked_fits+=1
    assert total_rows==summary['design']['exported_timepoints']
    assert max_identity_error<2e-14
    return dict(exported_rows_checked=total_rows,files_checked=len(summary['trajectory_files']),
                direct_sum_checks=references,maximum_direct_sum_relative_error=max_sum_error,
                maximum_identity_relative_error=max_identity_error,independent_lstsq_fits_checked=checked_fits,
                maximum_holdout_metric_scaled_error=max_metric_error,
                fitting_inspection='coefficients use only declared training slices; known future weights in N_eff explicitly labelled structural identity')


def audit_markov():
    import numpy as np
    summary=json.loads((HERE/'markov_results.json').read_text())
    assert summary['audit']['status']=='PASS'
    assert hashlib.sha256((HERE/'markov_sweep.py').read_bytes()).hexdigest()==summary['source_sha256']
    horizon=summary['horizon']
    total_rows=total_undefined=0
    max_oracle_error=D(0)
    max_metric_error=0.0
    fit_count=excluded_count=0
    references=[]
    fit_cases={'rho_m1','rho_m0p999999','rho_m0p5','star_m0p000001','star_0','star_0p000001','rho_1'}
    with localcontext() as ctx:
        ctx.prec=100
        for case in summary['cases']:
            path=HERE/case['file']['path']
            assert hashlib.sha256(path.read_bytes()).hexdigest()==case['file']['sha256']
            parameter=(D(3).sqrt()-2+D(case['critical_offset'])
                       if case['critical_offset'] is not None else D(case['rho_expression']))
            values=[]
            selected={}
            undefined=flips=zeros=0
            previous_sign=None
            with gzip.open(path,'rt',newline='') as handle:
                for expected_n,row in enumerate(csv.DictReader(handle),1):
                    assert int(row['n'])==expected_n and row['case']==case['id']
                    v,k=D(row['variance']),D(row['kappa4'])
                    assert v.is_finite() and k.is_finite() and v>=0
                    if row['gamma4']=='':
                        assert v==0 and k==0 and parameter==-1 and expected_n%2==0
                        assert row['status']=='ZERO_VARIANCE_NORMALIZATION_UNDEFINED'
                        gamma=None
                        values.append(float('nan'))
                        undefined+=1
                        previous_sign=None
                    else:
                        gamma=D(row['gamma4'])
                        assert gamma.is_finite() and v>0 and row['status']=='OK'
                        assert rel_error(gamma,k/(v*v))<D('5e-15')
                        sign=(gamma>0)-(gamma<0)
                        flips+=int(previous_sign is not None and previous_sign*sign<0)
                        zeros+=int(sign==0)
                        previous_sign=sign
                        values.append(float(gamma))
                    if expected_n in {2,3,17,997,4093,horizon-1,horizon}:
                        selected[expected_n]=dict(variance=v,kappa4=k,gamma4=gamma)
            assert len(values)==horizon==case['rows']
            assert undefined==case['undefined_rows']
            assert flips==case['adjacent_sign_flip_count']
            assert zeros==case['exact_zero_gamma_rows']
            total_rows+=len(values)
            total_undefined+=undefined
            for n,actual in selected.items():
                reference=tilted_matrix_moments(parameter,n,100)
                largest=D(0)
                for key,expected in reference.items():
                    if expected is None:
                        assert actual[key] is None
                    else:
                        error=abs(actual[key]-expected)/max(abs(expected),D('1e-70'))
                        assert error<D('5e-15'),(case['id'],n,key,error)
                        largest=max(largest,error)
                max_oracle_error=max(max_oracle_error,largest)
                references.append(dict(case=case['id'],n=n,max_relative_error=str(largest)))
            if case['id'] not in fit_cases:
                continue
            values=np.array(values)
            times=np.arange(1,horizon+1,dtype=float)
            valid=np.isfinite(values)
            for window in case['fit_windows']:
                lo,hi=window['train']
                assert window['heldout']==[hi+1,horizon]
                train=valid&(times>=lo)&(times<=hi)
                held=valid&(times>hi)
                assert int(train.sum())==window['train_valid']
                assert int(held.sum())==window['heldout_valid']
                nt,nh=times[train],times[held]
                yt,yh=values[train],values[held]
                for name,record in window['models'].items():
                    if name=='signed_free_power':
                        sign_consistent=np.all(yt>0) or np.all(yt<0)
                        if not sign_consistent:
                            assert record['status']=='EXCLUDED_TRAIN_SIGN_CHANGE_OR_ZERO'
                            excluded_count+=1
                            continue
                        assert record['status']=='FIT'
                        x,z=np.log(nt),np.log(abs(yt))
                        dx=x-x.mean()
                        slope=float(np.dot(dx,z-z.mean())/np.dot(dx,dx))
                        intercept=float(z.mean()-slope*x.mean())
                        amplitude=float(np.sign(yt[0])*np.exp(intercept))
                        prediction=amplitude*np.exp(slope*np.log(nh))
                        assert math.isclose(slope,record['coefficients']['power_exponent'],rel_tol=1e-8,abs_tol=1e-10)
                    else:
                        powers={'constant':[0],'C/n':[-1],'C/n^2':[-2],'C/n+D/n^2':[-1,-2]}[name]
                        design=np.column_stack([nt**power for power in powers])
                        # Different solve: unscaled QR, versus generator's scaled SVD.
                        q,r=np.linalg.qr(design,mode='reduced')
                        coef=np.linalg.solve(r,q.T@yt)
                        prediction=np.column_stack([nh**power for power in powers])@coef
                        for power,coefficient in zip(powers,coef):
                            expected=record['coefficients'][str(power)]
                            assert abs(coefficient-expected)/max(1,abs(expected))<2e-7,(case['id'],hi,name)
                    observed_metric=record['heldout']['normalized_rmse']
                    metric=float(np.linalg.norm(prediction-yh)/np.linalg.norm(yh))
                    error=abs(metric-observed_metric)/max(1,abs(observed_metric))
                    assert error<1e-8,(case['id'],hi,name,error)
                    assert int(np.count_nonzero(prediction*yh<0))==record['heldout']['wrong_sign_count']
                    max_metric_error=max(max_metric_error,error)
                    fit_count+=1
    assert total_rows==summary['timepoint_rows']
    assert total_undefined==horizon//2
    return dict(exported_rows_checked=total_rows,files_checked=len(summary['cases']),
                undefined_points_checked=total_undefined,independent_spectral_reference_points=references,
                maximum_spectral_relative_error=str(max_oracle_error),independent_QR_or_centered_OLS_fits_checked=fit_count,
                excluded_signed_power_fits_checked=excluded_count,maximum_holdout_metric_scaled_error=max_metric_error,
                fitting_inspection='fits and free-power sign exclusions use training values only; null points excluded with counts preserved')

def serializable(value):
    if isinstance(value,(D,F)):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    result=dict(auditor=AUDITOR,kind='independent_research_internal_audit',
                formal_driver_acceptance=False,self_checks=independent_self_checks())
    result['weighted']=audit_weighted()
    result['markov']=audit_markov()
    result['status']='PASS'
    result['generator_hashes']={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ('weighted_sweep.py','markov_sweep.py') if (HERE/name).exists()}
    result['summary_hashes']={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ('weighted_results.json','markov_results.json')}
    result['audit_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE/'audit_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=serializable)+'\n')
    print(json.dumps({'status':result['status'],'weighted_rows':result.get('weighted',{}).get('exported_rows_checked'),'markov_rows':result.get('markov',{}).get('exported_rows_checked'),'maximum_spectral_relative_error':result.get('markov',{}).get('maximum_spectral_relative_error')},default=serializable))


if __name__=='__main__':
    main()
