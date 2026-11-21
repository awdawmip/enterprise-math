"""Quick checks for the saved C87 complete QT certificate.

No full integral mesh is silently rerun. Use certify_qt_complete.py for
the complete 234-second reproduction in this environment.
"""
from fractions import Fraction as F
from pathlib import Path
import contextlib,hashlib,io,json
import verify_qt_geometry as geometry

def run():
    root=Path(__file__).parent
    with contextlib.redirect_stdout(io.StringIO()):geometry.run()
    geometric=json.loads((root/'qt_geometry_checks.json').read_text())
    cert=json.loads((root/'complete_qt_certificate.json').read_text())
    b=cert['kappa3'];den=int(b['denominator'])
    assert den==2**112
    lo,hi=F(int(b['lower_numerator']),den),F(int(b['upper_numerator']),den)
    assert F(17101,10000)<lo<hi<F(17833,10000)
    priorlo=F(8879797996758579248357681281004993,2**112)
    priorhi=F(9325116056440067185142329372765413,2**112)
    assert priorlo<lo<hi<priorhi
    components=['head','exact_middle','bounded_middle','tail']
    for field in ['lower_numerator','upper_numerator']:
        assert sum(int(cert[p][field])for p in components)==int(b[field])
    for name,digest in cert['source_sha256'].items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
    assert cert['area_mesh_per_unit']==1024
    assert cert['QT_whole_cell_mesh_per_axis']==64
    result={
        'status':'PASS',
        'exact_geometry_checks':geometric['status'],
        'exact_rational_source_cases':geometric['exact_rational_source_cases'],
        'independent_source_eliminations':geometric['independent_eliminations'],
        'directed_point_enclosure_checks':geometric['directed_point_enclosure_checks'],
        'whole_cell_boundary_boxes':geometric['whole_cell_boundary_boxes'],
        'saved_certificate_source_bindings':len(cert['source_sha256']),
        'certificate_component_sum':'PASS',
        'strict_kappa_bounds':['17101/10000','17833/10000'],
        'strict_improvement_over_C86_both_endpoints':True,
        'C86_immutable_commit':'16aa076c692d75590549e13aad3128eb34cb285f',
        'proof_sha256':hashlib.sha256((root/'QT_POSITIVE_INTEGRAL.md').read_bytes()).hexdigest(),
        'finite_checks_are_universal_proof':False,
        'complete_integral_meshes_recomputed_here':False}
    (root/'complete_qt_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
