"""Non-certified Monte Carlo estimate of the C83 triangle-gap constant.

For every rounded sample, the first two points are found exactly: the
dyadic basis and affine coefficients are converted to integers, and each
expanding triangle is completely searched by lattice rows. Statistical
sampling error is not bounded rigorously. The Haar inputs use ordinary
floating-point trigonometric functions.
"""
from argparse import ArgumentParser
from collections import Counter
from math import cos, sin, pi, sqrt, isfinite
from pathlib import Path
from time import perf_counter
import heapq
import json
import sys
import numpy as np


def ceildiv(n,d):
    return -((-n)//d)


def exact_sample(basis,shift):
    pairs=[float(x).as_integer_ratio() for x in basis]
    D=max(d for _,d in pairs)
    a,b,c,d=[n*(D//q) for n,q in pairs]
    pairs=[float(x).as_integer_ratio() for x in shift]
    S=max(q for _,q in pairs)
    s,t=[n*(S//q) for n,q in pairs]
    determinant=a*d-b*c
    assert determinant>0
    return a,b,c,d,D,S,s,t,determinant


def row_candidates(sample,R):
    a,b,c,d,D,S,s,t,det=sample
    # p=B*(m+s/S,n+t/S), with B=[[a,c],[b,d]]/D.
    den=det*S
    n_vertices=(-t*det,-b*D*R*S-t*det,a*D*R*S-t*det)
    nlo=ceildiv(min(n_vertices),den)
    nhi=max(n_vertices)//den
    vx,vy=a*S,b*S
    slope=vx+vy
    values=[]
    for n in range(nlo,nhi+1):
        qx=a*s+c*(n*S+t)
        qy=b*s+d*(n*S+t)
        lower=upper=None
        feasible=True
        for v,q in ((vx,qx),(vy,qy)):
            if v>0:
                z=ceildiv(-q,v);lower=z if lower is None else max(lower,z)
            elif v<0:
                z=(-q)//v;upper=z if upper is None else min(upper,z)
            elif q<0:
                feasible=False
        if not feasible or (lower is not None and upper is not None and lower>upper):
            continue
        if slope>=0:
            assert lower is not None
            first,step=lower,1
        else:
            assert upper is not None
            first,step=upper,-1
        for m in (first,first+step):
            if lower is not None and m<lower or upper is not None and m>upper:
                continue
            x,y=qx+vx*m,qy+vy*m
            assert x>=0 and y>=0
            value=x+y
            if value<=R*D*S:
                values.append(value)
    return heapq.nsmallest(2,values),nhi-nlo+1


def first_two(sample,max_doublings=40):
    R=2;rows=0
    for count in range(max_doublings+1):
        values,nrows=row_candidates(sample,R);rows+=nrows
        if len(values)==2:
            return values,R,count,rows
        R*=2
    raise RuntimeError('No first-two certificate after maximum triangle expansion')


def brute_check(sample,R):
    a,b,c,d,D,S,s,t,det=sample
    den=det*S
    ns=(-t*det,-b*D*R*S-t*det,a*D*R*S-t*det)
    ms=(-s*det,d*D*R*S-s*det,-c*D*R*S-s*det)
    nlo,nhi=ceildiv(min(ns),den),max(ns)//den
    mlo,mhi=ceildiv(min(ms),den),max(ms)//den
    if (nhi-nlo+1)*(mhi-mlo+1)>200000:
        return None
    found=[]
    for n in range(nlo,nhi+1):
        for m in range(mlo,mhi+1):
            x=a*(m*S+s)+c*(n*S+t)
            y=b*(m*S+s)+d*(n*S+t)
            if x>=0 and y>=0 and x+y<=R*D*S:
                found.append(x+y)
    return heapq.nsmallest(2,found)


def calculate(count,seed,batches=20):
    started=perf_counter();rng=np.random.default_rng(seed)
    random=rng.random((count,5))
    gaps=[];expansions=Counter();failures=[];checked=skipped=0
    max_R=max_rows=0;max_covolume_error=0.;min_V=1.;max_y=0.
    for index,(U,V,Z,s,t) in enumerate(random):
        if V==0:
            failures.append({'index':index,'reason':'V was zero; no replacement sample'});continue
        phi=pi*(U-.5)/3
        x,y=sin(phi),cos(phi)/V
        angle=pi*Z;ca,sa=cos(angle),sin(angle);r=sqrt(y)
        basis=(ca/r,sa/r,(ca*x-sa*y)/r,(sa*x+ca*y)/r)
        exact=exact_sample(basis,(s,t))
        try:
            values,R,nexp,rows=first_two(exact)
        except Exception as err:
            failures.append({'index':index,'reason':str(err)});continue
        if checked<64:
            brute=brute_check(exact,R)
            if brute is None:skipped+=1
            else:
                assert brute==values
                checked+=1
        *_,D,S,_,_,det=exact
        gap=(values[1]-values[0])/(S*sqrt(det))
        # D*S is the physical numerator denominator; normalizing the
        # dyadic covolume det/D^2 cancels D, leaving S*sqrt(det).
        assert isfinite(gap) and gap>=0
        gaps.append(gap);expansions[nexp]+=1
        max_R=max(max_R,R);max_rows=max(max_rows,rows)
        max_covolume_error=max(max_covolume_error,abs(det/(D*D)-1))
        min_V=min(min_V,V);max_y=max(max_y,y)
    a=np.array(gaps,dtype=float)
    k=2*sqrt(2)
    means=[float(np.mean(b))*k for b in np.array_split(a,batches) if len(b)]
    se=float(np.std(a,ddof=1)/sqrt(len(a)))*k
    mean=float(np.mean(a))*k
    return {'status':'NON_CERTIFIED_MONTE_CARLO','seed':seed,'generator':'numpy.default_rng / PCG64',
      'requested_samples':count,'completed_samples':len(gaps),'failures':failures,
      'Haar_parameters':{'phi':'pi*(U-1/2)/3','x':'sin(phi)','y':'cos(phi)/V',
        'rotation':'pi*Z','affine_shift':'B*(s,t); U,V,Z,s,t independent uniform(0,1)'},
      'statistical_scope':'Floating-point Haar sampling and ordinary sample standard errors; no certified confidence interval or rigorous quadrature error.',
      'first_two_scope':'Exact integer row enumeration for the dyadic basis and affine coefficients, then covolume normalization.',
      'gap_mean':float(np.mean(a)),'kappa3_estimate':mean,'sample_standard_error':se,
      'normal_95_percent_interval_descriptive_only':[mean-1.96*se,mean+1.96*se],
      'batch_kappa3_means':means,'gap_quantiles':{str(q):float(np.quantile(a,q)) for q in [0,.5,.9,.99,.999,1]},
      'adaptive_expansion_histogram':dict(sorted(expansions.items())),
      'initial_triangle_radius':2,'maximum_allowed_doublings':40,
      'max_triangle_radius':max_R,'max_total_rows_per_sample':max_rows,
      'no_window_truncation_for_completed_samples':True,
      'exact_brute_crosschecks':checked,'brute_crosschecks_skipped_for_size':skipped,
      'minimum_V_sampled':min_V,'maximum_y_sampled':max_y,
      'maximum_dyadic_covolume_error_before_normalization':max_covolume_error,
      'numpy_version':np.__version__,'python_version':sys.version,
      'elapsed_seconds':perf_counter()-started}


if __name__=='__main__':
    p=ArgumentParser();p.add_argument('--samples',type=int,default=200000)
    p.add_argument('--seed',type=int,default=20261119)
    p.add_argument('--output',type=Path,default=Path(__file__).with_name('triangle_gap_estimate.json'))
    args=p.parse_args();out=calculate(args.samples,args.seed)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
