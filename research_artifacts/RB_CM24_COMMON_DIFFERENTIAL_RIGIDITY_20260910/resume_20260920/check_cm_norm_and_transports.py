"""Exact finite certificate for the common-differential rigidity proof.

This verifies integer algebra/norm bounds and universal V4/twist formulae.
The geometric common-kernel/duality argument is a separate paper proof.
No old RB map checker, six-block checker or 1980-system search is executed.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
RING_PATH=ROOT/'research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/check_squareclass_rr.py'
RING_SHA='32282b30357638b5f0a2b709a0c917b29711b43a4d7f407a113bfb6502ddf269'

def build():
    assert hashlib.sha256(RING_PATH.read_bytes()).hexdigest()==RING_SHA
    spec=importlib.util.spec_from_file_location('existing_rb_ring',RING_PATH)
    ring=importlib.util.module_from_spec(spec);spec.loader.exec_module(ring)
    add,mul,scale,constant=ring.add,ring.multiply,ring.scale,ring.constant
    beta,lam,eta,beta_pull,C0,twist_d,x,t,k,s=[ring.variable(j) for j in range(10)]
    def sub(p,q):return add(p,scale(q,-1))
    def power(p,n):return mul(*([p]*n))
    checks=[];tampers=[]
    def equal(name,left,right):
        residual=sub(left,right)
        assert not residual,(name,ring.polynomial_rows(residual))
        checks.append({'name':name,'residual':[]})
    def nonzero(name,residual):
        assert residual,name
        tampers.append({'name':name,'detected':True,'residual':ring.polynomial_rows(residual)})

    cm=json.loads((HERE/'cm_class_polynomial.json').read_bytes())
    h=cm['coefficients_constant_first']
    assert cm['input_discriminant']==-24 and h==[14670139392,-4834944,1]
    j=add(constant(2417472),scale(beta,1707264))
    hj=add(power(j,2),scale(j,h[1]),constant(h[0]))
    equal('H_minus24_at_accepted_j',hj,scale(add(power(beta,2),constant(-2)),1707264*1707264))
    nonzero('changed_H_constant_is_detected',sub(add(hj,constant(1)),scale(add(power(beta,2),constant(-2)),1707264*1707264)))

    sys.path.insert(0,str(ROOT/'src'))
    from enterprise_math.exact_arithmetic import DivisionExpr,RootExpr,brc_integer_value,brc_evaluate_root
    traces=[]
    bound_squared,div_trace=brc_integer_value(DivisionExpr(36,6));traces.append(asdict(div_trace))
    bound_trace=brc_evaluate_root(RootExpr(bound_squared,2));traces.append(asdict(bound_trace))
    assert bound_trace.root_index==2
    square_cases=[];solutions=[]
    for b_abs in range(bound_trace.root_index+1):
        remainder=36-6*b_abs*b_abs
        rt=brc_evaluate_root(RootExpr(remainder,2));traces.append(asdict(rt))
        square_cases.append({'absolute_b':b_abs,'required_a_squared':remainder,'root_trace':asdict(rt)})
        if rt.exact:
            for a_sign in [-1,1]:
                if b_abs==0:solutions.append([a_sign*rt.root_index,0])
                else:
                    for b_sign in [-1,1]:solutions.append([a_sign*rt.root_index,b_sign*b_abs])
    assert solutions==[[-6,0],[6,0]]
    scalar_abs,scalar_trace=brc_integer_value(DivisionExpr(6,6));traces.append(asdict(scalar_trace));assert scalar_abs==1
    # Dropping integrality gives a genuine rational norm-36 counterexample.
    assert (-30)*(-30)+6*12*12==36*7*7
    rational_bad=[]
    for numerator in [30,12]:
        from enterprise_math.exact_arithmetic import brc_evaluate_division
        trace=brc_evaluate_division(DivisionExpr(numerator,7));rational_bad.append(asdict(trace));assert trace.remainder!=0
    # Changing the CM order to Gaussian integers creates additional norm-36 elements.
    assert 0*0+1*6*6==36 and 0*0+6*6*6!=36
    norm_tampers=[{'name':'integrality_cannot_be_removed','numerator_pair':[-30,12],'denominator':7,'norm_numerator':1764,'norm_denominator':49,'nonintegral_traces':rational_bad},
                  {'name':'CM_field_cannot_be_omitted','wrong_gaussian_element':[0,6],'wrong_order_norm':36,'correct_order_norm':216},
                  {'name':'relative_scalar_cannot_be_fixed_to_one','admissible_map':'[-1] composed with f0','pullback_scalar':-1,'difference_from_claimed_plus_phi':'-2 phi, nonzero by accepted phi input'}]

    # Universal target-coordinate identities. The R slot is now the formal x.
    one=constant(1);P=mul(x,sub(x,one),sub(x,lam))
    transforms=[('identity',x,one,one),
                ('T0',lam,x,scale(lam,-1)),
                ('T1',sub(x,lam),sub(x,one),sub(lam,one)),
                ('Tlambda',mul(lam,sub(x,one)),sub(x,lam),mul(lam,sub(one,lam)))]
    transport_rows=[]
    for name,N,D,J in transforms:
        derivative_numerator=sub(mul(ring.twice_delta(N),D),mul(N,ring.twice_delta(D)))
        equal(name+'_derivative',derivative_numerator,scale(mul(t,J),2))
        equal(name+'_same_Legendre_twist',mul(N,sub(N,D),sub(N,mul(lam,D)),D),mul(power(J,2),P))
        transport_rows.append({'name':name,'N':ring.polynomial_rows(N),'D':ring.polynomial_rows(D),'differential_and_Y_numerator_J':ring.polynomial_rows(J)})
        nonzero(name+'_wrong_Y_sign_changes_unsquared_differential',scale(J,2))
    # Inverse twist transport E0->Ed: y=eta*Y, eta^2*C0=d.
    Y=beta;Fpoly=lam
    equal('inverse_twist_transport',sub(power(mul(eta,Y),2),mul(twist_d,Fpoly)),
          add(mul(power(eta,2),sub(power(Y,2),mul(C0,Fpoly))),mul(sub(mul(power(eta,2),C0),twist_d),Fpoly)))
    nonzero('reciprocal_differential_multiplier_tamper',mul(beta_pull,sub(power(eta,2),one)))

    possible_indices=[]
    for degree_g in [1,2,3,6]:
        degree_v,trace=brc_integer_value(DivisionExpr(6,degree_g));traces.append(asdict(trace))
        possible_indices.append({'curve_to_common_factor_degree':degree_g,'finite_isogeny_degree':degree_v,'actual_value_determined':False})
    return {'schema':'RB_COMMON_DIFFERENTIAL_EXACT_CERTIFICATE_V1','status':'PASS_EXACT_FINITE_CHECKS',
            'scope':'Integer/transport checks only; PROOF.md establishes all geometric and CM-identification hypotheses',
            'ring_source_sha256':RING_SHA,'CM_polynomial':h,'accepted_j_coefficients':[2417472,1707264],
            'checks':checks,'tamper_checks':tampers,'norm_gate_tests':norm_tampers,
            'norm_equation':'a^2+6*b^2=36 with a,b integers','complete_norm_solutions':solutions,
            'square_cases':square_cases,'relative_scalars':[-1,1],'brc_traces':traces,
            'possible_uncomputed_finite_factors':possible_indices,'transports':transport_rows,
            'field_domain':'geometric rigidity over algebraic closure of L; arithmetic formulas over declared K containing L',
            'no_primitive_f0_assumption':True,'old_RB_checker_mains_executed':False,'old_1980_enumeration_executed':False,
            'geometric_proof_is_not_replaced_by_this_certificate':True}

def main():
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args()
    result=build();data=(json.dumps(result,indent=2,sort_keys=True)+'\n').encode()
    target=HERE/'exact_certificate.json'
    if args.write:target.write_bytes(data)
    else:assert target.read_bytes()==data,'Frozen certificate differs'
    print(json.dumps({'status':result['status'],'polynomial_checks':len(result['checks']),
                      'tamper_checks':len(result['tamper_checks']),'norm_gate_tests':len(result['norm_gate_tests']),
                      'norm_solutions':result['complete_norm_solutions'],'sha256':hashlib.sha256(data).hexdigest()}))

if __name__=='__main__':main()
