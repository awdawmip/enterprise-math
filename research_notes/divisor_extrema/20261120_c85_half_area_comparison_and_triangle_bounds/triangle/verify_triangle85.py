#!/usr/bin/env python3
"""Quick C85 certificate verification; does not rerun integration meshes."""
from fractions import Fraction
from pathlib import Path
import hashlib,json
from classify_small_triangles import enumerate_cases

ROOT=Path(__file__).parent

def verify():
    cases=enumerate_cases()
    saved=json.loads((ROOT/'small_triangle_checks.json').read_text())
    assert len(cases)==34 and saved['case_count']==34
    # JSON changes tuple containers to lists; compare the serialized structure.
    assert json.loads(json.dumps(cases))==saved['cases']
    certificates=[]
    for file,script in [('extended_certificate.json','certify_extended.py'),
                        ('middle_bounds_certificate.json','certify_middle_bounds.py'),
                        ('parallelogram_certificate.json','certify_farey_parallelogram.py')]:
        d=json.loads((ROOT/file).read_text())
        def endpoints(name):
            e=d[name];q=int(e['denominator'])
            assert q==2**112
            return Fraction(int(e['lower_numerator']),q),Fraction(int(e['upper_numerator']),q)
        parts=[endpoints(p)for p in ['head','exact_middle','bounded_middle','tail']]
        whole=endpoints('kappa3')
        assert sum(p[0]for p in parts)==whole[0]
        assert sum(p[1]for p in parts)==whole[1]
        assert whole[0]<=whole[1]
        assert hashlib.sha256((ROOT/script).read_bytes()).hexdigest()==d['script_sha256']
        for key,path in [('middle_script_sha256','certify_middle_bounds.py'),
                         ('extended_script_sha256','certify_extended.py'),
                         ('interval_kernel_sha256','c84_interval_kernel.py')]:
            if key in d:assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==d[key]
        certificates.append(whole)
    assert certificates[0][0]<=certificates[1][0]==certificates[2][0]
    assert certificates[2][1]<certificates[1][1]<certificates[0][1]
    assert Fraction(16529,10000)<certificates[2][0]
    assert certificates[2][1]<Fraction(979,500)<2
    b=(ROOT/'c84_interval_kernel.py').read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()=='64cb09dc3ff3c537c5604a55a2e06ba26a952a5e'
    assert Fraction(181,256)**2<Fraction(1,2)
    assert Fraction(181,256)**2*8<4
    assert Fraction(2,3)**2*9==4
    assert Fraction(1183,1024)**2>Fraction(4,3)
    return {'status':'PASS','exact_triangle_source_cases':34,
            'saved_certificates_checked':3,'full_integral_meshes_recomputed':False,
            'strict_final_bounds':['16529/10000','979/500'],
            'pinned_C84_kernel_blob':'64cb09dc3ff3c537c5604a55a2e06ba26a952a5e',
            'checks':['finite triangle identities','certificate sums',
                      'source-byte bindings','nested intervals','strict rational bounds',
                      'row cutoff inequalities']}

if __name__=='__main__':
    result=verify()
    (ROOT/'triangle85_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
