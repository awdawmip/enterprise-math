"""Quick exact checks for C86's doubled-face derivation and saved certificate.

This verifies algebra, the onset witness, source bindings and strict endpoints.
It does not rerun the complete numerical enclosure and does not replace the
analytic proofs or their independent human/project review.
"""
from fractions import Fraction as F
from pathlib import Path
import contextlib,hashlib,io,json
import sympy as s
import verify_chordal_identity as chordal

def run():
    t,H,u,M,N=s.symbols('t H u M N',positive=True)
    P1=(H**3*s.log(t)+u**3*t**2/2+(-3*H*u**2+u**3)*t
        +(u-H)**3*s.log(1-t))
    P2=(H**3*s.log(t)-M**3*t-(H-M)**2*(H+2*M)*s.log(1-t)
        +(H-M)**3/(1-t))
    P3=(-u**3*t**2/2+(3*N*u**2-2*u**3)*t
        -3*u*(u-N)**2*s.log(1-t)-(u-N)**3/(1-t))
    for primitive,integrand in [
        (P1,(H-u*t)**3/(t*(1-t))),
        (P2,(H-M*t)**3/(t*(1-t)**2)),
        (P3,(N-u*t)**3/(1-t)**2)]:
        assert s.factor(s.diff(primitive,t)-integrand)==0
    # After canceling the two H^3 log(epsilon) boundary terms.
    j12=(H**3*s.log(M/u)+(u-H)**3*s.log((u-H)/u)
         +(M-H)**2*(H+2*M)*s.log((M-H)/M)
         +H*u**2-s.Rational(5,2)*H**2*u+H*M**2
         +M*(M-H)**2-(M-H)**3)
    closed=(H**3*s.log(M/u)+(u-H)**3*s.log((u-H)/u)
            +(3*M-1/u)/u**2*s.log(1/(u*M))
            +H*(M**2+u**2+u**-2-s.Rational(5,2)*H*u))
    assert s.simplify((j12-closed).subs(M,H+1/u))==0
    j3=(P3.subs(t,1-u**-2)-P3.subs(t,0)).subs(N,u-1/u)
    closed3=u**3/2-3*u+s.Rational(3,2)/u+u**-3+6*s.log(u)/u
    assert s.simplify(s.expand_log(j3-closed3,force=True))==0
    # Exact factorizations used in the QT geometric extremum proof.
    identities=[
        ((4-3*t)**2-12*(1-t),(3*t-2)**2),
        ((1+3*t)**2-12*t,(3*t-1)**2),
        ((4-t)**2-16*(1-t),t**2+8*t),
        ((3+t)**2-16*t,(t-1)*(t-9))]
    for lhs,rhs in identities:assert s.expand(lhs-rhs)==0
    v=(F(1,2),F(-1,4));x=(F(1,2),F(1,4));w=(F(-1,4),F(1,2))
    points=[(x[0]-v[0],x[1]-v[1]),(x[0]+v[0],x[1]+v[1]),
            (x[0]+w[0],x[1]+w[1]),(x[0]-v[0]-w[0],x[1]-v[1]-w[1])]
    assert all(a>=0 and b>=0 and a+b<=1 for a,b in points)
    assert v[0]*w[1]-v[1]*w[0]==F(3,16)
    with contextlib.redirect_stdout(io.StringIO()):chordal.run()
    root=Path(__file__).parent
    cert=json.loads((root/'doubled_face_certificate.json').read_text())
    b=cert['kappa3'];den=int(b['denominator'])
    low,high=F(int(b['lower_numerator']),den),F(int(b['upper_numerator']),den)
    assert F(17101,10000)<low<high<F(449,250)
    for name,digest in cert['source_sha256'].items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
    proof_names=['CHORDAL_CORRECTION.md','DOUBLED_FACE_INTEGRAL.md','QT_SUPPORT.md']
    result={
        'status':'PASS',
        'angular_primitive_derivative_identities':3,
        'angular_boundary_simplifications':2,
        'QT_extremum_factorizations':4,
        'QT_exact_onset_witness_determinant':'3/16',
        'prior_chordal_finite_checks':'PASS',
        'saved_certificate_source_bindings':len(cert['source_sha256']),
        'strict_kappa_bounds':['17101/10000','449/250'],
        'proof_sha256':{name:hashlib.sha256((root/name).read_bytes()).hexdigest()
                       for name in proof_names},
        'finite_checks_are_universal_proof':False,
        'integral_meshes_recomputed_by_this_verifier':False}
    (root/'doubled_face_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
