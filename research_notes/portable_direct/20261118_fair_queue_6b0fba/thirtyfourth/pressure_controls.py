"""Supplement after preregistered benchmark: include fixed LU and direct face updates."""
import argparse
import hashlib
import json
import resource
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import splu
from threadpoolctl import threadpool_limits

from pressure_bench import HERE, NOW, NORM, PLAN, load_pilot, make_cases, run_method, scaled


def simple(method,frames,u,weights,g):
    start = NOW()
    lu = splu(frames[0][0].tocsc())
    w = gram = None
    setup = NOW()-start
    records = []
    for a,b,reference,amp in frames:
        start = NOW()
        solution = lu.solve(b)
        if method=='face_lu' and amp:
            if w is None:
                w = lu.solve(u)
                gram = u.T@w
            diagonal = amp*weights
            correction = np.linalg.solve(np.eye(4)+diagonal[:,None]*gram,diagonal*(u.T@solution))
            solution -= w@correction
        residual = scaled(NORM(b-a@solution),NORM(b))
        seconds = NOW()-start
        err = float(abs(g@(solution-reference)))
        records.append({'s':seconds,'e':err,'r':float(residual),'ok':bool(err<=1e-4 and residual<=1e-3)})
    return {'setup_s':setup,'frames':records,'s':setup+sum(r['s'] for r in records)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--archive',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args = ap.parse_args()
    pilot = load_pilot(args.archive)
    rng = np.random.default_rng(1873402)
    out = {'seed':1873402,'repetitions':5,'grids':{},'post_primary':True,
           'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'bench_sha256':hashlib.sha256((HERE/'pressure_bench.py').read_bytes()).hexdigest(),
           'source_zip_sha256':PLAN['source_sha256']}
    with threadpool_limits(limits=1):
        for n in PLAN['grids']:
            cases,g,lmin,u,weights,tol,*_ = make_cases(pilot,n)
            results = {}
            for case,frames in cases.items():
                methods = ['static_lu','trigger'] + ([] if case=='smooth' else ['face_lu'])
                records = {'orders':[],'runs':{m:[] for m in methods}}
                for k in range(5):
                    order = [str(m) for m in rng.permutation(methods)]
                    records['orders'].append(order)
                    for m in order:
                        if m=='trigger':
                            result = run_method(m,frames,n,g,lmin,u,weights,tol,case)
                        else:
                            result = simple(m,frames,u,weights,g)
                        records['runs'][m].append(result)
                results[case] = records
            out['grids'][str(n)] = results
    out['whole_process_max_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    args.output.write_text(json.dumps(out,separators=(',',':'),allow_nan=False)+'\n')


if __name__=='__main__':
    main()
