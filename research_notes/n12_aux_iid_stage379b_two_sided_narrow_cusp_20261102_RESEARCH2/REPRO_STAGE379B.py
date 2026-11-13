#!/usr/bin/env python3
"""Stage379-B replay/generator by exact reuse of immutable Stage377-B core.

Requires the sibling Stage377-B directory in the existing Enterprise Math
research branch. Checks the exact Git blob of the reused source. No new
symbolic math backend, network access or floating-point operations.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha1,sha256
import importlib.util
import argparse
import csv
import io

ROOT=Path(__file__).resolve().parent.parent
CORE=ROOT/'n12_aux_iid_stage377b_signed_bernstein_lower_q_y_20261102_RESEARCH2'/'REPRO_STAGE377B.py'
PINNED_CORE_BLOB='9b54a83059ff965e4807577448c3828cc64e8f04'
CSV_SHA='aa48034a214df51a493d387862e12d05eed5b18681299574f41264656262d828'
CSV_SIZE=182434
B_UP=F(97582683,10**10)
LAM=F(483,400)
C_REF=F(16174336378406867755705673,256000000000000000000000000)
P=(F(577,2500),F(469,2000),F(11,20),F(14,25))
Q_LO=(F(473,2000),F(239,1000),F(11513,20000),F(57566,100000))
Q_HI=(F(473,2000),F(239,1000),F(57574,100000),F(2303,4000))
RECTS={'P':P,'Q_LO':Q_LO,'Q_HI':Q_HI}
TARGETS={'P':F(37517335,10**9),'Q_LO':F(37446850,10**9),'Q_HI':F(37446805,10**9)}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--emit',type=Path)
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    raw=CORE.read_bytes()
    blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert blob==PINNED_CORE_BLOB,(blob,PINNED_CORE_BLOB)
    spec=importlib.util.spec_from_file_location('stage377b_pinned',CORE)
    core=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    core.RECTS=RECTS
    core.TARGETS=TARGETS
    core.LAMBDA=LAM
    core.DUAL_THRESHOLD=C_REF+LAM*B_UP
    core.signed_coefficients.cache_clear()
    assert core.BUDGET_UP==B_UP and core.REFERENCE_COST==C_REF
    core.root_and_comparator_checks()
    for q in ('Q_LO','Q_HI'):
        assert TARGETS['P']+TARGETS[q]>C_REF+LAM*B_UP
    f=lambda t:16*t*t-4*t-3
    assert f(F(575693,10**6))<0<f(F(575694,10**6))
    assert F(57566,10**5)<F(575693,10**6)<F(575694,10**6)<F(57574,10**5)
    certificate,stats=core.emit_certificate()
    counts=core.verify_certificate(certificate)
    assert counts=={'P':1344,'Q_LO':37,'Q_HI':72},counts
    rows=list(csv.DictReader(io.StringIO(certificate.decode('utf8'))))
    rows.sort(key=lambda r:(('P','Q_LO','Q_HI').index(r['source']),r['path']))
    header='region,path,xlo,xhi,ylo,yhi,lower\n'
    normalized=header+''.join(','.join(r[k] for k in ('source','path','xlo','xhi','ylo','yhi','certified_L_lower'))+'\n' for r in rows)
    result=normalized.encode('utf8')
    assert len(result)==CSV_SIZE and sha256(result).hexdigest()==CSV_SHA
    if args.emit:
        args.emit.write_bytes(result)
    if args.verify:
        assert args.verify.read_bytes()==result
    print('STAGE379B_EXACT_NARROWER_CUSP_QY_PASS')
    print('pinned_stage377_core_git_blob='+blob)
    print('P_leaves='+str(counts['P'])+';Q_LO_leaves='+str(counts['Q_LO'])+';Q_HI_leaves='+str(counts['Q_HI']))
    print('Q_LO_gap='+str(TARGETS['P']+TARGETS['Q_LO']-C_REF-LAM*B_UP))
    print('Q_HI_gap='+str(TARGETS['P']+TARGETS['Q_HI']-C_REF-LAM*B_UP))
    print('certificate_bytes='+str(len(result))+';sha256='+CSV_SHA)

if __name__=='__main__':main()
