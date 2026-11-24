#!/usr/bin/env python3
"""Interpret previously saved exploratory values; no new prime/log evaluation."""
from pathlib import Path
from collections import defaultdict
import argparse,hashlib,json


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--prior',type=Path,required=True,
                        help='root of riemann_matching_isotonic_anchors_20261124')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('saved_paid_drift_comparison.json'))
    args=parser.parse_args()
    path=args.prior/'deficit/macroscopic_exploration.json'
    data=json.loads(path.read_text())
    grouped=defaultdict(dict)
    for row in data['rows']:
        grouped[(row['kind'],row['L'],row['x'],row['R'])][row['drift_exact']]=row
    rows=[]
    for packet,variants in grouped.items():
        raw=variants['0'];other=next(v for k,v in variants.items() if k!='0')
        a=raw['crossing_residual_root_with_drift'];b=other['crossing_residual_root_with_drift']
        rows.append({'kind':packet[0],'packet':list(packet[1:]),'drift_exact':other['drift_exact'],
                     'zero_drift_residual_root':a,'fully_paid_drift_residual_root':b,
                     'increase':b-a,'old_pool_width':raw['G'],'new_pool_width':other['G'],
                     'old_width_bound':raw['max_geometry_root_with_drift'],
                     'new_width_bound':other['max_geometry_root_with_drift'],
                     'actual_positive_root':raw['true_positive_root_budget']})
    result={'schema':'RH_SAVED_PAID_DRIFT_COMPARISON_V1',
            'status':'EXPLORATORY_DOUBLE_PRECISION_PREDECESSOR_REUSED',
            'certified':False,'new_prime_sieves':0,'new_logarithms':0,
            'predecessor_commit':'3aeecbec1c6f9bfa4d8998f4a39689ef5da0a970',
            'input_relative_path':'deficit/macroscopic_exploration.json',
            'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'packet_count':len(rows),'all_paid_residuals_nondecreasing_to_double_precision':all(r['increase']>=-1e-12 for r in rows),
            'strict_paid_increases':sum(r['increase']>1e-12 for r in rows),
            'width_bound_improvements':sum(r['new_width_bound']<r['old_width_bound'] for r in rows),
            'minimum_paid_increase':min(r['increase'] for r in rows),
            'maximum_paid_increase':max(r['increase'] for r in rows),
            'rows':rows,
            'scope':'Descriptive reanalysis of old doubles; strict monotonicity theorem uses exact analytic argument, not these data.'}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','packet_count','strict_paid_increases','width_bound_improvements','minimum_paid_increase','maximum_paid_increase']}))


if __name__=='__main__':main()
