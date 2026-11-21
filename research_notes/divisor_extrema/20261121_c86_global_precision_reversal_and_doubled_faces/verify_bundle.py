#!/usr/bin/env python3
"""C86 reproducibility entry point: exact checks, with optional full integrals."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, time

HERE=Path(__file__).resolve().parent

def call(relative):
    p=subprocess.run([sys.executable,str(HERE/relative)],cwd=HERE,
                     text=True,capture_output=True)
    if p.returncode:
        raise RuntimeError(relative+"\n"+p.stdout+"\n"+p.stderr)
    return {"command":relative,"status":"PASS",
            "stdout_sha256":hashlib.sha256(p.stdout.encode()).hexdigest()}

def main_certificate():
    sys.path.insert(0,str(HERE/'triangle'))
    from c84_interval_kernel import I,Q,ZETA
    p=HERE/'mellin_integral_certificate.json'
    d=json.loads(p.read_text())
    chamber=HERE/'smallarea'/'mellin_chambers.json'
    assert d['chamber_source_sha256']==hashlib.sha256(chamber.read_bytes()).hexdigest()
    assert d['grid']==[96,96]
    assert d['interior_cells']+d['boundary_cells']==96**2
    def get(key):
        v=d[key];assert int(v['denominator'])==Q
        return I(int(v['lower_numerator']),int(v['upper_numerator']))
    j=get('weighted_integral')
    assert j.lo>0
    diff=(-1/(2*ZETA*F(19,20)*F(21,20)*F(41,20)))*j
    saved=get('moment_difference')
    assert (diff.lo,diff.hi)==(saved.lo,saved.hi)
    assert F(-2117,1000000)<F(saved.lo,Q)
    assert F(saved.hi,Q)<F(-1369,1000000)<0
    assert d['root_integer_checks']==217801
    assert d['strict_negative_proved'] is True
    return {"command":"main_certificate_exact_binding",
            "status":"PASS","full_cubature_rerun_by_this_check":False}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--full',action='store_true',
                        help='first recompute both complete directed integral certificates')
    args=parser.parse_args();start=time.time();runs=[]
    if args.full:
        runs.append(call('certify_mellin_integral.py'))
        runs.append(call('triangle/certify_doubled_face.py'))
    for script in [
        'smallarea/verify_finite_reduction.py',
        'phase/verify_mellin_regularities.py',
        'smallarea/certify_small_chamber.py',
        'phase/verify_exact_phase_moment.py',
        'triangle/verify_doubled_face.py',
        'smallarea/audit_doubled_face.py',
    ]:
        runs.append(call(script))
    runs.append(main_certificate())
    result={"schema":"C86_REPRODUCIBILITY_CHECKS_V1",
            "status":"PASS","mode":"full" if args.full else "exact_checks",
            "groups":len(runs),"failed":0,"runs":runs,
            "seconds":time.time()-start,
            "note":"The main and kappa integral certificates were computed in C86. "
                   "Quick mode verifies saved bindings and exact auxiliary derivations; "
                   "it does not claim to recompute their complete grids."}
    (HERE/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()

