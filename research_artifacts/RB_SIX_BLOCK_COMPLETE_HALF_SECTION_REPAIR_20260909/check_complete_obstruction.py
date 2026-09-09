"""Verify the complete-pencil fixed-k obstruction with the existing integer ring.

No previous checker main, assignment enumeration, numerical root, or approximate
field evaluation is executed. The imported ring algorithms are unchanged. Its
variable alphabet is extended by formal lambda and u, with all old indices fixed.
There is no added u-reduction algorithm: u^2=2 is handled by explicit polynomial
ideal certificates. Paper proofs justify pole orders and universal necessity.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RING_PATH = ROOT / 'research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/check_squareclass_rr.py'
RING_SHA256 = '32282b30357638b5f0a2b709a0c917b29711b43a4d7f407a113bfb6502ddf269'


def encoded(value):
    return (json.dumps(value, sort_keys=True, indent=2) + '\n').encode('utf-8')


def build_certificate():
    assert hashlib.sha256(RING_PATH.read_bytes()).hexdigest() == RING_SHA256
    spec = importlib.util.spec_from_file_location('rb_existing_integer_ring', RING_PATH)
    ring = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ring)
    assert ring.NAMES == ('a','b','c','d','e','f','R','t','k','s')
    ring.NAMES = ring.NAMES + ('lambda','u')
    ring.ZERO_MONOMIAL = (0,) * len(ring.NAMES)
    add, mul, sc, const = ring.add, ring.multiply, ring.scale, ring.constant
    a,b,c,d,e,f,R,t,k,s,lam,u = [ring.variable(j) for j in range(len(ring.NAMES))]

    def sub(left, right):
        return add(left, sc(right, -1))

    def pow_(value, exponent):
        return mul(*([value] * exponent))

    def eq(name, left, right):
        residual = sub(left, right)
        if residual:
            raise AssertionError(name + ': ' + str(ring.polynomial_rows(residual)))
        checks.append({'name': name, 'residual': []})

    def leading(poly):
        weight = max(2*m[6] + 3*m[7] for m in poly)
        return weight, {m:v for m,v in poly.items() if 2*m[6]+3*m[7] == weight}

    def coeff_R(poly, exponent):
        out = {}
        for monomial, value in poly.items():
            if monomial[6] == exponent:
                row = list(monomial)
                row[6] = 0
                out[tuple(row)] = value
        return out

    def reject(name, residual):
        assert residual, name + ': tamper was not detected'
        tampers.append({'name': name, 'detected': True,
                        'nonzero_residual': ring.polynomial_rows(residual)})

    checks, tampers = [], []
    P = add(pow_(R,3), sc(R,-3))
    F = mul(add(R,const(2)),t)
    G = add(mul(a,pow_(R,3)),mul(b,pow_(R,2)),mul(c,R),d,mul(add(mul(e,R),f),t))
    G1, Gl = sub(G,F), sub(G,mul(lam,F))
    D = ring.twice_delta
    N = sub(mul(F,D(G)),mul(G,D(F)))
    raw_t_squared = list(ring.ZERO_MONOMIAL)
    raw_t_squared[7] = 2
    eq('integer_derivation_preserves_curve',D(sub({tuple(raw_t_squared):1},P)),const(0))
    eq('F_integer_derivative',D(F),add(sc(P,2),mul(add(R,const(2)),sc(add(pow_(R,2),const(-1)),3))))
    assert leading(G)[0] == 6 and leading(N)[0] == 12
    eq('G_exact_pole6_coefficient',leading(G)[1],mul(a,pow_(R,3)))
    eq('N_exact_pole12_coefficient',leading(N)[1],mul(a,pow_(R,6)))
    eq('ODE_left_top_pole',leading(pow_(N,2))[1],mul(pow_(a,2),pow_(R,12)))
    right_base = mul(pow_(add(t,k),2),G,G1,Gl)
    eq('ODE_right_top_pole_before_4K',leading(right_base)[1],mul(pow_(a,3),pow_(R,12)))

    # Full half-section coefficient vectors, including the compensated finite pole.
    q0 = add(a,mul(b,R),mul(c,t))
    square = mul(d,pow_(q0,2))
    square_expanded = mul(d,add(mul(pow_(c,2),pow_(R,3)),mul(pow_(b,2),pow_(R,2)),
        mul(add(sc(mul(a,b),2),sc(pow_(c,2),-3)),R),pow_(a,2),
        mul(add(sc(mul(b,c,R),2),sc(mul(a,c),2)),t)))
    eq('trivial_sector_complete_coefficients',square,square_expanded)
    sector_names = ['T0','Tplus','Tminus']
    for name,r in zip(sector_names,[const(0),s,sc(s,-1)]):
        gamma = sub(R,r)
        Qr = add(pow_(R,2),mul(r,R),pow_(r,2),const(-3))
        linear = add(a,mul(b,R))
        sector = mul(d,add(mul(gamma,pow_(linear,2)),sc(mul(c,linear,t),2),mul(pow_(c,2),Qr)))
        numerator = add(mul(gamma,linear),mul(c,t))
        eq(name+'_quotient_factor',mul(gamma,Qr),P)
        eq(name+'_compensated_half_section',mul(gamma,sector),mul(d,pow_(numerator,2)))
        eq(name+'_exact_pole6_coefficient',leading(sector)[1],mul(d,pow_(b,2),pow_(R,3)))
        altered = sub(sector,mul(d,pow_(c,2),Qr))
        reject(name+'_omitted_compensating_term',sub(mul(gamma,altered),mul(d,pow_(numerator,2))))
    eq('three_nontrivial_squareclass_product',mul(R,sub(R,s),add(R,s)),pow_(t,2))

    # Restrictions forced by the full squared ODE at the three finite 2-torsion points.
    Pprime = sc(add(pow_(R,2),const(-1)),3)
    H = add(sc(pow_(R,2),72),sc(R,144),const(36))
    quotient = add(sc(pow_(R,3),9),sc(pow_(R,2),36),sc(R,45),const(36))
    eq('three_torsion_value_remainder',sub(pow_(mul(add(R,const(2)),Pprime),2),H),mul(P,quotient))
    reject('torsion_remainder_constant_36_to_37',sub(sub(pow_(mul(add(R,const(2)),Pprime),2),add(H,const(1))),mul(P,quotient)))
    q = pow_(k,2)
    Lb = add(mul(q,b),sc(a,-72))
    Lc = add(mul(q,c),mul(add(sc(q,3),const(-144)),a))
    Ld = add(mul(q,d),sc(a,-36))
    atQ = ring.restrict_to_critical_divisor(N)
    C2 = coeff_R(atQ,2)
    expected_C2 = add(mul(add(sc(q,6),const(-18)),a),
                      sc(mul(add(q,const(12)),b),-1),sc(c,-6),sc(d,-6))
    eq('critical_remainder_R2_coefficient',C2,expected_C2)
    psi = add(pow_(k,4),sc(q,-12),const(-324))
    combination = add(mul(q,C2),mul(add(q,const(12)),Lb),sc(Lc,6),sc(Ld,6))
    eq('complete_pencil_ODE_integer_elimination',combination,sc(mul(a,psi),6))
    reject('critical_R2_d_sign_reversed',sub(add(mul(q,add(C2,sc(d,12))),mul(add(q,const(12)),Lb),sc(Lc,6),sc(Ld,6)),sc(mul(a,psi),6)))

    # Natural integer coefficient normalization uses the existing BRC facade.
    sys.path.insert(0,str(ROOT/'src'))
    from enterprise_math.exact_arithmetic import DivisionExpr, brc_integer_value
    traces = []
    normalized = []
    for numerator in [264,144,120,240]:
        value,trace = brc_integer_value(DivisionExpr(numerator,24))
        normalized.append(value)
        traces.append(asdict(trace))
    assert normalized == [11,6,5,10]
    c0,cu,cs,cus = normalized
    h = add(const(c0),sc(u,-cu),sc(s,cs),sc(mul(u,s),-cus))
    q_fixed = add(sc(u,12),sc(s,-10))
    urel = add(pow_(u,2),const(-2))
    eq('frozen_k_squared_to_obstruction',sub(add(pow_(q_fixed,2),sc(q_fixed,-12),const(-324)),sc(h,24)),sc(urel,144))
    conjugates = [add(const(c0),sc(u,-cu*su),sc(s,cs*ss),sc(mul(u,s),-cus*su*ss))
                  for su,ss in [(1,1),(-1,1),(1,-1),(-1,-1)]]
    norm = mul(*conjugates)
    cofactor = add(sc(pow_(u,2),69696),const(86880))
    eq('obstruction_conjugate_product_nonzero',sub(norm,const(175876)),mul(urel,cofactor))
    eq('unreduced_norm_scaling',const(24*24*24*24*175876),const(58351435776))
    reject('false_zero_obstruction_norm',sub(norm,mul(urel,cofactor)))
    eq('frozen_k_is_nonzero',add(mul(q_fixed,add(sc(u,12),sc(s,10))),const(12)),sc(urel,144))
    discr = add(sc(mul(u,s),240),const(-584))
    eq('critical_cubic_discriminant_reduction',sub(add(const(4),sc(pow_(q_fixed,2),-1)),discr),sc(urel,-144))
    discr_conj = add(sc(mul(u,s),-240),const(-584))
    eq('critical_cubic_has_three_distinct_roots',add(mul(discr,discr_conj),const(4544)),sc(urel,-172800))

    problem = json.loads((HERE/'problem.json').read_bytes())
    assert hashlib.sha256((HERE/'frozen_inputs/raw_freeze_reduction.json').read_bytes()).hexdigest() == '0740e43ae09bc28fcb2facada23ea5e9fdfa535829e547eed27d2128dd6e8207'
    source = json.loads((HERE/'frozen_inputs/raw_freeze_reduction.json').read_bytes())['payload']
    assert problem['k'] == source['frozen_inputs']['k'] == '-i*3^(1/4)*(sqrt(6)-2)'
    assert problem['lambda'] == source['frozen_inputs']['lambda'] == '35+24*sqrt(2)-20*sqrt(3)-14*sqrt(6)'
    assert problem['integer_derivation_squared_factor'] == 4
    assert problem['k_squared_coefficients'] == {'sqrt2':12,'sqrt3':-10}
    return {
        'schema':'RB_SIX_BLOCK_COMPLETE_FIXED_K_INTEGER_CERTIFICATE_V1',
        'status':'PASS_EXACT_INTEGER_IDENTITIES',
        'scope':'Paper proof converts these universal identities and nonzero conditions to a complete fixed-k six-block exclusion; no Driver acceptance is asserted.',
        'ring_source_sha256':RING_SHA256,
        'ring_variables':list(ring.NAMES),
        'ring_extension':'Formal lambda and u only; unchanged algorithms; u^2=2 by explicit ideal certificates.',
        'problem_sha256':hashlib.sha256((HERE/'problem.json').read_bytes()).hexdigest(),
        'checks':checks,'tamper_checks':tampers,'brc_division_traces':traces,
        'critical_remainder':ring.polynomial_rows(atQ),
        'critical_R2_coefficient':ring.polynomial_rows(C2),
        'forced_condition':'k^4-12*k^2-324=0',
        'frozen_condition':'24*(11-6*sqrt2+5*sqrt3-10*sqrt6)',
        'reduced_obstruction_norm':175876,
        'unreduced_obstruction_norm':58351435776,
        'critical_discriminant_product':-4544,
        'all_four_half_section_sectors_included':True,
        'arithmetic_constants_retained':True,
        'proof_uses_larger_complete_L6O_space':True,
        'previous_180_360_assignment_enumeration_executed':False,
        'sympy_required_for_this_checker':False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    args = parser.parse_args()
    result = build_certificate()
    data = encoded(result)
    output = HERE/'integer-certificate.json'
    if args.write:
        output.write_bytes(data)
    else:
        assert output.read_bytes() == data, 'Frozen certificate differs from independently regenerated identities'
    print(json.dumps({'status':result['status'],'checks':len(result['checks']),
                      'tamper_checks':len(result['tamper_checks']),
                      'certificate_sha256':hashlib.sha256(data).hexdigest()},sort_keys=True))


if __name__ == '__main__':
    main()
