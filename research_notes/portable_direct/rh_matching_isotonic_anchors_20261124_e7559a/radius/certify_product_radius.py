#!/usr/bin/env python3
"""Refine saved actual-road intervals using a rational Laplace product bound."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial, prod
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


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--prior',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('product_radius_certificate.json'))
    args=parser.parse_args()
    base=args.prior / 'prior/riemann_cumulative_haar_20261123'
    paths={'harmonic':base/'dependencies/certify_fast_harmonic_energy.py',
           'oracle':base/'prefix_compute/certify_paired_prefix.py',
           'family':base/'prefix_compute/fixed_matched_family.json',
           'previous':args.prior/'matching_transfer/matching_kernel_certificate.json',
           'samples':base/'inputs/rh_partial_frontier_20261122/sparse_sample_observations.json'}
    m=module_at('harmonic_product_radius',paths['harmonic'])
    old=module_at('paired_prefix_product_radius',paths['oracle'])
    family=json.loads(paths['family'].read_text())
    previous=json.loads(paths['previous'].read_text())
    assert previous['samples_denominator_power_of_10']==m.DIGITS
    nodes=[row['n'] for row in previous['samples']]
    h=prod(a/(1+a) for a in map(F,family['nodes']))
    zeta_upper=sum((F(1,n*n) for n in range(1,257)),F(0))+F(1,256)
    e_lower=sum((F(1,factorial(n)) for n in range(25)),F(0))
    coefficient=h*zeta_upper/(2*e_lower)
    errors={};lower={};upper={};reference={};changed=[];records=[]
    for row in previous['samples']:
        n=row['n'];old_radius=int(row['new_error_radius'])
        raw=coefficient*n*n*m.S
        radius=-((-raw.numerator)//raw.denominator)
        radius=min(radius,old_radius)
        if radius<old_radius:changed.append(n)
        reference[n]=tuple(map(int,row['reference']))
        errors[n]=(radius,radius)
        lower[n]=(reference[n][0]-radius,)*2
        upper[n]=(reference[n][1]+radius,)*2
        assert int(row['lower'])<=lower[n][0]<=upper[n][0]<=int(row['upper'])
        records.append({'n':n,'reference':list(map(str,reference[n])),
                        'radius':str(radius),'lower':str(lower[n][0]),'upper':str(upper[n][0])})
    # Retain the generation-before-comparison order of the prior oracle.
    observations=json.loads(paths['samples'].read_text())
    actual={r['n']:m.decode(r['value']) for r in observations['samples']}
    assert all(lower[n][0]<=actual[n][0]<=actual[n][1]<=upper[n][1] for n in nodes)
    curvature=F(previous['source_curvature_constants_unchanged']['upper'])
    energy_upper,_=m.evaluate_partition(nodes,upper,curvature)
    energy_lower,_=m.evaluate_partition(nodes,lower,F(-12))
    radius_energy=old.linear_error_energy(m,nodes,errors)
    assert energy_lower[0]>=m.decode(previous['lower_positive_energy'])[0]
    assert energy_upper[1]<=m.decode(previous['upper_positive_energy'])[1]
    result={'schema':'RH_PRODUCT_RADIUS_REFINEMENT_V1','status':'PASS',
            'scope':'Same fixed eleven-thickness road and 1270 saved reference intervals; author interval certificate.',
            'window':[nodes[0],nodes[-1]],'node_count':len(nodes),'strictly_improved_radius_count':len(changed),
            'first_improved_node':min(changed),'last_improved_node':max(changed),
            'all_intervals_nested_in_previous':True,'all_historical_actual_intervals_contained':True,
            'proof_constants':{'laplace_parameter':'1','H_exact':str(h),'zeta2_upper':str(zeta_upper),
                               'zeta_upper_method':'sum n=1..256 of 1/n^2 plus integral_256^infinity t^-2 dt',
                               'e_lower':str(e_lower),'e_lower_method':'sum j=0..24 of 1/j!',
                               'point_radius_coefficient':str(coefficient)},
            'radius_at_B':m.record(errors[nodes[-1]]),'previous_radius_at_B':previous['radius_at_B'],
            'lower_positive_energy':m.record(energy_lower),'upper_positive_energy':m.record(energy_upper),
            'interpolated_radius_square_energy':m.record(radius_energy),
            'unchanged_curvature_constants':previous['source_curvature_constants_unchanged'],
            'incremental_point_generation':{'new_prime_sieve':False,'new_logarithms':0,'thickness_exponentials':0,
                                          'exact_rational_product_factors':len(family['nodes']),
                                          'prior_reference_intervals_reused':len(nodes)},
            'input_files':[{'role':key,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()} for key,path in paths.items()],
            'decimal_digits':m.DIGITS,'samples':records}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','node_count','strictly_improved_radius_count','first_improved_node','radius_at_B','lower_positive_energy','upper_positive_energy','interpolated_radius_square_energy']},ensure_ascii=False))


if __name__=='__main__':
    main()
