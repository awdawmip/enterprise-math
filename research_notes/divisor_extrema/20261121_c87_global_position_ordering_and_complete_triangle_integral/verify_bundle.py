#!/usr/bin/env python3
"""C87 quick verification. Full adaptive and kappa meshes are not rerun.

Checks saved whole-interval coverage and strict margins, independently
recomputed radial and position integrals, exact finite algebra and geometry,
source bindings, and the scope of an explicitly unproved strengthening.
"""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
Q=2**112


def interval(v):
    assert int(v['denominator'])==Q
    a,b=F(int(v['lower_numerator']),Q),F(int(v['upper_numerator']),Q)
    assert a<=b
    return a,b


def family_check():
    d=json.loads((ROOT/'integrated_kernel_certificate.json').read_text())
    assert d['status']=='PASS' and d['r_grid']==96
    assert d['interval_bits']==112
    rows=d['intervals'];last=F(1,8);ratios=[]
    assert len(rows)==d['accepted_x_intervals']==60
    for row in rows:
        a,b=map(F,row['x_interval'])
        assert a==last and a<b<=1
        last=b
        lower,upper=interval(row['A_interval'])
        centerlo,centerhi=interval(row['center'])
        _,errorhi=interval(row['error'])
        assert lower==centerlo-errorhi and upper==centerhi+errorhi
        assert row['interior_r_cells']+row['boundary_r_cells']==96
        assert lower>b*b/200
        ratios.append(lower/b**2)
    assert last==1
    assert min(ratios)==F(d['actual_minimum_certified_ratio'])
    assert min(ratios)>F(1,200)
    for name,digest in d['source_sha256'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    chamber=ROOT/'inputs/c86/smallarea/mellin_chambers.json'
    assert hashlib.sha256(chamber.read_bytes()).hexdigest()==d['chamber_source_sha256']
    assert (ROOT/'positions/mellin_chambers.json').read_bytes()==chamber.read_bytes()
    return {'status':'PASS','complete_closed_intervals':len(rows),
            'domain':['1/8','1'],'strict_lower_bound':'1/200',
            'source_bindings':len(d['source_sha256'])+1,
            'saved_integer_root_checks':d['integer_root_checks'],
            'adaptive_family_mesh_recomputed':False}


def inherited_check():
    rows=json.loads((ROOT/'inputs/INHERITED_PROOF_FILES.json').read_text())
    for row in rows:
        p=ROOT/row['bundled_path']
        assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
    return {'status':'PASS','unchanged_bundled_proof_files':len(rows)}


def execute(relative):
    process=subprocess.run([sys.executable,str(ROOT/relative)],cwd=ROOT,
                           capture_output=True,text=True,check=True)
    data=json.loads(process.stdout)
    assert data['status']=='PASS',relative
    return data


def main():
    checks={'whole_interval_positive_margin':family_check(),
            'inherited_proof_sources':inherited_check()}
    scripts=[
        ('position_expansion_and_values','positions/verify_positions.py'),
        ('low_half_pointwise_theorem','positivity/certify_low_half.py'),
        ('QT_two_eliminations_and_saved_integral','triangle/verify_complete_qt.py'),
        ('QT_independent_original_3D_polytope','positivity/audit_qt_integral.py'),
        ('conditional_high_half_local_joins','positivity/verify_high_half_joins.py')]
    with ThreadPoolExecutor(max_workers=3) as pool:
        jobs=[(name,pool.submit(execute,path)) for name,path in scripts]
        for name,job in jobs:checks[name]=job.result()
    assert checks['conditional_high_half_local_joins']['concavity_sign_inequality_proved'] is False
    result={'schema':'C87_BUNDLE_QUICK_CHECKS_V1','status':'PASS',
            'passed_groups':len(checks),'failed_groups':0,
            'full_adaptive_family_mesh_recomputed':False,
            'full_outer_kappa_mesh_recomputed':False,
            'external_peer_review_claimed':False,'checks':checks}
    (ROOT/'checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','passed_groups':len(checks),'failed_groups':0,
                      'full_meshes_recomputed':False},indent=2))


if __name__=='__main__':main()
