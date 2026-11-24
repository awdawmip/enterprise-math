#!/usr/bin/env python3
"""Outward interval checks of the actual single-thickness first-order correction."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sqrt_interval(m, value):
    lo = isqrt(max(0, value[0])*m.S)
    z = max(0, value[1])*m.S
    hi = isqrt(z)
    if hi*hi < z:
        hi += 1
    return lo, hi


def positive_division(m, numerator, denominator):
    assert numerator[0] >= 0 and denominator[0] > 0
    return numerator[0]*m.S//denominator[1], m.ceildiv(numerator[1]*m.S,denominator[0])


def run_case(m, helper, B):
    factors = [[] for _ in range(B+1)]
    for p in range(2,B+1):
        if not factors[p]:
            for n in range(p,B+1,p):
                factors[n].append(p)
    primes = [p for p in range(2,B+1) if factors[p] == [p]]
    logs = {p:m.log_int(p) for p in primes}
    a = F(1,B)
    one_minus = {p:m.sub(m.ONE, helper.exp_negative_small(m,m.qmul(logs[p],a))) for p in primes}
    lam = [m.ZERO]*(B+1)
    b = [m.ZERO]*(B+1)
    errors = [m.ZERO]*(B+1)
    remainder = [m.ZERO]*(B+1)
    signs = {'prime_power_positive':0,'two_distinct_negative':0,'three_or_more_positive':0}
    for n in range(2,B+1):
        ps = factors[n]
        Lrad = m.total(logs[p] for p in ps)
        if len(ps) == 1:
            lam[n] = logs[ps[0]]
            b[n] = m.qmul(m.square(logs[ps[0]]),-1,2)
        elif len(ps) == 2:
            b[n] = m.mul(logs[ps[0]],logs[ps[1]])
        value = m.ONE
        for p in ps:
            value = m.mul(value,one_minus[p])
        source = m.qmul(value,B)
        errors[n] = m.sub(source,lam[n])
        remainder[n] = m.sub(errors[n],m.qmul(b[n],a))
        radius = m.qmul(m.mul(m.square(Lrad),Lrad),1,6*B*B)[1]
        assert -radius <= remainder[n][0] <= remainder[n][1] <= radius
        if len(ps) == 2:
            assert remainder[n][1] < 0
            signs['two_distinct_negative'] += 1
        else:
            assert remainder[n][0] > 0
            signs['prime_power_positive' if len(ps)==1 else 'three_or_more_positive'] += 1
    # Independent Dirichlet-convolution seam for b on every integer.
    support = [n for n in range(2,B+1) if len(factors[n])==1]
    convolution = [m.ZERO]*(B+1)
    for d in support:
        for e in support:
            if d*e > B:
                break
            convolution[d*e] = m.add(convolution[d*e],m.mul(lam[d],lam[e]))
    for n in range(1,B+1):
        if lam[n] != m.ZERO:
            p = factors[n][0]
            exponent = 0
            k = n
            while k > 1:
                k //= p
                exponent += 1
            lambda_log_n = m.qmul(m.square(logs[p]),exponent)
        else:
            lambda_log_n = m.ZERO
        formula = m.qmul(m.sub(convolution[n],lambda_log_n),1,2)
        assert m.overlap(formula,b[n])
    L = m.log_int(B)
    S_B = m.total(m.qmul(lam[n],1,n) for n in support)
    exponent_upper = helper.exp_positive_small(m,m.qmul(S_B,a))
    cumulative_error = weighted_error = m.ZERO
    cumulative_b = weighted_b = m.ZERO
    cumulative_r = weighted_r = absolute_weighted_r = m.ZERO
    S_y = m.ZERO
    A = max(2,isqrt(B))
    energy = corrected_energy = m.ZERO
    negative_road_count = 0
    endpoint = None
    for y in range(1,B+1):
        cumulative_error = m.add(cumulative_error,errors[y])
        weighted_error = m.add(weighted_error,m.qmul(errors[y],1,y))
        cumulative_b = m.add(cumulative_b,b[y])
        weighted_b = m.add(weighted_b,m.qmul(b[y],1,y))
        cumulative_r = m.add(cumulative_r,remainder[y])
        weighted_r = m.add(weighted_r,m.qmul(remainder[y],1,y))
        absolute_r = m.neg(remainder[y]) if y>=2 and len(factors[y])==2 else remainder[y]
        absolute_weighted_r = m.add(absolute_weighted_r,m.qmul(absolute_r,1,y))
        S_y = m.add(S_y,m.qmul(lam[y],1,y))
        difference = m.sub(m.qmul(weighted_error,y),cumulative_error)
        Tb = m.sub(m.qmul(weighted_b,y),cumulative_b)
        corrected = m.sub(m.qmul(weighted_r,y),cumulative_r)
        assert m.overlap(corrected,m.sub(difference,m.qmul(Tb,a)))
        # Formula (9), enlarged only by log(y)<=log(B), S(y)<=S(B) in exp.
        average = m.qmul(m.add(m.add(
            m.qmul(m.mul(m.square(L),S_y),1,6),
            m.qmul(m.mul(L,m.square(S_y)),1,4)),
            m.qmul(m.mul(m.mul(m.square(S_y),S_y),exponent_upper),1,6)),1,B*B)
        assert absolute_weighted_r[1] <= average[1]
        point_bound = m.qmul(average,y)[1]
        assert -point_bound <= corrected[0] <= corrected[1] <= point_bound
        if y >= A:
            energy = m.add(energy,m.qmul(m.square(difference),1,y*y))
            corrected_energy = m.add(corrected_energy,m.qmul(m.square(corrected),1,y*y))
            negative_road_count += difference[1] < 0
        if y == B:
            endpoint = {'difference':m.record(difference),'first_order_Tb_over_B':m.record(m.qmul(Tb,a)),
                        'corrected_difference':m.record(corrected),'average_radius_upper':m.record((point_bound,point_bound)),
                        'summatory_b':m.record(cumulative_b)}
    norm = sqrt_interval(m,energy)
    corrected_norm = sqrt_interval(m,corrected_energy)
    normalized = positive_division(m,m.mul(norm,sqrt_interval(m,m.rat(B))),L)
    return {'B':B,'A':A,'a_exact':str(a),'prime_count':len(primes),
            'source_remainder_checks':B-1,'remainder_sign_counts':signs,
            'b_convolution_checks':B,'prefix_identity_checks':B,
            'prefix_average_source_checks':B,'prefix_average_road_checks':B,
            'negative_road_points_in_window':negative_road_count,'window_point_count':B-A+1,
            'matching_root_energy':m.record(norm),'corrected_root_energy':m.record(corrected_norm),
            'matching_norm_times_sqrtB_over_logB':m.record(normalized),'endpoint':endpoint}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True,help='riemann_matching_isotonic_anchors_20261124 package')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('single_thickness_bias_certificate.json'))
    args=parser.parse_args()
    harmonic=args.previous/'prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123/dependencies/certify_fast_harmonic_energy.py'
    helper_path=args.previous/'matching/verify_actual_matching.py'
    m=module_at('sharp_bias_harmonic',harmonic)
    helper=module_at('sharp_bias_old_helper',helper_path)
    rows=[run_case(m,helper,B) for B in (256,1024,4096,16384)]
    result={'schema':'EM_SINGLE_THICKNESS_FIRST_ORDER_V1','status':'PASS',
            'arithmetic':'80-digit outward integer intervals; exact rational parameters; certified logarithms and Taylor100/101 exponentials',
            'scope':'Finite actual-source and complete-prefix certificates. Asymptotic constants/rates are proved analytically, not inferred from these rows.',
            'dependencies':[{'path':str(p.relative_to(args.previous)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (harmonic,helper_path)],
            'cases':rows,
            'total_source_remainder_checks':sum(r['source_remainder_checks'] for r in rows),
            'total_b_convolution_checks':sum(r['b_convolution_checks'] for r in rows),
            'total_prefix_identity_checks':sum(r['prefix_identity_checks'] for r in rows),
            'total_prefix_average_checks':sum(2*r['prefix_average_road_checks'] for r in rows)}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','source_checks':result['total_source_remainder_checks'],
                     'cases':[{'B':r['B'],'root':r['matching_root_energy']['upper'],
                               'corrected_root':r['corrected_root_energy']['upper'],
                               'normalized':r['matching_norm_times_sqrtB_over_logB']['upper'],
                               'endpoint_difference':r['endpoint']['difference']['lower'],
                               'negative_points':r['negative_road_points_in_window']} for r in rows]},ensure_ascii=False))


if __name__=='__main__':
    main()
