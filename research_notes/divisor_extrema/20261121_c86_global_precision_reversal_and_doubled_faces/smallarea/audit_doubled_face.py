"""Independent algebra/certificate audit of C86's doubled triangle faces.

This is a review check, not a rerun of the outer kappa mesh. SymPy is used only
for exact rational identities and polynomial sign certificates; no float is
used for a proof assertion.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).parent
TRIANGLE = ROOT.parent / 'triangle'


def nonnegative_rational(expr, variable, left, right):
    """Certify a rational function by exact Bernstein coefficients."""
    expr = s.factor(expr)
    numerator, denominator = s.fraction(expr)
    z = s.symbols('z')
    def coefficients(poly):
        q = s.Poly(s.expand(poly.subs(variable, left + (right-left)*z)), z)
        n = q.degree()
        if n is s.S.NegativeInfinity:
            return [s.Integer(0)]
        power = [q.nth(i) for i in range(n+1)]
        return [sum(power[k]*s.binomial(i,k)/s.binomial(n,k) for k in range(i+1))
                for i in range(n+1)]
    if all(c < 0 for c in coefficients(denominator)):
        numerator, denominator = -numerator, -denominator
    assert all(c >= 0 for c in coefficients(numerator)), expr
    assert all(c > 0 for c in coefficients(denominator)), expr


def run():
    t, H, u, M, N = s.symbols('t H u M N', positive=True)
    f1 = (H-u*t)**3/(t*(1-t))
    f2 = (H-M*t)**3/(t*(1-t)**2)
    f3 = (N-u*t)**3/(1-t)**2
    P1 = H**3*s.log(t) - (H-u)**3*s.log(1-t) + u**3*t**2/2 + (u**3-3*H*u**2)*t
    P2 = H**3*s.log(t) + (H-M)**3/(1-t) - (H-M)**2*(H+2*M)*s.log(1-t) - M**3*t
    P3 = (3*N*u**2-2*u**3)*t-u**3*t**2/2-3*u*(u-N)**2*s.log(1-t)-(u-N)**3/(1-t)
    assert all(s.cancel(s.diff(P,t)-f) == 0 for P,f in [(P1,f1),(P2,f2),(P3,f3)])
    # Exact cancellation of the common H^3 log(epsilon) lower-end terms.
    polynomial = (u**3*(H/u)**2/2 + (u**3-3*H*u**2)*(H/u)
                  -(H-M)**3*H/(M-H) + M**2*H)
    expected = H*(M**2+u**2+u**(-2)-s.Rational(5,2)*H*u)
    assert s.cancel((polynomial-expected).subs(H,M-1/u)) == 0
    assert s.cancel(((H-M)**2*(H+2*M)-(3*M-1/u)/u**2).subs(H,M-1/u)) == 0
    top = 1-u**(-2)
    upper = (P3.subs(t,top)-P3.subs(t,0)).subs(N,u-1/u)
    upper = s.expand_log(upper,force=True)
    expected_upper = u**3/2-3*u+s.Rational(3,2)/u+u**(-3)+6*s.log(u)/u
    assert s.simplify(upper-expected_upper) == 0

    # Positive ordered basis multiplicities for the two actual four-vector sets.
    def det(v,w): return v[0]*w[1]-v[1]*w[0]
    def neg(v): return -v[0],-v[1]
    def add(v,w): return v[0]+w[0],v[1]+w[1]
    examples = [({(1,0),(-1,0),(0,1),(1,1)},(1,0)),
                ({(1,0),(-1,0),(0,1),(-1,-1)},(0,1))]
    for points,want in examples:
        qp=sum(det(v,w)==1 and neg(v) in points and add(v,w) in points
               for v,w in permutations(points,2))
        qt=sum(det(v,w)==1 and neg(v) in points and neg(add(v,w)) in points
               for v,w in permutations(points,2))
        assert (qp,qt)==want
    # The det-reversing basis map preserves the QP offsets exactly.
    v,w=(2,1),(1,1)
    V,W=neg(v),add(v,w)
    assert det(V,W)==-det(v,w)
    assert {v,neg(v),w,add(v,w)}=={V,neg(V),W,add(V,W)}

    # All final one-variable rational inequalities in the QT capacity proof.
    inequalities = [
        (s.Rational(1,6)-2*(1-t)/(4-3*t)**2,0,s.Rational(2,3)),
        (s.Rational(1,6)-1/(9*t),s.Rational(2,3),1),
        (s.Rational(1,6)-1/(9*(1-t)),0,s.Rational(1,3)),
        (s.Rational(1,6)-(1+t)/8,0,s.Rational(1,3)),
        (s.Rational(1,6)-2*t/(1+3*t)**2,s.Rational(1,3),1),
        (s.Rational(3,16)-3*t*(1-t)/4,s.Rational(1,2),s.Rational(2,3)),
        (s.Rational(1,6)-t/(4*(3*t-1)),s.Rational(2,3),1),
        (s.Rational(1,6)-(1-t)/(4*(2-3*t)),0,s.Rational(1,3)),
        (s.Rational(3,16)-3*t*(1-t)/4,s.Rational(1,3),s.Rational(1,2)),
        (s.Rational(1,8)-2*(1-t)/(4-t)**2,0,s.Rational(4,7)),
        (s.Rational(7,96)-1/(24*t),s.Rational(4,7),1),
        (s.Rational(7,96)-1/(24*(1-t)),0,s.Rational(3,7)),
        (s.Rational(1,8)-2*t/(3+t)**2,s.Rational(3,7),1),
        (s.Rational(1,8)-t/(4*(1+t)),s.Rational(1,2),1),
        (s.Rational(1,8)-(1-t)/(4*(2-t)),0,s.Rational(1,2)),
    ]
    for expression,left,right in inequalities:
        nonnegative_rational(expression,t,s.sympify(left),s.sympify(right))
    witness_x=(F(1,2),F(1,4));witness_v=(F(1,2),-F(1,4));witness_w=(-F(1,4),F(1,2))
    offsets=[witness_v,neg(witness_v),witness_w,neg(add(witness_v,witness_w))]
    for offset in offsets:
        point=add(witness_x,offset)
        assert min(point)>=0 and sum(point)<=1
    assert det(witness_v,witness_w)==F(3,16)

    certificate=json.loads((TRIANGLE/'doubled_face_certificate.json').read_text())
    den=int(certificate['kappa3']['denominator'])
    def bounds(name):
        row=certificate[name]
        assert int(row['denominator'])==den
        return F(int(row['lower_numerator']),den),F(int(row['upper_numerator']),den)
    lower,upper=bounds('kappa3')
    pieces=[bounds(k)for k in ['head','exact_middle','bounded_middle','tail']]
    assert sum(v[0]for v in pieces)==lower
    assert sum(v[1]for v in pieces)==upper
    assert F(17101,10000)<lower<upper<F(1796,1000)
    for name,digest in certificate['source_sha256'].items():
        assert hashlib.sha256((TRIANGLE/name).read_bytes()).hexdigest()==digest
    result={'status':'PASS','three_exact_angular_antiderivatives':True,
            'common_endpoint_log_cancellation':True,'QP_positive_basis_multiplicity':1,
            'QT_positive_basis_multiplicity':1,'QP_reflection_basis_map':True,
            'QT_rational_endpoint_inequalities':len(inequalities),
            'QT_sharp_capacity_witness':'3/16',
            'saved_kappa_sum_and_source_hashes':True,
            'strict_kappa_enclosure':['1.7101','1.796'],
            'outer_kappa_mesh_recomputed_by_review':False,
            'proof_assertions_use_floating_point':False}
    (ROOT/'doubled_face_review_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
