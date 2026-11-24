#!/usr/bin/env python3
"""Outward interval certificate for the original fixed eleven-thickness family.

Euler--Maclaurin with an explicit Bernoulli remainder encloses zeta and its
derivative. No floating-point value participates in a certificate decision.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import argparse
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode=True


def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


def reciprocal(m,z):
    assert z[0]>0
    return m.S*m.S//z[1],m.ceildiv(m.S*m.S,z[0])


def exp_negative(m,helper,x):
    assert 0<=x[0]<=x[1]
    shift=0
    while x[1]>m.S:
        x=m.qmul(x,1,2);shift+=1
    value=helper.exp_negative_small(m,x)
    for _ in range(shift):value=m.square(value)
    return value


def zeta_em(m,helper,s,N=64,order=24):
    assert s>1 and N>=2 and order>=1
    bernoulli=m.bernoulli(2*order)
    val=der=m.ZERO
    for n in range(1,N):
        logn=m.log_int(n)
        term=exp_negative(m,helper,m.qmul(logn,s))
        val=m.add(val,term)
        der=m.sub(der,m.mul(term,logn))
    ln=m.log_int(N)
    power=exp_negative(m,helper,m.qmul(ln,s))
    tail=m.qmul(power,F(N)/(s-1))
    val=m.add(val,tail)
    der=m.sub(der,m.mul(tail,m.add(ln,m.rat(1/(s-1)))))
    half=m.qmul(power,1,2)
    val=m.add(val,half);der=m.sub(der,m.mul(half,ln))
    rising=F(1);harmonic=F(0)
    terms=[]
    for k in range(1,2*order):
        rising*=s+k-1;harmonic+=1/(s+k-1)
        if k%2:
            j=(k+1)//2
            coefficient=bernoulli[2*j]*rising/F(factorial(2*j)*N**(2*j-1))
            term=m.qmul(power,coefficient)
            val=m.add(val,term)
            der=m.add(der,m.mul(term,m.sub(m.rat(harmonic),ln)))
            terms.append(term)
    # |B_(2M)({t})| <= |B_(2M)|.  Integration of |f^(2M)|
    # gives exactly the absolute value of the last displayed EM term.
    remainder=max(abs(terms[-1][0]),abs(terms[-1][1]))
    full_harmonic=harmonic+1/(s+2*order-1)
    derivative_factor=m.add(ln,m.rat(full_harmonic+1/(s+2*order-1)))
    derivative_remainder=m.mul((remainder,remainder),derivative_factor)[1]
    z=(val[0]-remainder,val[1]+remainder)
    dz=(der[0]-derivative_remainder,der[1]+derivative_remainder)
    assert z[0]>0 and dz[1]<0
    return z,dz,{'N':N,'order':order,'zeta_remainder_upper':m.record((remainder,remainder)),
                 'derivative_remainder_upper':m.record((derivative_remainder,derivative_remainder))}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True,
                        help='riemann_native_residual_growth_20261124 package')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('fixed_family_density_certificate.json'))
    args=parser.parse_args()
    old=args.previous/'prior/riemann_matching_isotonic_anchors_20261124'
    earlier=old/'prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123'
    helper_path=old/'matching/verify_actual_matching.py'
    interval_path=earlier/'dependencies/certify_fast_harmonic_energy.py'
    input_path=earlier/'prefix_compute/fixed_matched_family.json'
    m=module_at('fixed_density_intervals',interval_path)
    helper=module_at('fixed_density_exp',helper_path)
    data=json.loads(input_path.read_text())
    nodes=list(map(F,data['nodes']));weights=list(map(F,data['weights']))
    assert len(nodes)==len(weights)==11 and all(0<a<=F(1,2) for a in nodes)
    assert [sum((v*a**k for a,v in zip(nodes,weights)),F(0)) for k in range(11)]==[F(1)]+[F(0)]*10
    gamma=(m.rat(F(data['gamma']['lower']))[0],m.rat(F(data['gamma']['upper']))[1])
    density=constant=m.ZERO;rows=[]
    for a,v in zip(nodes,weights):
        z,dz,bounds=zeta_em(m,helper,1+a)
        g=reciprocal(m,z)
        gp=m.neg(m.mul(dz,m.square(g)))
        d=m.qmul(g,1/a)
        c=m.add(m.add(m.ONE,gamma),m.add(m.mul(m.sub(gamma,m.ONE),d),m.qmul(m.sub(gp,m.ONE),1/a)))
        density=m.add(density,m.qmul(d,v));constant=m.add(constant,m.qmul(c,v))
        rows.append({'a':str(a),'weight':str(v),'zeta':m.record(z),'zeta_prime':m.record(dz),
                     'mean_density':m.record(d),'road_constant':m.record(c),**bounds})
    difference=m.sub(density,m.ONE)
    assert difference[1]<0 and constant[0]>0
    minimum=min(nodes)
    inverse_sum=sum((v/a for a,v in zip(nodes,weights)),F(0))
    K=sum((abs(v)*(1/(a*a*(1-a))+2/a**3) for a,v in zip(nodes,weights)),F(0))
    exponent=20000
    log_y=m.qmul(m.LOG_TWO,exponent)
    decay=exp_negative(m,helper,m.qmul(log_y,minimum))
    inverse_tail=m.rat(abs(inverse_sum)/2**exponent)
    upper=m.add(m.add(m.mul(difference,log_y),constant),m.add(inverse_tail,m.qmul(decay,K)))
    assert upper[1]<0
    # Independent integral comparison is a coarse, rigorously valid check
    # of every EM enclosure, including the pole-near smallest parameter.
    coarse_checks=0
    for row,a in zip(rows,nodes):
        s=1+a;partial=m.ZERO
        for n in range(1,64):partial=m.add(partial,exp_negative(m,helper,m.qmul(m.log_int(n),s)))
        lower=m.add(partial,m.qmul(exp_negative(m,helper,m.qmul(m.log_int(64),a)),1/a))
        upper_coarse=m.add(partial,m.qmul(exp_negative(m,helper,m.qmul(m.log_int(63),a)),1/a))
        z=m.decode(row['zeta'])
        assert lower[0]<=z[0]<=z[1]<=upper_coarse[1]
        coarse_checks+=1
    result={'schema':'EM_FIXED_ELEVEN_MEAN_DENSITY_V1','status':'PASS',
            'scope':'Original fixed eleven rational thicknesses and weights, kept fixed for all source integers; eventual sign proved using an explicit elementary complete-road remainder.',
            'arithmetic':'Exact fractions and 80-digit outward integer intervals; Euler--Maclaurin24 at N64; scaled Taylor100/101 exponentials; no floating certificate decisions.',
            'dependencies':[{'path':str(p.relative_to(args.previous)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (input_path,interval_path,helper_path)],
            'matching_moments_checked':11,'zeta_enclosures':11,'zeta_derivative_enclosures':11,
            'independent_integral_comparison_checks':coarse_checks,'parameters':rows,
            'density_minus_one':m.record(difference),'road_constant':m.record(constant),
            'minimum_thickness':str(minimum),'signed_inverse_thickness_sum':str(inverse_sum),
            'elementary_tail_constant_exact':str(K),
            'eventual_negativity':{'threshold':'2^20000','threshold_exponent_base2':exponent,
               'log_threshold':m.record(log_y),'tail_power_bound':m.record(decay),
               'road_over_y_upper_expression':m.record(upper),
               'conclusion':'q_fixed(y)<0 for every real y>=2^20000. The decreasing elementary upper bound is negative at the threshold; this is a sufficient threshold, not a first sign-change claim.'}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','density_minus_one':result['density_minus_one'],
                      'road_constant':result['road_constant'],'negative_after':result['eventual_negativity']},ensure_ascii=False))


if __name__=='__main__':main()
