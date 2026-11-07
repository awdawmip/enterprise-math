#!/usr/bin/env python3
"""R375: exact seventh-corank global PF2 phase of a signed BRC K3 deformation.

Run from Enterprise Math PR #1592 checkout:
    python research_notes/r375_signed_k3_corank7_20261029_emr3/R375_verify.py --independent
Requires SymPy.  Derived solely from the original R346 signed twelve-term
K/J -> B -> D -> raw minors recurrence, without the R348/R363 all-index claim.
Exact interval signs use rational Bernstein coefficients, never sampling.
"""
from __future__ import annotations
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path
from sympy import Poly, Rational, Symbol, binomial, diff, expand

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K, J

theta = Symbol('theta')

def clean(values):
    z = list(values)
    while z and z[-1] == 0:
        z.pop()
    return tuple(z)

def add(a, b):
    return clean((a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b))))

def scale(a, q):
    return clean(v*q for v in a)

def multiply(a, b):
    if not a or not b:
        return ()
    out = [0]*(len(a) + len(b)-1)
    for i, va in enumerate(a):
        for j, vb in enumerate(b):
            out[i+j] += va*vb
    return clean(out)

def row_coefficients():
    """Fifteen raw-D finite minor observations, then differences j=0..14.

    r=7: highest B index is q+1+(k+1)=39; highest t degree 23.
    Coefficient arrays retain the full signed K/J polynomial algebra.
    """
    S, P = 39, 23
    signed_K = [None] + [
        [((int(value),) if value else ()) for value in K(i)[:P+1]]
        for i in range(1,13)
    ]
    assert signed_K[3][2] == (-8,)
    signed_K[3][2] = (-8, -8)
    B = [[() for _ in range(P+1)] for _ in range(S+1)]
    B[0][0] = B[0][1] = (1,)
    for s in range(1, S+1):
        for j, value in enumerate(J(s)[:P+1]):
            if value:
                B[s][j] = (int(value),)
        for i in range(1,min(s,12)+1):
            for j, value in enumerate(signed_K[i]):
                if not value:
                    continue
                for p in range(j,P+1):
                    if B[s-i][p-j]:
                        B[s][p] = add(B[s][p],multiply(value,B[s-i][p-j]))
    def D(q,k):
        result = ()
        for w in range(k+1):
            result = add(result,scale(B[q+w][q],
                        (-1)**(k-w)*comb(k,w)*2**(q-w)))
        return result
    observations = []
    for v in range(15):
        k = v+1
        q = 7+k
        minor = add(multiply(D(q,k),D(q+1,k+1)),
                    scale(multiply(D(q,k+1),D(q+1,k)),-1))
        observations.append(scale(minor,Fraction(5)**(13-2*k)))
    out = []
    while observations:
        out.append(expand(sum(Rational(z)*theta**i
                              for i,z in enumerate(observations[0]))))
        observations = [add(observations[i+1],scale(observations[i],-1))
                        for i in range(len(observations)-1)]
    return out



def bernstein_coefficients(polynomial, left, right):
    """Exact rational Bernstein coefficients on a closed rational interval."""
    left, right = Rational(left), Rational(right)
    assert left < right
    shifted = Poly(polynomial, theta, domain='QQ').shift(left)
    n = shifted.degree()
    powers = [v * (right-left)**i for i, v in
              enumerate(reversed(shifted.all_coeffs()))]
    return [sum(powers[i] * Rational(binomial(k, i), binomial(n, i))
                for i in range(k+1)) for k in range(n+1)]


def verify(independent=False):
    """Prove the finite corank-7 PF2 iff threshold with all exact arithmetic.

    Explicit intervals and signs produce a complete continuum certificate;
    no numerical mesh or infinite-index extraction theorem is assumed.
    """
    import hashlib
    c = row_coefficients()
    assert len(c) == 15
    c0 = (-270978252800000000000*theta**5
          +2346215014400000000000*theta**4
          -14029641728000000000000*theta**3
          +47505817753600000000000*theta**2
          -71512032089600000000000*theta
          +36053799376000000000000)
    assert expand(c[0]-c0) == 0
    assert expand(c[-1]-429*(30-16*theta)**14) == 0
    T = [expand(c[j]**2-c[j-1]*c[j+1]) for j in range(1,14)]
    a,b = Rational(126,125),Rational(1009,1000)
    groups=[]
    def cert(name, sequence, left, right):
        n=0
        for polynomial in sequence:
            beta=bernstein_coefficients(polynomial,left,right)
            assert all(z>0 for z in beta), (name,left,right)
            n+=len(beta)
        groups.append({'group':name,'polynomials':len(sequence),
            'interval':[str(left),str(right)],
            'strict_positive_Bernstein_coefficients':n})
    # Strict positivity/log-concavity on -1 < theta < rho7.
    cert('c1..c14',c[1:],-1,b)
    cert('T1..T13',T,-1,b)
    cert('c0_before_root',[c[0]],-1,a)
    cert('minus_c0_derivative',[-diff(c[0],theta)],a,b)
    assert c[0].subs(theta,a)>0>c[0].subs(theta,b)
    # Any theta>rho7 has at least one negative coefficient.
    cert('minus_c0_after_root_to_2',[-c[0]],b,2)
    cert('minus_c5_2_to_23_over_10',[-c[5]],2,Rational(23,10))
    cert('minus_c7_23_over_10_to_5_over_2',[-c[7]],Rational(23,10),Rational(5,2))
    cert('minus_c6_5_over_2_to_51_over_20',[-c[6]],Rational(5,2),Rational(51,20))
    cert('minus_c0_51_over_20_to_3',[-c[0]],Rational(51,20),3)
    # A globally valid tail certificate: -c0(51/20+y) has six positive
    # ordinary monomial coefficients, hence -c0(theta)>0 for theta>=51/20.
    tail=list(reversed(Poly(-c[0],theta,domain='QQ')
             .shift(Rational(51,20)).all_coeffs()))
    assert len(tail)==6 and all(t>0 for t in tail)
    # A separator: at theta=1 r7 remains PF2; r6 c0(1)<0, from R374.
    assert all(p.subs(theta,1)>0 for p in c)
    assert all(p.subs(theta,1)>0 for p in T)
    assert c[0].subs(theta,1)==93180073600000000000
    assert c[0].subs(theta,Rational(11,10))<0
    independent_points=[]
    if independent:
        sys.path.insert(0,str(HERE.parent/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
        from R369_check import compute_rows
        for input_value in (Rational(-1,2),Rational(0),Rational(1)):
            other,_=compute_rows(input_value,7)
            assert len(other[7])==15
            assert all(other[7][j]==c[j].subs(theta,input_value) for j in range(15))
            independent_points.append(str(input_value))
    coeff_strings=[[str(v) for v in Poly(p,theta,domain='ZZ').all_coeffs()]
                   for p in c]
    serialized=json.dumps(coeff_strings,separators=(',',':'))
    result={
        'schema':'EM_R375_SIGNED_K3_CORANK7_EXACT_PHASE_V1',
        'status':'R375_EXACT_PASS',
        'domain':'real theta>-1',
        'model':'original R346 signed 12-term BRC K/J, only K3[t^2]=-8(1+theta)',
        'raw_D_corank':7,
        'finite_newton_coefficient_count':15,
        'ordinary_Turan_defect_count':13,
        'theorem':'finite r=7 Newton sequence PF2 iff -1<theta<=rho7',
        'rho7':'unique zero of c0 in (126/125,1009/1000)',
        'c0_descending':coeff_strings[0],
        'c14_identity':'429*(30-16*theta)^14',
        'r7_threshold_vs_r6':'rho7>1>sigma6 (sigma6 in (901/1000,902/1000)); first seven common PF2 remains (-1,sigma6]',
        'Bernstein_groups':groups,
        'Bernstein_polynomial_count':sum(g['polynomials'] for g in groups),
        'positive_Bernstein_coefficient_count':sum(g['strict_positive_Bernstein_coefficients'] for g in groups),
        'tail_minus_c0_shift_51_over_20_ascending':[str(t) for t in tail],
        'all_15_c_polynomial_descending':coeff_strings,
        'all_15_c_polynomials_sha256':hashlib.sha256(serialized.encode()).hexdigest(),
        'independent_route_exact_rational_parameters':independent_points,
        'independent_route_exact_coefficient_equalities':15*len(independent_points),
        'input_KJ_source':'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_verify.py',
        'independent_source':'research_notes/r369_signed_k3_branch_top_catalan_20261029_emr3/R369_check.py',
        'arithmetic':'exact integers and rational Bernstein coefficients, no floating-point sign decisions',
        'R348_R363_all_index_extraction_assumed':False,
        'native_X6_mapping_claimed':False,
        'driver_review_or_admission_claimed':False
    }
    return result


if __name__=='__main__':
    evidence=verify('--independent' in sys.argv)
    dest=HERE/'R375_EVIDENCE.json'
    dest.write_text(json.dumps(evidence,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('R375_EXACT_PASS',json.dumps({
        'rho7':evidence['rho7'],
        'Bernstein_polynomials':evidence['Bernstein_polynomial_count'],
        'positive_Bernstein_coefficients':evidence['positive_Bernstein_coefficient_count'],
        'independent_exact_equalities':evidence['independent_route_exact_coefficient_equalities'],
        'all_15_poly_sha256':evidence['all_15_c_polynomials_sha256']
    },ensure_ascii=False))
