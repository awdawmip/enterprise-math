"""Reproduce time-stamped finite measurements. Requires original ZIP and SciPy."""
import argparse
import hashlib
import importlib
import json
import os
import platform
import resource
import sys
import time
import zipfile
from pathlib import Path

import numpy as np
import scipy
from scipy import sparse
from scipy.fft import dstn, idstn
from scipy.sparse.linalg import LinearOperator, cg, splu
from threadpoolctl import threadpool_limits

HERE = Path(__file__).resolve().parent
PLAN = json.loads((HERE / 'pressure_plan.json').read_text())
METHODS = PLAN['methods']
NORM = np.linalg.norm
NOW = time.perf_counter


def load_pilot(path):
    data = path.read_bytes()
    assert hashlib.sha256(data).hexdigest() == PLAN['source_sha256']
    with zipfile.ZipFile(path) as z:
        manifest = json.loads(z.read('cfd_pilot_20260928/MANIFEST.json'))
        for row in manifest['files']:
            original = z.read('cfd_pilot_20260928/' + row['name'])
            assert len(original) == row['bytes'] and hashlib.sha256(original).hexdigest() == row['sha256']
        assert len(manifest['files']) == 34 and len(z.namelist()) == 35
    sys.path.insert(0, str(path.resolve()) + '/cfd_pilot_20260928')
    return importlib.import_module('pilot')


def smooth_operator(n):
    # Weight varies only across x. Dirichlet edges are included in the diagonal.
    ids = np.arange(n*n).reshape(n,n)
    h = 1/(n+1)
    coordinates = (np.arange(n) + 1)*h
    xface = 0.6 + 0.4*(np.arange(n+1)+0.5)*h
    yface = 0.6 + 0.4*coordinates
    weights_x = np.broadcast_to(xface[1:n,None],(n-1,n)).ravel()
    weights_y = np.broadcast_to(yface[:,None],(n,n-1)).ravel()
    diagonal = np.repeat(xface[:-1]+xface[1:]+2*yface,n)
    left = np.concatenate([ids[:-1].ravel(),ids[:,:-1].ravel()])
    right = np.concatenate([ids[1:].ravel(),ids[:,1:].ravel()])
    off = -np.r_[weights_x,weights_y]
    return sparse.coo_matrix((np.r_[diagonal,off,off],
                             (np.r_[ids.ravel(),left,right],np.r_[ids.ravel(),right,left])),
                             shape=(n*n,n*n)).tocsr()/h**2


def localized_faces(n):
    coords = [(0.26,0.47),(0.31,0.53),(0.68,0.47),(0.73,0.53)]
    base = [int(x*n)*n+int(y*n) for x,y in coords]
    u = np.zeros((n*n,4))
    for j,i in enumerate(base):
        u[i,j],u[i+n,j] = n+1,-(n+1)
    weights = np.array([1,0.5,0.75,0.25])
    # U contains the physical inverse grid spacing and no conductivity weights.
    us = sparse.csr_matrix(u)
    return u, weights, (us @ sparse.diags(weights) @ us.T).tocsr()


def dst_inverse(n):
    indices = np.arange(1,n+1)
    d = 4*(n+1)**2*np.sin(np.pi*indices/(2*(n+1)))**2
    eig = np.add.outer(d,d)

    def solve(v):
        f = dstn(v.reshape(n,n),type=1,norm='ortho')
        return idstn(f/eig,type=1,norm='ortho').ravel()

    return LinearOperator((n*n,n*n),matvec=solve,dtype='float64')


def iterate(a,b,x0,pre,rtol):
    count = 0
    def receive(_):
        nonlocal count
        count += 1
    x,info = cg(a,b,x0=x0,M=pre,rtol=rtol,atol=0,maxiter=3000,callback=receive)
    return x,count,int(info)


def scaled(norm,bnorm):
    return norm/(bnorm if bnorm else 1.0)


def calibrate(matrix,training,g,n):
    pre = dst_inverse(n)
    logs = {}
    candidates = [1e-3,3e-4,1e-4,3e-5,1e-5,1e-6,1e-7]
    chosen = None
    for tol in candidates:
        metrics = []
        for b,reference in training:
            x,it,info = iterate(matrix,b,None,pre,tol)
            metrics.append([float(abs(g@(x-reference))),scaled(NORM(b-matrix@x),NORM(b)),it,info])
        logs[str(tol)] = metrics
        if all(e<=1e-4 and r<=1e-3 and info==0 for e,r,_,info in metrics):
            chosen = tol
            break
    assert chosen is not None
    return chosen,logs


def make_cases(pilot,n):
    start = NOW()
    a,x,y,g,lmin = pilot.operator(n,True)
    training = pilot.inputs(a,x,y,'train')
    references = [ref for _,ref in pilot.inputs(a,x,y,'test')]
    assert len(training) == 4 and len(references) == 12
    smooth = smooth_operator(n)
    u,weights,jump = localized_faces(n)
    jumps = [0,0,0,0,6,6,6,6,0,12,12,12]
    cases = {}
    for name in PLAN['cases']:
        frames = []
        for j,ref in enumerate(references):
            if name == 'fixed':
                matrix,amp = a,0
            elif name == 'smooth':
                amp = 0.25*(j/11)**2
                matrix = (a + amp*smooth).tocsr() if amp else a
            else:
                amp = jumps[j]
                matrix = (a + amp*jump).tocsr() if amp else a
            frames.append((matrix,matrix@ref,ref,amp))
        cases[name] = frames
    gen = NOW()-start
    start = NOW()
    tol,cal = calibrate(a,training,g,n)
    return cases, g, lmin, u, weights, tol, cal, gen, NOW()-start


def run_method(method,frames,n,g,lmin,u,weights,tol,case):
    setup_start = NOW()
    pre = dst_inverse(n) if method.startswith('dst') else None
    setup_duration = NOW()-setup_start
    lu = z = w = gram = None
    anchor_amp = 0
    last = None
    logs = []
    for j,(a,b,reference,amp) in enumerate(frames):
        begin = NOW()
        stage = {}
        it = 0
        info = 0
        checks = 0
        bnorm = NORM(b)
        decision = ''
        def mark(name,t0):
            stage[name] = stage.get(name,0) + NOW()-t0

        def rebuild(with_adjoint):
            nonlocal lu,z,w,gram,anchor_amp
            t0 = NOW()
            lu = splu(a.tocsc())
            anchor_amp = amp
            w = gram = None
            mark('factor_including_csc',t0)
            if with_adjoint:
                t0 = NOW()
                z = lu.solve(g)
                mark('adjoint',t0)

        def validate(candidate):
            nonlocal checks
            t0 = NOW()
            r = b-a@candidate
            nr = NORM(r)
            dual = float(abs(z@r) + NORM(g-a@z)*nr/lmin)
            relative = scaled(nr,bnorm)
            checks += 1
            mark('true_residual_and_adjoint_test',t0)
            return bool(relative<=1e-3 and dual<=1e-4), float(relative), dual

        dual = None
        if method in ('dst_cold','dst_warm'):
            t0 = NOW()
            solution,it,info = iterate(a,b,last if method=='dst_warm' else None,pre,tol)
            mark('dst_pcg',t0)
            decision = 'pcg'
        elif method == 'rebuild':
            rebuild(False)
            t0 = NOW()
            solution = lu.solve(b)
            mark('rhs_triangle_solves',t0)
            decision = 'rebuild'
        elif method == 'interval4':
            t0 = NOW()
            if j%4==0:
                rebuild(False)
                decision = 'refresh'
            else:
                decision = 'reuse_preconditioner'
            t0 = NOW()
            first = lu.solve(b)
            factor_pre = LinearOperator(a.shape,matvec=lu.solve,dtype='float64')
            solution,it,info = iterate(a,b,first,factor_pre,1e-8)
            mark('old_lu_and_pcg',t0)
        else:
            if lu is None:
                rebuild(True)
            t0 = NOW()
            solution = lu.solve(b)
            mark('rhs_triangle_solves',t0)
            good,relative,dual = validate(solution)
            decision = 'old_factor_accepted'
            if not good and case=='jump' and amp!=anchor_amp:
                t0 = NOW()
                if w is None:
                    w = lu.solve(u)
                    gram = u.T@w
                diagonal = (amp-anchor_amp)*weights
                correction = np.linalg.solve(np.eye(4)+diagonal[:,None]*gram,diagonal*(u.T@solution))
                solution -= w@correction
                mark('low_rank_setup_and_update',t0)
                good,relative,dual = validate(solution)
                decision = 'low_rank_accepted'
            if not good:
                rebuild(True)
                t0 = NOW()
                solution = lu.solve(b)
                mark('rhs_triangle_solves',t0)
                good,relative,dual = validate(solution)
                if not good:
                    raise ArithmeticError('rebuild failed numerical certificate')
                decision = 'rejected_then_rebuilt'

        if method != 'trigger':
            t0 = NOW()
            relative = scaled(NORM(b-a@solution),bnorm)
            mark('true_residual',t0)
        elapsed = NOW()-begin
        # The private manufactured reference is available only to evaluation.
        evaluation = NOW()
        err = float(abs(g@(solution-reference)))
        ok = bool(err<=1e-4 and relative<=1e-3 and info==0)
        evaluate_seconds = NOW()-evaluation
        logs.append({'d':decision,'s':elapsed,'stages':stage,'evaluation_s':evaluate_seconds,
                     'e':err,'r':float(relative),'bound':dual,'it':it,'info':info,'checks':checks,'ok':ok})
        last = solution
    return {'setup_s':setup_duration,'s':setup_duration+sum(row['s'] for row in logs),'frames':logs}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--archive',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    args = parser.parse_args()
    since = NOW()
    pilot = load_pilot(args.archive)
    source_time = NOW()-since
    rng = np.random.default_rng(PLAN['seed'])
    output = {'plan_sha256':hashlib.sha256((HERE/'pressure_plan.json').read_bytes()).hexdigest(),
              'bench_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_zip_sha256':PLAN['source_sha256'],'source_manifest_files_verified':34,
              'environment':{'python':sys.version.split()[0],'numpy':np.__version__,'scipy':scipy.__version__,
                             'os':platform.platform(),'logical_cpus':os.cpu_count()},
              'source_check_and_import_s':source_time,'grids':{}}
    with threadpool_limits(limits=1):
        for n in PLAN['grids']:
            cases,g,lmin,u,weights,tol,cal,gen,cal_time = make_cases(pilot,n)
            results = {'common_data_generation_s':gen,'calibration_s':cal_time,'calibration':cal,
                       'selected_tol':tol,'cases':{}}
            for case,frames in cases.items():
                result = {'orders':[],'runs':{method:[] for method in METHODS}}
                for rep in range(PLAN['repetitions']):
                    order = [str(m) for m in rng.permutation(METHODS)]
                    result['orders'].append(order)
                    for method in order:
                        result['runs'][method].append(run_method(method,frames,n,g,lmin,u,weights,tol,case))
                results['cases'][case] = result
                print(n,case,'completed',flush=True)
            output['grids'][str(n)] = results
    output['whole_process_max_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    args.output.write_text(json.dumps(output,separators=(',',':'),allow_nan=False)+'\n')


if __name__=='__main__':
    main()
