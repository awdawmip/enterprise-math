#!/usr/bin/env python3
"""Strict calibration of the original eleven-node family with two extra nodes.

All decisions use exact fractions or 80-place outward integer intervals.
The exact calibrated coefficients are computable real numbers defined by a
two-by-two system; a separate dyadic-coefficient rational family is certified.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial, isqrt
import argparse
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode=True


def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def weights(nodes):
    out=[]
    for a in nodes:
        value=F(1)
        for b in nodes:
            if b!=a:value*=b/(b-a)
        out.append(value)
    return out


def regular_constants(m,em):
    """Enclose gamma and gamma_1 by the same differentiated EM integral."""
    N=64;order=24;s=F(1);logn=m.log_int(N)
    gamma=m.sub(m.rat(sum((F(1,n) for n in range(1,N)),F(0))),logn)
    derivative=m.qmul(m.square(logn),F(1,2))
    for n in range(1,N):derivative=m.sub(derivative,m.qmul(m.log_int(n),F(1,n)))
    gamma=m.add(gamma,m.rat(F(1,2*N)))
    derivative=m.sub(derivative,m.qmul(logn,F(1,2*N)))
    bernoulli=m.bernoulli(2*order);rising=F(1);harmonic=F(0)
    for k in range(1,2*order):
        rising*=s+k-1;harmonic+=1/(s+k-1)
        if k%2:
            j=(k+1)//2
            term=m.rat(bernoulli[2*j]*rising/F(factorial(2*j)*N**(2*j)))
            gamma=m.add(gamma,term)
            derivative=m.add(derivative,m.mul(term,m.sub(m.rat(harmonic),logn)))
    remainder=max(abs(term[0]),abs(term[1]))
    full_harmonic=harmonic+F(1,2*order)
    factor=m.add(logn,m.rat(full_harmonic+F(1,2*order)))
    derivative_remainder=m.mul((remainder,remainder),factor)[1]
    gamma=(gamma[0]-remainder,gamma[1]+remainder)
    gamma1=m.neg((derivative[0]-derivative_remainder,derivative[1]+derivative_remainder))
    return gamma,gamma1,{'N':N,'order':order,'gamma_remainder_upper':m.record((remainder,remainder)),
                        'gamma1_remainder_upper':m.record((derivative_remainder,derivative_remainder))}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True,help='riemann_signed_green_thickness_phase_20261124 package')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('calibrated_family_certificate.json'))
    args=parser.parse_args();previous=args.previous
    older=previous/'prior/riemann_native_residual_growth_20261124/prior/riemann_matching_isotonic_anchors_20261124'
    early=older/'prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123'
    paths=[previous/'fixed_family/certify_fixed_family_density.py',older/'matching/verify_actual_matching.py',
           early/'dependencies/certify_fast_harmonic_energy.py',early/'prefix_compute/fixed_matched_family.json']
    em=module_at('calibration_zeta_em',paths[0]);helper=module_at('calibration_exp',paths[1]);m=module_at('calibration_intervals',paths[2])
    data=json.loads(paths[3].read_text());old_nodes=list(map(F,data['nodes']));old_weights=list(map(F,data['weights']))
    assert old_weights==weights(old_nodes)
    extra=[F(1,1000),F(1,2000)];nodes=old_nodes+extra
    assert len(set(nodes))==13 and all(0<a<=F(1,2) for a in nodes)
    bases=[weights(nodes[:j])+[F(0)]*(13-j) for j in (11,12,13)]
    moment_checks=0
    for count,base in zip((11,12,13),bases):
        for k in range(count):
            assert sum((w*a**k for w,a in zip(base,nodes)),F(0))==int(k==0)
            moment_checks+=1
    gamma,gamma1,regular_bounds=regular_constants(m,em)
    old_gamma=(m.rat(F(data['gamma']['lower']))[0],m.rat(F(data['gamma']['upper']))[1])
    assert old_gamma[0]<=gamma[0]<=gamma[1]<=old_gamma[1]

    def add(*terms):
        z=m.ZERO
        for term in terms:z=m.add(z,term)
        return z
    def div(a,b):
        if b[1]<0:return m.neg(m.mul(a,em.reciprocal(m,m.neg(b))))
        assert b[0]>0
        return m.mul(a,em.reciprocal(m,b))
    def abs_interval(x):
        if x[0]>=0:return x
        if x[1]<=0:return m.neg(x)
        return 0,max(-x[0],x[1])
    def sum_weighted(base,values):return add(*(m.qmul(value,w) for w,value in zip(base,values)))

    rows=[];densities=[];constants=[]
    for a in nodes:
        z,dz,bounds=em.zeta_em(m,helper,1+a)
        g=em.reciprocal(m,z);gp=m.neg(m.mul(dz,m.square(g)));d=m.qmul(g,1/a)
        c=add(m.ONE,gamma,m.mul(m.sub(gamma,m.ONE),d),m.qmul(m.sub(gp,m.ONE),1/a))
        densities.append(d);constants.append(c)
        rows.append({'a':str(a),'zeta':m.record(z),'zeta_prime':m.record(dz),
                     'mean_density':m.record(d),'road_constant':m.record(c),**bounds})
    density_errors=[m.sub(sum_weighted(base,densities),m.ONE) for base in bases]
    road_constants=[sum_weighted(base,constants) for base in bases]
    e0,e1,e2=density_errors;c0,c1,c2=road_constants
    aa=m.sub(e0,e2);bb=m.sub(e1,e2);cc=m.sub(c0,c2);dd=m.sub(c1,c2)
    determinant=m.sub(m.mul(aa,dd),m.mul(bb,cc))
    assert determinant[1]<0
    lambda0=div(m.sub(m.mul(bb,c2),m.mul(e2,dd)),determinant)
    lambda1=div(m.sub(m.mul(e2,cc),m.mul(aa,c2)),determinant)
    lambda2=m.sub(m.sub(m.ONE,lambda0),lambda1)
    lambdas=[lambda0,lambda1,lambda2]
    assert lambda0[0]>0 and lambda1[1]<0 and lambda2[0]>0
    assert all(x[0]<=0<=x[1] for x in [add(*(m.mul(l,e) for l,e in zip(lambdas,density_errors))),
                                      add(*(m.mul(l,c) for l,c in zip(lambdas,road_constants)))])
    actual_weights=[add(*(m.qmul(l,base[j]) for l,base in zip(lambdas,bases))) for j in range(13)]
    tv=add(*(abs_interval(w) for w in actual_weights));assert tv[1]<5*m.S

    # The determinant at the shrinking-node boundary proves a whole family,
    # rather than extrapolating from this one finite calibrated example.
    first_C=add(gamma,m.qmul(m.square(gamma),2),m.qmul(gamma1,3))
    r_d=m.sub(m.neg(gamma),add(*(m.qmul(m.sub(d,m.ONE),w/a) for d,w,a in zip(densities,old_weights,old_nodes))))
    r_c=m.sub(first_C,add(*(m.qmul(c,w/a) for c,w,a in zip(constants,old_weights,old_nodes))))
    boundary_determinant=m.sub(m.mul(e0,r_c),m.mul(c0,r_d))
    assert boundary_determinant[1]<0

    H=[]
    for count in (11,12,13):
        h=F(1)
        for a in nodes[:count]:h*=a/(1+a)
        H.append(h)
    combined_H=add(*(m.qmul(abs_interval(l),h) for l,h in zip(lambdas,H)))
    ratio=m.qmul(combined_H,1/H[0]);assert ratio[1]<m.rat(F(9,10**7))[0]
    z2,_,_=em.zeta_em(m,helper,F(2))
    inv_e=em.exp_negative(m,helper,m.ONE)
    laplace_constant=m.qmul(m.mul(m.mul(combined_H,z2),inv_e),F(1,2))
    A=1024;B=32768;N=B-A+1
    sqrt_N_lo=isqrt(N*m.S*m.S);sqrt_N=(sqrt_N_lo,sqrt_N_lo+1)
    point_bound=m.qmul(laplace_constant,B*B)
    root_bound=m.qmul(m.mul(laplace_constant,sqrt_N),B)
    assert point_bound[1]<m.rat(F(6,10**9))[0]
    assert root_bound[1]<m.rat(F(33,10**12))[0]

    # Dyadic coefficient approximation keeps all eleven moments EXACTLY.
    precision=100;denominator=2**precision
    rational_lambdas=[]
    errors=[]
    for value in lambdas[:2]:
        rational=F((value[0]+value[1])*denominator//(2*m.S),denominator)
        interval=m.rat(rational)
        assert interval[1]<value[0] and value[1]<m.rat(rational+F(1,denominator))[0]
        error=max(abs(interval[0]-value[1]),abs(interval[1]-value[0]))
        assert error<m.rat(F(1,2**(precision-1)))[0]
        rational_lambdas.append(rational);errors.append((error,error))
    rational_lambdas.append(1-sum(rational_lambdas))
    rational_weights=[sum((l*base[j] for l,base in zip(rational_lambdas,bases)),F(0)) for j in range(13)]
    for k in range(11):assert sum((w*a**k for w,a in zip(rational_weights,nodes)),F(0))==int(k==0)
    rational_density=m.sub(sum_weighted(rational_weights,densities),m.ONE)
    rational_constant=sum_weighted(rational_weights,constants)
    rational_tv=sum(map(abs,rational_weights),F(0))
    rounding_H=add(m.qmul(errors[0],H[0]+H[2]),m.qmul(errors[1],H[1]+H[2]))
    rounding_constant=m.qmul(m.mul(m.mul(rounding_H,z2),inv_e),F(1,2))
    rounding_point=m.qmul(rounding_constant,B*B)
    rounding_root=m.qmul(m.mul(rounding_constant,sqrt_N),B)
    assert abs_interval(rational_density)[1]<m.rat(F(1,10**44))[0]
    assert abs_interval(rational_constant)[1]<m.rat(F(1,10**44))[0]
    assert rounding_point[1]<m.rat(F(1,10**32))[0]
    assert rational_density[0]>0 and rational_constant[1]<0
    assert all(density_errors[i][1]<density_errors[i+1][0] for i in range(2))
    assert all(road_constants[i][0]>road_constants[i+1][1] for i in range(2))
    assert density_errors[2][1]<0 and road_constants[2][0]>0
    ceiling_lambdas=[rational_lambdas[0]+F(1,denominator),rational_lambdas[1]+F(1,denominator)]
    ceiling_lambdas.append(1-sum(ceiling_lambdas))
    ceiling_weights=[sum((l*base[j] for l,base in zip(ceiling_lambdas,bases)),F(0)) for j in range(13)]
    for k in range(11):assert sum((w*a**k for w,a in zip(ceiling_weights,nodes)),F(0))==int(k==0)
    ceiling_density=m.sub(sum_weighted(ceiling_weights,densities),m.ONE)
    ceiling_constant=sum_weighted(ceiling_weights,constants)
    assert ceiling_density[1]<0 and ceiling_constant[0]>0

    # The rational twins have opposite certified infinite-horizon signs.
    exponent=400000;log_threshold=m.qmul(m.LOG_TWO,exponent)
    tail_power=em.exp_negative(m,helper,m.qmul(log_threshold,min(nodes)))
    def eventual_bound(ws,density_error,constant,positive):
        v=sum((w/a for w,a in zip(ws,nodes)),F(0))
        k=sum((abs(w)*(1/(a*a*(1-a))+2/a**3) for w,a in zip(ws,nodes)),F(0))
        tail=add(m.rat(abs(v)/2**exponent),m.qmul(tail_power,k))
        main=add(m.mul(density_error,log_threshold),constant)
        bound=m.sub(main,tail) if positive else m.add(main,tail)
        assert (bound[0]>0) if positive else (bound[1]<0)
        return {'threshold':'2^400000','threshold_exponent_base2':exponent,
                'monotone_bound_at_threshold':m.record(bound),'exact_V_minus1':str(v),'exact_K':str(k),
                'conclusion':('q(y)>0' if positive else 'q(y)<0')+' for every real y>=2^400000'}
    floor_eventual=eventual_bound(rational_weights,rational_density,rational_constant,True)
    ceiling_eventual=eventual_bound(ceiling_weights,ceiling_density,ceiling_constant,False)
    twins_H=F(1,denominator)*(H[0]+H[1]+2*H[2])
    twins_constant=m.qmul(m.mul(m.qmul(z2,twins_H),inv_e),F(1,2))
    twins_point=m.qmul(twins_constant,B*B)
    twins_root=m.qmul(m.mul(twins_constant,sqrt_N),B)
    assert twins_point[1]<m.rat(F(6,10**33))[0]
    inverse_sum=add(*(m.qmul(w,1/a) for w,a in zip(actual_weights,nodes)))
    tail_constant=add(*(m.qmul(abs_interval(w),1/(a*a*(1-a))+2/a**3) for w,a in zip(actual_weights,nodes)))
    result={'schema':'EM_DENSITY_CONSTANT_CALIBRATED_THICKNESS_V1','status':'PASS',
            'scope':'A new thirteen-thickness family; exact real coefficients solve density and complete-road-constant calibration while preserving the original eleven polynomial matching moments. Original fixed eleven-thickness road remains unchanged.',
            'arithmetic':'Exact rational Lagrange bases and 80-place outward integer intervals; EM24/N64 for zeta, zeta prime, Euler gamma and first Stieltjes constant; no floating decisions.',
            'dependencies':[{'path':str(p.relative_to(previous)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],
            'extra_nodes':list(map(str,extra)),'all_nodes':list(map(str,nodes)),
            'regular_constants':{'gamma':m.record(gamma),'gamma1':m.record(gamma1),**regular_bounds},
            'basis_moment_checks':moment_checks,'basis_weights':[list(map(str,b)) for b in bases],
            'basis_density_errors':list(map(m.record,density_errors)),'basis_road_constants':list(map(m.record,road_constants)),
            'calibration_determinant':m.record(determinant),'real_mixture_coefficients':list(map(m.record,lambdas)),
            'real_weights':list(map(m.record,actual_weights)),'real_weight_total_variation':m.record(tv),
            'shrinking_family':{'definition':'u=epsilon, v=epsilon/2; exact two-by-two calibration for all sufficiently small positive epsilon',
                                'first_new_node_density_derivative':m.record(r_d),'first_new_node_constant_derivative':m.record(r_c),
                                'boundary_determinant':m.record(boundary_determinant),
                                'coefficient_orders':['O(epsilon^2)','O(epsilon)','1+O(epsilon)']},
            'complete_window_matching':{'A':A,'B':B,'H_at_s1':list(map(str,H)),
                                        'combined_H_at_s1':m.record(combined_H),'ratio_to_original_s1_radius':m.record(ratio),
                                        'B_point_radius_upper':m.record(point_bound),'root_radius_upper_all_true_endpoint_grids':m.record(root_bound)},
            'complete_calibrated_tail':{'minimum_thickness':str(min(nodes)),
                                        'V_minus1':m.record(inverse_sum),'K':m.record(tail_constant),
                                        'bound':'|q_cal(y)-V_minus1| <= K*y^(1-minimum_thickness), all real y>=1; density and linear constant are exactly zero by algebraic calibration.'},
            'rational_approximation':{'coefficient_fraction_bits':precision,'mixture_coefficients':list(map(str,rational_lambdas)),
                                      'weights':list(map(str,rational_weights)),'exact_matching_moments':11,'total_variation':str(rational_tv),
                                      'maximum_weight_numerator_bits':max(abs(w.numerator).bit_length() for w in rational_weights),
                                      'maximum_weight_denominator_bits':max(w.denominator.bit_length() for w in rational_weights),
                                      'density_error':m.record(rational_density),'road_constant':m.record(rational_constant),
                                      'extra_B_point_radius':m.record(rounding_point),'extra_root_radius':m.record(rounding_root),
                                      'eventual_sign':floor_eventual,
                                      'scope':'Rational coefficient approximation has explicitly bounded nonzero density/constant errors; it is not claimed to have exact infinite-horizon calibration.'},
            'rational_ceiling_twin':{'mixture_coefficients':list(map(str,ceiling_lambdas)),
                                      'weights':list(map(str,ceiling_weights)),'exact_matching_moments':11,
                                      'maximum_weight_numerator_bits':max(abs(w.numerator).bit_length() for w in ceiling_weights),
                                      'maximum_weight_denominator_bits':max(w.denominator.bit_length() for w in ceiling_weights),
                                      'density_error':m.record(ceiling_density),'road_constant':m.record(ceiling_constant),
                                      'eventual_sign':ceiling_eventual},
            'rational_twins_complete_window_distance':{'point_radius_at_B':m.record(twins_point),
                                                        'root_radius_all_true_endpoint_grids':m.record(twins_root),
                                                        'scope':'All y<=B and arbitrary true-endpoint grids; both sources are separately defined on all integers.'},
            'node_certificates':rows}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','determinant':result['calibration_determinant'],
                      'coefficients':result['real_mixture_coefficients'],
                      'total_variation':result['real_weight_total_variation'],
                      'boundary_determinant':result['shrinking_family']['boundary_determinant'],
                      'finite_window':result['complete_window_matching'],
                      'rational_approximation':{k:v for k,v in result['rational_approximation'].items() if k not in ('weights','total_variation')}},ensure_ascii=False))


if __name__=='__main__':main()
