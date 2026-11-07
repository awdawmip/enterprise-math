#!/usr/bin/env python3
"""Exact tuple equality checker for PREFIX-554 complete JSONL histograms.
Run PREFIX554_spool_and_batch_certificate.py at N=10 with all six modes first.
"""
import argparse, json
from pathlib import Path
from PREFIX553_batched_depth_stream_certificate import read_records,prepare

MODES=('cached','projected_spool','batch_2','batch_4','batch_5','batch_8')

def verify(folder):
    folder=Path(folder)
    reference=dict(read_records(folder/'cached.jsonl'))
    assert len(reference)==1056
    coefficients=sum(len(terms) for terms in reference.values())
    assert coefficients==187844
    for name in MODES[1:]:
        current=dict(read_records(folder/(name+'.jsonl')))
        assert current==reference,(name,'record or integer coefficient mismatch')
    ids,ph,sig,rows,roots=prepare()
    root_sets=[{ids[port] for port in roots[r]} for r in roots]
    assert len(root_sets)==12
    assert sum(len(c) for c in root_sets)==51
    assert set.union(*root_sets)==set(range(51))
    assert all(not root_sets[i].intersection(root_sets[j]) for i in range(12) for j in range(i+1,12))
    return {'status':'ALL_CHECKS_PASS','method':'Exact Python tuple and integer equality, not hash equality',
        'modes':MODES,'records_per_mode':len(reference),'nonzero_coefficients':coefficients,
        'partition_sizes':[len(v) for v in root_sets]}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--folder',default='p554_ref10');args=a.parse_args()
    print(json.dumps(verify(args.folder),ensure_ascii=False))
